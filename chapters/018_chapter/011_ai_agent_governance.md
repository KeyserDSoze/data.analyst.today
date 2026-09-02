## 18.10 AI e agenti come servizi operativi

Nel Capitolo 14 abbiamo costruito workflow AI-assisted controllabili attraverso Context Pack, permission boundary, Verification Bundle, eval ed escalation.

Quando quel workflow diventa ricorrente, il problema cambia ancora.

Non stiamo più governando soltanto una singola analisi.

Stiamo operando **un servizio che può agire molte volte, su dati che cambiano, con tool che cambiano e sotto pressioni diverse**.

La domanda quindi non è più soltanto:

> “Questo agente ha prodotto una risposta corretta?”

È:

> **“Possiamo mantenerlo affidabile, osservabile e revocabile mentre il sistema evolve?”**

## Dal prompt al servizio

Un agente operativo comprende almeno:

- modello;
- system instructions;
- Context Pack o knowledge source;
- tool e API;
- permission scope;
- semantic layer disponibile;
- policy;
- memory/state;
- eval suite;
- monitoring;
- escalation path;
- owner.

Cambiarne uno può cambiare il comportamento del sistema anche se il prompt principale resta identico.

Per questo l'oggetto operativo non è il prompt.

È l'**agent configuration effettivamente eseguita**.

## Agent Operating Profile

Per ogni agente ricorrente l'Analytics Operating Contract dovrebbe collegarsi a un profilo minimo.

| Campo | Esempio |
|---|---|
| Agent purpose | triage anomalie revenue |
| Criticality | T2 business-critical |
| Owner | Analytics Platform |
| Decision owner | VP Finance |
| Allowed data | certified finance + commerce marts |
| Allowed tools | read-only SQL, lineage, incident ticket |
| Forbidden actions | write warehouse, publish KPI, change metric definitions |
| Autonomy | investigate + recommend, no irreversible action |
| Eval suite | semantic, SQL, anomaly, abstention, escalation |
| Runtime budget | max 12 tool call per investigation |
| Stop conditions | source conflict, non-ready data, unsupported causal claim |
| Escalation | on-call analytics + metric owner |
| Audit | full execution manifest retained |
| Review cadence | monthly + on model/tool/policy change |

La tabella serve a rendere l'agente trattabile come un prodotto operativo, non come una capacità indefinita.

## Il lifecycle operativo

Un agente maturo dovrebbe attraversare stati riconoscibili.

### 1. REGISTER

Documentiamo purpose, owner, data boundary, tool boundary, risk tier e consumer.

Un agente non registrato che può accedere a sistemi produttivi è **shadow AI**.

### 2. EVALUATE

Prima del deploy verifichiamo almeno:

- casi normali;
- edge case;
- dati incompleti;
- conflitti tra fonti;
- richieste fuori scope;
- prompt injection o input ostili quando rilevante;
- tool failure;
- situazioni in cui la risposta corretta è `STOP` o `ESCALATE`.

Il risultato deve essere legato ai failure mode più costosi, non soltanto a una media aggregata.

### 3. DEPLOY

Il rollout dovrebbe essere proporzionato al rischio.

Possibili modalità:

- shadow mode;
- suggestion-only;
- human approval;
- limited audience;
- limited action scope;
- full autonomy solo dove impatto e reversibilità lo permettono.

### 4. MONITOR

Dopo il deploy monitoriamo non soltanto uptime e latency.

Possibili indicatori:

- abstention/escalation rate;
- tool failure;
- unsupported-claim rate;
- query/data reconciliation failure;
- costo per run;
- tool call per task;
- human override rate;
- downstream incident;
- distribution shift dei task;
- tasso di azioni rollbackate;
- qualità su un campione continuamente riesaminato.

### 5. INCIDENT

Un agente può generare incidenti diversi da una pipeline tradizionale.

Esempi:

- usa un asset deprecated;
- rafforza una causal claim;
- sceglie un tool fuori dal percorso atteso;
- entra in loop e consuma risorse;
- usa dati incompleti senza degradare il claim;
- propaga una stessa assunzione sbagliata su molti consumer.

