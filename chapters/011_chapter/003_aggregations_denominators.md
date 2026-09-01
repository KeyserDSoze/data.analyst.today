## 11.2 Aggregare significa scegliere una popolazione, un peso e un denominatore

`GROUP BY` sembra un’operazione tecnica. In realtà ogni aggregazione incorpora una decisione semantica.

Quando calcoliamo una metrica, dovremmo poter rispondere a quattro domande:

1. **che cosa sto sommando o contando?**
2. **qual è la popolazione eleggibile?**
3. **qual è il denominatore?**
4. **quale peso implicito assegno alle osservazioni?**

Se una di queste risposte è ambigua, la metrica può cambiare senza che cambi la formula.

### Caso simulato/composito — NovaCare e il miglioramento che nasceva dai `NULL`

NovaCare gestisce un customer service multicanale.

Il report mensile mostra:

- tempo medio di prima risposta: 4,8 ore;
- mese precedente: 5,6 ore;
- miglioramento apparente: 14%.

La query è semplice:

```sql
SELECT
    AVG(first_response_minutes) / 60.0 AS avg_hours
FROM tickets
WHERE created_at >= DATE '2026-07-01'
  AND created_at <  DATE '2026-08-01';
```

Nel mese corrente, però, è cambiata la pipeline: i ticket ancora aperti senza risposta hanno `first_response_minutes = NULL`.

`AVG` ignora i `NULL`.

Quindi i ticket peggiori — quelli che non hanno ancora ricevuto alcuna risposta — spariscono dalla popolazione osservata.

La sintassi non contiene errori. È cambiato il significato del denominatore.

### Popolazione eleggibile e popolazione osservata

Molte metriche diventano più robuste se distinguiamo esplicitamente:

- **eligible population** — casi che dovrebbero poter entrare nel calcolo;
- **observed population** — casi per cui abbiamo effettivamente un valore;
- **excluded population** — casi eliminati secondo una regola dichiarata.

Nel caso NovaCare potremmo produrre insieme:

- numero totale di ticket eleggibili;
- numero di ticket già risposti;
- numero ancora senza risposta;
- media sui ticket risposti;
- percentile o SLA breach sul totale, con una policy esplicita per i censored/open cases.

Il problema non è che `AVG` ignori i `NULL`. Il problema è dimenticare che lo fa.

### Conteggi diversi rispondono a domande diverse

```sql
COUNT(*)
```

conta righe.

```sql
COUNT(customer_id)
```

conta righe in cui `customer_id` non è `NULL`.

```sql
COUNT(DISTINCT customer_id)
```

conta identità cliente distinte non nulle.

Se una tabella contiene più righe per cliente, questi tre numeri non sono versioni alternative della stessa metrica. Rappresentano entità differenti.

### La media delle medie nasconde il peso

Consideriamo due negozi:

| Negozio | Ordini | AOV |
|---|---:|---:|
| A | 100 | €40 |
| B | 10.000 | €52 |

Fare `(40 + 52) / 2` produce €46.

Ma ogni negozio riceve così lo stesso peso, non ogni ordine.

L’AOV complessivo è invece:

```text
(100 × 40 + 10.000 × 52) / 10.100 ≈ 51,88 euro
```

La domanda da fare non è “media o media ponderata?”. È:

> **qual è l’unità che deve avere peso uno nella metrica finale?**

### Ratio of sums vs average of ratios

Per un return rate possiamo scrivere:

```sql
SUM(returned_units) * 1.0 / SUM(sold_units)
```

oppure:

```sql
AVG(returned_units * 1.0 / NULLIF(sold_units, 0))
```

Non sono equivalenti.

La prima formula assegna peso alle unità vendute. La seconda assegna peso alle righe o ai gruppi su cui stiamo facendo la media.

Per questo nell’Analytical Data Contract una ratio dovrebbe dichiarare almeno:

- numeratore;
- denominatore;
- unità di ponderazione;
- esclusioni;
- gestione dei denominatori zero;
- livello al quale numeratore e denominatore devono essere aggregati prima della divisione.

### Metriche additive, semi-additive e non additive

Una classificazione operativa utile è:

- **additive**: revenue, units, costi; possono essere sommate attraverso molte dimensioni;
- **semi-additive**: inventory, balance, headcount snapshot; possono essere aggregate su alcune dimensioni ma non liberamente nel tempo;
- **non additive**: percentuali, medie, ratio, score; spesso devono essere ricalcolate dai componenti.

Un saldo giornaliero di 10, 12 e 9 unità non implica uno stock di 31 unità. Abbiamo tre stati in tre momenti, non tre flussi.

### Caso simulato/composito — PeakSports e il seller “peggiore”

Un marketplace misura i resi.

Seller Alpha:

- 8 resi;
- 100 ordini;
- return rate 8%.

Seller Beta:

- 240 resi;
- 6.000 ordini;
- return rate 4%.

Se osserviamo i resi assoluti, Beta domina il volume.

Se osserviamo il tasso, Alpha è peggiore.

Ma Alpha vende quasi solo scarponi da sci, categoria con baseline di reso 12%.

Il confronto corretto può quindi richiedere un’ulteriore normalizzazione per category mix.

Questo esempio mostra una sequenza importante:

```text
conteggio
→ tasso
→ denominatore
→ composizione
→ confronto appropriato
```

L’aggregazione non è il punto finale del ragionamento. È una scelta di rappresentazione.

### Conservare componenti, non soltanto percentuali

Invece di materializzare soltanto:

```text
conversion_rate = 3,7%
```

è spesso preferibile conservare:

- `converted_sessions`;
- `eligible_sessions`.

Poi:

```text
conversion_rate = converted_sessions / eligible_sessions
```

può essere ricalcolato coerentemente per canale, Paese, settimana o prodotto.

Lo stesso principio vale per:

- margin %;
- return rate;
- attach rate;
- activation rate;
- churn rate;
- on-time delivery rate.

> **Una percentuale è spesso un risultato. Numeratore, denominatore e popolazione sono il vero contratto analitico.**
