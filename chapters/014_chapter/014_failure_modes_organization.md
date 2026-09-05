## 14.13 Failure mode organizzativi: quando la velocità diventa dipendenza condivisa

Finché l'AI entra in una singola analisi, il failure sembra locale. Quando entra in decine di workflow, cambia la scala del problema: owner, metriche, semantic layer, modelli, permission boundary e policy diventano **dipendenze condivise**. Un errore non si replica soltanto più velocemente; può essere confermato da sistemi diversi che in realtà dipendono dalla stessa fonte.

La domanda quindi non è più soltanto "questo agente funziona?". È:

> **quale infrastruttura organizzativa stiamo creando mentre automatizziamo?**

Possiamo leggere i principali failure mode come una stessa progressione:

| Failure mode | Che cosa diventa invisibile | Controllo necessario |
|---|---|---|
| agente orfano | ownership, credenziali, eval, stop policy | named owner + retirement path |
| approval theater | review umana solo nominale | review capacity + evidence interface + override log |
| failure correlato | dipendenza comune tra output apparentemente indipendenti | dependency map + independent evidence |
| claim promotion | un downstream agent aumenta la certezza | claim metadata + gate tra step |
| local metric optimization | KPI locale separato dal valore reale | objective + guardrails + downstream outcome |
| feedback loop | dati futuri influenzati dalla policy | decision/exposure logging |
| deskilling selettivo | perdita delle capacità di supervisione | skill fallback + review practice |
| shadow AI | dati, output e incidenti fuori governance | approved path + inventory |
| assenza di stop policy | loop di ricerca senza valore marginale | step/cost/information stop conditions |
| nessun inventario | impossibilità di governare scala e dipendenze | Agent Registry |

### Ownership: un workflow che gira non è un workflow posseduto

Un analyst può costruire un agente per il weekly forecast e cambiare team sei mesi dopo. Il workflow continua a funzionare, ma nessuno sa chi può cambiare le istruzioni, quale semantic model usa, quali credenziali possiede, chi riceve gli alert o quale eval autorizza una nuova versione. Tecnicamente non è rotto; operativamente è **orfano**.

Per un workflow ricorrente l'owner non è metadata decorativo. È la persona o funzione che può fermarlo, approvare cambiamenti e accettarne la responsabilità.

### Human-in-the-loop può diventare approval theater

Se un agente produce 80 raccomandazioni al giorno e una persona deve cliccare "Approve", dopo qualche settimana la review può ridursi a pochi secondi. Il controllo esiste formalmente ma non sostanzialmente. Un checkpoint umano funziona solo se il volume consente una review reale, l'interfaccia mostra evidenza e caveat, il reviewer sa cosa verificare e il sistema misura override e disagreement.

### Tre agenti non sono tre fonti indipendenti

Finance report, anomaly agent ed executive summary possono sembrare percorsi separati, ma se tutti leggono la stessa misura `Revenue_Current`, una modifica semantica errata può propagarsi a tutti. La triangolazione diventa falsa. Ogni confronto tra output deve quindi considerare **l'indipendenza dei percorsi che li hanno prodotti**.

Questo vale anche per il claim. Un anomaly agent può scrivere "pattern compatibile con possibile problema di pricing" e un executive-summary agent trasformarlo in "il pricing ha causato il calo". Il failure non avviene nel dato, ma nella promozione del livello di certezza. Gli artefatti intermedi devono quindi trasportare almeno metadata come:

```text
claim_level: L2
status: PROVISIONAL
causal_identification: NO
uncertainty: medium
```

Il downstream non può aumentarli senza un nuovo gate.

### Ottimizzare il KPI sbagliato

Un agente Marketing valutato soltanto sul ROAS può concentrare budget sui clienti già vicini all'acquisto. Il ROAS migliora mentre l'incremental revenue resta piatta. Lo stesso pattern compare quando premiamo "ticket chiusi", "automation rate" o "forecast error medio" senza guardrail. L'agente può fare esattamente ciò che gli abbiamo chiesto e produrre un risultato globalmente peggiore.

Per questo ogni objective deve essere legato a outcome downstream e guardrail. La funzione obiettivo è parte del contract, non un dettaglio di monitoring.

### Feedback loop: il modello cambia il dato che userà domani

Se uno score determina quali clienti ricevono un intervento, gli outcome futuri incorporano la policy del modello precedente. Retrainare senza registrare decisione ed exposure può confondere comportamento naturale, effetto dell'intervento e selection policy. L'AI può accelerare questo loop perché automatizza score, azione e aggiornamento. Il logging di **chi è stato esposto a quale policy e quando** diventa quindi parte della qualità del dato futuro.

### Preservare le competenze che servono per supervisionare

Non è necessario che ogni analyst continui a scrivere ogni join a memoria. Ma l'organizzazione deve conservare le capacità necessarie a riconoscere i failure che l'automazione può nascondere: grain e cardinalità, semantica temporale, statistical e causal reasoning, baseline, reconciliation, lettura di query e trace, capacità di riconoscere output fuori dominio.

Il rischio non è "usare troppo AI". È perdere proprio la competenza necessaria per dire **quando non fidarsi**.

### Shadow AI e percorso approvato

Se il percorso ufficiale è troppo lento o poco utile, i team possono incollare customer list, ticket o contratti in strumenti non approvati. L'organizzazione perde visibilità su dati esposti, retention, decisioni e incidenti. La risposta non può essere soltanto il divieto: serve un percorso approvato abbastanza utile da ridurre l'incentivo allo shadow workflow.

### Agent Registry e control plane minimo

Quando i workflow diventano numerosi, un inventario minimo è necessario:

```text
agent/workflow:
owner:
business purpose:
risk tier:
autonomy level:
data domains:
tools/actions:
production users:
eval suite:
last review:
incident contact:
retirement condition:
```

Da qui emerge un control plane organizzativo essenziale:

```text
inventory
→ identity & access
→ approved data/tool boundaries
→ evaluation
→ observability
→ incident management
→ change control
→ retirement
```

Microsoft, nel proprio *AI agent shared responsibility model*, rende esplicito che il deployer conserva responsabilità su dati, identità, least privilege, autorizzazione delle azioni, human oversight e governance d'uso anche quando usa piattaforme gestite.

Fonte: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

> **La scala dell'AI non moltiplica soltanto il lavoro prodotto. Moltiplica anche le dipendenze. Governare agenti significa rendere visibili owner, confini, obiettivi e failure correlati prima che la velocità li trasformi in infrastruttura invisibile.**
