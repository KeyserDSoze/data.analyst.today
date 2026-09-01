## 11.12 Data quality tests: trasformare il contratto in invarianti eseguibili

Ogni modello analitico contiene assunzioni.

Nel Capitolo 3 abbiamo imparato a valutarle durante una Data Readiness Review. Qui facciamo un passo diverso: **le assunzioni che devono restare vere nel tempo diventano controlli automatici del modello**.

Se l'Analytical Data Contract dichiara:

```text
grain: una riga per order_id
status domain: created|paid|shipped|delivered|cancelled
customer_sk: obbligatorio per ordini identificati
freshness: entro 07:30
net_revenue: riconciliabile con Finance entro tolleranza
```

allora abbiamo già quasi scritto la specifica dei test.

### Test strutturali

#### Unicità

Se il grain è una riga per ordine:

```sql
SELECT order_id
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Il risultato atteso è zero righe.

#### Not null

```sql
SELECT COUNT(*)
FROM fact_orders
WHERE order_id IS NULL;
```

#### Accepted values

```sql
SELECT DISTINCT status
FROM fact_orders
WHERE status NOT IN (
    'created', 'paid', 'shipped', 'delivered', 'cancelled'
);
```

#### Referential integrity

```sql
SELECT COUNT(*)
FROM fact_orders f
LEFT JOIN dim_customer d
  ON f.customer_sk = d.customer_sk
WHERE f.customer_sk IS NOT NULL
  AND d.customer_sk IS NULL;
```

Questi test verificano proprietà locali del dataset.

### Test di popolazione e comportamento

Molti failure mode non rompono nessuna chiave.

Esempi:

- ordini giornalieri -63%;
- `country` null rate da 0,4% a 18%;
- una sorgente smette di arrivare;
- revenue raddoppia in un'ora;
- lateness passa da 20 minuti a 7 ore;
- una categoria nuova compare improvvisamente sul 35% dei record.

Servono quindi controlli su:

- volume;
- freshness;
- completezza;
- distribuzioni;
- range;
- nuove categorie;
- continuità temporale;
- row multiplier dopo join critiche.

### Caso simulato/composito — BlueBasket e il record di conversione

BlueBasket vede la conversione passare dal 3,7% al 5,1% in un giorno.

Gli ordini sono quasi invariati. Le sessioni sono diminuite del 27%.

Un nuovo consent banner ha ridotto il tracking delle visite anonime, mentre gli acquisti finali continuano a essere registrati.

Il numeratore è quasi intatto. Il denominatore è incompleto.

Un semplice controllo avrebbe potuto segnalare:

```text
sessions_today < 0.85 × median_sessions_same_weekday_last_8_weeks
```

prima che il KPI venisse presentato come miglioramento di prodotto.

### Semantic checks: quando i valori sono validi ma il significato cambia

Supponiamo che `net_revenue` sia sempre:

- non-null;
- positivo;
- nel range storico;
- aggiornato in tempo.

Se da oggi include l'IVA mentre ieri la escludeva, quasi tutti i test tecnici possono passare.

Per questo alcuni invarianti devono verificare **relazioni tra sistemi o componenti semantici**.

Esempio:

```text
warehouse recognized revenue
vs
finance ledger
```

oppure:

```text
gross_revenue
- discounts
- refunds
= net_revenue
```

entro tolleranze dichiarate.

La qualità analitica non coincide con la validità dei singoli campi.

### Severity e comportamento del sistema

Non tutti i test devono avere lo stesso effetto.

Una policy utile distingue:

- **BLOCK**: il dataset non viene pubblicato;
- **WARN**: viene pubblicato con stato degradato e investigazione obbligatoria;
- **MONITOR**: deviazione registrata, nessun blocco automatico.

Per esempio:

| Invariante | Severity |
|---|---|
| duplicato su chiave primaria analitica | BLOCK |
| foreign key mancanti > 0,5% | BLOCK |
| freshness +20 minuti rispetto a SLA | WARN |
| mix geografico fuori range storico | MONITOR |

La severity dovrebbe riflettere il rischio decisionale, non la facilità tecnica del test.

### Non testare solo il risultato finale

Una pipeline di cinque trasformazioni può produrre un totale plausibile pur avendo compensato due errori opposti.

Per questo i controlli più utili vivono anche sui confini tra step:

```text
raw_orders
→ deduped_orders        [uniqueness, removed value]
→ valid_orders          [population, exclusions]
→ enriched_orders       [join coverage, row multiplier]
→ daily_metrics         [reconciliation, denominators]
```

Ogni trasformazione dovrebbe lasciare traccia di ciò che ha cambiato.

### Test e osservabilità non sono la stessa cosa

Un test verifica una condizione prevista.

L'osservabilità, che approfondiremo nel Capitolo 18, aiuta a capire comportamenti imprevisti e dipendenze del sistema.

Qui il principio è più semplice:

> **se un'assunzione è necessaria affinché la metrica conservi significato, e possiamo verificarla automaticamente, deve diventare un invariante del modello.**

### Campo del contract: quality invariants

L'Analytical Data Contract dovrebbe contenere almeno:

```text
invariant:
metric/query used to test it:
expected condition:
tolerance:
severity:
owner:
what happens on failure:
```

A quel punto la frase “questa tabella dovrebbe essere una riga per ordine” non è più documentazione passiva.

È una proprietà che la pipeline dimostra a ogni esecuzione.

> **Un modello affidabile non chiede agli utenti di ricordare tutte le sue assunzioni. Le rende eseguibili e fallisce in modo visibile quando smettono di essere vere.**
