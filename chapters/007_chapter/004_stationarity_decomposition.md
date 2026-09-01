## 7.3 Stazionarietà e decomposizione: rendere esplicita la struttura prima del forecast

Molti metodi temporali funzionano meglio quando la struttura statistica che devono modellare non cambia continuamente.

Una nozione centrale è la **stazionarietà**.

In termini pratici, una serie stazionaria presenta proprietà come livello, variabilità e dipendenza temporale sufficientemente stabili nel tempo. Trend persistenti, stagionalità o cambiamenti della scala possono violare questa idea.[^nist-stationarity]

L'obiettivo non è trasformare ogni serie in un esercizio accademico di stazionarietà. È capire se stiamo chiedendo al modello di imparare una relazione che cambia mentre la osserviamo.

### Caso simulato/composito — La volatilità che cresce insieme al marketplace

Un marketplace passa da circa 20.000 a oltre 80.000 ordini giornalieri in quattro anni.

| Anno | Ordini medi/giorno | Deviazione standard |
| --- | ---: | ---: |
| 2023 | 21.400 | 2.100 |
| 2024 | 31.800 | 3.900 |
| 2025 | 49.600 | 6.700 |
| 2026 | 78.300 | 12.900 |

La volatilità assoluta aumenta insieme alla scala del business.

Un errore di 5.000 ordini aveva un significato enorme nel 2023 e molto diverso nel 2026.

L'analista prova una trasformazione logaritmica e osserva variazioni relative. Il processo diventa più stabile in termini percentuali.

La trasformazione non “migliora i dati”. Cambia la domanda modellata:

- livello assoluto;
- variazione assoluta;
- variazione relativa.

La scelta deve seguire il costo decisionale dell'errore.

### Differenziare: modellare il cambiamento invece del livello

Se una serie cresce persistentemente, può essere utile osservare:

`differenza_t = valore_t - valore_(t-1)`

Per esempio:

| Mese | Clienti attivi | Differenza |
| --- | ---: | ---: |
| Gen | 102.000 | — |
| Feb | 105.500 | +3.500 |
| Mar | 109.100 | +3.600 |
| Apr | 112.400 | +3.300 |

I livelli crescono. Le variazioni mensili sono più stabili.

Ma differenziare non è gratuito: perdiamo la lettura diretta del livello e possiamo rimuovere struttura utile se lo facciamo meccanicamente.

### Decomposizione: trend, stagionalità e remainder

Una rappresentazione concettuale utile è:

`serie = trend + stagionalità + residuo`

In altri processi la stagionalità cresce insieme al livello e una lettura moltiplicativa può essere più naturale.

La decomposizione serve a separare domande:

- qual è il movimento di fondo?
- quale parte si ripete con il calendario?
- che cosa rimane dopo aver rimosso le strutture principali?

Hyndman e Athanasopoulos insistono sul fatto che una buona comprensione dei pattern della serie dovrebbe precedere la modellazione e il forecasting.[^fpp]

### Il residuo non è “la causa sconosciuta”

Dopo la decomposizione, il remainder contiene ciò che il metodo non ha attribuito a trend o stagionalità.

Può includere:

- rumore casuale;
- eventi speciali;
- cambi di mix;
- problemi di dato;
- effetti promozionali;
- cambi strutturali;
- struttura ancora non modellata.

Chiamarlo “rumore” troppo presto può cancellare il segnale che vogliamo investigare.

### Caso simulato/composito — Le cancellazioni hotel a Pasqua

Una piattaforma travel osserva cancellazioni +17% in aprile e apre un incidente.

La vista storica mostra un aumento simile ogni primavera, ma il picco si sposta perché Pasqua cambia data.

Una semplice stagionalità mensile non allinea bene l'evento. Quando il calendario viene trattato esplicitamente, gran parte del +17% risulta coerente con il pattern festivo; il residuo anomalo è molto più piccolo.

La conclusione cambia:

> non abbiamo evidenza sufficiente per trattare l'intero aumento come incidente operativo; una quota consistente è spiegabile dal calendario noto.

Non abbiamo dimostrato **perché** Pasqua aumenti le cancellazioni. Abbiamo costruito una baseline più corretta.

### Structural break: quando la decomposizione storica non basta

Immaginiamo che un marketplace introduca consegna gratuita permanente.

Dopo il lancio:

- il livello medio degli ordini cambia;
- la sensibilità al weekend cambia;
- la varianza cambia.

Non abbiamo un'anomalia isolata. Potremmo avere un **cambio di regime**.

Un modello addestrato su anni precedenti continuerà per un po' a interpretare il nuovo processo come una sequenza di errori.

Questa distinzione sarà centrale quando parleremo dei forecast che smettono di funzionare.

### Test statistico e giudizio analitico

Esistono test formali di stazionarietà e change-point. Sono utili, ma non sostituiscono il contesto.

Una rottura statistica può coincidere con:

- migrazione di tracking;
- nuova definizione del KPI;
- pricing;
- acquisizione;
- pandemia;
- cambio di canale;
- vera evoluzione del comportamento.

Il test segnala che il processo appare diverso. L'analista deve capire **che tipo di differenza** sta osservando.

### La domanda operativa

Nel Temporal Decision Brief questa parte dovrebbe dichiarare:

> **La serie presenta trend ______, stagionalità ______ e variabilità ______. Per modellarla usiamo/non usiamo trasformazione o differenziazione perché ______. Il residuo mostra ______ e non viene interpretato causalmente senza ulteriore evidenza.**

Decomporre significa rendere esplicita la struttura. Non significa aver spiegato il business.

[^nist-stationarity]: NIST/SEMATECH e-Handbook of Statistical Methods, “Stationarity”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc442.htm
[^fpp]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., https://otexts.com/fpp3/
