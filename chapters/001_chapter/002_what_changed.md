## 1.1 Cosa è cambiato davvero

Per capire il ruolo del Data Analyst nell'era dell'AI conviene separare due cose che spesso vengono confuse: **il lavoro analitico** e **il modo in cui quel lavoro viene eseguito**.

Il primo riguarda problemi, evidenze, interpretazioni e decisioni. Il secondo riguarda interfacce, linguaggi, strumenti, automazioni e infrastruttura. Il lavoro analitico evolve, ma lentamente; il modo di eseguirlo può cambiare nel giro di pochi anni, a volte di pochi mesi.

Per molto tempo una parte importante del vantaggio tecnico di un analista è dipesa dalla capacità di svolgere attività che richiedevano conoscenze operative specifiche: scrivere SQL, costruire formule e misure DAX, trasformare dati, programmare, configurare dashboard, conoscere le particolarità di strumenti diversi. Queste competenze non diventano inutili. Cambia però il loro peso relativo, perché il costo di ottenere una prima implementazione si sta abbassando.

Questo spostamento produce almeno quattro conseguenze.

### Dalla sintassi all'intento

Per interrogare un database serviva conoscere SQL. Per automatizzare un'analisi serviva Python o R. Per costruire determinate metriche in Power BI serviva DAX. Per trasformare un foglio elettronico bisognava conoscere formule, pivot, Power Query o macro.

L'AI generativa introduce un'altra possibilità: esprimere l'intento in linguaggio naturale e lasciare che un sistema traduca parte di quell'intento in codice o operazioni.

Possiamo chiedere, per esempio:

> “Calcola il fatturato mensile per categoria, confrontalo con lo stesso mese dell'anno precedente e segnala le categorie con una diminuzione superiore al 15%.”

Il sistema può produrre SQL, Python, DAX o una sequenza di trasformazioni. Il lavoro si sposta quindi in parte da *come scrivo questa istruzione?* a *che cosa sto davvero chiedendo e come verifico che l'implementazione corrisponda all'intento?*

La seconda domanda è meno meccanica della prima. “Fatturato” può significare lordo o netto, includere o escludere resi, dipendere dalla data dell'ordine o da quella di contabilizzazione, richiedere conversioni valutarie e diventare non confrontabile se nel frattempo è cambiato il perimetro aziendale. Un sistema può generare codice perfettamente valido prima che queste decisioni siano state prese.

L'AI riduce quindi il costo della traduzione tra intento e implementazione. **Non definisce automaticamente l'intento corretto.**

### Iterare costa meno, scegliere costa relativamente di più

Quando una query, un grafico o uno script richiedono meno tempo, possiamo esplorare ipotesi che in passato avremmo scartato per ragioni di costo. Una spiegazione secondaria può essere controllata; due definizioni alternative possono essere confrontate; un sanity check può essere costruito quasi senza attrito; una visualizzazione poco convincente può essere sostituita rapidamente.

Il beneficio non è soltanto fare prima la stessa analisi. È poter lavorare in modo più iterativo.

Ma l'abbondanza ha un effetto collaterale. Se produrre dieci alternative diventa economico, non diventa automaticamente economico valutarle tutte con la stessa profondità. Il nuovo collo di bottiglia si sposta verso priorità, semantica, verifica e capacità di fermarsi quando l'evidenza è sufficiente.

Il Capitolo 0 ha affrontato questo problema dal punto di vista della supervisione. Qui ci interessa la conseguenza economica: **quando l'esecuzione diventa abbondante, il giudizio diventa relativamente più scarso e quindi più prezioso.**

### I confini tra ruoli diventano più permeabili

In molte organizzazioni il percorso del lavoro era scandito da passaggi relativamente netti: richiesta di business, analyst, data engineer, BI developer, report. Le specializzazioni continuano a essere necessarie, soprattutto quando aumentano scala, affidabilità e rischio, ma attraversarne i confini costa meno.

Un analista può prototipare codice che prima avrebbe richiesto l'intervento immediato di uno sviluppatore. Un business user può interrogare in linguaggio naturale un modello semantico. Un data engineer può produrre documentazione o analisi esplorative più rapidamente. Un data scientist può costruire una prima visualizzazione senza attendere un passaggio di consegne.

Questa permeabilità non rende tutti specialisti di tutto. Al contrario, aumenta il valore di chi possiede una visione abbastanza ampia da riconoscere dove termina la propria autonomia. Un prototipo generato velocemente può essere sufficiente per un'esplorazione e completamente inadeguato per un processo che alimenta decisioni finanziarie ogni mattina.

La competenza trasversale diventa quindi saper seguire il percorso end-to-end e capire **quando procedere, quando verificare e quando coinvolgere una competenza specialistica**.

### La semantica diventa infrastruttura

Il cambiamento meno spettacolare è forse il più profondo. Il significato dei dati viene formalizzato sempre di più dentro i sistemi analitici: metriche, relazioni, descrizioni, sinonimi, regole di business e istruzioni possono vivere in semantic layer e modelli condivisi invece di restare soltanto nella testa degli analisti o in documenti separati.

L'AI rende questa formalizzazione ancora più importante. Microsoft, nella documentazione dedicata alla preparazione dei semantic model di Power BI per Copilot, raccomanda di restringere lo schema ai campi rilevanti e di fornire terminologia e istruzioni di business per ridurre l'ambiguità.[^ms-ai-schema][^ms-ai-faq]

La dinamica generale è semplice:

> **quando l'interfaccia diventa più semplice, il modello semantico sottostante deve diventare più rigoroso.**

Se l'utente non deve conoscere il nome esatto della tabella o della misura, qualcuno — o qualcosa — deve comunque sapere con precisione che cosa significano “revenue”, “cliente attivo” o “retention”. La complessità non scompare; una parte viene trasferita dal gesto dell'utente alla qualità del sistema che interpreta la richiesta.

### Che cosa cambia, quindi, per l'analista?

La competenza tecnica non scompare: cambia funzione.

Studiamo SQL non soltanto per ricordare come si scrive una `JOIN`, ma per capire grain, cardinalità, aggregazioni e duplicazioni. Studiamo statistica non per ripetere formule che un software può calcolare, ma per sapere quale conclusione è giustificata dall'evidenza. Studiamo visualizzazione non per aumentare il numero di grafici prodotti, ma per riconoscere quali rappresentazioni chiariscono un fenomeno e quali lo deformano. Studiamo architettura non perché ogni analista debba amministrare un warehouse, ma perché raccolta, trasformazione e modellazione determinano ciò che sarà possibile osservare dopo.

Il premio per la pura esecuzione diminuisce. **Aumenta il premio per il giudizio informato sull'esecuzione.**

La sezione successiva affronta l'altra metà della tesi: ciò che, nonostante tutti questi cambiamenti, è rimasto sorprendentemente stabile.

---

### Fonti

[^ms-ai-schema]: Microsoft Learn, *Prepare your data for AI - AI data schemas*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-data-schema
[^ms-ai-faq]: Microsoft Learn, *Frequently Asked Questions about Preparing Data for AI - Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq
