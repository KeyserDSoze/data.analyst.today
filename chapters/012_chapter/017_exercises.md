## 12.16 Esercizi: diagnosticare il percorso del dato

Gli esercizi non chiedono di scegliere il servizio cloud “migliore”.

Chiedono di costruire e criticare una **Data Flow Architecture Map** collegando requisiti decisionali, latenze, dipendenze e recovery.

### Esercizio 1 — Il dashboard delle 09:00

Il CEO apre un dashboard ogni mattina alle 09:00.

Il flusso è:

```text
ERP export 05:00
→ file landing
→ transform 06:00
→ warehouse 06:30
→ semantic refresh 07:00
→ dashboard
```

Oggi il file ERP arriva alle 08:20 ma tutti i task downstream partono agli orari previsti e terminano `SUCCESS` usando il file precedente.

Progetta:

1. dependency/readiness condition corretta;
2. freshness SLI/SLO;
3. stato da mostrare sul dashboard;
4. comportamento `BLOCK / STALE / DEGRADE`;
5. alert e owner.

### Esercizio 2 — Full reload o CDC?

Un e-commerce ha 600 milioni di righe ordine e circa 4 milioni di insert/update giornalieri.

Il full reload dura cinque ore.

Disegna due alternative:

**A. full reload**

**B. initial snapshot + CDC**

Per ciascuna valuta:

- workload sulla sorgente;
- freshness;
- delete;
- ordering;
- idempotenza;
- checkpoint;
- recovery dopo 48 ore di outage;
- possibilità di ricostruire lo stato.

Non assumere che CDC sia automaticamente migliore.

### Esercizio 3 — Pipeline verde, dato incompleto

Arrivano 25 file regionali su 28.

Il codice processa quelli presenti e termina senza errori.

Il report globale mostra revenue -14%.

Costruisci:

```text
expected completeness SLI:
SLO:
quality gate:
severity:
degraded behavior:
consumer message:
```

Spiega perché monitorare soltanto il job status non poteva intercettare il problema.

### Esercizio 4 — Event time e late data

Una pipeline streaming calcola transazioni per finestre di cinque minuti.

Tre eventi sono generati alle:

```text
10:01
10:03
10:04
```

ma vengono processati alle:

```text
10:02
10:04
10:14
```

Definisci:

- event time;
- processing time;
- cosa significa late data;
- come una watermark policy influenza la pubblicazione;
- provisional result e final/reconciled result.

Descrivi come testeresti il sistema con eventi early, on-time e late.

### Esercizio 5 — Il cambio schema che non rompe nulla

Il producer mantiene:

```text
speed: number
```

ma cambia l'unità da km/h a m/s.

Rispondi:

1. perché uno schema test può passare?
2. perché è un semantic breaking change?
3. quale producer contract avrebbe dovuto includere l'unità?
4. quale plausibility test potrebbe intercettarlo?
5. serve una nuova versione?
6. quali consumer individueresti tramite lineage?

### Esercizio 6 — Raw, curated e serving

Hai tre asset:

```text
raw_events
valid_events
customer_daily_activity
```

Per ciascuno specifica:

- state of data;
- garanzie esistenti;
- garanzie non ancora esistenti;
- consumer ammessi;
- replay source;
- quality gate.

Poi spiega quale layer useresti per:

- debugging di un evento;
- dashboard executive;
- ricostruzione dopo un bug di business logic.

### Esercizio 7 — Orchestrazione e retry

Un task scrive 730.000 righe, fallisce e viene automaticamente ritentato.

La seconda esecuzione usa `INSERT` puro.

Disegna due strategie sicure, scegliendo tra:

- staging + atomic publish;
- idempotent merge;
- partition replacement;
- checkpoint.

Per ciascuna indica come verificheresti il risultato dopo recovery.

### Esercizio 8 — SLO per due user journey

Lo stesso dominio dati serve:

**A. fraud operations**

azione necessaria entro pochi secondi/minuti.

**B. monthly Finance report**

richiede riconciliazione e quasi totale completezza.

Progetta SLI/SLO separati per:

