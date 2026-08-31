## 10.7 Accuracy non basta: precision, recall, ROC-AUC e PR-AUC

Un classificatore può essere eccellente secondo una metrica e quasi inutile per il business.

La scelta della metrica deve dipendere da:

- frequenza del fenomeno;
- costo dei falsi positivi;
- costo dei falsi negativi;
- capacità operativa;
- uso della probabilità stimata.

La documentazione ufficiale di scikit-learn include numerose metriche di classificazione, tra cui accuracy, precision-recall curve, ROC curve e AUC.

Fonte: https://scikit-learn.org/stable/modules/model_evaluation.html

### La confusion matrix

Per una classificazione binaria abbiamo:

| | Predetto positivo | Predetto negativo |
|---|---:|---:|
| Reale positivo | True Positive | False Negative |
| Reale negativo | False Positive | True Negative |

Da qui derivano metriche diverse.

### Precision

\[
Precision = \frac{TP}{TP+FP}
\]

Risponde a:

> tra i casi che ho segnalato come positivi, quanti lo erano davvero?

### Recall

\[
Recall = \frac{TP}{TP+FN}
\]

Risponde a:

> tra tutti i positivi reali, quanti ne ho intercettati?

### Caso realistico: ShieldPay e il fraud screening

ShieldPay processa 8 milioni di transazioni al mese.

Solo lo 0,18% è realmente fraudolento.

Un modello che predice sempre “non frode” avrebbe accuracy:

\[
99,82\%
\]

Sembra fantastico.

In realtà intercetta **zero frodi**.

Il team ha due livelli operativi:

- blocco automatico per rischio molto alto;
- revisione manuale per casi intermedi.

Per il blocco automatico serve precision elevata: bloccare clienti legittimi è costoso.

Per la coda di revisione manuale può essere accettabile maggiore recall, purché il volume rimanga gestibile.

La stessa probabilità prodotta dal modello alimenta quindi due policy diverse.

### ROC-AUC

La curva ROC confronta:

- true positive rate;
- false positive rate;

al variare della soglia.

ROC-AUC misura la capacità di ranking del modello attraverso tutte le soglie.

È utile, ma può risultare molto ottimista in problemi estremamente sbilanciati.

### Precision-Recall curve

Quando la classe positiva è rara, la curva precision-recall è spesso molto più informativa.

Per ShieldPay, due modelli hanno:

| Modello | ROC-AUC | PR-AUC |
|---|---:|---:|
| A | 0,962 | 0,284 |
| B | 0,951 | 0,367 |

Guardando solo ROC-AUC sceglieremmo A.

Ma B concentra meglio i casi di frode nelle prime posizioni del ranking e produce una coda di revisione più utile.

Il team sceglie B.

### F1 score

F1 combina precision e recall tramite media armonica:

\[
F1 = 2\frac{Precision \times Recall}{Precision+Recall}
\]

Può essere utile quando precision e recall hanno importanza simile.

Ma non incorpora direttamente costi economici diversi.

### Dal modello al valore economico

Supponiamo che:

- una frode non bloccata costi in media 480 euro;
- una revisione manuale costi 3,20 euro;
- bloccare erroneamente una transazione legittima abbia un costo medio stimato di 18 euro tra supporto e churn.

A quel punto la scelta della soglia può essere formulata come problema economico, non come gara tra metriche astratte.

### Caso realistico: CarePlus e il richiamo clienti

CarePlus vuole prevedere quali clienti hanno alta probabilità di non rinnovare.

Modello A:

- precision 62%;
- recall 31%.

Modello B:

- precision 41%;
- recall 68%.

Se il team può contattare solo 5.000 clienti, A può essere migliore.

Se l'intervento è una email automatica quasi gratuita, B può essere più utile.

Non esiste una metrica “migliore” indipendentemente dal processo decisionale.

### Regola operativa

Quando presenti un classificatore, evita di mostrare solo una metrica aggregata.

Mostra almeno:

- prevalenza della classe;
- confusion matrix a una o più soglie operative;
- precision;
- recall;
- curve o metriche di ranking appropriate;
- volume di casi generato;
- costo o beneficio atteso.

Il modello produce segnali. Il business deve trasformarli in una policy.
