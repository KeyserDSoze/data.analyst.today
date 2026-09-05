## 13.8 Caso end-to-end — Northstar Mobility e il Tooling Decision Record

**Caso simulato/composito.** Northstar Mobility gestisce servizi di mobilità urbana in **14 città europee**. Il COO chiede “un sistema unico” che copra KPI giornalieri, investigazione delle anomalie, alert operativi e analisi strategiche mensili.

La prima riunione parte dal tool: Excel perché tutti lo conoscono, Python perché è flessibile, BI perché centralizza, streaming perché è “real time”. Nessuna proposta è assurda. Il problema è che **quattro lavori diversi stanno venendo compressi in una sola scelta tecnologica**.

Il team cambia domanda e parte da decisione, frequenza e deadline:

| Need | Consumer | Frequenza | Decision deadline | Metodo |
|---|---|---:|---:|---|
| KPI ufficiali | COO / city manager | giornaliera | 07:30 | aggregazione |
| Diagnosi ad hoc | analyst | quando serve | ore | EDA / drill-down |
| Vehicle availability alert | Operations | continua | < 5 min | regola/anomaly |
| Strategic review | Strategy | mensile | giorni | cohort, pricing, modelli |

La matrice rende subito evidente che “un tool unico” non è un requisito, ma una preferenza introdotta troppo presto.

### Prima i vincoli condivisi, poi le superfici

Qualunque soluzione deve comunque rispettare definizioni metriche comuni, identità coerenti di city/vehicle/trip, controlli su completezza e freshness, access control, storia sufficiente e lineage verso le sorgenti. Questi vincoli arrivano dai Capitoli 11 e 12 e non vengono risolti scegliendo uno strumento.

Da qui il team assegna responsabilità diverse. I KPI giornalieri richiedono logica condivisa e consumo ricorrente: **certified SQL models + BI** è una combinazione naturale. L'investigazione resta più fluida in workspace SQL/notebook. Le analisi strategiche possono usare SQL per preparare il dataset e Python/R per metodi specialistici. Solo l'alert sulla vehicle availability ha una deadline inferiore a cinque minuti e giustifica un percorso a bassa latenza.

Gli spreadsheet non spariscono: restano utili come decision surface locale quando serve discutere scenari. L'AI può assistere query, documentazione e review. Ma nessuno di questi strumenti diventa il backbone soltanto perché è familiare o potente.

La soluzione assume quindi questa forma:

```text
operational sources
        ↓
shared data platform
        ↓
certified SQL models
        ├────────────→ BI: KPI giornalieri
        ├────────────→ analyst workspace: SQL / notebook
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

### Il TDR rende visibile il perché

Per i KPI giornalieri il record può essere molto semplice:

```text
Decision: monitoraggio operativo mattutino
Stage: recurring production
Freshness: entro 07:30
Consumers: COO + city managers
Method: aggregazioni e confronti
Choice: certified SQL models + BI
Reason: riuso, accesso condiviso, refresh e metriche governate
Exit condition: nuova review se la decisione richiede latenza <15 min
```

Per l'alert vehicle availability cambia il requisito:

```text
Decision: intervento operativo sulla disponibilità
Stage: production
Freshness: <5 min
Choice: low-latency event path + alerting
Reason: il ritardo ha costo operativo reale
```

Per Strategy la soluzione resta volutamente più esplorativa:

```text
Decision: investigazione mensile
Stage: exploratory / recurring analysis
Choice: SQL + Python/R/notebook
Serving: risultati sintetici, non notebook come prodotto executive
Exit condition: promuovere metriche stabili nel layer certificato
```

La stessa organizzazione usa quindi più strumenti senza incoerenza. L'incoerenza nascerebbe se ciascun team trasformasse il proprio strumento preferito nell'intera architettura.

### La scelta più importante è sapere quando cambiare

Northstar non registra soltanto cosa usare oggi. Registra i segnali che richiederanno una nuova review: aumento di frequenza, nuovo consumer downstream, maggiore criticità, volume che cambia il runtime, requisito di audit, manutenzione crescente, definizione diventata stabile e condivisa o nuova deadline di latenza.

Questo protegge da due errori opposti. La **premature industrialization** compra piattaforma prima di aver dimostrato valore. L'**accidental production** lascia invece che un prototipo diventi infrastruttura senza accorgersene.

Il risultato non è un “tool winner”, ma un portfolio coerente:

| Responsabilità | Superficie candidata |
|---|---|
| Scenario/interazione | spreadsheet |
| Relational compute vicino al dato | SQL |
| Metodi specialistici | Python/R |
| Laboratorio analitico | notebook |
| Consumo ricorrente | BI |
| Shared execution | data/cloud platform |
| Workflow semplice | low-code/no-code |
| Accelerazione costruzione/review | AI assistita |

La tabella non assegna automaticamente il tool. Ricorda soltanto che ogni superficie deve guadagnarsi una responsabilità concreta.

> **Il problema non è scegliere un vincitore. È assegnare a ogni componente una responsabilità e sapere quale cambiamento ci obbligherà a riassegnarla.**
