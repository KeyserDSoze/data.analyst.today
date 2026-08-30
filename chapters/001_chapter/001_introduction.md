# Capitolo 1 - Tutto è cambiato. Il problema è rimasto lo stesso

> La tecnologia dell'analisi dati cambia continuamente. Il nucleo del lavoro analitico molto meno.

## Introduzione

Negli ultimi trent'anni il lavoro sui dati ha cambiato interfaccia molte volte. Abbiamo visto il foglio elettronico diventare uno strumento universale, i database relazionali entrare nel lavoro quotidiano, la business intelligence portare dashboard e reporting self-service in azienda, Python e R rendere più accessibili analisi statistiche e automazione, il cloud separare sempre di più il calcolo dalla macchina locale e, infine, l'intelligenza artificiale generativa trasformare il linguaggio naturale in una nuova interfaccia verso dati, codice e modelli.

A prima vista potrebbe sembrare che ogni nuova ondata tecnologica cancelli la precedente e riscriva il mestiere del Data Analyst. In realtà cambia soprattutto **il costo dell'esecuzione**. Operazioni che un tempo richiedevano ore di lavoro, sintassi specifica e numerosi passaggi manuali possono oggi essere accelerate o parzialmente automatizzate. Una query SQL può essere proposta da un assistente AI. Uno script Python può essere generato a partire da una descrizione. Una dashboard può essere abbozzata da una richiesta in linguaggio naturale. Un modello semantico può essere interrogato senza che l'utente conosca la struttura sottostante.

Questa accelerazione è reale, ma non coincide con l'automazione dell'analisi nel suo significato più profondo.

Una query corretta non rende corretta una domanda sbagliata. Un dashboard elegante non rende utile una metrica irrilevante. Un modello sofisticato non elimina un bias nei dati. Una correlazione forte non dimostra automaticamente una relazione causale. E un sistema AI capace di produrre codice, grafici e spiegazioni in pochi secondi non può, da solo, garantire che il problema sia stato definito correttamente, che i dati rappresentino davvero il fenomeno che vogliamo studiare o che la conclusione sia adeguata alla decisione da prendere.

È significativo che anche gli strumenti analitici più moderni stiano tornando a enfatizzare concetti antichi: contesto, semantica, qualità del dato e definizioni condivise. La documentazione Microsoft per Copilot in Power BI, per esempio, avverte esplicitamente che un modello semantico non preparato può produrre risposte di bassa qualità, inaccurate o persino fuorvianti. Per migliorare gli output vengono raccomandati schema semplificato, terminologia aziendale, istruzioni contestuali e risposte verificate.[^ms-copilot-semantic] In altre parole: più l'interfaccia diventa intelligente, più diventa importante dare significato ai dati.

Il fenomeno non è nuovo. Molto prima dell'AI generativa, metodologie come CRISP-DM iniziavano il processo analitico dalla **Business Understanding**, seguita dalla comprensione dei dati, dalla preparazione, dalla modellazione, dalla valutazione e dal deployment.[^ibm-crisp] Il principio sottostante è semplice: prima di scegliere il metodo o lo strumento bisogna capire quale problema si sta cercando di risolvere.

Questo libro parte da qui.

Non costruiremo la figura del Data Analyst come una lista di software da imparare. Excel, SQL, Python, Power BI, notebook, data warehouse, lakehouse, servizi cloud e sistemi AI saranno tutti importanti, ma verranno collocati nel loro ruolo corretto: **strumenti all'interno di un processo decisionale**.

La domanda centrale non sarà quindi:

> "Quale tecnologia devo imparare?"

ma:

> "Come si passa da un problema reale a una conclusione affidabile e a una decisione migliore, scegliendo ogni volta gli strumenti più adatti?"

Questa distinzione diventerà ancora più importante nell'era dell'AI. Se la sintassi costa sempre meno, aumentano di valore la formulazione del problema, la conoscenza del dominio, il controllo delle assunzioni, la semantica delle metriche, la capacità di verificare gli output e il giudizio con cui si interpreta l'evidenza.

Il punto di partenza del nostro percorso sarà quindi il **ragionamento analitico**.

---

### Fonti

[^ms-copilot-semantic]: Microsoft Learn, *Use Copilot with Semantic Models in Power BI* e documentazione *Prepare your data for AI*, 2026. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^ibm-crisp]: IBM, documentazione CRISP-DM / SPSS Modeler, *Understanding and preparing data*. https://www.ibm.com/docs/en/ws-and-kc?topic=modeler-understanding-preparing-data
