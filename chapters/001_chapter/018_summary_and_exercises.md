## 1.17 Sintesi ed esercizi

Il primo capitolo ha introdotto una tesi semplice ma decisiva: gli strumenti dell'analisi cambiano rapidamente, il nucleo del ragionamento analitico molto meno.

Un Data Analyst moderno deve saper usare SQL, Python, fogli elettronici, strumenti di BI, cloud e AI quando servono. Ma il suo valore non coincide con nessuno di questi strumenti.

Il lavoro centrale consiste nel trasformare problemi vaghi in domande precise, scegliere metriche coerenti, comprendere i dati e le loro limitazioni, selezionare un metodo adeguato, interpretare l'evidenza e collegarla a decisioni verificabili.

### 1.17.1 Idee chiave da ricordare

- Una richiesta di business non è ancora una domanda analitica.
- Una metrica è una definizione, non un fatto naturale.
- I dati rappresentano la realtà attraverso sistemi, regole e processi di raccolta.
- Una relazione osservata non implica automaticamente causalità.
- L'incertezza va comunicata, non nascosta.
- L'AI riduce il costo dell'esecuzione ma non elimina il costo dell'errore.
- La semantica dei dati diventa più importante quando l'interazione con i dati diventa più automatizzata.
- Una buona analisi termina con una decisione o con una riduzione concreta dell'incertezza.
- Dopo l'azione bisogna misurare l'effetto.

### 1.17.2 Esercizio 1 — Trasformare una richiesta

Parti dalla frase:

> “I clienti non sono più soddisfatti.”

Scrivi almeno dieci domande che dovresti porre prima di analizzare dati.

Poi trasforma la richiesta in tre possibili domande analitiche misurabili, ciascuna con:

- metrica;
- popolazione;
- periodo;
- baseline;
- decisione associata.

### 1.17.3 Esercizio 2 — Definire una metrica

Definisci formalmente “cliente attivo”.

Crea almeno quattro definizioni alternative, per esempio:

- login negli ultimi 30 giorni;
- acquisto negli ultimi 90 giorni;
- almeno un ordine negli ultimi 12 mesi;
- abbonamento non cancellato.

Descrivi come la scelta della definizione potrebbe cambiare le conclusioni di un'analisi.

### 1.17.4 Esercizio 3 — Scomporre un problema

Una piattaforma SaaS registra un calo del 12% dei ricavi mensili.

Costruisci un issue tree con almeno tre livelli.

Esempio iniziale:

**Ricavi = clienti paganti × ricavo medio per cliente**

Poi continua a scomporre entrambe le componenti.

### 1.17.5 Esercizio 4 — Correlazione non significa causa

Scopri che gli utenti che utilizzano una certa funzionalità hanno una retention doppia rispetto agli altri.

Elenca almeno cinque spiegazioni alternative all'ipotesi “la funzionalità aumenta la retention”.

Progetta quindi un esperimento o un'analisi che possa fornire evidenza causale più forte.

### 1.17.6 Esercizio 5 — Analisi assistita da AI

Prendi un piccolo dataset pubblico.

Chiedi a un assistente AI di:

1. proporre cinque insight;
2. scrivere una query o uno script per verificarli;
3. indicare le assunzioni;
4. proporre spiegazioni alternative.

Successivamente verifica manualmente almeno due risultati.

Annota:

- dove l'AI è stata utile;
- dove ha introdotto ambiguità;
- cosa non avrebbe potuto sapere senza il tuo contesto;
- quali controlli hanno modificato la conclusione iniziale.

### 1.17.7 Esercizio 6 — Il memo decisionale

Scrivi una pagina che contenga soltanto:

- decisione da prendere;
- evidenza disponibile;
- evidenza mancante;
- principali rischi di interpretazione;
- raccomandazione;
- misura con cui valuterai il risultato dopo l'azione.

Non inserire grafici se non sono strettamente necessari.

L'esercizio serve a ricordare che il prodotto finale dell'analisi non è necessariamente una dashboard. Spesso è una decisione meglio informata.

### Domande di autovalutazione

Alla fine del capitolo dovresti essere in grado di rispondere con sicurezza a queste domande:

1. Qual è la differenza tra una richiesta di business e una domanda analitica?
2. Perché una metrica è una scelta semantica?
3. Perché i dati non coincidono con la realtà?
4. Qual è la differenza tra descrivere, diagnosticare, prevedere e stimare un effetto causale?
5. Quali errori può introdurre un confronto temporale ingenuo?
6. Perché l'AI può aumentare contemporaneamente produttività e rischio?
7. Quali parti di un'analisi dovrebbero rimanere riproducibili indipendentemente dall'assistente AI utilizzato?
8. Quando un'analisi può considerarsi conclusa?

### Chiusura del capitolo

Il resto del libro costruirà strumenti sempre più potenti sopra queste fondamenta.

Impareremo SQL, statistica, Python, visualizzazione, modellazione, architetture dati, cloud e AI. Ma ogni tecnologia verrà valutata con la stessa domanda:

> **Quale problema risolve, quale evidenza produce, quali assunzioni introduce e quando è lo strumento giusto?**

È questa domanda, più di qualsiasi software, a definire il mestiere dell'analista.
