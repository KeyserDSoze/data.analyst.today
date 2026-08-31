## 11.16 Caso studio: il KPI giusto costruito sul modello sbagliato

**AsterRetail** è un gruppo e-commerce e retail con 11 paesi, 4 canali di vendita e circa 9 milioni di ordini l'anno.

Il management vuole introdurre un KPI apparentemente semplice:

> **Repeat Purchase Rate a 90 giorni**

La metrica deve misurare la quota di nuovi clienti che effettuano almeno un secondo acquisto entro 90 giorni dal primo.

Dopo due settimane il team analytics pubblica il dashboard.

Il risultato sorprende:

- Italia: 31,8%;
- Francia: 29,6%;
- Germania: 18,4%;
- Spagna: 27,9%.

La Germania sembra avere un problema enorme di retention.

Il Country Manager propone immediatamente un budget promozionale aggiuntivo di €900.000.

### Primo controllo: il grain

La tabella usata dal dashboard è `order_items`.

Una riga rappresenta una riga prodotto, non un ordine.

Il team aveva usato:

```sql
COUNT(*)
```

in alcuni passaggi intermedi per contare gli acquisti.

Un ordine con quattro prodotti veniva quindi trattato come quattro eventi.

Correzione:

```sql
COUNT(DISTINCT order_id)
```

oppure, meglio, costruzione di un modello a grain ordine prima dell'analisi.

Il KPI tedesco sale da 18,4% a 21,1%.

Problema ancora presente.

### Secondo controllo: identità cliente

AsterRetail consente:

- account registrato;
- guest checkout;
- acquisto in negozio con loyalty card;
- marketplace esterno.

Il campo `customer_id` è nullo per molti guest checkout.

In Germania il guest checkout è molto più diffuso.

Il modello iniziale escludeva implicitamente i guest perché faceva un `INNER JOIN` con la dimensione clienti.

Questo produceva due effetti:

1. alcuni primi acquisti sparivano;
2. alcuni secondi acquisti non venivano riconciliati con il primo.

Dopo identity resolution e un `LEFT JOIN` coerente, il repeat rate tedesco sale al 25,7%.

### Terzo controllo: la data del primo acquisto

Il team aveva definito il primo acquisto usando `order_created_at`.

Per i negozi fisici, però, i dati arrivano al warehouse in batch e `created_at` viene valorizzato con la data di ingestion, non con la data reale dello scontrino.

In alcuni casi il secondo acquisto online appare quindi temporalmente precedente al primo acquisto retail.

La correzione usa una `purchase_event_date` normalizzata per canale.

Nuovo repeat rate Germania: 27,4%.

### Quarto controllo: storico del paese

Il dashboard segmenta per paese usando `dim_customer.country` corrente.

I clienti che si trasferiscono vengono quindi riclassificati retroattivamente.

Non è il problema principale, ma introduce instabilità.

Il team passa a `country_at_first_purchase`, ricostruito point-in-time.

Germania: 27,1%.

### Quinto controllo: resi e cancellazioni

La metrica considera come secondo acquisto un ordine poi completamente cancellato.

In Germania il tasso di cancellazione è leggermente più alto a causa di un metodo di pagamento locale.

Dopo aver definito un acquisto valido come ordine con almeno un importo netto positivo dopo cancellazioni e refund:

- Italia: 28,7%;
- Francia: 27,9%;
- Germania: 26,5%;
- Spagna: 27,2%.

La Germania non è più un outlier drammatico.

### Il problema non era una query

Durante l'indagine vengono trovati cinque problemi distinti:

1. grain errato;
2. join che eliminava clienti;
3. semantica temporale incoerente;
4. attributi dimensionali non point-in-time;
5. definizione incompleta di acquisto valido.

Nessuno di questi problemi avrebbe necessariamente prodotto un errore SQL.

### Il modello finale

Il team crea tre modelli riusabili:

```text
fct_orders_valid
    una riga per ordine valido

customer_first_purchase
    una riga per cliente con data/canale/paese di acquisizione

customer_repeat_90d
    una riga per cliente con flag repeat entro 90 giorni
```

La metrica finale diventa:

```sql
SELECT
    acquisition_country,
    AVG(CASE WHEN repeated_within_90d THEN 1.0 ELSE 0.0 END) AS repeat_rate_90d
FROM customer_repeat_90d
GROUP BY 1;
```

Semplice, perché la complessità semantica è stata spostata nei modelli appropriati.

### La decisione di business cambia

Il budget promozionale da €900.000 non viene approvato sulla base del presunto gap tedesco.

L'analisi successiva mostra invece un problema più specifico:

- clienti acquisiti da paid social in Germania: repeat 21%;
- organic: 30%;
- CRM/referral: 34%.

Il team sposta quindi l'indagine dal paese al mix di acquisizione e alla qualità delle cohort.

### La lezione

Quando una metrica importante sembra sorprendente, non chiedere subito:

> "Quale spiegazione business troviamo?"

Prima chiedere:

> "Il modello dati rappresenta davvero il fenomeno che crediamo di misurare?"

La sequenza corretta è:

**definizione → grain → identità → tempo → join → qualità → metrica → interpretazione → decisione**.
