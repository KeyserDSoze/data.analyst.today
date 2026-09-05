## 14.1 Dal prompt alla specifica: rendere esplicito ciò che il modello non deve indovinare

Nel lavoro analitico la qualità di una richiesta AI dipende meno dall'eleganza della frase e più dalla qualità della **specifica**. "Analizza le vendite" delega al modello troppe decisioni invisibili: quale revenue, quale periodo, quale perimetro, quale data economica, quale popolazione, quale baseline, quale livello di claim. Una richiesta professionale riduce proprio questo spazio di improvvisazione.

Confrontiamo:

> Analizza le vendite.

con:

> Confronta il net revenue delle ultime 8 settimane con le 8 precedenti, a perimetro negozi comparabile. Usa `payment_captured_at` come data economica, escludi ordini cancellati e refund completi, separa volume/prezzo/mix e segnala segmenti con contributo assoluto > €50k. Prima di interpretare verifica freshness e reconciliation con la misura certificata. Non formulare causal claim.

La seconda richiesta non è migliore perché è più lunga. È migliore perché esplicita decisioni che cambiano il significato del risultato.

### Il prompt come work order sopra contratti già esistenti

Non dobbiamo riscrivere nel prompt tutto ciò che abbiamo costruito nei capitoli precedenti. Se esistono Analytical Brief, Data Readiness Review, metric definitions, Analytical Data Contract o Data Flow Architecture Map, il sistema dovrebbe ricevere o recuperare la parte rilevante di quei contratti. Il prompt diventa una **work order** sopra contesto governato:

```text
Task
+ certified context
+ allowed assumptions
+ constraints
+ required evidence
+ output contract
```

Microsoft segue oggi una logica analoga in Power BI: AI data schemas, AI instructions, descrizioni e verified answers servono a trasferire nel semantic model terminologia, business context e risposte validate invece di lasciare tutto alla formulazione della domanda.

Fonti:

- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-instructions

### Context Pack

Per un task non banale usiamo un **Context Pack**. Non deve essere necessariamente compilato a mano: può essere costruito da metadata, semantic layer, catalogo e documentazione versionata.

```text
Decision:
Question:
Population / grain:
Metric definitions:
Time semantics:
Certified sources:
Known data limitations:
Allowed method:
Forbidden inference:
Expected output:
Required checks:
```

Prendiamo un SaaS con logo churn passato da `3,8%` a `4,6%`. Chiedere "perché il churn è aumentato?" invita il sistema a produrre spiegazioni plausibili — pricing, onboarding, supporto, competitor — prima che esista evidenza. Un Context Pack più maturo dichiara invece che la decisione è capire dove investire capacità di retention investigation, definisce numeratore e base del logo churn, impone il confronto Q2 vs Q1, richiede slice per cohort, plan, country, tenure e activation status, obbliga a verificare prima eventuali cambi di tracking/definizione e specifica che `association ≠ cause`. L'output deve separare contribution-to-delta, fatti osservati, ipotesi e next evidence.

Il sistema non riceve soltanto una domanda. Riceve **i confini epistemici del lavoro**.

### Known, Unknown, Must Ask

Una delle capacità più importanti di un workflow maturo è non trasformare l'ambiguità in una scelta arbitraria. Per questo classifichiamo ciò che il sistema incontra:

- **Known**: informazione presente nel contesto autorizzato;
- **Unknown**: informazione assente ma non bloccante;
- **Must Ask / Must Escalate**: ambiguità che cambia materialmente risultato o rischio.

Se la richiesta è "calcola ARPU per mercato" e il contesto contiene `gross_revenue`, `net_revenue` e tre definizioni di active user, scegliere la combinazione più plausibile è un errore. L'output corretto è segnalare che ARPU non è univoco e chiedere definizione di revenue e denominator policy.

> **Chiedere chiarimento può essere un risultato corretto.**

Questa regola diventa ancora più importante nei workflow agentici: un'assunzione implicita presa allo step 1 può propagarsi per dieci step e diventare sempre più difficile da vedere.

### Assumption budget

Non tutte le inferenze hanno lo stesso rischio. Possiamo quindi dichiarare un **assumption budget**:

```text
May infer:
- formato della tabella finale
- naming di alias temporanei

Must not infer:
- KPI definition
- population exclusions
- causal mechanism
- write target
- privacy classification
```

L'obiettivo non è eliminare ogni inferenza, ma separare convenzioni innocue da assunzioni che cambiano semantica, rischio o autorizzazione.

### Piano prima dell'esecuzione

Quando il costo di un errore è alto, conviene separare pianificazione ed esecuzione:

```text
plan
→ review
→ execute
→ verify
→ interpret
```

Possiamo chiedere prima: "Proponi il piano di investigazione. Non eseguire query e non formulare conclusioni." Dopo la review umana autorizziamo solo gli step necessari e aggiungiamo stop condition, per esempio: se una cardinalità non corrisponde alle attese, fermati. Questo crea un **commit point** prima che il sistema consumi risorse o propaghi una specifica sbagliata.

### L'output contract deve preservare i livelli di evidenza

Un testo fluente tende a trasformare osservazioni, ipotesi e raccomandazioni in una storia unica. Per evitarlo, l'output deve tenere separati i livelli:

| Livello | Esempio |
|---|---|
| Osservazione | mobile conversion `4,2% → 3,5%` |
| Localizzazione | 74% del delta è su Android 14 |
| Ipotesi | possibile problema nel payment flow |
| Evidenza mancante | error code / release telemetry |
| Causal claim | non consentito con i dati correnti |
| Recommendation | investigare build X prima di modificare pricing |

Il Context Pack entra quindi nella AI Analysis Control Sheet con versione, fonti certificate, ambiguità note, assumption budget, must-ask conditions e controlli richiesti prima dell'interpretazione.

> **Un buon prompt non rende intelligente una richiesta vaga. Una buona specifica rende visibili le decisioni che non vogliamo lasciare all'improvvisazione del modello.**
