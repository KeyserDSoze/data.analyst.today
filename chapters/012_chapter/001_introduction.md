# Capitolo 12 — Data architecture per Data Analyst

## 12.0 Dal dataset al percorso che lo rende disponibile

Nel Capitolo 11 abbiamo costruito l'**Analytical Data Contract**: grain, chiavi, tempo, metriche, trasformazioni e invarianti che permettono a un dataset di conservare il significato analitico promesso. Ora allarghiamo l'inquadratura, perché quel dataset non appare dal nulla.

Prima di arrivare a una query, a un modello semantico o a una dashboard, il dato nasce in un sistema, viene catturato, trasportato, memorizzato, trasformato, pubblicato e infine consumato. Ognuno di questi passaggi può introdurre latenza, perdita di record, duplicazioni, schema incompatibile, dati tardivi, stato parziale, nuovi costi e nuovi failure mode. Per un Data Analyst, capire l'architettura significa quindi saper rispondere a una domanda molto concreta:

> **Quale percorso ha attraversato questo dato prima di diventare il numero che sto usando per decidere?**

La risposta ci serve perché la correttezza della formula è soltanto una parte dell'evidenza. Due query identiche possono avere affidabilità molto diversa se una legge una sorgente operativa incompleta e l'altra un modello curato, riconciliato e pubblicato con uno SLO esplicito.

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

Per ogni passaggio vogliamo conoscere almeno owner, input/output, latenza attesa, freshness e completeness, contract boundary, comportamento in failure, retry/replay/backfill, monitoring e principali cost driver. La mappa non è un diagramma decorativo: deve permettere di distinguere rapidamente un problema business da un problema semantico, di pipeline, di freshness, di serving o di consumer.

### Caso simulato/composito — SwiftDrop e il dashboard corretto ma vecchio

SwiftDrop gestisce consegne urbane. Alle 09:00 il management vede un late-delivery rate del **7,8%**, mentre Operations sostiene che la mattina stia andando molto male. Il KPI è calcolato correttamente, ma il percorso del dato è questo:

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

Alle 09:00 il warehouse contiene quasi esclusivamente consegne del giorno precedente. La metrica è corretta rispetto ai dati disponibili e inutilizzabile rispetto alla decisione. Il failure mode non è nella formula: è nella relazione tra **time-to-decision** e **architecture latency**.

Questa distinzione accompagnerà tutto il capitolo. Non cercheremo l'architettura più moderna, ma l'architettura **minima sufficiente** a soddisfare correttezza, freshness, disponibilità, recovery, sicurezza, costo ed evoluzione futura.

### Dal significato al sistema

Il confine con il Capitolo 11 deve restare netto. Lì chiedevamo:

> Come rappresentiamo correttamente il fenomeno analitico?

Qui chiediamo:

> Quale sistema produce, trasporta e rende disponibile quella rappresentazione con le garanzie necessarie?

Il Capitolo 18 riprenderà governance, ownership e observability a livello organizzativo. In questo capitolo ci basta capire chi possiede un componente, quali dipendenze esistono, quale failure blocca il downstream e come si recupera.

> **L'architettura migliore non è quella con più componenti. È quella in cui il percorso dalla realtà alla decisione è sufficientemente affidabile, osservabile e proporzionato al valore della decisione.**
