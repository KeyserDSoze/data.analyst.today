## 10.17 Sintesi ed esercizi: dal passato osservato a una decisione futura governabile

Il predictive modeling non è una gara tra algoritmi. È una catena di contratti che parte da una decisione e deve sopravvivere al deployment:

**decisione → prediction time → target → feature `as-of` → baseline → validation → score → calibration → policy → operations → monitoring → outcome.**

Il capitolo ha mostrato che ogni passaggio protegge una promessa diversa. Prediction time impedisce di usare il futuro. La validation simula il modo in cui il sistema dovrà generalizzare. Baseline e regularization obbligano la complessità a guadagnarsi il proprio costo. Ranking, calibration e threshold separano ciò che il modello sa ordinare da ciò che possiamo trattare come probabilità e da ciò che l'organizzazione può realmente fare. Monitoring e feedback loop ricordano infine che il deployment cambia il mondo che produrrà i dati successivi.

La **Predictive Decision Card** ricompone questi pezzi in un solo artefatto. Non documenta soltanto un modello: documenta quale previsione stiamo facendo, con quale informazione, per quale popolazione, come è stata validata, quale policy attiva e che cosa accadrà quando una parte del sistema smetterà di funzionare.

> **Un modello utile non è quello che conosce meglio il passato. È quello che mantiene una promessa verificabile quando incontra dati, persone e processi che non erano nel notebook.**

Gli esercizi restano strutturati perché servono a usare quella promessa come strumento di lavoro.

---

### Esercizio 1 — Definisci la prediction task prima del modello

Un marketplace dice: “Vogliamo prevedere i seller problematici.” Il team Risk può revisionare **800 seller a settimana**.

Costruisci una specifica con prediction unit, prediction time, horizon, target, label maturity, azione, capacità e baseline. Poi spiega perché sono progetti differenti:

- seller con almeno un reclamo nei prossimi 30 giorni;
- seller che genereranno perdita netta > **€1.000**;
- seller su cui una review preventiva ridurrà davvero il danno.

L'ultima domanda richiede anche evidenza causale sull'intervento.

---

### Esercizio 2 — Il modello complesso ha davvero vinto?

| Modello | Feature | AUC train | AUC test | Precision@2000 |
|---|---:|---:|---:|---:|
| Logit | 22 | 0,79 | 0,77 | 36% |
| Boosting | 240 | 0,96 | 0,78 | 37% |

Il boosting richiede una pipeline aggiuntiva, serving più costoso ed explanations più complesse. Scrivi una **complexity justification**: quale guadagno è davvero out-of-sample, quanto cambia la decisione nei primi 2.000 casi, quali slice controlleresti e quale costo aggiuntivo deve essere giustificato?

---

### Esercizio 3 — Leakage `as-of`

Vuoi prevedere, 30 giorni prima della scadenza, quali clienti non rinnoveranno. Classifica queste feature come utilizzabili, leakage, ricostruibili solo `as-of` oppure dipendenti dalla policy/timing:

- ticket aperti nei 90 giorni precedenti;
- ultima data login nello snapshot storico;
- `current_contract_status` dalla tabella corrente;
- sconto di rinnovo applicato 10 giorni prima della scadenza;
- esito della chiamata retention;
- saldo fatture al prediction time.

Poi scrivi la query concettuale: **“Che cosa sapevamo esattamente alla data X?”**

---

### Esercizio 4 — Preprocessing leakage

Hai **300 osservazioni e 8.000 feature**. Il team esegue feature selection sull'intero dataset, poi split, training e ottiene accuracy **0,79** su un target quasi casuale.

Spiega dove entra il test, perché molte feature aumentano le coincidenze casuali, come ricostruire la pipeline e perché un `Pipeline` object aiuta ma non sostituisce il ragionamento sul prediction time. Confronta il caso con l'esempio scikit-learn delle **10.000 feature casuali**.

---

### Esercizio 5 — Random split o deployment simulation?

FinSure deve prevedere default su nuovi prestiti. Negli ultimi nove mesi sono cambiati underwriting e acquisition channels.

- random split ROC-AUC: **0,88**;
- out-of-time ROC-AUC: **0,76**.

Quale numero è più vicino alla decisione futura? Il modello è “peggiore” o è diventata più difficile la domanda di generalizzazione? Useresti anche group split? Scrivi il validation design statement della card.

---

### Esercizio 6 — Ranking buono, calibration cattiva

Un modello di default ha ROC-AUC **0,86**. Per clienti con score medio 30% osservi default 14%.

Spiega se il ranking può essere ancora utile, se lo score può entrare direttamente in `PD × LGD × EAD`, quale reliability analysis serve e come impareresti un calibratore senza contaminare la valutazione finale.

---

### Esercizio 7 — Threshold 0,5 o capacità 900?

Un modello predice escalation dei ticket. A soglia 0,5 genera **280 alert/giorno**, ma il team può gestirne **900**. A soglia 0,27 genera **860 alert**, con precision inferiore e recall maggiore. Una review costa **€4**, un'escalation persa **€180**.

