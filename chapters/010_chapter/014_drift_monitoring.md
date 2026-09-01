## 10.14 Monitoring: il modello può restare online mentre la decisione smette di funzionare

Il deployment non congela il mondo.

Dopo il lancio possono cambiare:

- dati;
- popolazione;
- base rate;
- relazione tra feature e target;
- pipeline di serving;
- soglie operative;
- efficacia dell'intervento;
- capacità del team che usa gli score.

Per questo "monitorare il modello" è troppo stretto. Dobbiamo monitorare il **sistema predittivo**.

### Cinque livelli diversi

È utile separare almeno:

1. **data quality** — schema, missing, categorie, freshness;
2. **training-serving parity / data drift** — ciò che il modello vede è ancora coerente con training e serving atteso?
3. **score behavior** — distribuzione degli score, volumi sopra soglia, coverage;
4. **predictive quality** — ranking, calibration, errori quando arrivano le label;
5. **decision outcome** — la policy alimentata dal modello continua a creare valore?

Un alert a un livello non implica automaticamente failure agli altri.

### Data drift e concept drift

**Data drift**: cambia la distribuzione di input o popolazione.

Esempi:

- più traffico mobile;
- nuovi mercati;
- mix clienti differente;
- nuove categorie prodotto.

**Concept drift**: cambia il rapporto tra informazioni e target.

Esempio: un calo di utilizzo che un tempo anticipava churn diventa normale dopo il lancio di un piano stagionale.

Questa distinzione è utile, ma in produzione spesso non osserviamo subito il concept drift perché il target arriva in ritardo.

### Caso simulato/composito — Horizon Travel

Horizon Travel prevede cancellazioni alberghiere.

Al lancio:

- ROC-AUC: 0,84;
- precision top 10%: 42%;
- calibration coerente.

Sei mesi dopo:

- ROC-AUC: 0,75;
- precision top 10%: 27%;
- probabilità sovrastimate.

Nel frattempo sono cambiati:

- policy di cancellazione gratuita;
- mobile share;
- mercati;
- paid channels;
- loyalty program.

Non esiste un solo "drift" da correggere. È cambiato il sistema di generazione dei dati e probabilmente anche il significato predittivo di alcune feature.

### Caso reale documentato — Google e il training-serving skew

Le *Rules of Machine Learning* di Google riportano che sistemi ML di produzione in Google hanno sofferto di **training-serving skew** con impatto negativo sulla performance.

Google distingue, tra le altre cose:

- differenza tra training e holdout;
- differenza tra holdout e dati del giorno successivo;
- differenza tra next-day e live serving.

Una grande discrepanza nell'ultimo passaggio può indicare un problema di engineering, perché lo stesso esempio dovrebbe produrre lo stesso comportamento se training e serving applicano la stessa logica.

Google raccomanda di misurare esplicitamente lo skew e di avvicinare il più possibile training e serving.

Fonte: https://developers.google.com/machine-learning/guides/rules-of-ml/

Questo è un caso importante perché mostra che un modello può degradare senza che l'algoritmo sia cambiato: basta che cambi il modo in cui le feature vengono prodotte.

### Label delay: quando non sappiamo ancora se stiamo sbagliando

Se prevediamo churn a 60 giorni, le label complete arrivano almeno 60 giorni dopo.

Nel frattempo possiamo monitorare proxy:

- missing rate;
- feature distributions;
- categorie nuove;
- score distribution;
- percentuale sopra soglia;
- volume per segmento;
- training-serving skew;
- model age.

Ma dobbiamo chiamarli con il loro nome: **early warning**, non prova di performance.

Quando le label maturano, dobbiamo tornare a:

- ranking/discrimination;
- precision/recall agli operating point;
- calibration;
- error distribution;
- performance per segmenti.

### Drift non significa automaticamente retraining

Un monitor segnala che il valore medio delle transazioni è salito del 18%.

Possibili reazioni:

1. retrain immediato;
2. rollback;
3. investigazione.

La terza è spesso la migliore prima mossa.

Il data drift può essere reale mentre performance e calibration restano stabili.

Al contrario, il modello può deteriorarsi senza un enorme shift marginale nelle singole feature perché cambia una relazione multivariata o il base rate.

Le regole di retraining devono quindi collegare segnali, performance e costo operativo, non una soglia universale di PSI.

### Score drift e capacity drift

Supponiamo che il threshold sia 0,45 e generi normalmente 2.000 alert/settimana.

Dopo un cambio di pricing gli score aumentano e gli alert diventano 5.500.

Anche prima di sapere se la discrimination sia peggiorata abbiamo un problema reale:

- il team può gestirne 2.000;
- la policy non è più eseguibile nello stesso modo.

Il sistema deve scegliere se:

- alzare temporaneamente la soglia;
- passare a top-K;
- aumentare capacità;
- ricalibrare;
- rivedere il modello.

Questa è **decision drift**: la relazione tra score e processo operativo non è più quella prevista.

### Feedback loop

Quando il modello cambia chi riceve un'azione, cambia anche i dati futuri.

Esempio:

`churn score → retention call → alcuni clienti non churnano → nuove label`

Se valutiamo ingenuamente il modello sulla popolazione trattata, un cliente ad alto rischio che non churna grazie all'intervento può sembrare un falso positivo.

La pipeline di monitoring deve quindi sapere:

- chi è stato score-ato;
- chi è stato selezionato;
- chi ha ricevuto davvero il trattamento;
- quale policy era attiva;
- se esiste un holdout o altra strategia per stimare l'efficacia della decisione.

Prediction, experimentation e causalità tornano a incontrarsi.

### Real-world metrics oltre AUC

Google sottolinea nelle proprie guide sui sistemi ML di produzione che migliorare una metrica del modello, come AUC, non dimostra automaticamente un miglioramento dell'esperienza reale. Servono metriche downstream separate.

Fonte: https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring

Per un churn model possiamo monitorare:

- model: AUC, calibration, precision@K;
- operations: contact rate, time-to-contact, capacity utilization;
- treatment: offer acceptance;
- business: incremental churn saved, margin netto, customer experience.

### Monitoring contract

La Predictive Decision Card dovrebbe indicare almeno:

| Layer | Metrica | Frequenza | Soglia/trigger | Owner | Azione |
|---|---|---|---|---|---|
| data | missing feature core | giornaliera | > 2% | data owner | investigate |
| serving | training-serving skew | giornaliera | material shift | ML/data | freeze release |
| score | top-K composition | settimanale | shift segmento | analyst | diagnose |
| performance | precision@2000 | mensile | < 30% | model owner | recalibrate/retrain |
| calibration | reliability | mensile | systematic bias | model owner | recalibrate |
| business | net value/action | mensile | sotto baseline | business owner | review policy |

### Retraining non è manutenzione automatica

Retrain può essere:

- calendar-based;
- performance-triggered;
- drift-triggered;
- event-triggered dopo cambi di prodotto/policy;
- continuo, in sistemi adatti.

Ma un retraining automatico su dati contaminati dal feedback loop può peggiorare il problema.

Prima di automatizzarlo servono:

- label policy;
- data lineage;
- evaluation gate;
- champion/challenger o rollback;
- versione del modello;
- monitoring post-deployment.

> **Un modello non fallisce solo quando AUC scende. Fallisce quando dati, score, policy o operations smettono di produrre la decisione affidabile per cui era stato costruito.**
