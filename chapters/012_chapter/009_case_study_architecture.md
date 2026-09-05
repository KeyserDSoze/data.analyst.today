## 12.8 Caso reale documentato: Virgin Media O2 e la semplificazione di un data estate complesso

I casi architetturali diventano facilmente diagrammi astratti. Il percorso di **Virgin Media O2 (VMO2)** è utile perché mostra un problema più concreto: dopo una fusione e anni di crescita, l'organizzazione non eredita soltanto più dati, ma anche più piattaforme, skill specialistiche, percorsi di ingestion, silos e failure boundary.

Google Cloud documenta che, dopo la fusione tra Virgin Media e O2, VMO2 avviò un programma pluriennale per consolidare un data estate composto da più data warehouse, Hadoop platform e stack legacy. Il legacy on-premises viene descritto come poco agile, costoso e causa di data silo e time-to-market più lento.

Fonte principale: https://cloud.google.com/customers/virgin-media-o2-data-platform-migration

### La vera difficoltà: convivere con più stati dell'architettura

Il programma non è una migrazione “big bang”. Il caso cita più transizioni che coinvolgono Hadoop/Hortonworks, Netezza, Teradata, pipeline della rete mobile e altri workload legacy.

Questa è una lezione importante per l'analista: **target architecture e current architecture possono convivere per anni**. Nello stesso periodo, due KPI possono attraversare percorsi con latency, qualità e recovery differenti. Sapere che “l'azienda usa BigQuery” non basta; dobbiamo sapere quale flusso alimenta la decisione che stiamo osservando.

Una lettura semplificata è:

```text
multiple operational systems
        ↓
multiple legacy integration paths
        ↓
legacy warehouses / Hadoop platforms
        ↓
different analytical consumers

                TRANSITION
                    ↓
more consolidated capture / storage / processing
                    ↓
shared analytical products and serving
```

### Consolidare riduce percorsi, non sostituisce la semantica

VMO2 descrive BigQuery come nucleo di un ambiente più integrato. Portare raw data in un punto più uniforme e usarlo per capacità di lake e warehouse riduce il numero di percorsi infrastrutturali incompatibili da mantenere.

Nel percorso relativo ai dati della rete mobile, Google riporta che la migrazione verso **BigQuery e Dataflow** ha aumentato la capacità dati del **400%** e ridotto il **TCO del 30%** rispetto alla piattaforma precedente. Sono risultati dichiarati nel caso pubblico, non benchmark universali.

La lezione quindi non è “usa BigQuery e risparmierai il 30%”. È che eliminare infrastruttura duplicata e consolidare workload può migliorare contemporaneamente capacità, costi e velocità di delivery quando il contesto lo consente.

La piattaforma unificata non risolve però automaticamente identity resolution, metric definition, classificazioni storiche, ownership o access policy. In altre parole:

```text
unify where/how data flows
≠
unify what business concepts mean
```

Per questo il Capitolo 11 resta indispensabile.

### Real time soltanto dove cambia l'azione

VMO2 cita BigQuery e Dataflow per insight granulari e real-time su network performance, compliance, customer experience e trend emergenti. Questo rafforza il principio del capitolo: un segnale operativo di rete e un close finanziario possono vivere nella stessa piattaforma con SLO diversi.

### Dalla piattaforma ai contratti

Nel dicembre 2025 VMO2 e Google Cloud hanno documentato anche l'uso di **data contracts** machine-readable come quality and assurance layer per i data product e gli use case AI.

Fonte: https://cloud.google.com/blog/products/data-analytics/vmo2-uses-data-contracts-to-build-scalable-ai-and-data-products/

L'evoluzione è significativa:

```text
ridurre i percorsi infrastrutturali
→ rendere esplicite le interfacce producer-consumer
```

Il caso mostra quindi che la modernizzazione non termina con il target state. Deve continuare con ownership, contract, SLO e recovery dei prodotti che viaggiano sulla piattaforma.

> **Una piattaforma moderna crea valore quando riduce il numero di percorsi fragili tra sorgente e decisione e rende più semplice capire quale percorso, quale garanzia e quale stato stanno alimentando ogni consumer durante la transizione.**
