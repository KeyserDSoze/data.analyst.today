## 7.11 Temporal Decision Brief: il deliverable operativo del capitolo

Una buona analisi temporale non termina con un grafico, un alert o un forecast. Termina con una sintesi che renda visibili **che cosa stiamo misurando, quale passato stiamo usando come riferimento, quanta incertezza resta e quale decisione cambia davvero**.

Per questo il **Temporal Decision Brief** deve restare strutturato e scansionabile. Non è una lista editoriale: è un artefatto operativo da compilare durante la review.

### 1. Series contract

```text
Metrica:
Unità:
Grain:
Frequenza:
Timezone:
Event time o processing time:
Politica su missing period:
Revisioni retroattive:
Freshness attesa:
```

Una serie oraria in UTC e una serie in ora locale possono produrre pattern differenti durante il daylight saving time. Una revenue giornaliera che viene revisionata per sette giorni non equivale a una misura “finale” disponibile in tempo reale.

### 2. Decisione e forecast target

```text
Decisione:
Decision owner:
Forecast target:
Forecast origin:
Horizon:
Grain decisionale:
Frequenza di aggiornamento:
```

Il forecast deve essere progettato attorno al momento in cui la decisione viene presa, non attorno alla frequenza più comoda del dataset.

### 3. Baseline temporale

```text
Baseline scelta:
Perché è coerente con il processo:
Eventuali aggiustamenti di calendario:
Che cosa NON controlla:
```

La baseline può essere il periodo precedente, lo stesso giorno della settimana, lo stesso periodo stagionale, una media mobile, drift, seasonal naïve o un forecast già in uso. Conta la coerenza con la domanda, non la semplicità della formula.

### 4. Struttura della serie

```text
Trend:
Stagionalità:
Eventi calendario:
Cicli:
Lag rilevanti:
Autocorrelazione residua:
Cambi di varianza:
Trasformazioni/differenziazione:
```

Non serve riportare ogni test eseguito. Serve rendere visibile quale struttura il modello deve riuscire a rappresentare.

### 5. Anomaly triage

```text
Segnale:
Data health:
Baseline:
Contesto calendario:
Scope/segmenti:
Persistenza:
Classificazione:
- data anomaly
- contextual anomaly
- business anomaly
- structural break
Materialità:
Ipotesi:
Cosa non è dimostrato:
```

Un detector deve poter dire “inusuale” senza trasformarlo automaticamente in “causato da”.

### 6. Baseline model

```text
Baseline:
Accuracy baseline:
Perché è credibile:
Quanto il modello la migliora:
In quali segmenti/horizon NON la migliora:
```

Un modello che non batte una baseline sensata non viene salvato dalla propria complessità.

### 7. Backtest `as-of`

```text
Training window:
Rolling o expanding:
Forecast origins:
Horizon testati:
Feature disponibili as-of:
Data vintage/revisioni:
Periodi speciali inclusi:
Leakage checks:
```

La domanda chiave è: **se fossimo davvero tornati a quella data, avremmo potuto produrre esattamente questa previsione con le informazioni allora disponibili?**

### 8. Accuracy e business loss

```text
Metrica primaria:
MAE:
RMSE se utile:
MAPE se appropriato:
MASE / confronto naïve:
Bias:
P90/P95 error:
Performance per horizon:
Performance per segmento:
Business loss:
```

La metrica primaria deve riflettere il tipo di errore che interessa alla decisione, non soltanto quello che fa apparire migliore il modello.

### 9. Forecast uncertainty

```text
Point forecast:
Prediction interval:
Coverage nominale:
Coverage osservata:
Width per horizon:
Probabilità di soglie critiche:
Scenari:
Incertezze non incluse nel modello:
```

Un intervallo deve essere calibrato e, allo stesso tempo, abbastanza informativo da cambiare una decisione.

### 10. Conditions of validity

Dichiara esplicitamente che cosa deve restare sufficientemente stabile: pricing, mix, capacità, calendario, relazione tra feature e target, tracking e comportamento del mercato. Poi definisci quali eventi obbligano a riaprire la previsione.

### 11. Monitoring e override

```text
Metriche monitorate:
Baseline challenger:
Soglia di deterioramento:
Segnali di drift:
Coverage monitoring:
Retraining/review trigger:
Override umano consentito:
Motivazione obbligatoria:
Valutazione ex-post degli override:
```

Un modello deve avere un processo di uscita e revisione, non soltanto un processo di deployment.

### 12. Decisione finale

Chiudi il brief con quattro righe:

**Forecast:** la nostra migliore stima/distribuzione è ______.

**Uncertainty:** la parte più materialmente incerta è ______.

**Validity:** il risultato è credibile finché ______.

**Decision:** raccomandiamo ______ perché il costo principale dell'errore è ______.

### Template compatto

| Campo | Risposta |
| --- | --- |
| Series contract |  |
| Decisione |  |
| Target / grain |  |
| Origin / horizon |  |
| Baseline temporale |  |
| Trend/stagionalità/calendar |  |
| Lag/autocorrelazione |  |
| Anomaly status |  |
| Baseline model |  |
| As-of validation |  |
| Accuracy |  |
| Business loss |  |
| Prediction interval / coverage |  |
| Conditions of validity |  |
| Drift / monitoring |  |
| Override |  |
| Decisione finale |  |

> **Il Temporal Decision Brief è completo quando un decision maker può capire che cosa il passato rende prevedibile, quale parte del futuro resta incerta, che cosa potrebbe rompere la previsione e come tutto questo modifica l'azione.**

Se contiene soltanto `forecast = 12.400`, non è ancora un brief. È una linea su un grafico.
