# Capitolo 14 — AI-assisted analytics: accelerare senza perdere rigore

Il Capitolo 0 ha fissato una regola che qui diventa operativa: **possiamo delegare l'esecuzione senza delegare la responsabilità di capire ciò che consegniamo**. Il Capitolo 13 ha aggiunto un secondo fatto: l'AI riduce drasticamente il costo di scrivere query, codice, documentazione e automazioni. Se generare diventa economico, il collo di bottiglia professionale si sposta. Non è più soltanto produrre una risposta, ma dimostrare che quella risposta merita il livello di fiducia richiesto dalla decisione.

Per questo l'unità di lavoro del capitolo non sarà il *prompt*. Sarà il **workflow controllato**:

```text
task
→ context
→ permission boundary
→ generation / execution
→ verification
→ evaluation
→ escalation
→ decision
→ audit trail
```

La sequenza conta perché gli errori più pericolosi non sono necessariamente risposte palesemente false. Un sistema può generare SQL valido usando il dataset sbagliato, scegliere una metrica reale con semantica diversa, propagare un'ipotesi non verificata per più step, formulare un causal claim a partire da un'associazione o compiere un'azione che nessuno gli aveva davvero autorizzato. In tutti questi casi l'output può apparire competente. È il **sistema di controllo** a essere insufficiente.

Un esempio rende il problema concreto. Un marketplace vede il GMV del Sud Europa a `-7,2%` settimana su settimana. Un assistente riceve la richiesta di trovare i driver per paese e categoria, genera una query corretta e identifica Electronics in Spagna come principale contributore. Il commerciale prepara una promozione da €400.000. Prima dell'approvazione, però, un analyst riconcilia il risultato con la metrica certificata e scopre che la query usa `order_created_at`, mentre la definizione economica ufficiale usa `payment_captured_at`. Proprio quella settimana un problema del payment processor aveva spostato molte capture al giorno successivo. Con la semantica corretta il delta si riduce e cambia anche la composizione geografica. La promozione non è più giustificata dall'evidenza disponibile.

L'AI non aveva "sbagliato SQL". Il workflow aveva permesso di passare da un output plausibile a una decisione prima di verificare **contesto, semantica e reconciliation**. Questa distinzione attraverserà tutto il capitolo:

> **output plausibile ≠ evidenza verificata ≠ decisione autorizzata.**

## La semantica diventa infrastruttura per l'AI

La natural-language analytics non elimina il lavoro fatto nei capitoli precedenti; lo rende ancora più importante. Microsoft avverte esplicitamente che Copilot applicato a semantic model non preparati può produrre output di bassa qualità, inaccurati o fuorvianti. Gli strumenti introdotti in Power BI — AI data schemas, AI instructions, descrizioni e verified answers — mostrano il pattern generale: se una domanda ricorrente ha un significato importante, conviene rendere quel significato parte del sistema invece di chiedere al modello di ricostruirlo ogni volta da zero.

Fonti:

- Microsoft Learn, *Use Copilot with semantic models in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- Microsoft Learn, *Prepare your data for AI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

Il NIST AI Risk Management Framework: Generative AI Profile porta lo stesso ragionamento a un livello più generale: i rischi della GenAI vanno identificati, misurati e gestiti nel contesto d'uso e lungo il lifecycle del sistema, non affidati a una generica fiducia nel modello. Il profilo NIST AI 600-1 è stato pubblicato nel 2024 e aggiornato nel 2026.

Fonte: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

La domanda matura quindi non è "possiamo fidarci dell'AI?". È:

> **Per questo task, con questo impatto, quale grado di autonomia e quale evidenza di affidabilità sono sufficienti?**

## Il deliverable: AI Analysis Control Sheet

Il deliverable del capitolo sarà la **AI Analysis Control Sheet (AACS)**. Non è un sostituto di Analytical Brief, Data Readiness Review, Causal Identification Brief, Experiment Contract, Predictive Decision Card o degli altri artefatti costruiti fin qui. Serve a collegarli quando l'AI entra nella catena.

```text
AI ANALYSIS CONTROL SHEET

Task / decision:
Risk tier:
Human owner:

Approved context / certified metrics:
Known ambiguity / must-ask conditions:

Allowed tools and data:
Read/write permissions:
Forbidden actions:

Expected artifact:
Required checks / reconciliation:
Method-specific gate:

Eval set / acceptance criteria:
Known failure modes:
Stop / escalation conditions:

Model / system version:
Instruction / context version:
Tool, query and code artifacts:
Reviewer / approver:
Final claim allowed:
Final status:
```

Più l'output può cambiare denaro, persone, compliance o processi operativi, meno questi campi possono restare impliciti.

## Il prompt cambia status

Il prompt resta utile, ma non è una formula magica. È una parte della specifica. Un prompt eccellente non compensa una fonte sbagliata, un permission boundary troppo ampio, una metrica incoerente, un test inesistente o un'assenza di escalation. Per questo non costruiremo un catalogo di "trucchi per parlare con l'AI". Costruiremo una disciplina per progettare **contesto, controlli, autonomia e responsabilità**.

Alla fine del capitolo il lettore dovrà saper trasformare una richiesta vaga in una specifica verificabile, delimitare dati e permessi, usare AI per codice, EDA, debugging e comunicazione senza perdere gli evidence gate, distinguere errori fattuali, semantici e narrativi, progettare human-in-the-loop ed eval, versionare il sistema di esecuzione e stabilire quando `STOP`, `PROVISIONAL` o `BLOCKED` sono risultati migliori di una risposta forzata.

> **L'AI rende economica la generazione. Il lavoro professionale consiste nel rendere economica anche la verifica, senza renderla superficiale.**
