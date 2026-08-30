## 4.2 La dispersione: due medie uguali possono nascondere due mondi diversi

Un valore centrale non basta. Due gruppi possono avere la stessa media e comportarsi in modo completamente diverso.

### Caso: due magazzini con la stessa produttività media

Due centri logistici processano in media 118 ordini per addetto al giorno.

Il management li considera equivalenti.

Poi vengono osservati i valori giornalieri delle ultime sei settimane.

Nel magazzino A quasi tutti gli addetti oscillano tra 108 e 128 ordini al giorno.

Nel magazzino B alcuni giorni si scende a 65, altri si superano i 170.

La media è uguale. La stabilità del processo no.

Per il responsabile operations questa differenza è decisiva: il secondo magazzino è molto più difficile da pianificare, richiede maggiore capacità di buffer e può produrre ritardi improvvisi.

### Range, varianza e deviazione standard

Il range è semplicemente la distanza tra minimo e massimo. È intuitivo ma molto sensibile agli estremi.

La varianza misura quanto le osservazioni si discostano mediamente dalla media, elevando al quadrato gli scarti.

La deviazione standard riporta questa dispersione nella stessa unità della variabile originale.

Non serve imparare la formula a memoria per usarla bene. Serve comprendere cosa significa:

**una deviazione standard elevata indica che il valore medio riassume una popolazione molto eterogenea.**

### Intervallo interquartile

L'IQR, o interquartile range, è la distanza tra il 25° e il 75° percentile.

È particolarmente utile quando la distribuzione contiene valori estremi perché descrive la dispersione della metà centrale dei dati.

### Coefficiente di variazione

Quando dobbiamo confrontare la variabilità di grandezze con scale molto diverse, possiamo usare il coefficiente di variazione:

**CV = deviazione standard / media**

Per esempio, una deviazione standard di 10 euro può essere enorme per un prodotto che costa mediamente 20 euro e irrilevante per uno che costa 2.000 euro.

### Cosa significa operativamente

La variabilità non è solo un concetto statistico. Può rappresentare:

- instabilità di processo;
- segmenti diversi mescolati insieme;
- stagionalità;
- errori di misura;
- domanda imprevedibile;
- comportamento differente tra clienti;
- rischio.

Un analista non dovrebbe quindi chiedersi soltanto "quanto vale in media?", ma anche:

**"quanto è prevedibile questo valore?"**
