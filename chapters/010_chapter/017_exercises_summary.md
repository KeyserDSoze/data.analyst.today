## 10.17 Sintesi ed esercizi: prevedere bene non basta

Il predictive modeling viene spesso raccontato come una gara tra algoritmi.

Il lavoro reale assomiglia di più a una catena di contratti:

**decisione → prediction time → target → feature `as-of` → baseline → validation → score → calibration → policy → operations → monitoring → outcome.**

Un errore in uno di questi passaggi può rendere inutile un modello tecnicamente eccellente.

Il deliverable del capitolo è la **Predictive Decision Card**. Serve a rendere esplicito non soltanto come il modello è stato addestrato, ma **quale promessa operativa stiamo facendo quando usiamo il suo output**.

### Le domande da portare via

Prima di fidarti di un sistema predittivo, chiedi:

1. cosa predice esattamente e a quale momento?
2. tutte le feature esistevano davvero a quel prediction time?
3. la validation simula il deployment reale?
4. il modello batte una baseline semplice fuori campione?
5. ordina bene i casi dove il business può agire?
6. se gli score vengono chiamati probabilità, sono calibrati?
7. threshold/top-K rispettano costi e capacità?
8. feature importance viene distinta dalla causalità?
9. che cosa monitoriamo prima e dopo l'arrivo delle label?
10. come separiamo performance del modello, execution della policy ed effetto dell'intervento?

> **Il modello migliore non è quello che conosce meglio il passato. È quello che mantiene una promessa utile quando incontra dati, persone e processi che non erano nel notebook.**

---

### Esercizio 1 — Definisci la prediction task prima di scegliere il modello

Un marketplace dice:

> "Vogliamo prevedere i seller problematici."

Sai che il team Risk può revisionare 800 seller a settimana.

Costruisci una prima specifica indicando:

- prediction unit;
- prediction time;
- horizon;
- target osservabile;
- label maturity;
- azione prevista;
- capacità;
- baseline.

Poi spiega perché queste tre domande rappresentano progetti differenti:

- seller che riceveranno almeno un reclamo nei prossimi 30 giorni;
- seller che genereranno perdita netta superiore a €1.000;
- seller su cui una review preventiva ridurrà davvero il danno.

---

### Esercizio 2 — Il modello più complesso ha davvero vinto?

Un SaaS confronta:

| Modello | Feature | AUC train | AUC test | Precision@2000 |
|---|---:|---:|---:|---:|
| Logit | 22 | 0,79 | 0,77 | 36% |
| Boosting | 240 | 0,96 | 0,78 | 37% |

Il boosting richiede una feature pipeline aggiuntiva, serving più costoso e explanations più complesse.

Prepara una **complexity justification**:

- qual è il miglioramento realmente out-of-sample?
- quanto cambia la decisione nei primi 2.000 casi?
- quali slice controlleresti?
- quale costo operativo aggiuntivo deve essere giustificato?
- quale modello promuoveresti e quali informazioni mancano?

---

### Esercizio 3 — Leakage `as-of`

Vuoi prevedere, 30 giorni prima della scadenza, quali clienti non rinnoveranno.

Feature candidate:

- ticket aperti nei 90 giorni precedenti al prediction time;
- ultima data login salvata nello snapshot storico;
- `current_contract_status` letto dalla tabella corrente;
- sconto di rinnovo applicato 10 giorni prima della scadenza;
- esito della chiamata retention;
- saldo fatture al prediction time.

Per ogni feature classifica:

- utilizzabile;
- leakage evidente;
- utilizzabile solo se ricostruita `as-of`;
- dipendente dalla precisa policy/timing del processo.

Poi scrivi la query concettuale:

> "Che cosa sapevamo esattamente alla data X?"

---

### Esercizio 4 — Preprocessing leakage

Hai 300 osservazioni e 8.000 feature.

Il team esegue:

1. feature selection sull'intero dataset;
2. split train/test;
3. training;
4. accuracy 0,79.

