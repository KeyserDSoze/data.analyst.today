## 9.14 A/A test: verificare che la macchina sappia riconoscere un pareggio

In un **A/A test** due gruppi ricevono la stessa esperienza. Il trattamento è nullo, ma il test non è inutile: l'oggetto sotto osservazione diventa la piattaforma che produce randomizzazione, exposure, telemetria, metriche e inferenza.

Un programma sperimentale che non si comporta bene sotto il null non dovrebbe essere dato per affidabile quando compare una variante B.

### Che cosa significa “comportarsi bene” sotto il null

Non ci aspettiamo differenze numeriche zero. La randomizzazione genera fluttuazioni casuali e, con molte metriche, alcune supereranno soglie nominali per caso. L'A/A va quindi letto come test del **sistema**, non come ricerca di una scorecard tutta grigia.

Su molti A/A o molte repliche vogliamo verificare che il false-positive behavior sia compatibile con il metodo, che SRM resti sotto controllo, che non compaiano differenze persistenti per platform o assignment path e che intervalli e scorecard abbiano la calibration attesa.

Con 100 metriche, la domanda “esiste almeno un `p < 0,05`?” è quasi priva di valore. È più utile chiedere quante metriche si muovono rispetto al false-positive rate previsto, se le stesse metriche falliscono ripetutamente, se i segni sono sistematici e se i problemi si concentrano su browser, app version o pipeline specifiche.

### Caso reale documentato — Microsoft Teams A/A'/B

Microsoft Teams ha documentato un problema nei confronti tra **build releases**. Il semplice A/B tra build poteva essere distorto dalla penetrazione dell'update e dall'`update effect`, cioè dal processo stesso di passare da una build all'altra.

Il team costruì un framework **A/A'/B** per separare meglio questi effetti e creare un gate più affidabile per le release. In un caso reale il sistema rilevò regressioni statisticamente significative e la release venne fermata per investigare prima di procedere.[^teams-aa]

Il punto è importante: la piattaforma non stava validando soltanto “feature A vs feature B”. Stava testando la catena

```text
build creation
-> distribution/update
-> exposure
-> metric collection
-> release decision
```

Lo stesso principio vale quando cambia l'infrastruttura sperimentale. Se migriamo da cookie-based ID ad account-based ID, gli A/A possono verificare allocation, persistent bucketing, cross-device identity, denominatori, missing events e false-positive behavior prima che il nuovo sistema decida grandi rollout.

### A/A come monitoraggio della piattaforma

Non deve essere per forza un rituale una tantum. Può essere ripetuto dopo modifiche della randomization service, migrazioni telemetry, cambi del metric engine o nuove procedure inferenziali.

Nel 2026 Microsoft ExP ha usato migliaia di A/A scorecard per valutare empiricamente metodi di treatment-effect assessment e il loro comportamento sotto il null.[^ms-tea] Questo è un uso molto diverso dal “facciamo un A/A per vedere se 50/50 funziona”: serve a misurare la calibration dell'intero sistema analitico su scorecard reali.

### Che cosa un A/A sano non dimostra

Un pareggio ben riconosciuto non garantisce che il prossimo A/B sia immune da treatment-dependent missingness, interference o metriche business mal definite. Non rende sicuro il rollout. Dimostra che alcuni componenti fondamentali funzionano quando **nessuna differenza reale dovrebbe esserci**.

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

> **Prima di chiedere alla piattaforma quale variante vince, è ragionevole verificare che sappia riconoscere un pareggio e che sappia farlo in modo calibrato.**

[^teams-aa]: Microsoft Research, *A/A’/B Testing: Evaluating Microsoft Teams across Build Releases*: https://www.microsoft.com/en-us/research/articles/a-a-b-testing-evaluating-microsoft-teams-across-build-releases/
[^ms-tea]: Microsoft Research, *Treatment Effect Assessment at Scale*, 15 luglio 2026: https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/
