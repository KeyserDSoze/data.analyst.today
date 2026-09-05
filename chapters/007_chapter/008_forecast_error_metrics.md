## 7.7 Misurare l'errore: accuracy statistica e costo decisionale

Dopo un backtest credibile possiamo misurare gli errori fuori campione. Ma “accuracy” non è un'unica proprietà: la metrica scelta stabilisce **quali errori pesano di più**. Per questo MAE, RMSE, MAPE e MASE non sono quattro modi equivalenti di raccontare la stessa performance.

Hyndman e Athanasopoulos distinguono innanzitutto il **residuo**, calcolato sui dati usati per stimare il modello, dal **forecast error**, che nasce confrontando una previsione genuina con un valore futuro non ancora osservato al momento del forecast.[^fpp-accuracy] Per una decisione ci interessano soprattutto i secondi.

Il **MAE** mantiene l'errore nella scala del business ed è facile da spiegare: se sbagliamo mediamente di sette pezzi, sappiamo cosa significa. Il **RMSE** dà più peso agli errori grandi perché eleva al quadrato gli scostamenti prima di aggregarli. Può essere utile quando pochi errori estremi sono particolarmente indesiderabili, ma non va confuso con una vera funzione di costo economico.

Il **MAPE** è intuitivo perché produce percentuali, ma diventa fragile quando il valore reale è zero o vicino a zero. Hyndman e Athanasopoulos evidenziano proprio questi limiti delle percentage errors.[^fpp-accuracy] Per SKU slow mover, frodi rare, nuovi prodotti o domanda intermittente, una percentuale può diventare indefinita o enorme per ragioni che hanno poco a che fare con la qualità operativa del modello.

Il **MASE** risponde a una domanda diversa: *quanto stiamo facendo meglio o peggio rispetto a una previsione naïve?* Scalando l'errore contro un benchmark costruito sul training set, consente confronti tra serie con scale diverse. In modo intuitivo, `MASE < 1` indica che il modello batte il benchmark usato per la scala; `MASE > 1` che fa peggio. È molto utile, ma non sostituisce il costo reale di sbagliare.

### Il segno dell'errore conta

Due modelli possono avere lo stesso MAE e conseguenze operative opposte. Se uno alterna sovrastime e sottostime mentre l'altro sottostima quasi sempre, una supply chain può ritrovarsi con stock-out persistenti nonostante un errore assoluto medio accettabile. Per questo il **bias** o mean forecast error deve accompagnare le metriche di grandezza.

### Caso simulato/composito — Il modello migliore in dashboard e peggiore in magazzino

Una società di ricambi industriali confronta due modelli su 3.400 SKU:

| Modello | MAPE medio |
| --- | ---: |
| A | 11,2% |
| B | 9,4% |

B sembra vincere nettamente. Dopo il rollout, però, aumentano gli stock-out dei componenti ad alto valore. Il modello B migliora molto su migliaia di SKU a basso volume e commette pochi errori molto costosi su circa quaranta componenti critici.

Il MAPE medio sta dicendo la verità sulla propria funzione matematica e fallendo la decisione economica. Quando il team introduce costo di stock-out, margine, lead time e criticità del ricambio, il modello A diventa preferibile.

La lezione si generalizza. Una sola metrica globale può nascondere failure mode per volume, valore economico, horizon, geografia, categoria, promozione o forecastability. Un modello può essere eccellente sui fast mover e inutile sugli intermittent-demand item senza che la media lo renda evidente.

### Dall'errore alla loss

Se il forecast governa lo stock, una forma concettuale della loss può essere:

`loss = costo_stockout × unità_mancanti + costo_overstock × unità_eccesso`

Quando i due costi sono asimmetrici, minimizzare MAE non coincide necessariamente con minimizzare il danno economico. La decisione può perfino richiedere un quantile della distribuzione prevista anziché il point forecast medio.

Questo è il passaggio essenziale: **la metrica statistica descrive l'errore; la funzione di loss descrive ciò che quell'errore fa al business**.

Per evitare cherry-picking, la metrica primaria dovrebbe essere collegata alla decisione prima del confronto finale. Possiamo comunque riportare MAE, RMSE, MAPE, MASE, bias, quantili e metriche per segmento, ma con ruoli espliciti: selezione, diagnostica, business loss e guardrail.

Nel Temporal Decision Brief la scheda di accuracy può rimanere strutturata:

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

A questo punto conosciamo la performance media e i failure mode. Manca ancora un pezzo: la previsione non è una linea, ma una distribuzione di futuri possibili.

[^fpp-accuracy]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Evaluating point forecast accuracy”, https://otexts.com/fpp3/accuracy.html
