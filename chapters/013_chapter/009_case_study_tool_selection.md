## 13.8 Caso end-to-end — Northstar Mobility e il Tooling Decision Record

**Caso simulato/composito.**

Northstar Mobility gestisce servizi di mobilità urbana in 14 città europee.

Il COO chiede “un sistema unico” per:

- KPI giornalieri;
- investigazione delle anomalie;
- alert operativi;
- analisi strategiche mensili.

La prima riunione parte male.

Una persona propone Excel perché tutti lo conoscono. Un'altra Python perché è più flessibile. BI vuole centralizzare tutto nel dashboard. Engineering propone streaming.

Ognuna delle proposte può essere tecnicamente sensata.

Il problema è che **stanno scegliendo un tool per quattro lavori diversi**.

### 1. Scomporre per decisione e tempo

Il team costruisce questa matrice.

| Need | Consumer | Frequenza | Decision deadline | Metodo |
|---|---|---:|---:|---|
| KPI ufficiali | COO / city manager | giornaliera | 07:30 | aggregazione |
| Diagnosi ad hoc | analyst | quando serve | ore | EDA / drill-down |
| Vehicle availability alert | Operations | continua | < 5 min | regola/anomaly |
| Strategic review | Strategy | mensile | giorni | cohort, pricing, modelli |

Già questa tabella rende poco plausibile una soluzione “tutto nello stesso ambiente”.

### 2. Vincoli comuni

Qualunque combinazione deve però rispettare:

```text
metric definitions condivise
identity di city / vehicle / trip
controlli su completezza e freshness
access control
history sufficiente
lineage verso le sorgenti
```

Questi requisiti arrivano dai Capitoli 11 e 12.

Il tool selection non li sostituisce.

### 3. Valutare le proposte

#### Tutto in spreadsheet

Ottimo per:

- scenari;
- review manuali;
- piccoli estratti.

Debole come backbone perché:

- gli eventi sono numerosi;
- servono refresh affidabili;
- esistono più consumer;
- gli alert non sono un uso naturale;
- la logica ufficiale rischia di duplicarsi.

**Verdetto:** utile come decision surface locale, non come source of truth.

#### Tutto in Python

Ottimo per:

- analisi avanzate;
- simulazione;
- automazione custom.

Debole come unica superficie perché:

- il COO non dovrebbe consumare notebook;
- KPI semplici non richiedono una libreria Python per ogni refresh;
- la semantica rischia di restare dispersa in script diversi.

**Verdetto:** adatto all'analisi specialistica, non a tutto il serving.

#### Tutto in BI

Ottimo per:

- KPI ricorrenti;
- distribuzione;
- drill-down controllato.

Debole per:

- modellistica avanzata;
- investigazione molto fluida;
- ingestion/alert operational real time;
- business logic che dovrebbe vivere upstream.

**Verdetto:** ottimo consumption layer per le domande stabilizzate.

#### Streaming per tutto

Il requisito più urgente è <5 minuti solo per vehicle availability.

Gli altri flussi tollerano 45 minuti, giornaliero o più.

**Verdetto:** usare bassa latenza dove il ritardo cambia l'azione, non come default architetturale.

### 4. Soluzione composita

Il team propone:

```text
operational sources
        ↓
shared data platform
        ↓
certified SQL models
        ├────────────→ BI: KPI giornalieri
        ├────────────→ analyst workspace: SQL/Notebook
        └────────────→ Strategy datasets → Python/R

availability events
        ↓
low-latency path
        ↓
Operations alert

scenario outputs
        ↓
spreadsheet quando serve interazione business
```

L'AI può assistere query, documentazione e review, ma non cambia i confini di ownership.

### 5. Il Tooling Decision Record

Per i KPI giornalieri:

```text
Decision: monitoraggio operativo mattutino
Stage: recurring production
Data scale: multi-city, storico condiviso
Freshness: entro 07:30
Consumers: COO + city managers
Method: aggregazioni e confronti
Choice: certified SQL models + BI
Rejected: spreadsheet backbone, notebook-only
Reason: riuso, accesso condiviso, refresh e metriche governate
Owner: Analytics + data platform
Exit condition: revisione se la decisione richiede latenza <15 min
```

Per l'alert vehicle availability:

```text
Decision: intervento operativo su disponibilità
Stage: production
Freshness: <5 min
Choice: low-latency event path + alerting
Rejected: daily BI refresh
Reason: il ritardo ha costo operativo reale
Exit condition: rivalutare se policy/azione cambia
```

Per Strategy:

```text
Decision: investigazione mensile
Stage: exploratory / recurring analysis
Choice: SQL + Python/R/notebook
Serving: risultati sintetici, non notebook come prodotto executive
Exit condition: promuovere metriche stabili nel layer certificato
```

### 6. Il punto più importante: definire la migrazione prima di averne bisogno

Northstar non decide soltanto quali tool usare oggi.

Definisce i segnali che richiedono una nuova review:

- aumento di frequenza;
- nuovo consumer downstream;
- maggiore criticità;
- volume che cambia il runtime;
- requisito di audit;
- crescita della manutenzione;
- definizione diventata stabile e condivisa;
- nuovo vincolo di latenza.

Questo impedisce due errori opposti:

**premature industrialization**

Costruire troppo prima di dimostrare il valore.

**accidental production**

Lasciare che un prototipo diventi infrastruttura senza accorgercene.

### 7. Tool portfolio invece di tool winner

La maturità non richiede un solo stack per ogni problema.

Richiede un **portfolio coerente**, nel quale ogni ambiente ha un ruolo comprensibile.

| Funzione | Ambiente candidato |
|---|---|
| Scenario/interazione | spreadsheet |
| Relational compute vicino al dato | SQL |
| Metodi specialistici | Python/R |
| Laboratorio analitico | notebook |
| Consumo ricorrente | BI |
| Shared execution | data/cloud platform |
| Workflow semplice | low-code/no-code |
| Accelerazione costruzione/review | AI assistita |

La tabella non assegna il tool automaticamente.

Serve a impedire che ogni team trasformi il proprio strumento preferito nell'intera architettura.

> **Il problema non è scegliere un vincitore. È assegnare a ogni componente una responsabilità e sapere quando quella responsabilità deve cambiare.**
