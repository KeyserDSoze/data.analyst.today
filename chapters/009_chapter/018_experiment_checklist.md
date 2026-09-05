## 9.17 Experiment Contract: congelare la logica della decisione prima dei risultati

Nel Capitolo 2 abbiamo costruito l'Analytical Brief; nel Capitolo 8 il Causal Identification Brief. Per un esperimento serve un oggetto ancora più operativo che colleghi **decisione, trattamento, popolazione, dati, inferenza e rollout** quando il risultato è ancora ignoto.

Lo chiameremo **Experiment Contract**. Il termine non indica un contratto legale: indica un accordo verificabile tra Product, Engineering, Data e business su ciò che stiamo testando e su come interpreteremo l'evidenza.

Il suo valore principale è ridurre la libertà di cambiare domanda, metrica, popolazione o regola di vittoria dopo aver visto il risultato. Per questo questa sezione resta deliberatamente strutturata: è un artefatto da compilare, non prosa da memorizzare.

### 1. Decisione, trattamento e meccanismo

```text
Decisione da supportare:
Treatment / control:
Versione, intensità, timing:
Meccanismo atteso:
Owner della decisione:
```

Il meccanismo può essere sintetizzato, per esempio:

`checkout più corto → meno abbandono durante payment → più ordini completati`

Serve a scegliere diagnostics coerenti e a distinguere un risultato che supporta la storia da un movimento inatteso che merita nuova indagine.

### 2. Popolazione e unità

```text
Eligibility:
Esclusioni pre-treatment:
Decision unit:
Randomization unit:
Exposure unit:
Analysis unit:
Identity key:
Cross-device/account policy:
Clustering:
Interference/spillover risk:
```

Questa parte deve rendere impossibile la frase “abbiamo randomizzato gli utenti” quando in realtà la feature è assegnata per cookie, la metrica è per sessione e la decisione appartiene all'account.

### 3. Metric Contract

Per ogni metrica decisionale documentiamo semantica e autorità:

| Campo | Esempio |
|---|---|
| Primary/OEC | net contribution margin per eligible user |
| Success threshold | almeno +€0,08/user |
| Guardrail | refund rate |
| Guardrail limit | non peggio di +0,20 pp |
| Maturity | 14 giorni dall'ordine |
| Decision | ship candidate solo se primary supera soglia e guardrail passa |

Aggiungiamo numeratore, denominatore, source of truth, finestre, filtri, late-data policy e ruolo di diagnostics/data-quality metrics.

### 4. Materialità, feasibility e durata

```text
Baseline:
Minimum effect of interest:
MDE planned:
Power/precision target:
Eligible traffic:
Expected exposure rate:
Randomization/clustering constraints:
Rare guardrail feasibility:
Minimum calendar duration:
Cycles da coprire:
Outcome maturity:
Variance reduction prevista:
```

Un test che non può distinguere effetti abbastanza importanti per il business non è “agile”: rischia di non separare le decisioni disponibili.

### 5. Inference plan

```text
Fixed horizon o sequential:
Analisi primaria:
Effect size + confidence interval:
Estimand (ITT o altro):
Multiple metrics/variants procedure:
Confirmatory segments:
Exploratory analyses:
Missing-data policy:
Exclusion policy:
```

L'obiettivo non è impedire esplorazione, ma distinguere **conferma** da **generazione di nuove ipotesi**.

### 6. Experiment Health Gate

```text
SRM rule:
Assignment stability:
Identity checks:
Exposure integrity:
Telemetry completeness:
Population/triggering integrity:
Metric integrity:
Interference/concurrent experiments:
Operational incidents:
Verdict: VALIDO / VALIDO CON CAVEAT / INVALIDO PER DECISIONE
```

Il gate precede effect analysis.

### 7. Decision matrix

| Primary | Guardrail | Health | Decisione |
|---|---|---|---|
| supera soglia | passa | valido | SHIP CANDIDATE |
| supera soglia | fallisce | valido | NO-SHIP / REDESIGN |
| sotto soglia | passa | valido | NO-SHIP o INCONCLUSIVE secondo CI/contract |
| qualsiasi | qualsiasi | invalido | REPAIR / RETEST |
| favorevole solo nello scope predefinito | passa | valido | SHIP WITH CONSTRAINTS |

La matrice non elimina il giudizio. Impedisce che il giudizio venga ridefinito solo perché una variante piace.

### 8. Rollout e rollback plan

```text
Exposure steps:
Minimum time per fase:
Operational metrics:
Business guardrails:
Rollback thresholds:
Partial/global rollback:
Kill-switch owner:
Mercati/segmenti esclusi:
Post-100% observation period:
```

Se non sappiamo come tornare indietro da un trattamento rischioso, questa informazione appartiene al design prima del test.

### 9. Dal contract al registro storico

Dopo la chiusura aggiungiamo:

```text
Health Gate result:
Effect estimate + uncertainty:
Guardrail outcome:
Exploratory findings:
Decision:
Actual rollout:
Incidents / rollback:
Learnings:
New hypotheses:
Links to query/notebook/metric definitions/certified dashboard:
```

In questo modo l'organizzazione evita di ricordare soltanto “B aveva vinto”, dimenticando popolazione, caveat e condizioni del risultato, e riduce il rischio di ripetere test già eseguiti perché la memoria del team è scomparsa.

### Template compatto

```text
Decision:
Treatment:
Mechanism:
Eligibility:
Randomization unit:
Exposure unit:
Analysis unit:
Identity key:
Primary/OEC:
Success threshold:
Guardrails + limits:
Diagnostics:
MDE / MEI:
Traffic / exposure / duration:
Inference plan:
Multiplicity plan:
Confirmatory segments:
Interference risks:
Health Gate rules:
Safety stop rules:
Decision matrix:
Rollout steps:
Rollback criteria:
Owners:
Final result:
Decision:
Learnings:
```

> **Il valore dell'Experiment Contract non è documentare meglio un test. È rendere verificabile, dopo i risultati, se abbiamo rispettato la decisione che avevamo progettato prima di conoscerli.**
