## 12.1 OLTP e analytics: il sistema che registra non è necessariamente quello da interrogare

La prima boundary della Data Flow Architecture Map nasce già alla sorgente. Un sistema può essere autorevole per registrare lo stato operativo e, nello stesso tempo, essere un pessimo punto da cui ricostruire storia, aggregazioni e analisi pesanti.

La distinzione tradizionale tra **OLTP** e **OLAP** è utile se la leggiamo così. I workload OLTP privilegiano transazioni frequenti, consistenza e tempi di risposta bassi; i workload analitici sono tipicamente read-intensive e richiedono scansioni, aggregazioni, storia e integrazione tra più sorgenti. Microsoft Azure Architecture Center descrive proprio questa differenza e ricorda che gli ambienti OLAP vengono aggiornati secondo la freshness necessaria al business, non necessariamente a ogni transazione.

Fonte: https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing

### Caso simulato/composito — UrbanBike e il report che compete con il checkout

UrbanBike usa inizialmente lo stesso PostgreSQL per applicazione e reporting. Ogni lunedì una query ricostruisce vendite, resi e commissioni su un volume ormai grande. Nella stessa finestra aumentano CPU e I/O e alcuni endpoint del checkout rallentano.

Il problema non è che il SQL analitico sia “vietato” sull'OLTP. È che due workload con priorità diverse stanno competendo sullo stesso failure domain e sulle stesse risorse. Una possibile evoluzione è:

```text
operational DB
      ↓
replication / ingestion
      ↓
analytical storage
      ↓
curated models
```

Questa separazione protegge il sistema operativo, ma non rende automaticamente il dato pronto per l'analisi. Una replica read-only può ancora avere replication lag, schema operativo difficile, storia sovrascritta e definizioni non conformate. **Source isolation** e **analytical readiness** risolvono problemi diversi.

### System of record e source for analysis

È utile distinguere due responsabilità. Il **system of record** è autorevole per lo stato operativo dell'entità; l'**analytical source o serving layer** è il punto consigliato per analizzare quella realtà dopo integrazione, storicizzazione e validazione.

Per esempio:

```text
customer current status → CRM
customer historical analytical dimension → curated analytical layer
```

Entrambi possono essere corretti, ma per domande differenti.

Anche i sistemi ibridi o HTAP non eliminano questa distinzione. Possono rendere il confine meno fisico, ma restano domande su isolamento del carico, storia disponibile, freshness, serving certificato e failure condivisi.

Nella Data Flow Architecture Map, per una sorgente critica vogliamo almeno:

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

> **Il sistema che registra la realtà non è automaticamente il posto migliore in cui ricostruirla analiticamente. La prima scelta architetturale è sapere quale responsabilità stiamo chiedendo a ciascun sistema.**
