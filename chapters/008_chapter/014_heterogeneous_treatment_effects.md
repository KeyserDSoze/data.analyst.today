## 8.13 Effetti eterogenei: la media può nascondere chi beneficia davvero

Un trattamento può avere un effetto medio positivo e contemporaneamente essere inutile o dannoso per alcuni segmenti.

Questo problema è centrale nelle decisioni reali.

### Caso realistico: programma di retention

Una piattaforma subscription testa una campagna di retention su clienti a rischio.

Effetto medio sul churn a 60 giorni:

- controllo: **18,4%**;
- trattamento: **15,9%**;
- effetto medio: **-2,5 punti percentuali**.

La campagna sembra funzionare.

Segmentando per anzianità cliente:

| Segmento | Effetto sul churn |
|---|---:|
| < 3 mesi | -0,3 pp |
| 3-12 mesi | -3,8 pp |
| > 12 mesi | -5,1 pp |

Segmentando per valore cliente:

| Segmento | Effetto sul churn |
|---|---:|
| basso valore | -0,7 pp |
| medio valore | -2,9 pp |
| alto valore | -6,4 pp |

La domanda operativa cambia: non "la campagna funziona?", ma **per chi funziona abbastanza da giustificare il costo?**

### ATE, ATT e CATE

In termini intuitivi:

- **ATE**: effetto medio nella popolazione;
- **ATT**: effetto medio sui trattati;
- **CATE**: effetto medio condizionato a caratteristiche o segmenti.

Il CATE è spesso molto vicino alla domanda che interessa davvero al business.

### Attenzione alla pesca nei segmenti

Dopo un esperimento è facile esplorare decine di segmentazioni finché qualcosa appare interessante.

Con 40 segmenti, alcune differenze apparenti emergeranno anche per puro caso.

Quindi l'analisi degli effetti eterogenei deve distinguere:

- segmenti ipotizzati prima dell'analisi;
- segmenti esplorativi;
- risultati replicati;
- risultati fragili su campioni piccoli.

### Caso pricing

Un marketplace aumenta la commissione del 5% al 5,5%.

Effetto medio sul numero di seller attivi: **-1,2%**.

Ma il dettaglio mostra:

- seller enterprise: -0,1%;
- seller mid-market: -0,8%;
- seller piccoli con margine basso: -6,7%.

Una media apparentemente innocua nasconde una forte concentrazione dell'impatto.

La decisione potrebbe diventare una struttura di pricing differenziata anziché un rollback totale.

### Modelli complessi non eliminano il problema causale

Tecniche di machine learning possono aiutare a stimare eterogeneità, ma non trasformano automaticamente dati osservazionali in evidenza causale.

Prima serve un disegno credibile per l'effetto causale. Poi possiamo studiare come quell'effetto varia.

### Regola pratica

> **L'effetto medio risponde a una domanda statistica. La decisione spesso richiede sapere dove l'effetto è grande, piccolo, nullo o negativo.**
