## 4.15 Box plot e IQR: confrontare distribuzioni senza ridurle a una media

Il box plot è utile perché comprime in poco spazio **posizione e dispersione** di una distribuzione. Mostra la mediana, i quartili, l'intervallo interquartile e, secondo una convenzione molto comune, evidenzia osservazioni lontane dalla parte centrale dei dati.

Il cuore del grafico è l'**interquartile range**, o IQR:

`IQR = Q3 − Q1`

`Q1` è il 25° percentile e `Q3` il 75° percentile. Tra i due si trova quindi il 50% centrale delle osservazioni.

Una costruzione molto diffusa segnala come valori esterni ai *whisker* quelli inferiori a:

`Q1 − 1,5 × IQR`

o superiori a:

`Q3 + 1,5 × IQR`

NIST descrive questa come una delle costruzioni standard del box plot.[^nist-boxplot]

La parola importante, però, è **segnala**. La regola `1,5 × IQR` non dimostra che un valore sia errato e non ordina di cancellarlo.

Nel Capitolo 3 abbiamo già affrontato la domanda di data quality: *questa osservazione rappresenta un fatto reale o un errore?* Qui la domanda è diversa:

> **Che cosa cambia nella nostra lettura quando osserviamo l'intera distribuzione invece della sola media?**

### Caso simulato/composito — Quattro hub con quasi la stessa media

La società logistica immaginaria **FastLane Distribution** confronta quattro hub italiani.

| Hub | Media giorni |
|---|---:|
| Torino | 2,8 |
| Bologna | 2,7 |
| Roma | 2,9 |
| Napoli | 2,8 |

Guardando soltanto la media, i quattro processi sembrano quasi equivalenti.

I box plot cambiano la lettura.

A Bologna il 50% centrale delle consegne è concentrato tra 2,5 e 2,9 giorni. Torino è un po' più dispersa. Roma mostra maggiore variabilità. Napoli ha una mediana simile agli altri hub, ma una coda di consegne molto lente.

Per Napoli:

- `Q1 = 2,2` giorni;
- mediana `= 2,6`;
- `Q3 = 3,1`;
- `IQR = 0,9`;
- soglia superiore convenzionale `= 4,45` giorni.

Nel trimestre 184 spedizioni superano 4,45 giorni e il massimo è 13,8.

La media di 2,8 giorni non era falsa. Era insufficiente per descrivere la stabilità del servizio.

### Un punto fuori dal box non è un ordine di cancellazione

Il 78% delle 184 spedizioni lente riguarda due isole minori servite solo tre volte a settimana. I valori sono reali e rappresentano proprio una parte dell'esperienza che operations deve conoscere.

Eliminarli renderebbe il grafico più ordinato, non il processo migliore.

Per questo, quando un punto estremo influenza molto una conclusione, l'EDA dovrebbe fare un **sensitivity check**:

- risultato con tutte le osservazioni;
- risultato senza il punto o il gruppo influente;
- spiegazione del perché l'osservazione esiste;
- decisione che cambia, oppure non cambia, tra le due letture.

### Il box plot comprime anche informazione

Il vantaggio del box plot è anche il suo limite. Due distribuzioni con quartili simili possono avere forme differenti: una può essere unimodale, un'altra bimodale; una può avere molti punti vicino alla mediana, un'altra due cluster separati.

Per questo, quando la forma conta, è utile affiancare al box plot:

- istogramma o density plot;
- punti individuali, se il campione è gestibile;
- numerosità del gruppo;
- eventualmente P90/P95 quando le code hanno valore operativo.

Il box plot è quindi soprattutto uno strumento di **confronto tra distribuzioni**, non una radiografia completa.

> **Una statistica compatta è utile quando sappiamo anche che cosa sta comprimendo.**

[^nist-boxplot]: NIST/SEMATECH, *Box Plot*, e-Handbook of Statistical Methods: https://itl.nist.gov/div898/handbook/eda/section3/boxplot.htm
