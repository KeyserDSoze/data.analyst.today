# Capitolo 2 — Dal problema di business al problema analitico

> **Una buona analisi non comincia dalla prima query. Comincia da un accordo esplicito su quale decisione stiamo cercando di migliorare e su quale evidenza potrebbe farci cambiare idea.**

Il Capitolo 1 ha costruito la catena che porta da un problema reale a una decisione: problema, domanda, dati, metodo, evidenza, interpretazione, decisione, azione e misurazione. Prima di poter percorrere quella catena, però, serve un passaggio che nel lavoro quotidiano viene spesso saltato. Qualcuno deve trasformare una richiesta ancora vaga in una specifica abbastanza chiara da poter essere eseguita senza che analyst, stakeholder e data engineer stiano lavorando, inconsapevolmente, su problemi diversi.

È raro che una richiesta arrivi già in forma analitica. Più spesso il business dice che le vendite “stanno andando male”, chiede una dashboard clienti, vuole sapere se il marketing “funziona”, domanda perché gli utenti abbandonano o pretende una previsione del prossimo trimestre. Queste frasi sono importanti perché segnalano un bisogno, ma non dicono ancora quale fenomeno misurare, quale confronto usare, quale decisione sia in gioco né quale livello di evidenza sarebbe sufficiente.

Il rischio è particolarmente alto proprio quando gli strumenti sono veloci. Se produrre una query, una segmentazione o una prima dashboard richiede pochi minuti, la tentazione naturale è iniziare subito. Ma l'esecuzione rapida rende economico andare nella direzione sbagliata; non rende economico scoprire due giorni dopo che “cliente”, “churn” o “vendita” significavano cose diverse per persone diverse.

Questo capitolo introduce quindi l'**Analytical Brief**: una specifica breve che rende esplicito il contratto di lavoro prima dell'esecuzione. Non è un project charter da dieci pagine e non serve a burocratizzare ogni richiesta. Serve a portare alla luce, nel momento in cui correggerle costa poco, le scelte che altrimenti emergerebbero dentro il codice o durante la presentazione finale.

## Il brief come contratto di lavoro

Un buon brief collega il problema di business alla decisione che deve essere presa e, da quella decisione, ricava la domanda analitica, le metriche, lo scope, la baseline, le ipotesi, i requisiti dati e il livello di approfondimento necessario. Questi elementi non sono campi indipendenti da compilare meccanicamente. Si vincolano a vicenda.

Se la decisione riguarda un rollout irreversibile, per esempio, il costo dell'errore può richiedere evidenza più forte e controlli più profondi. Se l'outcome è retention a 90 giorni, lo scope deve escludere le coorti che non hanno ancora maturato novanta giorni di osservazione. Se un'ipotesi riguarda il nuovo checkout mobile, il requisito dati deve includere l'esposizione alla release e una segmentazione per dispositivo. Se nessuna informazione plausibile cambierebbe la decisione, forse non serve una dashboard permanente ma soltanto un controllo rapido.

È questo sistema di dipendenze che trasforma il brief da modulo amministrativo a strumento analitico.

La logica è molto precedente all'AI. CRISP-DM colloca il *Business Understanding* prima del *Data Understanding*: obiettivi, vincoli e criteri di successo vengono chiariti prima di investire nella parte tecnica. IBM descrive esplicitamente questa fase come il momento in cui si comprendono gli obiettivi di business e si documentano le aspettative del progetto.[^ibm-business]

L'AI non cambia questo principio; lo rende più importante. Quando l'esecuzione diventa abbondante, il collo di bottiglia si sposta verso la qualità della specifica che governa quell'esecuzione.

## Che cosa costruiremo

Nel resto del capitolo costruiremo il brief nello stesso ordine in cui un problema acquista forma. Partiremo dal bisogno di business e dalla decisione, identificheremo chi possiede significato e autorità, definiremo outcome e metriche, trasformeremo intuizioni in ipotesi verificabili e fisseremo popolazione, tempo, baseline e segmentazioni. Solo allora tradurremo il piano in requisiti dati e metodo iniziale.

Nella seconda parte affronteremo una questione altrettanto importante: quanto lavoro vale la pena fare. Priorità, Value of Information, stop rule e risultati inconcludenti servono infatti a evitare sia l'analisi superficiale sia l'analisi infinita. Il punto non è sapere tutto; è sapere abbastanza per la decisione che abbiamo davanti e riconoscere quando i dati non consentono una conclusione più forte.

Il caso end-to-end riunirà questi passaggi mostrando come una richiesta apparentemente semplice — “facci una dashboard clienti” — possa cambiare completamente quando il brief costringe il team a verificare prima la metrica su cui quella dashboard dovrebbe poggiare.

Alla fine, il deliverable più importante del capitolo non sarà una query o un report. Sarà una domanda progettata abbastanza bene da rendere chiaro **che cosa vale la pena eseguire, che cosa dovrà essere verificato e quando avremo il diritto di fermarci**.

---

### Fonte

[^ibm-business]: IBM, *Business Understanding Overview / CRISP-DM*. https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview
