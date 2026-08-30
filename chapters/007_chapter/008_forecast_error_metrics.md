## 7.7 Misurare l'errore di previsione: MAE, RMSE, MAPE e il problema della metrica sbagliata

Un forecast non va giudicato chiedendo se ha "indovinato". Va giudicato rispetto a una funzione di errore coerente con la decisione che dobbiamo prendere.

Supponiamo che una catena retail preveda la domanda giornaliera di un prodotto in dieci punti vendita. Per uno store la domanda reale nei cinque giorni successivi è:

| Giorno | Reale | Forecast |
|---|---:|---:|
| Lun | 100 | 95 |
| Mar | 120 | 130 |
| Mer | 90 | 84 |
| Gio | 110 | 108 |
| Ven | 80 | 92 |

L'errore di forecast è la differenza tra valore osservato e valore previsto. Da qui possiamo costruire metriche diverse.

### MAE: errore medio assoluto

Il **Mean Absolute Error** considera la dimensione assoluta degli errori:

\[
MAE = \frac{1}{n}\sum |y_t - \hat{y}_t|
\]

Nel nostro esempio gli errori assoluti sono 5, 10, 6, 2 e 12. Il MAE è quindi 7 unità.

Il vantaggio è immediato: possiamo dire al responsabile supply chain che, in media, il forecast sbaglia di circa sette pezzi al giorno.

### RMSE: quando gli errori grandi devono pesare di più

Il **Root Mean Squared Error** eleva al quadrato gli errori prima di calcolare la media:

\[
RMSE = \sqrt{\frac{1}{n}\sum (y_t - \hat{y}_t)^2}
\]

Questo rende la metrica più sensibile agli errori grandi.

È utile quando uno scostamento molto grande è molto più costoso di più scostamenti piccoli. Per esempio, in un magazzino automatizzato un errore di 100 pallet può essere molto più problematico di dieci errori da 10 pallet.

### MAPE: intuitivo, ma non innocuo

Il **Mean Absolute Percentage Error** esprime l'errore in percentuale rispetto al valore reale.

È spesso apprezzato dai manager perché sembra intuitivo: "il forecast sbaglia in media dell'8%".

Ma il MAPE ha problemi seri quando il valore reale è zero o vicino a zero. Se una serie contiene giorni con domanda 0, 1 o 2 unità, una differenza piccola può produrre percentuali enormi o non definite.

Questo rende il MAPE particolarmente pericoloso per SKU a bassa rotazione, ticket rari, incidenti, frodi, conversioni di micro-segmenti e molte altre serie aziendali reali.

### Caso realistico: il modello migliore sulla dashboard era il peggiore per il magazzino

Una società di ricambi industriali confronta due modelli di forecast per 3.400 SKU.

Il team data science presenta:

| Modello | MAPE |
|---|---:|
| A | 11,2% |
| B | 9,4% |

Il modello B sembra migliore.

Il responsabile operations, però, segnala che dopo il rollout aumentano gli stock-out dei componenti ad alto valore.

L'analisi successiva mostra che il modello B migliora molto su migliaia di SKU a basso volume, ma commette pochi errori enormi su una quarantina di componenti critici. Il MAPE medio premia il modello, mentre il costo economico degli errori peggiora.

Quando il team introduce una valutazione pesata per margine, criticità e costo di stock-out, il modello A risulta preferibile.

La lezione è più generale:

> **La metrica di forecast non deve riflettere soltanto la statistica. Deve riflettere anche il costo decisionale dell'errore.**

### Una metrica non basta quasi mai

In pratica conviene osservare almeno:

- errore assoluto medio;
- distribuzione degli errori;
- bias medio, per capire se il modello tende a sovrastimare o sottostimare;
- performance per segmento;
- performance per orizzonte di forecast;
- confronto con una baseline semplice;
- costo business associato agli errori.

Hyndman e Athanasopoulos distinguono chiaramente gli errori di forecast dai residui e sottolineano che MAE, RMSE e MAPE hanno proprietà differenti; in particolare il MAPE può diventare instabile o indefinito quando i valori reali sono nulli o vicini a zero.

### Riferimenti

- Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd edition, sezione "Evaluating point forecast accuracy": https://otexts.com/fpp3/accuracy.html
