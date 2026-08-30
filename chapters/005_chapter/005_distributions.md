## 5.4 Distribuzioni di probabilità: non esiste soltanto la media

Una distribuzione di probabilità descrive come si distribuisce l'incertezza tra i possibili valori di una variabile.

Questa frase può sembrare astratta, ma nel lavoro analitico è estremamente concreta.

Supponiamo di avere due campagne marketing con lo stesso numero medio di conversioni: 100 al giorno.

La prima produce quasi sempre tra 95 e 105 conversioni.

La seconda alterna giornate da 40 conversioni a giornate da 170.

La media è identica. Il rischio operativo è completamente diverso.

La distribuzione ci permette di vedere ciò che la media nasconde.

### Variabili discrete e continue

Una variabile casuale discreta assume valori separati:

- numero di ordini;
- numero di churn;
- numero di guasti;
- numero di clienti che convertono.

Una variabile continua può assumere, almeno idealmente, qualunque valore in un intervallo:

- tempo di consegna;
- importo di una transazione;
- temperatura di un sensore;
- durata di una sessione.

Questa distinzione aiuta a scegliere il modello distributivo appropriato.

### Caso realistico: una campagna che “dovrebbe” generare 250 conversioni

Un marketplace invia una campagna email a 10.000 clienti.

Il conversion rate storico è 2,5%.

Il marketing manager dice:

> “Quindi ci aspettiamo 250 conversioni.”

È corretto come valore atteso, ma non significa che il risultato sarà esattamente 250.

Se trattiamo ogni cliente come una prova con due esiti — conversione o non conversione — e assumiamo probabilità individuale costante e indipendenza tra le prove, il numero di conversioni può essere modellato con una distribuzione binomiale.

NIST descrive la binomiale proprio come il modello per il numero di successi in \(n\) prove con due esiti mutuamente esclusivi e probabilità di successo \(p\) costante.[^1]

Nel nostro esempio:

\[
X \sim Binomiale(n=10.000,p=0,025)
\]

Il valore atteso è:

\[
E[X]=np=250
\]

La deviazione standard è circa:

\[
\sqrt{np(1-p)} \approx 15,6
\]

Un risultato di 236 conversioni non è quindi necessariamente un fallimento della campagna. Può essere perfettamente compatibile con la variabilità casuale del processo.

Questa distinzione è fondamentale quando valutiamo performance giornaliere, campagne, funnel e test.

### Ma le assunzioni reggono davvero?

Il modello binomiale richiede condizioni che nel mondo reale possono non essere vere.

La probabilità di conversione potrebbe non essere uguale per tutti i clienti.

I clienti potrebbero influenzarsi tra loro.

La campagna potrebbe essere inviata in orari diversi.

Parte del pubblico potrebbe essere composto da clienti molto più propensi ad acquistare.

Il modello può comunque essere utile, ma dobbiamo ricordare che è una semplificazione.

### Distribuzione normale

La distribuzione normale è uno dei modelli più utilizzati in statistica.

È simmetrica, unimodale e descritta da due parametri principali: media e deviazione standard. NIST ricorda che la normale ha un ruolo centrale sia nella teoria sia nelle applicazioni statistiche e che il Teorema del Limite Centrale spiega parte della sua importanza.[^2]

Ma non tutti i dati sono normali.

Tempi di attesa, importi di acquisto, redditi e lifetime value sono spesso asimmetrici.

Applicare automaticamente la normale a qualsiasi variabile perché “è quella classica” può generare stime sbagliate nelle code.

### Caso realistico: il costo medio di un sinistro

Una compagnia assicurativa osserva un costo medio per sinistro di 1.850 euro.

Un modello ingenuo tratta il costo come quasi normale.

Ma la distribuzione reale è fortemente asimmetrica:

- molti sinistri tra 300 e 900 euro;
- una quota più piccola tra 2.000 e 10.000 euro;
- rarissimi sinistri sopra 100.000 euro.

La media è trainata dalla coda destra.

Un modello normale sottostima drasticamente la probabilità di costi estremi.

La scelta della distribuzione non è quindi una formalità tecnica: può cambiare riserve, pricing e valutazione del rischio.

### Una distribuzione non è un'etichetta da assegnare

NIST sottolinea che le distribuzioni sono usate per intervalli, test e simulazioni, ma che le assunzioni distributive devono essere adeguate al dataset e alla tecnica utilizzata.[^3]

Questo porta a una regola semplice:

**prima osserviamo la forma dei dati; poi scegliamo il modello.**

Non il contrario.

---

[^1]: NIST/SEMATECH, *Binomial Distribution*: https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
[^2]: NIST/SEMATECH, *Normal Distribution*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
[^3]: NIST/SEMATECH, *Probability Distributions*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda36.htm
