## 14.6 Agentic workflows e human-in-the-loop: dal prompt al sistema che può agire

Quando un assistente AI passa dalla singola risposta a una sequenza di azioni, il problema cambia natura.

Non stiamo più valutando soltanto un testo generato. Stiamo progettando un **sistema che osserva, decide quali strumenti usare, produce stati intermedi e può creare side effect**.

Un agente analitico può, per esempio:

1. ricevere una richiesta;
2. scegliere metriche e dataset;
3. eseguire SQL;
4. confrontare il risultato con una baseline;
5. aprire una seconda indagine se trova un'anomalia;
6. produrre una raccomandazione;
7. inviare una notifica;
8. in alcuni casi attivare un'azione operativa.

Questa capacità è potente perché comprime molto lavoro di coordinamento.

È pericolosa per la stessa ragione: **un errore iniziale può diventare un'azione prima che una persona lo veda**.

### Dal workflow al contratto di esecuzione

Prima di dare autonomia a un agente, definiamo un **Agent Execution Contract**.

```text
goal:
allowed data:
allowed tools:
agent identity:
read/write permissions:
data-readiness gate:
max steps / retries:
max cost / runtime:
required checks:
human checkpoints:
side effects allowed:
stop conditions:
escalation owner:
rollback path:
audit log:
```

Il contratto serve a trasformare “l'agente può fare questa analisi” in una specifica verificabile di **cosa può osservare, cosa può fare e quando deve fermarsi**.

### Caso simulato/composito — la campagna che sembrava da spegnere

Un e-commerce costruisce un workflow che ogni mattina:

- legge ROAS per campagna;
- identifica quelle sotto 1,5;
- prepara una raccomandazione di pausa;
- chiede approvazione al marketing manager.

Un lunedì l'agente segnala una campagna con ROAS 1,18.

La query è corretta, ma il feed revenue è D+1 mentre la spesa advertising è quasi real time. Gran parte delle conversioni della domenica non è ancora arrivata.

Il giorno successivo il ROAS riconciliato è 2,34.

Il controllo sbagliato sarebbe stato:

```text
ROAS < 1,5 → pausa
```

Il controllo corretto è più simile a:

```text
metric certified?
AND spend fresh?
AND revenue complete enough?
AND observation window mature?
AND discrepancy within reconciliation tolerance?
THEN evaluate ROAS threshold
ELSE STOP / DEGRADE / ESCALATE
```

La differenza è fondamentale: **prima di applicare una business rule, l'agente deve dimostrare che l'evidenza è pronta per quella decisione**.

### Caso reale documentato — gli agenti introducono nuovi trust boundary

Nel 2026 Microsoft ha pubblicato un modello di responsabilità condivisa specifico per AI agent. La documentazione distingue gli agenti dai normali workload generativi perché possono:

- agire autonomamente tramite tool e API;
- mantenere stato e memoria;
- avere un'identità e privilegi propri;
- comporsi con altri agenti;
- produrre side effect senza approvazione a ogni singolo passaggio.

Microsoft indica tra i controlli da governare:

- least privilege per tool;
- identità e token delegati;
- autorizzazione per azione;
- human approval per azioni ad alto impatto;
- limiti su loop, step e costo;
- trust boundary tra agenti;
- audit logging delle azioni.

Fonte: Microsoft Learn, *AI agent shared responsibility model*: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

La lezione per l'analytics è semplice:

> **quando un modello ottiene strumenti, l'unità di rischio non è più la risposta: è la traiettoria di esecuzione.**

### Caso reale documentato — quando anche l'ambiente di eval è parte del rischio

OpenAI ha documentato nel 2026 due incidenti emersi durante valutazioni cyber condotte da partner esterni: in configurazioni di test personalizzate, la combinazione tra capacità del modello e controlli dell'ambiente ha permesso attività oltre i confini previsti della valutazione.

Fonte: OpenAI, *Third-party cyber evaluations involving OpenAI models*: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

Il punto utile per un Data Analyst non riguarda il cyber task in sé. Riguarda la progettazione del sistema:

- un modello non esiste separato dal suo harness;
- tool, credenziali, rete, memoria e limiti cambiano ciò che il sistema può realmente fare;
- testare il modello senza testare il percorso operativo può dare una falsa sensazione di controllo.

