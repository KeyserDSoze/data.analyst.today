## 10.15 Caso end-to-end: OrbitCom, dal buon modello offline al sistema decisionale che cambia il proprio futuro

> **Caso simulato/composito.** Azienda, numeri e circostanze sono costruiti a fini didattici combinando failure mode comuni nei sistemi predittivi in produzione.

OrbitCom è un operatore telecom con 3,8 milioni di clienti consumer.

Il management parte con una richiesta apparentemente semplice:

> **"Costruiamo un modello che preveda il churn."**

La review analitica la trasforma in una prediction task precisa.

### Predictive specification

**Decisione**  
Prioritizzare la capacità del team retention senza superare il volume che può essere gestito con qualità.

**Prediction unit**  
Cliente consumer attivo.

**Prediction time**  
Ogni lunedì alle 05:00.

**Target**  
Cancellazione volontaria nei successivi 60 giorni.

**Action capacity**  
Massimo 25.000 contatti/settimana.

**Baseline**  
Regola esistente basata su reclami recenti, payment issues e calo utilizzo.

Questa specifica cambia il progetto: non ci serve il miglior classifier astratto. Ci serve un ranking utile nei primi 25.000 casi e una pipeline che resti valida ogni lunedì.

### Feature availability review

Le feature candidate includono:

- tenure;
- variazione utilizzo dati;
- reclami chiusi e aperti prima del prediction time;
- payment failures storici;
- outage sperimentati;
- variazione della spesa;
- downgrade già avvenuti;
- app usage;
- device;
- piano tariffario.

Una feature iniziale, `last_retention_offer_result`, viene esclusa: in molti casi l'offerta viene fatta **dopo** che il rischio è già stato identificato e troppo vicino al churn event.

Un'altra, `competitor_offer_declared`, proviene da survey compilate soltanto da una parte dei clienti ed è mantenuta come feature sperimentale con coverage monitorata.

### Validation design

OrbitCom ha cambiato pricing e acquisition mix durante l'ultimo anno.

Il team evita quindi di affidarsi soltanto a random split.

Usa:

- train sui periodi più vecchi;
- validation su periodo successivo;
- test out-of-time sugli ultimi mesi maturi;
- analisi separata su nuovi clienti e clienti con tenure > 12 mesi.

Confronta tre sistemi:

| Modello | ROC-AUC test | PR-AUC | Precision@25k | Note |
|---|---:|---:|---:|---|
| regola esistente | 0,69 | 0,17 | 24% | baseline operativa |
| logistic regression | 0,82 | 0,31 | 38% | interpretabile |
| gradient boosting | 0,87 | 0,39 | 44% | modello candidato |

Il boosting migliora davvero il punto operativo: nei 25.000 clienti che il team può gestire concentra più churn futuri della baseline.

### Leakage test

Il team esegue una review `as-of` delle feature.

Trova due problemi:

1. uno snapshot CRM storico era ricostruito usando `current account status`;
2. una feature di ticket severity poteva essere aggiornata retroattivamente dopo la chiusura del ticket.

Dopo la ricostruzione corretta la ROC-AUC scende da 0,90 a 0,87.

Il calo viene classificato come miglioramento della credibilità, non come regressione del progetto.

### Calibration e threshold

Il modello ordina bene, ma tende a sovrastimare il rischio dei clienti più nuovi.

Il team mantiene il ranking globale ma introduce una procedura di calibration validata separatamente e controlla reliability per tenure.

La policy non usa threshold 0,5.

Usa:

> **top 25.000 account eleggibili per expected risk/value, con ulteriori guardrail business.**

La capacità operativa è quindi parte della policy fin dall'inizio.

### Model score non significa treatment effect

A questo punto il team potrebbe commettere l'errore centrale del Capitolo 8:

> "Se il modello identifica bene chi churnerà, allora chiamare quei clienti salverà il churn."

Non segue.

Un cliente può essere:

- ad alto rischio ma irrecuperabile;
- a medio rischio e molto persuadibile;
- ad alto valore ma poco sensibile all'intervento;
- destinato a non churnare anche senza chiamata.

