## 8.16 Causal Identification Brief: il gate prima di usare il verbo “causare”

Questa sezione resta deliberatamente strutturata. Non è un riepilogo da memorizzare: è un **artefatto operativo** da compilare prima di presentare una causal claim. Il suo compito è rendere visibile dove l'evidenza deriva dai dati e dove dipende da assunzioni sul processo.

### Decisione ed estimand

Prima di tutto deve essere chiaro quale decisione cambierebbe se l'effetto fosse diverso, chi la prende, quale azione è realmente disponibile e quanto è reversibile. Senza questa connessione la causal analysis rischia di diventare un esercizio di attribuzione.

L'estimand deve poi essere scritto senza abbreviazioni concettuali:

```text
Unità:
Trattamento:
Alternativa / controllo:
Outcome:
Orizzonte:
Popolazione target:
Effetto desiderato: ATE / ATT / CATE / locale / altro:
```

“Effetto del programma” è quasi sempre troppo vago.

### Treatment, timing e assignment mechanism

Il trattamento deve corrispondere a qualcosa di abbastanza stabile da poter essere interpretato. Documentiamo momento di assignment, exposure effettiva, intensità, durata, versioni diverse, cross-over o non-compliance, finestra pre-treatment e outcome window.

La domanda di controllo è:

> **Tutte le unità classificate come trattate hanno ricevuto qualcosa di sufficientemente simile da meritare lo stesso nome?**

Subito dopo viene la parte spesso più importante del brief:

```text
Perché alcune unità ricevono T e altre no?
Randomizzazione?
Soglia?
Decisione umana?
Auto-selezione?
Capacità operativa?
Policy territoriale?
Timing esterno?
```

Se non sappiamo come nasce il trattamento, non sappiamo quali bias aspettarci e non possiamo scegliere coerentemente l'identification strategy.

### Causal model e controfattuale

Disegniamo o descriviamo cause comuni di trattamento e outcome, interventi reattivi, selection mechanism, collider, mediatori, variabili post-treatment, spillover e cause importanti non osservate. Il DAG può essere semplice; deve però rendere criticabile la storia causale.

Poi completiamo una frase che dovrebbe essere impossibile lasciare vaga:

> **Il controfattuale dei trattati è rappresentato da ______ perché ______.**

Il primo spazio può contenere un gruppo randomizzato al controllo, una regione con traiettoria comparabile, unità appena oltre una soglia, matched controls nell'area di overlap o variazione indotta da uno strumento. Il secondo spazio è l'identification argument. Se non sappiamo riempirlo, il metodo non è ancora giustificato.

### Identification strategy

| Struttura disponibile | Design possibile | Assunzione centrale |
|---|---|---|
| random assignment | RCT | assignment preservato / interference gestita |
| cambiamento differenziale nel tempo | DiD | counterfactual trends credibili |
| selection on observables | matching / weighting | no material unobserved confounding + overlap |
| cutoff di eleggibilità | RDD | continuity / no problematic manipulation |
| fonte esterna che muove T | IV | relevance + independence + exclusion + interpretazione locale |

Questa tabella non è una gerarchia universale dei metodi. Serve a ricordare che il design deve seguire la struttura che rende possibile il confronto.

### Diagnostics specifici del design

Per una **randomizzazione** controlliamo integrità dell'assignment, attrition e altre esclusioni post-randomizzazione, compliance e interference. Il Capitolo 9 aggiungerà SRM, peeking, stopping, exposure e telemetry checks perché un esperimento valido sulla lavagna può rompersi in produzione.

Per una **DiD** guardiamo pre-trends, announcement e anticipation, shock differenziali, composizione della popolazione e treatment timing. Per **matching/weighting** controlliamo overlap, balance prima e dopo, pesi estremi, effective sample size e unità escluse. Per **RDD** verifichiamo manipolazione della running variable, covariate continuity, altre policy al cutoff, bandwidth sensitivity e placebo cutoff quando sensato. Per **IV** documentiamo first stage, plausibilità dell'exogeneity, possibili percorsi alternativi verso `Y`, weak-instrument risk e popolazione dei compliers.

### Falsification e sensitivity

