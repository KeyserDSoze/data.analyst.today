## 12.15 Data Flow Architecture Map: leggere il percorso del dato end-to-end

Il deliverable di questo capitolo è una **Data Flow Architecture Map**.

Non deve contenere ogni servizio cloud, subnet o dettaglio infrastrutturale.

Deve permettere a un Data Analyst di capire abbastanza bene il percorso del dato da sapere:

- dove cercare un failure;
- quale freshness aspettarsi;
- quale layer interrogare;
- chi è owner;
- cosa succede quando qualcosa cambia o si rompe.

### La struttura base

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

Per ogni nodo o passaggio annotiamo le proprietà seguenti.

### 1. Source

```text
system/entity:
system of record:
operational or analytical workload:
history available:
source owner:
sensitivity:
```

Domande:

- dove nasce il fenomeno?
- il source viene aggiornato o sovrascritto?
- possiamo interrogare direttamente senza impattare operations?

### 2. Capture

```text
mode: full / incremental / CDC / event
capture frequency:
initial snapshot:
insert/update/delete support:
source-side failure behavior:
```

Domande:

- come sappiamo che qualcosa è cambiato?
- catturiamo delete?
- esiste un bootstrap iniziale?

### 3. Transport

```text
batch / file / queue / stream:
expected lag:
ordering guarantee:
delivery semantics:
retry/replay:
retention:
```

Domande:

- gli eventi possono duplicarsi?
- possono arrivare fuori ordine?
- quanto a lungo possiamo rigiocarli?

### 4. Storage

```text
raw/source-aligned location:
curated location:
retention:
partitioning/layout:
schema evolution policy:
last known good state:
```

Domande:

- quale livello preserva la sorgente?
- possiamo ricostruire i layer downstream?
- qual è lo stato del dato in ciascun layer?

### 5. Transform

Qui richiamiamo l'**Analytical Data Contract** del Capitolo 11.

```text
model:
input/output grain:
key transformations:
quality gates:
update semantics:
version:
owner:
```

Il Capitolo 12 aggiunge soprattutto:

- quando la trasformazione può partire;
- da quali dependency dipende;
- cosa succede se fallisce;
- come viene riprocessata.

### 6. Serve

```text
serving interface:
warehouse/mart/semantic/API:
certification state:
refresh/freshness:
availability expectation:
degraded behavior:
```

Domande:

- qual è il punto consigliato per il consumer?
- cosa vede se il refresh odierno fallisce?
- può distinguere READY da STALE?

### 7. Consume

```text
consumer:
decision/use case:
decision deadline:
required freshness:
required completeness:
downstream action:
```

Questo è il punto da cui dovrebbero derivare gli SLO.

L'architettura esiste per servire un consumer reale, non il contrario.

### 8. Contract boundary

Per ogni producer-consumer interface:

```text
schema/version:
semantic expectations:
compatibility policy:
breaking-change process:
```

Distinguere sempre producer data contract e Analytical Data Contract.

### 9. Reliability

```text
SLI:
SLO:
quality readiness gate:
alert:
error/degradation policy:
```

Non monitorare solo task success.

Misurare ciò che il consumer percepisce:

- freshness;
- completeness;
- availability;
- reconciliation quando appropriata.

### 10. Recovery

```text
last known good:
retry policy:
idempotency:
checkpoint:
replay source:
backfill:
RPO/RTO:
recovery validation:
```

La recovery termina quando il dato è di nuovo affidabile, non quando il processo è semplicemente ripartito.

### 11. Lineage

```text
upstream dependencies:
downstream consumers:
change history:
impact-analysis capability:
```

Prendi un KPI critico e verifica di poter attraversare la mappa in entrambe le direzioni.

### 12. Economics

```text
major cost driver:
refresh/latency cost:
utilization:
complexity introduced:
scale trigger:
```

La soluzione deve essere proporzionata al valore e al rischio della decisione.

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

Dopo aver costruito la mappa, una persona nuova nel team dovrebbe riuscire in pochi minuti a rispondere a:

1. da dove nasce il dato?
2. quanto dovrebbe essere fresco?
3. quale asset deve interrogare?
4. quali upstream failure lo possono rendere inaffidabile?
5. chi contattare quando succede?
6. possiamo rigiocare o ricostruire la storia?
7. quale consumer viene impattato da una modifica?

Se queste risposte richiedono giorni di archeologia, la mappa non è ancora sufficiente.

### La domanda finale

> **Per questa decisione, sappiamo descrivere l'intero percorso del dato, le garanzie attese in ogni boundary e il comportamento del sistema quando una di quelle garanzie smette di essere vera?**

> **Il Data Analyst non deve saper amministrare ogni componente della piattaforma. Deve saper leggere abbastanza bene il sistema da non confondere un numero disponibile con un numero pronto per essere creduto.**
