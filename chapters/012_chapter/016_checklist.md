## 12.15 Data Flow Architecture Map: leggere il percorso del dato end-to-end

Il deliverable del capitolo è la **Data Flow Architecture Map**. Non deve descrivere ogni servizio cloud, subnet o dettaglio infrastrutturale. Deve permettere a una persona che non ha costruito la pipeline di capire abbastanza bene il percorso del dato da sapere quale asset interrogare, quale freshness aspettarsi, dove cercare un failure, chi è owner e come il sistema si comporta durante cambiamenti e incidenti.

La struttura base rimane:

```text
SOURCE
  ↓
CAPTURE
  ↓
TRANSPORT
  ↓
STORAGE
  ↓
TRANSFORM
  ↓
SERVE
  ↓
CONSUME
```

### 1. Decisione e consumer

La mappa dovrebbe partire dal fondo, non dalla tecnologia.

```text
consumer:
decision/use case:
decision deadline:
required freshness:
required completeness:
downstream action:
```

Sono queste proprietà a giustificare SLO, latenza e recovery del percorso.

### 2. Source e capture

```text
system/entity:
system of record:
workload type:
history available:
source owner:

capture mode: full / incremental / CDC / event
capture frequency:
initial snapshot:
insert/update/delete support:
```

Domande chiave: dove nasce il fenomeno, come sappiamo che è cambiato, quale storia esiste e quanto carico analitico può sostenere il source?

### 3. Transport e storage

```text
transport: batch / file / queue / stream
expected lag:
ordering guarantee:
delivery/retry semantics:
replay retention:

raw/source-aligned location:
curated location:
retention:
schema evolution policy:
last known good state:
```

Qui dobbiamo sapere se gli eventi possono duplicarsi o arrivare fuori ordine, quanto a lungo possiamo rigiocarli e da quale stato possiamo ricostruire il downstream.

### 4. Transform

La semantica dettagliata rimane nell'**Analytical Data Contract** del Capitolo 11. La mappa aggiunge la dimensione operativa:

```text
model:
input/output grain:
quality gates:
update semantics:
version:
upstream readiness:
retry/backfill:
publish boundary:
owner:
```

### 5. Serve

```text
serving interface:
warehouse / mart / semantic model / API:
certification state:
refresh/freshness:
availability expectation:
degraded behavior:
```

Il consumer deve sapere non soltanto dove leggere, ma anche che cosa vedrà quando il refresh odierno fallisce: `READY`, `DEGRADED`, `STALE`, `INCOMPLETE` o `FAILED`.

### 6. Contract e lineage

```text
producer contract/version:
compatibility policy:
breaking-change process:

upstream dependencies:
downstream consumers:
change history:
impact-analysis capability:
```

Prendi un KPI critico e verifica di poter attraversare la mappa in entrambe le direzioni: dal numero alle sorgenti e dal producer ai consumer impattati.

### 7. Reliability e recovery

```text
SLI:
SLO:
quality readiness gate:
alert:
degraded policy:

last known good:
idempotency:
checkpoint:
replay/backfill source:
RPO/RTO:
recovery validation:
```

La recovery termina quando il dato è nuovamente completo, fresco e riconciliato quanto richiesto, non quando il job è semplicemente tornato verde.

### 8. Economics

```text
major cost driver:
latency/reliability bought:
utilization:
complexity introduced:
failure cost mitigated:
scale trigger:
```

Ogni componente importante dovrebbe poter spiegare quale requisito soddisfa e quale segnale ci dirà che va semplificato o potenziato.

### Esempio compatto

```text
USE CASE
operations late-delivery alert

CONSUMER
regional operations; decision window < 20 min

SOURCE
operational shipments DB

CAPTURE
CDC insert/update/delete

TRANSPORT
managed change stream; replay retention 7d

STORAGE
raw changes retained 30d
curated shipment state retained historically

TRANSFORM
shipment state + promise model
quality gate: expected region coverage >= 99%

SERVE
operations mart + alert API

SLO
95% events visible < 5 min
99% region coverage < 15 min

DEGRADED MODE
show last update + affected region; suppress global alert if coverage below threshold

RECOVERY
replay from checkpoint; reconcile shipment counts against source

OWNER
Data Platform / Logistics Analytics
```

### Il test dei cinque minuti

Una persona nuova nel team dovrebbe riuscire rapidamente a rispondere a queste domande:

1. da dove nasce il dato?
2. quanto dovrebbe essere fresco e completo?
3. quale asset deve interrogare?
4. quali failure upstream possono renderlo inaffidabile?
5. chi è owner?
6. possiamo rigiocare o ricostruire la storia?
7. quale consumer viene impattato da una modifica?

Se servono giorni di archeologia, la mappa non è ancora sufficiente.

> **Il Data Analyst non deve amministrare ogni componente della piattaforma. Deve saper leggere abbastanza bene il sistema da non confondere un numero disponibile con un numero pronto per essere creduto.**
