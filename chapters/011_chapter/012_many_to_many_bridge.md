## 11.11 Many-to-many e bridge tables: quando il join moltiplica il mondo

Molte relazioni di business non sono uno-a-molti.

Un ordine può avere più promozioni. Un cliente può appartenere a più segmenti. Un medico può lavorare in più strutture. Un prodotto può appartenere a più collezioni. Un contratto può coinvolgere più account manager.

Quando due tabelle contengono entrambe più righe per la stessa chiave, un join diretto può creare una moltiplicazione combinatoria.

### Caso realistico: marketing attribution da €3,2M a €5,7M

**UrbanPeak**, retailer omnicanale, vuole attribuire il fatturato alle campagne marketing.

Ha:

```text
orders
order_id | revenue
O1       | 100
```

E una tabella touchpoint:

```text
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

attribuisce €100 a ciascuna campagna.

Il totale attribuito diventa €300, anche se l'ordine vale €100.

A scala mensile, UrbanPeak vede €5,7M di revenue attribuita contro €3,2M di revenue effettiva.

Il join è tecnicamente corretto. Il modello di allocazione no.

### La bridge table

Una bridge table rappresenta esplicitamente una relazione many-to-many.

Per esempio:

```text
bridge_order_campaign
order_id | campaign_id | allocation_weight
O1       | C10         | 0.50
O1       | C22         | 0.30
O1       | C35         | 0.20
```

La revenue attribuita può allora essere:

```sql
SUM(order_revenue * allocation_weight)
```

A condizione che, per ogni ordine:

```text
SUM(allocation_weight) = 1
```

### Il peso non è un dettaglio tecnico

Come distribuire il valore?

- equally weighted;
- first touch;
- last touch;
- position based;
- modello algoritmico;
- nessuna allocazione, mantenendo semplicemente la relazione.

La bridge table non decide il significato. Lo rende esplicito.

### Fact-to-fact join: un altro pericolo

Supponiamo di avere:

- `fact_orders`: una riga per ordine;
- `fact_support_tickets`: una riga per ticket.

Un cliente può avere 8 ordini e 5 ticket.

Se uniamo entrambe direttamente per `customer_id`, otteniamo fino a 40 combinazioni per quel cliente.

Revenue e ticket possono essere entrambi moltiplicati.

Una strategia spesso più sicura è aggregare prima ciascuna fact al grain desiderato:

```sql
WITH order_by_customer AS (...),
ticket_by_customer AS (...)
SELECT ...
FROM order_by_customer o
JOIN ticket_by_customer t
  ON o.customer_id = t.customer_id;
```

### Caso realistico: il supporto che sembrava causare più acquisti

Un SaaS B2B trova una correlazione impressionante tra numero di ticket e fatturato.

Dopo il join, i clienti con molti ordini e molti ticket generano molte più righe e dominano il dataset.

La relazione apparente è in parte un artefatto del grain.

Dopo aver aggregato correttamente a livello account, la correlazione scende drasticamente.

### Checklist per i many-to-many

Prima di un join chiedere:

- la chiave è unica a sinistra?
- è unica a destra?
- quante righe ci aspettiamo dopo il join?
- esiste una bridge table?
- serve un peso di allocazione?
- stiamo unendo due fact table?
- dobbiamo aggregare prima del join?

**Una relazione many-to-many non è un errore di database. Diventa un errore analitico quando viene trattata come se fosse one-to-many.**
