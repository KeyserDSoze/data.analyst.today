## 15.10 Decision quality, execution quality e outcome quality: non imparare la lezione sbagliata

Uno degli errori più costosi nell'apprendimento organizzativo è giudicare una decisione soltanto dal risultato finale. Se l'esito è buono diciamo “avevamo ragione”; se è cattivo diciamo “la decisione era sbagliata”. In un mondo incerto questa equivalenza non regge.

Dobbiamo separare tre oggetti.

**Decision quality** riguarda la scelta ex ante: obiettivo, alternative, evidenza, assunzioni, incertezza, trade-off, downside, switching threshold, reversibilità e criteri di review erano ragionevoli dato ciò che sapevamo?

**Execution quality** riguarda ciò che abbiamo fatto davvero: rollout, target population, budget, training, implementazione tecnica e guardrail hanno rispettato la decisione approvata?

**Outcome quality** riguarda ciò che è successo nel mondo: effetto dell'azione, variabilità, competitor, macroeconomia, shock e altri eventi esterni.

L'outcome è reale, ma non è una misura pura della qualità della decisione.

| Decision process | Outcome | Lettura |
|---|---|---|
| forte | buono | processo solido + esito favorevole |
| forte | cattivo | possibile bad luck, execution issue o downside già contemplato |
| debole | buono | fortuna; il risultato positivo non valida il processo |
| debole | cattivo | outcome negativo e processo da correggere |

La casella culturalmente più pericolosa è **processo debole + outcome buono**: tende a essere premiata e quindi replicata.

### La campagna che “ha funzionato”

Un e-commerce investe €600k in una campagna. La decisione nasce da un'analisi osservazionale:

```text
clienti esposti acquistano +35%
```

Non vengono considerati selection bias, business as usual, holdout, incrementalità o alternative. Dopo il lancio il sistema di attribuzione riporta €900k di revenue e l'iniziativa viene dichiarata un successo.

Tre mesi dopo un test controllato su una campagna simile mostra che gran parte di quella revenue sarebbe avvenuta comunque. Il primo progetto può perfino avere avuto un risultato netto positivo. Ma il **processo decisionale** era fragile perché confondeva attribuzione e incrementalità.

Se premiamo soltanto il risultato, insegniamo all'organizzazione a ripetere la fragilità.

### Una buona decisione può produrre un outcome negativo

Consideriamo:

```text
A:
80% → +€1M
20% → -€200k

B:
100% → +€100k
```

Se l'organizzazione può assorbire il downside, le probabilità hanno una base difendibile e A è coerente con gli obiettivi, scegliere A può essere una buona decisione. Se poi si realizza il 20% negativo, abbiamo osservato un outcome che il Decision Record aveva già riconosciuto come possibile.

Dire “avremmo dovuto scegliere B” soltanto dopo aver visto l'esito è hindsight bias.

### Tornare al timestamp epistemico

Per valutare decision quality dobbiamo recuperare il punto di vista ex ante: cosa sapevamo, quali range avevamo dichiarato, quali alternative erano davvero disponibili, quali rischi avevamo previsto e quale informazione era realisticamente ottenibile prima della deadline.

NASA descrive la Decision Analysis come caratterizzazione delle alternative rispetto alle priorità del decision-maker **dato lo stato di conoscenza disponibile**, includendo assunzioni, limitazioni, incertezza e robustezza del ranking.[^nasa-quality] Questo è il criterio corretto anche per una review aziendale.

Tuttavia “non potevamo saperlo” non deve diventare una scusa universale. Dobbiamo distinguere ciò che era davvero imprevedibile da ciò che non abbiamo investigato, abbiamo ignorato o abbiamo scelto di non vedere. Se un team non segmenta renewal risk, ignora customer research disponibile, salta un pilot e non definisce churn guardrail, una parte dell'incertezza non era inevitabile: era gestibile.

### Prima di giudicare l'outcome, ricostruire la catena

Quando il risultato sorprende, chiediamo:

```text
decision process issue?
execution issue?
external/context shock?
expected downside realized?
measurement issue?
```

Un A/B test può supportare un rollout e la revenue totale dell'azienda può comunque scendere nel mese successivo per stagionalità, competitor shock, traffico aggregato in calo o un'implementazione differente da quella testata. Serve ricostruire il nesso tra decisione e outcome prima di attribuire successo o fallimento.

### Misurare la calibrazione dell'organizzazione nel tempo

I Decision Record creano una base per valutare anche la qualità delle aspettative. Per decisioni comparabili registriamo:

```text
expected range
actual outcome
which scenario occurred
which assumption missed
```

Dopo molti casi possiamo chiedere se i range contengono abbastanza spesso gli esiti, se sottostimiamo sistematicamente i tempi, se siamo troppo ottimisti sul downside commerciale o se alcune categorie di decisione sono meglio calibrate di altre.

La review può usare una scorecard senza ridurla a un singolo voto:

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

La funzione della tabella è diagnosticare **dove migliorare il sistema decisionale**, non premiare chi ha avuto fortuna.

> **Una decisione di qualità non garantisce un buon risultato. Garantisce che abbiamo scelto in modo difendibile dato ciò che potevamo sapere, e che l'esito — favorevole o no — diventa informazione per decidere meglio la volta successiva.**

[^nasa-quality]: NASA, *6.8 Decision Analysis*, https://www.nasa.gov/reference/6-8-decision-analysis/
