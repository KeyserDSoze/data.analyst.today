## 14.9 AI per forecasting e modeling: rendere economica la ricerca senza rendere economica la validazione

I Capitoli 7 e 10 hanno già definito come valutare forecast e modelli predittivi.

Qui il problema è specifico dell'AI-assisted workflow:

> **cosa succede quando generare cento pipeline, feature set e varianti di modello costa quasi quanto generarne una?**

La risposta non è soltanto “possiamo provare di più”.

È anche:

> **aumenta la pressione sul validation design, perché diventa molto più facile adattarsi accidentalmente al test che dovrebbe valutarci.**

### Il rischio della ricerca automatizzata

Supponiamo di voler prevedere otto settimane di vendite per 12.000 SKU.

Un agente può provare:

- diverse trasformazioni;
- feature calendar;
- lag alternativi;
- modelli statistici;
- gradient boosting;
- modelli gerarchici;
- ensemble;
- molti iperparametri.

Se ogni variante viene confrontata sullo stesso holdout, quell'holdout smette progressivamente di essere indipendente.

Non perché i suoi target entrino direttamente nel training, ma perché **le nostre scelte vengono ottimizzate contro di esso**.

### Regola: separare generator, selector ed evaluator

Un workflow maturo distingue tre funzioni.

```text
Generator
→ propone feature, modelli e configurazioni

Selector
→ sceglie candidati su validation/backtest

Evaluator
→ valuta il candidato finale su dati non usati nella ricerca
```

Per task importanti, l'Evaluator dovrebbe essere il più indipendente possibile dal processo che ha generato la soluzione.

Questa è una forma di **holdout sovereignty**: una parte dell'evidenza deve restare fuori dal ciclo di ottimizzazione.

### Caso simulato/composito — il forecast “migliore” che peggiora il planning

Un distributore di elettronica usa un agente per ottimizzare il forecast settimanale.

Vecchio sistema:

- MAE medio: 17,4 unità per SKU-settimana;
- stockout rate: 6,1%;
- inventory days: 41.

Nuovo candidato:

- MAE: 13,2;
- stockout rate: 7,0%;
- inventory days: 46.

Il modello migliora la metrica media ma peggiora due outcome operativi.

L'analisi degli errori mostra che:

- il miglioramento è concentrato sugli SKU ad alto volume;
- la domanda intermittente resta fragile;
- il planning engine reagisce in modo asimmetrico agli errori;
- il costo di overforecast e underforecast non è lo stesso.

La conclusione corretta non è:

> “il nuovo modello è peggiore perché aumenta gli inventory days.”

È:

> “la metrica con cui abbiamo selezionato il modello non rappresenta sufficientemente la funzione di costo del sistema decisionale downstream.”

### Il Modeling Delegation Contract

Quando deleghiamo model search all'AI, la Control Sheet dovrebbe contenere:

```text
prediction/forecast decision:
prediction time:
horizon:
feature availability as-of:
baseline:
training window:
validation/backtest design:
untouched final holdout:
allowed model families:
search budget:
primary metric:
business loss / guardrails:
segment diagnostics:
uncertainty/calibration requirement:
deployment constraints:
monitoring plan:
```

Il modello può proporre alternative soltanto dentro questi vincoli.

### Baseline prima della ricerca

La velocità dell'AI rende ancora più importante una baseline semplice.

Per forecasting potrebbe essere:

- last value;
- seasonal naive;
- moving average;
- forecast operativo corrente.

Per classification/regression:

- prevalence/base rate;
- regola business attuale;
- regressione semplice;
- score esistente.

Se il nuovo sistema non batte una baseline sul criterio che conta davvero, la complessità aggiunta non ha guadagnato il diritto di entrare in produzione.

### Feature generation: la disponibilità `as-of` resta non negoziabile

Un agente può inventare feature molto predictive e inutilizzabili.

Esempio:

```text
feature: refund_confirmed_next_48h
```

può spiegare perfettamente un outcome passato.

Ma se il prediction time è prima del refund, quella feature non esiste ancora.

Ogni feature generata dovrebbe quindi avere un attributo:

```text
available_at_prediction_time: yes / no / uncertain
```

`uncertain` non significa “proviamo comunque”.

Significa **BLOCK finché la lineage temporale non viene chiarita**.

### Error analysis prima della leaderboard

Una leaderboard media nasconde struttura.

L'AI dovrebbe essere obbligata a produrre almeno:

- errore per segmento rilevante;
- periodi peggiori;
- tail behavior;
- failure cases;
- confronto con baseline;
- stabilità tra fold/backtest;
- sensibilità a feature e data window;
- eventuale calibration o interval coverage.

Perché il modello sbaglia è spesso più utile di sapere che è primo di 0,3 punti su una metrica media.

### Un modello offline non è ancora una policy

Anche un candidato predittivo valido deve attraversare il resto della Predictive Decision Card del Capitolo 10:

```text
score
→ threshold/top-K
→ capacity
→ intervention
→ outcome
→ monitoring
```

L'AI può ottimizzare un ranking perfetto e produrre zero valore se l'organizzazione non ha capacità di intervenire, se l'azione è inefficace o se il serving non replica le feature del training.

### Forecast: point estimate non basta

Se il forecast entra in una decisione di inventory, cash o capacity, chiediamo anche:

- prediction interval;
- coverage per horizon;
- errori per regime;
- comportamento nei periodi promozionali;
- revisioni tardive delle feature;
- scenario in cui il modello degrada.

Un agente che produce soltanto il valore centrale sta nascondendo una parte della decisione.

### Quando l'AI deve fermare la model search

La ricerca non deve continuare finché compare un numero migliore.

Stop condition possibili:

- improvement sotto soglia materiale;
- budget compute/costo esaurito;
- nessun candidato batte baseline in modo robusto;
- performance migliora ma guardrail peggiorano;
- il test finale è stato consultato troppe volte e deve essere ricostruito;
- i dati non rappresentano il deployment target;
- il business non può agire sul vantaggio predittivo.

### Fonte di governance

Il NIST AI RMF e il profilo Generative AI insistono sulla misurazione e valutazione nel contesto d'uso e lungo il lifecycle, non sulla sola performance di laboratorio.

Fonte: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

### Campo della AI Analysis Control Sheet

```text
model-search delegated?:
search budget:
baseline:
validation/backtest:
final untouched evidence:
leakage/as-of checks:
primary + business metrics:
segment failure analysis:
uncertainty/calibration:
deployment constraints:
release gate:
```

> **L'AI rende economico costruire candidati. Proprio per questo dobbiamo proteggere con maggiore disciplina l'evidenza che decide quale candidato merita fiducia.**
