## 7.5 Forecasting: definire target, orizzonte e baseline prima del modello

Forecasting significa usare informazione disponibile **fino a un certo istante** per descrivere valori futuri plausibili.

La frase contiene tre elementi che devono essere espliciti:

- **target** — che cosa prevediamo;
- **forecast origin** — quando la previsione viene emessa;
- **horizon** — quanto avanti dobbiamo prevedere.

Senza questi tre elementi, “il modello ha MAE 6%” è ancora una descrizione incompleta.

### Il forecast deve nascere da una decisione

La stessa serie può richiedere forecast diversi.

Per un magazzino:

- domani → staffing e picking;
- 14 giorni → replenishment locale;
- 90 giorni → acquisti internazionali;
- 12 mesi → capacità e budget.

Un modello eccellente a 1 giorno non è automaticamente utile a 90 giorni.

Il forecasting dovrebbe quindi iniziare da:

> **Quale decisione deve essere presa, quanto prima deve essere presa e quale variabile serve conoscere in quel momento?**

### Prima del modello: benchmark semplici

Hyndman e Athanasopoulos trattano metodi semplici come mean, naïve, seasonal naïve e drift come benchmark fondamentali per capire se un metodo più complesso sta aggiungendo capacità predittiva reale.[^fpp-toolbox]

Esempi:

**Naïve**

`forecast prossimo periodo = ultimo valore osservato`

**Seasonal naïve**

`forecast prossimo lunedì = valore dell'ultimo lunedì comparabile`

**Media mobile**

`forecast = media di una finestra recente`

**Drift / trend semplice**

proiezione della variazione media storica.

La baseline non è un modello “da junior”. È il costo minimo di complessità che ogni soluzione successiva deve giustificare.

### Caso simulato/composito — Il modello con 14 feature battuto dal martedì scorso

Una catena di supermercati vuole prevedere le transazioni giornaliere per pianificare i turni.

Il team costruisce un modello con:

- temperatura;
- pioggia;
- promozioni;
- festività;
- traffico web;
- calendario scolastico;
- prezzo medio;
- diversi lag;
- indicatori territoriali.

Nel backtest:

- modello complesso: MAE 5.480 transazioni;
- seasonal naïve `t-7`: MAE 5.210.

Il modello sofisticato perde contro “lo stesso giorno della settimana precedente”.

Non significa che meteo o promozioni siano irrilevanti. Significa che, con il disegno e le feature disponibili, il modello non estrae abbastanza informazione aggiuntiva da superare una struttura settimanale molto forte.

La baseline ha evitato di confondere complessità con progresso.

### Una baseline deve essere credibile per quel processo

La baseline più semplice non è sempre `ultimo valore`.

Se il processo è settimanale, seasonal naïve può essere molto più forte. Se il business cresce rapidamente, una baseline con drift può essere più corretta. Se esistono festività mobili, “stesso giorno dell'anno scorso” può richiedere un calendario comparabile.

L'obiettivo è costruire un benchmark che rappresenti **ciò che avremmo potuto fare con una regola semplice e ragionevole**.

### Accuracy relativa: “meglio di cosa?”

Dire:

> il MAE è 1.200

può essere difficile da interpretare.

Dire:

> il modello riduce il MAE del 18% rispetto al seasonal naïve sullo stesso backtest

fornisce un riferimento molto più operativo.

Metriche scalate come il **MASE** formalizzano proprio questa idea: confrontano l'errore del modello con quello di una previsione naïve o seasonal-naïve calcolata sul training set.[^fpp-accuracy]

In termini intuitivi:

- MASE < 1 → meglio del benchmark naïve usato per la scala;
- MASE > 1 → peggio del benchmark.

### L'orizzonte deve essere valutato separatamente

Supponiamo che un forecast produca:

| Orizzonte | MAE |
| --- | ---: |
| 1 giorno | 4,2% |
| 7 giorni | 6,8% |
| 30 giorni | 13,1% |
| 90 giorni | 24,7% |

Comprimere tutto in “MAE medio 8,7%” nasconde la domanda più importante: **a quale orizzonte prendiamo la decisione?**

Per questo il Temporal Decision Brief deve specificare target e horizon prima della metrica.

### Granularità: prevedere il totale può essere facile, prevedere ogni SKU no

Un retailer può prevedere abbastanza bene la domanda nazionale totale e molto male la combinazione `SKU × store × giorno`.

Più scendiamo di granularità:

- aumentano gli zeri;
- cresce la volatilità relativa;
- diminuisce il volume per serie;
- diventano più importanti gerarchie e aggregazioni.

La domanda di forecasting deve quindi includere anche il **grain**.

Prevedere “vendite settimana prossima” non basta. Dobbiamo sapere se intendiamo:

- totale azienda;
- regione;
- negozio;
- categoria;
- SKU-store.

### Forecastability: non tutto merita un modello

Alcune serie sono dominate da eventi non ripetitivi o da decisioni esterne non ancora rappresentate nei dati.

Se il processo è quasi interamente guidato da grandi ordini discrezionali di pochi clienti, un forecast puramente univariato può avere poco valore.

La risposta professionale può essere:

> la storia della serie da sola non contiene abbastanza segnale stabile; serve informazione commerciale esterna o un approccio per scenari.

Non costruire un modello è, a volte, la scelta analitica migliore.

### La scheda iniziale del forecast

Prima di modellare compiliamo:

```text
Target:
Grain:
Forecast origin:
Horizon richiesto:
Decisione supportata:
Costo di underforecast:
Costo di overforecast:
Baseline semplice:
Informazioni esterne disponibili al forecast origin:
```

Solo dopo ha senso discutere di algoritmo.

> **Un modello complesso deve guadagnarsi il diritto di esistere battendo una baseline credibile sulla decisione e sull'orizzonte che contano.**

[^fpp-toolbox]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “The forecaster's toolbox”, https://otexts.com/fpp3/toolbox.html
[^fpp-accuracy]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Evaluating point forecast accuracy”, https://otexts.com/fpp3/accuracy.html
