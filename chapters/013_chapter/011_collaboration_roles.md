## 13.10 Il team è parte dello stack: scegliere strumenti che qualcuno possa possedere

Una soluzione tecnicamente elegante può essere una pessima scelta se nessuno nel team reale può revisionarla, operarla o modificarla.

Per questo il Tooling Decision Record deve considerare **chi mantiene il lavoro**, non soltanto chi lo costruisce.

Il Capitolo 18 entrerà nell'operating model analitico. Qui ci interessa una conseguenza pratica:

> **la mantenibilità è una proprietà della combinazione tool + persone + processo.**

### Il rischio del “best tool in theory”

Immaginiamo due opzioni.

**A**

- soluzione tecnicamente ottimale;
- conosciuta da una sola persona;
- nessun supporto interno;
- deployment complesso.

**B**

- soluzione leggermente meno sofisticata;
- standard aziendale;
- sei persone in grado di revisionarla;
- logging e accessi già integrati.

Se la differenza di performance non cambia la decisione, B può avere un costo totale molto inferiore.

La familiarità non deve dominare la scelta, ma **la capacità collettiva è un requisito reale**.

### Caso simulato/composito — dashboard che si rompe ogni lunedì

Un analyst collega una dashboard direttamente a tre sorgenti operative.

Ogni lunedì un refresh fallisce e l'analyst interviene manualmente.

Finché il dashboard è un prototipo, questa soluzione può essere tollerabile.

Quando 80 manager iniziano a dipendere dall'output, il failure mode cambia natura.

Non serve che l'analyst diventi improvvisamente un data engineer.

Serve riconoscere che la responsabilità è passata da:

> analisi

ad

> **servizio dati ricorrente**.

Il tool e l'ownership devono essere rivalutati insieme.

### Handoff threshold

Alcuni segnali indicano che un artefatto sta attraversando un confine organizzativo:

- più team dipendono dall'output;
- serve SLA;
- servono credenziali/secret gestiti;
- una trasformazione è riusata ampiamente;
- il failure blocca un processo business;
- serve on-call o recovery;
- il codice deve essere deployment-ready;
- il dataset deve avere access control sofisticato.

A quel punto possiamo decidere di:

- mantenere ownership analytics con supporto engineering;
- estrarre alcuni componenti verso analytics engineering;
- affidare ingestion/orchestration a data engineering;
- mantenere la logica semantica sotto ownership business/analytics.

Il titolo del ruolo conta meno della **responsabilità esplicita**.

### Caso simulato/composito — modello eccellente, capacità operativa sbagliata

Un data scientist produce un churn score con AUC 0,89.

La lista contiene 62.000 account ad alto rischio.

Customer Success può contattarne 450 a settimana.

Questo non è un problema che si risolve scegliendo una libreria ML diversa.

Serve collaborazione tra:

- chi modella il rischio;
- chi conosce valore e segmenti;
- chi definisce la policy;
- chi esegue l'intervento;
- chi misura l'effetto.

Il Capitolo 10 ci ha già dato la Predictive Decision Card. Qui la lezione è che **lo strumento deve adattarsi al sistema di lavoro che trasforma l'output in azione**.

### Bus factor e tool choice

Una domanda utile è:

> Quante persone potrebbero mantenere questo processo se il suo autore fosse indisponibile per un mese?

Non esiste una soglia universale.

Ma per un processo critico:

```text
bus factor = 1
```

è un segnale di rischio.

Possibili mitigazioni:

- standardizzare il tool;
- documentare;
- fare pairing/review;
- ridurre custom code;
- spostare il workload su piattaforma supportata;
- creare runbook;
- trasferire ownership.

### Campo del Tooling Decision Record

```text
builder:
long-term owner:
reviewers available:
team skill coverage:
platform support:
on-call / recovery need:
bus factor:
handoff threshold:
documentation/runbook:
exit condition:
```

### Regola operativa

> **Non scegliere soltanto uno strumento che tu sappia usare. Scegli una soluzione che l'organizzazione possa continuare a capire e possedere quando il lavoro smette di essere personale.**
