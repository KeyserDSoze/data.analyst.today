## 4.15 Box plot e IQR: confrontare distribuzioni senza fingere che la media basti

Quando dobbiamo confrontare più gruppi, un istogramma per ciascuno può diventare ingombrante. Il **box plot** comprime centro e dispersione in una forma compatta: mostra mediana, quartili e interquartile range, cioè la larghezza del 50% centrale della distribuzione.

```text
IQR = Q3 - Q1
```

Una convenzione molto diffusa estende i *whisker* fino ai valori compatibili con `Q1 - 1,5 × IQR` e `Q3 + 1,5 × IQR`, segnalando separatamente le osservazioni oltre quei limiti.[^nist-boxplot] La parola importante è **segnalando**. La regola non stabilisce che un punto sia sbagliato e non ordina di eliminarlo.

Consideriamo **FastLane Distribution**, che confronta quattro hub. Le medie dei tempi di consegna sono quasi identiche: Torino 2,8 giorni, Bologna 2,7, Roma 2,9, Napoli 2,8. Se la performance venisse riassunta da quella sola riga, i quattro processi sembrerebbero equivalenti.

Il box plot mostra invece che Bologna ha una parte centrale molto compatta, Torino è un po' più dispersa, Roma ancora di più e Napoli presenta una mediana simile agli altri ma una coda di consegne lente. Per Napoli `Q1 = 2,2`, mediana `2,6`, `Q3 = 3,1` e `IQR = 0,9`; la soglia superiore convenzionale è quindi `4,45` giorni. Nel trimestre **184 spedizioni** la superano e il massimo arriva a 13,8 giorni.

L'indagine sul processo mostra che il 78% di quelle spedizioni lente riguarda due isole minori servite soltanto tre volte a settimana. I punti sono reali e rappresentano esattamente una parte dell'esperienza che Operations deve conoscere. Cancellarli renderebbe il box plot più ordinato, non il servizio più affidabile.

## Il box plot serve soprattutto a formulare la domanda successiva

La lettura utile non è “Napoli ha molti outlier”. È chiedere se la coda appartenga a un segmento identificabile, se il problema sia generalizzato o se una regola operativa produca tempi diversi. A quel punto possiamo confrontare il KPI completo con una sensitivity analysis per segmento senza modificare retroattivamente la definizione della popolazione.

Il box plot, inoltre, comprime anch'esso informazione. Due distribuzioni possono avere quartili quasi identici e forme molto diverse: una unimodale, l'altra bimodale; una concentrata vicino alla mediana, l'altra divisa in due cluster. Quando la forma conta conviene quindi affiancare istogramma o density plot, punti individuali se il campione è gestibile, numerosità del gruppo e percentili operativi come P90 o P95.

Questa complementarità è importante: non stiamo cercando il grafico “migliore” in assoluto, ma una rappresentazione che conservi le proprietà rilevanti per la domanda. Il box plot è particolarmente forte quando vogliamo confrontare rapidamente posizione, dispersione e code tra gruppi.

La stessa esigenza di confronto si presenta anche quando le variabili non sono numeriche. In quel caso la struttura non vive nei quartili ma nelle combinazioni di categorie e nei loro denominatori: il tema della prossima sezione.

> **Una statistica compatta è utile quando sappiamo sia ciò che rende visibile sia ciò che ha dovuto comprimere.**

[^nist-boxplot]: NIST/SEMATECH, *Box Plot*. https://itl.nist.gov/div898/handbook/eda/section3/boxplot.htm
