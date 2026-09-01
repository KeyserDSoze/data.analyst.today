# Capitolo 3 - Capire il dato prima di analizzarlo

> Un dataset non è la realtà. È una traccia prodotta da sistemi, persone e regole. Prima di analizzarla dobbiamo capire che cosa rappresenta e quanto è adatta alla domanda che vogliamo porre.

Nel Capitolo 2 abbiamo trasformato una richiesta di business in un **Analytical Brief**. Quel documento contiene già alcune assunzioni: quale popolazione ci interessa, quale metrica vogliamo misurare, quale periodo confrontare, quali segmenti osservare e quali dati dovrebbero permetterci di rispondere.

Adesso arriva il momento di verificare se i dati disponibili rispettano davvero quelle assunzioni.

È un passaggio meno visibile di una dashboard o di un modello statistico, ma spesso decide la qualità di tutto ciò che viene dopo.

Un file può avere milioni di righe, colonne ben nominate e nessun errore tecnico evidente, e tuttavia non essere ancora utilizzabile. Una riga può rappresentare un ordine, una riga d'ordine, una versione dell'ordine o uno snapshot giornaliero. `customer_id` può identificare un account invece di una persona. `revenue` può essere lordo, netto, riconosciuto o semplicemente ordinato. `created_at` può indicare quando un evento è avvenuto oppure quando è entrato nel warehouse.

Il lavoro dell'analista non consiste quindi nel "pulire il dataset" finché appare ordinato. Consiste nel ricostruire il **modello di realtà** incorporato nei dati e nel verificare se quel modello è sufficientemente affidabile per la decisione.

Useremo questo percorso:

**Riga → identità → tempo → qualità → anomalie → provenienza → riconciliazione → data readiness**

Alla fine dovremmo poter classificare un dataset in uno di tre modi:

- **pronto**: le proprietà critiche sono comprese e i rischi residui non compromettono la domanda;
- **utilizzabile con caveat**: alcuni limiti rimangono, ma possono essere quantificati e comunicati;
- **non pronto**: una o più incertezze sul dato rendono prematura l'analisi.

Questa distinzione è importante. Un analista professionale non promette che un dataset sia "perfetto". Stabilisce se è **fit for purpose** rispetto a uno specifico uso.

In questo capitolo studieremo osservazioni e variabili, granularità, chiavi e identità, eventi e snapshot, missing values, duplicati, outlier, tipi e domini, sanity check, lineage, riconciliazione, data contract e controlli automatici.

Non entreremo ancora nel disegno tecnico dei modelli SQL, che affronteremo nel Capitolo 11, né nell'architettura che trasporta il dato, che sarà il centro del Capitolo 12. Qui ci interessa una domanda più immediata:

> **Posso usare questi dati per sostenere la conclusione che sto per presentare?**

Prima di cercare pattern, dobbiamo guadagnarci il diritto di crederli.