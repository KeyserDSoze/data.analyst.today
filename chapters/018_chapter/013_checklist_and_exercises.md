## 18.12 Analytics Operating Contract, gate ed esercizi

Questo capitolo non termina con una checklist di tecnologie.

Termina con una domanda più impegnativa:

> **Questa analisi ricorrente ha davvero il diritto di diventare un servizio operativo?**

Industrializzare troppo presto crea infrastruttura per domande ancora instabili.

Industrializzare troppo tardi lascia decisioni critiche dipendenti da memoria, file locali e controlli manuali.

Serve quindi un gate.

## Promotion Gate: da analisi a prodotto operativo

Prima di promuovere un workflow chiediamo:

### Decisione

- Quale decisione ricorrente supporta?
- Chi è il decision owner?
- Con quale frequenza viene presa?
- Qual è il costo del dato sbagliato, in ritardo o non disponibile?
- Che cosa succede se il prodotto scompare per una settimana?

### Stabilità del significato

- Metriche, grain, popolazione e tempo sono abbastanza stabili?
- Esiste un semantic owner?
- Le varianti legittime sono nominate in modo distinto?
- I principali consumer condividono il significato?

### Scala e ripetizione

- Il processo è ricorrente?
- Viene usato da più persone o sistemi?
- Ricostruirlo manualmente ha un costo significativo?
- Gli errori manuali hanno già prodotto rischio o ritardo?

### Governabilità

- Possiamo testarlo?
- Possiamo monitorarlo?
- Possiamo definirne degraded mode e rollback/recovery?
- Possiamo identificare i downstream consumer?
- Possiamo versionare semantic e structural change?

Se le risposte sono immature, la scelta corretta può essere:

`KEEP EXPLORATORY`.

L'automazione non è sempre una promozione.

## Analytics Operating Contract

Quando il workflow supera il Promotion Gate, il contratto minimo può contenere:

### 1. Purpose e consumer

- recurring decision;
- consumer;
- decision cadence;
- decision deadline.

### 2. Criticality

- `T0 Exploratory`;
- `T1 Team`;
- `T2 Business-critical`;
- `T3 High-consequence`.

Il tier determina quanto rigore è proporzionato.

### 3. Ownership

- decision owner;
- semantic/metric owner;
- product/technical owner;
- source owner;
- governance/steward;
- escalation owner.

### 4. Product boundary

- input autorevoli;
- output;
- grain;
- semantic interface;
- consumer supportati;
- consumer fuori scope.

### 5. Reliability contract

- SLI;
- SLO;
- freshness;
- completeness;
- reconciliation;
- availability;
- error budget;
- latency se decision-critical.

### 6. Serving states

Definire esplicitamente gli stati che il consumer può vedere:

- `READY`;
- `READY WITH CAVEATS`;
- `STALE BUT SERVABLE`;
- `PARTIAL`;
- `BLOCKED`.

Per ogni stato devono essere chiari:

- cosa può essere usato;
- cosa non può essere usato;
- quale fallback esiste;
- chi può accettare il rischio residuo.

### 7. Testing strategy

Copertura almeno dei failure mode rilevanti attraverso:

- source contract test;
- structural test;
- transformation invariants;
- reconciliation;
- distribution/data-health check;
- semantic test;
- decision/consumer test;
- recovery test.

Ogni test deve avere disposition:

- `BLOCKING`;
- `WARNING`;
- `INFORMATIONAL`.

### 8. Observability e incident response

- monitor;
- alert actionability;
- severity;
- on-call/escalation;
- runbook;
- MTTR target quando rilevante;
- incident communication;
- postmortem;
- data repair/replay.

### 9. Change e compatibility

- versioning;
- technical diff;
- semantic diff;
- consumer impact analysis;
- notice period;
- shadow/dual run;
- backfill/forward-only decision;
- rollback/replay plan;
- deprecation policy.

### 10. Adoption

Misurare la ladder:

**availability → discoverability → usage → effective use → decision embedding → outcome**.

Evitare di chiamare `success` il solo numero di utenti.

### 11. Economics

- cost allocation;
- cost-to-serve;
- freshness/latency premium;
- anomaly detection sui costi;
- unit economics;
- capacity/budget owner.

### 12. AI/agent profile, se presente

- purpose;
- model/tool/context configuration;
- data boundary;
- permission boundary;
- autonomy level;
- eval suite;
- runtime/action budget;
- stop condition;
- escalation;
- audit;
- change/re-eval trigger;
- revoke/retire path.

### 13. Lifecycle

- review cadence;
- ownership transfer;
- deprecation state;
- retirement trigger;
- successor;
- archival/audit requirement.

## Operating Readiness Gate

Un prodotto può uscire dal gate come:

### READY TO OPERATE

Ownership, reliability, monitoring, change e recovery sono coerenti con il tier.

### READY WITH EXPLICIT DEBT

Il prodotto può operare, ma esistono gap accettati da un owner e con scadenza.

### SHADOW / LIMITED MODE

Il prodotto deve produrre output in parallelo o per consumer limitati prima della promozione.

### NOT READY

Il failure cost è troppo alto rispetto ai controlli disponibili.

### KEEP EXPLORATORY

La domanda o la semantica non sono abbastanza stabili da meritare industrializzazione.

Questa ultima risposta è importante.

> **Non tutto ciò che può essere automatizzato merita di diventare infrastruttura.**

## Esercizio 1 — Il report fragile

Ogni mattina alle 08:00 un report commerciale viene inviato a 200 manager.

Negli ultimi tre mesi:

- è arrivato in ritardo 7 volte;
- due volte ha mostrato dati incompleti;
- nessuno sa quale versione di `pipeline_coverage` sia ufficiale;
- il processo costa circa €9.000 al mese;
- il 60% dei destinatari non apre mai il report.

