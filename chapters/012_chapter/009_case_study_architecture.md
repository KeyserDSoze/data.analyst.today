## 12.8 Caso reale documentato: Virgin Media O2 e la semplificazione di un data estate complesso

I casi architetturali diventano facilmente racconti astratti pieni di scatole e frecce.

Il percorso di **Virgin Media O2 (VMO2)** è utile perché mostra un problema più concreto: quando un'organizzazione cresce, si fonde e accumula piattaforme, il costo non è soltanto infrastrutturale. Aumentano anche silos, dipendenze, tempi di delivery e difficoltà nel rendere il dato disponibile in modo coerente.

Google Cloud documenta il percorso di VMO2 dopo la fusione tra Virgin Media e O2: l'organizzazione si trovò a gestire molteplici data warehouse, data lake e piattaforme legacy, con problemi di scalabilità, performance, costi e accessibilità del dato.

Fonte principale:
https://cloud.google.com/customers/virgin-media-o2-data-platform-migration

### Il punto di partenza: molti sistemi, molti failure boundary

Prima della modernizzazione, il data estate comprendeva diversi stack costruiti in anni differenti.

Il problema architetturale può essere letto così:

```text
multiple operational systems
        ↓
multiple legacy integration stacks
        ↓
separate warehouses / Hadoop platforms
        ↓
different analytical consumers
```

Ogni piattaforma aggiungeva:

- capacità da gestire;
- competenze specialistiche;
- contratti e licenze;
- percorsi di ingestion differenti;
- silos;
- failure boundary separati.

VMO2 descrive esplicitamente il legacy on-premises come poco agile e costoso, con impatto sul time-to-market e sulla presenza di data silo.

### Non una migrazione unica, ma più transizioni

Il caso documenta un programma pluriennale con più migrazioni importanti.

Tra le piattaforme coinvolte compaiono:

- Hadoop/Hortonworks;
- Netezza;
- Teradata;
- pipeline mobile network;
- altri workload legacy.

Questa è una lezione importante per l'analista:

> **le architetture aziendali reali raramente passano in un weekend da “vecchio” a “nuovo”. Per anni possono esistere percorsi paralleli con garanzie e latenze differenti.**

Durante una transizione dobbiamo sapere quale percorso alimenta ogni decisione.

### Il raw data come punto di semplificazione

VMO2 descrive un'evoluzione verso BigQuery come nucleo del nuovo ambiente, con l'obiettivo di integrare i dati e ridurre i silos.

Nel caso study viene riportato:

> portare i raw data in BigQuery e usarli per costruire capacità sia di data lake sia di data warehouse ha semplificato significativamente l'architettura.

Per il nostro framework, questo significa creare un punto più uniforme tra:

```text
capture
→ durable storage
→ processing
→ analytical products
```

Non perché un solo prodotto risolva automaticamente ogni semantica, ma perché riduce il numero di percorsi infrastrutturali incompatibili da governare.

### Capacità e costo: risultati documentati

Google Cloud riporta che la migrazione di pipeline relative ai dati della rete mobile verso BigQuery e Dataflow ha aumentato la capacità dati del **400%** e ridotto il **TCO del 30%** rispetto alla piattaforma precedente per quel percorso di modernizzazione.

Il case study riporta inoltre una riduzione del TCO di circa il 30% per piattaforme on-premises equivalenti nel percorso complessivo.

Questi numeri sono risultati dichiarati nel caso pubblico, non valori simulati.

Ma la lezione del libro non è:

> “usa BigQuery e risparmierai il 30%”.

La lezione è:

> **consolidare workload e ridurre infrastruttura duplicata può cambiare contemporaneamente capacità, costi e velocità di delivery, ma il risultato dipende dal contesto specifico.**

### Real time dove crea valore

VMO2 cita BigQuery e Dataflow per analisi granulari e insight in tempo reale utili, tra le altre cose, a:

- performance di rete;
- compliance;
- customer experience;
- trend emergenti.

Questo è coerente con la regola della sezione precedente: non serve rendere ogni dato real time. La bassa latenza ha senso dove modifica un processo operativo.

Un close finanziario e un segnale di network performance possono quindi vivere nella stessa piattaforma ma avere SLO differenti.

### Unificazione infrastrutturale non significa una sola semantica

Anche dopo aver consolidato storage e compute, restano problemi analitici come:

- identity resolution;
- metric definitions;
- historical classification;
- data ownership;
- access policy.

Il Capitolo 11 continua quindi a essere necessario.

Un data platform unificato risolve soprattutto:

```text
where/how data flows
```

non automaticamente:

```text
what every business concept means
```

### Il secondo caso VMO2: data contracts

Nel 2025 VMO2 e Google Cloud hanno documentato anche un approccio ai **data contracts** per data products e AI: contratti machine-readable usati come quality and assurance layer affinché i dataset pubblicati siano documentati, affidabili e pronti al consumo.

Fonte:
https://cloud.google.com/blog/products/data-analytics/vmo2-uses-data-contracts-to-build-scalable-ai-and-data-products

Riprenderemo questo punto nella sezione 12.12.

È interessante perché mostra l'evoluzione naturale:

```text
consolidare la piattaforma
→ rendere esplicite le interfacce tra producer e consumer
```

### Costruire la Data Flow Architecture Map del caso

Una versione semplificata del percorso VMO2 può essere letta così:

```text
SOURCES
legacy platforms / network / business systems
        ↓
CAPTURE & MIGRATION
multiple migration and ingestion paths
        ↓
STORAGE / COMPUTE
consolidation around Google Cloud / BigQuery
        ↓
PROCESSING
BigQuery / Dataflow / related managed services
        ↓
DATA PRODUCTS & SERVING
shared analytical products / data sharing
        ↓
CONSUMERS
analytics / operational insights / AI / business teams
```

Per ogni nodo rimangono domande operative:

- chi è owner?
- quale workload è già migrato?
- quale percorso legacy è ancora attivo?
- quale freshness promette?
- come vengono versionate le interfacce?
- cosa succede durante una failure o una migrazione?

### La lezione del caso

L'architettura non è soltanto un diagramma “target state”.

È anche la capacità di governare la transizione tra stati diversi senza perdere affidabilità.

> **Una piattaforma moderna crea valore quando riduce il numero di percorsi fragili tra sorgente e decisione, rende più semplice ricostruire la provenienza e permette a workload diversi di ottenere il livello di capacità e latenza di cui hanno realmente bisogno.**
