## 10.7 Classification metrics: misurare ranking, probabilità e decisione come tre cose diverse

Un classificatore non ha una sola qualità. Possiamo chiedergli se ordina bene i casi, se gli score possono essere letti come probabilità e se, alla soglia o capacità reale, produce una coda operativa utile. Queste tre proprietà sono collegate ma non equivalenti.

Il primo passo è dichiarare il **base rate**. Se le frodi sono lo 0,18%, un classificatore che predice sempre “non frode” ottiene accuracy 99,82%. Il numero è corretto e quasi privo di valore decisionale. La prevalenza è anche il riferimento naturale della Precision-Recall curve: un ranking casuale ha precision attesa circa pari alla prevalenza.

Riferimento: https://scikit-learn.org/stable/modules/model_evaluation.html

### Caso simulato/composito — ShieldPay

ShieldPay processa 8 milioni di transazioni al mese; lo **0,18%** è frode confermata. Lo stesso score alimenta due policy: auto-block, dove un falso positivo costa molto, e manual review, dove il team può gestire al massimo 12.000 casi al giorno.

Per l'auto-block serve precision molto elevata. Per la review possiamo accettare più falsi positivi in cambio di recall, purché il volume resti dentro capacità. Lo stesso modello ha quindi due operating point diversi.

Questa osservazione sposta la domanda da:

> “Qual è il threshold del modello?”

A:

> **“Quale soglia rende sostenibile questa specifica policy?”**

### La confusion matrix appartiene alla policy

A una soglia fissata otteniamo TP, FP, FN e TN, da cui:

`precision = TP / (TP + FP)`

`recall = TP / (TP + FN)`

Precision e recall non sono proprietà immutabili del classifier: dipendono da modello, soglia, prevalenza e popolazione. Se cambia il base rate o il cutoff, cambia anche il significato operativo della coda.

ROC-AUC descrive la capacità di ranking lungo tutte le soglie e può essere interpretata come la probabilità che un positivo casuale riceva score maggiore di un negativo casuale. È utile, ma non dice quanti casi entreranno in review, quanto sarà la precision nel top 1% o quanto costa un falso positivo.

Con classi rare, la Precision-Recall curve rende spesso più visibile il trade-off nella regione che interessa. ShieldPay confronta:

| Modello | ROC-AUC | Average Precision / PR summary |
|---|---:|---:|
| A | 0,962 | 0,284 |
| B | 0,951 | 0,367 |

A discrimina leggermente meglio in senso ROC globale. B concentra meglio i positivi nella regione operativa. La scelta finale richiede comunque una valutazione alla capacità reale.

### Quando la capacità è fissa, la metrica può dichiararlo

Se Customer Success può chiamare 2.000 clienti, `precision@2000` risponde direttamente a quanti dei casi prioritizzati manifesteranno l'evento. Se Risk può revisionare l'1% delle transazioni, `recall@1%` dice quale quota dei positivi reali entra nella capacità disponibile.

Queste metriche non sostituiscono una scorecard più ampia, ma collegano la valutazione alla decisione. Lo stesso principio vale per target continui: MAE, RMSE o una business loss differente pesano errori diversi, quindi la loss deve riflettere ciò che costa davvero sbagliare.

### F1 non conosce il business

F1 sintetizza precision e recall, ma non sa che una frode persa costa 480 €, una review 3,20 €, un blocco legittimo 18 € o che la capacità giornaliera è limitata. Nessuna metrica tecnica incorporerà questi costi se non glieli rendiamo espliciti.

Per un classificatore operativo conviene quindi mostrare almeno base rate, ranking globale, PR summary per eventi rari, precision/recall agli operating point reali, confusion matrix, volume generato, slice critiche e — quando disponibile — costo o valore atteso della policy.

La calibration verrà separata nella prossima sezione, perché un modello può ordinare bene e assegnare numeri probabilistici sbagliati.

> **Un buon score ordina. Una buona probabilità quantifica. Una buona soglia rende l'azione sostenibile. Valutare un classificatore significa sapere quale delle tre proprietà stiamo misurando.**