## 14.9 AI per forecasting e modeling: rendere economica la ricerca senza svalutare la validazione

I Capitoli 7 e 10 hanno già definito come valutare forecast e modelli predittivi. Qui ci interessa una conseguenza specifica dell'AI-assisted workflow: **che cosa succede quando generare cento pipeline, feature set e varianti di modello costa quasi quanto generarne una?**

La capacità di provare di più è utile, ma rende molto più facile adattarsi accidentalmente all'evidenza che dovrebbe valutarci. Se ogni variante viene confrontata sullo stesso holdout e il risultato guida nuove feature, nuove trasformazioni e nuovi modelli, quell'holdout smette progressivamente di essere davvero indipendente. I target non entrano direttamente nel training, ma le nostre **decisioni** vengono ottimizzate contro di essi.

### Generator, selector, evaluator

Un workflow maturo separa tre funzioni:

```text
Generator
→ propone feature, modelli e configurazioni

Selector
→ sceglie candidati su validation/backtest

Evaluator
→ valuta il candidato finale su evidenza non usata nella ricerca
```

Per task importanti una parte dell'evidenza deve restare fuori dal ciclo di ottimizzazione. Possiamo chiamare questa disciplina **holdout sovereignty**: il test finale non è un cruscotto da consultare dopo ogni tentativo, ma un gate da proteggere.

### Il forecast "migliore" che peggiora il planning

Un distributore di elettronica usa un agente per ottimizzare il forecast settimanale.

Vecchio sistema:

```text
MAE medio:       17,4 unità per SKU-settimana
stockout rate:   6,1%
inventory days:  41
```

Nuovo candidato:

```text
MAE medio:       13,2
stockout rate:   7,0%
inventory days:  46
```

La metrica media migliora, ma due outcome operativi peggiorano. L'error analysis mostra che il vantaggio è concentrato sugli SKU ad alto volume, la domanda intermittente resta fragile e il planning engine reagisce in modo asimmetrico a overforecast e underforecast. La conclusione corretta non è che il nuovo modello "è peggiore" in assoluto. È che **la metrica di selezione non rappresenta abbastanza bene la funzione di costo della decisione downstream**.

### Modeling Delegation Contract

Quando deleghiamo model search all'AI, la Control Sheet deve vincolare il processo prima della leaderboard:

```text
prediction / forecast decision:
prediction time:
horizon:
feature availability as-of:
baseline:
training window:
validation / backtest design:
untouched final holdout:
allowed model families:
search budget:
primary metric:
business loss / guardrails:
segment diagnostics:
uncertainty / calibration requirement:
deployment constraints:
monitoring plan:
```

La velocità dell'AI rende ancora più importante una baseline semplice: last value, seasonal naive o forecast operativo corrente per le serie temporali; prevalence, regola business, regressione semplice o score esistente per i modelli predittivi. Se il candidato complesso non batte la baseline sul criterio che conta davvero, la complessità non ha guadagnato il diritto di entrare in produzione.

### Feature generation e frontiera `as-of`

Un agente può inventare feature molto predictive e inutilizzabili. Una variabile come `refund_confirmed_next_48h` può spiegare perfettamente un outcome storico e non esistere al prediction time. Ogni feature generata deve quindi avere almeno uno stato:

```text
available_at_prediction_time: YES / NO / UNCERTAIN
```

`UNCERTAIN` non significa "proviamo comunque". Significa **BLOCK** finché lineage e temporalità non vengono chiarite.

### Error analysis prima della classifica

Una leaderboard media nasconde struttura. Il workflow deve produrre anche errore per segmenti rilevanti, periodi peggiori, tail behavior, failure cases, confronto con baseline, stabilità tra fold/backtest, sensibilità a feature/window e, quando pertinente, calibration o interval coverage. Sapere **dove e come** il candidato fallisce è spesso più utile di sapere che vince di 0,3 punti su una metrica media.

Un modello offline, inoltre, non è ancora una policy. Deve rientrare nella Predictive Decision Card:

```text
score
→ threshold / top-K
→ capacity
→ intervention
→ outcome
→ monitoring
```

Un ranking eccellente può produrre zero valore se l'organizzazione non ha capacità di intervenire o se l'intervento non modifica l'outcome.

### Stop condition per la ricerca

La model search non deve continuare finché compare un numero migliore. Può fermarsi quando l'improvement è sotto una soglia materiale, il budget compute/costo è esaurito, nessun candidato batte la baseline in modo robusto, i guardrail peggiorano, il test finale è stato consultato troppe volte, i dati non rappresentano il deployment target o il business non può agire sul vantaggio predittivo.

Il NIST Generative AI Profile insiste su measurement ed evaluation nel contesto d'uso e lungo il lifecycle, non sulla sola performance di laboratorio.

Fonte: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

> **L'AI rende economico costruire candidati. Proprio per questo dobbiamo proteggere con maggiore disciplina l'evidenza che decide quale candidato merita fiducia.**
