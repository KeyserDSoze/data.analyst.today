## 7.11 Checklist operativa per serie temporali, anomalie e forecast

Prima di costruire o accettare un forecast, un Data Analyst dovrebbe passare attraverso una checklist minima.

### 1. Capire che cosa rappresenta la serie

- Qual è la metrica?
- Qual è la frequenza: ora, giorno, settimana, mese?
- Ci sono giorni mancanti?
- I timestamp sono in event time o processing time?
- Il dato viene revisionato dopo la prima pubblicazione?

### 2. Guardare la serie prima del modello

Verificare almeno:

- trend;
- stagionalità;
- cambi di livello;
- cambi di varianza;
- picchi;
- periodi anomali;
- pattern ricorrenti.

Una linea temporale ben letta può evitare ore di modellazione inutile.

### 3. Controllare la dipendenza temporale

L'autocorrelazione misura quanto i valori della stessa serie siano correlati a lag differenti. NIST evidenzia che è utile sia per rilevare non casualità sia per supportare l'identificazione del modello.

Domande operative:

- il valore di ieri contiene informazione su oggi?
- esiste un pattern a lag 7?
- a lag 12 per dati mensili?
- la dipendenza rimane dopo aver rimosso trend e stagionalità?

### 4. Stabilire una baseline

Prima di introdurre un modello sofisticato, confrontarlo con:

- ultimo valore;
- media storica;
- seasonal naive;
- media mobile;
- semplice trend.

Se un modello complesso non batte una baseline ragionevole fuori campione, la complessità non sta creando valore.

### 5. Validare nel tempo, non randomizzare il passato

Nel forecasting non possiamo trattare il tempo come un normale dataset tabellare.

Il training deve precedere temporalmente la validation. Quando possibile è utile usare rolling-origin evaluation o backtesting su più finestre.

### 6. Misurare più di un errore

Osservare:

- MAE;
- RMSE quando gli errori grandi sono particolarmente costosi;
- MAPE solo quando è appropriato;
- bias;
- errore per segmento;
- errore per orizzonte;
- errore nei periodi critici.

### 7. Cercare l'errore dove costa

Un errore di 20 unità non ha lo stesso significato per tutti i prodotti.

Associare l'errore a:

- margine;
- stock-out cost;
- overstock cost;
- SLA;
- capacità;
- customer impact.

### 8. Non confondere anomalia e dato sbagliato

Per ogni outlier temporale chiedere:

1. il dato è tecnicamente valido?
2. il processo di raccolta era regolare?
3. c'è stato un evento business?
4. l'anomalia è attesa per quel giorno o segmento?
5. la stessa anomalia compare in metriche correlate?

### 9. Comunicare l'incertezza

Mai presentare un forecast importante come una certezza puntuale quando l'incertezza è materialmente rilevante.

Mostrare intervalli, scenari o probabilità di superare soglie operative.

### 10. Esplicitare le condizioni di validità

Ogni previsione dovrebbe poter rispondere a:

> "Che cosa deve rimanere abbastanza simile perché questa previsione continui a essere credibile?"

Prezzi, canali, capacità, campagne, regolamentazione, tracking e mix clienti sono esempi di condizioni che possono rompere il modello.

### 11. Monitorare dopo il deployment

Il lavoro non termina quando il forecast viene pubblicato.

Monitorare:

- errore reale;
- bias;
- coverage degli intervalli;
- drift;
- performance per segmento;
- cambiamenti nelle baseline;
- anomalie nei dati in ingresso.

### Il principio finale

> **Una serie temporale non è una tabella con una colonna data. È un processo che evolve nel tempo, e il tempo contiene informazione.**

### Riferimenti

- NIST, *Autocorrelation*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm
- NIST, *Common Approaches to Univariate Time Series*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc444.htm
