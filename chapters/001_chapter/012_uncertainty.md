## 1.11 L'incertezza non è un difetto dell'analisi

Una cattiva cultura dei dati tende a premiare risposte nette. *Qual è il numero? Qual è la previsione? Qual è la causa? Quale opzione dobbiamo scegliere?*

La pressione è comprensibile: le organizzazioni devono agire. Ma molte domande reali non hanno una risposta perfettamente certa, e fingere che l'incertezza non esista non rende la decisione più semplice. La rende soltanto meno informata.

L'analista professionale non usa l'incertezza come alibi per evitare una conclusione e non la nasconde per sembrare più autorevole. Cerca di capire **da dove viene, quanto modifica ciò che crediamo e se cambia l'azione che conviene intraprendere**.

### Non tutta l'incertezza nasce nello stesso punto

Possiamo essere incerti perché la misurazione è imperfetta: tracking, sensori, survey e classificazioni osservano il fenomeno con errore. Possiamo esserlo perché vediamo soltanto un campione e vogliamo generalizzare alla popolazione. Oppure perché alcuni dati mancano in modo non casuale, perché la metrica è un proxy, perché il modello semplifica la realtà o perché stiamo parlando di un futuro che non è ancora avvenuto.

Nei problemi causali esiste poi un'incertezza ancora diversa: più spiegazioni possono essere compatibili con gli stessi dati osservazionali. Nei sistemi umani il comportamento aggiunge un ulteriore livello, perché clienti, concorrenti e organizzazioni reagiscono alle decisioni e cambiano nel tempo.

Mettere tutto sotto l'etichetta “margine di errore” può essere comodo, ma nasconde che queste fonti richiedono risposte diverse. Aumentare il campione riduce l'incertezza campionaria; non corregge una metrica che misura il fenomeno sbagliato. Un modello più complesso può catturare pattern aggiuntivi; non recupera eventi che il tracking non ha registrato. Un intervallo statistico molto stretto può essere perfettamente calcolato attorno a una definizione semanticamente fragile.

La prima domanda deve quindi essere: **di che tipo di incertezza stiamo parlando?**

### Precisione numerica e conoscenza non sono la stessa cosa

Una dashboard può mostrare:

`Revenue forecast: €4,382,741`

Il numero comunica precisione perché contiene molte cifre. Non ci dice quanto il futuro sia prevedibile.

Per una decisione potrebbe essere più informativo scrivere:

> previsione centrale: €4,38M; intervallo plausibile: €3,9–4,9M.

Il range sembra meno rassicurante, ma contiene un'informazione decisiva. Se un investimento è sostenibile soltanto sopra €4,7M, l'incertezza è centrale. Se rimane conveniente anche nello scenario da €3,9M, forse non abbiamo bisogno di una previsione più precisa per decidere.

Il valore dell'incertezza non sta quindi nel rendere il report più sofisticato. Sta nel mostrare **quanto la scelta sia robusta rispetto a ciò che non sappiamo**.

A seconda del problema possiamo rappresentarla con intervalli di confidenza o previsione, distribuzioni di probabilità, scenari, sensitivity analysis o range costruiti su assunzioni alternative. Nessuno di questi strumenti è universalmente migliore. La domanda è quale renda visibile l'incertezza che conta per la decisione.

### Significatività, dimensione dell'effetto e valore decisionale devono restare separati

Immaginiamo che un esperimento con milioni di utenti mostri un aumento del conversion rate dal 10,000% al 10,015%.

Con un campione enorme, la differenza può essere statisticamente molto convincente. Ma può essere economicamente irrilevante se il beneficio generato è inferiore al costo di implementazione o se introduce effetti collaterali.

Il contrario è possibile. Un effetto potenzialmente molto grande può essere stimato con elevata incertezza perché il campione è piccolo. In quel caso il problema non è che l'effetto non conti: è che non sappiamo ancora abbastanza bene quanto sia grande.

