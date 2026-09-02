## 18.11 Caso end-to-end: da report ricorrente a capacità analitica operativa

### Caso simulato/composito: Helios Mobility

Helios Mobility è un'azienda europea di micromobilità con circa 4,8 milioni di corse al mese.

Ogni lunedì mattina il management decide:

- come riallocare la flotta tra città;
- dove aumentare manutenzione e charging capacity;
- quali promozioni modificare;
- quali anomalie operative richiedono escalation;
- se il forecast trimestrale resta compatibile con il piano.

Il meeting usa un weekly business review con:

- rides;
- revenue;
- contribution margin;
- fleet availability;
- incident rate;
- retention;
- CAC;
- forecast delle corse.

Esistono molte dashboard.

Il sistema sembra maturo.

In realtà dipende ancora da persone, eccezioni e verifiche manuali.

## Situazione iniziale

Il pacchetto del lunedì richiede quasi due giorni-persona di preparazione distribuiti tra più analyst.

Emergono problemi ricorrenti:

- tre team usano definizioni diverse di `active_rider`;
- Finance riconcilia revenue con uno scarto medio dell'1,7%;
- il forecast viene mantenuto in notebook separati per città;
- una modifica all'app può cambiare tracking senza un consumer impact notice;
- se una sorgente arriva incompleta alle 05:00, il problema viene spesso scoperto nel meeting;
- alcune dashboard vengono refreshate ogni dieci minuti anche se servono una volta al giorno;
- nessuno possiede il weekly review end-to-end.

Helios non ha un problema di assenza di dati.

Ha un problema di **promessa operativa non esplicita**.

## Step 1 — Definire il recurring decision product

Il team non parte da:

> “Quali dashboard dobbiamo rifare?”

Parte da:

> “Quale decisione ricorrente non può permettersi di perdere significato o arrivare con dati non ready?”

Il `Weekly Mobility Review` viene classificato **T2 — business-critical**.

Il suo Analytics Operating Contract definisce:

| Campo | Decisione |
|---|---|
| Consumer | COO, CFO, City Operations |
| Decision owner | COO |
| Semantic owner | Finance per revenue/margin; Operations per fleet availability |
| Product owner | Analytics Platform |
| Criticality | T2 |
| Freshness | previous-day data ready entro 07:00 CET |
| Completeness | ≥99,5% delle ride attese o stato degradato esplicito |
| Finance reconciliation | scarto ≤0,25% prima del board-use |
| Degraded mode | last-known-good + affected-city exclusion + warning |
| Incident escalation | Analytics on-call → owner sorgente → decision owner |
| Change review | semantic diff + consumer impact analysis |
| Retirement review | semestrale |

Il cambiamento più importante non è tecnico.

Ora esiste una **promessa verificabile**.

## Step 2 — Separare ownership

Prima tutti erano “responsabili dei dati”.

Quindi nessuno era davvero accountable.

Il redesign separa:

- **decision owner** — accetta il rischio residuo del weekly review;
- **semantic owners** — decidono il significato delle metriche;
- **product owner** — mantiene pipeline, test, SLO e runbook;
- **source owners** — garantiscono contratti e change notice sulle sorgenti;
- **governance/stewardship** — controlla accesso, lineage e policy comuni.

Quando una metrica cambia, Analytics non decide più unilateralmente la nuova semantica.

## Step 3 — Ridurre l'ambiguità semantica

Il team certifica una singola versione executive di:

- active rider;
- completed ride;
- recognized revenue;
- contribution margin;
- vehicle availability;
- 30-day retention.

Le definizioni includono:

- grain;
- popolazione;
- timezone;
- event/accounting date;
- filtri;
- owner;
- versione;
- data di validità;
- alternative non executive eventualmente ancora esistenti.

Le varianti locali non vengono proibite.

Vengono nominate in modo diverso e non possono presentarsi come `certified executive metric`.

