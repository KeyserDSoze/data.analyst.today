## 10.16 Predictive Decision Card: documentare il sistema che trasforma uno score in una decisione

Il modello non è il deliverable finale di un progetto predittivo.

Il deliverable è una specifica verificabile che dica:

- che cosa viene previsto;
- con quale informazione disponibile;
- come è stata verificata la generalizzazione;
- come lo score diventa un'azione;
- quali limiti ha il sistema;
- come sapremo che sta degradando.

Lo chiameremo **Predictive Decision Card**.

Non sostituisce documentazione tecnica, model registry o governance regolatoria. Serve a collegare in una sola pagina logica **prediction task, evidence e decision policy**.

### 1. Decisione

Scrivere prima l'azione, non l'algoritmo.

Esempio:

> Ogni lunedì prioritizzare fino a 2.000 account per revisione Customer Success, senza superare la capacità disponibile e dando precedenza ai casi con maggiore valore atteso a rischio.

Se non sappiamo che cosa cambia grazie allo score, non abbiamo ancora definito l'utilità del modello.

### 2. Prediction unit

Quale entità riceve una previsione?

- cliente;
- account;
- ordine;
- transazione;
- ticket;
- macchina;
- spedizione.

Va indicata anche la chiave tecnica che rappresenta quell'entità e come vengono gestiti duplicati, account collegati o identità multi-device.

### 3. Prediction time

In quale istante viene prodotta la previsione?

Esempio:

> lunedì alle 05:00 Europe/Rome.

Questa riga definisce la frontiera informativa dell'intero sistema.

### 4. Horizon, target e label maturity

Specificare:

- evento o quantità da prevedere;
- finestra futura;
- regola di costruzione della label;
- momento in cui la label può essere considerata matura.

Esempio:

> churn volontario entro 60 giorni; la valutazione completa di una prediction batch è disponibile dopo 60 giorni più 7 giorni di stabilizzazione dei sistemi amministrativi.

Senza label maturity rischiamo di valutare troppo presto il modello e chiamare falsi negativi eventi che non hanno ancora avuto tempo di manifestarsi.

### 5. Popolazione e scope

Dichiarare:

- popolazione eleggibile;
- esclusioni;
- mercati;
- prodotti;
- segmenti;
- intervalli delle feature su cui esiste supporto sufficiente;
- casi fuori distribuzione o non coperti.

La card deve poter rispondere:

> **per chi sappiamo che questa performance è stata verificata?**

### 6. Feature availability e sorgenti `as-of`

Per ogni famiglia di feature importante documentare:

- source of truth;
- timestamp semantico;
- disponibilità al prediction time;
- possibilità di ricostruzione storica `as-of`;
- serving latency;
- eventuale fallback.

Le feature senza history affidabile devono essere marcate esplicitamente. "Esiste oggi" non significa "era disponibile nella validation storica".

### 7. Baseline

Ogni modello candidato deve avere un avversario semplice:

- media/mediana;
- base rate;
- regola operativa esistente;
- regressione lineare/logistica;
- heuristic score.

La domanda è:

> **quanto valore predittivo aggiunge il modello rispetto a ciò che avremmo fatto comunque?**

### 8. Validation design statement

Scrivere una frase in linguaggio business.

Esempio:

> Il test è out-of-time e lascia fuori interi account perché il modello dovrà generalizzare sia a clienti mai usati nel training sia a periodi futuri.

Poi documentare:

- train/validation/test;
- grouping;
- temporal ordering;
- cross-validation;
- eventuale final holdout;
- pipeline anti-leakage.

### 9. Modello candidato e complexity justification

Non basta scrivere `XGBoost` o `logistic regression`.

Registrare:

- famiglia di modello;
- feature set/versione;
- principali hyperparameter rilevanti;
- confronto con baseline;
- incremento fuori campione;
- costo aggiuntivo di serving/maintenance;
- motivo per cui la complessità è giustificata.

Esempio:

> gradient boosting aumenta precision@2000 dal 31% al 39% rispetto al logit, con latency e costi compatibili con batch settimanale.

### 10. Ranking/discrimination

Per classification/ranking indicare ciò che misura la capacità di ordinare i casi:

- ROC-AUC quando pertinente;
- PR-AUC / Average Precision per eventi rari;
- lift/gain;
- precision@K;
- recall@capacity;
- performance per segmenti critici.

Per target continui indicare metriche di errore e distribuzione degli errori coerenti con la decisione.

### 11. Calibration

Se gli score vengono trattati come probabilità, documentare:

- calibration globale;
- reliability per segmenti chiave;
- Brier/log loss o altre proper scoring rule;
- metodo di recalibration;
- dataset su cui è stato appreso il calibratore.

Uno score utile solo per ranking non deve essere venduto come probabilità affidabile.

### 12. Operating policy

Come diventa azione lo score?

Possibili policy:

