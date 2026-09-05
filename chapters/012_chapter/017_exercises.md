## 12.16 Esercizi: diagnosticare il percorso del dato

Gli esercizi non chiedono di scegliere il servizio cloud “migliore”. Chiedono di costruire e criticare una **Data Flow Architecture Map**, partendo dalla decisione e risalendo a latency, completeness, dependency, contract e recovery.

### Esercizio 1 — Il dashboard delle 09:00

Il CEO apre il dashboard ogni mattina alle 09:00.

```text
ERP export 05:00
→ file landing
→ transform 06:00
→ warehouse 06:30
→ semantic refresh 07:00
→ dashboard
```

Oggi il file ERP arriva alle 08:20 ma tutti i task downstream partono agli orari previsti e terminano `SUCCESS` usando il file precedente.

Definisci dependency/readiness condition, freshness SLI/SLO, stato da mostrare sul dashboard, comportamento `BLOCK / STALE / DEGRADE`, alert e owner.

### Esercizio 2 — Full reload o CDC?

Un e-commerce ha **600 milioni di righe ordine** e circa **4 milioni di insert/update giornalieri**. Il full reload dura cinque ore.

Confronta:

**A. full reload**  
**B. initial snapshot + CDC**

Valuta workload sulla sorgente, freshness, delete, ordering, idempotenza, checkpoint, recovery dopo 48 ore di outage e possibilità di ricostruire lo stato. Non assumere che CDC sia automaticamente migliore.

### Esercizio 3 — Pipeline verde, dato incompleto

Arrivano **25 file regionali su 28**. Il codice processa quelli presenti e termina senza errori. Il report globale mostra revenue `-14%`.

Costruisci:

```text
expected completeness SLI:
SLO:
quality gate:
severity:
degraded behavior:
consumer message:
```

Spiega perché il job status non poteva intercettare il problema.

### Esercizio 4 — Event time e late data

Una pipeline streaming calcola finestre di cinque minuti. Tre eventi sono generati alle `10:01`, `10:03`, `10:04`, ma processati alle `10:02`, `10:04`, `10:14`.

Definisci event time, processing time, late data, watermark policy, provisional result e final/reconciled result. Descrivi anche come testeresti eventi early, on-time e late.

### Esercizio 5 — Il cambio schema che non rompe nulla

Il producer mantiene:

```text
speed: number
```

ma cambia l'unità da km/h a m/s.

Spiega perché schema validation può passare, perché il cambiamento è semantic breaking, quale metadata avrebbe dovuto contenere il producer contract, quale plausibility test potrebbe intercettarlo, se serve una nuova versione e quali consumer individueresti tramite lineage.

### Esercizio 6 — Raw, curated e serving

Hai:

```text
raw_events
valid_events
customer_daily_activity
```

Per ciascun asset specifica stato del dato, garanzie presenti e assenti, consumer ammessi, replay source e quality gate. Poi scegli quale useresti per debugging di un evento, dashboard executive e ricostruzione dopo un bug nella business logic.

### Esercizio 7 — Orchestrazione e retry

Un task scrive **730.000 righe**, fallisce e viene ritentato automaticamente. La seconda esecuzione usa `INSERT` puro.

Progetta due strategie sicure scegliendo tra staging + atomic publish, idempotent merge, partition replacement e checkpoint. Per ciascuna spiega come verificheresti il risultato recuperato.

### Esercizio 8 — SLO per due user journey

Lo stesso dominio serve:

**A. fraud operations**, con azione necessaria entro secondi/minuti;  
**B. monthly Finance report**, con reconciliation e quasi totale completezza.

Progetta SLI/SLO separati per freshness, completeness, availability, reconciliation e recovery. Spiega perché un unico SLO per il dataset sarebbe poco informativo.

### Esercizio 9 — Semantic layer e serving failure

Il warehouse è aggiornato correttamente ma il semantic model non si aggiorna da sei ore.

Disegna:

```text
source → storage → transform → serve → dashboard
```

Indica failure boundary, SLI violato, comportamento last-known-good, timestamp da mostrare e quali consumer possono continuare a lavorare interrogando un layer precedente certificato.

### Esercizio 10 — Architecture review

Un report viene consultato da 20 persone una volta al giorno. Il team propone streaming sub-second, multi-region active-active, cluster always-on, sette giorni di replay e refresh continuo.

Valuta decision deadline, cost of lateness, cost of failure, RTO/RPO necessari, alternative più semplici e trigger futuri che giustificherebbero maggiore complessità.

### Esercizio 11 — Caso VMO2

Usando il caso pubblico Virgin Media O2, identifica almeno cinque motivi per cui consolidare piattaforme può creare valore oltre al costo del compute. Spiega poi perché “unificare la piattaforma” non equivale ad “unificare la semantica”.

### Esercizio 12 — Contract evolution end-to-end

Un producer aggiunge `battery_health` e successivamente cambia il tipo di `device_state`.

Per ogni modifica stabilisci se è additive, structural breaking o semantic breaking e definisci comportamento dell'ingestion, auto-evolve/rescue/fail, versioning, consumer notification, impact analysis ed eventuale backfill.

### Esercizio 13 — Recovery dopo una business rule sbagliata

Scopri che `net_revenue` ha sottratto due volte un tipo di refund per **43 giorni**. La pipeline oggi funziona perfettamente.

Disegna:

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

Indica quali layer ricostruire e quale raw/curated source usare.

### Esercizio 14 — Costruisci la Data Flow Architecture Map

Scegli un dataset reale o un dominio che conosci e completa:

```text
DECISION / CONSUMER
SOURCE
CAPTURE
TRANSPORT
STORAGE
TRANSFORM
SERVE
CONTRACT BOUNDARIES
LINEAGE
SLI/SLO
FAILURE MODES
RECOVERY
COST DRIVERS
OWNERS
```

Evidenzia tutti i campi per cui la risposta è `non lo so`: sono rischi reali da investigare.

### Autovalutazione

Alla fine del capitolo dovresti saper spiegare senza rifugiarti nel nome di un vendor perché system of record e analytical serving hanno responsabilità diverse; perché il replay dipende da dove preserviamo il dato; perché i layer rappresentano stati di affidabilità; perché real time è un requisito economico; come event time, watermark e late data influenzano la completezza; perché CDC non è ancora stato analitico; perché readiness vale più del calendario; come gli SLO descrivono l'esperienza del consumer; come contract evolution e recovery proteggono i downstream; e perché un'architettura può essere scalabile ma sproporzionata.

La transizione al Capitolo 13 nasce proprio da qui. Dopo aver imparato che ogni componente deve guadagnarsi il diritto di esistere attraverso una garanzia necessaria, possiamo applicare lo stesso principio agli strumenti del lavoro analitico: **non scegliere una tecnologia perché è nuova, potente o diffusa, ma perché è la complessità minima sufficiente per il problema e per il suo lifecycle reale**.

> **L'architettura è la sequenza di garanzie e failure boundary attraverso cui un evento del mondo reale diventa informazione utilizzabile. Conoscerla significa sapere non soltanto dove si trova il dato, ma quando possiamo fidarci del fatto che sia arrivato intero, aggiornato e recuperabile.**