- freshness;
- completeness;
- availability;
- reconciliation;
- recovery.

Spiega perché un unico SLO per il dataset sarebbe poco informativo.

### Esercizio 9 — Semantic layer e serving failure

Il warehouse è aggiornato correttamente ma il semantic model non si aggiorna da sei ore.

Disegna la mappa:

```text
source → storage → transform → serve → dashboard
```

Indica:

- dove si trova il failure;
- quale SLI è violato;
- se il dashboard deve usare last-known-good;
- quale timestamp mostrare;
- quali altri consumer possono continuare a lavorare interrogando il warehouse.

### Esercizio 10 — Cloud architecture review

Un report viene consultato da 20 persone una volta al giorno.

Il team propone:

- streaming sub-second;
- multi-region active-active;
- cluster always-on;
- sette giorni di event replay;
- dashboard refresh continuo.

Costruisci un'architecture review che chieda:

1. decision deadline;
2. cost of lateness;
3. cost of failure;
4. RTO/RPO necessari;
5. alternative più semplici;
6. trigger futuri che giustificherebbero maggiore complessità.

### Esercizio 11 — Caso VMO2

Usando il caso pubblico Virgin Media O2 citato nel capitolo, identifica almeno cinque motivi per cui consolidare piattaforme può generare valore oltre al costo del compute.

Poi spiega perché:

> “unificare la piattaforma”

non equivale automaticamente a:

> “unificare la semantica”.

### Esercizio 12 — Data contract end-to-end

Un producer aggiunge una colonna `battery_health` e successivamente cambia il tipo di `device_state`.

Per ogni modifica stabilisci:

- additive / structural breaking / semantic breaking;
- comportamento desiderato dell'ingestion;
- auto-evolve / rescue / fail;
- versioning;
- consumer notification;
- impact analysis;
- eventuale backfill.

### Esercizio 13 — Recovery dopo una business rule sbagliata

Scopri che il modello `net_revenue` ha sottratto due volte un tipo di refund per 43 giorni.

La pipeline oggi funziona perfettamente.

Disegna il recovery:

```text
identify affected period
→ freeze/publish state decision
→ correct code
→ backfill
→ validate invariants
→ reconcile Finance
→ republish
→ notify downstream
```

Indica quali layer devono essere ricostruiti e quale raw/curated source useresti.

### Esercizio 14 — Costruisci la Data Flow Architecture Map

Scegli un dataset reale che utilizzi nel tuo lavoro o un dominio che conosci.

Completa:

```text
DECISION / CONSUMER
SOURCE
CAPTURE
TRANSPORT
STORAGE
TRANSFORM
SERVE
CONSUME
CONTRACT BOUNDARIES
LINEAGE
SLI/SLO
FAILURE MODES
RECOVERY
COST DRIVERS
OWNERS
```

Poi evidenzia in rosso, idealmente su un diagramma o in una tabella, tutti i campi per cui la risposta è:

```text
non lo so
```

Quelli sono rischi reali da investigare.

### Autovalutazione

Dovresti essere in grado di spiegare senza nominare un vendor:

- perché OLTP e analytical serving hanno workload differenti;
- perché ingestion e transformation boundary contano per il replay;
- cosa promettono raw/curated/business layers;
- perché real time è un requisito economico, non estetico;
- differenza tra event time e processing time;
- cosa rappresenta una watermark;
- perché CDC non è ancora stato analitico;
- differenza tra scheduling e readiness orchestration;
- perché `SUCCESS` non garantisce completeness;
- come SLI/SLO descrivono l'esperienza del consumer;
- differenza tra schema evolution e contract evolution;
- cosa significa recovery del dato;
- perché una soluzione può essere contemporaneamente scalabile e sproporzionata.

La frase finale del capitolo è:

> **L'architettura è la sequenza di garanzie e failure boundary attraverso cui un evento del mondo reale diventa un'informazione disponibile per una decisione. Conoscerla significa sapere non soltanto dove si trova il dato, ma quando possiamo fidarci del fatto che sia arrivato intero, aggiornato e recuperabile.**
