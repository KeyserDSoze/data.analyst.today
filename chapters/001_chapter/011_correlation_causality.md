## 1.10 Correlazione, causalità e spiegazioni plausibili

Uno dei compiti più delicati dell'analista è impedire che un pattern interessante diventi, attraverso il linguaggio, una spiegazione più forte di quanto i dati permettano.

Possiamo osservare che due fenomeni si muovono insieme. Possiamo stimare quanto sia stabile la loro associazione. In condizioni più forti possiamo provare a sostenere che intervenire su uno dei due modificherebbe l'altro.

Sono tre livelli diversi di affermazione. Il passaggio dall'uno all'altro richiede nuova evidenza, non soltanto una frase più sicura.

### Dall'associazione all'intervento c'è un controfattuale

Supponiamo di osservare che i clienti che utilizzano frequentemente una funzione dell'app hanno retention più alta.

È naturale trasformare il pattern in una raccomandazione: spingiamo più utenti a usare quella funzione e la retention aumenterà. Ma la conclusione contiene una domanda che il semplice confronto non ha ancora risolto: **che cosa sarebbe successo agli stessi utenti se il loro uso della funzione fosse stato diverso?**

Gli utenti più coinvolti potrebbero essere contemporaneamente più propensi a usare la funzione e a rimanere clienti. La funzione potrebbe essere disponibile soprattutto sui piani premium. L'anzianità potrebbe influenzare sia l'utilizzo sia la retention. Oppure la direzione potrebbe essere inversa: utenti che stanno già perdendo interesse riducono l'uso di molte funzioni prima di abbandonare.

In tutti questi scenari l'associazione osservata può essere autentica. È l'interpretazione causale a cambiare.

Questo è il punto centrale: **un pattern può essere vero e la storia che gli costruiamo intorno può essere falsa.**

### Confondimento: quando una terza variabile costruisce la relazione

Immaginiamo di scoprire che i clienti contattati più spesso dal team commerciale acquistano di più. Potremmo concludere che aumentare il numero di chiamate farà crescere le vendite.

Ma il team potrebbe scegliere di chiamare più spesso proprio i clienti che considera più promettenti. Il potenziale commerciale influenza allora sia l'esposizione — il numero di chiamate — sia l'outcome — gli acquisti. Se non lo consideriamo, attribuiamo alle chiamate almeno una parte dell'effetto della selezione iniziale.

Questo è il problema del **confondimento**: una variabile rende gruppi apparentemente confrontabili diversi proprio su una dimensione che influenza l'esito.

Un modello statistico può controllare confondenti osservati e misurati bene. Non può garantire che non esistano variabili importanti che non abbiamo osservato, misurato o rappresentato correttamente. Per questo la sofisticazione del modello non sostituisce il ragionamento sul processo che ha generato i dati.

### Selezione: il dataset può aver già escluso la parte che ci serviva

Un'altra fonte di errore nasce prima dell'analisi. Se studiamo soltanto utenti ancora attivi per capire quali funzionalità “creano retention”, abbiamo rimosso proprio le persone che hanno abbandonato. Se analizziamo soltanto campagne considerate di successo, non sappiamo se le stesse caratteristiche fossero presenti anche nelle campagne fallite.

La domanda non è soltanto se il campione sia grande. È **per quale meccanismo una persona, un evento o un esperimento è entrato nel dataset che stiamo osservando**.

Se quel meccanismo dipende dall'esposizione o dall'outcome, il confronto può essere distorto anche con milioni di righe.

### La sequenza temporale elimina alcune storie, non tutte

Una causa deve precedere il proprio effetto. Sembra una regola banale, ma i dati aggregati la nascondono facilmente.

Se i clienti che aprono molti ticket hanno churn elevato, il supporto sta causando l'abbandono oppure problemi già presenti generano sia ticket sia churn? Se le aziende con più Data Analyst prendono più decisioni data-driven, sono gli analyst a cambiare la cultura o sono le aziende già data-driven ad assumere più analyst?

Ricostruire la sequenza temporale può eliminare spiegazioni impossibili e rendere altre più plausibili. Ma l'ordine temporale, da solo, non basta a dimostrare causalità: due eventi possono susseguirsi perché entrambi sono prodotti da una terza causa.

La temporalità è quindi una condizione necessaria per molte storie causali, non una prova sufficiente.

### Evidenza causale più forte significa progettare confronti più credibili

Quando possiamo randomizzare, costruiamo gruppi comparabili prima del trattamento e rendiamo molto più difficile che la selezione iniziale spieghi la differenza osservata. È uno dei motivi per cui gli esperimenti controllati sono così potenti.

Ma un A/B test non è automaticamente valido. Randomizzazione, exposure, durata, interferenze, metriche e modalità di analisi possono fallire. Il **Capitolo 9** sarà dedicato proprio alla sperimentazione nel mondo reale.

Quando non possiamo randomizzare, il problema non scompare: dobbiamo costruire il controfattuale usando disegni osservazionali o quasi-sperimentali e rendere esplicite le assunzioni che li sostengono. Il **Capitolo 8** entrerà in matching, regression discontinuity, variabili strumentali e altri approcci.

Per ora basta fissare una regola:

> **un modello più sofisticato non trasforma automaticamente un'associazione in causalità; è il disegno del confronto a rendere credibile la promessa controfattuale.**

### Cercare spiegazioni rivali è parte dell'analisi

Supponiamo che il fatturato cresca subito dopo una campagna marketing. Una narrazione coerente è disponibile in pochi secondi: la campagna ha funzionato.

Il lavoro analitico comincia proprio quando la storia sembra facile. Nello stesso periodo potrebbe essere iniziata una promozione, potrebbe essere cambiata la stagionalità, potrebbero essere aumentati i prezzi o essere entrati nuovi mercati. Il tracking potrebbe essere cambiato oppure il periodo usato come confronto potrebbe essere stato anomalo.

Non serve produrre un catalogo infinito di dubbi. Serve chiedersi quale osservazione distinguerebbe davvero le storie concorrenti. Se la crescita compare soltanto tra gli esposti alla campagna ma non in gruppi comparabili, una parte delle alternative perde forza. Se precede l'avvio della campagna, la storia principale deve essere rivista.

L'obiettivo non è accumulare spiegazioni plausibili. È **ridurre progressivamente lo spazio di quelle compatibili con l'evidenza**.

### Il linguaggio deve conservare la forza del metodo

Un'analisi osservazionale può sostenere:

> “Gli utenti che utilizzano la funzione X mostrano retention maggiore, anche dopo aver controllato alcune caratteristiche osservabili.”

È una frase informativa. Ma è diversa da:

> “La funzione X aumenta la retention.”

La seconda frase promette che, se intervenissimo su X, cambierebbe Y. Per dirlo dobbiamo avere un disegno capace di sostenere quella promessa.

Una breve audit trail prima di formulare una conclusione causale può quindi chiedere:

1. il pattern è abbastanza stabile da non sembrare soltanto rumore?
2. la sequenza temporale è compatibile con la storia proposta?
3. quali confondenti o meccanismi di selezione potrebbero produrre lo stesso pattern?
4. esiste una direzione causale inversa plausibile?
5. quale osservazione, esperimento o quasi-esperimento distinguerebbe meglio le spiegazioni rivali?

I sistemi generativi sono molto bravi a trasformare pattern in storie fluide. Proprio per questo la competenza rara non è produrre una spiegazione plausibile.

È capire **quale spiegazione meriti più fiducia e quale linguaggio siamo autorizzati a usare per descriverla**.
