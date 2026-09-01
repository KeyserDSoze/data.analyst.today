# Capitolo 12 — Data architecture per Data Analyst

## 12.0 Dal dataset al percorso che lo rende disponibile

Nel Capitolo 11 abbiamo costruito l'**Analytical Data Contract**: grain, chiavi, tempo, metriche, trasformazioni e invarianti che permettono a un dataset di conservare il significato analitico promesso.

Ora allarghiamo l'inquadratura.

Quel dataset non appare dal nulla.

Prima di arrivare a una query o a un semantic model, il dato:

1. nasce in un sistema;
2. viene catturato;
3. attraversa una rete o un meccanismo di ingestion;
4. viene memorizzato;
5. trasformato;
6. pubblicato;
7. consumato da persone o sistemi.

Ognuno di questi passaggi può introdurre:

- latenza;
- perdita di record;
- duplicazioni;
- schema incompatibile;
- dati tardivi;
- stato parziale;
- costi;
- dipendenze;
- nuovi failure mode.

Per un Data Analyst, capire l'architettura significa quindi saper rispondere a una domanda molto concreta:

> **Quale percorso ha attraversato questo dato prima di diventare il numero che sto usando per decidere?**

### Il deliverable del capitolo: Data Flow Architecture Map

Useremo una mappa semplice:

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

Per ogni passaggio vogliamo conoscere almeno:

```text
owner
input/output
expected latency
freshness/completeness expectation
schema/contract boundary
failure behavior
retry/replay/backfill
monitoring
cost driver
```

Non è un diagramma decorativo.

È la mappa che permette all'analista di distinguere rapidamente:

- problema business;
- problema semantico;
- problema di pipeline;
- problema di freshness;
- problema di serving;
- problema di consumer.

### Caso simulato/composito — SwiftDrop e il dashboard corretto ma vecchio

SwiftDrop gestisce consegne urbane.

Alle 09:00 il management guarda il late-delivery rate e vede:

```text
7,8%
```

Operations sostiene invece che la mattina stia andando molto male.

Il KPI è calcolato correttamente.

L'indagine mostra però questo flusso:

```text
operational orders DB
        ↓
batch extraction 06:00 / 18:00
        ↓
warehouse
        ↓
daily delivery model
        ↓
BI dashboard
```

Alle 09:00 il warehouse contiene quasi esclusivamente consegne del giorno precedente.

La metrica è corretta rispetto ai dati disponibili e inutilizzabile rispetto alla decisione.

Il failure mode non è nella formula.

È nella relazione tra:

```text
time-to-decision
vs
architecture latency
```

### L'architettura è parte dell'evidenza

Due query identiche possono avere affidabilità molto diversa se una legge:

- una sorgente operativa incompleta;
- una replica in ritardo;
- un raw layer non validato;
- un modello curato con SLO espliciti.

Per questo una frase come:

> “Il dato viene dal database.”

non è sufficiente.

Dobbiamo sapere:

- quale database;
- quale replica o snapshot;
- a quale istante;
- attraverso quale pipeline;
- con quali controlli;
- con quale politica sui dati tardivi;
- con quale stato di affidabilità.

### Il confine con il Capitolo 11

È importante non confondere i due capitoli.

**Capitolo 11**

> Come rappresentiamo correttamente il fenomeno analitico?

**Capitolo 12**

> Quale sistema produce, trasporta e rende disponibile quella rappresentazione con le garanzie necessarie?

Lo star schema, il semantic layer o le metriche non verranno quindi rispiegati da zero. Qui ci interessano soprattutto come **boundary di serving** dentro un flusso più ampio.

### Il confine con il Capitolo 18

Anche governance, ownership e observability torneranno più avanti.

Qui li trattiamo al livello necessario per leggere l'architettura:

- chi possiede un componente;
- quali dipendenze esistono;
- quale failure blocca il downstream;
- come si recupera.

Il Capitolo 18 affronterà invece la capacità organizzativa di gestire tutto questo su scala.

### Principio guida

Non cercheremo l'architettura più moderna.

Cercheremo l'architettura **minima sufficiente** a soddisfare:

- correttezza;
- freshness;
- disponibilità;
- recovery;
- sicurezza;
- costo;
- evoluzione futura.

> **L'architettura migliore non è quella con più componenti. È quella in cui il percorso dalla realtà alla decisione è sufficientemente affidabile, osservabile e proporzionato al valore della decisione.**