## Step 4 — Costruire SLI, SLO e degraded mode

Prima Helios monitorava soprattutto `job_success`.

Ora controlla anche:

- freshness per sorgente;
- città attese vs città ricevute;
- ride count e payment count;
- uniqueness di `ride_id`;
- quota telemetry late;
- revenue reconciliation;
- distribuzione per città;
- status dei known incident.

Il weekly review espone un **data health header** prima dei KPI.

Esempio:

```text
Freshness: OK
Ride completeness: 99.82%
Payment reconciliation: 99.93%
Known incidents: 1
Affected scope: Valencia telemetry only
Serving state: READY WITH CAVEATS
```

La reliability non è più invisibile.

## Step 5 — Il primo incidente reale del nuovo operating model

Un lunedì alle 05:40 un provider telemetria smette di consegnare parte degli eventi di Milano.

La pipeline termina senza errore tecnico.

Il vecchio sistema avrebbe pubblicato numeri parziali.

Il nuovo sistema rileva:

- city volume -19% rispetto alla baseline;
- active provider count sotto atteso;
- payment count incompatibile con il ride count;
- completeness stimata 82%.

Lo stato diventa:

`PARTIAL — DO NOT USE MILAN RIDE KPI FOR ALLOCATION`.

Il weekly review viene comunque pubblicato alle 07:00 con:

- altre città `READY`;
- Milano esclusa dai confronti operativi;
- last-known-good mostrato come riferimento, chiaramente etichettato;
- incident link e owner;
- forecast non ricalibrato sul dato incompleto.

Il sistema non ha evitato il fallimento della sorgente.

Ha evitato che il fallimento diventasse **una decisione sbagliata silenziosa**.

## Step 6 — Change management semantico

Tre mesi dopo Product modifica `ride_started`.

Prima l'evento era emesso quando il veicolo si sbloccava.

Dopo la modifica viene emesso quando il mezzo supera una soglia di movimento.

Schema e nome restano identici.

È un **semantic breaking change**.

Il Source Contract richiede un change notice.

Il team esegue:

1. impact analysis;
2. dual emission su un campione;
3. confronto vecchio/nuovo per città e device;
4. aggiornamento delle metriche colpite;
5. semantic owner approval;
6. data di efficacia esplicita;
7. comunicazione ai consumer;
8. decisione su backfill vs forward-only.

Il grafico storico non viene lasciato cambiare silenziosamente.

## Step 7 — CI/CD e testing pyramid

Le trasformazioni entrano in version control.

Per i cambi T2 il release gate richiede:

- structural test;
- transformation invariants;
- reconciliation;
- distribution checks;
- semantic diff;
- old-vs-new shadow run;
- approvazione del semantic owner quando necessario;
- rollback/replay plan.

Il team non tratta ogni modifica come high-risk.

Il rigore cresce con la probabilità che il cambiamento alteri una decisione senza essere visibile.

## Step 8 — Self-service e adoption

Helios aveva oltre 140 dashboard relative alle performance città.

Il redesign non cerca di aumentare il numero di utenti o asset.

Costruisce tre prodotti principali:

1. City Operations;
2. Finance Performance;
3. Weekly Mobility Review.

Poi misura la ladder:

**availability → discoverability → usage → effective use → decision embedding → outcome**.

Dopo la migrazione, alcune dashboard duplicate vengono ritirate.

Il numero totale di report diminuisce.

L'adozione migliora perché:

- una quota maggiore dei meeting usa metriche certificate;
- diminuiscono le reconciliation request;
- gli utenti trovano più rapidamente il prodotto autorevole;
- le decisioni operative iniziano da un data-health state comune.

Meno asset, maggiore capacità.

## Step 9 — Cost-to-serve

L'allocazione dei costi mostra che una parte rilevante del compute è assorbita da:

- refresh frequenti su report giornalieri;
- semantic model duplicati per città;
- query esplorative che scansionano raw event history;
- pipeline near-real-time usate da consumer non real-time.

