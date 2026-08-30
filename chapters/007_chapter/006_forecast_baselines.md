## 7.5 Forecasting: prima di un modello sofisticato serve una baseline

Fare forecasting significa stimare valori futuri usando informazione disponibile nel presente e nel passato. Ma una previsione non è utile solo perché è prodotta da un modello.

La domanda giusta non è:

> “Qual è il modello più avanzato che possiamo usare?”

La domanda giusta è:

> “Possiamo prevedere meglio di una regola semplice, in modo abbastanza stabile da migliorare una decisione?”

### Baseline semplici

Prima di confrontare ARIMA, exponential smoothing, Prophet, modelli gradient boosting o reti neurali, conviene costruire baseline banali ma forti.

Esempi:

**Naive forecast**

```text
forecast di domani = valore di oggi
```

**Seasonal naive**

```text
forecast del prossimo lunedì = valore del lunedì precedente
```

**Media mobile**

```text
forecast = media degli ultimi k periodi
```

**Media stagionale**

```text
forecast di dicembre = media dei dicembre comparabili
```

Se un modello complesso non supera stabilmente queste baseline, la complessità non sta comprando valore.

### Caso: il modello da 14 feature battuto dal “martedì scorso”

Una catena di supermercati vuole prevedere le transazioni giornaliere per pianificare i turni. Il team costruisce un modello con:

- temperatura;
- precipitazioni;
- promozioni;
- festività;
- traffico web;
- calendario scolastico;
- prezzo medio;
- lag multipli;
- indicatori territoriali.

Nel test storico il modello ottiene un MAE di 5.480 transazioni giornaliere.

Poi un analista propone una baseline seasonal naive:

```text
forecast_t = transazioni_(t-7)
```

MAE: 5.210.

La baseline semplice è migliore.

Il fallimento non significa che le feature siano inutili. Significa che il processo ha una forte struttura settimanale e che il modello complesso, così com'è stato costruito e validato, non aggiunge abbastanza informazione.

### Forecasting e decisione

Il forecast deve essere collegato a una decisione.

Se stiamo prevedendo domanda per il personale, un errore di +500 e uno di -500 non hanno necessariamente lo stesso costo. Sovrastimare può generare ore inutilizzate; sottostimare può generare code, SLA violati e clienti persi.

Per questo la metrica di errore non dovrebbe essere scelta solo per abitudine.

### Horizon

La qualità del forecast dipende dall'orizzonte:

- 15 minuti avanti;
- 1 giorno;
- 7 giorni;
- 3 mesi;
- 2 anni.

Un modello eccellente a un giorno può essere mediocre a 30 giorni.

Nel reporting è utile mostrare performance per orizzonte, non un solo numero aggregato.

### Caso: inventory planning

Un distributore B2B prevede domanda per 6.000 SKU. Il forecast a 7 giorni è abbastanza preciso per il replenishment rapido. A 90 giorni l'incertezza aumenta molto, ma il business usa comunque il punto centrale del forecast come se fosse una certezza per acquistare stock.

Risultato: sovraccumulo su prodotti lenti e stockout sui prodotti soggetti a promozioni.

Il problema non è solo il modello. È l'uso di una previsione puntuale senza considerare l'incertezza e senza distinguere l'orizzonte operativo.

> **Un forecast è uno strumento decisionale sotto incertezza, non una dichiarazione sul futuro.**

## Fonti

- NIST, *Introduction to Time Series Analysis*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
- NIST, *Triple Exponential Smoothing*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc435.htm
