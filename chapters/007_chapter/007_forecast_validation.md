## 7.6 Validare un forecast: il futuro non può essere usato per prevedere il passato

La validazione delle serie temporali richiede disciplina. Nei problemi standard di machine learning è comune dividere casualmente le osservazioni in train e test. Nelle serie temporali questa pratica può produrre leakage.

Se usiamo dati di marzo per prevedere gennaio, anche indirettamente, stiamo facendo qualcosa che in produzione non sarebbe possibile.

### Split temporale

Un'impostazione minima è:

```text
train: gennaio 2023 - dicembre 2025
test: gennaio 2026 - giugno 2026
```

Il modello vede solo il passato e viene valutato sul futuro.

Ma un singolo test può dipendere troppo da un periodo particolare. Per questo è spesso utile il **rolling-origin evaluation**:

```text
train fino a gennaio -> prevedi febbraio
train fino a febbraio -> prevedi marzo
train fino a marzo -> prevedi aprile
...
```

In questo modo osserviamo come il modello si comporta in più condizioni storiche.

### Caso: il forecast perfetto che conosceva il futuro

Un retailer costruisce un modello per prevedere le vendite giornaliere. Tra le feature compare `promotion_discount`.

Durante il training il dataset contiene il valore finale dello sconto effettivamente applicato in ogni giornata. Il modello ottiene risultati eccezionali.

MAE storico: 2.1%.

Quando viene messo in produzione, il team scopre che il piano promozionale viene modificato fino a poche ore prima dell'apertura e che il valore usato nel training non era sempre disponibile al momento in cui il forecast avrebbe dovuto essere prodotto.

In produzione il MAE sale al 9.8%.

Il modello non era davvero così bravo. Aveva accesso a informazione futura.

### Leakage temporale

Possibili fonti di leakage:

- feature aggiornate dopo l'istante di previsione;
- aggregazioni calcolate sull'intero dataset;
- normalizzazioni usando statistiche future;
- target encoding costruito includendo periodi successivi;
- stato finale di un ordine usato per prevedere un evento precedente;
- dati di campagne che al tempo del forecast erano solo pianificati, non confermati.

### Valutare stabilità e non solo media

Supponiamo che due modelli abbiano MAE simile:

| Modello | MAE medio | Peggior settimana |
|---|---:|---:|
| A | 6.2% | 11.4% |
| B | 6.0% | 28.7% |

Il modello B è leggermente migliore in media ma molto più fragile durante settimane anomale.

Per un processo operativo critico, il modello A potrebbe essere preferibile.

### Backtest durante eventi speciali

Un buon test dovrebbe includere, quando possibile:

- festività;
- promozioni;
- settimane normali;
- periodi di crescita;
- periodi di calo;
- cambi di regime;
- condizioni estreme plausibili.

Se il modello viene testato solo nei mesi tranquilli, non sappiamo come reagirà quando servirà davvero.

### Il forecast deve essere riproducibile “as of”

Una domanda utile è:

> **Se tornassimo davvero a quella data, avremmo avuto esattamente queste informazioni disponibili?**

Se la risposta è no, il backtest sta probabilmente sovrastimando la performance.

> **La validazione temporale non misura quanto bene spieghiamo il passato. Misura quanto bene avremmo potuto prevedere un futuro che, in quel momento, non conoscevamo.**
