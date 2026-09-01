## 15.10 Decision quality, execution quality e outcome quality: tre cose diverse

Uno degli errori più costosi nell'apprendimento organizzativo è giudicare una decisione soltanto dal risultato finale.

Se il risultato è buono:

> “Avevamo ragione.”

Se il risultato è cattivo:

> “La decisione era sbagliata.”

Ma in un mondo incerto questa equivalenza non regge.

Dobbiamo distinguere almeno tre oggetti.

### 1. Decision quality

La scelta era ragionevole **date le informazioni disponibili al momento**?

Guardiamo:

- obiettivo;
- alternative;
- evidenza;
- assunzioni;
- uncertainty;
- trade-off;
- downside;
- switching thresholds;
- reversibilità;
- criteri di review.

### 2. Execution quality

Abbiamo implementato davvero la decisione prevista?

Esempi:

- rollout corretto?
- target population corretta?
- budget allocato come deciso?
- training completato?
- guardrail osservati?
- sistema tecnico funzionante?

Una buona decisione può fallire perché l'esecuzione è diversa dal piano.

### 3. Outcome quality

Che cosa è successo nel mondo?

Questo include:

- effetto della decisione;
- casualità/variabilità;
- shock esterni;
- comportamento di competitor;
- cambi macro;
- eventi non previsti.

L'outcome è reale.

Non è però una misura pura della qualità della decisione.

### La matrice 2×2

| Decision process | Outcome | Lettura |
|---|---|---|
| forte | buono | scelta plausibilmente buona + esito favorevole |
| forte | cattivo | possibile bad luck, execution issue o rischio già contemplato |
| debole | buono | fortuna / outcome positivo non valida il processo |
| debole | cattivo | risultato negativo e processo da correggere |

La casella più pericolosa culturalmente è:

> **processo debole + outcome buono**

perché tende a essere premiata e replicata.

### Caso simulato/composito — la campagna “che ha funzionato”

Un e-commerce investe €600k in una campagna.

La decisione nasce da un'analisi osservazionale:

```text
clienti esposti acquistano +35%
```

Non vengono considerati:

- selection bias;
- business as usual;
- holdout;
- incrementalità;
- alternative.

Dopo il lancio il sistema di attribuzione riporta €900k di revenue.

Outcome superficiale:

> “successo.”

Tre mesi dopo un test controllato su una campagna simile mostra che gran parte di quella revenue sarebbe avvenuta comunque.

Il primo progetto può perfino aver avuto un risultato netto positivo.

Ma il **processo decisionale** era fragile: confondeva attribuzione e incrementalità.

Se premiamo soltanto l'outcome, insegniamo all'organizzazione a ripetere la fragilità.

### Una buona decisione può produrre un esito negativo

Supponiamo due alternative:

```text
A:
80% → +€1M
20% → -€200k

B:
100% → +€100k
```

Se:

- l'organizzazione può assorbire il downside;
- le probabilità hanno una base ragionevole;
- A è coerente con gli obiettivi;

scegliere A può essere una buona decisione.

Se poi si realizza il 20% negativo, abbiamo osservato un outcome previsto come possibile.

Non possiamo dire automaticamente:

> “Avremmo dovuto scegliere B.”

Quello sarebbe hindsight bias.

### Ex ante evaluation: congelare il punto di vista

Per valutare decision quality dobbiamo tornare al **timestamp epistemico** del Decision Record.

Domande:

- cosa sapevamo allora?
- quale range avevamo dichiarato?
- quali alternative erano realmente disponibili?
- quali rischi avevamo previsto?
- quale informazione non era realisticamente ottenibile?
- quale switching condition avevamo fissato?

Non possiamo usare informazioni emerse dopo per fingere che fossero ovvie prima.

### Ma “non potevamo saperlo” non deve diventare una scusa universale

Dobbiamo distinguere:

**Unknowable / genuinely unforeseeable**

da

**Not investigated / ignored / inconvenient**.

Esempio:

> “Non potevamo prevedere che il cliente non avrebbe accettato il nuovo prezzo.”

Forse.

Ma se:

- non abbiamo segmentato renewal risk;
- ignorato survey esistenti;
- saltato un pilot;
- non definito churn guardrail;

allora una parte dell'incertezza era gestibile.

### NASA: decisione data lo stato di conoscenza

NASA definisce la decision analysis come un framework per caratterizzare alternative rispetto alle priorità del decision-maker **dato lo stato di conoscenza disponibile**, documentando assunzioni, limitazioni, incertezza e robustezza.

Fonte: https://www.nasa.gov/reference/6-8-decision-analysis/

Questo rende esplicito il criterio corretto:

> la qualità del processo si valuta rispetto all'informazione e all'incertezza che esistevano al momento della scelta.

### Outcome review: attribuzione prima del giudizio

Anche quando il risultato è cattivo, chiediamo:

```text
1. decision process issue?
2. execution issue?
3. external/context shock?
4. expected downside realized?
5. measurement issue?
```

Esempio:

un A/B test supporta rollout.

Poi revenue totale scende.

Non significa che il trattamento abbia fallito.

Potrebbe esserci:

- stagionalità;
- competitor shock;
- traffico totale in calo;
- implementazione diversa dall'esperimento;
- outcome aggregato che nasconde uplift relativo.

Serve ricostruire il nesso tra decisione e outcome.

### Forecast calibration dell'organizzazione

Nel tempo possiamo misurare la qualità delle nostre aspettative.

Per Decision Record comparabili registriamo:

```text
expected range
actual outcome
which scenario occurred
which assumption missed
```

Dopo molti casi possiamo chiedere:

- i nostri range contengono abbastanza spesso gli esiti?
- siamo sistematicamente ottimisti sui tempi?
- sottostimiamo downside commerciali?
- quali team hanno forecast meglio calibrati?

La decision quality diventa una capacità misurabile nel tempo.

### Non premiare la certezza retrospettiva

Una cultura sana non premia chi dice:

> “Lo sapevo.”

senza evidenza che quella previsione fosse stata registrata prima.

Il Decision Record rende più facile distinguere:

- forecast reale;
- caveat reale;
- opinione ex post.

### Decision review scorecard

Dopo l'esito possiamo valutare separatamente:

| Dimensione | Valutazione |
|---|---|
| framing / objective | |
| alternatives quality | |
| evidence quality | |
| uncertainty representation | |
| downside / guardrails | |
| switching logic | |
| reversibility design | |
| execution fidelity | |
| outcome | |
| learning captured | |

Non comprimiamo necessariamente tutto in un voto unico.

La tabella serve a capire **dove migliorare**.

### Regola operativa

Quando un outcome sorprende:

1. recupera il Decision Record originale;
2. non aggiornare retroattivamente le assunzioni;
3. separa processo, execution e outcome;
4. identifica ciò che era prevedibile allora;
5. aggiorna prior, range, processi e guardrail per decisioni future;
6. non confondere bad luck con bad process né good luck con good process.

> **Una decisione di qualità non garantisce un buon risultato. Garantisce che abbiamo scelto in modo difendibile dato ciò che potevamo sapere, e che l'esito — favorevole o no — diventa informazione per decidere meglio la volta successiva.**
