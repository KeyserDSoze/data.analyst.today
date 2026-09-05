## 14.6 Agentic workflows e human-in-the-loop: governare la traiettoria, non soltanto la risposta

Quando un sistema AI passa dalla singola risposta a una sequenza di azioni, il rischio cambia natura. Non valutiamo più soltanto testo generato: progettiamo un **sistema che osserva, sceglie strumenti, mantiene stato, produce artefatti intermedi e può creare side effect**.

Un agente analitico può ricevere una richiesta, scegliere metriche e dataset, eseguire SQL, aprire una seconda indagine se trova un'anomalia, produrre una raccomandazione e perfino preparare o compiere un'azione. La capacità comprime molto lavoro di coordinamento; proprio per questo un errore iniziale può raggiungere il mondo reale prima che una persona lo veda.

### Agent Execution Contract

Prima di concedere autonomia definiamo un **Agent Execution Contract**:

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

Il contratto traduce "l'agente può fare questa analisi" in una specifica verificabile di ciò che può osservare, fare e quando deve fermarsi.

### Prima la readiness, poi la business rule

Un e-commerce costruisce un workflow che ogni mattina legge il ROAS, segnala campagne sotto `1,5` e prepara una raccomandazione di pausa. Un lunedì trova ROAS `1,18`. La query è corretta, ma la spesa advertising è quasi real time mentre il feed revenue è D+1. Il giorno successivo il ROAS riconciliato è `2,34`.

La policy sbagliata sarebbe:

```text
ROAS < 1,5 → pausa
```

Quella corretta deve verificare prima maturità e coerenza dell'evidenza:

```text
metric certified?
AND spend fresh?
AND revenue complete enough?
AND observation window mature?
AND reconciliation within tolerance?
THEN evaluate ROAS threshold
ELSE STOP / DEGRADE / ESCALATE
```

Un agente deve dimostrare che il dato è pronto **prima** di applicare la regola che trasforma il dato in azione.

### Gli agenti introducono nuovi trust boundary

Microsoft ha formalizzato nel 2026 un *AI agent shared responsibility model* che distingue agent identity, delegated tokens, per-action authorization, human approval, loop/step/cost limits, trust boundary tra agenti e action audit logging. La documentazione ribadisce che, indipendentemente dal modello di deployment, il deployer mantiene responsabilità su dati, identity/least privilege, autorizzazione delle azioni e human oversight.

Fonte: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

OpenAI ha inoltre documentato nell'agosto 2026 due incidenti emersi durante valutazioni cyber di terze parti in cui configurazione del test e controlli dell'ambiente, combinati con capacità del modello, hanno consentito attività oltre i confini previsti. Il punto che ci interessa non è il dominio cyber, ma il principio sistemico: **model + harness + tool + credenziali + rete + limiti** determinano ciò che un agente può realmente fare.

Fonte: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

### Autonomia come scala, non interruttore

| Livello | Comportamento | Esempio analitico |
|---|---|---|
| A0 — Suggest | propone, non esegue | suggerisce una query |
| A1 — Execute read-only | esegue azioni reversibili senza side effect | interroga viste autorizzate |
| A2 — Prepare action | prepara un cambiamento, umano approva | propone budget change o rollback |
| A3 — Bounded action | agisce entro policy rigide e osservabili | aggiorna un asset non critico entro soglie definite |

L'autonomia non cresce perché "il modello sembra bravo". Cresce quando task e failure mode sono abbastanza stabili, gli eval coprono casi rilevanti, i side effect sono limitati, rollback e monitoring funzionano e il beneficio supera il rischio aggiunto.

### Human-in-the-loop deve essere un controllo reale

Mettere una persona in ogni passaggio non crea automaticamente sicurezza. Un checkpoint efficace dichiara **che cosa il reviewer deve verificare**. Possiamo avere approval before action per budget, prezzi o clienti ad alto valore; approval on exception quando il sistema procede sui casi normali ma si ferma su reconciliation, freshness o schema failure; audit after action soltanto per attività a basso impatto, reversibili e completamente tracciate.

Due concetti aiutano a decidere: **reversibilità** e **blast radius**. Una query proposta è altamente reversibile e quasi priva di blast radius; una modifica prezzi su 400.000 SKU richiede un livello di controllo completamente diverso.

### Un agente maturo deve saper dire STOP

L'output professionale può essere:

> Non posso formulare una raccomandazione affidabile: `payments` è incompleta dalle 03:00 alle 06:20 e il KPI non ha superato il data-readiness gate.

Le stop condition possono includere freshness fuori SLO, reconciliation fallita, schema inatteso, ambiguità critica, budget di step/costo esaurito, richiesta fuori autorizzazione o evidenza insufficiente per il claim.

### Multi-agent non significa multi-evidence

In una catena `SQL agent → causal/diagnostic agent → executive writer`, ogni passaggio è un nuovo trust boundary. L'artefatto deve portare con sé provenance, status, claim level, criteri di accettazione e possibilità di rifiuto. Un agente downstream non può trasformare automaticamente un output upstream `PROVISIONAL` o `L2` in una conclusione `APPROVED` o causale.

La Control Sheet registra autonomy level, agent identity, data/tool scope, readiness gate, budget di step/retry/costo, deterministic checks, approval point, stop/escalation condition, rollback e action log.

> **Un agente utile non è quello che fa più cose da solo. È quello che opera entro un perimetro verificabile, sa fermarsi quando l'evidenza non basta e lascia una traccia difendibile di ciò che ha fatto.**
