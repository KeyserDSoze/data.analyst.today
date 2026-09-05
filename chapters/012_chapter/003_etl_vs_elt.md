## 12.2 ETL ed ELT: decidere dove trasformare senza perdere replayability

ETL ed ELT vengono spesso presentati come due scuole contrapposte. Per il nostro scopo sono invece due modi di posizionare una **transformation boundary**: dove applichiamo una trasformazione e quale versione del dato conserviamo per poter verificare, correggere o rifare quel lavoro.

Nel pattern ETL una parte significativa della trasformazione precede il caricamento nella destinazione analitica; nell'ELT il dato viene prima caricato nella piattaforma analitica e trasformato dopo. La differenza operativa conta, ma è più utile leggere il percorso così:

```text
capture
→ preserve
→ validate
→ conform
→ apply business logic
→ serve
```

Alcune trasformazioni devono avvenire presto per ragioni di sicurezza o compliance, per esempio tokenizzazione o rimozione di dati che non possiamo conservare. Altre — deduplicazione business, identity resolution, join tra domini, modeling dimensionale, metriche — beneficiano spesso di input durevoli e riprocessabili.

### Caso simulato/composito — MareaPay e il campo eliminato troppo presto

MareaPay riceve payload da un provider di pagamenti. La prima pipeline conserva soltanto `transaction_id`, `amount`, `currency` e `status`, perché sono gli unici campi usati dai report iniziali. Sei mesi dopo il team antifrode scopre che il payload originale conteneva anche authentication method, device signal, risk attributes e timestamp intermedi.

La trasformazione pre-load li aveva eliminati e il provider conserva il dettaglio storico solo per una finestra limitata. La nuova domanda non può essere ricostruita interamente.

L'errore non dimostra che ETL sia sbagliato. Dimostra che una trasformazione irreversibile è stata applicata **prima di aver deciso quale capacità di replay fosse necessaria**.

### Durable landing e failure boundary

Conservare una versione raw o source-aligned può permettere reprocessing, audit, debugging e backfill. Ma raw non significa “pronto per gli analyst”: quel layer ottimizza fedeltà e recuperabilità; il curated layer ottimizza affidabilità analitica.

Le linee guida Databricks sulle pipeline raccomandano di separare, quando possibile, ingestion e trasformazioni downstream, così un failure della business logic non impedisce ai nuovi dati di atterrare e rimanere disponibili per il reprocessing.

Fonte: https://docs.databricks.com/aws/en/ldp/best-practices

La domanda da fare a ogni boundary è semplice:

> **Se questa logica è sbagliata, possiamo ricostruire il risultato corretto?**

La risposta dipende da input conservato, versione del codice, parametri, metadata di ingestion, retention e capacità di backfill. Replayability non giustifica però una retention indiscriminata: audit e recovery vanno bilanciati con minimizzazione dei dati, sicurezza, costo e requisiti normativi.

Nella Data Flow Architecture Map documentiamo almeno:

```text
input preserved? sì/no
transformation location:
irreversible operations:
retention:
replay source:
backfill capability:
code/version reference:
failure blocks capture? sì/no
```

> **ETL vs ELT è una scorciatoia. La vera decisione è dove possiamo permetterci di perdere reversibilità e quale stato dobbiamo conservare per correggere l'evidenza quando scopriamo che la logica di ieri era sbagliata.**
