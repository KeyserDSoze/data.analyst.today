## 10.14 Monitoring: il modello può restare online mentre la decisione smette di funzionare

Il deployment non congela il mondo. Dopo il lancio possono cambiare dati, popolazione, base rate, relazione tra feature e target, pipeline di serving, soglie operative, efficacia dell'intervento e perfino la capacità del team che usa gli score.

Per questo “monitorare il modello” è una definizione troppo stretta. Dobbiamo monitorare il **sistema predittivo**.

### Cinque layer, una sola catena

È utile separare almeno cinque livelli:

1. **data quality** — schema, missing, categorie, freshness;
2. **training-serving parity / data drift** — ciò che il modello vede è ancora coerente con training e serving atteso?;
3. **score behavior** — distribuzione score, volumi sopra soglia, composizione top-K;
4. **predictive quality** — ranking, calibration ed errori quando maturano le label;
5. **decision outcome** — la policy alimentata dal modello crea ancora valore?

Un alert a un livello non implica automaticamente failure agli altri. La distinzione serve proprio a evitare diagnosi del tipo “AUC giù, retrain” quando il problema è altrove.

### Data drift, concept drift e label delay

Il **data drift** descrive un cambiamento nella distribuzione di input o popolazione: più mobile, nuovi mercati, nuovo mix clienti. Il **concept drift** descrive invece un cambiamento nel rapporto tra feature e target: una riduzione di utilizzo che un tempo anticipava churn può diventare normale dopo un cambio di prodotto.

In produzione non osserviamo sempre subito il secondo, perché il target può arrivare settimane o mesi dopo. Se prevediamo churn a 60 giorni, nel frattempo possiamo monitorare missing, feature distributions, nuove categorie, score distribution, volume sopra soglia, training-serving skew e model age. Sono **early warning**, non prova che la predictive quality sia cambiata.

Quando le label maturano torniamo a ranking, precision/recall agli operating point, calibration, distribuzione degli errori e slice critiche.

### Caso simulato/composito — Horizon Travel

Al lancio il modello di cancellazione di Horizon Travel ha:

- ROC-AUC: **0,84**;
- precision top 10%: **42%**;
- calibration coerente.

Sei mesi dopo:

- ROC-AUC: **0,75**;
- precision top 10%: **27%**;
- probabilità sovrastimate.

Nel frattempo sono cambiate policy di cancellazione gratuita, mobile share, mercati, paid channels e loyalty program. Non esiste un solo “drift” da correggere: è cambiato il sistema che genera dati e comportamento.

### Caso reale documentato — training-serving skew in Google

Le *Rules of Machine Learning* di Google documentano sistemi di produzione in cui il training-serving skew ha degradato la performance e raccomandano di misurarlo esplicitamente. Google distingue il gap training→holdout, holdout→next-day e next-day→live; una discrepanza nell'ultimo passaggio è spesso un segnale di engineering perché lo stesso esempio dovrebbe produrre lo stesso comportamento se training e serving applicano la stessa logica.

Riferimento: https://developers.google.com/machine-learning/guides/rules-of-ml/

La guida più recente sui production ML systems aggiunge un principio altrettanto importante: model metrics e real-world metrics devono essere monitorate separatamente, perché migliorare AUC non dimostra automaticamente un miglioramento dell'esperienza reale.

Riferimento: https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring

### Drift non significa retraining automatico

Se il valore medio delle transazioni cresce del 18%, la prima azione non deve essere necessariamente retrain. Potrebbe essere un vero data drift con performance e calibration ancora stabili. Al contrario, calibration o ranking possono peggiorare senza un enorme shift marginale nelle singole feature.

La reazione più robusta è spesso:

```text
segnale
→ investigazione
→ impatto su score/performance/policy
→ decisione: nessuna azione / recalibrate / retrain / redesign / rollback
```

Una soglia universale di PSI non può sostituire questo ragionamento.

### Score drift può diventare capacity drift

Supponiamo che una soglia `0,45` generi normalmente 2.000 alert/settimana. Dopo un cambio di pricing gli alert diventano 5.500, mentre il team può gestirne 2.000.

Anche prima delle label abbiamo un problema reale: la policy non è più eseguibile. Possiamo passare temporaneamente a top-K, cambiare soglia, aumentare capacità o rivedere calibration e modello. Questo è **decision drift**: lo score può essere statisticamente sensato e il processo operativo non esserlo più.

### Feedback loop: la policy cambia i dati futuri

Quando il modello decide chi riceve un'azione, modifica anche le label che osserveremo:

`churn score → retention call → alcuni clienti non churnano → nuove label`

Un cliente ad alto rischio salvato dall'intervento può sembrare un falso positivo se ignoriamo la policy. Per valutare correttamente il sistema dobbiamo sapere chi è stato score-ato, selezionato, contattato, realmente trattato e con quale policy. Quando possibile, un holdout o altro disegno causale separa predictive quality dall'effetto dell'intervento.

Prediction, experimentation e causalità tornano così a incontrarsi.

### Monitoring contract

La Predictive Decision Card dovrebbe trasformare il monitoring in una responsabilità esplicita:

| Layer | Metrica | Frequenza | Trigger | Owner | Azione |
|---|---|---|---|---|---|
| data | missing feature core | giornaliera | > 2% | data owner | investigate |
| serving | training-serving skew | giornaliera | material shift | ML/data | freeze release |
| score | top-K composition | settimanale | shift segmento | analyst | diagnose |
| performance | precision@2000 | mensile | < 30% | model owner | recalibrate/retrain |
| calibration | reliability | mensile | systematic bias | model owner | recalibrate |
| business | net value/action | mensile | sotto baseline | business owner | review policy |

Retraining può essere calendar-based, performance-triggered, drift-triggered o event-triggered, ma non deve diventare manutenzione automatica cieca. Se le label sono contaminate dal feedback loop, un retrain automatico può consolidare il problema.

> **Un modello non fallisce soltanto quando AUC scende. Fallisce quando dati, score, policy o operations smettono di produrre la decisione affidabile per cui era stato costruito.**