## 11.2 Aggregare significa scegliere una popolazione, un peso e un denominatore

Dopo aver fissato il grain, l’aggregazione decide **chi pesa quanto** nel numero finale. `GROUP BY`, `AVG` e `COUNT` sembrano operatori tecnici, ma ogni loro uso incorpora almeno quattro scelte: che cosa stiamo misurando, quale popolazione è eleggibile, quale denominatore usiamo e quale unità riceve peso uno.

### NovaCare: il miglioramento creato dai `NULL`

NovaCare gestisce un customer service multicanale. Il report mensile mostra un tempo medio di prima risposta di 4,8 ore, contro 5,6 nel mese precedente: un miglioramento apparente del 14%.

```sql
SELECT
    AVG(first_response_minutes) / 60.0 AS avg_hours
FROM tickets
WHERE created_at >= DATE '2026-07-01'
  AND created_at <  DATE '2026-08-01';
```

Nel mese corrente è però cambiata la pipeline: i ticket ancora aperti senza risposta hanno `first_response_minutes = NULL`. Poiché `AVG` ignora i `NULL`, proprio i casi peggiori scompaiono dal denominatore osservato.

La distinzione utile è quindi tra **eligible population**, cioè i casi che dovrebbero poter entrare nella metrica, **observed population**, i casi per cui abbiamo un valore, ed **excluded population**, quelli rimossi per una regola dichiarata. Nel caso NovaCare non basta riportare la media sui ticket risposti: servono anche il numero totale eleggibile, quanti ticket sono ancora senza risposta e una policy esplicita per open/censored cases.

Lo stesso principio vale per i conteggi. `COUNT(*)`, `COUNT(customer_id)` e `COUNT(DISTINCT customer_id)` non sono varianti stilistiche della stessa metrica: contano rispettivamente righe, valori non nulli e identità distinte. Se il grain non è uno per cliente, le tre risposte rappresentano fenomeni differenti.

### Il peso è spesso nascosto nella formula

Consideriamo due negozi:

| Negozio | Ordini | AOV |
|---|---:|---:|
| A | 100 | €40 |
| B | 10.000 | €52 |

La media semplice degli AOV, `(40 + 52) / 2 = 46`, assegna peso uno a ciascun negozio. Se vogliamo che ogni ordine pesi uno, l’AOV complessivo è invece:

```text
(100 × 40 + 10.000 × 52) / 10.100 ≈ 51,88 euro
```

La domanda non è “media o media ponderata?”. È: **qual è l’unità che deve avere peso uno?**

La stessa differenza compare tra ratio of sums e average of ratios:

```sql
SUM(returned_units) * 1.0 / SUM(sold_units)
```

non equivale a:

```sql
AVG(returned_units * 1.0 / NULLIF(sold_units, 0))
```

La prima assegna peso alle unità vendute; la seconda alle righe o ai gruppi. Una ratio matura dovrebbe quindi dichiarare numeratore, denominatore, unità di ponderazione, esclusioni, gestione degli zeri e livello al quale i componenti devono essere aggregati prima della divisione.

### Additività: distinguere flussi, stati e risultati

Revenue, units e costi sono spesso **additive**. Inventory, balance e headcount snapshot sono invece **semi-additive**: possono essere sommati su alcune dimensioni ma non liberamente nel tempo. Percentuali, medie, ratio e score sono in genere **non additive** e vanno ricalcolati dai componenti.

Uno stock giornaliero di 10, 12 e 9 unità non implica uno stock di 31: sono tre stati in tre momenti, non tre flussi. Per questo conservare soltanto la percentuale finale è spesso una scelta fragile. È più robusto materializzare i componenti:

```text
converted_sessions
eligible_sessions
```

per poi derivare:

```text
conversion_rate = converted_sessions / eligible_sessions
```

Lo stesso vale per margin %, return rate, attach rate, activation rate, churn rate e on-time delivery rate.

### PeakSports: il seller “peggiore” dipende dalla rappresentazione

Seller Alpha ha 8 resi su 100 ordini, return rate 8%. Seller Beta ha 240 resi su 6.000 ordini, return rate 4%. In volume assoluto Beta domina; in tasso Alpha è peggiore. Ma Alpha vende quasi solo scarponi da sci, categoria con baseline di reso 12%.

Il ragionamento corretto si muove quindi attraverso più rappresentazioni:

```text
conteggio
→ tasso
→ denominatore
→ composizione
→ confronto appropriato
```

L’aggregazione non chiude l’analisi. Decide quale informazione comprimiamo e quale peso assegniamo alla realtà.

> **Una percentuale è il risultato finale di un contratto. Numeratore, denominatore, popolazione e peso sono il contratto vero.**
