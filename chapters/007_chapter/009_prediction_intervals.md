## 7.8 Il forecast non è una linea: distribuzione, intervalli e coverage

Una previsione puntuale come:

> domanda prevista: 12.400 unità

è semplice da comunicare. È anche incompleta quando l'incertezza modifica la decisione.

Hyndman e Athanasopoulos descrivono il forecast come una **distribuzione di possibili valori futuri**; il point forecast è soltanto un riassunto di quella distribuzione. Gli intervalli di previsione rendono visibile una parte dell'incertezza.[^fpp-pi]

### Caso simulato/composito — Ordinare 12.400 non è la stessa cosa che prevedere 12.400

Un produttore deve ordinare un nuovo forno per il mercato italiano.

Il modello produce:

- point forecast: 12.400 unità;
- prediction interval 80%: 11.300–13.600;
- prediction interval 95%: 10.400–14.700.

Se il buyer vede solo 12.400, può trattarlo come un ordine consigliato.

Ma il forecast non conosce il costo della decisione.

Se lo stock-out è molto costoso e il riapprovvigionamento richiede mesi, può essere razionale ordinare sopra il valore centrale. Se l'obsolescenza è costosa e il replenishment è rapido, la decisione può essere più prudente.

La distribuzione di forecast alimenta la decisione. Non la sostituisce.

### Confidence interval e prediction interval

Il Capitolo 5 ha introdotto gli intervalli di confidenza per l'incertezza su una stima.

Qui la domanda è diversa: **quanto può variare una osservazione futura?**

Un prediction interval incorpora la variabilità del futuro prevista dal modello e tende quindi a essere più ampio dell'incertezza su un semplice parametro medio.

Confondere i due intervalli porta a rappresentare il futuro con precisione eccessiva.

### L'orizzonte allarga l'incertezza

Una proprietà comune dei forecast è che l'incertezza aumenta andando avanti nel tempo. Hyndman e Athanasopoulos mostrano che i prediction interval multi-step tendono ad allargarsi con l'horizon.[^fpp-pi]

Se la dashboard mostra la stessa banda stretta a:

- 1 giorno;
- 30 giorni;
- 12 mesi;

serve capire che cosa stia realmente rappresentando.

In alcuni modelli la dinamica può essere particolare, ma una precisione apparentemente invariata a lunghissimo orizzonte merita almeno una verifica.

### Un intervallo dichiarato al 80% deve essere verificato

Stampare “80% prediction interval” non significa che il sistema sia ben calibrato.

Nel backtest possiamo misurare la **coverage**:

> quale quota dei valori futuri osservati è caduta realmente dentro l'intervallo nominale dell'80%?

Se la coverage storica è 52%, gli intervalli sono troppo stretti o le assunzioni non reggono.

Se è 99%, potrebbero essere troppo conservativi per alcune decisioni.

La coverage dovrebbe essere letta anche per:

- horizon;
- segmento;
- regime normale vs promozionale;
- stagione;
- scala della serie.

### Width e coverage devono essere lette insieme

Un intervallo larghissimo può raggiungere facilmente alta coverage e risultare poco utile.

Un intervallo strettissimo è utile solo se rimane calibrato.

Quindi valutiamo almeno:

- **coverage** — quante osservazioni future conteniamo;
- **width** — quanto è ampia la banda;
- **business usefulness** — la banda è abbastanza informativa da cambiare la decisione?

Non basta ottimizzare un singolo numero.

### Caso simulato/composito — Il budget trasformato in promessa

Una società SaaS costruisce il piano annuale sul point forecast del new ARR:

| Trimestre | Point forecast |
| --- | ---: |
| Q1 | 4,8 M€ |
| Q2 | 5,2 M€ |
| Q3 | 5,7 M€ |
| Q4 | 6,1 M€ |

A metà anno il risultato è 9% sotto la linea centrale e parte una revisione dei costi.

L'analisi mostra che il dato reale è ancora dentro un intervallo di previsione che il modello considerava plausibile.

Il problema non è soltanto “forecast error”. È che l'organizzazione ha trasformato la media della distribuzione in una promessa di budget.

Il processo viene ridisegnato con:

- downside;
- base;
- upside;
- trigger espliciti per assunzioni di spesa.

Il forecast diventa una mappa dell'incertezza invece di una falsa certezza.

### Probabilità di superare una soglia

Per molte decisioni non serve sapere il point forecast. Serve sapere:

- probabilità di superare capacità;
- probabilità di stock-out;
- probabilità di scendere sotto una soglia di cassa;
- probabilità di mancare un SLA;
- probabilità di raggiungere un target.

Se la capacità massima è 14.000 unità, una domanda più utile di “forecast = 12.400” è:

> qual è la probabilità che la domanda superi 14.000?

Questo collega direttamente la distribuzione alla decisione.

### Intervalli condizionati alle assunzioni del modello

Un prediction interval non incorpora automaticamente ogni forma di incertezza del mondo reale.

Può non catturare bene:

- un competitor che entra improvvisamente;
- una nuova regolamentazione;
- una promozione non presente nel training;
- una rottura della supply chain;
- un cambio di pricing radicale;
- un errore nella feature pipeline.

La banda è una misura di incertezza **sotto il modello e le sue condizioni**, non un confine metafisico del futuro.

### Forecast distribution e scenari

Quando esistono decisioni note che cambieranno il processo, può essere più utile produrre scenari condizionati:

- forecast con prezzo invariato;
- forecast con +10% di prezzo;
- forecast con nuova capacità;
- forecast con campagna pianificata.

Gli scenari non vanno confusi con quantili della stessa distribuzione. Rispondono a ipotesi di mondo differenti.

### Il campo del Temporal Decision Brief

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

[^fpp-pi]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Distributional forecasts and prediction intervals”, https://otexts.com/fpp3/prediction-intervals.html
