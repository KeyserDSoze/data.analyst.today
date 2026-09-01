## 7.6 Validare un forecast: ricostruire ciò che avremmo saputo davvero

Un forecast va valutato su **previsioni genuine**, non sulla capacità del modello di spiegare dati che ha già visto.

Hyndman e Athanasopoulos sottolineano che l'accuracy deve essere misurata su dati non usati per il fitting e descrivono la time-series cross-validation come una sequenza di origini di forecast che avanzano nel tempo.[^fpp-tscv]

La regola è semplice:

> **in ogni backtest il modello può usare soltanto informazioni che sarebbero state disponibili al forecast origin.**

Questa è una condizione più forte del semplice “train prima, test dopo”.

### Split temporale minimo

Un primo schema può essere:

```text
train: gennaio 2023 – dicembre 2025
test: gennaio 2026 – giugno 2026
```

È già migliore di uno split casuale, perché il futuro non entra nel training.

Ma un solo periodo di test può essere fortunato o sfortunato.

### Rolling-origin evaluation

Un backtest più informativo può simulare molte previsioni storiche:

```text
origine 1: train fino a gennaio → forecast febbraio
origine 2: train fino a febbraio → forecast marzo
origine 3: train fino a marzo → forecast aprile
...
```

Se la decisione richiede un orizzonte di quattro settimane, ogni origine dovrebbe produrre e valutare anche quel vero orizzonte, non soltanto `h=1`.

Hyndman e Athanasopoulos mostrano esplicitamente che la cross-validation temporale può essere costruita per forecast multi-step e che l'errore tende a cambiare con l'orizzonte.[^fpp-tscv]

### Caso simulato/composito — Il forecast perfetto che conosceva la promozione finale

Un retailer vuole prevedere le vendite giornaliere.

Tra le feature compare `promotion_discount`.

Nel dataset storico il valore rappresenta lo sconto **effettivamente applicato** in ogni giornata. Il modello ottiene un MAE eccezionale.

Quando viene messo in produzione, la performance crolla.

Il motivo emerge ricostruendo il processo reale: al momento in cui il forecast settimanale veniva emesso, molte promozioni erano ancora modificabili e il valore finale dello sconto non era noto.

Il backtest aveva utilizzato una versione dell'informazione che apparteneva al futuro.

### Il concetto chiave: “as-of data”

Per una previsione emessa il 10 marzo alle 8:00, chiediamo:

> quale versione di ogni informazione era realmente conoscibile il 10 marzo alle 8:00?

Questo vale per:

- prezzi;
- promozioni;
- disponibilità stock;
- meteo;
- budget media;
- pipeline commerciale;
- ordini non ancora finalizzati;
- dati finanziari successivamente revisionati.

Un dataset storico “finale” può contenere correzioni che il modello operativo non avrebbe posseduto in tempo reale.

### Leakage temporale oltre le feature ovvie

Fonti frequenti:

- aggregazioni calcolate usando finestre che includono il futuro;
- normalizzazione con media/deviazione standard dell'intero dataset;
- target encoding costruito con periodi successivi;
- `order_status = delivered` usato per prevedere qualcosa avvenuto prima della consegna;
- stock finale della giornata usato in un forecast emesso al mattino;
- dati revisionati retroattivamente;
- calendario promozionale effettivo invece di quello pianificato disponibile all'epoca.

La domanda “questa colonna ha data precedente al target?” non è sufficiente. Conta **quando il valore era conoscibile**.

### Vintage data e revisioni

Alcune metriche cambiano dopo la prima pubblicazione.

Esempi:

- revenue con resi registrati dopo giorni;
- PIL e indicatori macro revisionati;
- attribution marketing ricostruita a posteriori;
- ordini cancellati dopo la chiusura giornaliera.

Se il modello in produzione vede la prima versione ma il backtest usa la versione finale corretta, la validazione può essere troppo ottimista.

Quando il problema è materialmente importante, serve conservare o ricostruire i **data vintages**.

### Backtest rappresentativo della realtà operativa

Un buon backtest dovrebbe attraversare condizioni diverse:

- settimane normali;
- festività;
- promozioni;
- picchi;
- cali;
- periodi di crescita;
- periodi di capacità limitata;
- eventuali cambi di regime rilevanti.

Non per garantire che il passato contenga ogni futuro possibile, ma per evitare di dichiarare robusto un modello testato soltanto nella zona più facile della storia.

### Performance media e worst-case

Due modelli:

| Modello | MAE medio | Peggior settimana |
| --- | ---: | ---: |
| A | 6,2% | 11,4% |
| B | 6,0% | 28,7% |

B vince di poco in media e perde drasticamente nel worst-case.

Se la previsione governa capacità critica, A potrebbe essere preferibile.

Una validazione decisionale guarda quindi anche:

- quantili dell'errore;
- periodi critici;
- bias;
- segmento;
- horizon;
- costo degli errori estremi.

### Il backtest deve includere la baseline

Ogni origine temporale dovrebbe valutare **modello e baseline sullo stesso futuro**.

Non ha senso confrontare:

- modello su un periodo recente difficile;
- baseline su un periodo storico diverso.

La domanda è:

> in quelle stesse condizioni, con la stessa informazione disponibile, il modello avrebbe prodotto una decisione migliore della regola semplice?

### Scheda di validazione

Nel Temporal Decision Brief registriamo:

```text
Forecast origin simulati:
Horizon:
Training window:
Expanding o rolling window:
Data disponibili as-of:
Revisioni/vintage gestiti:
Baseline:
Metriche:
Periodi speciali presenti:
Performance media:
Worst-case / quantili:
Stabilità per segmento e horizon:
```

> **Un backtest credibile non ricostruisce il passato come lo conosciamo oggi. Ricostruisce il passato come avremmo potuto conoscerlo allora.**

[^fpp-tscv]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Time series cross-validation”, https://otexts.com/fpp3/tscv.html
