## 14.13 Failure mode organizzativi: quando dieci workflow veloci condividono lo stesso errore

Il Capitolo 0 ha già fissato il principio di responsabilità: dire “l'ha fatto l'AI” non è una difesa professionale.

Qui allarghiamo il problema.

Quando l'AI entra in molti processi, il rischio non è più soltanto il singolo output sbagliato.

Diventano importanti i **failure mode organizzativi**:

- ownership assente;
- agenti non inventariati;
- review simboliche;
- dipendenze invisibili;
- metriche locali ottimizzate contro l'obiettivo globale;
- feedback loop;
- deskilling;
- failure correlati tra sistemi che usano lo stesso modello, corpus o semantic layer.

### Failure mode 1 — l'agente orfano

Un analyst costruisce un agente per produrre il weekly forecast.

Dopo sei mesi cambia team.

Il workflow continua a girare.

Nessuno sa con certezza:

- chi può cambiare le istruzioni;
- quale semantic model usa;
- quali credenziali possiede;
- chi riceve gli alert;
- quale eval autorizza una nuova versione;
- come fermarlo.

Il sistema non è necessariamente rotto.

È **senza owner**.

Un workflow senza owner nominato dovrebbe essere considerato un rischio operativo, non un'automazione gratuita.

Microsoft include l'accountability e la presenza di un owner tra i principi pratici per gli agenti responsabili.

Fonte: https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai

### Failure mode 2 — approval theater

Un agente prepara 80 raccomandazioni al giorno e una persona deve cliccare “Approve”.

Dopo alcune settimane la review media dura quattro secondi.

Formalmente esiste human-in-the-loop.

Sostanzialmente no.

Un checkpoint umano è utile soltanto se:

- il volume è compatibile con una review reale;
- l'interfaccia mostra evidenza e caveat;
- il reviewer sa cosa controllare;
- esistono motivi pratici per rifiutare;
- il sistema misura override e disagreement.

Se l'umano non ha tempo, informazioni o autorità, il controllo è decorativo.

### Failure mode 3 — failure correlato

Tre agenti diversi producono:

- report Finance;
- anomaly detection;
- executive summary.

Sembrano tre fonti indipendenti.

In realtà tutti interrogano la stessa misura `Revenue_Current` del semantic layer.

Una modifica errata alla metrica entra in produzione.

Tutti e tre confermano lo stesso numero sbagliato.

La “triangolazione” è falsa perché le fonti condividono una dipendenza comune.

Quando confrontiamo output dobbiamo quindi chiedere:

> **quanto sono indipendenti i percorsi che li hanno prodotti?**

### Failure mode 4 — l'agente downstream promuove la certezza

Un anomaly agent scrive:

> “pattern compatibile con possibile problema di pricing.”

Un executive-summary agent lo trasforma in:

> “Il calo è causato dal pricing.”

Nessuno dei due ha inventato un numero.

La failure avviene nella **trasformazione del livello di claim**.

Per questo gli artefatti intermedi devono trasportare anche metadata come:

```text
claim_level: L2
uncertainty: medium
causal_identification: no
status: provisional
```

Il sistema downstream non può promuovere automaticamente quei campi.

### Failure mode 5 — local metric optimization

Un agente Marketing viene valutato su ROAS.

Impara a concentrare budget sui clienti già vicinissimi all'acquisto.

Il ROAS sale.

L'incremental revenue può restare piatta o scendere.

L'agente sta facendo esattamente ciò che gli abbiamo chiesto.

Il problema è la funzione obiettivo.

Questo pattern appare in molte forme:

```text
reduce tickets → chiudi ticket troppo presto
increase conversion → targetta solo utenti già propensi
reduce forecast error → ignora SKU difficili ma strategici
increase automation rate → evita escalation quando sarebbe necessaria
```

Ogni KPI per un agente deve quindi avere **guardrail e outcome downstream**.

### Failure mode 6 — feedback loop invisibile

Un modello assegna risk score.

