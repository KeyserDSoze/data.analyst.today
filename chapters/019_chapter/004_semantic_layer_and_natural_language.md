## 19.3 Semantic leverage: quando l'interfaccia diventa più semplice

Una delle promesse più visibili dell'AI applicata ai dati è che chiunque potrà interrogare il business in linguaggio naturale. È plausibile che una parte crescente dell'interazione con l'analytics diventi conversazionale. Ma una UI più semplice non rende più semplice il problema sottostante. Spesso lo rende soltanto meno visibile.

Se un manager chiede “qual è il churn in Francia?”, la generazione della query può essere quasi istantanea. La domanda continua però a contenere un'ambiguità strutturale: logo churn o revenue churn? Cancellation o non-renewal? Volontario o totale? A 30, 60 o 90 giorni? Mensile o annualizzato? La difficoltà non è tradurre le parole in SQL. È collegare quelle parole alla **versione di realtà che l'organizzazione ha deciso di considerare autorevole per quella decisione**.

La catena resta quindi:

**linguaggio umano → concetto business → entità/metrica → semantic contract → dati → query → evidenza**

Il natural-language access comprime soprattutto l'ultimo tratto. Se il semantic contract è debole, rende semplicemente più facile produrre una risposta sbagliata in modo convincente.

Questo cambia la scala del problema. Una definizione ambigua usata da due analyst genera due numeri. La stessa ambiguità esposta a migliaia di richieste conversazionali può diventare un **blast radius semantico**. Per questo l'AI aumenta il valore di metriche certificate, entity definition, time semantics, lineage, freshness metadata, ownership, deprecation status, access policy e risposte verificate per le domande critiche. Il Capitolo 11 le ha trattate come data modeling; il Capitolo 18 come operating responsibility. Qui vediamo la conseguenza professionale: **formalizzare il significato è una forma di leverage**.

Il lavoro resta spesso invisibile perché l'utente vede soltanto una casella di testo. Dietro quella casella qualcuno deve aver deciso che cosa sia un customer, quale evento renda una transazione valida, quale data governi il periodo, quale revenue sia certificata, quali metriche non siano combinabili, che cosa fare con un asset deprecated o stale e quando una parola ambigua richieda chiarimento invece di una risposta automatica.

Consideriamo la richiesta “mostrami i 20 clienti con revenue più alta negli ultimi 12 mesi”. In un'azienda con contratti annuali, professional services, crediti, invoice multi-entity, revenue recognition differita e ARR separato dalla recognized revenue, `invoice_amount` può essere un campo reale e la classifica può essere matematicamente perfetta. Ma se la decisione riguarda gli account prioritari del board, il concetto corretto potrebbe essere recognized revenue o ARR a seconda dello scopo. L'errore non è sintattico: è **ontologico**.

È qui che la **semantic fluency** diventa una capacità professionale. Non significa conoscere a memoria un glossario. Significa trasformare parole business in entità e metriche verificabili, accorgersi quando due stakeholder chiamano nello stesso modo concetti diversi, distinguere il campo disponibile dal concetto corretto, rendere esplicite le eccezioni invece di nasconderle nella query e collaborare con Finance, Product, Engineering e Governance per stabilire il significato che può essere riusato.

Una possibile evoluzione del ruolo passa quindi da “costruisco il dashboard che risponde alla domanda” a **“rendo il dominio interrogabile senza costringere ogni consumer a ricostruirne il significato”**. Questo può voler dire curare metric contract, semantic model, verified answer, failure query e policy di chiarimento. È semantic product thinking, non semplice report building.

Microsoft documenta oggi questa esigenza direttamente nelle funzioni di preparazione dei semantic model per Copilot in Power BI. AI data schema, verified answers e AI instructions servono a restringere il contesto, ridurre ambiguità, mappare il linguaggio dell'organizzazione e guidare il sistema verso campi e risposte approvate. La stessa documentazione avverte che le instructions sono guidance interpretata dal modello, non una garanzia assoluta: la semantica resta quindi un sistema da progettare e testare, non un prompt magico.

Fonti pubbliche:
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq

Più l'interfaccia diventa naturale, meno la velocità nel costruire una vista distingue da sola un analyst. Resta una domanda più difficile: **come facciamo in modo che migliaia di domande diverse attraversino un significato coerente senza impedire l'esplorazione?**

Chi sa rispondere non sta soltanto modellando dati. Sta progettando la grammatica con cui persone e agenti parlano del business.

> **Quando la sintassi diventa economica, la semantica diventa infrastruttura.**