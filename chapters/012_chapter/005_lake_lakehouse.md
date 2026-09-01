## 12.4 Lake, lakehouse e architetture a livelli: distinguere lo stato del dato

Un data lake nasce dalla possibilità di conservare grandi quantità di dati, anche semi-strutturati o non ancora modellati, in storage relativamente economico.

Un lakehouse cerca di combinare questa flessibilità con proprietà tipiche di un ambiente analitico più strutturato:

- tabelle governate;
- schema e transazioni;
- affidabilità;
- performance analitica;
- supporto a BI e ML.

Per il Data Analyst, però, la domanda più utile non è:

> warehouse o lakehouse?

È:

> **In quale stato si trova il dato che sto usando? È source-aligned, validato o già modellato per il business?**

### Caso reale documentato — la medallion architecture come crescita della qualità

Databricks descrive Bronze, Silver e Gold come livelli in cui la qualità del dato aumenta progressivamente:

- Bronze preserva dati raw e provenance;
- Silver applica pulizia, validazione, deduplicazione e normalizzazione;
- Gold contiene dati allineati a business logic, analytics e reporting.

Fonte: https://docs.databricks.com/aws/en/lakehouse/medallion

Il concetto importante non è il colore.

È la separazione tra **stati del dato con garanzie differenti**.

### Bronze: fedeltà e replay

Un raw/source-aligned layer ottimizza:

- fedeltà alla sorgente;
- metadata di ingestion;
- audit;
- reprocessing;
- debugging.

Non promette automaticamente:

- deduplicazione business;
- chiavi conformate;
- metriche corrette;
- usability per dashboard.

Un analyst che interroga Bronze deve sapere che sta entrando prima del confine di curation.

### Silver: rendere il dato composable

Un curated layer può occuparsi di:

- tipi e schema;
- record invalidi;
- dedup/version handling;
- late data;
- identity resolution tecnica;
- normalizzazione di timezone/unità;
- join di riferimento.

Qui il dato diventa più adatto a essere combinato e riutilizzato.

Ma non significa ancora che ogni decisione business debba leggere Silver direttamente.

### Gold: serving orientato alle decisioni

Il layer business/serving può contenere:

- facts e dimensions;
- data marts;
- aggregazioni;
- feature o dataset curati;
- input al semantic layer.

Le regole semantiche precise rimangono materia del Capitolo 11.

In questa architettura Gold significa soprattutto:

> **questo asset ha superato boundary di qualità e trasformazione sufficienti per uno specifico tipo di consumo.**

### Caso simulato/composito — NovaMedia e il lake che nessuno vuole interrogare

NovaMedia raccoglie eventi web, mobile, video e advertising.

Dopo un anno il lake contiene directory come:

```text
/events/new/
/events/new_v2/
/events/new_final/
/events/new_final_fixed/
/mobile/events_backup/
```

Tutti i dati “esistono”.

Nessuno sa però:

- quale dataset sia autorevole;
- quale schema aspettarsi;
- quale sia l'ultimo backfill;
- quali file abbiano superato controlli;
- quale tabella sia appropriata per il reporting.

Gli analyst iniziano a copiare file localmente.

Il problema non è il data lake.

È l'assenza di **state boundaries e ownership**.

Una struttura più chiara diventa:

```text
bronze.raw_events
        ↓
silver.valid_events
        ↓
gold.content_engagement_daily
```

Ogni transizione ha input, output, test e owner.

### Layering come recovery strategy

La separazione a livelli ha anche valore durante un incidente.

Se una nuova business rule in Gold è sbagliata:

```text
Bronze: intatto
Silver: intatto
Gold: da ricostruire
```

Possiamo correggere la logica e riprocessare senza richiedere nuovamente i dati alla sorgente.

Le best practice di affidabilità Databricks collegano esplicitamente layer raw/curated/final alla possibilità di rebuild e recovery.

Fonte: https://docs.databricks.com/aws/en/lakehouse-architecture/reliability-best-practices

### Non moltiplicare layer per moda

Per un progetto piccolo potrebbe bastare:

```text
source snapshot
→ curated analytical table
```

Aggiungere cinque livelli nominali senza responsabilità differenti crea solo più cose da gestire.

Un layer merita di esistere se introduce almeno una boundary utile:

- durability;
- privacy;
- schema;
- qualità;
- business semantics;
- performance;
- access control.

### Campo della Data Flow Architecture Map

Per ogni layer annotiamo:

```text
state of data:
what guarantees begin here:
what guarantees do NOT exist yet:
upstream replay source:
quality gates:
retention:
owner:
allowed consumers:
```

### Regola operativa

Quando vediamo nomi come `raw`, `bronze`, `silver`, `curated`, `gold`, `serving`, chiediamo:

> **Quale promessa cambia davvero attraversando questo confine?**

Se nessuno sa rispondere, il layer è probabilmente una convenzione nominale e non una vera architettura.

> **L'architettura a livelli è utile quando rende visibile lo stato di affidabilità del dato e permette di ricostruire i layer downstream senza perdere la sorgente.**
