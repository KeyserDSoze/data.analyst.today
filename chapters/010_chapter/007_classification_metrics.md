## 10.7 Classification metrics: separare ranking, probabilità e operating point

Un classificatore non ha una sola qualità.

Possiamo chiedere almeno tre cose diverse:

1. **ranking:** ordina i positivi sopra i negativi?
2. **probabilità:** gli score possono essere interpretati come probabilità affidabili?
3. **operating point:** alla soglia o capacità reale, il flusso di decisioni è utile?

Confondere questi livelli porta a frasi come:

> "AUC 0,91 significa 91% di accuratezza."

Non è così.

### Partire dal base rate

Prima di qualsiasi metrica, dichiariamo la prevalenza della classe positiva.

Se le frodi sono lo 0,18%, un classificatore che dice sempre "non frode" ha accuracy 99,82%.

Il numero è corretto e quasi privo di valore operativo.

Lo stesso base rate è importante anche per interpretare la Precision-Recall curve: con un ranking casuale, la precision attesa è circa la prevalenza della classe positiva.

Fonte: https://scikit-learn.org/stable/modules/model_evaluation.html

### Confusion matrix: il modello visto alla soglia reale

A una soglia specifica otteniamo:

| | Predetto positivo | Predetto negativo |
|---|---:|---:|
| Reale positivo | TP | FN |
| Reale negativo | FP | TN |

Da qui:

`precision = TP / (TP + FP)`

`recall = TP / (TP + FN)`

Queste metriche non appartengono al modello in astratto. Appartengono a **modello + soglia + prevalenza + popolazione**.

Se cambia uno di questi elementi, possono cambiare anche precision e recall.

### Caso simulato/composito — ShieldPay e due code operative

ShieldPay processa 8 milioni di transazioni al mese; lo 0,18% è frode confermata.

Il modello alimenta due decisioni:

- **auto-block:** costo del falso positivo molto alto;
- **manual review:** capacità massima di 12.000 casi al giorno.

Per l'auto-block il team vuole precision molto elevata.

Per la manual review può accettare più falsi positivi pur di aumentare recall, ma il volume deve rimanere entro capacità.

Lo stesso score produce quindi due operating point differenti.

Questo mostra perché chiedere "qual è il threshold del modello?" è spesso la domanda sbagliata. Esistono soglie della **policy**.

### ROC-AUC: capacità di ranking su tutte le soglie

ROC-AUC misura, in termini intuitivi, quanto spesso un positivo casuale riceve score maggiore di un negativo casuale.

È utile per confrontare discrimination, ma non dice direttamente:

- quanti casi arriveranno al team;
- quale sarà la precision al top 1%;
- quanto costa un falso positivo;
- se le probabilità sono calibrate.

Con classi rare, false positive rate piccoli possono corrispondere a un numero enorme di falsi positivi perché i negativi sono moltissimi.

### Precision-Recall: zoom sulla classe positiva

Nei problemi fortemente sbilanciati la curva precision-recall rende molto visibile il trade-off operativo.

ShieldPay confronta due modelli:

| Modello | ROC-AUC | Average Precision / PR summary |
|---|---:|---:|
| A | 0,962 | 0,284 |
| B | 0,951 | 0,367 |

A ha ROC-AUC leggermente maggiore. B concentra meglio i positivi dove il team può agire.

La scelta finale richiede comunque il confronto alle soglie reali, non solo una metrica aggregata.

### Precision@K e recall@capacity

Quando la capacità è fissa, metriche di ranking legate al volume possono essere più naturali.

Se Customer Success può chiamare 2.000 clienti:

> **precision@2000** = quanti dei 2.000 clienti prioritizzati manifestano davvero l'evento?

Se il team antifrode può revisionare l'1% delle transazioni:

> **recall@1%** = quale quota delle frodi reali entra in quell'1%?

Queste metriche rendono esplicito il vincolo operativo.

### F1 non conosce la tua funzione di costo

F1 sintetizza precision e recall in un singolo numero e può essere utile quando vogliamo attribuire loro importanza simile.

Ma non sa che:

- una frode persa costa 480 euro;
- una review costa 3,20 euro;
- bloccare un cliente legittimo può avere un costo commerciale di 18 euro;
- il team può gestire solo un certo volume.

Una metrica tecnica non sostituisce la funzione di utilità.

### Metriche per target continuo e classificazione: stessa regola

Anche nella regressione la scelta della metrica deve riflettere l'errore che conta.

- MAE tratta gli errori in modo lineare;
- RMSE penalizza maggiormente errori grandi;
- metriche percentuali hanno problemi specifici vicino a zero;
- una business loss può essere asimmetrica.

Il principio è lo stesso del Capitolo 7 sul forecasting: **la loss utile dipende dalla decisione**.

### Evaluation table minima

Per un classificatore operativo conviene riportare:

- prevalenza/base rate;
- ROC-AUC o altra misura di ranking pertinente;
- PR curve/AP quando la classe è rara;
- precision e recall agli operating point reali;
- confusion matrix alle soglie candidate;
- volume generato;
- performance per segmenti critici;
- costo/valore atteso della policy, quando stimabile.

La calibration verrà trattata separatamente nella prossima sezione.

> **Un buon score ordina. Una buona probabilità quantifica. Una buona soglia rende l'azione sostenibile. Sono tre proprietà diverse e vanno misurate separatamente.**
