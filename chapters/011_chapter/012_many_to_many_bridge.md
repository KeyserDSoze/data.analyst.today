## 11.11 Many-to-many e bridge tables: quando una relazione richiede una regola di allocazione

Molte relazioni di business sono naturalmente many-to-many: un ordine può usare più promozioni, un cliente appartenere a più segmenti, un contratto coinvolgere più account manager. Il problema nasce quando una misura attraversa quella relazione e ogni associazione riceve implicitamente l’intero valore della fact.

### UrbanPeak: revenue attribuita maggiore della revenue reale

UrbanPeak vuole analizzare il fatturato associato ai touchpoint marketing. Un ordine vale €100 ed è collegato a Paid Search, Email e Retargeting. Una query diretta:

```sql
SELECT
    campaign,
    SUM(revenue)
FROM orders
JOIN order_touchpoints USING(order_id)
GROUP BY 1;
```

attribuisce €100 a ciascuna campagna. Il totale “attribuito” diventa €300. A scala mensile il dashboard può arrivare a **€5,7M di revenue attribuita contro €3,2M di revenue effettiva** senza alcun errore di sintassi.

Il join rappresenta correttamente la relazione; manca la policy con cui una misura deve attraversarla.

Una bridge può rendere questa scelta esplicita:

```text
bridge_order_campaign
order_id | campaign_id | allocation_weight
O1       | C10         | 0.50
O1       | C22         | 0.30
O1       | C35         | 0.20
```

La misura allocata diventa:

```sql
SUM(order_revenue * allocation_weight)
```

con un invariante verificabile:

```text
per ogni order_id, SUM(allocation_weight) = 1
```

Il peso, però, non viene scoperto dalla bridge. È una decisione business: equal split, first touch, last touch, position based, quota contrattuale, tempo dedicato o altra policy. In alcuni casi non serve allocare nulla: se la domanda è “quali coupon compaiono negli ordini ad alto valore?”, la bridge descrive soltanto una relazione. Se chiediamo “quanta revenue attribuiamo a ciascun coupon?”, dobbiamo introdurre una regola economica.

### Fact-to-fact: la moltiplicazione può essere ancora meno visibile

Supponiamo di avere `fact_orders` a una riga per ordine e `fact_support_tickets` a una riga per ticket. Un account con 8 ordini e 5 ticket può produrre 40 righe se le fact vengono unite direttamente per `account_id`. Revenue viene ripetuta per ticket e ticket per ordine; qualsiasi correlazione viene implicitamente pesata dalla molteplicità.

Se la domanda vive a livello account-periodo, è spesso più coerente costruire prima:

```sql
WITH orders_by_account AS (...),
tickets_by_account AS (...)
SELECT ...
FROM orders_by_account o
JOIN tickets_by_account t
  ON o.account_id = t.account_id;
```

Il principio non è “aggregare sempre prima”, ma **portare le misure allo stesso grain analitico prima di confrontarle**.

Un SaaS B2B può altrimenti osservare una relazione fortissima tra ticket e revenue soltanto perché gli account con molti ordini e molti ticket producono decine di righe. Dopo aver ricostruito una riga per account-periodo, la relazione può ridursi drasticamente. Il problema non era statistico: era il peso introdotto dal join.

### Relationship semantics nell’Analytical Data Contract

```text
left grain:
right grain:
relationship grain:
bridge key:
allocation required? sì/no
allocation rule:
weight invariant:
unallocated cases:
expected row multiplier:
```

Questa specifica permette di testare se i pesi sommano a uno, se esistono associazioni orfane, se il row multiplier è quello atteso e se il totale allocato si riconcilia con il totale originale.

> **Una many-to-many non è una relazione da eliminare. È una relazione che obbliga a distinguere tra “essere associati” e “ricevere una quota del valore”.**
