## 10.8 Calibration e soglie: stimare rischio e decidere un'azione sono due problemi diversi

Un modello può ordinare molto bene i casi e produrre probabilità poco credibili.

Questa distinzione diventa critica quando lo score entra in:

- expected loss;
- pricing;
- provisioning;
- prioritizzazione per valore atteso;
- soglie di rischio.

Scikit-learn definisce un classificatore ben calibrato come un modello per cui, tra i casi a cui assegna probabilità vicina a 0,8, circa l'80% appartiene effettivamente alla classe positiva nel lungo periodo.

Fonte: https://scikit-learn.org/stable/modules/calibration.html

### Ranking buono, probabilità sbagliate

Immaginiamo:

| Score medio previsto | Evento osservato |
|---:|---:|
| 15% | 14% |
| 35% | 24% |
| 55% | 38% |
| 75% | 52% |

Il rischio cresce insieme allo score: il ranking contiene informazione.

Ma il modello sovrastima sistematicamente la probabilità.

Usare `0,75` come se significasse davvero 75% gonfierebbe expected loss e potrebbe modificare decisioni economiche.

### Caso simulato/composito — NovaCredit

NovaCredit usa un modello per stimare probability of default a 12 mesi.

Il risk committee combina:

`Expected Loss = PD × LGD × EAD`

Dove:

- `PD` = probability of default;
- `LGD` = loss given default;
- `EAD` = exposure at default.

Il modello ha ROC-AUC 0,84, quindi discrimina discretamente.

Nella fascia con PD prevista 20–30%, però, il default osservato è 13%.

Una PD sistematicamente troppo alta può contribuire a:

- pricing troppo aggressivo;
- rifiuto di clienti profittevoli;
- stime economiche distorte;
- allocazione di capitale non coerente con il rischio osservato.

La discrimination non salva la calibration quando il numero viene usato come probabilità.

### Reliability diagram e segment calibration

Una calibration curve confronta, per gruppi di score:

- probabilità prevista media;
- frequenza osservata dell'evento.

La diagonale `predicted = observed` rappresenta calibration ideale.

Ma una curva globale può nascondere errori rilevanti per:

- paese;
- canale;
- prodotto;
- customer segment;
- device;
- periodo temporale.

Se la decisione cambia per questi segmenti, la calibration va controllata anche lì, con prudenza sulla numerosità.

### Brier score: utile, ma non è una calibration curve in un numero

Per target binari il Brier score può essere scritto come:

`Brier = mean((predicted_probability - outcome)^2)`

È una proper scoring rule utile per la qualità probabilistica complessiva.

La documentazione scikit-learn ricorda però che Brier e log loss riflettono insieme aspetti di calibration e discrimination. Un Brier migliore non dimostra da solo che la calibration curve sia migliore in ogni regione dello score.

Perciò conviene usare:

- score probabilistico;
- reliability diagram;
- distribuzione degli score;
- metriche per segmenti rilevanti.

### Recalibration senza contaminare la valutazione

Tecniche come sigmoid/Platt scaling, isotonic regression o temperature scaling possono migliorare la mappa tra score e probabilità.

Il principio più importante è il data separation: il calibratore deve essere appreso su dati indipendenti da quelli usati per fit del classifier, o tramite una procedura cross-validated adeguata. Calibrare sulle stesse predizioni in-sample produce probabilità troppo ottimistiche.

Scikit-learn implementa questa disciplina con `CalibratedClassifierCV`.

### Dalla probabilità alla soglia

Anche un modello perfettamente calibrato non decide autonomamente la soglia.

Scikit-learn separa esplicitamente:

- **statistical problem:** stimare probabilità/score;
- **decision problem:** scegliere quale azione prendere a partire dallo score.

Fonte: https://scikit-learn.org/1.9/modules/classification_threshold.html

Il cutoff `0,5` è un default dell'API, non una legge statistica o economica.

### Caso simulato/composito — ServiceOne e la capacità della coda

ServiceOne prevede quali ticket finiranno in escalation.

Con soglia 0,5:

- 280 ticket/giorno vengono segnalati;
- il team specializzato può gestirne 900;
- molte escalation costose restano fuori.

Una soglia 0,27 produce:

- 860 ticket/giorno;
- recall molto maggiore;
- precision inferiore ma ancora sostenibile.

La nuova soglia può creare più valore anche se non modifica in alcun modo ROC-AUC: il ranking del modello è identico, cambia solo la policy operativa.

### Tuning della soglia: proteggere il test set

La soglia non dovrebbe essere scelta guardando il test finale e poi riportando la stessa performance come se fosse out-of-sample.

Se ottimizziamo threshold, cost matrix o top-K su un dataset, quel dataset è parte del processo di tuning.

La valutazione finale deve quindi usare:

- validation separata;
- cross-validation interna;
- oppure un test successivo non toccato.

Scikit-learn offre, per esempio, `TunedThresholdClassifierCV`, che separa il modello probabilistico dalla scelta dell'operating threshold.

### Threshold economics

Una policy può considerare:

- costo FP;
- costo FN;
- valore a rischio;
- costo dell'intervento;
- capacità massima;
- vincoli regolatori;
- fairness/servizio;
- reversibilità dell'azione.

Per esempio, due clienti con stesso `P(churn)` possono ricevere priorità diversa se il valore economico a rischio è molto diverso.

Ma attenzione: per stimare il **beneficio dell'intervento** non basta la probabilità di churn. Serve evidenza sull'incremental effect dell'azione, collegandoci di nuovo ai Capitoli 8 e 9.

### Calibration drift

La calibration può degradare anche quando AUC rimane quasi stabile.

Se il base rate di churn raddoppia dopo un cambiamento di prezzo, il modello può continuare a ordinare bene i clienti ma sottostimare sistematicamente le probabilità.

Per questo in produzione monitoreremo separatamente:

- ranking/discrimination;
- calibration;
- prevalenza;
- distribuzione score;
- operating volumes.

> **Lo score ordina il rischio. La calibration dà significato numerico allo score. La soglia trasforma quel numero in una policy. Un sistema predittivo serio governa tutti e tre i livelli separatamente.**
