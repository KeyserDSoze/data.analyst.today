# Capitolo 7 — Serie temporali, anomalie e forecasting

> **Il tempo non è soltanto una dimensione del dato. È informazione sul processo che ha generato il dato.**

Nel Capitolo 4 abbiamo guardato il tempo come una delle dimensioni dell'EDA: trend visivi, confronti tra periodi, pattern che meritano attenzione.

Qui facciamo un passo diverso.

Una serie temporale contiene **dipendenza, calendario, memoria e cambi di regime**. Il valore di oggi può essere informativo su domani. Un lunedì può assomigliare più agli altri lunedì che alla domenica precedente. Un picco può essere eccezionale rispetto alla media, ma perfettamente normale per Black Friday.

Questo cambia tre domande che in un dashboard sembrano simili ma non lo sono:

1. **Descrizione temporale:** che struttura osserviamo nel passato?
2. **Anomaly detection:** ciò che sta accadendo ora è insolito rispetto a una baseline appropriata?
3. **Forecasting:** quali valori futuri sono plausibili, con quale incertezza, dato ciò che sappiamo oggi?

E nessuna delle tre risponde automaticamente a una quarta domanda:

> **Perché il cambiamento è avvenuto?**

Quella è una domanda causale, che appartiene al Capitolo 8.

## 7.0 Dal grafico temporale alla decisione

NIST sottolinea che le serie temporali possono contenere struttura interna — autocorrelazione, trend e stagionalità — e che questa struttura deve essere considerata nell'analisi e nella modellazione.[^nist-ts]

Hyndman e Athanasopoulos pongono un principio complementare: il forecasting quantitativo ha senso quando esistono dati storici rilevanti e quando è ragionevole aspettarsi che **almeno una parte della struttura passata continui nel futuro**.[^fpp-data]

Questa seconda condizione è spesso la più importante e la meno discussa.

Un modello può essere sofisticato, validato e apparentemente preciso. Se nel frattempo il processo economico è cambiato, il passato può avere perso proprio la relazione che rendeva utile il forecast.

### Caso simulato/composito — Il lunedì in cui “crollano le vendite”

Alle 9:12 di lunedì il direttore commerciale di una catena retail scrive al team analytics:

> “Le vendite di ieri sono crollate del 24%. Cosa sta succedendo?”

Il dashboard mostra:

| Giorno | Ricavi |
| --- | ---: |
| Domenica precedente | 1,84 M€ |
| Domenica corrente | 1,40 M€ |
| Variazione | -23,9% |

Il numero è corretto rispetto ai dati caricati. La sua interpretazione non è ancora pronta.

L'analista controlla tre cose.

**1. Baseline comparabile.** La domenica precedente coincideva con un weekend promozionale nazionale.

**2. Calendario.** Rispetto alla domenica comparabile dell'anno precedente, il dato disponibile appare in crescita.

**3. Freshness.** Trentasei negozi non hanno ancora inviato la chiusura di cassa.

Dopo l'arrivo dei dati mancanti, i ricavi diventano 1,51 M€.

Il movimento non scompare, ma cambia significato: non è più “il business è improvvisamente crollato del 24%”. È un confronto contro una baseline promozionale eccezionale, costruito inizialmente su una giornata incompleta.

Questo episodio contiene l'intero capitolo in miniatura:

**dato temporale → baseline → calendario → completezza → struttura → anomalia → previsione → decisione**.

### Una anomalia non è una causa

Supponiamo che, una volta corretti i dati, la domenica rimanga davvero molto sotto la baseline stagionale.

Abbiamo allora evidenza di un comportamento insolito.

Non abbiamo ancora dimostrato che la causa sia:

- prezzo;
- competitor;
- stock-out;
- meteo;
- campagna;
- checkout;
- cambiamento di mix.

Un detector di anomalie produce un **segnale di investigazione**, non una spiegazione causale.

Questo confine sarà mantenuto in tutto il capitolo.

### Un forecast non è una promessa

Supponiamo invece che il modello dica:

> vendite previste per domenica prossima: 1,62 M€.

Quel numero non è il futuro. È un punto centrale ottenuto sotto determinate assunzioni e sulla base delle informazioni disponibili al momento della previsione.

Per essere decisionale servono almeno:

- orizzonte;
- intervallo o distribuzione di previsione;
- confronto con una baseline semplice;
- errore storico fuori campione;
- condizioni sotto cui il modello rimane valido;
- costo di sovrastima e sottostima.

Una previsione può essere statisticamente buona e operativamente inutile. Può anche essere mediocre in una metrica media e molto utile proprio dove l'errore costa di più.

## Il deliverable del capitolo: Temporal Decision Brief

Alla fine del capitolo ogni analisi temporale importante dovrebbe poter essere sintetizzata in un **Temporal Decision Brief**.

La struttura è:

```text
SERIE
Che cosa misura, con quale frequenza e quale timestamp?

BASELINE
Quale confronto rappresenta davvero il comportamento atteso?

STRUTTURA
Trend, stagionalità, calendario, autocorrelazione, cambi di scala?

ANOMALIA
È un problema del dato, un evento contestuale, un vero scostamento o un cambio di regime?

FORECAST TARGET
Che cosa dobbiamo prevedere, a quale orizzonte e per quale decisione?

BASELINE MODEL
Quale regola semplice dobbiamo battere?

BACKTEST
Avremmo avuto davvero quelle informazioni a quella data?

ERRORE
Quanto sbagliamo e dove costa di più?

INCERTEZZA
Quali scenari/intervalli sono plausibili e quanto sono calibrati?

CONDIZIONI DI VALIDITÀ
Che cosa deve restare abbastanza stabile perché il forecast continui a essere credibile?

AZIONE / MONITORAGGIO
Quale decisione cambia e quali segnali richiedono override o revisione?
```

Non è un template di model documentation. È un ponte tra la struttura temporale e la decisione.

### Il percorso del capitolo

Seguiremo questa sequenza:

**Series contract → baseline temporale → trend/stagionalità → lag/autocorrelazione → decomposizione → anomaly triage → forecast baseline → backtest → metriche e costo → prediction interval → regime change → Temporal Decision Brief**

L'obiettivo non è diventare specialisti di ogni famiglia di modelli.

È imparare a riconoscere quando il tempo contiene informazione, quando un modello sta usando il futuro senza accorgersene, quando un'anomalia appartiene al sistema di osservazione e quando una previsione è abbastanza affidabile da meritare una decisione.

> **Il forecast migliore non è quello che sembra conoscere il futuro. È quello che dichiara correttamente ciò che sa, ciò che assume e quanto costa quando sbaglia.**

[^nist-ts]: NIST/SEMATECH e-Handbook of Statistical Methods, “Introduction to Time Series Analysis”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
[^fpp-data]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Forecasting data and methods”, https://otexts.com/fpp3/data-methods.html
