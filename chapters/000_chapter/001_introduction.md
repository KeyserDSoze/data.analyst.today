# Capitolo 0 — Al timone

> **Nota editoriale sui casi del libro.** In queste pagine distingueremo sempre tra **casi reali documentati** e **casi simulati/compositi**. I primi riguardano organizzazioni, eventi o pratiche sostenuti da fonti pubbliche attendibili, indicate quando rilevanti. I secondi sono costruiti a fini didattici: nomi, numeri e circostanze possono essere inventati o combinare dinamiche plausibili osservabili nel lavoro reale. Un'azienda fittizia va quindi letta come caso simulato/composito, non come cronaca di un evento realmente accaduto.

## L'AI può fare il lavoro. La responsabilità resta tua.

Immaginiamo che un dashboard presenti un errore importante. Una metrica è sbagliata, il management ha già visto il numero e qualcuno chiede all'analista che cosa sia successo.

La risposta peggiore non è:

> “Ho sbagliato un join.”

La risposta peggiore è:

> “Boh, l'ha fatto l'AI.”

In quella frase c'è quasi tutto il problema professionale che questo capitolo vuole affrontare.

Non perché usare l'AI sia sbagliato. Al contrario: l'AI può rendere un analista molto più capace. Può esplorare schemi dati, generare SQL e Python, cercare anomalie, controllare data quality, proporre ipotesi, costruire forecast, preparare grafici, leggere documentazione e produrre una prima sintesi per il management.

E può farlo non soltanto come singolo assistente, ma attraverso più agenti specializzati che lavorano in parallelo.

Il punto è un altro: **chi sta guidando il processo?**

Se davanti a un bug non sappiamo spiegare che cosa il sistema stava cercando di fare, quali dati ha usato, quali assunzioni ha introdotto e quali controlli erano previsti, non abbiamo davvero delegato un'attività. Abbiamo delegato anche la comprensione.

E quindi, di fatto, il timone.

### Il lavoro cambia forma

Per gran parte della storia dell'analisi dati, essere bravi significava anche saper eseguire personalmente una grande quantità di attività: scrivere query, pulire file, costruire formule, cercare errori, preparare grafici, programmare, leggere documentazione, creare presentazioni.

L'AI rende molte di queste attività più economiche e veloci.

Questo non rende irrilevante l'analista. Sposta il punto in cui si concentra il suo valore.

Quando l'esecuzione diventa abbondante, aumentano l'importanza di domande come:

- qual è la decisione che stiamo cercando di migliorare?
- qual è la domanda analitica corretta?
- quali dati sono adatti a rispondere?
- quali metriche e assunzioni stiamo usando?
- quale metodo distingue una spiegazione plausibile da una credibile?
- quali controlli sono sufficienti per questo livello di rischio?
- quando il sistema può procedere e quando deve fermarsi?
- quale conclusione è abbastanza solida da diventare un'azione?

La competenza si sposta dall'**eseguire tutto personalmente** al **governare un sistema capace di eseguire molto più di quanto una singola persona potrebbe fare**.

### Il nuovo standard professionale

Se un agente genera una query che duplica la revenue, il fatto che non abbiamo scritto personalmente il `JOIN` non elimina la nostra responsabilità sul numero consegnato.

Se un modello generato con l'AI contiene leakage, non diventa accettabile perché il training è stato automatico.

Se un sistema suggerisce di cambiare un prezzo, bloccare una campagna o intervenire su clienti ad alto rischio, dobbiamo sapere quale evidenza sostiene quella raccomandazione e quali alternative sono state escluse.

Il nuovo standard professionale non può essere soltanto:

> “L'ho fatto io.”

Ma nemmeno:

> “L'ha fatto l'AI.”

Deve diventare:

> **“Posso spiegare come è stato prodotto, quali controlli abbiamo eseguito, dove potrebbe sbagliare e perché ritengo il risultato sufficientemente affidabile per questa decisione.”**

Questo non significa conoscere ogni token generato o rifare ogni passaggio a mano. Significa conoscere abbastanza bene obiettivo, dati, metodo, controlli e rischi da poter dirigere il sistema e intervenire quando qualcosa non torna.

### L'AI moltiplica capacità. E può moltiplicare gli errori.

Un analista umano può produrre poche query sbagliate in una giornata. Un sistema agentico può produrne centinaia.

Può anche produrre centinaia di query corrette.

La velocità amplifica entrambe le possibilità.

Per questo la produttività non può essere misurata semplicemente come **più output per unità di tempo**. Deve diventare **più output utile e affidabile per unità di tempo**.

> **La velocità senza supervisione non è produttività. È capacità di produrre errori più velocemente.**

Quando il costo dell'esecuzione tende a diminuire, il costo della verifica, della semantica e del giudizio diventa centrale.

### La catena che useremo nel resto del libro

Nel lavoro AI-native, il processo dovrebbe assomigliare a:

**Intento → Delega → Osservazione → Verifica → Critica → Decisione → Responsabilità**

non a:

**Prompt → Output → Copia e incolla**

Le sezioni che seguono trasformano questa idea in un metodo operativo: come dirigere più agenti, come verificare senza rifare tutto, come definire limiti e stop condition, come evitare il deskilling e come scegliere quanta autonomia concedere.

Il principio, però, viene prima di tutto il resto:

> **L'AI può lavorare per noi. Al timone restiamo noi.**
