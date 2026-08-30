## 1.1 Cosa è cambiato davvero

Per capire il ruolo del Data Analyst nell'era dell'intelligenza artificiale bisogna distinguere due cose che spesso vengono confuse: **il lavoro analitico** e **il modo in cui quel lavoro viene eseguito**.

Il primo cambia lentamente. Il secondo cambia molto velocemente.

Per anni una parte significativa del valore tecnico di un analista è derivata dalla capacità di svolgere attività che richiedevano conoscenze operative specifiche: scrivere query SQL, costruire formule, preparare dataset, creare modelli di calcolo, programmare trasformazioni, realizzare visualizzazioni, configurare dashboard e conoscere le peculiarità di un determinato ambiente software.

Queste capacità restano importanti. Ma il loro valore relativo sta cambiando, perché il costo necessario per produrre una prima versione di molti artefatti tecnici si sta abbassando rapidamente.

### Dalla sintassi all'intento

Per molto tempo l'interazione con un sistema informatico è stata dominata dalla sintassi. Per ottenere un risultato bisognava conoscere il linguaggio richiesto dallo strumento.

Per interrogare un database serviva SQL. Per automatizzare un'analisi serviva un linguaggio come Python o R. Per costruire determinati calcoli in Power BI bisognava conoscere DAX. Per trasformare dati in un foglio elettronico era necessario padroneggiare formule, tabelle pivot, Power Query o macro.

L'intelligenza artificiale generativa introduce una nuova interfaccia: **l'intento espresso in linguaggio naturale**.

Un analista può descrivere ciò che vuole ottenere e chiedere al sistema di proporre il codice necessario. Questo sposta parte del lavoro da "ricordare come si scrive" a "sapere cosa si vuole ottenere".

La differenza è sostanziale.

Un utente può chiedere:

> "Calcola il fatturato mensile per categoria, confrontalo con lo stesso mese dell'anno precedente e segnala le categorie con una diminuzione superiore al 15%."

Da questa richiesta un assistente può proporre una query SQL, uno script Python, una misura DAX o un flusso di trasformazione.

Ma il fatto che il sistema sia in grado di tradurre l'intento in codice non significa che l'intento sia corretto.

La definizione di "fatturato" potrebbe essere ambigua. Potrebbero esserci ordini annullati o resi. La data corretta potrebbe essere quella dell'ordine, della spedizione o della contabilizzazione. Potrebbero esserci valute diverse. Il confronto anno su anno potrebbe essere alterato dalla stagionalità o da variazioni nel perimetro aziendale.

L'AI può accelerare la traduzione dell'intento in esecuzione. Non elimina il bisogno di definire correttamente l'intento.

### Il costo marginale dell'analisi si abbassa

Quando produrre una query, un grafico o uno script richiede meno tempo, diventa economicamente possibile esplorare più ipotesi.

Questo è uno dei benefici più importanti dell'AI per l'analista.

Prima un'ipotesi secondaria poteva non essere verificata perché richiedeva troppo lavoro tecnico. Oggi può essere testata in pochi minuti. È possibile generare rapidamente varianti di una query, controllare una metrica da angolazioni differenti, creare prototipi di visualizzazione o chiedere una spiegazione di un metodo statistico prima di applicarlo.

L'analista può quindi dedicare meno tempo ad alcune attività meccaniche e più tempo alla parte investigativa.

Ma esiste il rovescio della medaglia.

Se il costo marginale di un'analisi tende verso zero, anche il costo marginale di una **cattiva analisi** tende verso zero.

Possiamo produrre dieci grafici inutili invece di uno. Possiamo testare decine di correlazioni senza una teoria. Possiamo generare codice che sembra plausibile ma contiene un errore logico. Possiamo costruire una narrazione convincente a partire da dati che non supportano realmente la conclusione.

La capacità di generare output aumenta più velocemente della capacità umana di valutarli.

Per questo la verifica diventa una competenza centrale.

### La separazione tra autore ed esecutore si riduce

Tradizionalmente molte organizzazioni separavano nettamente i ruoli.

Un business user formulava una richiesta. Un analista la traduceva in specifiche. Un data engineer preparava i dati. Un BI developer costruiva il report. Un altro team gestiva l'infrastruttura.

