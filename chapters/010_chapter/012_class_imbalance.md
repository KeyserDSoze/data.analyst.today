## 10.12 Class imbalance: il base rate decide quanto costa trovare ogni positivo

Frode, guasto critico, default e incidenti di sicurezza hanno spesso eventi positivi rari. Questo non rende il dataset sbagliato: spesso descrive esattamente il mondo reale. Il problema è che, con base rate basso, metriche e intuizioni cambiano significato operativo.

### Caso simulato/composito — SafePay

SafePay processa **1.000.000 di transazioni al giorno** e lo **0,6%** è frode confermata: 6.000 positivi e 994.000 negativi. Un modello che predice sempre “non frode” ottiene accuracy **99,4%**. La metrica è corretta e risponde alla domanda sbagliata.

La domanda utile è quanta frode riusciamo a concentrare nella capacità di intervento senza generare un volume ingestibile di falsi positivi.

Supponiamo due modelli:

**Modello A**: recall 92%, precision 8%. Intercetta circa **5.520** frodi ma genera oltre **63.000 falsi positivi**.

**Modello B**: recall 74%, precision 31%. Intercetta circa **4.440** frodi e produce meno di **10.000 falsi positivi**.

Se il team dispone di 8.000 review, nessuno dei due numeri “vince” in astratto. Servono costo della frode, costo del blocco errato, capacità, eventuale secondo controllo e vincoli normativi. L'operating point fa parte della valutazione.

### Il training può essere riequilibrato; il test deve restare realistico

Class weights, oversampling, undersampling o metodi sintetici possono aiutare il learner durante il training. Queste tecniche cambiano la distribuzione che il modello vede mentre impara.

Non dovrebbero però trasformare il test finale in un mondo artificiale 50/50 quando la produzione ha prevalenza 0,6%. Precision, expected alert volume e probabilità calibrate dipendono dal base rate reale. La valutazione deve quindi tornare alla popolazione che alimenterà la decisione.

### Calibration e prevalenza possono muoversi separatamente dal ranking

Un modello addestrato con frode 0,6% può continuare a ordinare abbastanza bene i casi quando la prevalenza sale all'1,2%, ma sottostimare sistematicamente le probabilità. Per questo monitoriamo separatamente prevalenza, score distribution, ranking, precision/recall agli operating point e calibration.

### Caso simulato/composito — PlantGuard

PlantGuard prevede guasti critici: circa **1 macchina su 400** ha un guasto nel mese successivo. Il modello ha ROC-AUC **0,91** e il team può ispezionare 150 macchine al mese. Nel top 150:

- 18 avranno davvero un guasto;
- 132 no;
- precision = **12%**.

La slide “AUC 0,91” non dice se 12% sia buono. Se un'ispezione costa 300 € e un guasto non prevenuto 150.000 €, il ranking può creare enorme valore. Se l'ispezione richiede due giorni di fermo impianto, la policy cambia.

### Eventi rari significano anche label lente e metriche rumorose

Su un segmento con 20 positivi al mese, precision e recall possono oscillare molto per puro rumore. Alert e retraining trigger devono quindi considerare volume dei positivi, variabilità, finestra temporale e costo di reagire troppo spesso.

Spesso il vincolo più naturale è direttamente `K`: 500 review, 2.000 chiamate, 100 ispezioni, 1% del traffico. La domanda diventa:

> **quanti positivi o quanto valore concentriamo nella capacità che possiamo davvero usare?**

Questa formulazione ricompone class imbalance, ranking e operations nella stessa decisione.

> **Con eventi rari, la prevalenza non è un dettaglio statistico. Determina quanti negativi attraversiamo per trovare ogni positivo e quindi se il modello è economicamente e operativamente sostenibile.**