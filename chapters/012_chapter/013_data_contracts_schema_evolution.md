## 12.12 Producer data contracts e schema evolution: cambiare l'interfaccia senza sorprendere i consumer

Nel Capitolo 11 abbiamo usato l'**Analytical Data Contract** per specificare ciò che un modello analitico promette di rappresentare. Qui il termine *data contract* riguarda un'altra boundary: l'interfaccia tra chi produce un dataset o evento e chi lo consuma downstream.

Un producer contract può includere schema, tipi, nullability, chiavi, semantica dei campi, unità, quality expectation, freshness, ownership e policy di evoluzione. I due contratti sono complementari:

```text
producer contract
→ “questo è ciò che la sorgente promette di pubblicare”

analytical contract
→ “questo è ciò che il modello promette di rappresentare”
```

Una pipeline può rispettare perfettamente il primo e costruire comunque una metrica sbagliata nel secondo.

### Caso reale documentato — Virgin Media O2 e i data contracts

Nel dicembre 2025 Virgin Media O2 e Google Cloud hanno descritto contratti machine-readable usati come **quality and assurance layer** per data product e AI, con l'obiettivo di rendere i dataset pubblicati documentati, affidabili e pronti al consumo.

Fonte: https://cloud.google.com/blog/products/data-analytics/vmo2-uses-data-contracts-to-build-scalable-ai-and-data-products/

Il passaggio importante è da documentazione passiva a promessa almeno in parte verificabile automaticamente.

### Caso simulato/composito — FleetOne e la stessa colonna con una nuova unità

FleetOne riceve telemetria con un campo `speed: number`. Un aggiornamento firmware cambia l'unità da km/h a m/s senza modificare nome o tipo.

Lo schema continua a essere valido. La pipeline non fallisce. Il dashboard mostra un crollo della velocità media.

Questo è un **semantic breaking change**. Un registry che conosce soltanto nome e tipo della colonna non può proteggerci se il contract non dichiara anche unità e significato.

### Non tutti i cambiamenti hanno lo stesso rischio

Una nuova colonna nullable può essere additive e backward-compatible. Rimuovere o rinominare una colonna può essere structural breaking. Cambiare il significato mantenendo lo stesso schema può essere semantic breaking ed essere persino più pericoloso, perché tutto continua a funzionare.

Databricks Auto Loader rende esplicita questa scelta tecnica con modalità diverse per l'evoluzione dello schema: aggiunta controllata di colonne, rescue dei campi inattesi, fail on new columns o nessuna evoluzione automatica.

Fonti:
- https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema
- https://docs.databricks.com/aws/en/data-engineering/schema-evolution

Il punto architetturale è che ogni componente — connector, parser, storage, transform, semantic model — può reagire in modo diverso. **“La piattaforma supporta schema evolution” non significa che il data flow resti compatibile end-to-end.**

### Fail, rescue o evolve sono policy di rischio

Possiamo preferire fail fast quando un cambiamento inatteso è ad alto rischio; rescue/quarantine quando vogliamo continuare a catturare raw data senza pubblicare automaticamente il nuovo significato; auto-evolve per cambiamenti additivi controllati.

Quando la semantica cambia davvero può servire una transizione versionata:

```text
v1
→ deprecation window
→ v2
```

con consumer da migrare, data di entrata in vigore, eventuale backfill e mapping tra vecchia e nuova definizione.

Nella Data Flow Architecture Map annotiamo:

```text
contract owner:
schema/version:
semantic metadata:
quality/freshness promises:
compatibility policy:
allowed additive changes:
breaking-change process:
deprecation window:
consumer notification:
lineage/impact analysis:
```

> **Schema evolution è la capacità tecnica di continuare a leggere dati che cambiano. Contract evolution è la disciplina con cui decidiamo quali cambiamenti i consumer possono accettare senza rompere il servizio o, peggio, mantenendolo verde mentre cambia il significato.**
