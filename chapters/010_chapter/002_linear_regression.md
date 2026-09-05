## 10.2 Regressione lineare: la prima baseline da battere per target continui

Dopo avere definito prediction time, target e decisione, il passo successivo non è cercare il modello più sofisticato. È costruire un riferimento semplice che ci permetta di capire se la complessità successiva compra davvero informazione utile.

Per un target numerico, la regressione lineare è spesso una baseline eccellente. Non perché il mondo sia lineare, ma perché rende visibile il rapporto tra feature e previsione, produce residui facili da ispezionare e stabilisce un livello di performance che ogni modello più complesso dovrà superare fuori campione.

In forma compatta:

`ŷ = β0 + β1x1 + β2x2 + ... + βpxp`

Nell'ordinary least squares classico i coefficienti vengono scelti minimizzando la somma dei residui al quadrato. Questa definizione tecnica è utile, ma la domanda professionale resta: **quanto migliora la decisione rispetto a una baseline ancora più semplice?**

Riferimento: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

### Caso simulato/composito — BrightFoods

BrightFoods distribuisce prodotti freschi a ristoranti e hotel. Operations deve stimare, nel momento in cui un ordine viene rilasciato al magazzino, quanti minuti serviranno per completare il picking.

```text
Prediction unit: ordine
Prediction time: rilascio al warehouse
Target: minuti fino a picking_complete
Decisione: sequenziamento ordini e assegnazione capacità
```

Il dataset contiene 310.000 ordini. Le feature utilizzabili sono soltanto quelle conoscibili al rilascio: numero di righe, numero di pezzi, quota refrigerata, distanza attesa tra zone, ora del giorno, saturazione corrente del magazzino ed esperienza media del team di turno.

Un primo modello produce, in forma semplificata:

`minutes_hat = 8.4 + 0.31*lines + 0.018*pieces + 6.7*refrigerated_share + 11.2*saturation`

Il coefficiente della saturazione non autorizza a dire che ridurre la saturazione di una unità **causerebbe** 11,2 minuti in meno. Dice soltanto che, nel modello e nella popolazione osservata, la saturazione contribuisce alla previsione condizionatamente alle altre feature incluse. Il confine con la causalità del Capitolo 8 deve rimanere netto anche quando il coefficiente è intuitivo.

### La baseline rende visibile il valore aggiunto

Prima del modello multivariato BrightFoods confronta tre riferimenti sullo stesso test temporale:

| Baseline/modello | MAE |
|---|---:|
| mediana globale | 12,8 min |
| mediana per fascia di numero righe | 9,6 min |
| regressione lineare | 7,9 min |

La tabella racconta molto più di un singolo score. Una parte importante del miglioramento deriva già dal conoscere la dimensione dell'ordine; la regressione aggiunge altro segnale. Se in produzione il modello scendesse sotto la performance della mediana per fascia, avremmo un riferimento concreto per dichiarare deterioramento.

### I residui dicono dove la promessa si rompe

Per ogni osservazione:

`residuo = valore osservato - valore previsto`

Se un ordine richiede 52 minuti e il modello ne prevede 39, il residuo è `+13`. L'errore medio è utile, ma non dice **dove** il modello fallisce. Per questo BrightFoods guarda i residui per deposito, fascia oraria, dimensione ordine, clienti con SLA premium, giorni di picco e livello di saturazione.

I residui molto positivi si concentrano nei turni notturni di un deposito. L'indagine scopre scanner barcode con connettività intermittente. Il modello non ha dimostrato la causa; ha localizzato un tratto del processo in cui la previsione è sistematicamente debole e che merita investigazione.

Questa è una funzione importante dei modelli semplici: oltre a prevedere, mostrano con chiarezza **che cosa non stanno spiegando**.

### R² non è una business loss

`R²` descrive quanta variabilità viene catturata rispetto alla baseline che predice la media. Non dice quanto costa l'errore, se gli errori peggiori sono sui clienti più importanti, se le feature esistono davvero in serving o se la relazione è causale.

Per BrightFoods un MAE di 8 minuti può essere accettabile nel complesso e inaccettabile se gli errori P95 sui clienti premium arrivano a 25 minuti. Per questo la valutazione di un target continuo dovrebbe mostrare almeno errore medio coerente con la decisione, mediana dell'errore assoluto, code P90/P95, bias sistematico e performance per slice business rilevanti.

La distinzione è semplice:

> “in media sbagliamo poco”

non equivale a

> “sbagliamo poco dove il costo dell'errore è alto”.

### Quando serve più complessità

Una regressione lineare può lasciare residui strutturati quando esistono soglie, saturazioni, interazioni, curvature o cambi di regime. Ma il passaggio a spline, alberi, boosting o altri modelli dovrebbe seguire una diagnosi: quale pattern resta fuori campione, quanto è stabile e quanto migliora una loss rilevante per la decisione?

> **La regressione lineare non è il modello da usare per essere semplici. È la baseline che rende misurabile il diritto di essere più complessi.**