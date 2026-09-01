# Capitolo 4 - Statistica descrittiva ed Exploratory Data Analysis

> Prima di spiegare un fenomeno, dobbiamo imparare a descriverlo senza distruggerne la struttura.

Nel Capitolo 3 abbiamo stabilito se i dati fossero abbastanza affidabili per essere usati. Adesso il problema cambia.

Abbiamo un dataset che ha superato una **Data Readiness Review**. Sappiamo che cosa rappresentano le righe, quali sono le chiavi, quale tempo stiamo osservando e quali caveat restano. Possiamo finalmente fare una domanda diversa:

> **Che forma ha il fenomeno nei dati?**

La statistica descrittiva serve a comprimere migliaia o milioni di osservazioni in quantità interpretabili: medie, mediane, percentili, tassi, misure di dispersione. L'Exploratory Data Analysis, o **EDA**, impedisce però che quella compressione cancelli proprio la struttura che dovremmo capire.

NIST descrive l'EDA come un approccio che usa soprattutto tecniche grafiche per massimizzare la comprensione del dataset, scoprirne la struttura, individuare anomalie e verificare assunzioni prima di imporre un modello formale.[^nist-eda]

La parola importante è **esplorare**.

Non significa generare grafici senza una domanda. Significa osservare il fenomeno da più angolazioni e separare con disciplina tre livelli:

1. **ciò che vediamo**;
2. **ciò che potrebbe spiegarlo**;
3. **ciò che non abbiamo ancora dimostrato**.

### Un riassunto può essere corretto e comunque insufficiente

Immaginiamo una società di logistica che comunichi:

```text
tempo medio di consegna
trimestre precedente: 3,8 giorni
trimestre corrente:   3,1 giorni
```

La conclusione spontanea è: il servizio è migliorato.

Segmentando per area emerge però:

```text
urbano:  2,1 → 1,8 giorni
rurale:  5,6 → 6,4 giorni
quota ordini urbani: 58% → 74%
```

Il totale migliora, ma una parte importante della variazione dipende anche dal **mix** degli ordini. Il dato medio non era falso. Era una compressione che nascondeva due dinamiche differenti.

Questo capitolo insegnerà a resistere alla tentazione di trasformare il primo numero disponibile in una storia.

### Caso reale documentato — quattro dataset quasi uguali nei numeri, diversissimi nei grafici

Un esempio classico è il **quartetto di Anscombe**, pubblicato da Francis Anscombe nel 1973 e ripreso dal NIST come dimostrazione del ruolo dell'EDA.

I quattro dataset hanno praticamente gli stessi riepiloghi principali: stessa media di `X`, stessa media di `Y`, stessa retta di regressione, deviazione residua quasi identica e correlazione circa `0,816`. Se guardassimo soltanto quei numeri, potremmo considerarli equivalenti.

Gli scatter plot mostrano invece quattro strutture molto diverse: una relazione lineare plausibile, una relazione curva, un dataset dominato da un outlier e un caso in cui un singolo punto ad alta leva determina quasi tutta la relazione.[^nist-anscombe]

La lezione non è che le statistiche sintetiche siano inutili.

È che **ogni sintesi perde informazione**, e l'analista deve sapere quale informazione rischia di perdere.

### Il percorso del capitolo

Procederemo così:

**centro → dispersione → code → forma → confronti → relazioni → tempo → robustezza → composizione → sintesi operativa**

Alla fine, un buon output di EDA non sarà una galleria di grafici. Sarà una mappa del fenomeno:

- quali pattern sono solidi;
- quali dipendono dalla composizione;
- quali sono guidati da pochi punti;
- quali cambiano con la baseline;
- quali spiegazioni sono plausibili;
- quale evidenza manca per passare da descrizione a spiegazione.

> **L'EDA non deve produrre la storia più convincente. Deve impedire che una storia prematura sopravviva al confronto con i dati.**

[^nist-eda]: NIST/SEMATECH, *Exploratory Data Analysis*. https://www.itl.nist.gov/div898/handbook/eda/eda_d.htm
[^nist-anscombe]: NIST/SEMATECH, *An EDA/Graphics Example*. https://www.itl.nist.gov/div898/handbook/eda/section1/eda16.htm