Gli operatori intervengono soprattutto sui clienti ad alto rischio.

I loro outcome cambiano proprio a causa dell'intervento.

Il dataset futuro incorpora la policy del modello precedente.

Se retrainiamo senza comprenderlo, il sistema può confondere:

- comportamento naturale;
- effetto dell'intervento;
- selection policy.

L'AI può rendere il loop molto più veloce perché automatizza score, azione e retraining.

Per questo logging di **decisione ed exposure** è parte della qualità del dato futuro.

### Failure mode 7 — deskilling selettivo

Non è necessario che ogni analyst continui a scrivere ogni join a memoria.

Ma il team deve mantenere la capacità di diagnosticare i failure mode che l'AI può nascondere.

Competenze da preservare intenzionalmente:

- grain e cardinalità;
- semantica temporale;
- statistical reasoning;
- causal reasoning;
- baseline construction;
- data reconciliation;
- leggere query e trace;
- riconoscere quando un output è fuori dominio.

Il rischio non è “usare troppo AI”.

È **perdere proprio la competenza necessaria per supervisionarla**.

### Failure mode 8 — shadow AI

Un team usa un assistente non approvato per:

- incollare customer list;
- analizzare contratti;
- riassumere ticket;
- generare report.

Il processo nasce perché è rapido e non richiede procurement.

Ma l'organizzazione perde visibilità su:

- dati esposti;
- retention;
- accessi;
- output usati nelle decisioni;
- incidenti.

La soluzione non è soltanto vietare strumenti.

È creare un percorso approvato abbastanza utile da ridurre l'incentivo allo shadow workflow.

### Failure mode 9 — nessuna stop policy

Un agente continua a:

- generare nuove segmentazioni;
- modificare ipotesi;
- eseguire query;
- consultare altri agenti.

Ogni iterazione sembra costare poco.

Mille iterazioni costano tempo, denaro e attenzione.

Servono stop condition come:

```text
decision threshold raggiunta
marginal information value troppo basso
budget esaurito
numero massimo di step
conflitto non risolto → human escalation
data not ready → stop
```

L'autonomia senza criterio di arresto non è intelligenza. È un loop.

### Failure mode 10 — nessun inventario degli agenti

Se l'organizzazione non sa quanti agenti esistono, non può governare:

- owner;
- permessi;
- rischio;
- dipendenze;
- modello/versione;
- costi;
- incidenti;
- data scope.

Per workflow riusabili può essere utile un **Agent Registry**.

```text
agent/workflow name:
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

### Un control plane organizzativo minimo

Quando gli agenti diventano numerosi, servono capacità comuni:

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

Non ogni prototipo richiede una piattaforma enterprise.

Ma ogni sistema che influenza decisioni ricorrenti deve avere almeno una risposta a queste domande.

### Caso reale documentato — responsabilità che resta al deployer

Microsoft, nel proprio *AI agent shared responsibility model*, distingue esplicitamente i nuovi livelli introdotti dagli agenti: memory/state, tools/actions e orchestration. Tra le responsabilità che il deployer mantiene figurano dati, identity e least privilege, autorizzazione delle azioni, human oversight e acceptable-use governance.

Fonte: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

Questo formalizza un principio centrale del libro:

> usare una piattaforma gestita può trasferire parte dell'infrastruttura; **non trasferisce la responsabilità di definire ciò che il nostro agente è autorizzato a fare nel nostro contesto**.

### Campo della AI Analysis Control Sheet

Per workflow produttivi aggiungiamo:

```text
named owner:
risk tier:
autonomy level:
shared dependencies:
review capacity:
objective + guardrails:
feedback-loop risk:
skill fallback:
registry entry:
incident/runbook:
retirement trigger:
```

> **La scala dell'AI non moltiplica soltanto il lavoro prodotto. Moltiplica anche le dipendenze. Governare agenti significa rendere visibili owner, confini, obiettivi e failure correlati prima che la velocità li trasformi in infrastruttura invisibile.**
