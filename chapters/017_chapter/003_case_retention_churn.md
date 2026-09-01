## 17.2 “Quali clienti dobbiamo salvare?”: rischio, causa e persuadibilità

### Caso simulato/composito: NorthPeak

Una piattaforma SaaS B2B, **NorthPeak**, vede il logo churn salire dal 2,8% al 4,1% trimestrale.

Il Chief Customer Officer chiede:

> “Quali clienti dobbiamo salvare subito?”

La frase sembra chiedere un churn model.

In realtà contiene almeno quattro decisioni:

1. dove nasce il deterioramento?
2. quali account hanno probabilità elevata di non rinnovare?
3. quali account possono essere influenzati da un intervento?
4. quali interventi hanno valore economico positivo dato il costo e la capacità del team?

Quattro domande diverse richiedono quattro tipi di evidenza diversi.

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | allocare capacità Customer Success e correggere il meccanismo che genera churn |
| Failure cost | spendere retention budget su clienti irrecuperabili o intervenire troppo tardi |
| Claim necessario | predittivo per priorità; causale per scegliere l'intervento |
| Capacità | 500 interventi ad alta intensità per trimestre |
| Reversibilità | alta per targeting; media per redesign onboarding |
| Stop rule | nessuna campagna sui top-risk finché rischio e persuadibilità non sono separati |

## 1. Definire churn e popolazione

Il team chiarisce:

- unità: account, non utenti;
- churn: contratto non rinnovato alla data di renewal;
- finestra di previsione: 90 giorni;
- esclusioni: trial, account con meno di 60 giorni di vita, contratti già in dismissione;
- outcome economico: NRR e contribution margin, non soltanto logo retention.

Questa specifica diventa parte dell'**Analytical Brief**.

Senza di essa, un modello potrebbe essere statisticamente buono e semanticamente inutile.

## 2. Prima localizzare il deterioramento

Prima del machine learning, le coorti mostrano che il peggioramento è concentrato nei clienti acquisiti negli ultimi dodici mesi tramite un nuovo partner channel.

Il churn dei clienti direct-sales è quasi stabile.

Il **Lifecycle Diagnostic Map** mostra inoltre:

- activation entro 14 giorni: `71% → 54%`;
- uso della feature core nel primo mese: `-19%`;
- ticket di onboarding: `+32%`;
- time-to-first-value: `+4,6 giorni`.

Il finding più importante non è ancora “questi account sono ad alto rischio”.

È:

> **“Il deterioramento comincia molto prima del rinnovo ed è concentrato in una specifica origine commerciale.”**

Questo cambia la politica possibile: non possiamo aspettare gli ultimi 30 giorni prima del renewal.

## 3. Predictive Decision Card: chi rischia davvero?

Il team costruisce un modello con:

- AUC 0,84;
- calibration verificata per decili di rischio;
- validazione temporale;
- controlli di leakage rispetto a informazioni disponibili soltanto dopo la decisione di rinnovo.

Le feature più informative includono:

- diminuzione di utilizzo;
- mancata attivazione della feature core;
- numero e severità dei ticket;
- distanza dal renewal;
- NPS;
- seat utilization.

Ma la **Predictive Decision Card** registra esplicitamente un limite:

> feature importance non equivale a causalità.

Il fatto che molti ticket predicano churn non significa che ridurre il numero di ticket nel database riduca churn. Potrebbe significare che i ticket sono una conseguenza di problemi più profondi.

## Caso reale documentato: Microsoft Customer Insights

Microsoft documenta un workflow end-to-end di transactional churn prediction che comprende ingestione dei dati, unificazione dei profili, costruzione della transaction history, configurazione del modello, review delle spiegazioni e creazione di segmenti ad alto rischio.

Fonte: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/sample-guide-predict-transactional-churn

Il caso è utile per mostrare cosa fa bene un sistema predittivo: **identificare una popolazione con rischio elevato**.

Non risolve però automaticamente la domanda successiva:

> “Quale intervento cambierà il comportamento di questi clienti?”

Quello è un problema causale e decisionale diverso.

## 4. Risk score non è treatment opportunity

I 500 account con score più alto vengono analizzati economicamente.

Alcuni sono quasi certamente persi per ragioni che un intervento Customer Success non può cambiare:

- azienda chiusa;
- merger;
- budget azzerato;
- migrazione strategica già deliberata;
- prodotto non più compatibile con il processo del cliente.

