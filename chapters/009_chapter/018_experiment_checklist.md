## 9.17 Experiment Contract: rendere verificabile la decisione prima di vedere i risultati

Nel Capitolo 2 abbiamo introdotto l'Analytical Brief. Nel Capitolo 8 abbiamo costruito il Causal Identification Brief. Per un esperimento serve un oggetto ancora più operativo: un documento che colleghi **decisione, design, dati, inferenza e rollout** prima che il risultato sia noto.

Lo chiameremo **Experiment Contract**.

Il nome "contract" è intenzionale. Non è un contratto legale: è un accordo verificabile tra Product, Engineering, Data e business su che cosa stiamo testando e su come interpreteremo ciò che accadrà.

Il suo scopo principale è ridurre la libertà di riscrivere la storia dopo aver visto i dati.

### 1. Decisione e ipotesi

**Decisione da supportare**  
Che cosa faremo diversamente se l'evidenza è favorevole, neutra o negativa?

**Treatment**  
Che cosa cambia esattamente rispetto al controllo? Versione, intensità, timing e condizioni devono essere descritti abbastanza bene da permettere a un'altra persona di ricostruire l'intervento.

**Meccanismo atteso**  
Perché il trattamento dovrebbe modificare l'outcome?

Esempio:

`checkout più corto → meno abbandono durante payment → più ordini completati`

Questa catena aiuta anche a scegliere diagnostic metrics sensate.

### 2. Popolazione e unità

Documentare:

- popolazione eleggibile;
- esclusioni definite prima del trattamento;
- unità di randomizzazione;
- unità di exposure;
- unità di analisi;
- identity key;
- regole per utenti multi-device o account condivisi;
- clustering;
- rischio di spillover/interferenza.

Questa sezione deve rendere impossibile la frase vaga:

> "abbiamo randomizzato gli utenti"

quando in realtà la feature è assegnata per cookie, la metrica è per sessione e l'outcome economico appartiene all'account.

### 3. Metric Contract

Per ogni metrica decisionale servono almeno:

- nome e ruolo: primary/OEC, guardrail, secondary/diagnostic;
- definizione semantica;
- numeratore e denominatore;
- unità;
- finestra temporale;
- maturazione necessaria;
- source of truth;
- eventuali filtri;
- direzione desiderata;
- soglia che cambia la decisione.

Esempio:

| Campo | Definizione |
|---|---|
| Primary | net contribution margin per eligible user |
| Success threshold | almeno +€0,08/user |
| Guardrail | refund rate |
| Guardrail limit | non peggio di +0,20 pp |
| Maturity | 14 giorni dall'ordine |
| Decision | ship candidate solo se primary supera soglia e guardrail passa |

La soglia evita di trasformare "statisticamente diverso" in sinonimo di "utile".

### 4. Feasibility e sensibilità

Prima del lancio dichiarare:

- baseline;
- Minimum Detectable Effect business-relevant;
- potenza/precisione target, rimandando alla teoria del Capitolo 5;
- traffico eleggibile atteso;
- exposure rate atteso;
- durata minima;
- cicli temporali da coprire;
- metriche rare che potrebbero richiedere più tempo;
- eventuale variance reduction prevista, come CUPED.

Un test che non può distinguere effetti abbastanza importanti per il business non è "veloce". È un test che rischia di non rispondere alla domanda.

### 5. Inference plan

Definire prima:

- fixed horizon o sequential design;
- analisi primaria;
- confidence interval/effect size da riportare;
- trattamento delle multiple metriche/varianti;
- segmenti confermativi predefiniti;
- analisi che saranno considerate esplorative;
- regole per missing data ed esclusioni;
- eventuale estimand ITT o altro estimand esplicitamente motivato.

Questa parte non serve a impedire l'esplorazione. Serve a distinguere **conferma** da **generazione di nuove ipotesi**.

### 6. Health Gate

Il contract deve dichiarare quali controlli possono invalidare il test o limitarne lo scope:

- SRM;
- assignment stability;
- exposure integrity;
- logging completeness;
- population/triggering integrity;
- metric integrity;
- interference/concurrent experiments;
- incidenti operativi.

Il verdetto del gate sarà:

**VALIDO / VALIDO CON CAVEAT / INVALIDO PER DECISIONE**.

### 7. Decision matrix

La decisione dovrebbe poter essere ricostruita senza riaprire una negoziazione da zero dopo ogni test.

Esempio:

| Primary | Guardrail | Health | Decisione |
|---|---|---|---|
| supera soglia | passa | valido | SHIP CANDIDATE |
| supera soglia | fallisce | valido | NO-SHIP / REDESIGN |
| sotto soglia | passa | valido | NO-SHIP o inconclusive secondo CI |
| qualsiasi | qualsiasi | invalido | REPAIR/RETEST |
| favorevole solo su segmento predefinito | passa | valido | SHIP WITH CONSTRAINTS |

La decision matrix non elimina il giudizio. Evita però che il giudizio cambi soltanto perché il risultato piace.

### 8. Rollout e rollback plan

Prima del test, non dopo la vittoria, dovrebbero essere almeno abbozzati:

- exposure steps;
- durata minima per fase;
- metriche operative di monitoraggio;
- soglie di rollback;
- partial/global rollback;
- owner del kill switch;
- segmenti o mercati esclusi dal rollout iniziale;
- periodo di osservazione post-100%.

Se non sappiamo come tornare indietro da un trattamento rischioso, questa è informazione rilevante già quando decidiamo quanto traffico esporre nell'esperimento.

### 9. Registro finale dell'esperimento

Dopo la chiusura il contract diventa un record storico. Si aggiungono:

- risultato del Health Gate;
- effect size e intervalli;
- comportamento delle guardrail;
- analisi esplorative chiaramente marcate;
- decisione;
- rollout effettivo;
- incidenti e rollback;
- learnings;
- nuove ipotesi generate;
- link a query, notebook, metric definitions e dashboard certificata.

Questo evita due sprechi frequenti:

1. ripetere un esperimento perché nessuno sa che era già stato fatto;
2. ricordare soltanto "B aveva vinto" dimenticando popolazione, caveat e condizioni del risultato.

### Template compatto

Un Experiment Contract può essere sintetizzato così:

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
MDE:
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

La forma può cambiare. La disciplina no.

> **Il valore dell'Experiment Contract non è documentare meglio un test. È rendere più difficile cambiare domanda, metrica, popolazione o regola di vittoria dopo aver visto il risultato.**
