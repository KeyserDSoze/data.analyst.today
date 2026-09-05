## 7.8 Il forecast non è una linea: distribuzione, intervalli e coverage

Una previsione puntuale come “domanda prevista: 12.400 unità” è semplice da comunicare, ma spesso troppo povera per una decisione. Hyndman e Athanasopoulos trattano il forecast come una **distribuzione di possibili valori futuri**; il point forecast è soltanto un riassunto di quella distribuzione e gli intervalli di previsione rendono visibile una parte dell'incertezza.[^fpp-pi]

### Caso simulato/composito — Ordinare 12.400 non è prevedere 12.400

Un produttore deve ordinare un nuovo forno per il mercato italiano. Il modello restituisce:

- point forecast: **12.400 unità**;
- prediction interval 80%: **11.300–13.600**;
- prediction interval 95%: **10.400–14.700**.

Il buyer non dovrebbe leggere 12.400 come quantità d'ordine automatica. Se lo stock-out è molto costoso e il riapprovvigionamento richiede mesi, può essere razionale ordinare sopra il centro della distribuzione. Se l'obsolescenza è costosa e il replenishment è rapido, può convenire una decisione più prudente. Il forecast descrive l'incertezza; la policy decide come trasformarla in azione.

Questa distinzione chiarisce anche il rapporto con il Capitolo 5. Un **confidence interval** riguarda l'incertezza su un parametro o una stima; un **prediction interval** riguarda la variabilità di una futura osservazione sotto il modello. Il secondo incorpora la variabilità del futuro e tende quindi a essere più ampio. Confonderli significa rappresentare ciò che accadrà con una precisione che non possediamo.

### L'incertezza cambia con l'orizzonte

Andando più avanti nel tempo, in molti processi aumenta la quantità di futuro che il modello deve ricostruire senza nuovi dati osservati. Gli intervalli multi-step tendono quindi ad allargarsi con l'horizon.[^fpp-pi] Una dashboard che mostra la stessa banda stretta a 1 giorno, 30 giorni e 12 mesi non è necessariamente sbagliata, ma merita una domanda esplicita su che cosa quella banda rappresenti davvero.

### Un intervallo nominale deve guadagnarsi la propria etichetta

Scrivere “80% prediction interval” non garantisce che l'intervallo sia calibrato. Nel backtest misuriamo la **coverage**: quale quota dei valori futuri osservati cade realmente dentro una banda che dichiara copertura dell'80%?

Se la coverage storica è **52%**, gli intervalli sono troppo stretti o le assunzioni non stanno reggendo. Se è **99%**, possono essere così larghi da risultare poco informativi. Coverage e **width** vanno quindi lette insieme: una banda utile deve contenere il futuro con frequenza coerente con il livello nominale senza diventare tanto larga da non cambiare più alcuna decisione.

La verifica deve inoltre essere segmentata per horizon, stagione, regime normale/promozionale e parti del portafoglio. Un intervallo ben calibrato a un giorno può degradare drasticamente a otto settimane.

### Caso simulato/composito — Il budget trasformato in promessa

Una società SaaS pianifica il new ARR annuale usando soltanto il punto centrale:

| Trimestre | Point forecast |
| --- | ---: |
| Q1 | 4,8 M€ |
| Q2 | 5,2 M€ |
| Q3 | 5,7 M€ |
| Q4 | 6,1 M€ |

A metà anno il risultato è 9% sotto la linea e parte una revisione dei costi. L'analisi successiva mostra che il dato reale è ancora dentro un intervallo che il modello considerava plausibile. Il problema non è soltanto l'errore del forecast: l'organizzazione ha trasformato la media della distribuzione in una promessa di budget.

Il processo viene allora ridisegnato con scenari downside, base e upside, collegati a trigger espliciti per le assunzioni di spesa. La previsione smette di fingere certezza e diventa una mappa delle condizioni sotto cui agire.

### La soglia può essere più importante del punto centrale

Molte decisioni non richiedono “qual è la previsione media?”, ma “qual è la probabilità di superare una soglia?”. Se la capacità massima è **14.000 unità**, può essere molto più utile stimare `P(domanda > 14.000)` che discutere se il point forecast sia 12.400 o 12.600.

Lo stesso vale per probabilità di stock-out, di scendere sotto una soglia di cassa, di mancare uno SLA o di raggiungere un target. Qui la distribuzione si collega direttamente alla decisione.

Resta però un limite importante: un prediction interval è condizionato al modello e alle sue condizioni di validità. Non incorpora automaticamente un competitor inatteso, una nuova regolamentazione, una promozione senza precedenti, una rottura della supply chain o un cambio radicale di pricing. Quando sappiamo che il mondo potrebbe cambiare per una decisione specifica, può essere più corretto produrre **scenari condizionati** — prezzo invariato, prezzo +10%, nuova capacità, nuova campagna — invece di fingere che tutti quei mondi appartengano alla stessa distribuzione.

Nel Temporal Decision Brief registriamo quindi:

```text
Point forecast:
Forecast distribution / intervalli:
Coverage nominale:
Coverage osservata nel backtest:
Width per horizon:
Probabilità di superare soglie critiche:
Scenari condizionati:
Fonti di incertezza NON incluse:
Decisione associata:
```

> **Una previsione senza incertezza comunica più precisione di quella che possiede. Una previsione con un intervallo non calibrato comunica rigore senza averlo ancora verificato.**

Il passo successivo è inevitabile: anche un forecast ben validato può smettere di meritare fiducia quando cambia il processo che rendeva utile il suo passato.

[^fpp-pi]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Distributional forecasts and prediction intervals”, https://otexts.com/fpp3/prediction-intervals.html
