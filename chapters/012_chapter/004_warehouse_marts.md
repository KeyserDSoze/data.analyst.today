## 12.3 Warehouse e data mart: creare un confine analitico tra sorgenti e consumo

Nel Capitolo 11 abbiamo già visto come modellare fatti, dimensioni e metriche. Qui il punto è diverso:

> **Perché un'organizzazione introduce un ambiente analitico condiviso invece di lasciare che ogni consumer interroghi direttamente le sorgenti?**

Un data warehouse crea un **integration and serving boundary**.

Può diventare il luogo in cui:

- dati di più sistemi vengono riuniti;
- storia viene conservata;
- identità vengono riconciliate;
- modelli curati diventano riusabili;
- workload analitici vengono isolati dalle applicazioni operative;
- freshness e qualità possono essere misurate in modo coerente.

### Il valore non è “centralizzare tutto”

Un warehouse non è utile perché contiene molti terabyte.

È utile quando riduce il costo marginale di rispondere alla prossima domanda.

Se per ogni KPI dobbiamo ancora:

1. collegarci a cinque sorgenti;
2. capire da zero le chiavi;
3. ricostruire la storia;
4. riconciliare Finance;
5. duplicare business logic;

la presenza di un warehouse non ha ancora creato una vera capacità analitica condivisa.

### Caso simulato/composito — OrionCloud e cinque percorsi verso la revenue

OrionCloud cresce attraverso acquisizioni e possiede:

- CRM;
- billing legacy;
- billing nuovo;
- ERP;
- product database.

I team costruiscono flussi indipendenti:

```text
billing legacy → Finance workbook
CRM → Sales dashboard
product DB → Product analytics
new billing → Customer Success report
ERP → executive report
```

Il problema non è soltanto che i numeri differiscono.

Il problema architetturale è che esistono **cinque percorsi non coordinati** dalla sorgente alla decisione.

Quando una sorgente cambia o arriva in ritardo, ogni consumer scopre il problema separatamente.

Un integration layer condiviso permette invece:

```text
sources
   ↓
conformed analytical storage
   ↓
domain models / marts
   ↓
semantic serving
```

La semantica resta quella definita nel Capitolo 11; qui cambia il modo in cui viene resa disponibile a più consumer.

### Data mart: avvicinare serving e dominio

Un data mart è una vista curata per un dominio, per esempio:

- Finance;
- Sales;
- Supply Chain;
- Product.

Può essere:

- schema logico;
- insieme di tabelle;
- materializzazione fisica;
- modello servito da una piattaforma condivisa.

La forma tecnica conta meno della responsabilità:

> **il mart riduce la distanza tra una piattaforma generica e un insieme di decisioni specifiche del dominio.**

### Centralizzazione e autonomia

Due estremi falliscono spesso.

**Tutto decentralizzato**

Ogni team copia raw data e ricostruisce definizioni.

Risultato:

- velocità locale;
- incoerenza globale;
- molte pipeline duplicate.

**Tutto centralizzato**

Ogni nuova domanda richiede un ticket al team data centrale.

Risultato:

- coerenza potenziale;
- coda crescente;
- self-service quasi nullo.

Una struttura più matura può separare:

```text
shared platform/integration
+
domain-owned curated models
+
certified serving interfaces
```

Il Capitolo 18 riprenderà questa tensione come operating model organizzativo.

### Warehouse come failure boundary

Un punto spesso sottovalutato è che il warehouse separa anche failure domain diversi.

Se il CRM è temporaneamente indisponibile, possiamo avere:

- ultimo snapshot valido ancora interrogabile;
- pipeline che segnala freshness degradata;
- dashboard che non colpisce direttamente il CRM.

Questo non elimina il problema, ma rende possibile una degradazione controllata.

### Quando un mart crea una nuova verità parallela

Un mart diventa pericoloso se:

- copia dati senza lineage;
- modifica definizioni localmente;
- non riceve breaking changes;
- non si riconcilia con i modelli condivisi.

Quindi un mart dovrebbe essere un **consumer governato della piattaforma**, non una seconda piattaforma nascosta.

### Campo della Data Flow Architecture Map

Per ogni warehouse/mart annotiamo:

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

### Regola operativa

Quando entriamo in un nuovo ambiente chiediamo:

1. qual è il punto di integrazione tra sorgenti?
2. quali asset sono source-aligned e quali business-ready?
3. quali mart sono ufficiali?
4. quali logiche appartengono alla piattaforma condivisa e quali al dominio?
5. cosa succede ai consumer se una sorgente upstream fallisce?

> **Un warehouse non è soltanto un posto dove mettere dati. È un confine che dovrebbe ridurre accoppiamento, duplicazione e fragilità tra sistemi che producono dati e persone che devono usarli.**
