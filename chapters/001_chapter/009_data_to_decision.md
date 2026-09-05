## 1.8 Dai dati alla decisione: la catena del valore analitico

Un dataset non è ancora un'analisi. Un grafico non è ancora un insight. Un insight non è ancora una decisione.

Queste distinzioni sembrano linguistiche finché non osserviamo come un errore si propaga. Se la domanda è formulata male, possiamo raccogliere dati perfetti sul fenomeno sbagliato. Se la metrica è incoerente con la domanda, un metodo sofisticato rende più precisa una rappresentazione inadeguata. Se interpretiamo un'associazione come causa, la decisione può essere molto razionale rispetto a una premessa che non abbiamo dimostrato.

Per rendere visibile questa propagazione useremo una catena di riferimento lungo tutto il libro:

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**

La catena non è una pipeline rigida. Nel lavoro reale si torna continuamente indietro. Un limite nei dati può costringerci a riformulare la domanda; un risultato inatteso può richiedere una nuova segmentazione; una decisione reversibile può essere usata come esperimento per produrre nuova evidenza. La sequenza serve a ricordare che ogni passaggio svolge una funzione diversa e introduce errori diversi.

### Dal problema alla domanda: decidere che cosa deve diventare osservabile

Supponiamo che il business dica:

> “I nuovi clienti stanno acquistando meno.”

Questa è una descrizione del problema, non ancora la sua formulazione analitica. Potremmo trasformarla in:

> “Il numero di ordini per nuovo cliente nei primi 30 giorni è diminuito rispetto alle coorti comparabili dell'anno precedente?”

Abbiamo introdotto una metrica, una popolazione, una finestra temporale e una baseline. Queste scelte possono essere discusse e corrette. Senza di esse potremmo interrogare i dati a lungo senza sapere quale risultato conti come risposta.

### Dai dati al metodo: rappresentare il fenomeno con il minimo necessario

Una volta definita la domanda dobbiamo capire quali informazioni la rendano osservabile. Nel nostro esempio potrebbero servire ordini, anagrafica clienti, coorti di acquisizione, canali marketing, resi, variazioni di prezzo ed eventi di prodotto.

Non significa che dobbiamo usare tutto ciò che possediamo. Significa ricostruire il pezzo di realtà sufficiente a distinguere le spiegazioni rilevanti.

Anche il metodo dovrebbe seguire la stessa logica. Una decomposizione per coorte può essere sufficiente. In altri casi servono un test statistico, un modello o un esperimento. La complessità non è un risultato in sé: **un metodo più articolato è utile soltanto quando compra una forma di evidenza che un metodo più semplice non può fornire.**

### Dall'output all'evidenza: restringere le spiegazioni possibili

Supponiamo che l'analisi mostri clienti esistenti stabili, calo concentrato nei nuovi clienti, traffico invariato, conversione dei nuovi utenti in diminuzione e peggioramento particolarmente forte nei mercati in cui è stata introdotta una nuova soglia per la spedizione gratuita.

Nessuno di questi elementi, isolato, è “la risposta”. Insieme però restringono lo spazio delle spiegazioni plausibili. Se il traffico è stabile, una parte delle ipotesi di acquisizione perde forza. Se il calo è concentrato nei nuovi clienti, una spiegazione che dovrebbe colpire uniformemente la base diventa meno convincente. Se il pattern coincide con alcuni mercati e non con altri, la geografia dell'intervento diventa informativa.

È questo che intendiamo per **evidenza**: un insieme di osservazioni che rende alcune spiegazioni più compatibili dei concorrenti.

L'evidenza è più utile quando non si limita ad accumulare segnali a favore della prima storia, ma cerca anche ciò che dovrebbe osservare se quella storia fosse sbagliata.

### Dall'evidenza all'interpretazione: non promettere più di quanto sappiamo

Dai pattern precedenti possiamo formulare:

> “Il calo della conversione è concentrato nei mercati interessati dalla nuova politica di spedizione; la modifica è quindi una spiegazione plausibile da verificare.”

È una frase diversa da:

> “La nuova politica di spedizione ha causato il calo.”

La seconda introduce una promessa controfattuale: sostiene che, modificando quella policy, cambierebbe l'outcome. Per dirlo serve evidenza causale più forte.

L'interpretazione è quindi il punto in cui distinguiamo ciò che abbiamo osservato da ciò che stiamo inferendo. Molte analisi fragili non falliscono nel calcolo: falliscono proprio in questo salto linguistico.

### Dall'interpretazione alla decisione: aggiungere ciò che i dati non decidono

Anche se la nuova soglia di spedizione è la spiegazione principale, l'azione non è automatica. L'azienda potrebbe ripristinare le condizioni precedenti, testare soglie diverse, segmentare la policy per valore del carrello oppure non intervenire se il costo logistico della modifica supera il beneficio atteso.

I dati aiutano a stimare le conseguenze delle alternative. Non contengono da soli costi, priorità, vincoli operativi e appetito al rischio. La decisione nasce quando queste dimensioni incontrano l'evidenza.

Per questo una stessa analisi può giustificare azioni diverse in contesti diversi senza che una delle due organizzazioni stia “ignorando i dati”.

### L'azione produce nuova informazione

La catena non termina quando una slide viene approvata. Se cambiamo la soglia di spedizione, dobbiamo osservare che cosa accade a conversione, margine, valore medio del carrello e costi logistici, e dobbiamo farlo nei segmenti in cui ci aspettavamo l'effetto.

La misurazione serve a due cose. Valuta se la decisione ha raggiunto l'obiettivo e aggiorna il nostro modello del fenomeno. Se il comportamento non cambia come previsto, abbiamo imparato qualcosa anche sulla spiegazione che ci aveva portati ad agire.

In questo senso l'analisi è un ciclo, non un documento.

### Dove può rompersi la catena

| Passaggio | Possibile errore |
|---|---|
| Problema | affrontiamo un sintomo irrilevante |
| Domanda | la formulazione è vaga o non verificabile |
| Dati | la rappresentazione è incompleta o distorta |
| Metodo | il confronto o il modello non sono adatti |
| Evidenza | selezioniamo soltanto risultati favorevoli |
| Interpretazione | andiamo oltre ciò che i dati sostengono |
| Decisione | ignoriamo costi, rischio o vincoli |
| Azione | l'intervento viene implementato diversamente dal previsto |
| Misurazione | non sappiamo se la decisione ha funzionato |

La tabella spiega perché la qualità analitica non può essere valutata controllando soltanto il codice. Un processo può essere corretto in un anello e fallire in quello precedente.

### Il rischio delle dashboard senza decisione

Molte organizzazioni accumulano report che descrivono ciò che è successo senza essere collegati a un comportamento o a un processo decisionale. Non significa che ogni dashboard debba prescrivere un'azione, ma è utile essere chiari sul ruolo che svolge.

Una domanda semplice durante la progettazione è:

> **“Quale comportamento potrebbe cambiare se questa informazione fosse diversa da ciò che ci aspettiamo?”**

Se nessuno sa rispondere, il report può avere valore di monitoraggio, trasparenza o conoscenza, ma non dovremmo chiamarlo automaticamente decision support.

La catena del valore analitico serve proprio a rendere visibile questa distinzione:

> **Il valore non nasce quando produciamo il numero. Nasce quando il numero, attraverso un processo affidabile, modifica ciò che sappiamo e migliora ciò che facciamo.**
