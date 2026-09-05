## 11.16 Caso end-to-end: il contribution margin corretto costruito sul modello sbagliato

### AsterRetail: quando la classifica cambia perché cambia la rappresentazione

AsterRetail vende elettronica e piccoli elettrodomestici in undici Paesi europei attraverso e-commerce, marketplace e negozi fisici. Il management vuole decidere quali categorie spingere nel prossimo trimestre e usa come KPI il **Contribution Margin per categoria**:

```text
net revenue
- cost of goods sold
- payment fees
- variable fulfillment cost
- allocated outbound shipping cost
```

Il primo dashboard produce:

| Categoria | Contribution margin % |
|---|---:|
| Smart Home | 29,8% |
| Audio | 25,6% |
| Gaming | 24,9% |
| Small Appliances | 18,1% |

La proposta è ridurre investimenti su Small Appliances e spostare budget verso Smart Home. Prima di agire, il team ricostruisce l’**Analytical Data Contract** della metrica.

Il primo problema è il grain. Il dashboard parte da `orders`, una riga per ordine, ma revenue e COGS vivono a livello `order_line`; i refund possono essere parziali per linea; shipping cost vive a livello spedizione; payment fee a livello transazione; la categoria nella dimensione prodotto. Un singolo ordine può contenere tre categorie. Attribuire l’intero margine dell’ordine a una sola categoria non è un’approssimazione neutra: cambia la domanda. Il grain economico di partenza diventa quindi **una riga per linea d’ordine valida**.

### Rendere compatibili misure che nascono a grain diversi

La query originale unisce `order_lines` direttamente a `payment_transactions` tramite `order_id`. Un ordine con quattro linee e tre transazioni può generare dodici righe: revenue e COGS vengono ripetuti. Il team costruisce prima `payment_fees_by_order`, una riga per ordine con la sola fee economicamente rilevante, e poi definisce come quella misura order-level deve essere allocata sulle linee.

La policy stabilita è proporzionale al net revenue valido della linea rispetto al totale dell’ordine. Questo rende testabile un invariant:

```text
SUM(line_payment_fee_allocated) = order_payment_fee
```

Lo shipping richiede una relazione ancora più esplicita. Un ordine può generare più spedizioni e una spedizione può contenere più linee e categorie. Viene quindi creata:

```text
bridge_shipment_order_line
shipment_id
order_line_id
shipped_units
allocation_weight
```

Per questo caso il costo outbound viene allocato in proporzione alle unità spedite ponderate per classe volumetrica del prodotto. Non è l’unica policy possibile; è quella dichiarata e riconciliabile:

```text
SUM(line_shipping_cost_allocated)
=
SUM(shipment_cost)
```

entro la tolleranza di arrotondamento.

### Il passato economico continua a cambiare dopo la vendita

La prima versione incrementale processa soltanto gli ordini creati nelle ultime 24 ore. I refund, però, arrivano giorni o settimane dopo. La conseguenza è sottile: la revenue recente sembra corretta, mentre il net revenue storico viene progressivamente sovrastimato e le categorie con resi tardivi appaiono troppo profittevoli.

Il contract cambia quindi update semantics:

```text
change detection = order_line.updated_at OR refund.updated_at
lookback = 45 giorni
late cases oltre finestra = coda di reconciliation/backfill
```

Anche la categoria prodotto riscriveva il passato. Durante l’anno alcuni dispositivi passano da `Electronics` a `Smart Home`. Se il report storico usa `dim_product.category` corrente, vendite precedenti vengono spostate retroattivamente e Smart Home sembra crescere più del reale secondo la tassonomia dell’epoca. Per la decisione corrente il team sceglie la categoria **valida alla order date**.

Il gruppo opera inoltre in più valute. Il dashboard originale usa il cambio corrente, rendendo la storia instabile. Il contract fissa:

```text
reporting currency: EUR
FX policy: monthly accounting rate valid for recognized revenue month
```

Una domanda di cash economics potrebbe usare una policy diversa; il punto è non lasciare il tasso implicito.

### I test diventano la prova del modello

Prima della pubblicazione il team verifica più livelli:

```text
GRAIN
order_line_id unico nel modello finale

JOIN
nessun aumento inatteso di order_line_id distinti

REFUND
allocated refund per order_line = refund economico sorgente

PAYMENT FEES
somma fee allocate per ordine = fee ordine

SHIPPING
somma costi allocati per spedizione = costo spedizione

DIMENSION HISTORY
ogni order_line ha esattamente una versione prodotto valida alla order_date

RECONCILIATION
recognized net revenue warehouse vs Finance entro tolleranza concordata
```

La classifica cambia:

| Categoria | Dashboard iniziale | Modello validato |
|---|---:|---:|
| Smart Home | 29,8% | 23,7% |
| Audio | 25,6% | 24,8% |
| Gaming | 24,9% | 22,9% |
| Small Appliances | 18,1% | 22,4% |

Small Appliances non era strutturalmente la categoria peggiore. Era penalizzata da allocazione shipping incoerente e classificazioni prodotto correnti; Smart Home era favorita da refund tardivi non rientrati, riclassificazione storica e duplicazioni legate ai pagamenti.

La decisione cambia di conseguenza. Il management non esegue il riallocamento generalizzato del budget. Decide invece di intervenire sui prodotti Smart Home con refund/return cost elevati, testare packaging e carrier sulle sottocategorie bulky, mantenere investimenti sugli Small Appliances con contribution margin netto alto e certificare il modello come sorgente condivisa per Finance, Merchandising e BI.

### Analytical Data Contract finale

```text
business question:
contribution margin per categoria di vendita

grain:
una riga per order_line_id valido

business keys:
order_id, order_line_id, product_id

time semantics:
order date per attribuzione commerciale
recognized revenue month per FX accounting

product dimension:
point-in-time alla order_date

metric components:
net revenue
COGS
allocated payment fee
allocated variable fulfillment cost
allocated outbound shipping

allocation invariants:
fees e shipping devono riconciliarsi ai totali sorgente

update semantics:
record mutabili, refund tardivi, lookback + reconciliation

quality gates:
uniqueness, join coverage, allocation conservation, Finance reconciliation

service envelope:
refresh giornaliero entro 07:30

owner:
Analytics Engineering + Finance metric owner
```

Nessun failure mode principale richiedeva SQL sintatticamente invalido. Erano errori di grain, cardinalità, allocazione, tempo, storia, incrementalità e riconciliazione.

> **Quando la rappresentazione è corretta, la query finale può diventare semplice. La complessità che merita di esistere va spostata in modelli, contratti e test riusabili, non duplicata silenziosamente in ogni consumer.**
