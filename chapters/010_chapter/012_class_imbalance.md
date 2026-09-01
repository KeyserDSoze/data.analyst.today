## 10.12 Class imbalance: il problema non è avere pochi positivi, ma decidere con un base rate raro

Frode, guasto critico, default e incidenti di sicurezza hanno spesso una caratteristica comune: l'evento positivo è raro.

Questo non rende automaticamente il dataset "sbagliato". È spesso il mondo reale.

Il problema è che molte metriche e intuizioni cambiano radicalmente quando il base rate è basso.

### Caso simulato/composito — SafePay

SafePay processa 1.000.000 di transazioni al giorno. Lo 0,6% è frode confermata:

- positivi: 6.000;
- negativi: 994.000.

Un modello che predice sempre "non frode" ottiene accuracy 99,4%.

Il risultato non è un paradosso. È la dimostrazione che l'accuracy risponde a una domanda poco utile in questo contesto.

La sezione 10.7 ha già introdotto precision, recall e PR-AUC. Qui il punto è capire che **prevalenza, training strategy e operating capacity devono rimanere coerenti**.

### Due modelli, due code molto diverse

Supponiamo:

**Modello A**
- recall: 92%;
- precision: 8%.

Circa 5.520 frodi intercettate e oltre 63.000 falsi positivi.

**Modello B**
- recall: 74%;
- precision: 31%.

Circa 4.440 frodi intercettate e meno di 10.000 falsi positivi.

Quale modello è migliore?

Dipende da:

- valore medio della frode;
- capacità della coda manuale;
- costo del blocco errato;
- disponibilità di un secondo controllo automatico;
- requisiti normativi;
- rischio reputazionale.

Con 8.000 review disponibili, il modello A potrebbe essere inutilizzabile senza un operating threshold molto più severo, anche se il recall massimo è maggiore.

### Resampling cambia il training distribution

Per aiutare il modello possiamo usare:

- class weights;
- oversampling;
- undersampling;
- metodi sintetici, quando appropriati.

Queste tecniche modificano il modo in cui il learner vede le classi durante il training.

Non dovrebbero però trasformare artificialmente il test finale in un mondo 50/50 se in produzione il base rate è 0,6%.

Altrimenti precision e valori probabilistici possono diventare difficili da trasferire alla realtà.

### Calibration e prevalenza

Quando il base rate cambia, anche la calibration può cambiare.

Un modello addestrato in un periodo con 0,6% di frode può mantenere un ranking ragionevole in un periodo con 1,2%, ma sottostimare sistematicamente le probabilità.

Quindi in problemi rari monitoriamo separatamente:

- prevalenza reale;
- score distribution;
- ranking;
- precision/recall agli operating point;
- calibration.

### Caso simulato/composito — PlantGuard

PlantGuard prevede guasti critici: circa 1 macchina su 400 ha un guasto nel mese successivo.

Il modello ha ROC-AUC 0,91.

Il maintenance team può ispezionare 150 macchine al mese.

Nel top 150:

- 18 avranno davvero un guasto;
- 132 no.

Precision: 12%.

La slide "AUC 0,91" non dice se 12% sia buono o cattivo.

Se un'ispezione costa 300 euro e un guasto non prevenuto costa 150.000 euro, il ranking può avere enorme valore anche con molti falsi positivi.

Se l'ispezione richiede fermare l'impianto due giorni, la decisione cambia.

### Rare outcome e label delay

Gli eventi rari generano anche un problema di monitoring: servono più osservazioni o più tempo per capire se la performance è cambiata.

Su un segmento con 20 positivi al mese, oscillazioni di precision possono essere enormi per puro rumore.

Perciò soglie di alert e retraining devono considerare:

- volume dei positivi;
- intervalli/variabilità;
- aggregazione temporale;
- costo di reagire troppo spesso.

### La metrica naturale può essere la capacità

In molti sistemi il vincolo principale è `K`:

- 500 review;
- 2.000 chiamate;
- 100 ispezioni;
- 1% del traffico.

La domanda diventa allora:

> **quanto valore o quanti positivi concentriamo nella capacità che possiamo davvero usare?**

Questo collega direttamente ranking e operations.

> **Con classi rare, la prevalenza non è un dettaglio statistico. È il contesto che determina quanti falsi positivi dobbiamo attraversare per trovare ogni positivo e quindi se il modello è operativamente sostenibile.**
