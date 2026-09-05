## 9.8 Metric sensitivity: una misura deve essere giusta e capace di vedere il cambiamento

Una metrica può essere importantissima per il business e, nello stesso tempo, poco adatta a un esperimento breve. Se l'outcome è raro, molto skewed, estremamente variabile o matura lentamente, il test può essere valido e tuttavia produrre intervalli troppo larghi per distinguere un effetto decision-relevant.

La domanda sulla power diventa quindi una domanda di **metric design**:

> **questa definizione rappresenta bene ciò che ci interessa e possiede abbastanza sensibilità con il traffico disponibile?**

### Caso simulato/composito — Task completati per utente

Un prodotto collaboration testa un suggerimento automatico. Il controllo completa 1,84 task/utente, il trattamento 1,89: `+2,7%`, ma con un intervallo ancora ampio. Il test era stato progettato per rilevare +7%, mentre il business considera utile anche +2%.

In più la distribuzione ha una coda estrema: molti utenti completano 0–2 task, pochi power user decine o centinaia. La frase “non significativo, feature inutile” confonde effetto con capacità di misura. Il test non è abbastanza sensibile per distinguere la zona che ora interessa alla decisione.

Questo non autorizza però a cambiare metrica dopo aver visto il risultato. Provare log transform, winsorization, cap differenti, dodici denominatori e venti segmenti finché qualcosa diventa verde trasforma il metric design in p-hacking. Le alternative devono essere motivate dalla distribuzione e dalla semantica, valutate idealmente su dati pre-esperimento o A/A e congelate prima dell'analisi confermativa.

### Caso reale documentato — Microsoft Teams e Time in App

Microsoft Research descrive un processo di **metric sensitivity analysis** applicato a Bing, MSN e Microsoft Teams. Per `Time in App`, Teams valutò definizioni, trasformazioni e variance reduction e scelse una metrica basata sul log del tempo capped, con variance reduction quando disponibile.[^ms-sensitivity]

La lezione non è usare sempre log o capping. È trattare la metrica come parte del design: una misura rumorosa può rendere invisibili effetti utili o richiedere traffico sproporzionato.

### Sensibilità senza perdere la semantica

Le leve disponibili sono diverse ma appartengono alla stessa decisione. Possiamo scegliere un'aggregazione più coerente con la randomization unit, usare trasformazioni robuste per code estreme, sfruttare covariate pre-treatment, oppure ricorrere a una proxy più precoce quando l'outcome finale matura troppo lentamente.

Ogni leva cambia qualcosa. `time per active user` pesa la popolazione diversamente da `time per user`; una winsorization cambia il contributo dei power user; una proxy di breve termine non diventa magicamente il target lungo termine. La sensibilità non deve essere acquistata sacrificando il significato senza dichiararlo.

Una proxy è accettabile quando il legame con l'outcome più lontano è documentato abbastanza da renderla utile, quando non è facilmente gaming-able e quando guardrail e decisione riconoscono che stiamo stimando **l'effetto sulla proxy**, non garantendo il target futuro.

### Sensitivity significa informazione, non più vittorie

Una metrica migliore non dovrebbe rendere B significativa più spesso per definizione. Dovrebbe produrre intervalli più informativi attorno agli effetti che ci interessano. Se l'effetto reale è vicino a zero, una misura sensibile ci aiuta anche a escludere più chiaramente benefici o danni materialmente grandi.

Per questo la sensitivity analysis va fatta prima del lancio usando storico o A/A: varianza, skewness, zeri, stabilità del denominatore, expected standard error, MDE a diversi orizzonti e guadagno potenziale di variance reduction.

### Metric sensitivity card

```text
Business construct:
Candidate metric:
Randomization unit:
Distribution / skew:
Zeros / rare events:
Variance:
Historical stability:
Expected MDE:
Alternative aggregation:
Transformation justified?
Pre-experiment covariates available?
Proxy vs long-term outcome trade-off:
Chosen definition and interpretation:
```

> **Una metrica sperimentale deve essere semanticamente corretta e statisticamente capace di vedere gli effetti che cambiano la decisione. Se manca una delle due proprietà, il test può essere rigoroso e comunque poco utile.**

[^ms-sensitivity]: Microsoft Research, *Beyond Power Analysis: Metric Sensitivity Analysis in A/B Tests*: https://www.microsoft.com/en-us/research/articles/beyond-power-analysis-metric-sensitivity-in-a-b-tests/
