## 12.12 Producer data contracts e schema evolution: cambiare l'interfaccia senza sorprendere i consumer

Nel Capitolo 11 abbiamo creato un **Analytical Data Contract** per specificare il significato di una trasformazione analitica.

Qui usiamo il termine *data contract* in un senso diverso e complementare:

> **l'interfaccia tra chi produce un dataset o evento e chi lo consuma downstream.**

Questa interfaccia può includere:

- schema;
- tipi;
- nullability;
- chiavi;
- semantica dei campi;
- quality expectation;
- freshness;
- ownership;
- policy di evoluzione.

### Due contract da non confondere

**Producer data contract — Capitolo 12**

```text
“Questo è ciò che la sorgente promette di pubblicare.”
```

**Analytical Data Contract — Capitolo 11**

```text
“Questo è ciò che il modello analitico promette di rappresentare.”
```

Esempio:

```text
producer contract:
order.status enum, currency ISO, updated_at semantics

analytical contract:
net revenue per valid order line, refund policy, point-in-time product category
```

Entrambi servono perché una pipeline può rispettare perfettamente lo schema sorgente e costruire comunque una metrica semanticamente sbagliata.

### Caso reale documentato — Virgin Media O2 e i data contracts

Virgin Media O2 e Google Cloud hanno documentato nel 2025 l'uso di data contracts come quality and assurance layer per data products e AI.

I contratti sono descritti come machine-readable e applicati agli asset pubblicati per rendere esplicite aspettative di qualità e affidabilità tra team produttori e consumer.

Fonte:
https://cloud.google.com/blog/products/data-analytics/vmo2-uses-data-contracts-to-build-scalable-ai-and-data-products

Il punto interessante per questo libro è il passaggio da:

```text
“abbiamo documentato la tabella”
```

a:

```text
“la pipeline può verificare automaticamente parte della promessa”
```

### Caso simulato/composito — FleetOne e la stessa colonna con una nuova unità

FleetOne riceve telemetria:

```json
{
  "vehicle_id": "A8821",
  "speed": 74,
  "engine_temp": 91
}
```

Un aggiornamento firmware cambia `speed` da km/h a m/s senza modificare il nome del campo.

Lo schema continua a essere:

```text
speed: number
```

La pipeline non fallisce.

Il dashboard mostra un crollo della velocità media.

Questo è un **semantic breaking change**.

Un semplice schema registry non può proteggerci se il contratto non specifica anche l'unità e il significato.

### Schema evolution: non tutti i cambiamenti hanno lo stesso rischio

Possiamo distinguere almeno:

**Additive**

```text
+ battery_health nullable
```

Potenzialmente backward-compatible per consumer che ignorano il nuovo campo.

**Structural breaking**

```text
customer_id int → struct
column removed
column renamed
```

Può rompere parser e query.

**Semantic breaking**

```text
same column, same type, different unit/meaning
```

Può essere ancora più pericoloso perché il sistema continua a funzionare.

### Caso reale documentato — schema evolution configurabile

Databricks Auto Loader permette di scegliere comportamenti differenti quando incontra nuove colonne, tra cui:

- aggiungerle;
- salvare campi inattesi in rescued data;
- fallire esplicitamente su nuove colonne;
- non evolvere automaticamente lo schema.

Fonte:
https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema

La documentazione recente sottolinea anche che i componenti di un'architettura — connector, parser, engine e dataset — possono gestire schema evolution in modo indipendente.

Fonte:
https://docs.databricks.com/aws/en/data-engineering/schema-evolution

Questo è un punto fondamentale:

> **“La piattaforma supporta schema evolution” non significa che l'intero data flow evolverà in modo compatibile.**

Ogni boundary può reagire diversamente.

### Fail fast vs rescue vs auto-evolve

Non esiste una policy migliore sempre.

**Fail fast** è utile quando:

- lo schema è critico;
- un cambiamento inatteso è ad alto rischio;
- preferiamo fermare la pipeline piuttosto che reinterpretare dati.

**Rescue/quarantine** è utile quando:

- vogliamo continuare a catturare raw data;
- non vogliamo perdere campi inattesi;
- il serving curato deve restare stabile.

**Auto-evolve** può essere utile per cambiamenti additivi controllati.

L'importante è che la policy sia scelta, non ereditata inconsapevolmente dal default del tool.

### Compatibilità come proprietà end-to-end

Una nuova colonna può essere backward-compatible nel raw layer e breaking nel BI model se un consumer usa `SELECT *` o un export posizionale.

Per questo l'impact analysis deve attraversare la lineage:

```text
producer change
→ ingestion
→ storage schema
→ transformations
→ serving
→ consumers
```

La compatibilità non appartiene soltanto alla sorgente.

### Versionare quando il cambiamento cambia il significato

Una modifica semantica importante può richiedere:

```text
v1 → deprecation period → v2
```

con:

- data di entrata in vigore;
- consumer da migrare;
- mapping tra vecchia e nuova semantica;
- eventuale backfill;
- periodo di convivenza.

Non bisogna versionare ogni colonna aggiunta.

Bisogna evitare i **breaking change nascosti**.

### Campo della Data Flow Architecture Map

Per ogni producer boundary annotiamo:

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

### Regola operativa

Prima di cambiare un producer chiediamo:

1. chi consuma questo asset?
2. il cambiamento è additive, structural breaking o semantic breaking?
3. quale componente può adattarsi automaticamente?
4. adattarsi automaticamente significa anche restare semanticamente corretto?
5. serve versione o deprecation window?
6. possiamo rilevare automaticamente la violazione del contract?

> **Schema evolution è la capacità tecnica di continuare a leggere dati che cambiano. Contract evolution è la disciplina con cui decidiamo quali cambiamenti i consumer possono accettare senza perdere il significato o rompere il servizio.**