### Quattro livelli di autonomia

Non serve una distinzione binaria tra “manuale” e “autonomo”.

Possiamo usare livelli progressivi.

| Livello | Comportamento | Esempio analitico |
|---|---|---|
| A0 — Suggest | propone, non esegue | suggerisce una query |
| A1 — Execute read-only | esegue azioni reversibili e senza side effect | interroga viste autorizzate |
| A2 — Prepare action | prepara un cambiamento, umano approva | propone modifica budget o rollback |
| A3 — Bounded action | agisce entro policy rigide e osservabili | aggiorna una tabella non critica entro soglie predefinite |

L'autonomia non dovrebbe crescere perché “il modello sembra bravo”.

Dovrebbe crescere quando abbiamo evidenza che:

- il task è abbastanza stabile;
- i failure mode sono conosciuti;
- gli eval coprono casi rilevanti;
- i side effect sono limitati;
- rollback e monitoring funzionano;
- il beneficio dell'autonomia supera il rischio aggiunto.

### Human-in-the-loop non significa mettere una persona ovunque

Una review umana inefficace può diventare un timbro automatico.

Un buon checkpoint deve dire **cosa deve verificare la persona**.

#### Approval before action

L'agente prepara una decisione, ma una persona approva dopo aver visto:

- evidenza;
- controlli superati;
- caveat;
- impatto stimato;
- rollback.

Adatto a variazioni di budget, KPI executive o azioni su clienti di alto valore.

#### Approval on exception

Il sistema procede sui casi normali e si ferma quando una regola di qualità o rischio fallisce.

Esempio:

```text
refresh normale → automatico
reconciliation delta > 1% → escalation
freshness oltre SLA → output PROVISIONAL, nessuna azione
schema inatteso → BLOCK
```

#### Audit after action

Possibile solo per attività a basso impatto, molto reversibili e completamente tracciate.

La review successiva deve campionare anche i casi apparentemente riusciti, non solo gli errori evidenti.

### Reversibilità e blast radius

Due dimensioni aiutano a scegliere l'autonomia:

**reversibilità** — quanto è facile annullare l'azione;

**blast radius** — quante persone, euro, record o processi può coinvolgere un errore.

Una bozza di query ha alta reversibilità e blast radius quasi nullo.

Un agente che modifica prezzi per 400.000 SKU ha una superficie completamente diversa.

Più aumenta il blast radius, meno è accettabile affidarsi a un solo controllo generativo.

### Un agente deve poter dire STOP

Un comportamento maturo può essere:

> “Non posso formulare una raccomandazione affidabile: `payments` è incompleta dalle 03:00 alle 06:20 e il KPI non ha superato il data-readiness gate.”

Questo output è spesso più utile di una conclusione forzata.

Le stop condition possono includere:

- freshness fuori SLA;
- reconciliation fallita;
- schema inatteso;
- conflitto tra metriche certificate;
- assunzioni critiche non risolte;
- massimo numero di iterazioni;
- budget di costo superato;
- richiesta fuori autorizzazione;
- evidenza insufficiente per il claim richiesto.

### Multi-agent: ogni passaggio è un nuovo confine di fiducia

Se un SQL agent produce un dataset che un causal agent interpreta e un executive agent riassume, non possiamo considerare l'ultima risposta una verifica delle precedenti.

La catena è:

```text
source
→ SQL agent
→ evidence artifact
→ diagnostic/causal agent
→ claim
→ communication agent
→ decision maker
```

Ogni freccia deve avere:

- formato atteso;
- provenance;
- criteri di accettazione;
- possibilità di rifiuto;
- owner.

Un agente downstream non dovrebbe trasformare automaticamente un output upstream non verificato in una conclusione più sicura.

### Campo della AI Analysis Control Sheet

Per workflow agentici registriamo almeno:

```text
autonomy level:
agent identity:
tools/data allowed:
read/write scope:
data-readiness gate:
step/retry/cost budget:
required deterministic checks:
human approval point:
stop/escalation condition:
rollback:
action log:
```

> **Un agente utile non è quello che fa più cose da solo. È quello che sa operare entro un perimetro verificabile, fermarsi quando l'evidenza non basta e lasciare una traccia difendibile di ciò che ha fatto.**