Una causal claim forte dovrebbe cercare attivamente modi per essere smentita. A seconda del design possono essere utili placebo outcome, placebo treatment date, effetti apparenti pre-trattamento, cutoff fittizi, specifiche alternative, esclusione di periodi anomali, negative controls, balance checks o sensitivity a unobserved confounding.

Un risultato che esiste soltanto nella specifica più favorevole merita una causal claim più debole, non una presentazione più selettiva.

### Effect, uncertainty e scope

Non consegniamo soltanto il segno del coefficiente. Il brief deve riportare dimensione assoluta, eventuale dimensione relativa, intervallo di incertezza, denominatore, popolazione, heterogeneity e rilevanza economica. Il Capitolo 5 fornisce il linguaggio della precisione; qui dobbiamo legarlo allo scope del design.

```text
L'effetto è locale a un cutoff?
Riguarda i trattati o tutta la popolazione?
Riguarda i compliers?
È stimato solo nell'area di common support?
Il mercato/periodo è particolare?
La treatment implementation è replicabile?
```

Internal validity ed external validity sono domande diverse. Una stima locale molto credibile non diventa automaticamente una policy globale.

### Claim ladder finale

| Livello | Linguaggio |
|---|---|
| Descrittivo | I trattati mostrano outcome migliori/peggiori. |
| Aggiustato osservazionale | La differenza rimane dopo bilanciamento delle covariate osservate. |
| Causale condizionato | Sotto le assunzioni del design, la stima è compatibile con un effetto causale di questa dimensione. |
| Decisionale | Per questa popolazione, l'effetto stimato e il suo valore economico giustificano questa policy, con questi guardrail. |

La regola è usare la frase più forte che l'evidenza sostiene, non quella più forte che il management vorrebbe sentire.

### Cosa non sappiamo

Ogni brief deve contenere anche il confine dell'evidenza:

```text
Incertezza statistica:
Assunzioni non verificabili direttamente:
Confondenti non osservati plausibili:
Limiti di generalizzazione:
Possibili spillover:
Dato o esperimento che ridurrebbe maggiormente l'incertezza:
```

Dichiarare un limite non indebolisce automaticamente l'analisi. Permette al decision maker di sapere **dove termina la conoscenza attuale e quale nuova evidenza avrebbe più valore**.

## Template finale

```text
CAUSAL IDENTIFICATION BRIEF

Decisione:
Estimand:
Treatment / alternative:
Population / horizon:
Assignment mechanism:
Causal model / DAG:
Counterfactual:
Identification strategy:
Core assumptions:
Diagnostics passed / failed:
Falsification / sensitivity:
Effect estimate + uncertainty:
Heterogeneity:
Scope / external validity:
Economic implication:
Claim consentito:
What we do not know:
Next evidence-generating step:
```

La frase da evitare rimane:

> “Abbiamo controllato per tutte le variabili, quindi è causale.”

Non possiamo quasi mai dimostrare che tutte le cause rilevanti siano state misurate, temporizzate e aggiustate correttamente. La formulazione professionale è più precisa:

> **Questo design identifica l'effetto sotto queste assunzioni; questi diagnostics le rendono più o meno plausibili; l'effetto stimato vale per questa popolazione e la causal claim non va estesa oltre questo scope senza nuova evidenza.**

## Dal design all'esperimento reale

Il Capitolo 8 termina dove comincia il problema operativo del Capitolo 9. Qui abbiamo visto **perché** la randomizzazione può costruire un controfattuale forte. Nel prossimo capitolo vedremo quanto è facile distruggere quel vantaggio durante l'implementazione: identità instabile, contamination, exposure diversa dall'assignment, Sample Ratio Mismatch, telemetria incompleta, metriche cambiate durante il test, peeking e rollout che modifica il sistema.

Il Causal Identification Brief definisce quale confronto dovrebbe essere credibile. L'**Experiment Contract** del Capitolo 9 dovrà preservare quella credibilità dal primo bucket fino alla decisione di ship.

> **La causalità professionale non consiste nel sembrare certi. Consiste nel sapere esattamente quale confronto rende credibile la conclusione, quali assunzioni restano e quale frase siamo autorizzati a difendere.**