Dobbiamo quindi tenere separati tre oggetti: **la dimensione dell'effetto**, **l'incertezza con cui la stimiamo** e **il valore che quell'effetto avrebbe nella decisione**. Il Capitolo 5 entrerà nel dettaglio statistico; qui ci interessa impedire che una sola etichetta, come “significativo”, sostituisca tutte e tre le domande.

### La soglia di evidenza dipende dal costo dei due errori possibili

Supponiamo di stimare una probabilità del 60% che un'iniziativa produca un beneficio. È sufficiente per procedere?

La probabilità, da sola, non può rispondere.

Se possiamo fare un piccolo test a basso costo e annullarlo facilmente, il 60% può essere più che sufficiente: agire produce informazione e il danno potenziale è limitato. Se dobbiamo prendere una decisione costosa, difficile da invertire e capace di produrre un danno significativo, la stessa evidenza può essere troppo debole.

Dietro ogni scelta esistono almeno due errori: agire quando non avremmo dovuto e non agire quando avremmo dovuto. I loro costi raramente sono simmetrici. In fraud detection, per esempio, un falso positivo può bloccare un cliente legittimo, mentre un falso negativo lascia passare una frode. Modificare la soglia significa scegliere quale combinazione di questi costi siamo disposti ad accettare.

Per questo “quanta certezza serve?” è in parte una domanda statistica e in parte una domanda decisionale.

### L'incertezza di misurazione viene prima dell'inferenza

NIST tratta l'incertezza come parte integrante della scienza della misurazione: osservazioni, modelli e distribuzioni servono a descrivere ciò che possiamo conoscere a partire da misure imperfette.[^nist-uncertainty]

Il principio è utile anche nel business analytics. Prima di quantificare con grande precisione l'incertezza campionaria dobbiamo verificare se la misura di partenza rappresenti il fenomeno giusto. Un intervallo strettissimo attorno a una metrica mal definita non la rende più vera; ci rende soltanto molto sicuri rispetto al numero che abbiamo deciso di calcolare.

### Comunicare l'incertezza significa renderla operativa

Dire soltanto “non siamo sicuri” trasferisce il problema a chi deve decidere. Una comunicazione utile distingue invece ciò che osserviamo direttamente, la forza dell'evidenza, ciò che rimane ambiguo e soprattutto quale decisione sia sensibile a quell'ambiguità.

Per esempio:

> “I dati indicano un calo della conversione del 6–9% nel segmento mobile dopo la modifica del checkout. Il pattern è stabile per quattro settimane, ma nello stesso periodo è cambiato anche il mix delle campagne marketing. Non possiamo attribuire interamente il calo al checkout. Un test controllato permetterebbe di separare meglio i due effetti.”

La frase non finge certezza, ma non rinuncia neppure a informare. Specifica che cosa sappiamo, che cosa limita la conclusione e quale informazione aggiuntiva avrebbe valore.

Questo è il criterio che useremo nel resto del libro:

> **L'incertezza va ridotta quando possibile, quantificata quando utile e dichiarata quando non può essere eliminata. Poi va collegata alla decisione che potrebbe cambiare.**

Un sistema generativo può esprimere una spiegazione fragile con grande sicurezza linguistica. La forma del testo non misura l'incertezza epistemica. Proprio per questo, quando l'AI partecipa all'analisi, dovremo mantenere separati fatti osservati, calcoli, assunzioni, ipotesi e interpretazioni, come introdotto nel Capitolo 0 e come approfondiremo nel Capitolo 14.

Nascondere l'incertezza non rende l'analisi più forte.

La rende più fragile nel momento in cui qualcuno deve usarla.

---

### Fonte

[^nist-uncertainty]: NIST, *Concepts, Principles, and Methods for the Assessment of Measurement Uncertainty*. https://www.nist.gov/publications/concepts-principles-and-methods-assessment-measurement-uncertainty
