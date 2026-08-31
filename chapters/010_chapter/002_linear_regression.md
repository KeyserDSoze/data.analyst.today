## 10.2 Regressione lineare: stimare una quantità continua

La regressione lineare prova a rappresentare una variabile numerica come combinazione lineare di una o più feature.

Nella forma più semplice:

\[
y = \beta_0 + \beta_1 x + \varepsilon
\]

Con più variabili:

\[
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_px_p + \varepsilon
\]

Dove:

- `y` è il target;
- `x1...xp` sono le feature;
- `β` sono i coefficienti stimati;
- `ε` rappresenta ciò che il modello non spiega.

La documentazione di scikit-learn descrive `LinearRegression` come ordinary least squares: i coefficienti vengono scelti minimizzando la somma dei quadrati dei residui tra valori osservati e valori predetti.

Fonte: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

### Caso realistico: BrightFoods e il tempo di preparazione ordini

BrightFoods distribuisce prodotti freschi a ristoranti e hotel. Il responsabile operations vuole stimare il tempo necessario per preparare ogni ordine prima che il camion arrivi.

Il dataset contiene 310.000 ordini con:

- numero di righe d'ordine;
- numero di pezzi;
- quota di prodotti refrigerati;
- distanza media tra le zone di picking;
- ora del giorno;
- saturazione del magazzino;
- esperienza media del team di turno;
- minuti effettivi di preparazione.

Un primo modello produce:

\[
\widehat{minutes} = 8.4 + 0.31 \cdot lines + 0.018 \cdot pieces + 6.7 \cdot refrigerated + 11.2 \cdot saturation
\]

Dove `saturation` varia da 0 a 1.

Una lettura superficiale potrebbe dire:

- ogni riga aggiunge 0,31 minuti;
- ogni pezzo aggiunge 0,018 minuti;
- un ordine totalmente refrigerato aggiunge 6,7 minuti;
- passare da magazzino vuoto a piena saturazione aggiunge 11,2 minuti.

Ma qui arriva la parte importante: **un coefficiente non è una legge universale**.

Esprime un'associazione condizionata alle altre variabili incluse nel modello e alla popolazione osservata.

### Residui: il modello parla anche quando sbaglia

Per ogni osservazione:

\[
residuo = y - \hat{y}
\]

Se un ordine richiede 52 minuti e il modello ne prevede 39, il residuo è +13.

Analizzare i residui è fondamentale perché può rivelare:

- non linearità;
- segmenti mancanti;
- errori di misura;
- outlier;
- variabili importanti non incluse;
- cambiamenti di regime.

Nel caso BrightFoods, i residui molto positivi sono concentrati nei turni notturni del deposito di Parma.

L'indagine operativa scopre che durante quel turno una parte degli scanner barcode ha connettività intermittente. Il modello non “ha fallito”: ha fatto emergere un processo che il dataset non rappresentava esplicitamente.

### R² non è una patente di qualità

Il coefficiente di determinazione `R²` indica quanta parte della variabilità osservata viene spiegata dal modello rispetto a una baseline che predice la media.

Un R² alto può essere utile, ma non garantisce che:

- il modello generalizzi;
- le feature siano disponibili in produzione;
- le relazioni siano causali;
- gli errori siano accettabili per il business.

Un modello con R² = 0,91 ma con errori enormi proprio sugli ordini premium può essere peggiore di un modello con R² = 0,84 ma performance stabile nei segmenti critici.

### Errore tipico

> “Il coefficiente della saturazione è 11,2, quindi se riduciamo la saturazione il tempo di preparazione scenderà di 11,2 minuti.”

Non necessariamente.

Questo è un salto da associazione a causalità.

La regressione può supportare la diagnosi e la predizione, ma da sola non identifica automaticamente l'effetto di un intervento.

### Metodo operativo

Quando usi una regressione lineare:

1. definisci bene il target;
2. controlla disponibilità temporale delle feature;
3. esplora relazioni e distribuzioni;
4. stima il modello;
5. guarda i residui;
6. valuta il modello su dati non usati per il training;
7. segmenta gli errori;
8. interpreta i coefficienti con prudenza;
9. collega il modello alla decisione reale.