Il team assegna freshness tier differenti:

- fleet incident operations → near-real-time;
- city performance → hourly;
- Finance/weekly review → daily;
- exploratory analysis → on demand.

L'obiettivo non è comprimere il cloud bill in astratto.

È rendere il **cost-to-serve coerente con il valore della latenza**.

## Step 10 — Introdurre agenti senza creare un secondo shadow system

Helios introduce un agente per il triage dei data incident.

L'Agent Operating Profile consente:

- query read-only;
- accesso al semantic layer certificato;
- lineage lookup;
- apertura ticket;
- proposta di decomposizioni;
- sintesi di evidence e alternative hypothesis.

Non consente:

- modifica di metriche;
- write nel warehouse;
- chiusura automatica di incident T2;
- pubblicazione autonoma di causal claim;
- azioni sui sistemi operativi.

## Step 11 — L'incidente dell'agente

Dopo un update del tool di lineage, l'agente inizia a selezionare una vista deprecated che contiene ancora una vecchia definizione di revenue.

Gli eval pre-deploy non avevano coperto quella combinazione.

Il monitoring rileva un aumento dei reconciliation failure nel Verification Bundle.

Il runbook applica:

1. revoca temporanea del lineage tool;
2. agente in `suggestion-only`;
3. blocco degli output finance-related;
4. identificazione dei run già prodotti;
5. re-eval con il nuovo tool;
6. ripristino solo dopo superamento del gate.

La lezione non è “l'agente ha sbagliato”.

È che il sistema possedeva **una capability di ridurre l'autorità prima di aver capito completamente il failure mode**.

## Step 12 — Misurare il successo senza confondere activity con value

Dopo sei mesi, essendo un caso didattico composito, immaginiamo la seguente scorecard:

### Reliability

- incidenti scoperti dagli utenti invece che dal monitoring: forte riduzione;
- finance reconciliation entro SLO: in aumento;
- MTTR dei data incident T2: in diminuzione.

### Semantic consistency

- `active_rider` executive: una sola versione certificata;
- dashboard legacy duplicate: progressivamente ritirate;
- semantic breaking change con notice: tracciate.

### Adoption

- decision process che usano prodotti certificati: in aumento;
- tempo speso a chiedere “quale numero è corretto?”: in diminuzione;
- usage di asset deprecated: verso zero.

### Economics

- cost-to-serve per city performance review: in diminuzione;
- compute near-real-time riservato ai workload che ne hanno bisogno.

### AI operations

- agent run con audit completo: 100% target;
- high-severity unsupported claim: zero tolleranza;
- escalation/abstention monitorate come comportamento desiderato, non come failure automatico.

Il punto non sono i numeri specifici del caso composito.

È che il successo viene misurato lungo **reliability, semantica, adoption, economia e governance**, non soltanto attraverso uptime o quantità di dashboard.

## La lezione

Helios non ha costruito una dashboard migliore.

Ha trasformato una routine critica in un sistema con:

**decisione → tier → ownership → contract → SLO → test → degraded mode → change control → self-service → cost-to-serve → agent governance → learning**.

Questa è la differenza tra automatizzare un output e costruire una capacità organizzativa.

> **Scalare analytics significa rendere esplicito cosa promettiamo, chi ne risponde, come degradiamo quando la promessa non può essere mantenuta e quando abbiamo il diritto di ritirare o cambiare il sistema.**

## Collegamento a un caso pubblico

La Microsoft Fabric Adoption Roadmap tratta l'adozione organizzativa come combinazione di ownership, governance, Center of Excellence, mentoring, supporto, system oversight e change management, non come semplice distribuzione di una piattaforma. È un riferimento utile perché rafforza la stessa idea del caso Helios: la capacità analitica scala quando **persone, processi e tecnologia** evolvono insieme.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap
