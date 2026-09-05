## 12.3 Warehouse e data mart: creare un confine analitico tra sorgenti e consumo

Una volta separati i workload e preservato abbastanza stato da poter riprocessare, serve un punto in cui più sorgenti possano diventare una capacità analitica condivisa. È qui che warehouse e data mart hanno valore architetturale.

Un data warehouse non è utile perché centralizza molti terabyte. È utile quando riduce il costo marginale di rispondere alla prossima domanda: integra sorgenti, conserva storia, riconcilia identità, isola workload analitici dalle applicazioni operative e offre un luogo in cui freshness e qualità possono essere misurate con criteri comuni.

Se per ogni KPI dobbiamo ancora collegarci da zero a cinque sistemi, riscoprire chiavi, ricostruire storia e duplicare business logic, la presenza del warehouse non ha ancora creato una vera capacità condivisa.

### Caso simulato/composito — OrionCloud e cinque percorsi verso la revenue

OrionCloud cresce per acquisizioni e possiede CRM, billing legacy, billing nuovo, ERP e product database. I team costruiscono cinque percorsi indipendenti verso Finance, Sales, Product, Customer Success ed executive reporting.

Il problema non è soltanto che i numeri differiscono. È che esistono **cinque data flow non coordinati**. Quando una sorgente cambia o arriva in ritardo, ogni consumer deve scoprirlo separatamente.

Un percorso più maturo diventa:

```text
sources
   ↓
conformed analytical storage
   ↓
domain models / marts
   ↓
semantic serving
```

La semantica resta quella del Capitolo 11; qui cambia il modo in cui quella semantica viene resa disponibile e riusabile.

### Marts: autonomia senza nuove verità parallele

Un data mart avvicina il serving a un dominio come Finance, Sales, Supply Chain o Product. Può essere uno schema logico, un insieme di tabelle o una materializzazione fisica: la forma conta meno della responsabilità. Deve ridurre la distanza tra piattaforma generica e decisioni del dominio senza creare una seconda piattaforma nascosta.

Due estremi sono fragili. Se tutto è decentralizzato, ogni team ricostruisce raw data e definizioni: velocità locale, incoerenza globale. Se tutto è centralizzato, ogni nuova domanda richiede un ticket al team data centrale: coerenza potenziale, ma self-service quasi nullo.

Una separazione più matura è:

```text
shared platform / integration
+
domain-owned curated models
+
certified serving interfaces
```

Il warehouse funziona anche come failure boundary. Se il CRM è indisponibile, il downstream può ancora avere l'ultimo stato valido, con freshness degradata esplicitamente, invece di colpire direttamente il sistema operativo.

Nella Data Flow Architecture Map annotiamo per warehouse e mart:

```text
role: integration / domain serving / both
upstream sources:
load cadence:
curation boundary:
history retained:
downstream consumers:
owner:
failure behavior:
last known good state available? sì/no
```

> **Warehouse e mart hanno valore quando riducono accoppiamento, duplicazione e fragilità tra sistemi che producono dati e consumer che devono usarli, senza nascondere dove vive la responsabilità semantica.**
