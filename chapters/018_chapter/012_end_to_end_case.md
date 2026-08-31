## 18.11 Caso end-to-end: da dashboard artigianale a sistema analitico governato
Consideriamo **Helios Mobility**, azienda europea di micromobilità con circa 4,8 milioni di corse al mese.

Ogni lunedì il management riceve un pacchetto con:

- rides;
- revenue;
- gross margin;
- fleet availability;
- incident rate;
- retention;
- CAC;
- forecast delle corse.

Il processo sembra maturo perché esistono molte dashboard.

In realtà è fragile.

## Situazione iniziale

Il weekly business review richiede ogni volta quasi due giorni di lavoro manuale.

Tre team usano definizioni diverse di `active_rider`.

Finance riconcilia revenue con uno scarto medio dell'1,7%.

Il forecast viene ricalcolato in notebook separati per città.

Una modifica all'app può cambiare il tracking senza che analytics lo sappia.

Se una pipeline fallisce alle 5:00, spesso il problema viene scoperto alle 9:30 durante il meeting.

L'azienda non ha un problema di assenza di dati.

Ha un problema di **sistema analitico**.

## Fase 1 — Identificare i prodotti decisionali

Il team evita di partire dalla domanda:

> “Quali dashboard dobbiamo rifare?”

Parte invece da:

> “Quali decisioni ricorrenti devono essere supportate?”

Emergono cinque prodotti:

1. city performance;
2. fleet allocation;
3. pricing e promotions;
4. retention;
5. weekly executive review.

Ogni prodotto riceve:

- business owner;
- analytical owner;
- metriche certificate;
- freshness target;
- qualità minima;
- downstream consumers.

## Fase 2 — Semantic layer

Il team definisce una singola logica per:

- active rider;
- completed ride;
- recognized revenue;
- contribution margin;
- vehicle availability;
- retention.

Ogni definizione contiene:

- formula;
- grain;
- filtri;
- owner;
- versione;
- data di validità.

Quando una metrica cambia, la modifica viene trattata come cambiamento di prodotto, non come semplice edit SQL.

## Fase 3 — Test e osservabilità

Vengono introdotti controlli su:

- completezza eventi;
- unicità ride_id;
- riconciliazione pagamenti;
- lag di ingestion;
- distribuzione delle corse per città;
- delta anomali dei KPI.

Ma soprattutto viene creato un **data health header** per il weekly review.

Prima dei KPI il management vede:

- freshness: OK;
- completeness: 99,96%;
- payment reconciliation: 99,91%;
- known incidents: 1;
- confidence status: green/yellow/red.

L'affidabilità smette di essere invisibile.

## Fase 4 — CI/CD e breaking changes

Le trasformazioni passano in version control.

Ogni modifica rilevante richiede:

1. pull request;
2. test automatici;
3. confronto delle metriche vecchie/nuove;
4. approvazione del metric owner per cambi semantici;
5. deploy controllato.

Quando il team Product modifica il tracking di `ride_started`, il contratto dati segnala il cambiamento prima del rollout completo.

## Fase 5 — Cost management

L'azienda scopre che il 37% del costo compute analytics viene da refresh ad alta frequenza di dashboard poco usate.

La segmentazione dei workload distingue:

- near-real-time per fleet operations;
- hourly per city performance;
- daily per executive/finance;
- on-demand per analisi esplorative.

Il costo mensile diminuisce del 24% senza ridurre il valore operativo.

## Fase 6 — AI e agenti

Helios introduce agenti per:

- triage dei data incident;
- generazione di query esplorative;
- sintesi delle anomalie;
- preparazione della prima bozza del weekly review.

Ma gli agenti lavorano sul semantic layer certificato e non possono modificare metriche o sistemi operativi senza escalation.

Quando un agente identifica un calo del 18% nelle corse a Milano, produce:

- decomposizione;
- query;
- fonti;
- possibili spiegazioni;
- confidence;
- alternative hypothesis.

Non può pubblicare direttamente “domanda in calo”.

Nel caso specifico il problema è un ritardo di telemetria di un provider, non il mercato.

## Fase 7 — Misurare il successo

Dopo sei mesi:

- preparazione del weekly review: da ~14 ore-persona a ~3;
- scarto di revenue vs Finance: da 1,7% a <0,2%;
- incidenti scoperti durante meeting: -73%;
- definizioni attive di active rider: da 7 a 1 certificata;
- costo compute per mille corse analizzate: -19%;
- tempo mediano per diagnosticare un'anomalia: da 96 a 28 minuti.

Questi numeri sono **caso simulato/composito**, costruito per didattica, non un caso pubblico documentato.

## La lezione

Helios non ha “costruito una dashboard migliore”.

Ha trasformato analytics in un sistema con:

**semantica → ownership → test → osservabilità → deployment → cost control → governance → misurazione dell'impatto**

Questa è la differenza tra produrre analisi e costruire una capacità analitica organizzativa.

> **Scalare analytics non significa far girare più query. Significa rendere affidabile, ripetibile e governabile il percorso che porta dai dati alla decisione.**
