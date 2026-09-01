## 8.16 Causal Identification Brief: il gate prima di usare il verbo “causare”

Prima di presentare una causal claim, l'analista dovrebbe riuscire a compilare una scheda come questa.

Non è burocrazia.

È il modo per separare ciò che sappiamo dai passaggi che dipendono da assunzioni.

## 1. Decisione

```text
Quale decisione cambierebbe se l'effetto fosse diverso?
Chi decide?
Quale azione è realmente disponibile?
Quanto è reversibile?
```

Una causal analysis senza una decisione o policy collegata rischia di diventare un esercizio di attribuzione senza uso operativo.

## 2. Estimand

Specificare:

```text
Unità:
Trattamento:
Alternativa / controllo:
Outcome:
Orizzonte:
Popolazione target:
Effetto desiderato: ATE / ATT / CATE / locale / altro:
```

La frase “effetto del programma” è quasi sempre troppo vaga.

## 3. Treatment versions e timing

Documentare:

- quando avviene assignment;
- quando avviene exposure;
- intensità e durata;
- versioni diverse del trattamento;
- cross-over o non-compliance;
- finestra pre-treatment;
- finestra outcome.

Chiedere:

> **tutte le unità classificate come trattate hanno ricevuto qualcosa di sufficientemente simile da meritare lo stesso nome?**

## 4. Assignment mechanism

Questa è spesso la sezione più importante.

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

Se non comprendiamo come nasce il trattamento, non sappiamo quali bias aspettarci.

## 5. Causal model

Disegnare o descrivere:

- cause comuni di trattamento e outcome;
- reverse causality / treatment by indication;
- selection mechanism;
- collider plausibili;
- mediatori;
- variabili post-treatment;
- spillover/interference;
- cause importanti non osservate.

Il DAG può essere semplice. Deve però rendere esplicita la storia.

## 6. Controfattuale

Scrivere in una frase:

> “Il controfattuale dei trattati è rappresentato da ______ perché ______.”

Esempi:

- gruppo randomizzato al controllo;
- regione con traiettoria comparabile;
- unità appena oltre una soglia;
- matched controls nell'area di overlap;
- variazione indotta da uno strumento.

Se il secondo spazio resta vago, l'identificazione non è ancora chiara.

## 7. Identification strategy

Il metodo deve seguire il processo di assegnazione.

| Struttura disponibile | Design possibile | Assunzione centrale |
|---|---|---|
| random assignment | RCT | assignment preservato / interference gestita |
| cambiamento differenziale nel tempo | DiD | counterfactual trends credibili |
| selection on observables | matching / weighting | no material unobserved confounding + overlap |
| cutoff di eleggibilità | RDD | continuity / no problematic manipulation |
| fonte esterna che muove T | IV | relevance + independence + exclusion + interpretazione locale |

Non esiste una gerarchia universale che renda automaticamente un metodo “causale”.

Esiste un metodo più o meno coerente con la struttura del problema.

## 8. Diagnostics

### Randomizzazione

- assignment integrity;
- attrition/post-randomization exclusions;
- compliance;
- interference.

Il Capitolo 9 aggiungerà SRM, peeking, stopping e gli altri controlli sperimentali.

### DiD

- pre-trends;
- announcement/anticipation;
- shock differenziali;
- composizione;
- treatment timing.

### Matching / weighting

- overlap;
- balance pre/post;
- pesi estremi;
- effective sample size;
- unità escluse.

### RDD

- manipolazione running variable;
- covariate continuity;
- altri trattamenti al cutoff;
- bandwidth sensitivity;
- placebo cutoff quando sensato.

### IV

- first stage;
- plausibilità dell'exogeneity;
- percorsi alternativi verso Y;
- weak instrument risk;
- popolazione dei compliers.

## 9. Falsification e sensitivity

Una causal claim forte dovrebbe cercare modi per provare a smentirsi.

Possibili test:

- placebo outcome;
- placebo treatment date;
- effetto apparente prima del trattamento;
- cutoff fittizi;
- specifiche alternative;
- exclusion di periodi anomali;
- balance checks;
- negative controls quando appropriati;
- sensitivity a unobserved confounding, se disponibile.

Un risultato che esiste solo nella specifica più favorevole merita prudenza.

## 10. Effect + uncertainty

Non consegnare soltanto il segno del coefficiente.

Specificare:

- dimensione assoluta;
- dimensione relativa se utile;
- intervallo di incertezza;
- denominatore;
- popolazione a cui si riferisce;
- eventuale eterogeneità;
- rilevanza economica.

Il Capitolo 5 fornisce il linguaggio dell'incertezza; il Capitolo 15 collegherà effetto, economics e decisione.

## 11. Scope ed external validity

Chiedere:

```text
L'effetto è locale a un cutoff?
Riguarda i trattati o tutta la popolazione?
Riguarda i compliers?
È stimato solo nell'area di common support?
Il mercato/periodo è particolare?
La treatment implementation è replicabile?
```

Internal validity e generalizzazione non sono la stessa domanda.

## 12. Claim ladder finale

Scegliere deliberatamente il livello di linguaggio.

**Descrittivo**

> “I trattati mostrano outcome migliori.”

**Aggiustato osservazionale**

> “La differenza rimane dopo bilanciamento delle covariate osservate.”

**Causale condizionato**

> “Sotto le assunzioni del design, la stima è compatibile con un effetto causale di questa dimensione.”

**Decisionale**

> “Per questa popolazione, l'effetto stimato e il suo valore economico giustificano questa policy, con questi guardrail.”

Usare la frase più forte che l'evidenza sostiene, non quella più forte che il management vorrebbe sentire.

## 13. Cosa non sappiamo

Ogni brief deve contenere almeno una sezione:

```text
Incertezza statistica:
Assunzioni non verificabili direttamente:
Confondenti non osservati plausibili:
Limiti di generalizzazione:
Possibili spillover:
Dato o esperimento che ridurrebbe maggiormente l'incertezza:
```

Una limitazione dichiarata non indebolisce automaticamente una causal analysis.

Permette di sapere **dove finisce l'evidenza**.

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

## La frase da evitare

> “Abbiamo controllato per tutte le variabili, quindi è causale.”

Non possiamo quasi mai dimostrare che tutte le cause rilevanti siano state misurate e aggiustate correttamente.

## La frase professionale

> **“Questo design identifica l'effetto sotto queste assunzioni; questi diagnostics le rendono più o meno plausibili; l'effetto stimato vale per questa popolazione e la causal claim non va estesa oltre questo scope senza nuova evidenza.”**

È meno comoda di un coefficiente isolato.

È il tipo di frase su cui si possono costruire decisioni serie.

> **La causalità professionale non consiste nel sembrare certi. Consiste nel sapere esattamente quale confronto rende credibile la conclusione, quali assunzioni restano e quale frase siamo autorizzati a difendere.**
