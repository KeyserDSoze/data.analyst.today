## 9.8 Metric sensitivity: quando il problema non è il prodotto ma la misura

Nel Capitolo 5 abbiamo definito la potenza statistica.

Nel lavoro sperimentale quotidiano la domanda utile è spesso più concreta:

> **La metrica scelta è abbastanza sensibile da vedere un cambiamento decision-relevant con il traffico che abbiamo?**

Una metrica può essere importante per il business e contemporaneamente pessima come strumento sperimentale di breve periodo.

### Caso simulato/composito — Task completati per utente

Un prodotto collaboration testa un suggerimento automatico.

Dopo il test:

- controllo: 1,84 task completati/utente;
- trattamento: 1,89;
- delta: +2,7%;
- intervallo ancora ampio.

Il test era stato progettato per rilevare un aumento del 7%, ma il business considera interessante anche +2%.

Inoltre la metrica ha una coda estrema:

- molti utenti completano 0–2 task;
- pochi power user ne completano decine o centinaia.

Dire semplicemente:

> “Non significativo, feature inutile.”

sarebbe una lettura sbagliata.

L'esperimento non è abbastanza sensibile per la domanda che il team ha scoperto di avere.

### Non progettare la metrica dopo aver visto l'effetto

Esiste però un rischio opposto.

Se dopo un test piatto proviamo:

- log transform;
- winsorization;
- cap a percentili diversi;
- 12 denominatori;
- 20 segmenti;

finché una variante diventa significativa, abbiamo trasformato metric design in p-hacking.

Le trasformazioni e alternative devono essere:

- motivate da distribuzione e semantica;
- idealmente valutate su dati pre-esperimento o test storici;
- dichiarate prima dell'analisi confermativa del nuovo test.

### Caso reale documentato — Microsoft Teams e Time in App

Microsoft Research descrive un processo di **metric sensitivity analysis** usato su metriche di Bing, MSN e Microsoft Teams. Per `Time in App`, Teams valutò differenti definizioni, trasformazioni e tecniche di variance reduction; la soluzione scelta fu una metrica basata sul **log del tempo capped**, applicando variance reduction quando possibile.[^ms-sensitivity]

La lezione non è “usa sempre il log”.

È:

> **metric design è parte del disegno sperimentale. Una metrica rumorosa può rendere invisibili effetti utili oppure richiedere traffico sproporzionato.**

### Cinque leve di sensibilità

#### 1. Definizione della metrica

Una metrica più vicina al comportamento influenzato dal trattamento può muoversi più facilmente.

Ma una proxy troppo locale può perdere il legame con il valore business.

#### 2. Aggregation level

`time per user`, `time per active user`, proportion of users above a threshold e altre aggregazioni pesano le unità in modi differenti.

La scelta deve rispettare l'unità di randomizzazione e la decisione.

#### 3. Trasformazioni robuste

Per distribuzioni estremamente skewed possono essere utili:

- log transform;
- capping/winsorization predefiniti;
- metriche robuste.

Ma ogni trasformazione cambia interpretazione e weighting.

#### 4. Covariate pre-experiment

Informazione raccolta prima del trattamento può spiegare parte della varianza e aumentare precisione senza introdurre post-treatment bias.

Questo è il principio alla base di CUPED, che vedremo subito dopo.

#### 5. Outcome più precoce o proxy

Un outcome di lungo termine può essere troppo lento per un esperimento di due settimane.

Possiamo considerare una proxy se:

- ha relazione documentata col target lungo termine;
- non è facilmente gaming-able;
- esistono guardrail;
- la decisione riconosce che stiamo stimando un effetto sulla proxy, non direttamente sul target futuro.

### Sensitivity non significa “più significatività”

Una metrica sensibile non deve produrre più vittorie.

Deve produrre **intervalli più informativi** attorno agli effetti che ci interessano.

Se l'effetto reale è zero, una metrica più sensibile dovrebbe aiutarci anche a escludere più chiaramente effetti materialmente positivi o negativi.

### Pre-experiment sensitivity analysis

Prima del lancio possiamo usare storico o A/A data per stimare:

- varianza;
- skewness;
- frequenza di zeri;
- stabilità del denominatore;
- expected standard error;
- MDE a vari orizzonti;
- guadagno potenziale di CUPED;
- sensitivity per segmenti e randomization unit.

Questo trasforma la domanda da:

> “Quale metrica ci piace?”

A:

> “Quale definizione rappresenta bene la decisione **e** è misurabile con il sistema sperimentale disponibile?”

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

> **Una metrica sperimentale deve essere semanticamente giusta e statisticamente capace di muoversi. Se manca una delle due proprietà, il test può essere corretto e comunque poco utile.**

[^ms-sensitivity]: Microsoft Research, *Beyond Power Analysis: Metric Sensitivity Analysis in A/B Tests*: https://www.microsoft.com/en-us/research/articles/beyond-power-analysis-metric-sensitivity-in-a-b-tests/
