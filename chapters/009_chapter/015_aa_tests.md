## 9.14 A/A test: testare la macchina che produce gli esperimenti

In un **A/A test** due gruppi ricevono la stessa esperienza.

Se non esiste trattamento, perché spendere traffico?

Perché stiamo testando un altro oggetto:

> **la piattaforma di randomizzazione, exposure, telemetria, metriche e analisi.**

Un programma sperimentale che non riesce a comportarsi bene sotto il null non dovrebbe essere dato per affidabile quando compare una variante B.

### Che cosa ci aspettiamo sotto A/A

Non ci aspettiamo che ogni metrica sia numericamente identica.

La randomizzazione produce differenze casuali.

Se analizziamo molte metriche, alcune possono superare una soglia nominale per caso.

Ci aspettiamo però che, nel tempo e su molti A/A:

- false positive rate sia compatibile con il metodo;
- p-value/calibration behavior non mostri pattern sistematici anomali;
- SRM resti sotto controllo;
- non esistano differenze persistenti legate a platform, app version o assignment path;
- intervalli abbiano coverage coerente con le proprietà attese.

### Non giudicare A/A con “esiste almeno un p < 0,05?”

Con 100 metriche, qualche p-value piccolo è normale anche sotto il null.

Le domande migliori sono:

- quante metriche si muovono rispetto al false-positive rate atteso?
- le stesse metriche falliscono ripetutamente?
- il segno delle differenze è sistematico?
- i failure si concentrano per piattaforma o pipeline?
- l'SRM è sano?
- le scorecard aggregate sono calibrate?

Un A/A test è una prova del **sistema**, non una caccia a una cella perfettamente zero.

## Caso reale documentato — Microsoft Teams A/A'/B

Microsoft Teams ha documentato un problema particolare nel confronto tra **build releases**. Un semplice confronto tra build poteva essere distorto da differenze nella penetrazione dell'update e dall'`update effect`, cioè dal processo stesso di passare da una build all'altra.

Il team sviluppò un framework **A/A'/B** per separare meglio questi effetti e creare un gate più affidabile per le release. In un test reale il framework rilevò regressioni statisticamente significative e il team fermò la release per investigare prima di procedere.[^teams-aa]

Il caso è importante perché il “trattamento” da validare non era soltanto una feature.

Era l'intera catena:

```text
build creation
-> distribution/update
-> exposure
-> metric collection
-> release decision
```

### A/A per una nuova experimentation platform

Supponiamo di migrare da cookie-based ID a account-based ID.

Prima di affidare grandi decisioni alla nuova piattaforma, eseguiamo diversi A/A e controlliamo:

- 50/50 assignment;
- persistent bucketing;
- cross-device identity;
- metric denominators;
- missing events;
- balance di covariate pre-experiment;
- false positive behavior.

Se i risultati falliscono, abbiamo trovato il bug **prima** che producesse ship/no-ship sbagliati.

### A/A non è solo un test una tantum

In sistemi maturi può essere usato anche come monitoraggio periodico:

- dopo cambi della randomization service;
- dopo migrazioni telemetry;
- dopo modifiche di metric engine;
- dopo identity changes;
- per validare nuove procedure inferenziali;
- per confrontare false-positive behavior di metodi su scorecard reali.

Nel 2026 Microsoft ExP, per esempio, ha usato migliaia di A/A scorecard per valutare metodi di treatment-effect assessment e verificare empiricamente il loro comportamento sotto il null.[^ms-tea]

### A/A non può validare tutto

Un A/A sano non dimostra che:

- un A/B non avrà treatment-dependent missingness;
- non esisterà interference;
- la metrica primaria rappresenti il valore business;
- il rollout sarà sicuro.

Dimostra che alcuni componenti fondamentali si comportano correttamente quando **nessuna differenza reale dovrebbe essere presente**.

### Platform validation card

```text
System change being validated:
Randomization unit:
Expected allocation:
Number of A/A replications:
SRM behavior:
Metric false-positive calibration:
Persistent metric biases:
Platform/device slices:
Telemetry completeness:
Interval/scorecard calibration:
Failure patterns:
Gate to reopen A/B decisions:
```

> **Prima di chiedere alla piattaforma quale variante vince, è ragionevole verificare che sappia riconoscere un pareggio.**

[^teams-aa]: Microsoft Research, *A/A’/B Testing: Evaluating Microsoft Teams across Build Releases*: https://www.microsoft.com/en-us/research/articles/a-a-b-testing-evaluating-microsoft-teams-across-build-releases/
[^ms-tea]: Microsoft Research, *Treatment Effect Assessment at Scale*, 15 luglio 2026: https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/
