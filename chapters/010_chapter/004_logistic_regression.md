## 10.4 Regressione logistica: una baseline probabilistica, non una soglia a 0,5

Quando il target è binario — churn sì/no, default sì/no, frode sì/no — una regressione logistica è spesso una baseline molto forte.

Il suo valore non sta nel produrre direttamente una classe. Sta nel produrre uno **score probabilistico** che possiamo valutare come ranking, calibrare e successivamente tradurre in una decisione.

In forma concettuale:

`logit(p) = β0 + β1x1 + ... + βpxp`

La funzione logistica trasforma poi quel valore in una probabilità compresa tra 0 e 1.

Fonte: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

### Caso simulato/composito — AtlasTel e il churn a 60 giorni

AtlasTel offre connettività a piccole imprese.

**Prediction unit:** account attivo.  
**Prediction time:** lunedì alle 06:00.  
**Target:** cancellazione volontaria entro 60 giorni.  
**Decisione:** costruire una coda settimanale per il team retention.

Feature disponibili al prediction time:

- tenure;
- fatture insolute negli ultimi 90 giorni;
- variazione di utilizzo;
- ticket tecnici già aperti;
- outage sperimentati;
- prezzo attuale e variazioni già entrate in vigore;
- chiamate al supporto storiche;
- utilizzo del portale.

Il modello produce:

| Account | Score di churn |
|---|---:|
| A | 0,08 |
| B | 0,23 |
| C | 0,64 |
| D | 0,81 |

A questo punto non sappiamo ancora chi contattare.

La statistica ha prodotto una stima. La policy deve ancora essere progettata.

### Odds e coefficienti: leggibili, ma facili da abusare

La regressione logistica è lineare nei log-odds. Esponendo un coefficiente otteniamo un odds ratio.

Se `exp(β) = 1,5`, un aumento unitario della feature è associato a odds dell'evento 1,5 volte maggiori, condizionatamente alle altre feature incluse.

Due cautele:

1. odds e probabilità non sono la stessa cosa;
2. un odds ratio predittivo non diventa automaticamente un effetto causale.

Nel primo modello AtlasTel il numero di chiamate al supporto è fortemente associato al churn.

Ridurre artificialmente le chiamate non è una strategia di retention. Le chiamate possono essere un segnale di disservizi, fatture errate o problemi tecnici.

### Il modello produce probabilità; la policy produce classi

Scikit-learn distingue esplicitamente il problema statistico di stimare score/probabilità dal problema decisionale di trasformarli in un'azione. Il threshold predefinito di 0,5 è solo una convenzione software e non è ottimale per la maggior parte dei problemi business.

Fonte: https://scikit-learn.org/stable/modules/classification_threshold.html

AtlasTel può usare la stessa distribuzione di score in modi molto diversi:

- contattare il top 5%;
- contattare tutti sopra 0,70;
- prendere il top 2.000 perché quella è la capacità settimanale;
- combinare probabilità e valore economico;
- applicare soglie differenti per segmenti, se la policy è giustificata e governata.

La scelta non dovrebbe essere incorporata implicitamente dentro `predict()`.

### Ranking prima della soglia

Prima di discutere il cutoff conviene chiedere se il modello ordina bene i casi.

Se i clienti nel decile più alto di score non hanno più churn dei decili inferiori, la soglia non può salvare il modello.

Un controllo semplice è costruire una tabella per decili o quantili:

| Decile di rischio | Churn osservato |
|---|---:|
| 1 — più basso | 1,2% |
| 5 | 5,6% |
| 9 | 18,4% |
| 10 — più alto | 31,7% |

Questa vista non sostituisce ROC-AUC o PR-AUC, ma rende il ranking comprensibile anche a stakeholder non tecnici.

### Probability estimate e expected value

Quando uno score è sufficientemente calibrato possiamo combinarlo con quantità economiche.

Esempio semplificato:

`expected_churn_loss = P(churn) × value_at_risk`

Due clienti con score 0,60 possono così ricevere priorità molto diversa se il valore a rischio è 200 euro oppure 20.000 euro.

Attenzione però: questo calcolo descrive il rischio atteso dell'evento. Non dice quanto valore verrà salvato dall'intervento. Per quello servono anche evidenze sull'effetto causale dell'azione, come discusso nei Capitoli 8 e 9.

### Perché la logistica resta una baseline eccellente

Anche quando il modello finale sarà gradient boosting o un altro estimatore complesso, la regressione logistica offre un confronto utile:

- è veloce;
- è regolarizzabile;
- produce ranking e probabilità;
- rende visibili coefficienti e segni;
- mette in evidenza quanto valore predittivo stiamo realmente guadagnando dalla complessità.

> **La regressione logistica non è il modello “semplice prima di fare ML vero”. È un benchmark probabilistico che un modello più complesso deve battere fuori campione e nella decisione reale.**
