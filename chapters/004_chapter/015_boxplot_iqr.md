## 4.15 Box plot e IQR: vedere centro, dispersione e anomalie insieme

Il box plot è uno dei grafici più compatti dell'analisi esplorativa. In pochi elementi visualizza mediana, quartili, dispersione centrale e valori potenzialmente anomali.

Il cuore del box plot è l'**interquartile range**, o IQR:

\[
IQR = Q3 - Q1
\]

`Q1` è il 25° percentile e `Q3` il 75° percentile. L'IQR contiene quindi il 50% centrale delle osservazioni.

Una convenzione molto usata considera potenziali outlier i valori inferiori a:

\[
Q1 - 1,5 \times IQR
\]

oppure superiori a:

\[
Q3 + 1,5 \times IQR
\]

NIST descrive proprio questa costruzione come una delle varianti standard del box plot per evidenziare valori estremi.[^nist-boxplot]

### Caso: i tempi di consegna sembrano quasi identici

La società logistica **FastLane Distribution** confronta quattro hub italiani. La media del tempo di consegna è sorprendentemente simile:

| Hub | Media giorni |
|---|---:|
| Torino | 2,8 |
| Bologna | 2,7 |
| Roma | 2,9 |
| Napoli | 2,8 |

Un report basato soltanto sulla media potrebbe concludere che i quattro hub hanno performance equivalenti.

I box plot raccontano una storia diversa.

Per Torino, metà delle spedizioni cade tra 2,3 e 3,1 giorni. Per Bologna, tra 2,5 e 2,9. Roma ha una dispersione più ampia, mentre Napoli presenta una coda di consegne molto lente.

A Napoli:

- Q1 = 2,2 giorni;
- mediana = 2,6;
- Q3 = 3,1;
- IQR = 0,9;
- soglia superiore = 4,45 giorni.

Il dataset contiene 184 spedizioni oltre 4,45 giorni, con un massimo di 13,8 giorni.

La media di 2,8 giorni non era falsa. Era incompleta.

### Il punto fuori dal box non è automaticamente un errore

Il responsabile operations propone di eliminare tutte le spedizioni oltre la soglia IQR perché “sono outlier”. È un errore concettuale.

Il criterio IQR segnala valori insoliti rispetto alla distribuzione. Non stabilisce la loro causa.

Le 184 spedizioni vengono quindi investigate. Il 78% riguarda due isole minori servite solo tre volte a settimana. I tempi sono reali e operativamente importanti.

Eliminandoli, il team avrebbe reso il dataset più ordinato ma il modello operativo meno vero.

### Confrontare distribuzioni, non solo singoli numeri

Il box plot è particolarmente utile quando dobbiamo confrontare gruppi:

- sedi;
- prodotti;
- team;
- mercati;
- periodi;
- versioni di un processo.

NIST sottolinea proprio l'utilità dei box plot nel rilevare differenze di posizione e variabilità tra gruppi.[^nist-boxplot]

La lezione è importante: due gruppi possono avere la stessa media e processi molto diversi.

[^nist-boxplot]: NIST/SEMATECH, “Box Plot”, *e-Handbook of Statistical Methods*, https://itl.nist.gov/div898/handbook/eda/section3/boxplot.htm
