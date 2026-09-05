## 10.8 Calibration e soglie: dare significato allo score prima di usarlo come probabilità

Un modello può ordinare molto bene i casi e produrre probabilità poco credibili. La distinzione diventa critica quando lo score entra in expected loss, pricing, provisioning o qualunque decisione che attribuisca al numero un significato quantitativo.

Scikit-learn definisce un classificatore ben calibrato in modo intuitivo: tra i casi a cui assegna probabilità vicina a 0,8, nel lungo periodo circa l'80% dovrebbe appartenere alla classe positiva.

Riferimento: https://scikit-learn.org/stable/modules/calibration.html

### Ranking corretto, probabilità sbagliate

Supponiamo di osservare:

| Score medio previsto | Evento osservato |
|---:|---:|
| 15% | 14% |
| 35% | 24% |
| 55% | 38% |
| 75% | 52% |

Il rischio cresce insieme allo score, quindi il ranking contiene informazione. Ma il modello sovrastima sistematicamente la probabilità. Usare `0,75` come se significasse davvero 75% produrrebbe expected loss gonfiata e soglie economiche distorte.

### Caso simulato/composito — NovaCredit

NovaCredit stima probability of default a 12 mesi. Il risk committee usa:

`Expected Loss = PD × LGD × EAD`

Il modello ha ROC-AUC **0,84**, ma nella fascia con PD prevista tra 20% e 30% il default osservato è **13%**. La discrimination può quindi essere discreta mentre la probabilità è troppo alta per il calcolo economico.

La calibration curve confronta probabilità prevista media e frequenza osservata. La diagonale `predicted = observed` è il riferimento ideale, ma una curva globale può nascondere errori importanti per paese, prodotto, canale, customer segment o periodo. Se la policy cambia per quei gruppi, la calibration va controllata anche lì, senza dimenticare la numerosità.

Il Brier score è utile per la qualità probabilistica complessiva:

`Brier = mean((predicted_probability - outcome)^2)`

ma combina aspetti di calibration e discrimination. Non sostituisce una reliability analysis nelle regioni dello score che guidano la decisione.

### Recalibration richiede separazione dei dati

Sigmoid/Platt scaling, isotonic regression e temperature scaling possono correggere la mappa score → probabilità. Il punto fondamentale non è il nome della tecnica ma la separazione dei dati: il calibratore non dovrebbe essere fit-tato sulle stesse predizioni in-sample usate per addestrare il classifier.

La documentazione corrente di scikit-learn ribadisce che il calibratore dovrebbe vedere dati indipendenti o predizioni ottenute tramite una procedura cross-validated adeguata; `CalibratedClassifierCV` implementa proprio questa disciplina.

Riferimento: https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html

### La soglia è una decisione, non un attributo del modello

Anche una probabilità perfettamente calibrata non decide da sola quando agire. La documentazione scikit-learn separa esplicitamente il problema statistico di stimare una probabilità dal problema decisionale di trasformarla in una classe o azione. `TunedThresholdClassifierCV`, per esempio, può scegliere tramite cross-validation un cutoff ottimizzato rispetto a una metrica di utilità senza cambiare le probabilità del modello.

Riferimento: https://scikit-learn.org/stable/modules/classification_threshold.html

### Caso simulato/composito — ServiceOne

ServiceOne prevede quali ticket finiranno in escalation. Con soglia `0,5` genera **280 ticket/giorno**, ma il team specializzato può gestirne **900**. Una soglia `0,27` genera **860 ticket/giorno**, aumenta molto il recall e riduce la precision, restando però dentro capacità.

ROC-AUC non cambia: il ranking è identico. È la policy a essere diversa.

Per questo threshold o top-K dovrebbero essere scelti considerando costo FP, costo FN, valore a rischio, costo dell'intervento, capacità, vincoli di servizio e reversibilità. Se la soglia viene ottimizzata su un dataset, quel dataset appartiene al tuning: non può essere riutilizzato ingenuamente come test finale untouched.

### Calibration drift e decision drift

In produzione ranking e calibration possono degradare in modo diverso. Se il base rate di churn raddoppia dopo un cambio di prezzo, AUC può restare quasi stabile mentre le probabilità diventano sistematicamente troppo basse. Se il volume sopra soglia supera la capacità, anche un modello statisticamente sano può alimentare una policy non più eseguibile.

Per questo monitoreremo separatamente discrimination, calibration, prevalenza, score distribution e operating volume.

> **Lo score ordina il rischio. La calibration dà significato numerico allo score. La soglia trasforma quel numero in una policy. Un sistema predittivo governabile tiene separati questi tre livelli e li ricompone soltanto nella decisione.**