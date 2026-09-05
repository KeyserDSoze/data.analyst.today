## 0.2 Delegare l'esecuzione, non la responsabilità

L'AI rende possibile separare due cose che per molto tempo sono state quasi inseparabili: **fare materialmente il lavoro** e **rispondere professionalmente del lavoro**. Questa separazione non è un dettaglio organizzativo; è una delle competenze centrali del lavoro AI-native.

Un analista può non scrivere personalmente una query e restare responsabile del numero che quella query produce. Può non addestrare a mano un modello e restare responsabile di come quel modello viene usato. Può non preparare la prima bozza di una presentazione e restare responsabile del messaggio consegnato al management. Per questo la domanda «chi ha premuto i tasti?» diventa sempre meno interessante. La domanda utile è un'altra:

> **Chi è in grado di spiegare, difendere, fermare e correggere il processo?**

Il problema diventa più chiaro se evitiamo due estremi opposti. Da una parte c'è il rifiuto della delega: «se non scrivo io il codice, non mi fido». È una posizione che spreca capacità utile, perché non esiste un merito professionale nel compiere più lentamente un'attività che può essere accelerata senza perdere controllo. Dall'altra c'è la delega del giudizio: «se il modello l'ha detto, sarà giusto». Qui il rischio è maggiore, perché uno strumento di amplificazione viene trasformato in un sostituto dell'ownership.

La posizione professionale sta fra questi due estremi, ma non è un compromesso tiepido. È una regola precisa: **delegare ciò che può essere delegato, mantenendo ownership su obiettivo, assunzioni, evidenze, controlli e decisione**.

### Caso simulato/composito: il report del lunedì

Un'azienda B2B automatizza il weekly business review. Ogni lunedì un agente estrae i KPI, li confronta con forecast e anno precedente, individua anomalie, genera possibili spiegazioni e prepara una slide con raccomandazioni. Per otto settimane il processo funziona bene e proprio questa continuità costruisce fiducia: il report arriva puntuale, le anomalie sembrano sensate, le spiegazioni sono abbastanza utili da entrare nella routine.

Alla nona settimana il report mostra una pipeline coverage in crescita del 22% e expected bookings in aumento del 14%. Da quei numeri l'agente deduce una raccomandazione coerente: aumentare il target del trimestre. Il VP Sales, però, nota un'incongruenza semplice ma importante. Il numero di opportunità aperte non è cresciuto abbastanza da rendere intuitivo quel salto di coverage.

L'indagine ricostruisce allora il dato a monte e scopre che una modifica al CRM ha duplicato il valore di alcune opportunità multi-currency durante il consolidamento. L'agente non aveva inventato un numero e non aveva commesso un errore evidente di logica. Aveva letto correttamente un dato sbagliato e, a partire da quell'input plausibile, aveva costruito una raccomandazione altrettanto plausibile.

È un failure mode più insidioso dell'allucinazione manifesta: **input plausibile → elaborazione plausibile → conclusione plausibile → decisione sbagliata**. Il fatto che il report sia automatico non riduce la necessità di un owner; la aumenta, perché la stessa pipeline può ripetere l'errore con regolarità e autorevolezza.

### Un owner rende il risultato ispezionabile

Ogni output importante dovrebbe avere un owner che non è obbligato a eseguire personalmente ogni passaggio, ma deve conoscere abbastanza il processo da governarlo. Deve sapere da quali sistemi arriva il dato, quale definizione delle metriche viene usata, quali trasformazioni sono critiche e quali controlli devono passare prima della pubblicazione. Deve inoltre conoscere i failure mode già noti, sapere che cosa succede quando un controllo fallisce e avere l'autorità per fermare o correggere il processo.

Senza questa ownership, l'errore può circolare fra sistemi, agenti e report senza che nessuno abbia l'obbligo di comprenderlo. Con un owner, invece, una conclusione importante non termina semplicemente con una frase: resta collegata a un percorso verificabile.

Se un agente afferma che «la Francia è il principale driver del calo», l'analista deve poter vedere la decomposizione del delta. Se sostiene che «la campagna ha causato un aumento delle vendite», deve essere possibile ricostruire il disegno causale e capire quali alternative siano state escluse. Se dichiara che «il modello è migliorato», servono baseline, split, metriche e risultati fuori campione.

Le evidenze cambiano con il tipo di lavoro, ma la logica resta la stessa. Query e trasformazioni rendono ispezionabile l'implementazione; filtri, popolazioni e definizioni metriche rendono ispezionabile la semantica; sorgenti, conteggi e reconciliation aiutano a controllare la rappresentazione del dato; test e grafici diagnostici mettono sotto pressione il comportamento del sistema; ipotesi alternative e limiti conosciuti impediscono di confondere una spiegazione comoda con una conclusione dimostrata. Non significa mostrare tutto a tutti. Significa poter risalire dal risultato alle evidenze che lo sostengono quando la decisione lo richiede.

Un disclaimer non crea questa accountability. Scrivere sotto un report «Output generato dall'AI. Verificare prima dell'uso» può essere utile per comunicare la natura dell'output, ma non sostituisce un processo di review se quel report viene davvero usato per prendere decisioni. Una nota a piè di pagina non può assumersi la responsabilità al posto di una persona o di un processo.

La profondità dell'ownership deve infine seguire il rischio. Più un'azione è costosa, irreversibile, visibile esternamente o impattante su persone, denaro e compliance, più l'owner deve richiedere evidenze forti e approvazioni esplicite. Nei task a basso rischio la review può essere leggera; nei processi critici deve entrare nel design stesso del workflow.

> **La capacità dell'AI modifica chi esegue il lavoro. Non cancella la necessità di sapere chi ne risponde.**