Il runbook deve poter:

- disabilitare l'agente;
- revocare un tool;
- ridurre l'autonomia;
- forzare suggestion-only;
- passare a last-known-good configuration;
- notificare i consumer di output già prodotti.

### 6. CHANGE

Una modifica a modello, tool, permission, knowledge source o policy deve avere un change classification.

Per esempio:

- cambio copy del prompt → low risk;
- nuovo warehouse tool → capability change;
- write permission → authority change;
- semantic model v2 → context/semantic change;
- modello differente → behavior change.

I cambi più importanti richiedono re-eval e rollout controllato.

### 7. REVOKE / RETIRE

Un agente deve poter essere spento.

Possibili trigger:

- owner assente;
- eval sotto soglia;
- sistema sostituito;
- cost-to-serve eccessivo;
- permission non più giustificate;
- processo business non più esistente;
- incident rate incompatibile con il tier.

L'assenza di una retirement policy crea agenti orfani con credenziali e autorità che sopravvivono al loro scopo.

## Human oversight deve avere capacità reale

Scrivere `human-in-the-loop` in un diagramma non risolve il problema.

La review deve specificare:

- **chi** approva;
- **che cosa** vede;
- **entro quanto tempo** deve reagire;
- **quale autorità** ha per bloccare o rollbackare;
- **che cosa succede** se non risponde.

Se il reviewer riceve cento richieste al giorno, senza priorità e senza evidenza sufficiente, abbiamo costruito **approval theater**.

Il controllo esiste formalmente ma non operativamente.

## Budget di autonomia

L'autonomia non è soltanto `read` vs `write`.

Possiamo limitare anche:

- numero di tool call;
- spesa per task;
- durata;
- profondità di iterazione;
- numero di consumer coinvolti;
- valore economico massimo dell'azione;
- ampiezza del rollout;
- frequenza di esecuzione.

Questi limiti trasformano un'autonomia generica in un **budget operativo**.

## Caso simulato/composito: l'agente che ottimizza il criterio sbagliato

Un retailer usa un agente per proporre automaticamente la pressione promozionale settimanale.

Objective iniziale:

> massimizzare contribution margin nelle quattro settimane successive.

L'agente riduce gli incentivi sui segmenti nei quali il modello ha bassa probabilità di conversione.

Nel breve periodo il margine migliora.

Dopo qualche settimana emerge però che la policy ha quasi eliminato l'esplorazione su clienti nuovi e segmenti poco conosciuti.

Il sistema non ha violato il proprio objective.

Ha rivelato che l'objective era incompleto.

Il redesign aggiunge guardrail su:

- quota new customers;
- exploration budget;
- coverage dei segmenti;
- concentrazione della spesa;
- long-term value;
- feedback loop.

E riduce l'autonomia da `execute` a `recommend + bounded rollout` finché gli eval non coprono meglio il failure mode.

## Governance dei failure correlati

Con molti agenti emerge un rischio organizzativo nuovo.

Cinque workflow possono sembrare indipendenti ma usare:

- la stessa semantic metric sbagliata;
- lo stesso modello;
- la stessa knowledge source;
- la stessa assunzione sul business;
- lo stesso tool con un bug.

Quindi la governance deve poter rispondere anche a:

> **“Quali agenti e decisioni sono esposti a questo componente?”**

Servono registry, lineage delle dipendenze e capability di revoca trasversale.

## Il legame con il framework NIST

Il NIST AI Risk Management Framework e il profilo per la Generative AI trattano la trustworthiness come una proprietà da gestire lungo design, sviluppo, uso ed evaluation di prodotti e sistemi AI.

Per il nostro operating model la lezione è semplice:

**un eval pre-deploy non sostituisce monitoring, ownership e change management dopo il deploy**.

Fonti pubbliche:

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## Una regola operativa

> **Un agente pronto per una demo non è automaticamente pronto per possedere una parte di un processo ricorrente.**

La maturità si vede quando il sistema sa non soltanto agire, ma anche **degradare, fermarsi, essere revisionato, perdere autorità ed essere ritirato**.
