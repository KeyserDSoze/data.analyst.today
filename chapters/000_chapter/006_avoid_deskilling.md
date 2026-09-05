## 0.5 Evitare il deskilling: usare l'AI senza perdere la capacità di pensare

L'AI può renderci più capaci e, nello stesso tempo, più fragili. Le due cose non si escludono. Se deleghiamo progressivamente ogni passaggio senza mantenere comprensione dei principi, aumentiamo l'output ma rischiamo il **deskilling**: perdiamo proprio le competenze che ci servono per riconoscere, correggere e governare gli errori del sistema che utilizziamo.

Non è nostalgia per il lavoro manuale. È un problema di resilienza professionale. La domanda non è quante attività siamo ancora in grado di eseguire senza assistenza, ma se conserviamo abbastanza comprensione da accorgerci quando l'assistenza sta producendo qualcosa di plausibile e sbagliato.

### Produttività apparente, dipendenza reale

Immaginiamo un analyst junior che usa l'AI per scrivere SQL, interpretare errori, scegliere statistiche, selezionare grafici, costruire modelli e formulare conclusioni. Può produrre molto più output di un analyst di qualche anno prima e, finché i casi sono ordinari, questa accelerazione può sembrare indistinguibile da un aumento di competenza.

La differenza emerge quando l'output smette di essere palesemente errato e diventa soltanto sospetto. Un join many-to-many può duplicare la revenue lasciando una query perfettamente eseguibile. Una variabile disponibile soltanto dopo l'evento target può migliorare artificialmente le performance di un modello. Un intervallo di confidenza può essere calcolato correttamente e interpretato male. Una correlazione può essere forte e tuttavia non sostenere la spiegazione causale proposta.

Per riconoscere questi problemi non basta sapere chiedere all'AI «controlla se è giusto». Serve un modello mentale che permetta di formulare la domanda successiva. Se quel modello manca, la velocità non elimina la dipendenza: la nasconde.

### Quali competenze possono cambiare e quali devono restare

Evitare il deskilling non significa continuare a fare tutto manualmente. Alcune abilità possono perdere valore relativo proprio perché l'AI le rende economiche: ricordare la sintassi esatta di ogni funzione, memorizzare tutti i parametri di una libreria, scrivere boilerplate da zero o ricostruire a mano attività meccaniche che un sistema svolge bene e in modo verificabile.

Questo libera spazio per competenze che diventano più importanti quando l'esecuzione è facile. Grain e cardinalità permettono di capire che cosa rappresenta una riga e come un join può alterare il fenomeno misurato. La semantica delle metriche protegge da numeri formalmente corretti ma concettualmente sbagliati. Probabilità, incertezza, causalità, temporalità e design sperimentale servono a distinguere una storia plausibile da un'inferenza sostenibile. Validazione e business understanding collegano il metodo al contesto, mentre la capacità di leggere query e codice permette di ispezionare ciò che abbiamo delegato senza doverlo produrre da zero.

L'obiettivo non è sapere tutto a memoria. È **possedere abbastanza fondamenta da poter giudicare ciò che viene delegato**.

### Caso simulato/composito: la senior che non scrive più SQL

Una responsabile analytics coordina un team e usa agenti per generare quasi tutte le query operative. Non scrive SQL da mesi. Durante un'analisi pricing, un agente produce una tabella che mostra il margine medio per categoria e conclude che una categoria a basso prezzo ha il margine percentuale più alto.

La manager non ripete l'analisi dall'inizio, ma nota che il margine assoluto non riconcilia con Finance. Questa incongruenza è sufficiente per cambiare il livello di fiducia nell'output. Apre la query e individua rapidamente il problema: il join con una tabella di promozioni è many-to-many e duplica alcune righe.

Non aveva scritto la query, ma aveva conservato quattro capacità che rendono utile la delega: sapeva leggere SQL, ragionare sul grain, riconoscere una reconciliation impossibile e formulare un test capace di spiegare l'anomalia. Sapeva anche tradurre il difetto tecnico nella conseguenza analitica: quel margine non era affidabile perché il dataset aveva alterato la molteplicità delle osservazioni.

Questa è la differenza tra delega e deskilling.

### Essere “manual enough to understand”

Per una competenza importante non è necessario eseguire ogni volta tutto a mano. Dovremmo però essere ancora in grado di spiegare il principio, riconoscere gli errori tipici, formulare un controllo, leggere l'implementazione generata e intervenire quando il sistema fallisce. Non serve diventare i migliori programmatori, statistici o data engineer del team; serve evitare di diventare incapaci di distinguere un sistema sano da uno rotto.

L'AI può aiutarci anche a mantenere questa capacità, se la usiamo come sparring partner invece che come sostituto immediato del ragionamento. Possiamo chiederle di farci domande per verificare se abbiamo capito un modello, di indicare dove il nostro ragionamento è debole senza fornire subito la soluzione, di proporre un controesempio, di fare code review lasciando a noi la correzione o di esplicitare un'assunzione che stiamo dando per scontata. Possiamo anche formulare prima una previsione qualitativa — che segno ci aspettiamo, quale ordine di grandezza, quale segmento dovrebbe cambiare — e confrontarla poi con il risultato calcolato.

La stessa tecnologia che può sostituire passivamente un'attività può quindi rendere l'apprendimento più attivo. La differenza dipende dal modo in cui la inseriamo nel processo.

Per le competenze fondamentali conviene inoltre conservare una quota di pratica deliberata. Formulare ipotesi prima di chiederne altre all'agente, ricostruire periodicamente una metrica critica, fare una prima code review senza assistenza o spiegare un concetto statistico con parole proprie non significa riportare il lavoro quotidiano all'epoca pre-AI. Significa esercitare le capacità che useremo proprio nei momenti in cui l'automazione non sarà sufficiente.

Il Capitolo 19 tornerà sul tema dal punto di vista della carriera e dell'apprendimento nel lungo periodo. Qui ci basta fissare il principio operativo:

> **Possiamo delegare la produzione, ma dobbiamo preservare le competenze che ci permettono di accorgerci quando la produzione sta andando nella direzione sbagliata.**

Il test più semplice resta una domanda: «Perché pensi che questo risultato sia corretto?». Se l'unica risposta disponibile è «perché l'AI lo ha prodotto», abbiamo ceduto il timone.
