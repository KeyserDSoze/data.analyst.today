# Capitolo 7 — Serie temporali, anomalie e forecasting

> **Il tempo non è soltanto una dimensione del dato. È informazione sul processo che ha generato il dato.**

Nel Capitolo 6 il tempo era soprattutto l'età della relazione con il cliente: quando entra, quanto impiega a raggiungere valore, quando aumenta il rischio di uscita. Qui il tempo diventa qualcosa di ancora più strutturale. Una serie temporale conserva calendario, memoria, stagionalità e cambi di regime; per questo il valore di oggi non è intercambiabile con una riga qualsiasi del passato.

Un lunedì può assomigliare più agli altri lunedì che alla domenica precedente. Un picco può essere eccezionale rispetto alla media del mese e perfettamente normale per Black Friday. Una previsione che funzionava ieri può degradare senza che l'algoritmo sia cambiato, semplicemente perché è cambiato il processo economico che collegava passato e futuro.

Il capitolo ruota quindi attorno a tre domande che in dashboard spesso vengono confuse. La prima è descrittiva: **quale struttura contiene la serie?** La seconda è diagnostica: **ciò che sta accadendo è davvero insolito rispetto a una baseline appropriata?** La terza è predittiva: **quali valori futuri sono plausibili, con quale incertezza, usando soltanto ciò che era conoscibile al momento della previsione?** Nessuna delle tre, da sola, risponde a una quarta domanda: *perché il cambiamento è avvenuto?* Quella è una domanda causale e sarà il punto di partenza del Capitolo 8.

## 7.0 Dal grafico temporale alla decisione

NIST ricorda che le serie temporali possono contenere trend, stagionalità e autocorrelazione e che questa struttura deve essere considerata prima di modellare il processo.[^nist-ts] Hyndman e Athanasopoulos aggiungono una condizione ancora più importante: il forecasting quantitativo ha senso quando disponiamo di dati storici rilevanti e abbiamo ragioni per credere che **almeno una parte della struttura passata continui nel futuro**.[^fpp-data]

Questa continuità non è un dettaglio tecnico. È il contratto implicito di ogni previsione. Un modello sofisticato può essere perfettamente calcolato e diventare poco credibile se cambia il prezzo, il canale, la capacità, il comportamento dei clienti o il sistema che genera una feature. Prima di chiederci quale algoritmo usare, dobbiamo quindi chiederci quale passato sia davvero comparabile con il presente e quale informazione sarebbe stata disponibile al momento della decisione.

### Caso simulato/composito — Il lunedì in cui “crollano le vendite”

Alle 9:12 di lunedì il direttore commerciale di una catena retail scrive al team analytics:

> “Le vendite di ieri sono crollate del 24%. Cosa sta succedendo?”

Il dashboard mostra:

| Giorno | Ricavi |
| --- | ---: |
| Domenica precedente | 1,84 M€ |
| Domenica corrente | 1,40 M€ |
| Variazione | -23,9% |

Il numero è corretto rispetto ai dati caricati, ma la sua interpretazione non è pronta. La domenica precedente coincideva con un weekend promozionale nazionale, quindi il confronto recente usa una baseline eccezionale. Rispetto alla domenica comparabile dell'anno precedente, il dato disponibile appare invece in crescita. Infine, trentasei negozi non hanno ancora inviato la chiusura di cassa.

Quando gli eventi mancanti arrivano, i ricavi diventano **1,51 M€**. Il movimento non scompare, ma cambia natura. Non stiamo osservando un business che “crolla del 24%”: stiamo osservando una giornata inizialmente incompleta, confrontata con un riferimento promozionale non comparabile.

Questo episodio contiene quasi tutto il capitolo. Il dato temporale deve prima essere collocato dentro una baseline e un calendario; poi va verificata la completezza; soltanto a quel punto possiamo decidere se lo scostamento sia normale, anomalo o parte di un nuovo regime. Se infine vogliamo anticipare ciò che accadrà dopo, dobbiamo trasformare quella struttura in un forecast e collegarne l'errore alla decisione.

Un'anomalia, anche quando è reale, non è una causa. Se la domenica restasse molto sotto una baseline stagionale corretta avremmo evidenza di un comportamento insolito, non la prova che il problema sia prezzo, stock-out, meteo, checkout, competitor o mix. Un detector produce un **segnale di investigazione**; la spiegazione richiede altro lavoro.

Lo stesso vale per il forecast. Se il modello stima **1,62 M€** per domenica prossima, quel numero non è il futuro: è un punto centrale dentro una distribuzione di esiti plausibili, condizionata alle informazioni e alle assunzioni disponibili oggi. Per renderlo decisionale dobbiamo conoscere l'orizzonte, la baseline semplice che il modello deve battere, l'errore storico fuori campione, l'incertezza della previsione, le condizioni di validità e il costo di sovrastimare o sottostimare.

## Il deliverable del capitolo: Temporal Decision Brief

Alla fine del capitolo una analisi temporale importante dovrebbe poter essere condensata in un **Temporal Decision Brief**. Non è documentazione del modello: è il punto in cui serie, incertezza e decisione vengono ricomposte.

```text
SERIE
Che cosa misura, con quale frequenza e quale timestamp?

BASELINE
Quale confronto rappresenta davvero il comportamento atteso?

STRUTTURA
Trend, stagionalità, calendario, autocorrelazione, cambi di scala?

ANOMALIA
È un problema del dato, un evento contestuale, un vero scostamento o un cambio di regime?

FORECAST TARGET
Che cosa dobbiamo prevedere, a quale orizzonte e per quale decisione?

BASELINE MODEL
Quale regola semplice dobbiamo battere?

BACKTEST
Avremmo avuto davvero quelle informazioni a quella data?

ERRORE
Quanto sbagliamo e dove costa di più?

INCERTEZZA
Quali scenari/intervalli sono plausibili e quanto sono calibrati?

CONDIZIONI DI VALIDITÀ
Che cosa deve restare abbastanza stabile perché il forecast continui a essere credibile?

AZIONE / MONITORAGGIO
Quale decisione cambia e quali segnali richiedono override o revisione?
```

Il percorso del capitolo seguirà tre movimenti. Prima capiremo **quale passato è comparabile**, leggendo baseline, trend, stagionalità, lag, autocorrelazione e decomposizione. Poi useremo quella struttura per distinguere un'anomalia del dato, un evento contestuale, un vero scostamento e un cambio di regime. Infine passeremo al forecasting: target e orizzonte, baseline, validazione `as-of`, metriche, business loss, intervalli, drift e condizioni di validità.

> **Il forecast migliore non è quello che sembra conoscere il futuro. È quello che dichiara correttamente ciò che sa, ciò che assume e quanto costa quando sbaglia.**

[^nist-ts]: NIST/SEMATECH e-Handbook of Statistical Methods, “Introduction to Time Series Analysis”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
[^fpp-data]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Forecasting data and methods”, https://otexts.com/fpp3/data-methods.html
