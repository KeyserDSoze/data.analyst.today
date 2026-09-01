## 11.16 Caso end-to-end: il contribution margin corretto costruito sul modello sbagliato

### Caso simulato/composito — AsterRetail

AsterRetail vende elettronica e piccoli elettrodomestici in undici Paesi europei, attraverso e-commerce, marketplace e negozi fisici.

Il management vuole decidere quali categorie spingere nel prossimo trimestre.

Il KPI scelto è:

> **Contribution Margin per categoria**

La definizione business concordata è:

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

Il management propone di ridurre investimenti su Small Appliances e spostare budget verso Smart Home.

Prima della decisione, il team costruisce l'**Analytical Data Contract** della metrica.

### 1. Qual è il grain del fenomeno economico?

Il dashboard parte da `orders`, una riga per ordine.

Ma:

- revenue e COGS vivono a livello `order_line`;
- refund possono essere parziali e riferirsi a singole linee;
- shipping cost può essere a livello spedizione;
- payment fee vive a livello transazione;
- categoria prodotto vive nella dimensione prodotto.

Un solo ordine può contenere tre categorie.

Attribuire l'intero margine dell'ordine a una sola categoria scelta arbitrariamente è già semanticamente sbagliato.

Il grain economico di partenza diventa:

> **una riga per linea d'ordine valida**.

### 2. Il join con i pagamenti moltiplica le linee

Alcuni ordini hanno:

- autorizzazione;
- cattura;
- retry;
- refund.

La query originale unisce `order_lines` direttamente a `payment_transactions` tramite `order_id`.

Un ordine con quattro linee e tre transazioni genera fino a dodici righe.

Revenue e COGS vengono ripetuti.

Il team costruisce prima:

```text
payment_fees_by_order
una riga per order_id
```

con la sola fee economicamente rilevante aggregata per ordine.

Poi decide come allocarla sulle linee.

### 3. Una misura a livello ordine richiede una policy di allocazione

Le payment fee sono note per ordine, ma il KPI è per categoria.

Serve una policy.

Il contract stabilisce:

```text
payment fee allocation:
proporzionale al net revenue della linea sul net revenue valido dell'ordine
```

Per ogni ordine:

```text
SUM(line_payment_fee_allocated) = order_payment_fee
```

Questo diventa un invariante testabile.

### 4. Lo shipping cost è ancora più complesso

Un ordine può essere diviso in due spedizioni.

Una spedizione può contenere più linee e categorie.

La tabella `shipments` non è quindi direttamente compatibile con `order_lines`.

Il team crea una bridge:

```text
bridge_shipment_order_line
shipment_id
order_line_id
shipped_units
allocation_weight
```

La policy scelta per il caso è allocare il costo di spedizione in proporzione alle unità spedite ponderate per una classe volumetrica del prodotto.

Non è l'unica policy possibile.

Il punto è che ora è esplicita e riconciliabile:

```text
SUM(line_shipping_cost_allocated)
=
SUM(shipment_cost)
```

entro una tolleranza di arrotondamento.

### 5. I refund arrivano dopo la vendita

La prima versione del modello incrementale processa soltanto gli ordini creati nelle ultime 24 ore.

I refund, però, arrivano spesso giorni o settimane dopo.

Il risultato:

- revenue recente corretta;
- net revenue storico progressivamente sovrastimato;
- categorie con resi tardivi apparentemente troppo profittevoli.

Il team modifica l'update semantics:

```text
change detection = order_line.updated_at OR refund.updated_at
lookback = 45 giorni
late cases oltre finestra = coda di reconciliation/backfill
```

### 6. La categoria corrente riscrive il passato

Durante l'anno AsterRetail riorganizza il catalogo.

Alcuni dispositivi passano da:

```text
Electronics → Smart Home
```

Se il report storico usa `dim_product.category` corrente, vendite precedenti alla riclassificazione vengono spostate retroattivamente.

Il management pensa che Smart Home sia cresciuta molto più di quanto sia realmente accaduto sotto la classificazione dell'epoca.

Per la domanda corrente viene deciso:

> analizzare ogni vendita nella categoria valida alla data dell'ordine.

Il modello usa quindi la versione point-in-time della dimensione prodotto.

### 7. Valute: quale tasso di cambio?

Il gruppo opera in più valute.

Il dashboard originale converte tutti gli importi con il cambio corrente.

Questo rende instabile la storia.

Il contract specifica:

```text
reporting currency: EUR
FX policy: monthly accounting rate valid for recognized revenue month
```

Una diversa domanda, per esempio cash economics, potrebbe richiedere una policy diversa.

### 8. I test del modello

Prima della pubblicazione vengono eseguiti invarianti su più livelli.

**Grain**

```text
order_line_id unico nel modello economico finale
```

**Join**

```text
nessun aumento inatteso di order_line_id distinti
```

**Refund**

```text
allocated refund per order_line = refund economico sorgente
```

**Payment fees**

```text
somma fee allocate per ordine = fee ordine
```

**Shipping**

```text
somma costi allocati per spedizione = costo spedizione
```

**Dimension history**

```text
ogni order_line ha esattamente una versione prodotto valida alla order_date
```

**Reconciliation**

```text
recognized net revenue warehouse vs Finance entro tolleranza concordata
```

### 9. La classifica cambia

Dopo la ricostruzione:

| Categoria | Dashboard iniziale | Modello validato |
|---|---:|---:|
| Smart Home | 29,8% | 23,7% |
| Audio | 25,6% | 24,8% |
| Gaming | 24,9% | 22,9% |
| Small Appliances | 18,1% | 22,4% |

Small Appliances non era strutturalmente la categoria peggiore.

Era penalizzata da:

- allocazione shipping incoerente;
- classificazioni di prodotto correnti;

mentre Smart Home era favorita da:

- refund tardivi non ancora rientrati;
- riclassificazione storica di prodotti;
- duplicazioni legate ai pagamenti.

### 10. La decisione cambia

Il management non esegue il riallocamento generalizzato del budget.

La decisione diventa più specifica:

1. intervenire su prodotti Smart Home con refund e return cost elevati;
2. testare packaging e carrier su specifiche sottocategorie bulky;
3. mantenere investimenti su Small Appliances ad alto contribution margin netto;
4. certificare il nuovo modello come sorgente condivisa per Finance, Merchandising e BI.

### L'Analytical Data Contract finale

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

### La lezione del caso

Nessuno dei failure mode principali richiedeva SQL sintatticamente invalido.

Erano errori di rappresentazione:

- grain;
- cardinalità;
- allocazione;
- tempo;
- storia dimensionale;
- incrementalità;
- riconciliazione.

Quando questi elementi vengono risolti, la query finale del KPI può essere relativamente semplice.

> **La complessità che merita di esistere va spostata in modelli, contratti e test riusabili. Non duplicata silenziosamente in ogni query che consuma il dato.**
