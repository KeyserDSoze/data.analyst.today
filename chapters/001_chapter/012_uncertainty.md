## 1.11 L'incertezza non è un difetto dell'analisi

Una cattiva cultura dei dati tende a premiare risposte nette.

> “Qual è il numero?”

> “Qual è la previsione?”

> “Qual è la causa?”

> “Quale opzione dobbiamo scegliere?”

Molte domande reali, però, non hanno una risposta perfettamente certa.

L'analista professionale non elimina artificialmente l'incertezza. Cerca di capire **da dove viene, quanto conta e che cosa cambia nella decisione**.

### Da dove nasce l'incertezza

Può entrare nell'analisi in punti molto diversi.

**Misurazione.** Tracking, sensori, survey e classificazioni possono essere imperfetti.

**Campionamento.** Osserviamo una parte della popolazione e vogliamo generalizzare.

**Dati mancanti.** Alcuni eventi non vengono registrati o mancano in modo non casuale.

**Definizione.** Una metrica è spesso un proxy imperfetto del concetto che ci interessa.

**Modello.** Ogni modello semplifica la realtà e incorpora assunzioni.

**Futuro.** Forecast e probabilità riguardano eventi che non sono ancora avvenuti.

**Comportamento.** Clienti, concorrenti e organizzazioni reagiscono e cambiano.

**Causalità.** Nei dati osservazionali possono restare spiegazioni alternative.

Trattare tutte queste fonti come un unico “margine di errore” rischia di nascondere il problema vero.

### Precisione apparente

Una dashboard può mostrare:

`Revenue forecast: €4,382,741`

Le cifre trasmettono precisione numerica. Non necessariamente conoscenza accurata del futuro.

Per una decisione potrebbe essere più informativo comunicare:

> previsione centrale: €4,38M; intervallo plausibile: €3,9–4,9M.

Il range è meno rassicurante, ma rende visibile un'informazione che il singolo numero nasconde.

### Non esiste un solo modo di rappresentare l'incertezza

A seconda del problema possiamo usare:

- intervalli di confidenza;
- intervalli di previsione;
- distribuzioni di probabilità;
- scenari;
- sensitivity analysis;
- range costruiti su assunzioni alternative.

Questi strumenti non sono decorazioni statistiche. Servono quando aiutano a distinguere decisioni robuste da decisioni che funzionano soltanto in uno scenario molto specifico.

### Significatività statistica e rilevanza pratica

Immaginiamo che un esperimento con milioni di utenti mostri un aumento del conversion rate dal 10,000% al 10,015%.

La differenza può essere statisticamente molto convincente e, allo stesso tempo, economicamente irrilevante.

Dipende dal volume, dal valore di ogni conversione, dal costo di implementazione e dagli effetti collaterali.

Il contrario è possibile: un effetto economicamente grande può essere stimato con troppa incertezza perché il campione è piccolo.

Dobbiamo quindi tenere separati almeno tre elementi:

1. **dimensione dell'effetto**;
2. **incertezza sulla stima**;
3. **rilevanza decisionale dell'effetto**.

Il Capitolo 5 entrerà nel dettaglio statistico. Qui ci interessa la separazione concettuale.

### La soglia dipende dal costo dell'errore

Supponiamo di stimare una probabilità del 60% che un'iniziativa produca un beneficio.

È sufficiente per procedere?

La percentuale, da sola, non risponde.

Se un piccolo test costa poco ed è reversibile, il 60% può essere sufficiente. Se una decisione è difficile da invertire e può produrre un danno enorme, richiederemo evidenza molto più forte.

Ogni decisione contiene almeno due errori possibili:

- agire quando non avremmo dovuto;
- non agire quando avremmo dovuto.

In fraud detection, per esempio, un falso positivo può bloccare un cliente legittimo, mentre un falso negativo lascia passare una frode.

La soglia corretta dipende dall'asimmetria tra questi costi.

### L'incertezza di misurazione viene prima dell'inferenza

NIST tratta l'incertezza come parte integrante della scienza della misurazione: modelli, osservazioni e distribuzioni servono a descrivere ciò che possiamo conoscere da misure imperfette.

Fonte:
- https://www.nist.gov/publications/concepts-principles-and-methods-assessment-measurement-uncertainty

Il principio è utile anche nel business analytics.

Un intervallo statistico strettissimo attorno a una metrica mal definita non rende la metrica più vera.

Prima di quantificare l'incertezza campionaria dobbiamo chiederci se stiamo misurando il fenomeno giusto.

### Comunicare l'incertezza senza diventare vaghi

Dire soltanto “non siamo sicuri” è poco utile.

Una comunicazione professionale specifica:

- che cosa sappiamo;
- quanto è robusta l'evidenza;
- che cosa non sappiamo;
- perché non lo sappiamo;
- quale decisione è sensibile a questa incertezza;
- quale informazione aggiuntiva la ridurrebbe maggiormente.

Per esempio:

> “I dati indicano un calo della conversione del 6–9% nel segmento mobile dopo la modifica del checkout. Il pattern è stabile per quattro settimane, ma nello stesso periodo è cambiato anche il mix delle campagne marketing. Non possiamo attribuire interamente il calo al checkout. Un test controllato permetterebbe di separare meglio i due effetti.”

Questa frase non nasconde l'incertezza e non la usa come alibi per non concludere nulla.

La rende utilizzabile.

### AI e sicurezza linguistica

Un sistema generativo può esprimere con grande fluidità anche una spiegazione fragile.

La forma linguistica non è una misura dell'incertezza epistemica.

Per questo, quando l'AI partecipa all'analisi, è utile separare esplicitamente fatti osservati, calcoli, assunzioni, ipotesi, interpretazioni e informazioni mancanti. Il metodo di supervisione è stato introdotto nel Capitolo 0 e verrà approfondito nel Capitolo 14.

Il principio che ci serve qui è più generale:

> **L'incertezza deve essere ridotta quando possibile, quantificata quando utile e dichiarata quando non può essere eliminata.**

Nasconderla non rende l'analisi più forte.

La rende più fragile.
