## 7.11 Temporal Decision Brief: il deliverable operativo del capitolo

Una buona analisi temporale non termina con un grafico, un alert o un forecast.

Termina con una sintesi che renda visibili:

- ciò che la serie rappresenta;
- quale struttura temporale è stata modellata;
- quale baseline è stata superata;
- quanta incertezza resta;
- in quali condizioni la previsione può fallire;
- quale decisione usa davvero il risultato.

Questo è il **Temporal Decision Brief**.

### 1. Series contract

Prima del modello, definisci la serie.

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

Una serie oraria in UTC e una serie oraria in ora locale possono produrre pattern diversi durante daylight saving time. Una revenue giornaliera che viene revisionata per sette giorni non è la stessa cosa di una misura “finale” disponibile in tempo reale.

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

Dichiara quale confronto rappresenta l'atteso.

Possibili baseline:

- periodo precedente;
- stesso giorno della settimana;
- stesso periodo dell'anno precedente;
- seasonal naïve;
- media mobile;
- drift;
- forecast corrente.

Aggiungi:

> Perché questa baseline è coerente con il processo?

### 4. Struttura della serie

Descrivi sinteticamente:

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

Non serve documentare ogni test. Serve rendere visibile la struttura che il modello deve conoscere.

### 5. Anomaly triage

Per un alert o scostamento importante:

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

Un detector non dovrebbe saltare direttamente da “inusuale” a “causato da”.

### 6. Baseline model

Ogni forecast deve avere un benchmark dichiarato.

```text
Baseline:
Accuracy baseline:
Perché è una baseline credibile:
Quanto il modello la migliora:
In quali segmenti/horizon NON la migliora:
```

Un modello che non batte il seasonal naïve non deve essere salvato dalla sua complessità.

### 7. Backtest as-of

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

La domanda chiave è:

> Se fossimo davvero tornati a quella data, avremmo potuto produrre esattamente questa previsione?

### 8. Accuracy e loss

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

La metrica primaria deve riflettere il tipo di errore che interessa alla decisione.

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

Un intervallo deve essere sia calibrato sia abbastanza stretto da essere utile.

### 10. Conditions of validity

Elenca esplicitamente ciò che il modello assume abbastanza stabile:

- pricing;
- mix;
- capacità;
- calendario;
- relazione tra feature e target;
- sistema di tracking;
- comportamento di clienti/mercato.

Poi definisci quali eventi invalidano o indeboliscono la previsione.

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

Il modello deve avere un processo di uscita, non soltanto un processo di deployment.

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

### La regola finale

Un Temporal Decision Brief è completo quando permette a un decision maker di capire:

> **che cosa il passato rende prevedibile, quale parte del futuro rimane incerta, quali condizioni potrebbero rompere la previsione e come questa incertezza modifica una decisione reale.**

Se contiene soltanto “forecast = 12.400”, non è ancora un brief. È una linea su un grafico.
