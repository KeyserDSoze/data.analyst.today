## 10.2 Regressione lineare: una baseline interpretabile per target continui

La regressione lineare è uno dei migliori punti di partenza quando il target è numerico.

Non perché il mondo sia lineare, ma perché offre tre vantaggi pratici:

- costruisce una baseline difficile da fraintendere tecnicamente;
- rende visibile la relazione tra feature e previsione;
- produce residui facili da analizzare.

In forma compatta:

`ŷ = β0 + β1x1 + β2x2 + ... + βpxp`

Il modello sceglie i coefficienti per ridurre la distanza tra valori osservati e previsti secondo la funzione di loss adottata; nell'ordinary least squares classico, minimizza la somma dei residui al quadrato.

Fonte: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

### Caso simulato/composito — BrightFoods e il tempo di preparazione ordini

BrightFoods distribuisce prodotti freschi a ristoranti e hotel. Operations deve stimare, al momento in cui un ordine viene rilasciato al magazzino, quanti minuti serviranno per completare il picking.

**Prediction unit:** ordine.  
**Prediction time:** rilascio al warehouse.  
**Target:** minuti fino a `picking_complete`.  
**Decisione:** sequenziamento ordini e assegnazione capacità.

Il dataset contiene 310.000 ordini con feature conoscibili al prediction time:

- numero di righe;
- numero di pezzi;
- quota di prodotti refrigerati;
- distanza attesa tra zone di picking;
- ora del giorno;
- saturazione corrente del magazzino;
- esperienza media del team di turno.

Un primo modello produce, in forma semplificata:

`minutes_hat = 8.4 + 0.31*lines + 0.018*pieces + 6.7*refrigerated_share + 11.2*saturation`

Il coefficiente sulla saturazione non significa:

> "se riduciamo la saturazione di una unità, causeremo 11,2 minuti in meno."

Significa che, **nel modello e nella popolazione osservata**, la saturazione contribuisce alla previsione condizionatamente alle altre feature incluse.

La distinzione con la causalità del Capitolo 8 deve rimanere esplicita.

### Prima domanda: batte davvero una baseline più semplice?

Prima del modello multivariato BrightFoods confronta:

1. mediana storica globale;
2. mediana per fascia di numero righe;
3. regressione lineare.

Supponiamo che sul test temporale ottenga:

| Baseline/modello | MAE |
|---|---:|
| mediana globale | 12,8 min |
| mediana per fascia | 9,6 min |
| regressione lineare | 7,9 min |

Ora sappiamo che una parte consistente del valore viene davvero dalla struttura predittiva e non dal fatto di aver costruito un modello sofisticato.

Una baseline semplice è importante anche mesi dopo: se il modello di produzione non la batte più, abbiamo un segnale molto concreto di deterioramento.

### I residui sono una mappa degli errori

Per ogni osservazione:

`residuo = valore osservato - valore previsto`

Un ordine richiede 52 minuti e il modello ne prevede 39: residuo `+13`.

Il valore medio dell'errore è utile, ma raramente basta. Conviene cercare struttura nei residui per:

- deposito;
- fascia oraria;
- dimensione ordine;
- cliente premium/non premium;
- giorni di picco;
- distanza prevista;
- periodo temporale.

Nel caso BrightFoods i residui molto positivi si concentrano nei turni notturni di un deposito.

L'indagine scopre scanner barcode con connettività intermittente.

Il modello non ha dimostrato la causa del problema, ma ha localizzato una regione del processo in cui la previsione fallisce sistematicamente e che merita investigazione.

### R²: utile, ma risponde a una domanda limitata

`R²` confronta il modello con una baseline che predice la media e descrive quanta variabilità viene catturata dal modello secondo quella definizione.

Non ci dice automaticamente:

- quanto costa l'errore;
- se gli errori sono concentrati nei casi più importanti;
- se le feature esistono in produzione;
- se il modello generalizza a periodi nuovi;
- se le relazioni sono causali.

Per il warehouse un MAE di 8 minuti può essere eccellente sugli ordini standard e inaccettabile se gli errori sui clienti con SLA premium arrivano a 25 minuti.

### Error distribution, non soltanto errore medio

Per target continui è utile mostrare almeno:

- MAE o altra loss coerente con la decisione;
- mediana dell'errore assoluto;
- percentili P90/P95 dell'errore;
- bias medio, cioè sovra/sottostima sistematica;
- errore per segmenti importanti.

Questo rende visibile la differenza tra:

> "in media sbagliamo poco"

ed

> "sbagliamo poco dove conta".

### Quando la linearità è insufficiente

Una regressione lineare può perdere:

- soglie;
- saturazioni;
- interazioni;
- relazioni fortemente curve;
- cambi di regime.

Ma il passaggio a un modello più complesso dovrebbe seguire una diagnosi:

1. quale pattern resta nei residui?
2. è stabile fuori campione?
3. quale complessità aggiuntiva lo cattura?
4. quanto migliora una metrica che interessa alla decisione?

> **La regressione lineare non è il modello da usare quando vogliamo essere semplici. È la baseline da battere prima di poter giustificare una complessità maggiore.**
