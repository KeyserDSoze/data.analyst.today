## 5.10 Standard error: quanto oscilla la nostra stima

Lo **standard error** misura la variabilità di una statistica tra possibili campioni ottenuti con lo stesso processo.

Per la media, sotto condizioni semplici di campionamento indipendente, una stima comune è:

`SE(x̄) ≈ s / √n`

La formula mostra una relazione fondamentale:

> a parità di variabilità del fenomeno, aumentando il campione la media stimata tende a diventare più precisa.

Ma la precisione migliora con la **radice quadrata** di `n`.

Raddoppiare il campione non dimezza lo standard error. Per dimezzarlo servono, in prima approssimazione, quattro volte le osservazioni.

### Deviazione standard e standard error non sono sinonimi

La **deviazione standard** risponde a:

> quanto variano le singole osservazioni?

Lo **standard error** risponde a:

> quanto varierebbe la statistica che sto stimando se ripetessi il campionamento?

Un processo può avere tempi di consegna molto variabili e, grazie a milioni di ordini, una media conosciuta con grande precisione.

Oppure può avere osservazioni relativamente omogenee ma una media poco precisa perché abbiamo pochi casi.

Questa distinzione è una delle più importanti del capitolo.

### Caso simulato/composito — Milano e Parma

Una piattaforma di food delivery confronta il tempo medio di consegna mensile.

**Milano**

- `n = 48.200` ordini;
- media = 31,4 minuti;
- deviazione standard = 9,8 minuti.

**Parma**

- `n = 620` ordini;
- media = 29,9 minuti;
- deviazione standard = 10,1 minuti.

Le deviazioni standard sono simili: le singole consegne hanno variabilità comparabile.

Ma la media di Parma è stimata su una base molto più piccola e quindi oscilla molto di più da periodo a periodo.

La settimana successiva Parma passa a 33,1 minuti; poi torna a 30,4. Il management cerca ogni volta una spiegazione operativa.

Una parte di quei movimenti può invece essere semplicemente la maggiore **sampling variability** di un mercato piccolo.

### La formula semplice non vale automaticamente per ogni dataset

`SE = s / √n` presuppone una struttura semplice. Nel lavoro reale possiamo avere:

- utenti con più eventi;
- clienti raggruppati per azienda;
- ordini dentro lo stesso store;
- osservazioni serialmente correlate nel tempo;
- campionamenti stratificati o clusterizzati;
- pesi di survey.

In questi casi 10.000 righe non equivalgono necessariamente a 10.000 osservazioni indipendenti.

Trattarle come tali può sottostimare l'incertezza.

Questo è un principio che ricomparirà negli A/B test: **l'unità di analisi e l'unità di randomizzazione determinano quanta informazione indipendente abbiamo realmente**.

### Le classifiche spingono i piccoli campioni agli estremi

Se ordiniamo decine di unità per un KPI, quelle con pochi casi tenderanno più facilmente a comparire tra i valori estremi semplicemente perché le loro stime sono più rumorose.

Per questo un ranking professionale dovrebbe mostrare, quando utile:

- valore stimato;
- denominatore;
- intervallo di incertezza;
- periodo di osservazione.

Ordinare soltanto per la stima puntuale può trasformare rumore in reputazione.

### Dalla precisione all'intervallo

Lo standard error è un ingrediente centrale degli intervalli di confidenza.

La logica è:

**stima puntuale + variabilità campionaria → intervallo di valori compatibili con il metodo**.

Prima, però, dobbiamo capire perché in molti problemi la sampling distribution assume una forma abbastanza regolare da permetterci questo passaggio. È il ruolo del Central Limit Theorem.

> **La dimensione del dataset non è la stessa cosa della quantità di informazione indipendente contenuta nel dataset.**
