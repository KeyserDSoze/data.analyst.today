## 14.12 Versioning e auditability: ricostruire il sistema che ha prodotto il claim

Nei workflow AI il prompt è parte della logica, ma non è l'intera logica. La stessa istruzione può produrre comportamenti diversi se cambiano modello, reasoning configuration, tool, permessi, semantic model, retrieval corpus, dati, orchestration, budget di step o evaluator. Per questo il vero oggetto da versionare è il **sistema di esecuzione**.

### Execution Manifest

Per un'analisi ad alto impatto registriamo abbastanza informazioni da poter rispondere, quando serve, a una domanda semplice:

> **Quale sistema ha prodotto questa decisione e su quale evidenza?**

Un manifest minimo può contenere:

```text
run_id:
timestamp:
trigger / user:
model + configuration:
instruction version:
context pack version:
semantic model / metric version:
data snapshot or as-of timestamp:
retrieval sources:
tools enabled:
agent identity + permission scope:
step/retry/cost budget:
queries / tool calls:
checks executed:
human interventions:
final claim:
final action / output:
```

Non significa conservare ogni token per sempre. Significa mantenere la catena minima necessaria per ricostruire il comportamento rilevante.

### Una frase può cambiare un KPI

Un team Finance usa un agente per generare la sintesi del lunedì. Per mesi l'istruzione dice: "Usa la revenue riconosciuta nel periodo, metrica certificata Finance." Dopo una semplificazione diventa: "Analizza la revenue della settimana." Il modello seleziona `invoice_amount`, che include importi emessi ma non ancora riconosciuti secondo la policy interna.

Dashboard, warehouse e pipeline di invio non cambiano. Cambia soltanto l'istruzione, e il CFO riceve un miglioramento apparente che non esiste secondo la metrica governata. Senza versioning dell'istruzione e della metrica selezionata, il failure è difficile da spiegare.

### Versionare anche il contesto recuperato

Un prompt può restare identico mentre cambia il corpus. Se una definizione churn passa da v17 a v18 o una verified answer viene aggiornata, la stessa richiesta può produrre una risposta diversa. Per workflow importanti registriamo quindi almeno document/version id, metric/version id, retrieval timestamp e gli eventuali artefatti governati recuperati.

### Reproducibility non significa stessa frase

I sistemi generativi possono essere non deterministici. L'obiettivo dell'audit non è necessariamente ottenere lo stesso identico wording, ma ricostruire lo stesso perimetro di dati, le stesse regole, la stessa versione del sistema, lo stesso livello di autorizzazione e gli stessi controlli.

Possiamo distinguere:

- **execution reproducibility**: riusciamo a ricostruire configurazione e input della run?
- **semantic reproducibility**: la stessa evidenza porta allo stesso livello di claim e alla stessa decision policy?

Per analytics la seconda è spesso più importante della ripetizione parola per parola.

### Prompt come soft code

Le istruzioni AI modificano il comportamento, possono introdurre regressioni, hanno dipendenze, richiedono review e possono essere rollbackate. Ma il comportamento può cambiare anche senza modificare il testo. Per questo il promotion flow deve essere:

```text
change
→ semantic diff
→ regression eval
→ failure-case review
→ staged rollout
→ monitoring
→ rollback if needed
```

Il diff testuale è soltanto un indizio. Il vero diff è **comportamentale**: quali eval cambiano esito, quali tool vengono chiamati diversamente, cambia il tasso di escalation, cambiano le metriche selezionate, aumentano costo o failure mode?

### Multi-agent: provenance fino alla sorgente

In una catena `planner → SQL agent → reviewer → executive writer`, non basta sapere chi ha prodotto il memo finale. Dobbiamo poter risalire:

```text
memo claim
→ evidence artifact
→ query
→ source snapshot
→ metric definition
```

Se un agente riassume o modifica un claim, il trace deve rendere visibile quel passaggio e il claim level non può aumentare senza un nuovo gate.

L'auditability resta proporzionata al rischio. Una sessione EDA personale può richiedere logging leggero; un sistema che pubblica KPI ufficiali, usa dati personali o prepara azioni ad alto impatto richiede molto di più. NIST tratta il rischio lungo il lifecycle; Microsoft include identity, authorization, human oversight e action audit logging tra i controlli da governare negli agenti.

Fonti:

- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

> **Auditability non significa conservare tutto. Significa conservare la catena minima necessaria per ricostruire perché un sistema ha avuto il diritto di produrre quel claim o quell'azione.**
