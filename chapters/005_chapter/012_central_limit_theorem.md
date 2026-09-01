## 5.11 Teorema del Limite Centrale: la normalità riguarda spesso la stima, non il dato grezzo

Il **Teorema del Limite Centrale**, o CLT, è uno dei ponti più importanti tra probabilità e inferenza.

In forma intuitiva, sotto condizioni appropriate, se prendiamo molti campioni della stessa dimensione e calcoliamo ogni volta la media, la distribuzione di quelle medie tende ad assumere una forma approssimativamente normale al crescere della dimensione del campione — anche quando la distribuzione delle osservazioni originali non è normale.

NIST riassume due proprietà centrali:

- la sampling distribution della media tende verso una forma normale all'aumentare di `n`;
- la sua dispersione si riduce come `σ / √n`.[^nist-clt]

Questo non significa:

> “i dati diventano normali”.

Significa:

> **in molte condizioni, la distribuzione della media campionaria diventa molto più regolare della distribuzione dei dati individuali.**

### Caso simulato/composito — Ordini fortemente asimmetrici, medie molto più regolari

Un e-commerce di arredamento ha una distribuzione degli importi molto asimmetrica:

- moltissimi ordini tra 40 e 180 €;
- alcuni tra 600 e 1.500 €;
- pochi progetti completi tra 8.000 e 20.000 €.

La distribuzione del **singolo ordine** non assomiglia affatto a una campana normale.

Il CFO, però, vuole stimare l'AOV di una popolazione ampia tramite campioni casuali.

Se il team prende ripetutamente campioni di 500 ordini e calcola ogni volta la media, le medie risultano molto meno asimmetriche dei singoli importi.

Il CLT spiega perché procedure basate sulla sampling distribution della media possono funzionare anche quando il dato grezzo è lontano dalla normalità.

### Il mito di `n = 30`

Una regola didattica molto diffusa dice:

> “con 30 osservazioni possiamo assumere normalità”.

È troppo meccanica per il lavoro professionale.

La velocità di convergenza dipende da fattori come:

- asimmetria;
- code pesanti;
- presenza di eventi estremi;
- distribuzioni con varianza molto elevata;
- dipendenza tra osservazioni.

Con dati relativamente regolari, 30 casi possono essere già utili. Con fenomeni estremamente heavy-tailed, 30 possono essere pochissimi.

Non serve memorizzare una soglia universale. Serve capire **quanto è difficile il processo che stiamo campionando**.

### La dipendenza riduce l'informazione effettiva

Immaginiamo di avere 10.000 click generati da soli 120 utenti.

Il file contiene 10.000 righe. Ma non abbiamo 10.000 utenti indipendenti.

Gli eventi dello stesso utente possono essere fortemente correlati.

Lo stesso problema compare con:

- transazioni ripetute dello stesso cliente;
- misure dello stesso sensore;
- ordini dello stesso negozio;
- dipendenti dello stesso team;
- serie temporali consecutive.

Applicare formule che trattano ogni riga come osservazione indipendente può produrre uno standard error artificialmente piccolo.

### Quando il CLT è utile all'analista

Il CLT aiuta a capire perché possiamo costruire, in molti contesti:

- intervalli per una media;
- approssimazioni normali di statistiche aggregate;
- test inferenziali;
- ragionamenti sulla precisione delle stime.

Ma non è una licenza per ignorare:

- disegno del campione;
- unità di analisi;
- dipendenza;
- bias;
- qualità del dato.

Il CLT affronta una parte specifica del problema: **la forma della variabilità campionaria**.

Non corregge un campione sbagliato e non rende casuale ciò che non lo è.

### La frase da ricordare

> **Non chiedere “i miei dati sono normali?”. Chiedi “quale statistica sto stimando, quale sampling distribution mi serve e le condizioni rendono ragionevole l'approssimazione che sto usando?”.**

È una domanda meno scolastica e molto più utile.

[^nist-clt]: NIST/SEMATECH, *Normal Distribution — Theoretical Justification: Central Limit Theorem*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
