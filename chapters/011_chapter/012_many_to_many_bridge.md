## 11.11 Many-to-many e bridge tables: quando una relazione richiede una regola di allocazione

Molte relazioni di business non sono one-to-many.

Un ordine può usare più promozioni. Un cliente può appartenere a più segmenti. Un medico può lavorare in più strutture. Un contratto può coinvolgere più account manager. Un prodotto può comparire in più collezioni.

Il problema non è che la relazione sia many-to-many. Il problema nasce quando la trattiamo come se ogni associazione potesse ricevere l'intero valore della fact.

### Caso simulato/composito — UrbanPeak e la revenue attribuita che supera la revenue reale

UrbanPeak vuole analizzare il fatturato associato ai touchpoint marketing.

Ha:

```text
orders
order_id | revenue
O1       | 100
```

E:

```text
order_touchpoints
order_id | campaign
O1       | Paid Search
O1       | Email
O1       | Retargeting
```

Una query ingenua:

```sql
SELECT
    campaign,
    SUM(revenue)
FROM orders
JOIN order_touchpoints USING(order_id)
GROUP BY 1;
```

attribuisce €100 a ogni campagna.

Il totale attribuito diventa €300 per un ordine che vale €100.

A scala mensile, una dashboard potrebbe mostrare €5,7M di revenue attribuita contro €3,2M di revenue effettiva.

La join condition è valida. È il **modello di allocazione** a non essere definito.

### La bridge table rende esplicita la relazione

Una bridge può contenere:

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

Ma anche questo non risolve automaticamente il problema analitico.

### Il peso è una scelta di business

Possibili policy:

- equal split;
- first touch;
- last touch;
- position based;
- quota contrattuale;
- tempo dedicato;
- superficie occupata;
- nessuna allocazione, se vogliamo soltanto rappresentare la relazione.

La bridge table non scopre quale sia la policy corretta. Fa una cosa più importante: **impedisce che la policy resti implicita nel join**.

### Relazione e allocazione non sono la stessa cosa

Supponiamo che un ordine abbia tre coupon applicati.

Potremmo voler sapere:

> quali coupon compaiono negli ordini ad alto valore?

In questo caso può bastare la relazione many-to-many, senza dividere la revenue.

Se invece chiediamo:

> quanta revenue attribuiamo a ciascun coupon?

serve una regola di allocazione.

Sono domande diverse.

### Fact-to-fact join: il moltiplicatore più facile da ignorare

Abbiamo:

- `fact_orders`: una riga per ordine;
- `fact_support_tickets`: una riga per ticket.

Un account ha 8 ordini e 5 ticket.

Un join diretto per `account_id` può produrre 40 righe.

A quel punto:

- revenue viene ripetuta per ogni ticket;
- ticket vengono ripetuti per ogni ordine;
- qualsiasi correlazione costruita su quel dataset viene implicitamente pesata dalla molteplicità.

Se la domanda è a livello account, una strategia più coerente è:

```sql
WITH orders_by_account AS (...),
tickets_by_account AS (...)
SELECT ...
FROM orders_by_account o
JOIN tickets_by_account t
  ON o.account_id = t.account_id;
```

Il principio non è “aggregare sempre prima”. È:

> **portare le fonti allo stesso grain analitico prima di confrontare misure che devono vivere allo stesso livello.**

### Caso simulato/composito — il supporto che sembrava aumentare il fatturato

Un SaaS B2B trova una relazione molto forte tra ticket aperti e revenue.

Nel dataset ottenuto con una join fact-to-fact, gli account con molti ordini e molti ticket producono decine di righe e dominano la stima.

Dopo aver costruito una riga per account-periodo, la relazione si riduce drasticamente.

Il problema non era un algoritmo sofisticato. Era il peso implicito introdotto dal join.

### Campo del contract: relationship semantics

Per una relazione many-to-many, l'Analytical Data Contract dovrebbe dichiarare:

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

Questo rende testabili domande come:

- i pesi sommano a 1?
- esistono associazioni senza parent?
- la join produce il numero di righe atteso?
- il totale allocato si riconcilia con il totale originale?

### Regola operativa

Prima di una many-to-many chiedere:

1. vogliamo rappresentare una relazione o allocare un valore?
2. qual è il grain della bridge?
3. una fact viene ripetuta più volte?
4. il totale deve conservarsi dopo l'allocazione?
5. quale policy business determina il peso?
6. la stessa policy viene usata da tutti i consumer?

> **Una many-to-many non è un'anomalia da eliminare. È una relazione che richiede semantica esplicita prima che una misura possa attraversarla senza moltiplicarsi.**
