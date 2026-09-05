## 7.3 Stazionarietà e decomposizione: capire se stiamo ancora osservando lo stesso processo

Lag e autocorrelazione ci dicono che il passato contiene memoria. Prima di trasferire quella memoria nel futuro dobbiamo però fare una domanda più profonda: **le proprietà del processo sono rimaste abbastanza stabili perché il passato e il presente siano ancora comparabili?**

La nozione di **stazionarietà** formalizza una parte di questo problema. In termini pratici, una serie è più facile da modellare quando livello, variabilità e struttura di dipendenza non cambiano continuamente; trend persistenti, stagionalità e cambi di scala possono violare questa stabilità.[^nist-stationarity] Non è necessario trasformare ogni progetto in un esercizio teorico. Serve riconoscere quando stiamo chiedendo al modello di imparare una relazione che cambia mentre la osserviamo.

### Caso simulato/composito — La volatilità che cresce con il marketplace

Un marketplace passa da circa 20.000 a oltre 80.000 ordini giornalieri in quattro anni:

| Anno | Ordini medi/giorno | Deviazione standard |
| --- | ---: | ---: |
| 2023 | 21.400 | 2.100 |
| 2024 | 31.800 | 3.900 |
| 2025 | 49.600 | 6.700 |
| 2026 | 78.300 | 12.900 |

La volatilità assoluta cresce insieme alla scala. Un errore di 5.000 ordini aveva un peso enorme nel 2023 e molto diverso nel 2026. Guardando la serie su scala logaritmica e ragionando in variazioni relative, il comportamento appare più stabile in termini percentuali.

La trasformazione non “migliora” i dati. Cambia l'oggetto che stiamo modellando: livello assoluto, variazione assoluta o variazione relativa. La scelta deve essere coerente con la decisione e con il costo dell'errore.

Lo stesso vale per la **differenziazione**. Se i clienti attivi passano da 102.000 a 105.500, poi 109.100 e 112.400, i livelli mostrano crescita continua mentre le differenze mensili — +3.500, +3.600, +3.300 — sono molto più stabili. Modellare il cambiamento può rendere più chiara la dinamica, ma comporta un costo: perdiamo la lettura diretta del livello e rischiamo di rimuovere struttura utile se differenziamo meccanicamente.

### Decomporre per sapere che cosa resta

Una rappresentazione concettuale utile è:

`serie = trend + stagionalità + residuo`

Quando l'ampiezza stagionale cresce con il livello può essere più naturale una struttura moltiplicativa. In entrambi i casi la decomposizione serve a separare domande diverse: qual è il movimento di fondo? quale parte si ripete con il calendario? che cosa rimane dopo aver rappresentato le componenti principali? Hyndman e Athanasopoulos insistono proprio sulla necessità di comprendere i pattern della serie prima del forecasting.[^fpp]

Il **remainder** non va però chiamato troppo rapidamente “rumore”. Può contenere casualità, eventi speciali, problemi di dato, promozioni, cambi di mix, rotture strutturali o dipendenza che il modello non ha ancora catturato. Eliminare ciò che resta senza investigarlo può significare cancellare proprio il segnale che ci interessa.

Una piattaforma travel, per esempio, osserva cancellazioni **+17% in aprile** e apre un incidente. La storia mostra però un aumento simile ogni primavera; il picco si sposta perché Pasqua cambia data. Una semplice stagionalità mensile non allinea bene l'evento. Quando il calendario festivo viene trattato esplicitamente, gran parte del +17% diventa coerente con la struttura nota e il residuo anomalo si riduce molto. Non abbiamo spiegato causalmente perché Pasqua aumenti le cancellazioni; abbiamo soltanto smesso di chiamare anomalia ciò che la baseline avrebbe dovuto aspettarsi.

### Quando cambia il regime

Il problema diventa più serio quando non cambia un singolo punto ma il processo stesso. Se un marketplace introduce consegna gratuita permanente, possono cambiare insieme livello medio degli ordini, sensibilità al weekend e varianza. Un modello addestrato sul vecchio regime può continuare per settimane a interpretare il nuovo come una sequenza di errori.

Test formali di stazionarietà e change-point possono aiutare, ma il contesto resta indispensabile. Una rottura statistica può coincidere con pricing, acquisizione, pandemia, tracking, nuova definizione del KPI o vera evoluzione del comportamento. Il test segnala che la serie appare diversa; l'analista deve capire **che tipo di differenza** sta osservando.

Nel Temporal Decision Brief questa parte dovrebbe riuscire a dichiarare:

> **La serie presenta trend ______, stagionalità ______ e variabilità ______. Usiamo/non usiamo trasformazione o differenziazione perché ______. Dopo aver rappresentato la struttura nota, il residuo mostra ______; non lo interpretiamo causalmente senza ulteriore evidenza.**

A questo punto abbiamo una baseline e un modello mentale del comportamento normale. Possiamo quindi affrontare la domanda operativa successiva: **quando uno scostamento merita davvero di essere chiamato anomalia?**

[^nist-stationarity]: NIST/SEMATECH e-Handbook of Statistical Methods, “Stationarity”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc442.htm
[^fpp]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., https://otexts.com/fpp3/