Queste separazioni non scompariranno nelle organizzazioni complesse, ma l'AI riduce il costo di attraversare i confini tra ruoli.

Un analista può produrre più facilmente codice. Un business user può interrogare direttamente un modello semantico. Un data engineer può generare documentazione. Un BI developer può chiedere spiegazioni statistiche. Un data scientist può creare rapidamente prototipi di dashboard.

Questo rende più importante una competenza trasversale: **capire l'intero sistema abbastanza bene da sapere cosa delegare e cosa controllare**.

Il Data Analyst moderno non deve necessariamente diventare specialista profondo di ogni tecnologia. Deve però comprendere il percorso del dato, le assunzioni introdotte a ogni passaggio e le conseguenze delle proprie scelte.

### La semantica diventa infrastruttura

Uno degli sviluppi più interessanti dell'analytics moderno è che il significato dei dati viene sempre più formalizzato all'interno dell'infrastruttura.

Un tempo molte definizioni vivevano nella testa degli analisti o in documenti separati. Oggi metriche, relazioni, descrizioni e logiche di business vengono incorporate nei modelli semantici.

L'arrivo dell'AI rende questa formalizzazione ancora più importante. Microsoft, nella documentazione di Power BI, sottolinea che Copilot funziona meglio quando il modello è preparato con schemi mirati, descrizioni chiare, terminologia aziendale e istruzioni che riducono l'ambiguità.[^ms-ai-schema] La piattaforma permette perfino di configurare "verified answers", cioè risposte validate dagli autori del modello per determinate categorie di domande.[^ms-ai-faq]

Questo ci dice qualcosa di importante: il problema non è soltanto dare all'AI accesso ai dati. Bisogna darle accesso al **significato corretto dei dati**.

### Il lavoro diventa più iterativo

L'analisi non è mai stata realmente un processo lineare, ma gli strumenti moderni rendono l'iterazione molto più veloce.

Si può partire da una domanda, esplorare il dato, scoprire un'anomalia, tornare alla definizione della metrica, modificare la segmentazione, verificare una nuova ipotesi e produrre un secondo risultato in tempi molto brevi.

Questa dinamica è coerente con metodologie come CRISP-DM, che distinguono business understanding, data understanding, data preparation, modeling, evaluation e deployment, senza presupporre che il percorso sia una semplice linea retta.[^ibm-crisp]

L'AI accelera soprattutto il passaggio da un'iterazione alla successiva.

Non sostituisce la necessità di capire **perché** stiamo iterando.

### Cosa cambia quindi per l'analista

Il cambiamento fondamentale può essere riassunto così:

**prima gran parte del vantaggio competitivo personale derivava dal saper eseguire; oggi cresce il valore del saper dirigere, verificare e integrare l'esecuzione.**

Questo non significa che la competenza tecnica perda importanza. Significa che cambia la sua funzione.

Non impariamo SQL soltanto per essere più veloci di un sistema AI nello scrivere una `JOIN`. Lo impariamo perché dobbiamo capire la struttura di una query, riconoscere duplicazioni, controllare il livello di granularità, individuare errori nelle aggregazioni e verificare che il risultato corrisponda al problema.

Non impariamo statistica perché dobbiamo calcolare manualmente ogni formula. La impariamo perché dobbiamo sapere quale conclusione è giustificata dall'evidenza.

Non impariamo data visualization perché dobbiamo disegnare ogni grafico a mano. La impariamo perché dobbiamo riconoscere quando una rappresentazione distorce o chiarisce il fenomeno.

Non impariamo architettura dati perché ogni analista debba amministrare un data warehouse. La impariamo perché il modo in cui il dato viene raccolto, trasformato e modellato influenza ciò che possiamo concludere.

L'AI sta quindi comprimendo il valore della pura esecuzione e aumentando il valore del **giudizio informato**.

---

### Fonti

[^ms-ai-schema]: Microsoft Learn, *Prepare your data for AI - AI data schemas*, aggiornato nel 2026. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-data-schema
[^ms-ai-faq]: Microsoft Learn, *Frequently Asked Questions about Preparing Data for AI - Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq
[^ibm-crisp]: IBM, *Understanding and preparing data*, documentazione CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/en/ws-and-kc?topic=modeler-understanding-preparing-data
