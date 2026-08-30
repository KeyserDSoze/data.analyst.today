## 1.11 L'incertezza non è un difetto dell'analisi

Una cattiva cultura dei dati tende a premiare risposte nette.

"Qual è il numero?"

"Qual è la previsione?"

"Qual è la causa?"

"Quale opzione dobbiamo scegliere?"

Il problema è che molte domande reali non hanno una risposta perfettamente certa.

L'analista professionale non elimina artificialmente l'incertezza. La misura, la rende visibile e la incorpora nel processo decisionale.

### Da dove nasce l'incertezza

L'incertezza può entrare nell'analisi in molti punti differenti.

**Misurazione.** Un sensore, un questionario, un sistema di tracking o una classificazione possono produrre valori imperfetti.

**Campionamento.** Osserviamo spesso una parte della popolazione e cerchiamo di generalizzare.

**Dati mancanti.** Alcuni eventi non vengono registrati oppure vengono registrati soltanto per determinati soggetti.

**Definizioni.** Una metrica può rappresentare soltanto approssimativamente il concetto che ci interessa.

**Modello.** Ogni modello statistico semplifica la realtà e introduce assunzioni.

**Futuro.** Previsioni e forecast riguardano eventi che non sono ancora avvenuti.

**Comportamento umano.** Clienti, concorrenti e organizzazioni modificano il proprio comportamento.

**Causalità.** Nei dati osservazionali possono esistere spiegazioni alternative non completamente eliminabili.

### Precisione apparente

Una dashboard può mostrare un valore come:

`Revenue forecast: € 4,382,741`

La presenza di molte cifre trasmette precisione. Non necessariamente trasmette accuratezza.

Una previsione più corretta potrebbe essere:

> previsione centrale: 4,38 milioni di euro; intervallo plausibile: 3,9–4,9 milioni.

L'intervallo è meno rassicurante, ma contiene più informazione utile.

### Intervalli, distribuzioni e scenari

Quando l'incertezza è rilevante, un singolo numero può essere insufficiente.

Possiamo comunicare:

- intervalli di confidenza;
- intervalli di previsione;
- distribuzioni di probabilità;
- scenari best/base/worst case;
- sensitivity analysis;
- range basati su assunzioni differenti.

La scelta dipende dal problema.

Non useremo questi strumenti come decorazioni statistiche. Li utilizzeremo quando aiutano a prendere decisioni migliori.

### Significatività statistica e significatività pratica

Immaginiamo che un esperimento con milioni di utenti mostri che un nuovo pulsante aumenta il conversion rate dal 10,000% al 10,015%.

Con un campione enorme la differenza potrebbe risultare statisticamente significativa.

Ma è economicamente importante?

Dipende dal volume, dal costo dell'implementazione, dagli effetti secondari e dal valore economico di ogni conversione.

Il contrario è altrettanto importante.

Un effetto economicamente rilevante può non raggiungere la soglia statistica desiderata perché il campione è troppo piccolo.

L'analista deve tenere separati almeno tre concetti:

1. **dimensione dell'effetto**;
2. **incertezza sulla stima**;
3. **rilevanza decisionale dell'effetto**.

### Probabilità e decisioni

Le decisioni aziendali vengono spesso prese prima che l'incertezza scompaia.

Supponiamo di stimare una probabilità del 60% che una nuova iniziativa produca un beneficio.

È sufficiente per procedere?

Non possiamo rispondere senza conoscere costi e conseguenze.

Se il costo del test è minimo e il potenziale beneficio è enorme, una probabilità del 60% potrebbe essere più che sufficiente.

Se un errore può mettere a rischio l'azienda, potremmo richiedere evidenza molto più forte.

Per questo la decisione non dipende soltanto dalla probabilità che un'ipotesi sia vera. Dipende anche dalla funzione di costo degli errori.

### Due tipi di errore

In molti problemi possiamo commettere almeno due errori opposti:

- agire quando non avremmo dovuto;
- non agire quando avremmo dovuto.

In fraud detection, per esempio, un falso positivo può bloccare un cliente legittimo, mentre un falso negativo lascia passare una frode.

In una campagna commerciale, contattare un cliente che non avrebbe acquistato può essere poco costoso; non contattare un cliente ad alto valore può essere molto più costoso.

La soglia decisionale dovrebbe riflettere questa asimmetria.

### L'incertezza di misurazione esiste prima della statistica

NIST tratta l'incertezza come parte integrante della scienza della misurazione: probabilità, distribuzioni, modelli di misura e osservazioni sono strumenti per esprimere e interpretare ciò che possiamo conoscere da misurazioni imperfette.

Questo principio è utile anche nel business analytics.

Prima di discutere sofisticati intervalli statistici dovremmo chiederci se la variabile stessa è misurata correttamente.

Un intervallo di confidenza molto stretto attorno a una metrica mal definita non rende la metrica più utile.

### L'AI e la falsa sicurezza

I sistemi generativi tendono a produrre risposte linguisticamente fluide. La fluidità può essere facilmente scambiata per certezza epistemica.

Una spiegazione può sembrare convincente senza essere ben supportata.

Per questo, quando utilizziamo l'AI nell'analisi, dovremmo chiederle esplicitamente di distinguere:

- fatti osservati;
- calcoli;
- assunzioni;
- ipotesi;
- interpretazioni;
- informazioni mancanti;
- possibili spiegazioni alternative.

E poi dobbiamo verificare questi elementi.

### Comunicare bene l'incertezza

Dire semplicemente "non siamo sicuri" è poco utile.

Una comunicazione migliore specifica:

- che cosa sappiamo;
- quanto è robusta l'evidenza;
- che cosa non sappiamo;
- perché non lo sappiamo;
- quali conseguenze produce questa incertezza;
- quale informazione aggiuntiva ridurrebbe maggiormente l'incertezza.

Esempio:

> I dati indicano un calo della conversione del 6–9% nel segmento mobile dopo la modifica del checkout. Il pattern è consistente per quattro settimane, ma nello stesso periodo è cambiato anche il mix delle campagne marketing. Non possiamo quindi attribuire interamente il calo al checkout. Un test controllato permetterebbe di separare i due effetti.

Questa frase è meno spettacolare di una conclusione assoluta.

È però molto più utile per decidere.

### Il principio operativo

Nel resto del libro adotteremo questa regola:

> **L'incertezza deve essere ridotta quando possibile, quantificata quando utile e dichiarata quando non può essere eliminata.**

Nascondere l'incertezza non rende l'analisi più forte.

La rende semplicemente più fragile.

### Fonte di approfondimento

- NIST, *Concepts, Principles, and Methods for the Assessment of Measurement Uncertainty*: https://www.nist.gov/publications/concepts-principles-and-methods-assessment-measurement-uncertainty
