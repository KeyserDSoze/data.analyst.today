# Capitolo 3 — Capire il dato prima di analizzarlo

> **Un dataset non è la realtà. È una traccia prodotta da sistemi, persone e regole. Prima di analizzarla dobbiamo capire che cosa rappresenta e quanto è adatta alla domanda che vogliamo porre.**

Nel Capitolo 2 abbiamo trasformato una richiesta di business in un **Analytical Brief**. Quel documento contiene già una promessa: sappiamo quale popolazione vogliamo osservare, quale metrica conta, quale periodo confrontare, quali segmenti potrebbero cambiare la spiegazione e quali dati dovrebbero permetterci di rispondere.

Il Capitolo 3 mette quella promessa alla prova. La domanda non è più soltanto *quali dati ci servono?*, ma **se le fonti disponibili rappresentano davvero ciò che il brief presume**.

È un passaggio meno visibile di una dashboard o di un modello, ma spesso decide la qualità di tutto ciò che viene dopo. Un file può contenere milioni di righe, colonne ben nominate e nessun errore di esecuzione, e restare comunque inadatto alla domanda. Una riga può rappresentare un ordine, una riga d'ordine, una versione dell'ordine o uno snapshot giornaliero. `customer_id` può identificare un account anziché una persona. `revenue` può significare importo ordinato, fatturato netto o ricavo riconosciuto. `created_at` può registrare il momento dell'evento oppure quello in cui il record è entrato nel warehouse.

Questi non sono problemi cosmetici da correggere durante il cleaning. Sono differenze nel **modello di realtà incorporato nel dato**. Se sbagliamo quel modello, possiamo ottenere query corrette che contano la cosa sbagliata, trend coerenti costruiti su popolazioni mutate e KPI apparentemente precisi che non sono confrontabili nel tempo.

Per questo il lavoro dell'analista non consiste nel rendere il dataset ordinato. Consiste nel ricostruire abbastanza della sua storia da sapere quali conclusioni può sostenere.

## Dalla riga alla readiness

Seguiremo un percorso che parte dalla rappresentazione più elementare e arriva alla decisione di usare o non usare il dato:

**Riga → grain → identità → tempo → qualità → anomalie → lineage → riconciliazione → data readiness**

La sequenza conta perché ogni passaggio restringe il significato del successivo. Prima di parlare di duplicati dobbiamo sapere quale grain dovrebbe essere unico. Prima di trattare un missing dobbiamo capire se quel valore dovrebbe esistere per quel record. Prima di chiamare outlier un importo estremo dobbiamo conoscere unità, dominio e processo che lo ha prodotto. Prima di riconciliare due dashboard dobbiamo verificare se stanno davvero misurando la stessa cosa.

L'obiettivo finale non è certificare un dataset come “buono” o “cattivo” in astratto. È arrivare a un verdetto **fit for purpose** rispetto all'Analytical Brief.

Un dataset può essere **pronto** quando le proprietà critiche sono comprese e i rischi residui non compromettono la domanda; **pronto con caveat** quando può essere utilizzato soltanto entro limiti espliciti; oppure **non pronto** quando un'incertezza sulla rappresentazione è abbastanza grande da rendere prematura la conclusione.

Questa distinzione permette di essere rigorosi senza inseguire la perfezione. Un dato preliminare può essere adeguato per un monitoraggio aggregato e inaccettabile per un'azione sul singolo cliente. Una fonte può essere utile per confrontare mesi maturi e non esserlo per le ultime ventiquattro ore. La qualità richiesta dipende dall'uso e dal costo dell'errore.

Nel capitolo studieremo quindi osservazioni e variabili, granularità, chiavi e identità, eventi e snapshot, missing, duplicati, outlier, tipi e domini, profiling, lineage, riconciliazione, data contract e controlli automatici. Il data modeling approfondito arriverà nel Capitolo 11 e l'architettura nel Capitolo 12; qui ci interessa ciò che l'analista deve capire **prima** di affidare una conclusione a quelle strutture.

La domanda guida sarà sempre la stessa:

> **Posso usare questi dati per sostenere la conclusione che sto per presentare, e quali limiti devo rendere visibili?**

Prima di cercare pattern, dobbiamo guadagnarci il diritto di crederli.
