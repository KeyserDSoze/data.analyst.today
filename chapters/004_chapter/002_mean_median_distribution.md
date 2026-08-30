## 4.1 Media, mediana e forma della distribuzione

La media risponde a una domanda precisa: quale valore otterremmo se distribuissimo uniformemente il totale tra tutte le osservazioni?

È utile, ma non è sempre rappresentativa dell'esperienza tipica.

La mediana, invece, è il valore che divide la distribuzione in due metà: il 50% delle osservazioni è sotto e il 50% sopra.

Quando una distribuzione è fortemente asimmetrica, media e mediana possono raccontare storie molto diverse.

### Caso: lo stipendio medio dell'azienda

Una startup tecnologica di 41 persone comunica internamente che lo stipendio medio annuo è 62.400 euro.

La cifra sembra descrivere un'organizzazione con compensi piuttosto elevati.

L'analista HR guarda la distribuzione:

- 18 persone guadagnano tra 32.000 e 40.000 euro;
- 13 tra 40.000 e 55.000;
- 6 tra 55.000 e 75.000;
- 3 dirigenti guadagnano oltre 140.000 euro;
- il CEO guadagna 260.000 euro.

La mediana è 46.800 euro.

Dire che il dipendente "medio" guadagna 62.400 euro sarebbe quindi fuorviante se il nostro obiettivo fosse descrivere l'esperienza tipica.

La media non è sbagliata. Risponde semplicemente a una domanda diversa.

### Cosa guardare oltre al valore centrale

Una buona analisi descrittiva considera almeno:

- valore medio;
- mediana;
- minimo e massimo;
- quartili;
- percentili utili al contesto;
- dispersione;
- forma della distribuzione;
- presenza di code lunghe o più modalità.

### Il percentile come linguaggio operativo

In molti problemi reali il percentile è più utile della media.

Un team di customer support può avere un tempo medio di risposta di 3 ore. Ma se il 95° percentile è 18 ore, significa che una parte non trascurabile dei clienti vive un'esperienza molto peggiore di quella suggerita dalla media.

Per questo nei sistemi operativi si usano spesso metriche come P90, P95 e P99.

### Regola pratica

Prima di riportare una media, chiedersi sempre:

1. la distribuzione è simmetrica?
2. ci sono valori estremi?
3. la media descrive davvero un'esperienza tipica?
4. un percentile sarebbe più utile per la decisione?
