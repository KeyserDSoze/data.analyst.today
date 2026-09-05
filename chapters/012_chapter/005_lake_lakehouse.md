## 12.4 Lake, lakehouse e architetture a livelli: distinguere lo stato del dato

Warehouse e lakehouse vengono spesso confrontati come alternative di piattaforma. Per un Data Analyst è più utile chiedere in quale **stato di affidabilità** si trova il dato che sta usando.

Un data lake rende economico conservare grandi quantità di dati, anche semi-strutturati o non ancora modellati. Un lakehouse cerca di aggiungere a quella flessibilità proprietà di gestione e serving più strutturate. Ma il valore analitico non nasce dal nome della piattaforma: nasce dal fatto che il percorso distingua chiaramente dati source-aligned, dati validati e dati modellati per il business.

### Bronze, Silver e Gold come confini di promessa

Databricks descrive la medallion architecture come una progressione di qualità: Bronze conserva dati raw e provenance; Silver applica pulizia, validazione, deduplicazione e normalizzazione; Gold serve dati allineati a business logic, analytics e reporting. Le linee guida correnti insistono anche sulla possibilità di ricostruire i layer downstream a partire dal raw persistito.

Fonti:
- https://docs.databricks.com/aws/en/lakehouse/medallion
- https://docs.databricks.com/aws/en/lakehouse-architecture/reliability/best-practices

Il punto non è il colore. È sapere quale promessa inizia attraversando un boundary.

Nel raw layer ottimizziamo fedeltà, provenance, audit e replay; non promettiamo automaticamente deduplicazione business o metriche corrette. Nel curated layer il dato diventa più composable attraverso schema, controlli, dedup, gestione dei late data e normalizzazione. Nel serving layer entrano facts, dimensions, data mart, aggregazioni e altri asset progettati per decisioni specifiche.

### Caso simulato/composito — NovaMedia e il lake che nessuno vuole interrogare

NovaMedia raccoglie eventi web, mobile, video e advertising. Dopo un anno il lake contiene directory chiamate `new`, `new_v2`, `new_final`, `new_final_fixed` e vari backup. Tutti i dati “esistono”, ma nessuno sa quale dataset sia autorevole, quale schema aspettarsi, quale backfill sia l'ultimo o quale asset abbia superato i controlli.

Gli analyst iniziano a copiare file localmente. Il problema non è il data lake: è l'assenza di **state boundaries e ownership**.

Una struttura leggibile diventa:

```text
bronze.raw_events
        ↓
silver.valid_events
        ↓
gold.content_engagement_daily
```

Ogni transizione ha input, output, test e owner. Se una business rule Gold è sbagliata, Bronze e Silver possono restare intatti e il serving può essere ricostruito.

### Un layer deve guadagnarsi il diritto di esistere

Per un progetto piccolo può bastare:

```text
source snapshot
→ curated analytical table
```

Aggiungere livelli nominali senza responsabilità differenti aumenta soltanto il numero di cose da gestire. Un layer è giustificato quando introduce almeno una boundary utile di durabilità, privacy, schema, qualità, business semantics, performance o access control.

Per ciascun layer la Data Flow Architecture Map dovrebbe poter dire:

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

> **L'architettura a livelli è utile quando rende visibile quanto possiamo fidarci del dato in ciascun punto e quale stato possiamo usare per ricostruire ciò che viene dopo.**