Il target è quasi casuale.

Spiega:

- dove entra informazione del test;
- perché molte feature rendono più facile trovare correlazioni casuali;
- come ricostruire la pipeline corretta;
- perché un `Pipeline` object può aiutare ma non sostituisce il ragionamento sul prediction time.

Confronta il caso con l'esempio documentato di scikit-learn sulle 10.000 feature casuali.

---

### Esercizio 5 — Random split o deployment simulation?

FinSure deve prevedere default su nuovi prestiti.

Il dataset contiene cinque anni, ma negli ultimi nove mesi sono cambiati underwriting e acquisition channels.

Con random split:

- ROC-AUC: 0,88.

Con out-of-time test:

- ROC-AUC: 0,76.

Rispondi:

1. quale numero è più vicino alla decisione futura?
2. il modello è necessariamente peggiorato o è cambiata la domanda di generalizzazione?
3. useresti anche group split per cliente/azienda?
4. quale validation design statement inseriresti nella card?

---

### Esercizio 6 — Ranking buono, calibration cattiva

Un modello di default ha ROC-AUC 0,86.

Per clienti con score medio 30% osservi default 14%.

Domande:

- il ranking può essere ancora utile?
- puoi usare direttamente lo score in `PD × LGD × EAD`?
- quale reliability analysis faresti?
- come impareresti un calibratore senza contaminare la valutazione?
- dopo recalibration useresti lo stesso test set per dichiarare la performance finale?

---

### Esercizio 7 — Threshold 0,5 o capacità 900?

Un modello predice escalation dei ticket.

A soglia 0,5 genera 280 alert/giorno. Il team specializzato può gestirne 900.

A soglia 0,27 genera 860 alert con:

- precision inferiore;
- recall molto maggiore;
- costo medio di review €4;
- costo medio di un'escalation persa €180.

Costruisci una policy decisionale confrontando:

- threshold;
- top-K;
- expected cost;
- capacità.

Spiega perché la soglia non è una proprietà del classifier.

---

### Esercizio 8 — Evento raro e volume operativo

SafePay processa 500.000 transazioni; frode 0,4%.

Alla soglia corrente:

- recall: 85%;
- precision: 12%.

Calcola circa:

- frodi totali;
- frodi intercettate;
- numero totale di alert;
- falsi positivi.

Poi rispondi:

- se la coda manuale può gestire 4.000 casi, la policy è sostenibile?
- quali costi devono essere stimati?
- perché bilanciare artificialmente il test set renderebbe la precision poco trasferibile alla produzione?

---

### Esercizio 9 — Feature importance non è intervention map

Un modello di churn mostra:

1. failed payments;
2. numero ticket;
3. tenure;
4. response time support;
5. login frequency.

Il management vuole trasformare la classifica in un piano d'azione.

Crea una tabella con colonne:

- predictive importance;
- modificabile?;
- possibile causa o solo segnale?;
- evidenza causale disponibile?;
- prossimo passo.

Indica quali domande appartengono al Capitolo 8/9 anziché al predictive modeling.

---

### Esercizio 10 — Drift non significa retraining automatico

Un modello antifrode mostra forte shift nel valore medio delle transazioni dopo una campagna.

Quando le label maturano:

- ROC-AUC stabile;
- precision@K stabile;
- calibration stabile.

Che cosa concludi?

Disegna un monitoring response distinguendo:

- data drift;
- predictive failure;
- alert investigativo;
- retraining trigger.

Poi considera il caso opposto: feature distributions apparentemente stabili, ma calibration peggiora. Perché anche questo è possibile?

---

### Esercizio 11 — Training-serving skew

Il modello è stato addestrato con `customer_balance_30d` calcolato da una pipeline batch alle 23:59.

In serving viene usata una query realtime con:

- timezone diversa;
- esclusione differente dei refund;
- aggiornamenti parziali delle ultime due ore.

Offline AUC rimane ottima, online la precision scende.