- threshold;
- top-K;
- più soglie per diversi livelli di intervento;
- ranking combinato con valore economico;
- review umana.

Registrare:

- cutoff o capacità;
- data su cui è stato scelto;
- logica di tuning;
- condizioni di override.

La soglia è parte della policy e deve avere una versione, proprio come il modello.

### 13. Capacity e cost matrix

Esplicitare almeno:

- capacità massima/minima;
- costo FP;
- costo FN;
- costo dell'azione;
- valore a rischio;
- eventuali vincoli di servizio o regolatori.

Se il team può gestire 2.000 alert, una policy che ne produce 6.000 non è pronta anche se la metrica del modello è eccellente.

### 14. Interpretabilità e causal caveat

Documentare:

- metodo di feature importance/explanation;
- dataset su cui viene calcolato;
- stabilità delle feature principali;
- gruppi correlati/proxy;
- variabili non modificabili;
- leve con evidenza causale separata.

Frase obbligatoria quando pertinente:

> **Feature importance descrive ciò che il modello usa per predire; non dimostra l'effetto di modificare quella feature.**

### 15. Monitoring contract

Per ciascun layer indicare metrica, frequenza, trigger, owner e azione.

Minimo:

- data quality/freshness;
- training-serving skew;
- feature/population drift;
- score distribution;
- volume sopra soglia/top-K composition;
- ranking/error metrics quando maturano le label;
- calibration;
- metriche operative;
- outcome downstream.

### 16. Retraining e recalibration triggers

Specificare quando il sistema viene rivalutato:

- calendario;
- deterioramento performance;
- calibration drift;
- cambi di policy/prodotto;
- nuove popolazioni;
- feature pipeline change.

E distinguere:

- **recalibration** — corregge la mappa score → probabilità;
- **retraining** — ricalcola il modello;
- **redesign** — cambia target, feature o processo decisionale.

Non ogni drift richiede retraining.

### 17. Fallback e rollback

Che cosa succede se:

- scoring non parte;
- una feature core manca;
- il modello supera una soglia di deterioramento;
- il serving produce output fuori range?

Definire:

- baseline/heuristic fallback;
- ultima versione stabile;
- freeze della policy;
- rollback del modello;
- owner autorizzato.

### 18. Owner, versioni e lineage

Registrare almeno:

- model owner;
- business owner;
- data/feature owner;
- model version;
- feature version;
- policy/threshold version;
- training window;
- codice/query/notebook/pipeline;
- data di validazione.

Uno score senza lineage diventa presto impossibile da difendere.

### 19. Se lo score attiva un trattamento: separare prediction da policy effect

Quando lo score decide chi riceve una chiamata, sconto, ispezione o intervento, la card deve spiegare come verrà misurato il valore della policy.

Possibili strumenti:

- randomized holdout;
- experiment;
- quasi-esperimento;
- altro design causale appropriato.

La performance predittiva risponde a:

> **chi è a rischio?**

La valutazione della policy risponde a:

> **l'azione cambia davvero l'outcome e crea valore netto?**

Non vanno fuse nella stessa metrica.

### 20. Release status e limitazioni

Un linguaggio utile può essere:

- **NOT READY — validation insufficiente**;
- **NOT READY — leakage/serving issue**;
- **SHADOW MODE**;
- **PILOT / HUMAN-IN-THE-LOOP**;
- **PRODUCTION WITH CONSTRAINTS**;
- **PRODUCTION**;
- **FREEZE / RECALIBRATE**;
- **ROLLBACK**;
- **RETIRED**.

Aggiungere sempre le limitazioni che cambiano l'uso:

> validato solo su Italia e Francia; performance non verificata sui nuovi mercati DACH; label maturity 60 giorni; calibration instabile sui clienti con tenure < 30 giorni.

### Template compatto

```text
Decision:
Prediction unit:
Prediction time:
Target / horizon:
Label maturity:
Population / scope:
Feature sources / as-of availability:
Baseline:
Validation design:
Candidate model / version:
Complexity justification:
Ranking / error metrics:
Calibration:
Operating policy / threshold / top-K:
Capacity / cost assumptions:
Interpretability / causal caveats:
Monitoring contract:
Retraining / recalibration triggers:
Fallback / rollback:
Owners / lineage:
Policy-effect evaluation:
Release status:
Known limitations:
```

### La domanda finale

La card deve permettere a una persona che non ha costruito il modello di completare questa frase:

> **"Questo sistema produce questa previsione in questo momento, per questa popolazione, usando soltanto queste informazioni; è stato validato in questo modo; attiva questa policy; se sbaglia succede questo; se degrada faremo questo."**

Se non riusciamo a scriverla, non abbiamo ancora un sistema predittivo governabile.

> **La Predictive Decision Card non documenta soltanto il modello. Documenta la promessa che stiamo facendo quando lasciamo che quel modello influenzi una decisione.**
