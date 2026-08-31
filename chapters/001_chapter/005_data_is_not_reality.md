## 1.4 I dati non sono la realtà

Uno degli errori più pericolosi nell'analisi è confondere il dato con il fenomeno che il dato cerca di rappresentare.

Un database non contiene il mondo reale.

Contiene una rappresentazione del mondo reale costruita attraverso sistemi, processi, definizioni e regole operative.

Quando leggiamo una colonna chiamata `customer`, `revenue`, `active_user` o `conversion`, stiamo già osservando il risultato di una serie di scelte.

Chi è considerato cliente? Quando una persona diventa cliente? Un ordine annullato conta? Una vendita viene registrata all'ordine, al pagamento, alla spedizione o alla contabilizzazione? Un utente è attivo se apre l'app, se effettua una sessione o se compie un'azione specifica?

I nomi familiari possono far sembrare naturali decisioni che naturali non sono.

### Un evento, più rappresentazioni

Immaginiamo un e-commerce.

Un cliente effettua un ordine alle 23:58 del 31 gennaio. Il pagamento viene autorizzato alle 00:01 del 1° febbraio. Il magazzino prepara il pacco il 2 febbraio. La spedizione parte il 3. Il cliente restituisce metà dell'ordine il 10 e riceve il rimborso il 15.

A quale mese appartiene quella vendita?

Non esiste una risposta universale.

Per analizzare la domanda commerciale può avere senso la data dell'ordine. Per il cash flow contano pagamento e rimborso. Per la logistica conta l'evasione. Per la contabilità può valere un'altra regola ancora.

Lo stesso evento reale produce più date, stati e importi validi per domande diverse.

La scelta analitica consiste nel collegare la rappresentazione corretta al fenomeno corretto.

### Misurare significa scegliere

Una metrica comprime una parte della realtà in una rappresentazione utilizzabile.

Quando la definiamo decidiamo implicitamente:

- cosa includere e cosa escludere;
- quale unità usare;
- quale intervallo temporale osservare;
- come aggregare gli eventi;
- come gestire eccezioni, resi e valori mancanti;
- quale popolazione considerare;
- quale momento del processo rappresenta il fenomeno.

Per questo due dashboard possono mostrare numeri diversi pur partendo dallo stesso ecosistema dati. Non è detto che una delle due contenga un bug. Potrebbero rappresentare due definizioni diverse.

La sezione 1.9 entrerà nel dettaglio delle metriche. Qui ci interessa una regola più generale:

> **prima del calcolo esiste sempre un modello della realtà, esplicito o implicito.**

### Il dato osservato non è sempre il fenomeno desiderato

Molti concetti importanti non possono essere osservati direttamente.

Vogliamo conoscere la soddisfazione del cliente, ma osserviamo survey, recensioni, reclami, utilizzo e retention.

Vogliamo misurare produttività, ma osserviamo ticket chiusi, ore lavorate, output prodotti o tempi di ciclo.

Vogliamo misurare qualità, ma osserviamo difetti, resi, errori o reclami.

Queste variabili funzionano come **proxy**: segnali osservabili che rappresentano fenomeni più complessi.

Un proxy può essere molto utile. Diventa pericoloso quando smettiamo di ricordare che è un'approssimazione.

Un aumento dei ticket chiusi può significare maggiore produttività. Può anche significare ticket più semplici, classificazioni diverse o incentivi a chiudere troppo in fretta.

### Anche l'assenza di dato ha un significato

Ciò che non viene registrato può essere importante quanto ciò che compare in tabella.

Un sistema di supporto contiene i problemi segnalati, non necessariamente tutti i problemi vissuti dai clienti.

Una survey contiene le risposte di chi ha scelto di rispondere.

Un funnel digitale contiene gli eventi che il tracking è riuscito a osservare.

Questo introduce una domanda che accompagnerà tutto il libro:

> **Quale meccanismo ha determinato che questa osservazione entrasse — o non entrasse — nel dataset?**

È una domanda di qualità, ma anche di selezione e di interpretazione.

### Perché l'AI rende il problema più visibile

Un sistema generativo può costruire una query sintatticamente perfetta usando la colonna sbagliata, la relazione sbagliata o una definizione non adatta alla domanda.

La documentazione Microsoft per Copilot in Power BI mette in evidenza proprio la dipendenza degli output dal modello semantico e dal contesto fornito agli strumenti AI.

Fonti:
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

Ma il principio non appartiene all'AI. Vale per qualsiasi analisi.

> **Prima di chiedere che cosa dicono i dati, dobbiamo capire che cosa rappresentano e come sono stati prodotti.**
