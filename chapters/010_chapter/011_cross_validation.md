## 10.11 Cross-validation: misurare stabilità, non produrre una media rassicurante

Un singolo split può essere corretto e comunque fortunato o sfortunato.

La cross-validation aiuta a capire quanto la performance dipende dalla particolare divisione dei dati e supporta model selection e tuning senza consumare subito il test finale.

Ma la domanda più importante resta la stessa della sezione 10.5:

> **quale futuro stiamo cercando di simulare?**

Il numero di fold viene dopo.

### Caso simulato/composito — MedSupply

MedSupply prevede ritardi superiori a 48 ore per ordini ospedalieri.

Un singolo split produce AUC 0,82.

Cinque fold mostrano:

| Fold | AUC |
|---|---:|
| 1 | 0,83 |
| 2 | 0,81 |
| 3 | 0,74 |
| 4 | 0,79 |
| 5 | 0,72 |

Media circa 0,78.

Il valore della cross-validation non è soltanto aver abbassato il numero da 0,82 a 0,78.

I fold peggiori contengono molte più spedizioni internazionali.

Ora abbiamo una nuova domanda:

> il modello generalizza male perché il campione è piccolo, o perché domestic e international sono processi predittivi differenti?

La varianza tra fold è quindi informazione diagnostica, non rumore da nascondere dietro la media.

### Random K-fold non è il default universale

Il classico K-fold casuale è ragionevole quando le osservazioni possono essere considerate exchangeable rispetto al deployment che vogliamo simulare.

È fragile quando esistono:

- tempo;
- gruppi;
- entità ripetute;
- geografie;
- dipendenze tra righe;
- distribuzioni future differenti.

Possiamo avere:

- `GroupKFold` o strategie analoghe per tenere unità correlate nello stesso lato;
- split stratificati per mantenere class balance quando appropriato;
- validazione temporale/forward chaining;
- holdout geografici o di dominio.

Lo strumento deve seguire la prediction task.

### Tempo: non duplicare il Capitolo 7

Per target futuri la validation deve rispettare l'ordine temporale.

Esempio:

```text
train fino a giugno  → validate luglio
train fino a luglio  → validate agosto
train fino ad agosto → validate settembre
```

Il Capitolo 7 ha trattato in dettaglio backtesting e `as-of` validation per serie temporali. Qui il principio è più generale: **nessun fold deve usare per il training informazione cronologicamente successiva alla prediction che sta simulando**, quando il deployment non potrebbe farlo.

### Caso simulato/composito — Finora

Finora costruisce un modello di default.

Random CV:

- AUC media: 0,86.

Forward validation:

- Q1: 0,81;
- Q2: 0,78;
- Q3: 0,75.

Acquisition mix e underwriting sono cambiati nel tempo.

La random CV mescola regimi e risponde a una domanda troppo facile. La sequenza temporale mostra invece un deterioramento che assomiglia al deployment.

### Tuning dentro la validation

Se cross-validation viene usata per scegliere:

- feature;
- regolarizzazione;
- hyperparameter;
- modello;
- calibration method;
- threshold;

quelle scelte appartengono al processo di sviluppo.

La stima riportata come test finale non dovrebbe essere la stessa osservazione usata per ottimizzare continuamente queste decisioni.

Nei progetti con tuning intenso può essere necessario:

- nested CV;
- validation + test holdout;
- oppure un successivo periodo out-of-time realmente untouched.

Non serve applicare nested CV a ogni dashboard predittiva. Serve capire il rischio di selection overfitting del processo di model search.

### Media, dispersione e worst slice

Un report di CV migliore di `mean score = 0,81` può mostrare:

- media;
- deviazione/range tra fold;
- performance per fold;
- composizione dei fold;
- worst-case business slice;
- confronto con baseline nello stesso fold.

Un modello che batte la baseline in 5/5 periodi con margine modesto può essere più affidabile di uno con media maggiore ma che crolla in due periodi critici.

### Validation design statement

Nella Predictive Decision Card scriveremo una frase come:

> **"La validation lascia fuori interi account e rispetta l'ordine temporale perché il modello deve generalizzare sia a clienti nuovi sia a mesi futuri."**

Quella frase comunica più informazione di:

> "abbiamo usato 5-fold CV".

> **La cross-validation non rende automaticamente robusta una valutazione. La rende utile solo quando i fold rappresentano i modi in cui il modello dovrà generalizzare davvero.**
