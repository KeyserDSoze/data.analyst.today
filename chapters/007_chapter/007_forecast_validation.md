## 7.6 Validare un forecast: ricostruire ciò che avremmo saputo davvero

Una previsione va valutata su **forecast genuini**, non sulla capacità del modello di spiegare dati che ha già visto. In una serie temporale questo requisito è più severo del semplice “train prima, test dopo”: per ogni origine di forecast dobbiamo ricostruire quali informazioni sarebbero state realmente conoscibili in quel momento.

Hyndman e Athanasopoulos descrivono la time-series cross-validation proprio come una sequenza di origini che avanzano nel tempo, usando ogni volta soltanto osservazioni precedenti al punto previsto.[^fpp-tscv] Questa logica è il cuore del backtest professionale.

Uno split minimo può separare, per esempio, gennaio 2023–dicembre 2025 per il training e gennaio–giugno 2026 per il test. È già migliore di uno split casuale, perché impedisce al futuro di entrare direttamente nel training. Ma un singolo periodo può essere eccezionalmente facile o difficile. Per questo una **rolling-origin evaluation** simula molte decisioni storiche: train fino a gennaio e forecast febbraio, poi train fino a febbraio e forecast marzo, e così via. Se la decisione reale richiede quattro settimane di anticipo, ogni origine deve valutare davvero `h=4`, non soltanto il passo successivo.

### Caso simulato/composito — Il forecast perfetto che conosceva la promozione finale

Un retailer prevede le vendite giornaliere usando anche `promotion_discount`. Nel dataset storico quella colonna contiene lo sconto **effettivamente applicato** in ogni giornata. Il backtest è eccellente; in produzione la performance crolla.

Il problema non è l'algoritmo. Quando il forecast settimanale veniva emesso, molte promozioni erano ancora modificabili e lo sconto finale non era noto. Il test storico aveva fornito al modello una versione dell'informazione che apparteneva al futuro.

Questo porta al concetto operativo più importante della sezione: **as-of data**. Per una previsione emessa il 10 marzo alle 8:00 dobbiamo sapere quale versione di prezzi, promozioni, stock, meteo, budget media, pipeline commerciale, ordini e dati finanziari fosse effettivamente disponibile il 10 marzo alle 8:00.

La data nominale di una colonna non basta. Possiamo introdurre leakage con aggregazioni che includono finestre future, normalizzazione calcolata sull'intero dataset, target encoding costruito con periodi successivi, stock finale della giornata usato in un forecast mattutino, status di consegna successivi al momento previsto o calendari promozionali “finali” che allora erano ancora incompleti.

### Il passato può essere revisionato

Alcune metriche cambiano dopo la prima pubblicazione. Revenue e resi possono essere ricostruiti per giorni; attribution marketing può essere aggiornata a posteriori; indicatori macro vengono revisionati; un ordine inizialmente valido può essere cancellato più tardi. Se il modello operativo vedeva la prima versione ma il backtest usa il dato finale corretto, la validazione diventa troppo ottimista.

Quando la differenza è materiale, dobbiamo conservare o ricostruire i **data vintages**. Il backtest non deve riprodurre il passato come lo conosciamo oggi; deve riprodurlo come avremmo potuto conoscerlo allora.

### Testare condizioni diverse, non soltanto la media

Un backtest credibile dovrebbe attraversare settimane normali, festività, promozioni, picchi, cali, crescita, vincoli di capacità ed eventuali cambi di regime. Non perché il passato possa contenere ogni futuro possibile, ma perché un modello validato solo nelle finestre facili non merita l'etichetta di robusto.

Consideriamo due modelli:

| Modello | MAE medio | Peggior settimana |
| --- | ---: | ---: |
| A | 6,2% | 11,4% |
| B | 6,0% | 28,7% |

B vince leggermente in media e fallisce molto peggio nel worst-case. Se il forecast governa capacità critica, A può essere la scelta migliore. La validazione deve quindi guardare anche quantili dell'errore, bias, horizon, segmenti materiali e periodi in cui sbagliare costa di più.

La baseline deve essere valutata **sugli stessi forecast origin e sugli stessi futuri** del modello. Non ha senso confrontare un modello su un periodo recente difficile con una regola semplice su un altro pezzo di storia. La domanda corretta è: *nelle medesime condizioni e con la stessa informazione disponibile, la soluzione complessa avrebbe prodotto una decisione migliore?*

Nel Temporal Decision Brief la scheda di validazione resta un artefatto utile:

```text
Forecast origin simulati:
Horizon:
Training window:
Expanding o rolling window:
Data disponibili as-of:
Revisioni/vintage gestiti:
Baseline:
Metriche:
Periodi speciali presenti:
Performance media:
Worst-case / quantili:
Stabilità per segmento e horizon:
```

> **Un backtest credibile non ricostruisce il passato come lo conosciamo oggi. Ricostruisce il passato come avremmo potuto conoscerlo allora.**

Una volta ottenuti errori realmente fuori campione possiamo finalmente discutere di “accuracy”. Ma anche lì rimane una domanda: **quale tipo di errore conta davvero per il business?**

[^fpp-tscv]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Time series cross-validation”, https://otexts.com/fpp3/tscv.html
