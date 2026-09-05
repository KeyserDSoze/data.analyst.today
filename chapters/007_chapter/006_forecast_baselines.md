## 7.5 Forecasting: definire target, orizzonte e baseline prima del modello

Dopo aver capito quale struttura del passato è informativa, possiamo provare a trasferirne una parte nel futuro. Ma “fare forecasting” resta una frase troppo vaga finché non dichiariamo **che cosa prevediamo, quando emettiamo la previsione e quanto avanti dobbiamo guardare**.

Target, forecast origin e horizon non sono dettagli di implementazione. Sono parte della domanda. La stessa serie di domanda può servire a pianificare lo staffing di domani, il replenishment tra due settimane, gli acquisti internazionali a novanta giorni o la capacità dell'anno successivo. Un modello eccellente a un giorno può essere inutile a otto settimane, e un forecast molto accurato al totale azienda può fallire proprio al grain `SKU × store` dove viene presa la decisione.

Per questo il forecasting dovrebbe iniziare da una domanda operativa:

> **Quale decisione deve essere presa, quanto prima deve essere presa e quale variabile dobbiamo conoscere in quel momento?**

### La complessità deve battere una regola credibile

Prima di discutere algoritmi costruiamo un benchmark. Hyndman e Athanasopoulos trattano metodi come mean, naïve, seasonal naïve e drift come baseline essenziali proprio perché mostrano se la complessità sta aggiungendo capacità predittiva reale.[^fpp-toolbox]

Un forecast naïve usa l'ultimo valore osservato; un seasonal naïve usa l'ultimo periodo stagionalmente comparabile; una media mobile comprime una finestra recente; un drift semplice proietta una tendenza storica. Nessuna di queste regole è “da junior”. Sono il livello minimo che un modello più costoso deve riuscire a superare.

Una catena di supermercati, per esempio, costruisce un modello giornaliero con temperatura, pioggia, promozioni, festività, traffico web, calendario scolastico, prezzo medio, lag e indicatori territoriali. Nel backtest il modello complesso ottiene **MAE 5.480 transazioni**; il seasonal naïve `t-7` ottiene **5.210**. Il risultato non dimostra che meteo e promozioni siano inutili. Dimostra che, con le feature e il disegno attuali, il modello non estrae abbastanza informazione aggiuntiva da superare la memoria settimanale.

La baseline va comunque scelta in modo coerente con il processo. `Ultimo valore` può essere una pessima regola per una serie settimanale; un seasonal naïve può essere insufficiente in un business con crescita molto forte; “stesso giorno dell'anno scorso” può essere fuorviante quando festività mobili o promozioni non sono allineate. Il benchmark deve rappresentare **ciò che avremmo realmente potuto fare con una regola semplice e sensata**.

Dire “MAE 1.200” senza riferimento può essere difficile da interpretare. Dire “il modello riduce il MAE del 18% rispetto al seasonal naïve sullo stesso backtest” rende immediatamente visibile l'informazione aggiuntiva. Metriche scalate come il **MASE** formalizzano la stessa idea confrontando l'errore del modello con quello di una baseline naïve o seasonal-naïve sul training set.[^fpp-accuracy] In modo intuitivo, `MASE < 1` indica che il modello batte il benchmark usato per la scala; `MASE > 1` che fa peggio.

### L'horizon è parte della performance

Un'unica accuracy media può nascondere il punto decisivo. Consideriamo:

| Orizzonte | MAE |
| --- | ---: |
| 1 giorno | 4,2% |
| 7 giorni | 6,8% |
| 30 giorni | 13,1% |
| 90 giorni | 24,7% |

Riassumere tutto con “MAE medio 8,7%” elimina la domanda più importante: **a quale orizzonte viene presa la decisione?** Se procurement deve impegnarsi a novanta giorni, la qualità del forecast a un giorno non compensa l'errore a novanta.

Lo stesso vale per il grain. Un retailer può prevedere bene la domanda nazionale e molto male `SKU × store × giorno`. Scendendo di granularità aumentano zeri, volatilità relativa e sparsità. Per questo “prevedere le vendite della settimana prossima” non è una specifica sufficiente: dobbiamo sapere se intendiamo azienda, regione, negozio, categoria o SKU-store.

### Non tutto è forecastable nello stesso modo

Alcune serie sono dominate da grandi eventi discrezionali, decisioni commerciali esterne o cambiamenti che la storia non contiene. Se pochi clienti generano ordini enormi e non ripetitivi, un modello univariato può non avere abbastanza segnale stabile. In quel caso la risposta professionale può essere: **la serie da sola non basta; servono informazione commerciale, scenari o un processo diverso**.

Prima di modellare compiliamo quindi una scheda minima:

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

Questa specifica trasforma “facciamo un forecast” in un problema valutabile. Il passo successivo sarà verificare se il modello sarebbe riuscito davvero a produrre quelle previsioni nel passato **senza usare informazione che allora apparteneva ancora al futuro**.

> **Un modello complesso deve guadagnarsi il diritto di esistere battendo una baseline credibile sulla decisione e sull'orizzonte che contano.**

[^fpp-toolbox]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “The forecaster's toolbox”, https://otexts.com/fpp3/toolbox.html
[^fpp-accuracy]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Evaluating point forecast accuracy”, https://otexts.com/fpp3/accuracy.html
