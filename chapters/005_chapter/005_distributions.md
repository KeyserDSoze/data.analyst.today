## 5.4 Distribuzioni di probabilità: un modello degli esiti possibili

Una distribuzione di probabilità non è soltanto una curva con un nome. È una descrizione di **quali valori può assumere un processo incerto e con quale peso relativo**.

Questo permette di rispondere a domande che una media da sola non può risolvere:

- quanto è probabile superare una soglia?
- quanto è plausibile osservare un risultato estremo?
- quanto varia il numero di eventi attorno al valore atteso?
- quale coda negativa dobbiamo dimensionare operativamente?

Il punto editoriale di questa sezione è quindi semplice:

> **una distribuzione è utile quando traduce il meccanismo del processo in assunzioni controllabili.**

### Discreto e continuo

Una variabile casuale **discreta** assume valori separati, per esempio:

- numero di ordini;
- numero di conversioni;
- numero di guasti;
- numero di clienti che fanno churn.

Una variabile **continua** può assumere, almeno idealmente, qualsiasi valore in un intervallo:

- tempo di consegna;
- importo di una transazione;
- temperatura;
- durata di una sessione.

La distinzione aiuta a capire quale famiglia di modelli può essere plausibile, ma non basta da sola a scegliere una distribuzione.

### Caso simulato/composito — “Ci aspettiamo 250 conversioni”

Un marketplace invia una campagna a 10.000 clienti. Il conversion rate atteso per una popolazione comparabile è 2,5%.

Il marketing manager conclude:

> “Quindi faremo circa 250 conversioni.”

`10.000 × 2,5% = 250` è il valore atteso, non il risultato garantito.

Se semplifichiamo il processo assumendo che:

1. ogni cliente abbia due esiti rilevanti, converte/non converte;
2. le 10.000 prove siano sufficientemente indipendenti;
3. la probabilità di conversione sia approssimativamente costante;

allora il numero di conversioni può essere modellato con una **binomiale**.

NIST descrive la distribuzione binomiale proprio come modello del numero di successi in `n` prove con due esiti e probabilità `p` costante.[^nist-binomial]

Nel nostro caso:

`X ~ Binomiale(n = 10.000, p = 0,025)`.

Il valore atteso è 250 e la deviazione standard è circa 15,6 conversioni.

Un risultato di 236 conversioni è quindi inferiore all'atteso, ma non è automaticamente evidenza di una campagna “rotta”. Fa parte del tipo di oscillazione che il modello considera plausibile.

La domanda professionale non è:

> “Abbiamo centrato esattamente 250?”

ma:

> **“Quanto è insolito il risultato osservato rispetto alla variabilità che ci aspettiamo dal processo?”**

### Il modello è un contratto di assunzioni

Nella campagna reale, l'ipotesi binomiale può essere approssimativa.

La probabilità di conversione può variare tra clienti. Alcuni appartengono a segmenti molto più propensi all'acquisto. Più persone della stessa azienda possono influenzarsi. La campagna può essere inviata in orari differenti.

Il modello può restare utile, ma solo se ricordiamo che:

> **il nome della distribuzione comprime un insieme di assunzioni sul processo.**

Quando quelle assunzioni falliscono in modo importante, anche una formula eseguita perfettamente risponde al modello sbagliato.

### La normale: importante, ma spesso nel posto sbagliato

La distribuzione normale ha un ruolo centrale nella statistica. NIST ricorda che molte procedure inferenziali la utilizzano e che il Central Limit Theorem spiega perché emerge frequentemente nelle **distribuzioni campionarie**.[^nist-normal]

Questo non significa che ogni variabile di business debba essere normale.

Importi, tempi di attesa, revenue per cliente e lifetime value possono essere fortemente asimmetrici o avere code pesanti.

Una distinzione che ci servirà più avanti è:

> **la distribuzione dei dati originali e la distribuzione di una statistica campionaria non sono la stessa cosa.**

Un AOV individuale può essere fortemente asimmetrico mentre, sotto condizioni appropriate e con campioni abbastanza grandi, la distribuzione della media campionaria può diventare approssimativamente normale.

Questa è una delle idee centrali del Central Limit Theorem, che affronteremo nella sezione 5.11.

### Caso simulato/composito — La coda che determina la decisione

Una compagnia assicurativa osserva molti sinistri da poche centinaia di euro e un numero ridotto di sinistri estremamente costosi.

La media può essere 1.850 €, ma il processo è fortemente asimmetrico.

Per il team che deve dimensionare riserve e capitale non basta stimare correttamente il centro. Conta la probabilità della **coda destra**.

Un modello che descrive bene la media ma sottostima drasticamente gli eventi estremi può essere peggiore, per quella decisione, di un modello meno elegante ma più realistico sulle code.

### Una piccola mappa, non un catalogo da memorizzare

Nel lavoro dell'analista incontreremo spesso idee come:

| Processo | Modello che può essere utile | Domanda |
|---|---|---|
| un singolo esito sì/no | Bernoulli | accade oppure no? |
| numero di successi su `n` prove | Binomiale | quanti successi? |
| conteggio di eventi su un'esposizione | Poisson, in condizioni appropriate | quanti eventi nel periodo/spazio? |
| errori o sampling distribution | Normale, in molte condizioni | quanto oscilla una stima? |

Questa tabella non è una regola automatica. È un promemoria per chiedere:

> **Quale processo sto rappresentando e quali assunzioni devo poter difendere?**

[^nist-binomial]: NIST/SEMATECH, *Binomial Distribution*: https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
[^nist-normal]: NIST/SEMATECH, *Normal Distribution*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
