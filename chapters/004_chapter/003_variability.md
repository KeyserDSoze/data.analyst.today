## 4.2 Variabilità: la parte del fenomeno che il centro non racconta

Due processi possono avere la stessa media e produrre esperienze operative completamente diverse. Per questo la dispersione non è un'aggiunta tecnica al riepilogo: spesso è ciò che determina capacità di pianificazione, rischio, affidabilità e qualità del servizio.

Immaginiamo due centri logistici che processano entrambi, in media, **118 ordini per addetto al giorno**. Nel magazzino A quasi tutti i valori delle ultime sei settimane cadono tra 108 e 128; nel magazzino B alcuni giorni scendono a 65 e altri superano 170. La media coincide, ma il primo processo è molto più prevedibile. Nel secondo la stessa capacità media convive con un'incertezza operativa molto maggiore.

Non possiamo ancora dire perché. Turni, mix di ordini, sistemi, domanda o staffing possono produrre quella dispersione. L'EDA deve prima descrivere la differenza senza trasformarla in una causa: **la media rappresenta il comportamento abituale del magazzino A molto meglio di quello del magazzino B**.

Le diverse misure di variabilità sono modi differenti di comprimere questa informazione. Il **range**, `massimo - minimo`, è immediato ma dipende completamente da due osservazioni e può esplodere per un singolo caso eccezionale. È utile come primo segnale, non come descrizione completa.

La **varianza** incorpora invece gli scarti quadratici dalla media, mentre la **deviazione standard** riporta quella dispersione nell'unità originale della variabile. Un processo con `media = 100` e `SD = 4` racconta una storia molto diversa da uno con `media = 100` e `SD = 38`, anche se il centro è identico. Poiché però deviazione standard e media sono entrambe sensibili ai valori estremi, nelle distribuzioni asimmetriche può essere più informativo affiancare la mediana all'**interquartile range**:

```text
IQR = Q3 - Q1
```

L'IQR descrive la larghezza del 50% centrale della distribuzione. Media + deviazione standard e mediana + IQR non sono coppie concorrenti: osservano aspetti differenti e diventano più o meno utili a seconda della forma del fenomeno.

Quando dobbiamo confrontare dispersioni su scale molto diverse possiamo incontrare anche il **coefficiente di variazione**, `SD / media`. Una deviazione standard di 10 euro pesa molto se la media è 20 e molto poco se è 2.000. Il CV rende questa differenza relativa, ma perde interpretabilità quando la media è vicina a zero o la scala non ha uno zero significativo. Anche qui, la formula non sostituisce il contesto.

## La variabilità può essere struttura, non rumore

Una dispersione ampia non è necessariamente qualcosa da “ripulire”. Può essere il segnale che abbiamo mescolato segmenti con comportamenti diversi, che esiste stagionalità, che il processo cambia tra condizioni operative o che il rischio è davvero concentrato in una coda.

Questo cambia il modo di esplorare. Se la variabilità complessiva è alta ma ogni segmento è internamente stabile, il problema può essere soprattutto di **composizione**. Se invece ogni segmento resta molto disperso, stiamo osservando un fenomeno diverso. La domanda non è quindi come ridurre la deviazione standard nel dataset, ma **come è organizzata la variabilità e quale parte conta per la decisione**.

Per esempio, dire “il tempo medio di evasione è 4,2 ore” lascia il processo quasi invisibile. Dire “la mediana è 3,7 ore; metà degli ordini cade tra 2,8 e 5,1 ore, mentre una coda di casi molto lenti porta la media a 4,2” rende visibili insieme centro, dispersione e asimmetria.

La sezione successiva entra proprio in quella coda. In molti processi operativi il costo più importante non vive vicino alla media, ma nei casi peggiori.

> **La dispersione non è un dettaglio statistico attorno al centro. È spesso la parte della distribuzione che determina rischio, capacità e qualità dell'esperienza.**
