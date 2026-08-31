## 12.8 Caso studio: l'azienda che aveva tutti i dati ma nessuna verità condivisa

**LumenCommerce** è un retailer omnicanale con 1,4 miliardi di euro di fatturato, 180 negozi fisici, e-commerce, app mobile e programma loyalty.

La crescita è stata rapida. L'architettura dati, invece, è cresciuta per aggiunte successive.

### Il problema iniziale

Il CEO chiede una domanda apparentemente semplice:

> Qual è il valore reale del cliente omnicanale rispetto a quello solo online o solo negozio?

Tre settimane dopo non esiste ancora una risposta condivisa.

Il team scopre che:

- gli ordini e-commerce sono in PostgreSQL;
- i POS inviano file ogni notte;
- il loyalty system usa un customer ID differente;
- i resi negozio possono riferirsi a ordini online;
- gli eventi app arrivano in streaming;
- Finance riceve dati dall'ERP;
- Marketing ha un proprio database con attribution e campagne;
- cinque dashboard Power BI costruiscono metriche con logiche diverse.

L'azienda possiede tutti i dati necessari. Ma non possiede ancora una **catena analitica affidabile**.

## Prima architettura: integrazione punto-punto

Nel tempo erano nate pipeline specifiche:

```text
POS → Finance report
E-commerce DB → Marketing dashboard
CRM → Loyalty dashboard
App events → Product dashboard
ERP → CFO workbook
```

Ogni caso funziona isolatamente.

Il problema emerge quando bisogna combinare domini.

Un cliente può essere:

```text
customer_id = 93822
loyalty_id = L-773811
email_hash = 9f8...
app_user_id = u_442901
```

Senza identity resolution non esiste davvero un "cliente omnicanale" analizzabile.

## Ridisegnare partendo dalle decisioni

Il team evita di iniziare scegliendo la tecnologia.

Definisce prima i requisiti:

1. Finance richiede numeri riconciliabili giornalmente.
2. Operations richiede vendite quasi real time ogni 15 minuti.
3. Marketing richiede customer journey e campagne.
4. Product richiede eventi granulari dell'app.
5. Data Science vuole storia sufficientemente dettagliata per modelli.
6. Tutti devono usare una definizione coerente di cliente, ordine, vendita netta e reso.

## La nuova struttura concettuale

Viene progettato un flusso a livelli:

```text
SORGENTI
POS / e-commerce / loyalty / ERP / app / ads
                    ↓
INGESTION
batch + streaming
                    ↓
RAW / BRONZE
copia fedele delle sorgenti
                    ↓
CURATED / SILVER
identity resolution
standardizzazione date e valute
validazione e deduplication
ordini e resi riconciliati
                    ↓
BUSINESS / GOLD
fact_orders
fact_returns
fact_customer_activity
dim_customer
dim_product
dim_store
dim_date
                    ↓
SEMANTIC LAYER
net_sales
active_customer
omnichannel_customer
repeat_purchase
                    ↓
CONSUMO
BI / notebooks / ML / alerts
```

## Un errore evitato: usare tutto in streaming

La prima proposta tecnica prevedeva streaming quasi ovunque.

L'analisi dei requisiti mostra invece che non serve.

- Eventi app: streaming.
- Vendite e-commerce per operations: aggiornamento 5–15 minuti.
- POS: micro-batch durante la giornata.
- ERP: giornaliero.
- Finance close: batch riconciliato.

Questa scelta riduce complessità e costi senza peggiorare alcuna decisione.

## Il nuovo customer model

La parte più difficile non è infrastrutturale ma semantica.

Il team costruisce una tabella di identity mapping con livelli di confidenza.

Esempio:

```text
canonical_customer_id = C184930
loyalty_id            = L773811
online_account_id     = O230911
app_user_id           = U442901
match_method          = authenticated_link
confidence            = high
```

Per i guest checkout senza identificazione certa, l'azienda evita di forzare match probabilistici nei KPI finanziari.

Questo abbassa leggermente il numero apparente di clienti omnicanale, ma aumenta l'affidabilità.

## Il risultato analitico

Dopo il nuovo modello, il team calcola il valore cliente a 12 mesi.

| Segmento | Clienti | Revenue media 12m | Margine medio 12m |
|---|---:|---:|---:|
| Solo negozio | 1,82M | €284 | €91 |
| Solo online | 1,14M | €318 | €96 |
| Omnicanale | 0,46M | €711 | €206 |

A prima vista l'omnicanale sembra molto più prezioso.

Ma il Capitolo 8 ci ricorda di non saltare dalla correlazione alla causalità.

I clienti omnicanale potrebbero essere già i clienti più coinvolti.

Il risultato viene quindi usato per:

- segmentazione;
- prioritizzazione;
- formulazione di un'ipotesi;
- progettazione di esperimenti per capire se facilitare il secondo canale aumenta realmente valore e retention.

L'architettura ha reso possibile l'analisi. Non ha creato causalità.

## Benefici dopo sei mesi

LumenCommerce misura:

- tempo medio per produrre un nuovo KPI cross-channel: da 9 giorni a 2,5;
- dashboard con definizioni revenue locali: da 17 a 3, con piano di migrazione;
- incidenti mensili da duplicazioni ingestion: da 8 a 1;
- query dirette sui database operativi: -71%;
- tempo medio per identificare upstream cause di un KPI errato: da ore/giorni a meno di 40 minuti nei dataset con lineage completa.

Non tutto viene centralizzato.

I team mantengono libertà esplorativa nei workspace, ma le metriche executive devono derivare da dataset certificati.

## La lezione

L'architettura non viene valutata dal numero di servizi cloud presenti nel diagramma.

Viene valutata dalla sua capacità di rendere più affidabile e meno costoso il percorso:

**evento operativo → dato → trasformazione → significato → analisi → decisione**.

La domanda più importante per un Data Analyst non è:

> Usiamo un warehouse o un lakehouse?

È:

> Per questa decisione, quale percorso ha fatto il dato e quali assunzioni sono state introdotte lungo il percorso?
