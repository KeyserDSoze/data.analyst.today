## 18.1 Metriche certificate e ownership
Quando un'organizzazione cresce, il problema raramente è la mancanza di numeri.

È l'eccesso di versioni dello stesso numero.

“Revenue” può significare booked revenue, billed revenue, recognized revenue, net revenue o gross merchandise value.

“Active customer” può significare:

- almeno un login negli ultimi 30 giorni;
- almeno un ordine;
- almeno una transazione riuscita;
- subscription non cancellata;
- utilizzo superiore a una soglia.

Finché un analyst lavora da solo, queste differenze possono essere gestite informalmente.

Quando dieci team consumano la stessa metrica, diventano un problema di sistema.

## Una metrica non è solo una formula

Una metrica affidabile dovrebbe avere almeno:

- nome;
- definizione business;
- formula;
- grain;
- popolazione inclusa ed esclusa;
- finestra temporale;
- timezone;
- source of truth;
- owner;
- data freshness attesa;
- eventuali limitazioni note;
- versione o data di validità.

Il punto più trascurato è spesso l'owner.

Chi decide cosa significa “active customer”?

Il data team può implementare la logica, ma la semantica deve avere un proprietario riconoscibile.

## Due ownership diverse

È utile distinguere almeno:

### Business owner

Risponde del significato.

Esempio: Finance è owner della definizione di recognized revenue.

### Technical owner

Risponde dell'implementazione, disponibilità e qualità del dato.

Esempio: Analytics Engineering mantiene la pipeline che produce la metrica.

Se queste responsabilità sono confuse, accadono due errori opposti.

Il data team prende decisioni semantiche che dovrebbe prendere il business.

Oppure il business modifica una definizione senza comprendere gli impatti tecnici downstream.

## Caso realistico: tre NRR nello stesso board pack

Una società SaaS prepara il board meeting.

La stessa presentazione contiene:

- NRR = 108% nella slide Finance;
- NRR = 104% nella slide Customer Success;
- NRR = 111% nella slide Product.

Tutti i numeri sono matematicamente corretti.

Finance esclude contratti non ancora riconosciuti.

Customer Success misura account assegnati alle proprie regioni.

Product include expansion maturata entro 30 giorni dal rinnovo.

Il problema non è SQL.

È governance semantica.

Il team costruisce quindi una definizione certificata:

**NRR = opening recurring revenue della coorte + expansion − contraction − churn, diviso opening recurring revenue**, con regole esplicite per currency, M&A, account migration e timing.

Le altre varianti non vengono vietate.

Vengono rinominate.

Per esempio:

- CS-managed NRR;
- recognized NRR;
- product cohort NRR.

Questa scelta apparentemente lessicale cambia la qualità delle conversazioni.

## Certification non significa immobilità

Una metrica certificata può cambiare.

Anzi, deve poter evolvere.

Ma il cambiamento richiede disciplina.

Se modifichiamo la definizione di active user, dobbiamo sapere:

- da quale data vale?
- il passato viene ricalcolato?
- le dashboard storiche cambieranno?
- le soglie di alert devono cambiare?
- i modelli che usano quella feature devono essere retrainati?
- quali consumer devono essere informati?

La semantica ha una lifecycle esattamente come il software.

## Il semantic layer come infrastruttura organizzativa

Le piattaforme moderne stanno rendendo questa idea più esplicita. La documentazione Databricks del 2026 descrive metric views, domini, pagine autorevoli e segnali di certification/deprecation come strumenti per assicurare che utenti umani e sistemi AI interpretino i dati in modo coerente sotto un unico modello di governance.

Questo è particolarmente importante nell'era degli agenti.

Se un analista umano può chiedere chiarimenti, un agente tende spesso a utilizzare la prima definizione disponibile.

Più aumentiamo l'automazione, più dobbiamo ridurre l'ambiguità semantica a monte.

## Un principio importante

> **Self-service senza semantica condivisa non è democratizzazione dei dati. È democratizzazione dell'incoerenza.**

La maturità non consiste nel permettere a tutti di calcolare qualsiasi cosa.

Consiste nel rendere semplici le metriche comuni, esplicite le varianti e visibile la responsabilità.

## Scheda minima di una metrica

Un'organizzazione può partire anche da qualcosa di molto semplice:

| Campo | Esempio |
|---|---|
| Nome | Net Revenue Retention |
| Business owner | VP Finance |
| Technical owner | Analytics Engineering |
| Grain | customer × month |
| Formula | (Opening ARR + expansion - contraction - churn) / Opening ARR |
| Esclusioni | trial, internal accounts, acquired portfolios fino alla normalizzazione |
| Fonte | billing_curated |
| Freshness | entro 07:00 CET del giorno lavorativo successivo |
| Certification | certified |
| Versione | v3, valida dal FY2027 |

Non serve iniziare con un catalogo gigantesco.

Serve iniziare dalle metriche che cambiano decisioni.

**Quando una metrica entra nei processi decisionali ricorrenti, la sua definizione diventa infrastruttura.**

## Fonti

- Databricks, *Unity Catalog semantics*: https://docs.databricks.com/gcp/en/uc-semantics
- Databricks, *Guiding principles — Curate data and offer trusted data-as-products*: https://docs.databricks.com/gcp/en/lakehouse-architecture/guiding-principles
