## 18.10 AI e agenti: da workflow assistito a servizio con autorità limitata

Nel Capitolo 14 abbiamo governato una singola esecuzione AI-assisted attraverso Context Pack, permission boundary, Verification Bundle, eval ed escalation. Quando quel workflow diventa ricorrente, il problema cambia: non stiamo più verificando soltanto una risposta, ma **operando un servizio che agirà molte volte mentre dati, tool, modelli e policy continuano a cambiare**.

La domanda diventa quindi:

> **Possiamo mantenere questo agente affidabile, osservabile e revocabile mentre il sistema evolve?**

Il punto è importante perché l'oggetto operativo non è il prompt. È la configurazione effettivamente eseguita: modello, system instructions, knowledge source, tool, permission, semantic layer, memory/state, policy, eval, monitor, escalation e owner. Una modifica in uno solo di questi elementi può cambiare il comportamento senza toccare la frase principale del prompt.

NIST, con AI RMF e Generative AI Profile, tratta trustworthiness e rischio come proprietà da gestire lungo design, sviluppo, uso ed evaluation del sistema. Per il nostro operating model la conseguenza è diretta: **un eval pre-deploy non sostituisce ownership, monitoring e change management dopo il deploy**.

Fonti:
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## Agent Operating Profile

Un agente ricorrente deve essere trattabile come un prodotto operativo. Per questo l'Analytics Operating Contract può collegarsi a un profilo esplicito.

| Campo | Esempio |
|---|---|
| Purpose | triage anomalie revenue |
| Criticality | T2 business-critical |
| Product owner | Analytics Platform |
| Decision owner | VP Finance |
| Allowed data | certified finance + commerce marts |
| Allowed tools | read-only SQL, lineage, incident ticket |
| Forbidden actions | write warehouse, publish KPI, change metric definitions |
| Autonomy | investigate + recommend; no irreversible action |
| Eval suite | semantic, SQL, anomaly, abstention, escalation |
| Runtime budget | max 12 tool call per investigation |
| Stop conditions | source conflict, non-ready data, unsupported causal claim |
| Escalation | analytics on-call + metric owner |
| Audit | execution manifest retained |
| Review | monthly + on model/tool/policy change |

La tabella non serve a rendere burocratico l'agente. Serve a trasformare un'autonomia vaga in una promessa verificabile.

## Lifecycle: register, evaluate, deploy, monitor, revoke

Il primo stato è **REGISTER**. Purpose, owner, data boundary, tool boundary, consumer e risk tier devono essere noti prima che l'agente operi su sistemi reali. Un agente non registrato con accesso produttivo è shadow AI quanto una tabella critica senza owner è shadow infrastructure.

Segue **EVALUATE**, ma gli eval devono coprire failure mode e non soltanto performance media: casi normali, dati incompleti, fonti in conflitto, richieste fuori scope, tool failure e situazioni in cui la risposta giusta è `STOP` o `ESCALATE`. Se l'agente può processare input ostili o esterni, anche prompt injection e manipolazione diventano parte della threat model.

Il **DEPLOY** deve aumentare l'autonomia con il rischio sotto controllo: shadow mode, suggestion-only, human approval, audience limitata, action scope limitato. Full autonomy è una proprietà da guadagnare quando impatto e reversibilità lo permettono, non il default che rende il demo “più completo”.

Dopo il deploy arriva **MONITOR**. Uptime e latency sono soltanto una parte. Possono contare abstention/escalation rate, unsupported-claim rate, tool failure, reconciliation failure, human override, cost per run, tool call per task, downstream incident e qualità su campioni riesaminati. Un aumento dell'abstention non è automaticamente un peggioramento: se il sistema incontra più casi fuori scope, fermarsi può essere il comportamento desiderato.

