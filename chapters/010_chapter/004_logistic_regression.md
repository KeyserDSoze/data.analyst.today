## 10.4 Regressione logistica: prima stimare il rischio, poi decidere la soglia

Quando il target è binario — churn sì/no, default sì/no, frode sì/no — la regressione logistica è spesso una baseline molto forte. Il suo valore non sta nel produrre direttamente una classe, ma nel generare uno **score probabilistico** che possiamo valutare come ranking, calibrare e soltanto dopo tradurre in una policy.

In forma concettuale:

`logit(p) = β0 + β1x1 + ... + βpxp`

La funzione logistica trasforma poi il risultato in un valore tra 0 e 1. La distinzione importante è che il modello stima uno score; la decisione su chi contattare, bloccare o revisionare appartiene a un livello successivo.

Riferimento: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

### Caso simulato/composito — AtlasTel

AtlasTel offre connettività a piccole imprese. Ogni lunedì alle 06:00 deve ordinare gli account attivi per rischio di cancellazione volontaria nei successivi 60 giorni, così il team retention può costruire la propria coda settimanale.

```text
Prediction unit: account attivo
Prediction time: lunedì 06:00
Target: churn volontario entro 60 giorni
Decisione: priorità della coda retention
```

Le feature disponibili al prediction time comprendono tenure, fatture insolute negli ultimi 90 giorni, variazione di utilizzo, ticket già aperti, outage sperimentati, prezzo in vigore, chiamate storiche al supporto e uso del portale.

Il modello produce, per esempio:

| Account | Score di churn |
|---|---:|
| A | 0,08 |
| B | 0,23 |
| C | 0,64 |
| D | 0,81 |

Questa tabella non dice ancora chi chiamare. Dice soltanto come il modello ordina e quantifica il rischio secondo la propria rappresentazione del problema.

### I coefficienti restano predittivi

La regressione logistica è lineare nei log-odds; esponendo un coefficiente otteniamo un odds ratio. Se `exp(β) = 1,5`, un aumento unitario della feature è associato a odds dell'evento 1,5 volte maggiori, condizionatamente alle altre feature incluse.

Questo non trasforma l'odds ratio in un treatment effect. Nel modello AtlasTel il numero di chiamate al supporto può essere fortemente associato al churn perché segnala disservizi, fatture errate o problemi tecnici. Ridurre artificialmente le chiamate non è una strategia di retention.

La regola del capitolo resta quindi la stessa: **una feature può essere un ottimo segnale senza essere una leva**.

### Il threshold 0,5 non appartiene al problema business

La documentazione scikit-learn separa esplicitamente il problema statistico di stimare score/probabilità dal problema decisionale di scegliere un'azione. Il cutoff `0,5` è una convenzione predefinita di classificazione, non una soglia universalmente corretta.

Riferimento: https://scikit-learn.org/stable/modules/classification_threshold.html

AtlasTel potrebbe usare la stessa distribuzione di score per contattare il top 5%, tutti sopra 0,70, i primi 2.000 clienti oppure una graduatoria combinata con valore economico a rischio. In tutti questi casi il modello è identico; cambia la **policy**.

Prima di discutere il cutoff conviene verificare che il ranking contenga davvero segnale. Una vista per decili può renderlo intuitivo:

| Decile di rischio | Churn osservato |
|---|---:|
| 1 — più basso | 1,2% |
| 5 | 5,6% |
| 9 | 18,4% |
| 10 — più alto | 31,7% |

Se il decile 10 non contiene più eventi dei decili inferiori, nessuna soglia può salvare il modello. ROC-AUC e PR-AUC daranno una lettura più formale; la tabella rende il comportamento comprensibile anche fuori dal team tecnico.

### Probabilità e valore atteso

Quando lo score è sufficientemente calibrato può entrare in calcoli come:

`expected_churn_loss = P(churn) × value_at_risk`

Due clienti con `P(churn)=0,60` possono avere priorità molto diversa se il valore a rischio è 200 € oppure 20.000 €. Anche qui però manca ancora un pezzo: il rischio atteso non dice quanto churn verrà **evitato** dall'intervento. Per quello servono evidenze causali sulla policy, come nei Capitoli 8 e 9.

### Perché resta una baseline importante

Un modello più complesso — per esempio gradient boosting — deve dimostrare di migliorare non soltanto una metrica astratta ma la performance fuori campione **nel punto operativo che conta**. La regressione logistica offre un benchmark veloce, regolarizzabile e leggibile, e rende evidente quanto valore predittivo stiamo realmente comprando con la complessità.

> **La regressione logistica non è il modello semplice che precede il “vero ML”. È il benchmark probabilistico che obbliga ogni modello successivo a dimostrare un vantaggio reale nella decisione.**