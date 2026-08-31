## 10.12 Class imbalance: quando l'accuracy racconta quasi niente

Molti problemi aziendali importanti riguardano eventi rari:

- frodi;
- default;
- churn di clienti premium;
- guasti critici;
- incidenti di sicurezza;
- anomalie operative.

In questi casi la classe positiva può rappresentare una frazione minima delle osservazioni.

### Caso simulato: SafePay e il modello con 99,4% di accuracy

SafePay gestisce pagamenti digitali. Solo lo 0,6% delle transazioni è fraudolento.

Un modello che predice sempre “non frode” ottiene:

**accuracy = 99,4%**

Tecnicamente il numero è corretto.

Operativamente il modello è inutile.

Per problemi sbilanciati bisogna guardare soprattutto:

- precision;
- recall;
- F1;
- PR-AUC;
- costi dei falsi positivi e falsi negativi;
- performance alle soglie operative.

### Il costo degli errori non è simmetrico

Supponiamo che SafePay analizzi 1.000.000 di transazioni al giorno, di cui 6.000 fraudolente.

Modello A:

- recall 92%;
- precision 8%.

Intercetta 5.520 frodi, ma genera circa 63.480 falsi positivi.

Modello B:

- recall 74%;
- precision 31%.

Intercetta 4.440 frodi e genera circa 9.883 falsi positivi.

Qual è migliore?

Non lo decide una formula universale.

Dipende da:

- valore medio della frode;
- costo di revisione manuale;
- danno di bloccare un cliente legittimo;
- capacità del team antifrode;
- obblighi normativi;
- rischio reputazionale.

### ROC-AUC può sembrare ottima mentre l'operatività è pessima

Con eventi molto rari, una ROC-AUC alta non garantisce una precision utile alle soglie reali.

Per questo la precision-recall curve è spesso più informativa nei problemi fortemente sbilanciati.

### Caso simulato: PlantGuard e i guasti critici

PlantGuard vuole prevedere guasti su macchinari industriali.

Solo 1 macchina su 400 ha un guasto critico nel mese successivo.

Il modello raggiunge ROC-AUC 0,91.

La presentazione al management parla di “91% di performance”.

Ma alla soglia scelta per ispezionare le 150 macchine più rischiose:

- 18 sono realmente destinate a guastarsi;
- 132 sono falsi allarmi.

La precision operativa è quindi 12%.

Può comunque essere utile, se un guasto costa centinaia di migliaia di euro e l'ispezione è economica.

Ma questa è una decisione economica, non una proprietà astratta del modello.

### Resampling e class weights

Tecniche come oversampling, undersampling e class weighting possono aiutare il training.

Ma non devono alterare la valutazione finale.

Il test set dovrebbe riflettere, per quanto possibile, la prevalenza reale del problema.

Se bilanci artificialmente anche il test set, rischi di ottenere metriche molto lontane dal comportamento in produzione.

### Metodo operativo

Nei problemi sbilanciati:

1. misura sempre la prevalenza reale;
2. costruisci una confusion matrix alla soglia operativa;
3. calcola precision e recall;
4. traduci FP e FN in costi o conseguenze;
5. valuta la capacità operativa di gestire gli alert;
6. monitora la prevalenza nel tempo.

Il modello non deve semplicemente “distinguere le classi”.

Deve produrre un flusso di decisioni sostenibile.