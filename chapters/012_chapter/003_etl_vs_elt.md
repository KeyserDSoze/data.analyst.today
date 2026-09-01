## 12.2 ETL ed ELT: decidere dove trasformare senza perdere replayability

ETL ed ELT vengono spesso presentati come due scuole contrapposte.

Per un Data Analyst è più utile considerarli come una domanda architetturale:

> **In quale punto del flusso applichiamo una trasformazione e quale versione del dato conserviamo per poterla verificare o rifare?**

### ETL

Nel pattern classico:

```text
Extract
→ Transform
→ Load
```

una parte significativa della trasformazione avviene prima del caricamento nella destinazione analitica.

### ELT

Nel pattern:

```text
Extract
→ Load
→ Transform
```

il dato viene prima portato nella piattaforma analitica e poi trasformato usando il compute disponibile lì.

La crescita di object storage, warehouse cloud e motori scalabili ha reso questo secondo pattern molto comune.

Ma l'acronimo non è la decisione importante.

### Le responsabilità da separare

Una pipeline può essere letta meglio come:

```text
capture
→ preserve
→ validate
→ conform
→ apply business logic
→ serve
```

Alcune trasformazioni devono avvenire presto:

- rimozione/tokenizzazione di dati che non possiamo conservare;
- controlli di formato necessari per ricevere il dato;
- decryption in boundary controllati;
- policy di compliance.

Altre possono essere posticipate:

- deduplicazione business;
- identity resolution;
- join tra domini;
- dimensional modeling;
- metriche.

### Caso simulato/composito — MareaPay e il campo eliminato troppo presto

MareaPay riceve payload da un provider di pagamenti.

La prima pipeline conserva soltanto:

```text
transaction_id
amount
currency
status
```

perché sono gli unici campi necessari ai report iniziali.

Sei mesi dopo il team antifrode scopre che il payload originale conteneva anche:

- authentication method;
- device signal;
- risk attributes;
- timestamp intermedi.

La trasformazione pre-load li aveva eliminati.

Il provider mantiene il dettaglio storico solo per una finestra limitata.

La nuova domanda non può più essere ricostruita interamente.

L'errore non dimostra che ETL sia sbagliato.

Dimostra che una trasformazione irreversibile è stata applicata **prima di aver deciso quale capacità di replay era necessaria**.

### Raw retention come opzione di recovery

Conservare una versione raw o source-aligned può aiutare a:

- riprocessare dopo un bug;
- applicare nuova logica;
- auditare una trasformazione;
- recuperare campi non usati inizialmente;
- verificare schema changes.

Ma:

> **conservare raw non significa servire raw agli analyst.**

Il raw layer ottimizza replay e fedeltà alla sorgente. Il curated/serving layer ottimizza affidabilità analitica.

Sono responsabilità diverse.

### Caso reale documentato — separare ingestion e trasformazione

Le linee guida attuali di Databricks per pipeline affidabili raccomandano di separare ingestion e trasformazioni downstream, così un failure della business logic non impedisce necessariamente di continuare a far atterrare i dati sorgente. Questo crea un failure boundary utile: possiamo conservare ciò che è arrivato e riprocessarlo quando il codice viene corretto.

Fonte: https://docs.databricks.com/aws/en/ldp/best-practices

Il pattern è generale:

```text
source
→ durable landing
→ transformation
```

riduce il rischio che un bug downstream provochi contemporaneamente perdita del dato in ingresso.

### Reversibilità della trasformazione

Per ogni step chiediamo:

> Se questa logica è sbagliata, posso ricostruire il risultato corretto?

Una trasformazione è più recuperabile se abbiamo:

- input conservato;
- codice/versione;
- parametri/cut-off;
- metadata di ingestion;
- capacità di backfill.

È meno recuperabile se sovrascrive l'unica copia esistente.

### Privacy: raw non significa conservare tutto per sempre

Replayability ha anche un costo e un limite.

Non è una giustificazione per conservare indefinitamente ogni dato.

Dobbiamo bilanciare:

- audit/reprocessing;
- minimizzazione dei dati;
- retention;
- sicurezza;
- costo;
- requisiti normativi.

Il Capitolo 18 riprenderà questi trade-off a livello di governance.

### Campo della Data Flow Architecture Map

Per ogni transformation boundary annotiamo:

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

### Regola operativa

ETL vs ELT è una scorciatoia terminologica.

Le domande professionali sono:

1. dove viene applicata la trasformazione?
2. quali dati vengono persi in modo irreversibile?
3. possiamo riprocessare?
4. la failure della trasformazione blocca l'ingestion?
5. quale layer è appropriato per il consumo analitico?

> **Una buona pipeline non conserva tutto indiscriminatamente. Conserva abbastanza stato e provenienza da poter correggere il passato quando scopriamo che la logica di ieri era sbagliata.**