Confronta threshold, top-K, expected cost e capacità. Spiega perché la soglia è una proprietà della policy, non del classifier.

---

### Esercizio 8 — Evento raro e volume operativo

SafePay processa **500.000 transazioni**; frode **0,4%**. Alla soglia corrente recall = **85%**, precision = **12%**.

Stima frodi totali, frodi intercettate, alert totali e falsi positivi. Se la coda può gestire 4.000 casi, la policy è sostenibile? Quali costi mancano? Perché un test set artificialmente 50/50 renderebbe la precision poco trasferibile?

---

### Esercizio 9 — Feature importance non è intervention map

Un churn model ordina tra le feature principali failed payments, numero ticket, tenure, response time support e login frequency.

Costruisci una tabella con:

| Feature | Predictive importance | Modificabile? | Segnale o possibile causa? | Evidenza causale? | Prossimo passo |
|---|---|---|---|---|---|

Indica quali domande appartengono ai Capitoli 8 e 9 invece che al predictive modeling.

---

### Esercizio 10 — Drift non significa retraining

Un modello antifrode mostra forte shift nel valore medio delle transazioni. Quando maturano le label, ROC-AUC, precision@K e calibration sono stabili.

Distingui data drift, predictive failure, alert investigativo e retraining trigger. Poi considera il caso opposto: feature distributions apparentemente stabili ma calibration in peggioramento. Come può succedere?

---

### Esercizio 11 — Training-serving skew

`customer_balance_30d` viene calcolato in training da batch alle 23:59 e in serving da una query realtime con timezone diversa, diversa esclusione dei refund e aggiornamenti parziali delle ultime due ore. Offline AUC resta alta, online precision scende.

Progetta la diagnosi: confronto training/serving sugli stessi esempi, metriche di skew, freeze di modello/feature/policy e soluzione per impedire che le due implementazioni divergano di nuovo.

---

### Esercizio 12 — Feedback loop

Un churn model seleziona i **5.000 clienti più a rischio** e tutti ricevono un voucher. Tre mesi dopo molti clienti ad alto score non hanno churnato. Il team conclude che sono falsi positivi.

Discuti almeno tre possibilità: modello sovrastimato, voucher efficace, label alterata dalla policy. Proponi un disegno che separi predictive evaluation e treatment effect usando i Capitoli 8 e 9.

---

### Esercizio 13 — Model health buono, decision system cattivo

Un retention model mantiene AUC **0,84**, calibration stabile e precision@2000 **40%**. Nel frattempo contact rate scende **92% → 55%**, time-to-contact **8 → 40 ore**, acceptance **30% → 17%**, costo voucher **+35%**.

Scrivi un verdetto separando model health, execution operativa, treatment efficacy, economics e decision status.

---

### Esercizio 14 — Leadership meeting: OrbitCom

La slide dice: “Churn model AUC 0,87. Progetto ML riuscito.” Le informazioni complete sono:

- baseline precision@25k: 24%;
- modello: 44% offline, 29% dopo tre mesi;
- acquisition campaign cambia il mix clienti;
- calibration peggiora sui clienti nuovi;
- contact rate scende al 63%;
- clienti ad alto score vengono trattati;
- manca ancora un holdout per misurare incremental churn saved.

Scrivi un executive summary in sei punti: cosa funziona, cosa degrada, cosa non attribuire al modello, cosa monitorare, decisione immediata e design necessario per misurare il valore della policy.

---

### Esercizio 15 — Compila la Predictive Decision Card

Una fabbrica vuole prevedere guasti critici con **14 giorni** di anticipo e può ispezionare al massimo **80 macchine a settimana**.

Compila la card completa: decision, prediction unit/time, target/horizon, label maturity, scope, feature availability, baseline, validation, candidate model, ranking/error metrics, calibration se utile, top-K/threshold, capacity/cost matrix, interpretability caveat, monitoring, retraining, fallback, owner/version e release status.

Poi gestisci tre failure mode:

- sensore core mancante;
- precision@80 dimezzata;
- volume di macchine ad alto rischio raddoppiato.

Per ciascuno scegli e giustifica **freeze, fallback, recalibration, retraining o redesign**.

### Ponte al Capitolo 11

Questo capitolo ha reso il tempo e la semantica delle feature parte della validità del modello. Il prossimo farà un passo a monte: quelle feature, metriche e popolazioni devono essere costruite attraverso query e trasformazioni che preservino **grain, chiavi, tempo e definizione**.

Un modello può essere validato perfettamente e ricevere comunque un dataset sbagliato se un join moltiplica righe, una dimensione corrente riscrive il passato o una metrica cambia denominatore. Per questo il prossimo deliverable sarà l'**Analytical Data Contract**.

> **Prima abbiamo imparato a non far entrare il futuro nel modello. Ora dobbiamo imparare a non perdere il significato mentre trasformiamo i dati che il modello e l'analisi useranno.**