Prepara una diagnosi:

- come confronteresti feature training vs serving sugli stessi esempi?
- quali metriche di skew registreresti?
- congelaresti il modello, la feature o la policy?
- come eviteresti che la divergenza ricompaia?

---

### Esercizio 12 — Feedback loop

Un churn model seleziona i 5.000 clienti più a rischio. Tutti ricevono un voucher.

Tre mesi dopo molti clienti ad alto score non hanno churnato.

Il team conclude:

> "Il modello genera troppi falsi positivi."

Spiega almeno tre possibilità alternative:

1. modello davvero sovrastimato;
2. voucher efficace;
3. selezione/label alterata dal processo operativo.

Proponi un modo per separare predictive evaluation e treatment effect, usando i concetti dei Capitoli 8 e 9.

---

### Esercizio 13 — Model metric buona, decision system cattivo

Un modello di retention ha:

- AUC stabile a 0,84;
- calibration stabile;
- precision@2000 stabile al 40%.

Ma:

- il contact rate scende dal 92% al 55%;
- time-to-contact passa da 8 a 40 ore;
- acceptance dell'offerta passa dal 30% al 17%;
- costo voucher cresce del 35%.

Il modello è "sano"?

Scrivi una risposta che separi:

- model health;
- operational execution;
- treatment efficacy;
- economics;
- decision status.

---

### Esercizio 14 — Leadership meeting: OrbitCom

Hai questa slide:

> "Churn model AUC 0,87. Progetto ML riuscito."

Le informazioni complete sono:

- baseline precision@25k: 24%;
- modello: 44% offline, 29% dopo tre mesi;
- nuova acquisition campaign cambia il mix clienti;
- calibration peggiora sui clienti nuovi;
- contact rate scende al 63%;
- gli utenti ad alto score vengono trattati, quindi le label future incorporano il programma retention;
- il team non ha ancora un holdout per misurare incremental churn saved.

Scrivi un executive summary in sei punti:

1. cosa funziona;
2. cosa è degradato;
3. cosa non possiamo attribuire al modello;
4. che cosa monitorare;
5. quale decisione prendere ora;
6. quale esperimento/design serve per misurare il valore della policy.

---

### Esercizio 15 — Compila la Predictive Decision Card

Una fabbrica vuole prevedere guasti critici delle macchine con 14 giorni di anticipo. Può ispezionare al massimo 80 macchine a settimana.

Costruisci l'intera card:

- decision;
- prediction unit/time;
- target/horizon;
- label maturity;
- scope;
- feature availability;
- baseline;
- validation design;
- candidate model;
- ranking/error metrics;
- calibration, se necessaria;
- top-K/threshold;
- capacity e cost matrix;
- interpretability caveat;
- monitoring;
- retraining;
- fallback;
- owner/version;
- release status.

Poi immagina tre failure mode:

- sensore core mancante;
- precision@80 dimezzata;
- volume di macchine ad alto rischio raddoppiato.

Per ciascuno indica se serve **freeze, fallback, recalibration, retraining o redesign**.

### Autovalutazione

Dovresti essere in grado di spiegare senza rifugiarti nel nome di un algoritmo:

- che cos'è il prediction time e perché governa le feature;
- come scegliere uno split che simuli il deployment;
- che differenza c'è tra leakage e training-serving skew;
- perché una baseline semplice è obbligatoria;
- differenza tra ranking, calibration e threshold;
- perché class imbalance è soprattutto un problema di base rate e capacità;
- come giustificare complessità e regularizzazione;
- perché permutation importance non dimostra causalità;
- che differenza c'è tra data drift, predictive degradation e decision drift;
- perché uno score che attiva un intervento crea un feedback loop;
- cosa contiene una Predictive Decision Card.

Se queste risposte sono chiare, il predictive modeling non è più una collezione di algoritmi. È diventato un sistema controllabile per trasformare informazione incompleta sul futuro in una decisione migliore.
