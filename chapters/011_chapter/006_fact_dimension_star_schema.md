## 11.5 Fact, dimension e star schema: progettare un modello che protegga il significato

I sistemi operativi sono progettati per far funzionare processi; i modelli analitici devono renderli interrogabili in modo coerente. Copiare direttamente la struttura di un ERP o di un CRM nel layer analitico spesso trasferisce a ogni consumer la responsabilità di ricostruire grain, relazioni e storia attraverso join ripetuti e fragili.

Lo **star schema** offre una separazione utile: le **fact table** rappresentano osservazioni, eventi, transazioni o snapshot; le **dimension table** forniscono il contesto con cui filtrare e raggruppare quei fatti. Microsoft Learn sottolinea proprio questa divisione e raccomanda fact table a grain coerente.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

La parte importante, però, non è disegnare una stella. È partire dal processo di business e chiedere **che cosa vogliamo misurare**. Solo dopo definiamo il grain della fact: una riga per linea di vendita confermata, una riga per evento contrattuale, una riga per prodotto-magazzino-giorno a fine giornata. Il grain della fact diventa il contratto delle aggregazioni possibili.

### Meridian Retail: dal clone dell’ERP a un modello condiviso

Meridian Retail ha 180 negozi e un e-commerce europeo. Il primo data mart commerciale copia quasi integralmente l’ERP; per ottenere revenue mensile per categoria e regione servono join tra nove tabelle operative. Dopo pochi mesi emergono tre failure mode: dashboard diverse assegnano negozi a regioni diverse, le categorie prodotto storiche vengono reinterpretate con la classificazione corrente e alcune query duplicano revenue attraverso relazioni many-to-many.

Il team ridisegna il processo:

```text
                 dim_date
                    |
dim_store --- fact_sales --- dim_product
                    |
               dim_customer
```

`fact_sales` contiene una riga per linea di vendita confermata e conserva misure atomiche come quantity, gross revenue, discount amount, return amount quando attribuibile, net revenue e cost. Le dimensioni forniscono il contesto. Il vantaggio non è soltanto avere query più corte: è fare in modo che grain, relazioni e storia non debbano essere reinventati da ogni dashboard.

### Evento e stato non sono la stessa fact

Per l’inventario possiamo registrare movimenti:

```text
+10 ricezione
-3 vendita
-1 danneggiato
```

oppure snapshot periodici:

```text
2026-08-01 → stock 84
2026-08-02 → stock 80
2026-08-03 → stock 91
```

La prima fact descrive flussi; la seconda stati. Possono coesistere, ma non sono intercambiabili. Sommare stock giornaliero nel tempo significa trattare uno stato come un flusso.

Lo stesso principio vale per le date. Una vendita può avere `order_date`, `payment_date`, `ship_date`, `delivery_date`, `recognition_date` e `return_date`. Queste colonne non sono ridondanza tecnica: rappresentano eventi economici e operativi differenti. Un modello robusto deve poter distinguere bookings, cash incassato, consegne e revenue riconosciuto senza farli collassare sotto un unico “mese”.

### La storia dimensionale è parte del modello

Supponiamo che un prodotto passi da `Accessories` a `Premium Accessories`. Possiamo voler riclassificare oggi tutto lo storico, oppure sapere come era classificato il prodotto al momento della vendita. Sono due domande legittime e producono report differenti.

Quando serve preservare il contesto storico, una fact può puntare a una **surrogate key** che identifica una versione della dimensione, mentre la business key continua a identificare l’entità. Microsoft Learn include surrogate key e Slowly Changing Dimensions tra i concetti centrali del modeling a stella proprio perché permettono di distinguere identità e versioni storiche.

Lo star schema non significa quindi “una tabella larga per tutto”. Una tabella unica può mescolare misure a grain diversi, ripetere attributi su milioni di righe e rendere difficile preservare la storia. Il confine più utile rimane:

```text
fatto osservato
+
contesto dell’osservazione
```

### Fact contract

| Campo | Esempio |
|---|---|
| processo | vendita |
| grain | linea di vendita confermata |
| business key | `order_id + line_number` |
| date roles | order, payment, ship, recognition |
| misure additive | quantity, net revenue, cost |
| semi/non additive | margin %, unit price medio |
| dimensioni | date, product, store, customer |
| history policy | categoria prodotto as-of vendita |
| late-arriving policy | aggiornamento dimensionale/reconciliation |

> **Il modello dati migliore non copia fedelmente il database operativo. Rende semplici e verificabili le domande analitiche importanti, e rende più difficile formulare per errore quelle sbagliate.**
