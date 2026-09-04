## 1.2 Cosa non è cambiato

Se il modo di eseguire l'analisi cambia rapidamente, conviene chiedersi che cosa rimanga stabile sotto l'interfaccia.

Prendiamo una frase comune:

> “Le vendite stanno diminuendo.”

Possiamo ottenere in pochi secondi un grafico, una query o una decomposizione automatica. Ma la velocità non risolve l'ambiguità contenuta nella frase. Non sappiamo ancora che cosa significhi “vendite”, rispetto a quale baseline stiamo osservando il calo, quale popolazione conti, quale decisione debba essere presa né quali spiegazioni sarebbero compatibili con ciò che osserviamo.

Queste non sono domande preliminari che possiamo saltare grazie a strumenti migliori. **Sono il lavoro che determina che cosa gli strumenti debbano fare.**

### Il problema viene prima dei dati

Una delle tesi fondamentali del libro può sembrare paradossale:

> **L'analisi dei dati non comincia dai dati. Comincia dal problema.**

Un dataset può contenere milioni di righe e tuttavia non dirci quali siano rilevanti, quale qualità sia sufficiente o quale metodo abbia senso applicare. Queste scelte dipendono dall'incertezza che stiamo cercando di ridurre.

Framework sviluppati molto prima dell'AI generativa formalizzano lo stesso principio. In CRISP-DM la prima fase è la **Business Understanding**: chiarire obiettivi, vincoli e criteri di successo prima di investire nelle fasi tecniche.[^ibm-business] Subito dopo arriva la **Data Understanding**, che richiede di esaminare contenuto e qualità dei dati prima della modellazione.[^ibm-data-understanding]

Le due fasi sono separate nel framework, ma nel lavoro reale dialogano continuamente. Una domanda di business può rivelarsi impossibile da osservare con i dati disponibili; un limite del dato può obbligarci a riformulare la domanda; una definizione apparentemente ovvia può cambiare quando scopriamo come il processo operativo registra davvero gli eventi.

Il punto è che il problema guida la ricerca dei dati, mentre i dati pongono limiti a ciò che possiamo affermare sul problema.

### Definizioni e confronti continuano a determinare il significato

Concetti come revenue, cliente attivo, churn, conversione o margine non sono semplicemente nomi di colonne. Sono definizioni. Un calcolo può essere sintatticamente corretto e semanticamente sbagliato: possiamo sommare la colonna giusta usando la data sbagliata, confrontare popolazioni non equivalenti o scegliere un denominatore che rende la metrica inadatta alla decisione.

Anche il confronto introduce significato. Dire che una metrica è alta, bassa, cresciuta o diminuita presuppone una baseline. Mese precedente, anno precedente, forecast, budget, trend storico o gruppo di controllo rispondono a domande diverse. La baseline non è un dettaglio che scegliamo alla fine per costruire il grafico; è parte della formulazione del problema.

Lo stesso vale per i dati. Un database non contiene la realtà: contiene ciò che sistemi e processi sono riusciti o hanno deciso di registrare. Eventi possono mancare, definizioni possono cambiare e trasformazioni apparentemente innocue possono modificare il fenomeno osservato. Per questo la domanda non è soltanto *che cosa dice il dataset?*, ma *come è stato prodotto e quale parte del fenomeno non riesce a rappresentare?*

### L'evidenza non elimina il bisogno di giudizio

Strumenti più potenti possono trovare più pattern. Non trasformano automaticamente quei pattern in spiegazioni.

Due fenomeni possono muoversi insieme perché uno influenza l'altro, perché esiste una causa comune, perché la selezione del campione li rende artificialmente simili o perché stiamo osservando una coincidenza. Allo stesso modo, un forecast può essere preciso senza essere certo e un effetto statisticamente rilevabile può essere troppo piccolo per cambiare una decisione.

Il lavoro dell'analista consiste anche nel calibrare la forza della conclusione alla forza dell'evidenza. A volte potremo descrivere con sicurezza ciò che è accaduto ma non dire perché. A volte avremo una spiegazione plausibile ma non una stima causale. A volte avremo un intervallo ampio ma comunque sufficiente per scegliere un test economico e reversibile.

L'incertezza, quindi, non scompare con l'automazione. Cambia il modo in cui possiamo esplorarla, non la necessità di gestirla.

### La decisione rimane il punto di arrivo

Un'analisi può essere esplorativa o conoscitiva e non produrre immediatamente un'azione. Ma per avere valore deve ridurre un'incertezza rilevante per qualcuno. La domanda professionale non è quanti numeri abbiamo prodotto, bensì quale differenza quei numeri fanno nella comprensione del problema o nella qualità della scelta.

Questo spiega perché gli strumenti possano cambiare radicalmente mentre la responsabilità centrale rimane più stabile:

> **Un analista non viene pagato per produrre numeri. Viene pagato per ridurre l'incertezza in modo sufficientemente affidabile da migliorare una decisione.**

Le sezioni successive smonteranno questa frase pezzo per pezzo: che cosa significa davvero “ridurre incertezza”, che cosa rende un dato una rappresentazione credibile e come si costruisce il percorso che porta da una richiesta vaga a un'evidenza utilizzabile.

---

### Fonti

[^ibm-business]: IBM, *Business Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/it/spss-modeler/19.0.0?topic=understanding-business-overview
[^ibm-data-understanding]: IBM, *Data Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview
