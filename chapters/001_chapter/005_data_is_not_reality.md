## 1.4 I dati non sono la realtà

Uno degli errori più pericolosi nell'analisi è confondere il dato con il fenomeno che il dato cerca di rappresentare.

Un database non contiene il mondo reale. Contiene una rappresentazione del mondo reale costruita attraverso sistemi, processi, definizioni e regole operative.

Quando leggiamo una colonna chiamata `customer`, `revenue`, `active_user` o `conversion`, stiamo già osservando il risultato di una serie di scelte.

Chi è considerato cliente? Quando una persona diventa cliente? Un ordine annullato conta? Una vendita viene registrata al momento dell'ordine, del pagamento o della consegna? Un utente è attivo se apre l'app, se effettua una sessione, se compie un'azione specifica o se genera valore economico?

Ogni metrica porta con sé una definizione.

### Il dato è prodotto da un sistema

Immaginiamo un e-commerce.

Un cliente effettua un ordine alle 23:58 del 31 gennaio. Il pagamento viene autorizzato alle 00:01 del 1° febbraio. Il magazzino prepara il pacco il 2 febbraio. La spedizione parte il 3 febbraio. Il cliente restituisce metà dell'ordine il 10 febbraio e riceve il rimborso il 15 febbraio.

In quale mese appartiene quella vendita?

Non esiste una risposta universale.

Dipende dalla domanda.

Per analizzare la domanda commerciale può avere senso utilizzare la data dell'ordine. Per la contabilità potrebbe essere rilevante un'altra data. Per la logistica conta la data di evasione. Per il cash flow conta il momento del pagamento e del rimborso.

La stessa transazione può quindi appartenere a periodi differenti a seconda del fenomeno che vogliamo studiare.

### Misurare significa scegliere

Una metrica non è semplicemente un numero. È una funzione che comprime una parte della realtà in una rappresentazione utilizzabile.

Quando scegliamo una metrica decidiamo implicitamente:

- cosa includere;
- cosa escludere;
- quale unità utilizzare;
- quale intervallo temporale osservare;
- come aggregare gli eventi;
- come gestire eccezioni e valori mancanti;
- quale popolazione considerare.

Questa è una delle ragioni per cui due dashboard possono mostrare numeri diversi pur essendo entrambe tecnicamente corrette.

### Il problema semantico

L'AI rende questo punto ancora più importante.

Un sistema generativo può costruire una query sintatticamente perfetta e utilizzare comunque la colonna sbagliata, la relazione sbagliata o la definizione sbagliata della metrica.

La documentazione Microsoft per Copilot in Power BI evidenzia che output errati possono derivare sia da prompt ambigui sia da problemi nel modello semantico sottostante. Microsoft raccomanda di preparare dati, modello e contesto aziendale prima di utilizzare Copilot per interrogare i dati.

Fonti:

- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

Questo ci porta a una regola fondamentale:

> **Prima di chiedere cosa dicono i dati, dobbiamo capire che cosa rappresentano.**

### Il dato osservato non è sempre il dato desiderato

Spesso il fenomeno che ci interessa non può essere misurato direttamente.

Vogliamo conoscere la soddisfazione del cliente, ma osserviamo recensioni, survey, reclami e retention.

Vogliamo misurare la produttività, ma osserviamo ticket chiusi, ore lavorate o output prodotti.

Vogliamo misurare la qualità, ma osserviamo resi, errori o difetti.

Questi sono *proxy*: variabili osservabili utilizzate per rappresentare fenomeni più complessi.

I proxy possono essere utilissimi, ma diventano pericolosi quando dimentichiamo che sono approssimazioni.

Una parte essenziale del mestiere dell'analista consiste proprio nel mantenere distinta la realtà dalla sua rappresentazione numerica.