Costruire un Analytics Operating Contract che includa:

1. recurring decision;
2. criticality tier;
3. ownership;
4. SLI/SLO;
5. serving states;
6. testing strategy;
7. adoption ladder;
8. cost-to-serve;
9. retirement trigger.

Domanda finale:

> il prodotto va migliorato, ridimensionato o ritirato?

## Esercizio 2 — Tutto verde, ma il numero è sbagliato

Una pipeline `customer_health` mostra:

- job success 100%;
- freshness entro SLO;
- schema invariato;
- null rate stabile;
- row count nel range atteso.

Tuttavia, il team Customer Success scopre che `renewal_date` è stata ridefinita dal CRM come data prevista invece che data contrattuale.

Progettare:

- failure-mode classification;
- test che avrebbe potuto intercettarlo;
- semantic diff;
- blast-radius analysis;
- serving state durante l'incidente;
- comunicazione ai consumer;
- recovery/backfill.

## Esercizio 3 — Error budget consumato

Una dashboard executive T2 ha SLO di readiness del 99% dei giorni lavorativi.

Nel trimestre corrente il budget di failure è quasi esaurito.

Il team propone comunque tre nuove feature che aumentano complessità e dipendenze.

Decidere:

- se congelare feature work;
- quali cause del failure budget affrontare;
- quali SLI verificare;
- chi deve accettare un eventuale cambio di SLO;
- come evitare che `99%` diventi un numero rituale scollegato dalla decisione.

## Esercizio 4 — Self-service ad alta adozione, bassa efficacia

Una piattaforma analytics ha:

- 2.400 utenti registrati;
- 61% utenti attivi mensili;
- 490 dashboard;
- 38 metriche certificate;
- 74 metriche duplicate non certificate;
- 11 incidenti dati al mese;
- quattro ore medie di riconciliazione prima del monthly business review.

Costruire una scorecard che distingua:

- availability/discoverability;
- usage;
- effective use;
- decision embedding;
- reliability;
- semantic consistency;
- business outcome;
- cost efficiency.

Quali metriche potrebbero diminuire mentre il sistema migliora?

## Esercizio 5 — Un agente entra in produzione

Un agente può:

- interrogare il warehouse;
- generare SQL;
- leggere lineage;
- produrre grafici;
- inviare una sintesi;
- aprire ticket di data incident.

Prima versione: suggestion-only.

Seconda versione: può anche sospendere automaticamente una campagna marketing fino a €500.000 al mese.

Per entrambe costruire l'Agent Operating Profile:

- criticality;
- data/tool boundary;
- authority;
- eval;
- runtime/action budget;
- monitoring;
- stop condition;
- escalation;
- rollback/revoke;
- re-eval trigger;
- retirement.

Spiegare perché il secondo agente non è soltanto “la prima versione con un tool in più”.

## Esercizio 6 — Change management umano

Una nuova versione del semantic layer è tecnicamente migliore ma cambia:

- nomi di alcune metriche;
- navigation path;
- workflow usato da Finance;
- export disponibile agli utenti;
- ownership di due data product.

La CI è tutta verde.

Progettare il change plan considerando:

- consumer impact;
- training/support;
- dual run;
- migration deadline;
- deprecation;
- feedback;
- resistance;
- rollback.

La Microsoft Fabric Adoption Roadmap sottolinea che il change management analytics riguarda anche l'impatto sulle persone e sui processi, non soltanto il deploy tecnico.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-change-management

## Esercizio 7 — Il prodotto che nessuno vuole spegnere

Una tabella certificata `customer_360_v1`:

- ha un successore `customer_360_v2` da 14 mesi;
- costa €18.000 al mese;
- riceve ancora il 7% delle query;
- non ha owner attivo;
- contiene due definizioni legacy non più supportate;
- è usata da tre job notturni di cui nessuno conosce il business owner.

Progettare un retirement plan:

1. lineage/discovery;
2. consumer classification;
3. replacement validation;
4. notice;
5. migration;
6. access restriction progressiva;
7. archival/audit;
8. shutdown;
9. post-retirement monitoring.

## Esercizio finale — Operating system senza etichetta

Un marketplace ha cinque processi:

**A.** executive revenue review giornaliero;

**B.** forecast trimestrale aggiornato mensilmente;

**C.** fraud decision in pochi secondi;

**D.** notebook una tantum per valutare una nuova categoria;

**E.** agente che triagea anomalie e può aprire incident.

Per ciascuno decidere:

- se merita un Analytics Operating Contract;
- criticality tier;
- ownership;
- reliability target;
- testing depth;
- degraded mode;
- change process;
- cost model;
- adoption/outcome metric;
- AI governance se rilevante;
- retirement/review cadence.

L'obiettivo non è assegnare più governance a tutto.

È assegnare **il minimo controllo sufficiente al costo del failure**.

## Chiusura del capitolo

Il percorso completo è:

**analisi → asset → prodotto → servizio operativo → capacità organizzativa**.

A ogni passaggio cresce la necessità di esplicitare:

**promessa → owner → failure boundary → controllo → recovery → costo → lifecycle**.

Un'organizzazione matura non dipende da un analyst eroico che ricorda tutte le eccezioni.

E non cerca neppure di eliminare ogni giudizio umano attraverso l'automazione.

Costruisce un sistema in cui il giudizio importante è posizionato nei punti giusti e il resto del processo rende visibili le condizioni in cui quel giudizio deve essere esercitato.

> **La vera scalabilità non è fare più analisi con le stesse persone. È fare in modo che una decisione continui a ricevere evidenza affidabile anche quando cambiano dati, persone, software, agenti e organizzazione.**
