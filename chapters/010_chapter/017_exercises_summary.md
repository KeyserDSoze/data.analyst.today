## 10.17 Sintesi ed esercizi: prevedere bene non basta

Questo capitolo ha introdotto i principali strumenti predittivi che un Data Analyst deve saper comprendere, valutare e contestualizzare.

Il punto centrale non è diventare specialisti di machine learning.

È imparare a distinguere tra:

- adattamento ai dati passati;
- capacità di generalizzare;
- utilità operativa;
- interpretazione corretta;
- valore decisionale.

### Cosa portare via dal capitolo

Una regressione lineare o logistica può essere più utile di un modello complesso se è più stabile e interpretabile.

Un coefficiente non è automaticamente una causa.

Una feature importance non è automaticamente una spiegazione causale.

Un'accuracy alta può essere inutile con classi sbilanciate.

Una ROC-AUC eccellente può non tradursi in una soglia operativa sostenibile.

Un modello ben calibrato può essere più utile di uno con ranking leggermente migliore.

Un modello che performa bene offline può degradare in produzione per drift, cambi di processo, feedback loop o limiti operativi.

E soprattutto:

> il valore del modello dipende da ciò che succede dopo la previsione.

---

### Esercizio 1 — Il modello di churn “migliorato”

Un'azienda SaaS confronta due modelli.

| Modello | AUC train | AUC test |
|---|---:|---:|
| A | 0,79 | 0,77 |
| B | 0,96 | 0,78 |

Il modello B usa 240 feature, il modello A ne usa 22.

Domande:

1. Quale modello mostra più rischio di overfitting?
2. Il miglioramento da 0,77 a 0,78 giustifica la complessità?
3. Quali altri criteri useresti prima di scegliere?

---

### Esercizio 2 — Fraud detection

Su 500.000 transazioni, lo 0,4% è fraudolento.

Il modello produce:

- recall 85%;
- precision 12%.

Domande:

1. Quante frodi intercetta?
2. Quanti falsi positivi genera circa?
3. Quali costi devi conoscere per scegliere una soglia?
4. Perché accuracy non è una metrica sufficiente?

---

### Esercizio 3 — Leakage temporale

Vuoi prevedere quali clienti non rinnoveranno un abbonamento 30 giorni prima della scadenza.

Tra le feature trovi:

- numero ticket ultimi 90 giorni;
- ultima data login;
- sconto applicato al rinnovo;
- numero email ricevute;
- esito chiamata retention.

Quali variabili potrebbero contenere leakage e perché?

---

### Esercizio 4 — Feature importance

Un modello di default assegna elevata importanza alla variabile `numero_solleciti_pagamento`.

Il business conclude:

> “I solleciti causano il default, quindi dobbiamo mandarli meno spesso.”

Spiega perché la conclusione non è giustificata.

Quali analisi ulteriori proporresti?

---

### Esercizio 5 — Cross-validation temporale

Un retailer vuole prevedere domanda settimanale.

Il team usa random 5-fold cross-validation su tre anni di dati e ottiene MAPE 8%.

Quando testa sugli ultimi tre mesi, il MAPE sale al 17%.

Elenca almeno tre possibili spiegazioni e proponi una strategia di validation più realistica.

---

### Esercizio 6 — Calibration

Un modello assegna probabilità media di default del 20% a un gruppo di 10.000 clienti.

Dopo sei mesi, solo il 9% va realmente in default.

Domande:

1. Che problema osservi?
2. Il ranking del modello potrebbe comunque essere buono?
3. Perché questa differenza è importante se il punteggio viene usato per pricing o provisioning?

---

### Esercizio 7 — Drift o failure?

Un modello di cancellazione alberghiera mostra forte drift nella distribuzione del valore della prenotazione.

La performance, quando arrivano le label, rimane però stabile.

Che cosa concludi?

Quali controlli manterresti attivi?

---

### Esercizio 8 — Caso leadership meeting

Un modello di churn entra in produzione con questi risultati:

- AUC offline: 0,88;
- precision top 5%: 47%;
- dopo quattro mesi precision top 5%: 31%;
- il team retention riesce a contattare solo il 58% dei clienti selezionati;
- il tasso di accettazione delle offerte è sceso dal 36% al 21%;
- la composizione dei nuovi clienti è cambiata dopo una campagna marketing.

Prepara una conclusione per il management separando:

1. problemi del modello;
2. problemi dei dati;
3. problemi operativi;
4. problemi di efficacia dell'intervento;
5. azioni da intraprendere.

---

### Autovalutazione

Dovresti essere in grado di spiegare con parole semplici:

- differenza tra regressione lineare e logistica;
- differenza tra train, validation e test;
- che cos'è il data leakage;
- cosa significano precision e recall;
- perché la soglia è una decisione business;
- che cos'è la calibration;
- differenza tra underfitting e overfitting;
- perché serve regularizzazione;
- come scegliere una cross-validation coerente;
- perché feature importance non significa causalità;
- cosa sono data drift e concept drift;
- perché un modello in produzione deve essere monitorato.

Se riesci a rispondere a queste domande collegandole a una decisione reale, hai capito il cuore del predictive modeling per un Data Analyst.