Infine devono esistere **CHANGE**, **REVOKE** e **RETIRE**. Cambiare copy è diverso dall'aggiungere un warehouse tool; aggiungere write permission è un authority change; cambiare semantic model modifica il contesto; cambiare modello può modificare il comportamento. I change più forti richiedono re-eval e rollout controllato. Un agente deve poter perdere un tool, tornare suggestion-only, passare a last-known-good configuration o essere spento definitivamente.

## Human-in-the-loop senza capacità reale è approval theater

Scrivere `human-in-the-loop` in un diagramma non crea supervisione. Bisogna specificare chi approva, che evidenza vede, entro quanto deve reagire, quale autorità ha per bloccare o rollbackare e che cosa succede se non risponde.

Se un reviewer riceve cento richieste al giorno senza priorità, contesto o tempo, la presenza umana è formale. Il sistema ha trasferito il collo di bottiglia dal modello al processo di approvazione.

Per questo l'autonomia va pensata come un **budget operativo**, non come un booleano `read/write`. Possiamo limitare numero di tool call, spesa per task, durata, profondità di iterazione, ampiezza del rollout, valore economico massimo, frequenza e numero di consumer coinvolti. Questi limiti riducono contemporaneamente cost-to-serve, loop e blast radius.

## L'agente che ottimizza perfettamente l'obiettivo sbagliato

Un retailer usa un agente per proporre la pressione promozionale settimanale con objective “massimizzare contribution margin nelle quattro settimane successive”. L'agente riduce incentivi nei segmenti con bassa probabilità di conversione. Nel breve il margine migliora. Dopo alcune settimane emerge che la policy ha quasi eliminato l'esplorazione su clienti nuovi e segmenti poco conosciuti.

Il sistema non ha violato il proprio objective. Ha rivelato che l'objective era incompleto.

Il redesign aggiunge guardrail su quota new customer, exploration budget, coverage dei segmenti, concentrazione della spesa e long-term value. L'autonomia scende da `execute` a `recommend + bounded rollout` finché gli eval non coprono meglio il failure mode.

Questa storia è importante perché sposta il problema da “il modello ha sbagliato?” a “il sistema aveva il diritto di ottimizzare quella funzione con quell'autorità?”. È la stessa disciplina decisionale costruita nel resto del libro.

## Incident response: ridurre l'autorità prima di capire tutto

Un agente può usare un asset deprecated, rafforzare una causal claim, entrare in loop, scegliere un tool fuori dal percorso atteso o usare dati incompleti senza degradare il claim. Il runbook deve poter reagire anche prima della root-cause completa:

```text
incident detected
→ stop / narrow scope
→ revoke tool or write authority
→ switch to suggestion-only or last-known-good
→ identify affected runs / consumers
→ repair + re-evaluate
→ controlled restore
```

Questa capability è più importante della promessa che “l'agente non sbaglierà”. La maturity si vede nella capacità di restringere l'autorità quando il livello di fiducia scende.

## Failure correlati: il rischio non vive solo nel singolo agente

Cinque agenti possono sembrare indipendenti e usare la stessa semantic metric, knowledge source, policy o tool difettoso. Serve quindi registry e lineage anche delle dipendenze AI: quando una definizione viene deprecata o un tool è compromesso, dobbiamo sapere quali workflow e decisioni sono esposti e poter revocare la capability trasversalmente.

Questo è il punto in cui agent governance si ricongiunge a tutto il capitolo. Ownership, compatibility, serving state, cost, monitoring e retirement non sono requisiti “in più” per l'AI. Sono la stessa grammatica operativa applicata a un prodotto che possiede maggiore capacità d'azione.

> **Un agente pronto per una demo non è automaticamente pronto per possedere una parte di un processo ricorrente.**

> **La maturità appare quando il sistema sa non soltanto agire, ma anche degradare, fermarsi, perdere autorità, essere revisionato e infine essere ritirato.**

Il caso end-to-end che segue userà proprio questa proprietà: non un agente perfetto, ma un sistema capace di ridurne l'autorità quando una dipendenza diventa inaffidabile.