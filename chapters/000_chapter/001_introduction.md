# Capitolo 0 — Al timone

> **Nota editoriale sui casi del libro.** In queste pagine distingueremo sempre tra **casi reali documentati** e **casi simulati/compositi**. I primi riguardano organizzazioni, eventi o pratiche sostenuti da fonti pubbliche attendibili, indicate quando rilevanti. I secondi sono costruiti a fini didattici: nomi, numeri e circostanze possono essere inventati o combinare dinamiche plausibili osservabili nel lavoro reale. Un'azienda fittizia va quindi letta come caso simulato/composito, non come cronaca di un evento realmente accaduto.

## L'AI può fare il lavoro. La responsabilità resta tua.

Immaginiamo che un dashboard presenti un errore importante. Una metrica è sbagliata, il management ha già visto il numero e qualcuno chiede all'analista che cosa sia successo. Dire «ho sbagliato un join» non è una buona notizia, ma almeno identifica un errore che può essere ricostruito, corretto e spiegato. La risposta davvero pericolosa è un'altra: «Boh, l'ha fatto l'AI».

In quella frase c'è quasi tutto il problema professionale che questo capitolo vuole affrontare. Non perché usare l'AI sia sbagliato. Al contrario, l'AI può rendere un analista molto più capace: può esplorare schemi dati, generare SQL e Python, cercare anomalie, controllare la data quality, proporre ipotesi, costruire forecast, preparare grafici, leggere documentazione e produrre una prima sintesi per il management. Può anche distribuire queste attività fra più agenti specializzati e farle procedere in parallelo. Il punto, quindi, non è quanto lavoro possa essere delegato, ma **chi sta guidando il processo mentre quel lavoro viene eseguito**.

Se davanti a un bug non sappiamo spiegare che cosa il sistema stava cercando di fare, quali dati ha usato, quali assunzioni ha introdotto e quali controlli erano previsti, non abbiamo delegato soltanto l'esecuzione. Abbiamo delegato anche la comprensione. Ed è in quel momento che abbiamo ceduto il timone.

### Il lavoro cambia forma

Per gran parte della storia dell'analisi dati, essere bravi ha significato anche saper eseguire personalmente una grande quantità di attività: scrivere query, pulire file, costruire formule, cercare errori, preparare grafici, programmare, leggere documentazione, creare presentazioni. L'AI rende molte di queste attività più economiche e veloci. Questo non rende irrilevante l'analista; sposta il punto in cui si concentra il suo valore.

Quando l'esecuzione diventa abbondante, la scarsità si trasferisce altrove. Diventa più importante capire quale decisione stiamo cercando di migliorare, trasformarla nella domanda analitica corretta e scegliere dati che rappresentino davvero il fenomeno. Occorre stabilire quali metriche e assunzioni useremo, quale metodo sia adeguato, quali controlli siano sufficienti per il rischio in gioco e quale evidenza distingua una spiegazione soltanto plausibile da una credibile. Infine bisogna decidere quando l'analisi è abbastanza solida da sostenere un'azione e quando, invece, il sistema deve fermarsi e chiedere più informazioni.

La competenza si sposta così dall'**eseguire tutto personalmente** al **governare un sistema capace di eseguire molto più di quanto una singola persona potrebbe fare**. È un cambiamento di ruolo prima ancora che di strumenti.

### Il nuovo standard professionale

Se un agente genera una query che duplica la revenue, il fatto che non abbiamo scritto personalmente il `JOIN` non elimina la nostra responsabilità sul numero consegnato. Se un modello generato con l'AI contiene leakage, non diventa accettabile perché il training è stato automatico. Se un sistema suggerisce di cambiare un prezzo, bloccare una campagna o intervenire su clienti ad alto rischio, dobbiamo sapere quale evidenza sostiene quella raccomandazione, quali alternative sono state considerate e quali condizioni renderebbero prudente non agire.

Il nuovo standard professionale non può quindi ridursi né a «l'ho fatto io» né a «l'ha fatto l'AI». Deve diventare qualcosa di più esigente:

> **“Posso spiegare come è stato prodotto, quali controlli abbiamo eseguito, dove potrebbe sbagliare e perché ritengo il risultato sufficientemente affidabile per questa decisione.”**

Questo non significa conoscere ogni token generato o rifare ogni passaggio a mano. Significa conoscere abbastanza bene obiettivo, dati, metodo, controlli e rischi da poter dirigere il sistema e intervenire quando qualcosa non torna.

L'AI, infatti, non amplifica soltanto la capacità produttiva. Amplifica anche la scala alla quale un errore può propagarsi. Un analista umano può produrre poche query sbagliate in una giornata; un sistema agentico può produrne centinaia. Naturalmente può produrre anche centinaia di query corrette. Proprio per questo la velocità, da sola, smette di essere una misura sufficiente della produttività. La metrica utile diventa **più output utile e affidabile per unità di tempo**, perché quando il costo dell'esecuzione diminuisce acquistano valore la semantica, la verifica e il giudizio.

> **La velocità senza supervisione non è produttività. È capacità di produrre errori più velocemente.**

### La catena che useremo nel resto del libro

Nel lavoro AI-native non ci interessa un processo che somigli a **Prompt → Output → Copia e incolla**. Ci interessa una catena diversa:

**Intento → Delega → Osservazione → Verifica → Critica → Decisione → Responsabilità**

Ogni passaggio risponde a una domanda che il semplice prompt non risolve. L'intento chiarisce il problema; la delega assegna un mandato; l'osservazione rende visibile ciò che il sistema sta facendo; la verifica mette alla prova dati e metodo; la critica cerca spiegazioni rivali e failure mode; la decisione collega l'evidenza a un'azione; la responsabilità mantiene un owner umano del risultato.

Le sezioni che seguono trasformano questa idea in un metodo operativo. Vedremo come dirigere più agenti senza creare una catena di consenso, come verificare senza rifare tutto, come definire limiti e stop condition, come evitare che la delega diventi deskilling e come scegliere quanta autonomia concedere. Il principio, però, viene prima di tutto il resto:

> **L'AI può lavorare per noi. Al timone restiamo noi.**