OrbitCom crea quindi, tra gli account eleggibili alla retention policy, un **holdout sperimentale** compatibile con vincoli etici e commerciali per misurare l'incremental effect del programma.

Prediction decide **chi è a rischio**. Experimentation misura **che cosa produce la policy**.

### Primo mese di produzione

Nel primo mese:

- scoring pipeline stabile;
- precision@25k vicina al test;
- contact rate 91%;
- capacity quasi pienamente utilizzata;
- calibration nei range previsti.

Il progetto viene classificato come production-ready, ma non "finito".

### Tre mesi dopo: quattro problemi diversi

Le metriche cambiano:

| Metrica | Test offline | Mese 1 | Mese 3 |
|---|---:|---:|---:|
| ROC-AUC | 0,87 | 0,85 | 0,77 |
| precision@25k | 44% | 41% | 29% |
| contact rate | — | 91% | 63% |
| quota nuovi clienti nel top-K | 18% | 21% | 37% |

Il team evita di dire semplicemente "il modello è peggiorato" e separa quattro diagnosi.

#### 1. Population/data drift

Una campagna acquisisce molti clienti giovani, mensili e mobile-first, poco rappresentati nel training.

#### 2. Concept/calibration drift

Un nuovo piano con roaming incluso cambia il significato di `domestic_data_usage_drop`. Il ranking si deteriora e le probabilità diventano troppo alte in alcuni segmenti.

#### 3. Operational degradation

Il team retention perde capacità durante una riorganizzazione. Il contact rate scende al 63% e molti clienti vengono raggiunti tardi.

#### 4. Feedback loop

I clienti ad alto score ricevono interventi. Se alcuni non churnano grazie alla policy, le label future riflettono anche l'effetto del sistema stesso.

Senza tracciare assignment, exposure e treatment, retraining e performance monitoring diventano ambigui.

### La dashboard viene divisa in quattro layer

```text
DATA
feature freshness · missing · training-serving skew · population mix

MODEL
ranking · precision@25k · calibration · score distribution

OPERATIONS
selected · contacted · time-to-contact · capacity · treatment delivered

OUTCOME
churn · incremental effect vs holdout · value saved · cost · customer guardrails
```

Questa separazione evita di attribuire al modello un problema del call center o, al contrario, di usare problemi operativi per nascondere un deterioramento predittivo.

### Retraining: non basta premere un pulsante

OrbitCom definisce:

- retraining candidate mensile;
- champion/challenger evaluation su out-of-time recente;
- gate su calibration e precision@25k;
- verifica training-serving parity;
- rollback se il challenger non supera la baseline concordata;
- versionamento feature/model/policy;
- holdout per valutare la retention policy separatamente dal risk model.

Un nuovo modello viene promosso solo se migliora la decisione prevista, non perché usa dati più recenti.

### La decisione finale cambia forma

La domanda iniziale era:

> "Chi farà churn?"

Il sistema maturo deve rispondere invece a più domande coordinate:

1. chi è a rischio entro 60 giorni?
2. quanto è affidabile lo score nella popolazione corrente?
3. chi entra nei 25.000 slot operativi?
4. chi viene realmente contattato?
5. quale intervento produce valore incrementale?
6. il costo e la customer experience restano accettabili?
7. quando modello o policy devono essere fermati, ricalibrati o ridisegnati?

### La lezione del caso

Un modello può fallire in almeno quattro modi differenti:

- **prediction failure** — non ordina o stima più bene;
- **data/serving failure** — le feature non rappresentano più ciò su cui è stato validato;
- **policy failure** — threshold/ranking generano un'azione sbagliata o ingestibile;
- **treatment failure** — l'azione non produce più abbastanza effetto incrementale.

Chiamare tutto "model performance" rende la diagnosi peggiore.

> **Il prodotto predittivo non è il file del modello. È la catena che trasforma dati disponibili oggi in una priorità, una decisione, un'azione e una misura del risultato futuro.**
