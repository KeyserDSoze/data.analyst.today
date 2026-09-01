## 10.10 Regularizzazione: preferire pattern stabili a coefficienti spettacolari

Quando un modello ha abbastanza libertà da inseguire rumore, possiamo introdurre una preferenza esplicita per soluzioni più semplici.

La regularizzazione fa esattamente questo: accetta un po' meno fit sul training set in cambio di maggiore stabilità fuori campione.

Nei modelli lineari due famiglie classiche sono:

- **L2 / Ridge:** riduce coefficienti grandi senza portarli normalmente a zero;
- **L1 / Lasso:** può portare alcuni coefficienti esattamente a zero.

Per un Data Analyst la parte importante non è memorizzare la penalizzazione. È capire **quale problema operativo stiamo cercando di ridurre**.

### Caso simulato/composito — BrightTel e 180 segnali di churn

BrightTel costruisce una regressione logistica di churn con 180 feature.

Una variabile rara identifica 73 clienti con una combinazione specifica di device, offerta e canale. Sul training set è fortemente associata al target e riceve un coefficiente enorme.

Nei periodi successivi il pattern quasi scompare.

Confronto:

| Modello | AUC train | AUC validation |
|---|---:|---:|
| penalizzazione debole | 0,88 | 0,74 |
| L2 più forte | 0,83 | 0,77 |
| L1 | 0,81 | 0,76 |

Il modello L2 "perde" cinque punti sul training e guadagna tre punti dove conta.

Questa è l'intuizione della regularizzazione.

### Regularizzazione e feature correlate

Supponiamo di avere:

- spesa 30 giorni;
- spesa 28 giorni;
- ordini 30 giorni;
- AOV;
- revenue 30 giorni.

Le feature contengono informazione sovrapposta.

Con L1 una può rimanere e altre essere portate a zero. Questo non significa che le feature eliminate siano concettualmente inutili o causalmente irrilevanti. Significa che, **per quella soluzione predittiva**, il modello può ottenere una performance simile usando un sottoinsieme.

Con feature fortemente correlate, la selezione può essere instabile tra campioni.

Quindi "coefficiente zero" non deve diventare una conclusione sul business.

### Regularizzazione come hyperparameter

La quantità di penalizzazione deve essere scelta usando validation/cross-validation coerente con il deployment.

Troppo poca:

- coefficienti instabili;
- variance elevata;
- overfitting.

Troppa:

- pattern reali compressi;
- underfitting;
- ranking meno utile.

Il valore ottimale non è una proprietà universale del dataset. Dipende anche da split, metrica e popolazione futura.

### Stabilità dei coefficienti

Nei modelli interpretabili conviene guardare non soltanto il coefficiente finale, ma quanto cambia tra:

- fold;
- periodi temporali;
- bootstrap/campioni;
- versioni del modello.

Un coefficiente che cambia segno continuamente può essere un segnale di:

- multicollinearità;
- poco supporto dati;
- instabilità del processo;
- feature engineering fragile.

La regularizzazione può attenuare il problema, ma la diagnosi resta importante.

### Quando aiuta

La regularizzazione è particolarmente utile quando:

- il numero di feature è elevato;
- esistono feature ridondanti;
- alcuni coefficienti sono estremi;
- il train-validation gap è elevato;
- vogliamo un modello più parsimonioso;
- la performance è sensibile a piccole variazioni del training set.

### Che cosa non risolve

Non corregge automaticamente:

- leakage;
- label definita male;
- train-serving skew;
- selection bias nella popolazione;
- concept drift;
- mancata calibration;
- causalità confusa con prediction.

Un modello regolarizzato su dati sbagliati è semplicemente un modello più disciplinato che impara il problema sbagliato.

> **Regularizzare significa imporre un prezzo alla complessità statistica. Non significa risolvere la complessità semantica del problema.**
