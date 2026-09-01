## 12.1 OLTP e analytics: il sistema che registra non è necessariamente quello da interrogare

Una delle prime domande della Data Flow Architecture Map è:

> **Dove nasce il dato e quel sistema è progettato anche per il tipo di analisi che vogliamo eseguire?**

La distinzione tradizionale tra **OLTP** e **OLAP** è utile proprio per questo.

In modo semplificato:

- **OLTP** privilegia transazioni operative frequenti, consistenza e tempi di risposta bassi;
- **OLAP / analytical serving** privilegia scansioni, aggregazioni, storia e query su grandi volumi.

Microsoft Azure Architecture Center descrive i workload analitici come tipicamente read-intensive, alimentati da dati storici e curati, mentre le sorgenti transazionali sono progettate prima di tutto per sostenere il processo operativo.

Fonte: https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing

### Lo stesso dominio, due responsabilità diverse

In un e-commerce il sistema operativo deve poter:

```text
creare ordine
→ autorizzare pagamento
→ riservare stock
→ aggiornare stato
→ rispondere all'applicazione
```

Il workload analitico può invece chiedere:

> Qual è il contribution margin per categoria, paese e coorte negli ultimi 24 mesi, corretto per refund e riclassificazioni storiche?

La seconda domanda può richiedere:

- molte più righe;
- storia;
- più sorgenti;
- join e aggregazioni pesanti;
- definizioni che non appartengono al database transazionale.

### Caso simulato/composito — UrbanBike e il report che compete con il checkout

UrbanBike usa inizialmente lo stesso PostgreSQL per applicazione e reporting.

Ogni lunedì una query ricostruisce vendite, resi e commissioni su un volume ormai molto grande.

Nella stessa finestra:

- aumentano CPU e I/O;
- le query operative attendono più a lungo;
- alcuni endpoint del checkout rallentano.

Il problema non è che SQL analitico sia “vietato” sull'OLTP.

Il problema è che due workload con priorità diverse stanno competendo sullo stesso failure domain e sulle stesse risorse.

Una possibile evoluzione è:

```text
operational DB
      ↓
replication / ingestion
      ↓
analytical storage
      ↓
curated models
```

### Replica non significa automaticamente dato pronto

Spostare il carico su una replica read-only risolve parte del problema operativo, ma non crea automaticamente un prodotto analitico affidabile.

Una replica può avere:

- replication lag;
- schema operativo difficile da usare;
- storia sovrascritta;
- dati distribuiti su più sistemi;
- definizioni non conformate.

Quindi dobbiamo distinguere:

```text
source isolation
≠
analytical readiness
```

La replica protegge il sistema operativo. Il layer analitico risolve un problema diverso.

### HTAP e sistemi ibridi non annullano la domanda

Esistono piattaforme capaci di sostenere workload transazionali e analitici nello stesso ecosistema.

La presenza di tecnologia ibrida non elimina però le domande architetturali:

- quali query possono competere con il traffico operativo?
- quale storia è disponibile?
- quale freshness è garantita?
- qual è il serving model certificato?
- quale failure impatta entrambi i workload?

Il confine può diventare meno fisico, ma resta un confine di responsabilità.

### Source of record vs source for analysis

Un concetto utile è separare:

**system of record**

Il sistema autorevole per lo stato operativo di un'entità.

**analytical source / serving layer**

Il punto consigliato per analizzare quella realtà, eventualmente integrata, storicizzata e validata.

Per esempio:

```text
customer current status → CRM
customer historical analytical dimension → warehouse/lakehouse curated layer
```

Entrambi possono essere “corretti” per usi diversi.

### Campo della Data Flow Architecture Map

Per ogni sorgente critica annotiamo:

```text
system of record:
workload type:
allowed analytical load:
history available:
replication/ingestion path:
expected lag:
downstream analytical source:
owner:
```

### Regola operativa

Prima di interrogare direttamente una sorgente chiediamo:

1. sto mettendo a rischio un workload operativo?
2. la sorgente contiene la storia necessaria?
3. esiste una replica o un layer analitico più appropriato?
4. qual è il lag tra sorgente e serving layer?
5. quale dei due è certificato per la decisione?

> **Il sistema che registra la realtà non è automaticamente il posto migliore in cui ricostruirla analiticamente.**
