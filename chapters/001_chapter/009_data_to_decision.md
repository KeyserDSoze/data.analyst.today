## 1.8 Dai dati alla decisione: la catena del valore analitico

Un dataset non è ancora un'analisi. Un grafico non è ancora un insight. E un insight non è ancora una decisione.

Per capire il lavoro del Data Analyst è utile separare con precisione i diversi passaggi che collegano un'osservazione grezza a un'azione concreta.

Possiamo rappresentare il processo in questo modo:

**Dati → Informazione → Evidenza → Interpretazione → Decisione → Azione → Risultato → Nuovi dati**

Questa sequenza è circolare. Ogni decisione produce conseguenze; le conseguenze generano nuovi dati; i nuovi dati permettono di valutare se la decisione ha funzionato.

### Dati

I dati sono registrazioni di eventi, stati o misurazioni. Una riga in una tabella ordini, una visita a una pagina, il timestamp di un pagamento, la temperatura rilevata da un sensore o il saldo di un conto sono dati.

Il dato da solo non porta necessariamente significato. Il numero `1842`, senza contesto, non dice quasi nulla. Potrebbe essere un numero di ordini, una quantità prodotta, un identificativo o una misura espressa in una certa unità.

### Informazione

Il dato diventa informazione quando viene collocato in un contesto.

> Questo mese abbiamo registrato 1.842 ordini.

Ora conosciamo il fenomeno e il periodo. Ma non sappiamo ancora se 1.842 sia molto, poco, buono o cattivo.

Aggiungiamo un confronto:

> Questo mese abbiamo registrato 1.842 ordini, il 13% in meno rispetto allo stesso mese dell'anno precedente.

Il confronto rende l'informazione più utile. Tuttavia non abbiamo ancora spiegato il fenomeno.

### Evidenza

L'evidenza nasce quando l'analisi restringe il campo delle spiegazioni possibili.

Supponiamo di scoprire che:

- gli ordini dei clienti esistenti sono rimasti stabili;
- il calo proviene quasi interamente dai nuovi clienti;
- il traffico sul sito è invariato;
- il tasso di conversione dei nuovi utenti è diminuito;
- il calo è concentrato nei paesi in cui è stato recentemente introdotto un costo di spedizione minimo.

A questo punto non abbiamo ancora dimostrato una relazione causale, ma abbiamo costruito evidenza molto più utile di un semplice grafico delle vendite.

### Interpretazione

L'evidenza deve essere interpretata.

L'analista potrebbe formulare l'ipotesi che il nuovo costo di spedizione abbia contribuito al calo della conversione. Ma un analista rigoroso distingue tra ciò che osserva e ciò che conclude.

Osservazione:

> La diminuzione della conversione è maggiore nei mercati interessati dalla nuova politica di spedizione.

Interpretazione:

> La nuova politica di spedizione è una spiegazione plausibile del calo e merita una verifica più rigorosa.

La differenza è fondamentale. Una buona analisi non nasconde il livello di incertezza delle proprie conclusioni.

### Decisione

A questo punto il problema diventa manageriale.

L'azienda potrebbe decidere di:

- ripristinare temporaneamente le condizioni precedenti;
- effettuare un test controllato su una parte degli utenti;
- modificare la soglia della spedizione gratuita;
- segmentare la politica in base al valore del carrello;
- non intervenire, se il costo della modifica supera il beneficio atteso.

L'analisi non prende automaticamente la decisione. Fornisce una struttura informativa migliore per prenderla.

### Azione e risultato

La qualità dell'analisi dovrebbe essere valutata anche dopo la decisione.

Se una modifica viene implementata, dobbiamo misurarne l'effetto. È aumentata la conversione? È diminuito il margine? Il valore medio del carrello è cambiato? Ci sono conseguenze inattese?

Il processo analitico quindi non termina con una presentazione o con una dashboard.

Termina quando siamo in grado di osservare il risultato dell'azione e aggiornare ciò che pensiamo di sapere.

### Il rischio delle dashboard senza decisione

Molte organizzazioni accumulano dashboard che descrivono continuamente ciò che è successo ma non sono collegate a un processo decisionale definito.

Una dashboard può essere tecnicamente perfetta e organizzativamente inutile.

Una domanda utile da porre durante la progettazione di qualsiasi analisi è:

> **Quale comportamento potrebbe cambiare se questa informazione fosse diversa da ciò che ci aspettiamo?**

Se nessuno sa rispondere, è possibile che stiamo producendo reporting e non vera analisi decisionale.

### Il ciclo analitico

Nel resto del libro utilizzeremo spesso il seguente ciclo:

1. definire la decisione;
2. formulare la domanda analitica;
3. individuare i dati necessari;
4. verificarne significato e qualità;
5. scegliere il metodo;
6. produrre evidenza;
7. interpretare l'evidenza;
8. comunicare limiti e incertezza;
9. prendere o supportare una decisione;
10. misurarne l'effetto.

L'AI può accelerare quasi tutti questi passaggi operativi. Ma la struttura logica rimane la stessa.

Ed è questa struttura, più di qualsiasi software, che distingue un'analisi utile da una semplice elaborazione di dati.
