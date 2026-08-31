## 1.8 Dai dati alla decisione: la catena del valore analitico

Un dataset non è ancora un'analisi.

Un grafico non è ancora un insight.

Un insight non è ancora una decisione.

Per capire dove nasce il valore dell'analisi è utile separare i passaggi che collegano un'osservazione a un'azione.

Useremo questa catena come riferimento per tutto il libro:

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**

Non è un processo perfettamente lineare. Si torna spesso indietro: un problema nei dati può costringerci a riformulare la domanda; un risultato inatteso può richiedere una nuova segmentazione; una decisione può generare nuove informazioni.

Ma la sequenza rende visibile una cosa importante: **ogni passaggio introduce scelte e possibili errori diversi.**

### Problema e domanda

Il problema appartiene al mondo reale.

> “I nuovi clienti stanno acquistando meno.”

La domanda analitica formalizza ciò che vogliamo verificare.

> “Il numero di ordini per nuovo cliente nei primi 30 giorni è diminuito rispetto alle coorti comparabili dell'anno precedente?”

Senza questa trasformazione rischiamo di interrogare dati senza sapere che cosa dovrebbe contare come risposta.

### Dati e metodo

Una volta definita la domanda, dobbiamo individuare quali dati rappresentano il fenomeno e quale metodo è appropriato.

Possiamo aver bisogno di:

- ordini e clienti;
- coorti di acquisizione;
- canali marketing;
- resi e cancellazioni;
- eventi di prodotto;
- variazioni di prezzo o di esperienza.

Il metodo può essere una semplice decomposizione, un confronto tra coorti, un test statistico, un modello o un esperimento.

La complessità del metodo non è un obiettivo. Deve essere proporzionata alla domanda.

### Evidenza

Supponiamo che l'analisi mostri:

- ordini dei clienti esistenti stabili;
- calo concentrato nei nuovi clienti;
- traffico invariato;
- conversione dei nuovi utenti in diminuzione;
- peggioramento concentrato nei mercati dove è stata introdotta una nuova soglia per la spedizione gratuita.

Questi elementi restringono lo spazio delle spiegazioni possibili.

È questo che intendiamo per **evidenza**: non un dato isolato, ma un insieme di osservazioni che rende alcune spiegazioni più compatibili dei concorrenti.

### Interpretazione

L'evidenza non parla da sola.

Una formulazione prudente potrebbe essere:

> “Il calo della conversione è concentrato nei mercati interessati dalla nuova politica di spedizione; la modifica è quindi una spiegazione plausibile da verificare.”

È diverso da:

> “La nuova politica di spedizione ha causato il calo.”

La seconda frase richiede un livello di evidenza causale più forte.

L'interpretazione è il passaggio in cui l'analista deve distinguere ciò che osserva da ciò che inferisce.

### Decisione

L'azienda potrebbe:

- ripristinare temporaneamente le condizioni precedenti;
- testare soglie diverse;
- segmentare la policy per valore del carrello;
- non intervenire se il costo della modifica supera il beneficio atteso.

I dati non selezionano automaticamente una di queste opzioni.

La decisione combina evidenza con costi, vincoli, rischio, reversibilità e obiettivi aziendali.

### Azione e misurazione

La catena non termina quando il management approva una slide.

Se viene modificata la soglia di spedizione, dobbiamo osservare ciò che succede dopo:

- conversione;
- margine;
- valore medio del carrello;
- costi logistici;
- comportamento per segmento;
- effetti inattesi.

La misurazione successiva serve sia a valutare l'azione sia ad aggiornare il nostro modello del fenomeno.

### Dove può rompersi la catena

Ogni anello ha un failure mode tipico.

| Passaggio | Possibile errore |
|---|---|
| Problema | affrontiamo un sintomo irrilevante |
| Domanda | la formulazione è vaga o non verificabile |
| Dati | la rappresentazione è incompleta o distorta |
| Metodo | il confronto o il modello non sono adatti |
| Evidenza | selezioniamo solo risultati favorevoli |
| Interpretazione | andiamo oltre ciò che i dati sostengono |
| Decisione | ignoriamo costi, rischio o vincoli |
| Azione | l'intervento viene implementato diversamente dal previsto |
| Misurazione | non sappiamo se la decisione ha funzionato |

Questo è il motivo per cui la qualità analitica non può essere valutata soltanto controllando il codice.

### Il rischio delle dashboard senza decisione

Molte organizzazioni accumulano report che descrivono ciò che è successo senza essere collegati a un comportamento o a un processo decisionale.

Una domanda utile durante la progettazione è:

> **“Quale comportamento potrebbe cambiare se questa informazione fosse diversa da ciò che ci aspettiamo?”**

Se nessuno sa rispondere, il report può comunque avere valore informativo, ma dobbiamo essere onesti sul suo ruolo. Non è automaticamente decision support.

La catena del valore analitico ci aiuta proprio a evitare questa confusione.

> **Il valore non nasce quando produciamo il numero. Nasce quando il numero, attraverso un processo affidabile, modifica ciò che sappiamo e migliora ciò che facciamo.**
