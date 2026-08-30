# Capitolo 3 - Capire il dato prima di analizzarlo

> Prima di calcolare una metrica dobbiamo capire che cosa rappresenta una riga, che cosa rappresenta una colonna, da dove arriva il dato e quali errori possono essere entrati nel processo di raccolta.

Nel capitolo precedente abbiamo imparato a trasformare un problema di business in una domanda analitica. Ora dobbiamo affrontare il passaggio successivo: capire il dato che useremo per rispondere.

È qui che molti progetti iniziano a deragliare.

Un dataset può sembrare ordinato, avere migliaia di righe e colonne ben nominate, e tuttavia contenere ambiguità profonde: una riga può rappresentare un ordine, una riga d'ordine, un pagamento, una spedizione o uno snapshot giornaliero. Una colonna chiamata `revenue` può significare lordo, netto, imponibile, valore prima dei resi o valore dopo gli sconti. Un campo `customer_id` può non identificare davvero una persona univoca. Un timestamp può rappresentare la creazione dell'evento, la sua elaborazione o il momento in cui è arrivato nel data warehouse.

Per questo il Data Analyst deve sviluppare una capacità che precede qualsiasi formula: **leggere la struttura del dato come una rappresentazione del processo reale che l'ha prodotto**.

In questo capitolo costruiremo un metodo per farlo in modo sistematico. Studieremo osservazioni, variabili, granularità, chiavi, eventi, snapshot, qualità del dato, missing values, duplicati, vincoli, lineage e controlli di sanity. L'obiettivo non è diventare Data Engineer, ma arrivare al punto in cui l'analista sa riconoscere quando un dataset è affidabile, quando è ambiguo e quando non può ancora essere usato per una decisione.
