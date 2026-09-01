## 7.7 Misurare l'errore: accuracy statistica e costo decisionale

Un forecast non è “giusto” o “sbagliato”. Produce errori di dimensione e direzione diverse in momenti diversi.

La scelta della metrica stabilisce **quali errori consideriamo più importanti**.

Per questo MAE, RMSE, MAPE o MASE non sono semplicemente modi alternativi di mostrare lo stesso risultato.

### Forecast error e residuo non sono la stessa cosa

Hyndman e Athanasopoulos distinguono chiaramente:

- **residuo** — errore calcolato sui dati usati per stimare il modello;
- **forecast error** — differenza tra valore futuro osservato e previsione prodotta senza aver visto quel valore.[^fpp-accuracy]

La performance decisionale deve essere valutata sui secondi.

Un modello può adattarsi perfettamente al training set e prevedere male il futuro.

### MAE: quanto sbagliamo nella scala del business

Il **Mean Absolute Error** è la media dell'errore assoluto.

Se per cinque giorni gli errori sono 5, 10, 6, 2 e 12 unità, il MAE è 7.

È facile da spiegare:

> il forecast sbaglia mediamente di circa sette pezzi al giorno.

È particolarmente utile quando un errore di una unità ha un significato relativamente costante.

### RMSE: dare più peso agli errori grandi

Il **Root Mean Squared Error** penalizza maggiormente gli errori grandi perché usa il quadrato dello scostamento prima di fare la media.

Può essere coerente con processi in cui pochi errori estremi sono molto dannosi.

Ma attenzione: usare RMSE non significa automaticamente modellare il vero costo economico. Significa soltanto scegliere una funzione che cresce più rapidamente dell'errore assoluto.

Se il costo reale di stock-out è fortemente asimmetrico, serve ancora una funzione di loss business.

### MAPE: percentuale intuitiva, fragilità reale

Il **Mean Absolute Percentage Error** è popolare perché produce frasi facili:

> errore medio 8%.

Ma quando il valore reale è zero o vicino a zero, il MAPE diventa indefinito o enorme. Hyndman e Athanasopoulos evidenziano questo problema e notano anche altri limiti delle percentage errors.[^fpp-accuracy]

È quindi fragile per:

- SKU slow mover;
- frodi rare;
- incidenti;
- vendite di nuovi prodotti;
- piccoli segmenti;
- serie intermittenti.

### MASE: confrontare serie diverse contro una baseline

Il **Mean Absolute Scaled Error** scala gli errori usando l'errore di una previsione naïve calcolata sul training set. Per serie stagionali, il benchmark può essere seasonal naïve.[^fpp-accuracy]

Il vantaggio è importante:

- è scale-free;
- può confrontare serie con unità e volumi diversi;
- conserva un'interpretazione relativa alla baseline.

In modo intuitivo:

- `MASE < 1` → il modello batte, in media, il benchmark usato per la scala;
- `MASE > 1` → il modello fa peggio.

Non sostituisce la metrica business, ma impedisce di celebrare un modello che non supera una regola elementare.

### Bias: sbagliare sempre dalla stessa parte

Due modelli possono avere lo stesso MAE e comportamento molto diverso.

Modello A alterna sovrastime e sottostime.

Modello B sottostima quasi sempre.

Per una supply chain, un bias negativo persistente può generare stock-out continui anche se l'errore assoluto medio è discreto.

Per questo è utile monitorare anche il **mean forecast error** o altra misura della direzione sistematica degli errori.

### Caso simulato/composito — Il modello migliore in dashboard e peggiore in magazzino

Una società di ricambi industriali confronta due modelli su 3.400 SKU.

| Modello | MAPE medio |
| --- | ---: |
| A | 11,2% |
| B | 9,4% |

B sembra migliore.

Dopo il rollout, però, aumentano gli stock-out dei componenti ad alto valore.

L'analisi mostra che B migliora molto su migliaia di SKU a basso volume ma commette pochi errori molto costosi su circa quaranta componenti critici.

Il MAPE medio assegna a ogni osservazione un peso che non riflette la criticità economica.

Quando il team valuta:

- costo di stock-out;
- margine;
- lead time;
- criticità del ricambio;

il modello A diventa preferibile.

### Accuracy per segmento

Una sola metrica globale può nascondere failure mode importanti.

Conviene almeno segmentare per:

- volume;
- valore economico;
- horizon;
- geografia;
- prodotto;
- promozione vs periodo normale;
- forecastability della serie.

Un modello può essere eccellente sui fast mover e inutile sugli intermittent-demand item.

Questo non implica necessariamente due algoritmi diversi. Implica almeno due diagnosi diverse.

### Accuracy non è la stessa cosa di decision quality

Supponiamo che una previsione di domanda sia usata per ordinare stock.

Il costo può essere:

`loss = costo_stockout × unità_mancanti + costo_overstock × unità_eccesso`

Se stock-out e overstock hanno costi diversi, minimizzare MAE non coincide necessariamente con minimizzare la loss economica.

La decisione potrebbe richiedere un quantile della distribuzione prevista, non la media.

Questa è la connessione tra forecasting e decisione: **la metrica statistica descrive l'errore; la funzione di loss descrive ciò che quell'errore fa al business.**

### Non scegliere la metrica dopo aver visto chi vince

Un rischio pratico è calcolare sei metriche e presentare quella che favorisce il modello preferito.

La metrica primaria dovrebbe essere collegata alla decisione **prima** del confronto finale.

Possiamo comunque riportare più metriche, ma con ruoli chiari:

- metrica primaria di selezione;
- metriche diagnostiche;
- loss economica;
- guardrail.

### Scheda di accuracy

Il Temporal Decision Brief dovrebbe includere:

```text
Metrica primaria:
Perché è coerente con la decisione:
Baseline di confronto:
MAE / RMSE / MASE / altro:
Bias:
Performance per horizon:
Performance per segmenti critici:
Worst-case / P90-P95 dell'errore:
Business loss:
```

> **Il forecast non va ottimizzato per il numero che lo fa sembrare migliore. Va ottimizzato per gli errori che il business non può permettersi.**

[^fpp-accuracy]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Evaluating point forecast accuracy”, https://otexts.com/fpp3/accuracy.html
