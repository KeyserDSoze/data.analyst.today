## 11.12 Data quality tests: trasformare il contratto in invarianti eseguibili

Ogni modello analitico contiene assunzioni. Nel Capitolo 3 le abbiamo valutate durante la Data Readiness Review; qui facciamo un passo diverso: **quando un’assunzione deve continuare a essere vera a ogni refresh, diventa un test del prodotto dati**.

Se l’Analytical Data Contract dichiara:

```text
grain: una riga per order_id
status domain: created|paid|shipped|delivered|cancelled
customer_sk: obbligatorio per ordini identificati
freshness: entro 07:30
net_revenue: riconciliabile con Finance entro tolleranza
```

ha già specificato gran parte dei controlli necessari.

I test strutturali verificano proprietà locali come unicità, not-null, accepted values e referential integrity. Per esempio, se il grain è una riga per ordine:

```sql
SELECT order_id
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Il risultato atteso è zero righe. Ma una tabella unica e completa sul piano sintattico può comunque essere semanticamente rotta.

### BlueBasket: il record di conversione creato dal denominatore

BlueBasket vede la conversione passare dal **3,7% al 5,1%** in un giorno. Gli ordini sono quasi invariati; le sessioni diminuiscono del 27%. Un nuovo consent banner ha ridotto il tracking delle visite anonime mentre gli acquisti finali continuano a essere registrati.

Il numeratore è quasi intatto; il denominatore è incompleto. Un semplice controllo di volume avrebbe potuto segnalare:

```text
sessions_today < 0.85 × median_sessions_same_weekday_last_8_weeks
```

prima che il KPI venisse interpretato come miglioramento di prodotto.

Per questo i test devono coprire anche popolazione e comportamento: volume, freshness, completezza, range, nuove categorie, continuità temporale, join coverage e row multiplier. Non stanno cercando soltanto valori “invalidi”; stanno verificando che il processo stia ancora producendo la popolazione e il grain promessi.

### Semantic checks: quando tutti i campi sono validi ma il significato cambia

`net_revenue` può essere non-null, positivo, nel range storico e puntuale, ma cambiare comunque definizione, per esempio includendo l’IVA da oggi quando ieri la escludeva. Quasi tutti i test locali passerebbero.

Servono quindi invarianti che mettano in relazione sistemi o componenti:

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

entro tolleranze dichiarate. La qualità analitica non coincide con la validità delle singole colonne: comprende la conservazione delle relazioni che danno significato alla metrica.

### Severity: il test deve sapere che cosa autorizza

Non tutti i failure mode hanno lo stesso rischio. Una policy utile distingue **BLOCK**, quando il dataset non deve essere pubblicato; **WARN**, quando può essere pubblicato in stato degradato con investigazione obbligatoria; **MONITOR**, quando la deviazione viene registrata ma non blocca automaticamente.

| Invariante | Severity |
|---|---|
| duplicato su chiave primaria analitica | BLOCK |
| foreign key mancanti > 0,5% | BLOCK |
| freshness +20 minuti rispetto a SLA | WARN |
| mix geografico fuori range storico | MONITOR |

La severity dovrebbe derivare dal rischio decisionale, non dalla facilità con cui abbiamo scritto il test.

### Testare anche i confini tra trasformazioni

Una pipeline può produrre un totale finale plausibile pur compensando due errori opposti. Per questo è utile osservare i passaggi:

```text
raw_orders
→ deduped_orders        [uniqueness, removed value]
→ valid_orders          [population, exclusions]
→ enriched_orders       [join coverage, row multiplier]
→ daily_metrics         [reconciliation, denominators]
```

Ogni step dovrebbe lasciare traccia di ciò che ha cambiato. Un test verifica una condizione prevista; l’osservabilità, che tornerà nel Capitolo 18, aiuterà invece a investigare comportamenti non previsti. Qui basta una regola: se un’assunzione è necessaria affinché la metrica mantenga significato e possiamo verificarla automaticamente, deve diventare un invariant.

### Quality invariant nel contract

```text
invariant:
metric/query used to test it:
expected condition:
tolerance:
severity:
owner:
what happens on failure:
```

> **Un modello affidabile non chiede ai consumer di ricordare tutte le sue assunzioni. Le rende eseguibili e fallisce in modo visibile quando smettono di essere vere.**
