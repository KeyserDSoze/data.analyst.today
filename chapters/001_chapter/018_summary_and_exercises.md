## 1.17 Sintesi ed esercizi

Il capitolo ha costruito una tesi semplice ma decisiva: gli strumenti dell'analisi cambiano rapidamente, mentre il nucleo del ragionamento analitico cambia molto meno.

Un Data Analyst moderno deve saper usare fogli elettronici, SQL, Python, BI, cloud e AI quando servono. Ma il suo valore non coincide con nessuno di questi strumenti.

Il lavoro centrale consiste nel trasformare problemi vaghi in domande verificabili, capire che cosa rappresentano i dati, scegliere metriche e confronti coerenti, usare un metodo proporzionato, interpretare l'evidenza senza andare oltre ciò che sostiene e collegarla a decisioni di cui possiamo misurare l'effetto.

### 1.17.1 Idee chiave da ricordare

- Una richiesta di business non è ancora una domanda analitica.
- I dati sono rappresentazioni prodotte da sistemi, non la realtà stessa.
- Una metrica è una definizione, non un fatto naturale.
- Descrivere, diagnosticare, prevedere, stimare un effetto causale e scegliere un'azione sono problemi diversi.
- Una relazione osservata non implica automaticamente causalità.
- L'incertezza va resa utilizzabile, non nascosta.
- L'AI riduce il costo dell'execution, non il costo di una decisione sbagliata.
- Il valore dell'analisi emerge lungo la catena tra problema, evidenza e decisione.
- Dopo l'azione, la misurazione genera nuova evidenza.

La formula di riferimento è:

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**

### 1.17.2 Esercizio 1 — Trasformare una richiesta

Parti dalla frase:

> “I clienti non sono più soddisfatti.”

Scrivi almeno dieci domande che dovresti porre prima di analizzare dati.

Poi costruisci tre formulazioni analitiche diverse, specificando per ciascuna:

- tipo di domanda;
- metrica;
- popolazione;
- periodo;
- baseline;
- decisione o incertezza associata.

### 1.17.3 Esercizio 2 — Definire una metrica

Definisci formalmente “cliente attivo”.

Crea almeno quattro definizioni alternative, per esempio:

- login negli ultimi 30 giorni;
- acquisto negli ultimi 90 giorni;
- almeno un ordine negli ultimi 12 mesi;
- abbonamento non cancellato.

Per ogni definizione indica:

- business in cui avrebbe senso;
- casi che classificherebbe diversamente;
- decisione per cui sarebbe inadatta.

### 1.17.4 Esercizio 3 — Dato e realtà

Scegli un concetto non direttamente osservabile, come soddisfazione, engagement, produttività o qualità.

Elenca almeno quattro proxy possibili.

Per ciascuno chiediti:

- che cosa cattura bene?
- che cosa non osserva?
- quale comportamento potrebbe incentivare se diventasse KPI?
- in quale situazione produrrebbe una conclusione fuorviante?

### 1.17.5 Esercizio 4 — Scomporre un problema

Una piattaforma SaaS registra un calo del 12% dei ricavi mensili.

Costruisci un issue tree con almeno tre livelli.

Puoi partire da:

**Ricavi = clienti paganti × ricavo medio per cliente**

Poi continua a scomporre le componenti fino ad arrivare a variabili osservabili o a ipotesi verificabili.

### 1.17.6 Esercizio 5 — Correlazione non significa causa

Scopri che gli utenti che utilizzano una certa funzionalità hanno retention doppia rispetto agli altri.

Elenca almeno cinque spiegazioni compatibili con il pattern senza assumere che la funzionalità causi retention.

Poi indica:

- quali dati aggiuntivi cercheresti;
- quale ordine temporale controlleresti;
- quale esperimento o disegno osservazionale produrrebbe evidenza più forte.

### 1.17.7 Esercizio 6 — L'incertezza cambia la decisione

Hai due progetti:

- Progetto A: beneficio atteso elevato, test poco costoso e facilmente reversibile;
- Progetto B: beneficio simile, ma implementazione costosa e difficile da invertire.

Per entrambi l'evidenza iniziale suggerisce una probabilità del 60% di successo.

Spiega perché la stessa probabilità può giustificare decisioni diverse. Elenca quali informazioni aggiuntive avrebbero maggiore valore nei due casi.

### 1.17.8 Esercizio 7 — Analisi assistita da AI

Prendi un piccolo dataset pubblico e usa un assistente AI per:

1. proporre cinque possibili domande analitiche;
2. scegliere con motivazione una sola domanda;
3. generare codice o query per esplorarla;
4. elencare assunzioni e failure mode;
5. proporre almeno due controlli indipendenti;
6. formulare una conclusione con un livello di certezza esplicito.

Poi verifica manualmente almeno due passaggi critici.

Annota:

- dove l'AI ha ampliato le possibilità;
- dove mancava contesto;
- quale controllo ha avuto più valore;
- se la conclusione finale è diversa dalla prima risposta generata.

### 1.17.9 Esercizio 8 — Il memo decisionale

Scrivi una pagina che contenga soltanto:

- decisione da prendere;
- evidenza disponibile;
- evidenza mancante;
- principali rischi di interpretazione;
- raccomandazione;
- misura con cui valuterai il risultato dopo l'azione.

Non inserire grafici se non sono necessari alla decisione.

L'esercizio serve a ricordare che il prodotto finale dell'analisi non è necessariamente un dashboard. Spesso è una scelta meglio informata.

### Domande di autovalutazione

Alla fine del capitolo dovresti saper rispondere a queste domande:

1. Che cosa è cambiato davvero nel lavoro analitico con gli strumenti moderni e l'AI?
2. Qual è la differenza tra una richiesta di business e una domanda analitica?
3. Perché i dati non coincidono con la realtà?
4. Perché una metrica è una scelta semantica?
5. Qual è la differenza tra domanda descrittiva, diagnostica, predittiva, causale e decisionale?
6. In che modo confondenti, selezione e causalità inversa possono produrre spiegazioni sbagliate?
7. Perché significatività, dimensione dell'effetto e rilevanza decisionale non sono la stessa cosa?
8. Quali parti del lavoro appartengono a execution, analysis e decision intelligence?
9. Quando un'analisi può considerarsi sufficientemente completa per una decisione?
10. Come misureresti ciò che accade dopo l'azione?

### Chiusura del capitolo

Il resto del libro costruirà strumenti sempre più potenti sopra queste fondamenta.

Ogni tecnologia verrà valutata con la stessa domanda:

> **Quale problema risolve, quale evidenza produce, quali assunzioni introduce e quando è lo strumento giusto?**

È questa disciplina, più di qualsiasi software, a definire il mestiere dell'analista.
