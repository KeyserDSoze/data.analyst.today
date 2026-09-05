## 1.17 Sintesi ed esercizi

Il capitolo è partito da un'apparente contraddizione. Gli strumenti dell'analisi cambiano a grande velocità, e l'AI sta accelerando ulteriormente questa trasformazione; eppure il nucleo del lavoro continua a ruotare attorno a problemi molto più stabili.

Un Data Analyst moderno deve saper usare fogli elettronici, SQL, Python, BI, cloud e AI quando sono gli strumenti adatti. Ma il suo valore non coincide con nessuno di essi. Si manifesta nella capacità di trasformare una richiesta vaga in una domanda verificabile, capire che cosa i dati rappresentano e che cosa lasciano fuori, definire metriche coerenti con la decisione, scegliere confronti e metodi proporzionati, distinguere pattern da cause e rendere l'incertezza utilizzabile.

Il filo che collega questi passaggi è la catena che useremo nel resto del libro:

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**

Non è una pipeline lineare. È un sistema di controllo del significato. Se un passaggio rivela un problema, possiamo tornare indietro; se un'azione è reversibile, possiamo usarla per produrre nuova evidenza; se la misura non rappresenta bene il fenomeno, nessuna sofisticazione successiva può recuperare automaticamente ciò che abbiamo perso a monte.

L'AI modifica soprattutto il costo con cui possiamo attraversare questa catena. Può ampliare le alternative e accelerare l'execution. Non riduce da sola il costo di una decisione sbagliata e non elimina la necessità di sapere quale evidenza siamo disposti a credere.

Gli esercizi seguenti servono quindi meno a verificare memoria e più ad allenare i passaggi in cui il significato può rompersi.

### 1.17.1 Esercizio 1 — Trasformare una richiesta

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

L'obiettivo non è trovare la formulazione “corretta” in assoluto, ma mostrare come decisioni diverse generino domande e misure diverse.

### 1.17.2 Esercizio 2 — Definire una metrica

Definisci formalmente “cliente attivo”.

Crea almeno quattro definizioni alternative, per esempio:

- login negli ultimi 30 giorni;
- acquisto negli ultimi 90 giorni;
- almeno un ordine negli ultimi 12 mesi;
- abbonamento non cancellato.

Per ogni definizione indica:

- un business in cui avrebbe senso;
- casi che classificherebbe diversamente dalle altre;
- una decisione per cui sarebbe inadatta.

Chiudi l'esercizio scegliendo una definizione e scrivendo il suo mini contratto semantico: popolazione, data di riferimento, esclusioni e owner.

### 1.17.3 Esercizio 3 — Dato e realtà

Scegli un concetto non direttamente osservabile, come soddisfazione, engagement, produttività o qualità.

Individua almeno quattro proxy possibili. Per ciascuno chiediti che cosa catturi bene, quale parte del fenomeno lasci invisibile, quale comportamento potrebbe incentivare se diventasse un KPI e in quale situazione produrrebbe una conclusione fuorviante.

Poi indica quale combinazione di proxy useresti per una decisione reale e perché nessuno, preso da solo, sarebbe sufficiente.

### 1.17.4 Esercizio 4 — Scomporre un problema

Una piattaforma SaaS registra un calo del 12% dei ricavi mensili.

Costruisci un issue tree con almeno tre livelli.

Puoi partire da:

**Ricavi = clienti paganti × ricavo medio per cliente**

Continua a scomporre le componenti fino ad arrivare a variabili osservabili o ipotesi verificabili. Prima di proporre una causa, indica quali rami dell'albero spieghino effettivamente il delta e quali possano essere deprioritizzati.

### 1.17.5 Esercizio 5 — Correlazione non significa causa

Scopri che gli utenti che utilizzano una certa funzionalità hanno retention doppia rispetto agli altri.

Elenca almeno cinque spiegazioni compatibili con il pattern senza assumere che la funzionalità causi retention.

Poi indica:

- quali dati aggiuntivi cercheresti;
- quale ordine temporale controlleresti;
- quale meccanismo di selezione potrebbe distorcere il confronto;
- quale esperimento o disegno osservazionale produrrebbe evidenza più forte.

Chiudi scrivendo due frasi: una consentita dai soli dati osservazionali e una che potresti usare soltanto dopo avere ottenuto evidenza causale adeguata.

### 1.17.6 Esercizio 6 — L'incertezza cambia la decisione

Hai due progetti:

- **Progetto A:** beneficio atteso elevato, test poco costoso e facilmente reversibile;
- **Progetto B:** beneficio simile, ma implementazione costosa e difficile da invertire.

Per entrambi l'evidenza iniziale suggerisce una probabilità del 60% di successo.

Spiega perché la stessa probabilità può giustificare decisioni diverse. Indica quale errore sia più costoso nei due casi, quali informazioni aggiuntive abbiano maggiore valore e se sia preferibile agire, sperimentare o raccogliere altra evidenza prima della decisione.

### 1.17.7 Esercizio 7 — Analisi assistita da AI

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

L'esercizio non misura quanta parte del lavoro hai delegato. Misura se, alla fine, sai ricostruire perché la conclusione meriti fiducia.

### 1.17.8 Esercizio 8 — Il memo decisionale

Scrivi una pagina che contenga soltanto:

- decisione da prendere;
- evidenza disponibile;
- evidenza mancante;
- principali rischi di interpretazione;
- raccomandazione;
- misura con cui valuterai il risultato dopo l'azione.

Non inserire grafici se non sono necessari alla decisione.

L'esercizio serve a ricordare che il prodotto finale dell'analisi non è necessariamente un dashboard. Spesso è una scelta meglio informata e un modo chiaro per sapere, dopo, se quella scelta ha funzionato.

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

Abbiamo definito il mestiere prima di entrare nei suoi strumenti. Il passaggio successivo è rendere operativo il primo anello della catena: trasformare una richiesta in un problema ben inquadrato, con decisione, stakeholder, perimetro, metriche e criteri di successo espliciti.

È ciò che farà il Capitolo 2.

Da qui in avanti ogni tecnologia verrà valutata con la stessa domanda:

> **Quale problema risolve, quale evidenza produce, quali assunzioni introduce e quando è lo strumento giusto?**

È questa disciplina, più di qualsiasi software, a definire il mestiere dell'analista.
