# Capitolo 14 — AI-assisted analytics: accelerare senza perdere rigore

Il Capitolo 0 ha fissato una regola che qui non ripeteremo da zero:

> **l'esecuzione può essere delegata; la responsabilità di capire ciò che consegniamo no.**

Il Capitolo 13 ha aggiunto un secondo elemento: l'AI riduce il costo di costruire query, codice, automazioni e documentazione.

Questo capitolo affronta quindi la domanda successiva:

> **come progettiamo un workflow AI-assisted in cui la maggiore velocità non riduca la qualità dell'evidenza?**

Il problema non è soltanto che un modello possa “allucinare”.

Un sistema AI può produrre output perfettamente plausibili e tecnicamente validi che falliscono perché:

- hanno ricevuto contesto insufficiente;
- usano il dataset sbagliato;
- interpretano male una metrica;
- hanno permessi troppo ampi;
- propagano un errore da uno step al successivo;
- trasformano un'ipotesi in una spiegazione;
- producono una recommendation più forte dell'evidenza;
- non lasciano una traccia sufficiente per ricostruire cosa è successo.

Per questo la nuova unità di lavoro non sarà il **prompt**.

Sarà il **workflow controllato**.

## 14.0 Dalla generazione alla catena di controllo

Per un'analisi importante useremo questa sequenza:

```text
task
→ context
→ permission boundary
→ generation
→ verification
→ evaluation
→ escalation
→ decision
→ audit trail
```

Ogni passaggio risponde a una domanda diversa.

### Task

Che cosa stiamo delegando?

```text
scrivere codice
riassumere un output
proporre ipotesi
esplorare dati
eseguire query
preparare una recommendation
```

### Context

Quali fatti e definizioni può usare il sistema?

- schema;
- grain;
- metriche certificate;
- glossary;
- date;
- popolazione;
- vincoli del dominio;
- esempi verificati.

### Permission boundary

Che cosa può **fare**, non soltanto che cosa può leggere?

```text
read-only query?
creare file?
scrivere su database?
inviare messaggi?
modificare dashboard?
avviare workflow?
```

### Generation

Quale artefatto deve produrre?

### Verification

Quali controlli indipendenti devono passare prima che l'output sia trattato come evidenza?

### Evaluation

Come misuriamo nel tempo se il workflow funziona sul tipo di task reale per cui viene usato?

### Escalation

Quando il sistema deve fermarsi e chiedere intervento umano?

### Decision

Quale decisione può supportare l'output e quale invece rimane fuori scope?

### Audit trail

Possiamo ricostruire input, contesto, versione, tool call, output, verifiche e approvazione?

Questa catena è il vero oggetto del capitolo.

## Caso simulato/composito — SQL perfetto, campagna sbagliata

Un marketplace vede GMV del Sud Europa a -7,2% settimana su settimana.

Un assistente riceve:

> “Trova i driver del calo per paese e categoria.”

Genera rapidamente una query complessa e identifica Electronics in Spagna come principale contributore.

Il commerciale prepara una promozione da €400.000.

Prima dell'approvazione un analyst esegue la reconciliation con il KPI certificato e scopre che la query usa `order_created_at`, mentre la metrica ufficiale usa `payment_captured_at`.

Durante quella settimana un problema del payment processor aveva spostato molte capture al giorno successivo.

Con la semantica corretta:

- il delta è molto più piccolo;
- la composizione geografica cambia;
- la promozione non è più giustificata dall'evidenza disponibile.

L'errore non era:

```text
AI non sa scrivere SQL
```

Era:

```text
context insufficiente
+ nessuna reconciliation obbligatoria
+ decisione preparata prima del verification gate
```

Questa distinzione sarà ricorrente:

**output plausibile ≠ evidenza verificata ≠ decisione autorizzata**.

## Perché la semantica diventa infrastruttura per l'AI

La natural-language analytics non elimina la necessità di modelli semantici ben preparati.

Microsoft oggi avverte esplicitamente che usare Copilot con semantic model non preparati può produrre output di bassa qualità, inaccurati o fuorvianti.[^ms-semantic]

Per questo Power BI ha introdotto strumenti come:

- AI data schemas;
- AI instructions;
- descrizioni;
- **verified answers**.

Le verified answers permettono agli autori del modello di associare domande importanti a risposte curate e validate, così che alcuni intenti non dipendano ogni volta da una nuova generazione.[^ms-verified]

La lezione generale è più importante del prodotto:

> **per alcune domande ricorrenti ad alto valore, è meglio recuperare una risposta governata che rigenerare ogni volta il significato da zero.**

## NIST: generative AI come problema di risk management e evaluation

Il NIST AI RMF Generative AI Profile è costruito proprio sull'idea che i rischi della GenAI debbano essere identificati, misurati e gestiti lungo design, sviluppo, uso ed evaluation, in modo proporzionato al contesto.[^nist-genai]

Questo ci impedisce due estremi.

**Estremo 1**

> Non fidarti mai dell'AI.

È troppo generico per essere operativo.

**Estremo 2**

> Se il modello è bravo, possiamo automatizzare.

È altrettanto generico.

La domanda matura è:

> **per questo task, con questo impatto, quale grado di autonomia e quale evidenza di affidabilità sono sufficienti?**

## AI Analysis Control Sheet

Il deliverable canonico del capitolo sarà la **AI Analysis Control Sheet (AACS)**.

Una versione compatta può essere:

```text
AI ANALYSIS CONTROL SHEET

Task:
Decision supported:
Risk tier:
Human owner:

Allowed context:
Certified data / metrics:
Known ambiguity:

Allowed tools:
Read permissions:
Write/action permissions:
Forbidden actions:

Expected output:
Required evidence:
Required checks:
Independent reconciliation:

Eval set / acceptance criteria:
Known failure modes:
Escalation / stop conditions:

Model / system version:
Prompt/instructions version:
Tool/query/code artifacts:
Reviewer / approver:
Final claim allowed:
```

Non ogni richiesta richiede questa forma completa.

Ma più un output AI può cambiare una decisione reale, più questi campi dovrebbero smettere di essere impliciti.

## Il ruolo del prompt

Il prompt resta importante, ma cambia status.

Non è una formula magica.

È una parte della specifica del workflow.

Un prompt eccellente non compensa:

- una fonte sbagliata;
- permessi eccessivi;
- assenza di test;
- metriche incoerenti;
- evaluation inesistente;
- escalation non definita.

Per questo il capitolo non insegnerà “trucchi per parlare con l'AI”.

Insegnerà a progettare **contesto, controlli e responsabilità**.

## Obiettivo del capitolo

Alla fine il lettore dovrebbe saper:

- trasformare un task ambiguo in una specifica verificabile;
- delimitare contesto e permessi;
- usare AI per codice, EDA, debugging e comunicazione mantenendo evidence gates;
- distinguere confabulation, semantic error e narrative overreach;
- progettare human-in-the-loop e agentic workflow;
- costruire eval basate sui task reali;
- gestire privacy e dati sensibili;
- versionare istruzioni, artefatti ed execution trace;
- definire stop/escalation conditions;
- stabilire quale claim l'evidenza consente davvero.

> **L'AI rende economica la generazione. Il lavoro professionale consiste nel rendere economica anche la verifica senza renderla superficiale.**

[^ms-semantic]: Microsoft Learn, *Use Copilot with semantic models in Power BI*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^ms-verified]: Microsoft Learn, *Prepare your data for AI - Verified answers*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-verified-answers
[^nist-genai]: NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