Questi account possono avere altissimo churn risk e bassissima persuadibilità.

Il team costruisce quindi una matrice:

| | Alta persuadibilità | Bassa persuadibilità |
|---|---|---|
| Alto rischio | priorità di intervento | evitare spreco |
| Basso rischio | test selettivo | nessuna azione |

A questa matrice aggiunge il valore economico del cliente e il costo dell'intervento.

La priorità operativa diventa quindi funzione di:

**rischio × valore × effetto incrementale atteso − costo dell'intervento**.

Non basta ordinare per churn probability.

## 5. Il dato osservazionale può invertire la storia

Storicamente i Customer Success Manager chiamavano soprattutto gli account più fragili.

Nei dati osservazionali, chi riceveva una chiamata churnava di più.

Una lettura ingenua avrebbe concluso:

> “Le chiamate fanno aumentare il churn.”

È selection bias: il trattamento veniva assegnato proprio ai clienti peggiori.

Il **Causal Identification Brief** registra quindi che il confronto trattati/non trattati storico non identifica l'effetto della chiamata.

## 6. Experiment Contract: quale intervento cambia davvero l'esito?

Il team decide di randomizzare un nuovo programma di onboarding intensivo su una parte dei nuovi account partner-channel.

L'esperimento viene progettato prima del rollout con:

- unità di randomizzazione: account;
- primary outcome: activation entro 30 giorni;
- outcome downstream: renewal e NRR;
- guardrail: costo CSM, ticket, time-to-resolution;
- segmento: nuovi account partner-channel;
- durata sufficiente a osservare almeno i proxy precoci e successivamente i rinnovi;
- policy di analisi dell'eterogeneità definita prima di guardare i risultati.

La decisione non è “il modello ha trovato gli utenti giusti”.

È costruire una catena in cui prediction e causalità svolgono ruoli differenti.

## 7. Decision Record

Le alternative diventano:

### A — Contattare i 500 score più alti

Semplice, ma tratta rischio e persuadibilità come se fossero la stessa cosa.

### B — Correggere soltanto onboarding partner-channel

Affronta il meccanismo principale, ma ignora account legacy già in deterioramento.

### C — Policy combinata

- correggere onboarding partner-channel;
- intervenire prima, entro i primi 30 giorni;
- usare il risk model per priorità operativa;
- escludere account non persuadibili o economicamente non convenienti;
- usare esperimenti per stimare l'effetto incrementale degli interventi;
- mantenere una coda di monitoraggio sui clienti ad alto valore.

La scelta è C.

## 8. Switching condition

La policy cambierà se:

- l'uplift dell'onboarding intensivo è vicino a zero;
- il costo per renewal salvato supera il contribution margin atteso;
- il partner channel migliora spontaneamente dopo correzioni di processo;
- la calibration del modello degrada;
- la capacità Customer Success cambia in modo sostanziale.

Queste condizioni entrano nel Decision Record prima del rollout.

## 9. Decision Communication Pack

La headline non è:

> “Abbiamo un churn model con AUC 0,84.”

È:

> **“Il deterioramento di churn è concentrato nelle nuove coorti partner-channel e nasce durante l'attivazione. Il risk model ci aiuta a prioritizzare, ma non identifica chi può essere salvato. Proponiamo di correggere onboarding e allocare la capacità retention usando rischio, valore e uplift incrementale.”**

Le evidenze principali sono:

1. cohort comparison;
2. activation path;
3. calibration/risk distribution;
4. economia della capacità;
5. risultato dell'esperimento quando disponibile.

## 10. Outcome review

Metriche:

- 30-day activation;
- time-to-first-value;
- feature adoption;
- renewal rate;
- incremental retention uplift;
- costo per renewal salvato;
- NRR per coorte;
- calibration drift del risk model.

## Cosa abbiamo scelto di non fare

Non serve un modello causale complesso su tutto il customer lifecycle prima di agire.

Non serve nemmeno aspettare il renewal outcome finale per correggere un onboarding chiaramente deteriorato se l'intervento è reversibile e i proxy precoci sono affidabili.

La catena effettiva è:

**Analytical Brief → Lifecycle Diagnostic Map → Predictive Decision Card → Causal Identification Brief → Experiment Contract → Decision Record → Decision Communication Pack**

> **Predire chi perderemo non equivale a sapere chi possiamo salvare. E sapere chi possiamo salvare non equivale ancora a sapere se conviene farlo.**
