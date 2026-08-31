## 12.4 Data lake e lakehouse: flessibilità senza perdere affidabilità

Un **data lake** nasce dall'idea di poter conservare grandi quantità di dati, spesso in formati diversi e con costi di storage relativamente bassi.

Può contenere:

- file CSV e Parquet;
- JSON;
- log applicativi;
- eventi clickstream;
- immagini o altri oggetti;
- dati semi-strutturati;
- estrazioni raw da sistemi operativi.

Questa flessibilità è potente, ma introduce un rischio: se il lake diventa soltanto un deposito di file senza struttura, ownership, catalogo e controlli, trovare il dato giusto può diventare più difficile, non più facile.

Da qui nasce il concetto di **lakehouse**, che cerca di combinare la flessibilità e la scalabilità del lake con proprietà tipiche dei sistemi analitici più strutturati: tabelle governate, transazioni, schema enforcement, qualità, catalogazione e supporto a BI e ML.

Databricks definisce il lakehouse come un sistema che combina benefici di data lake e data warehouse e lo collega frequentemente a un'architettura a livelli che migliora progressivamente qualità e struttura dei dati.

## Medallion architecture: Bronze, Silver, Gold

Un pattern diffuso è la cosiddetta **medallion architecture**.

### Bronze

Contiene dati raw o quasi raw.

Obiettivi principali:

- preservare fedeltà alla sorgente;
- consentire replay e reprocessing;
- mantenere metadata di provenienza;
- evitare trasformazioni irreversibili premature.

### Silver

Contiene dati validati e puliti.

Tipicamente qui avvengono:

- schema enforcement;
- type casting;
- deduplication;
- gestione null;
- normalizzazione;
- gestione record fuori ordine o arrivati in ritardo;
- primi join e arricchimenti.

### Gold

Contiene dati orientati al consumo business.

Tipicamente:

- modelli dimensionali;
- metriche;
- aggregazioni;
- dataset ottimizzati per dashboard e reporting;
- viste di dominio.

Databricks documenta esplicitamente che Bronze, Silver e Gold rappresentano livelli crescenti di qualità e che la Gold layer è normalmente allineata alla business logic e ai requisiti di reporting.

## Caso realistico: il lake che nessuno voleva usare

**NovaMedia** raccoglie eventi da sito web, app mobile, piattaforma video e advertising.

Il team costruisce un data lake e celebra il fatto di avere "tutto il dato in un unico posto".

Dopo un anno contiene oltre 80.000 oggetti e centinaia di directory con nomi come:

```text
/events/new/
/events/new_v2/
/events/new_final/
/events/new_final_fixed/
/mobile/events_backup/
```

Gli analyst iniziano a copiare file nei propri workspace perché non sanno quale sia la versione corretta.

Il problema non è lo storage. È la mancanza di:

- catalogo;
- ownership;
- schema stabile;
- quality checks;
- convenzioni;
- livelli curati.

Il team introduce quindi tre layer:

```text
bronze.raw_events
silver.sessionized_events
gold.content_engagement_daily
```

Il vantaggio non è il nome "medallion". È che ora ogni layer ha un contratto chiaro.

## Un pattern, non una religione

Bronze/Silver/Gold non è obbligatorio e non risolve automaticamente la qualità del dato.

Può essere eccessivo per una startup con tre tabelle e un report settimanale.

Il criterio utile è chiedersi:

> Abbiamo bisogno di separare il dato ricevuto, quello validato e quello pronto per il business?

Se la risposta è sì, un'architettura a livelli può ridurre ambiguità e migliorare debuggabilità.

### Fonti pubbliche

Databricks, *What is the medallion lakehouse architecture?*:
https://docs.databricks.com/gcp/en/lakehouse/medallion

Databricks, *What is a data lakehouse?*:
https://docs.databricks.com/aws/en/lakehouse/
