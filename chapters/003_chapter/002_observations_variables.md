## 3.1 Osservazioni, variabili e unità di analisi

Il primo contatto con un dataset dovrebbe essere meno ambizioso di quanto sembri. Prima di calcolare una media o costruire un grafico dobbiamo riuscire a spiegare che cosa rappresentano una riga e una colonna. Dietro queste due domande elementari si nasconde la distinzione tra **record**, **entità** e **osservazione**.

Un record è ciò che il sistema ha memorizzato. L'entità è l'oggetto reale o concettuale che ci interessa — cliente, ordine, prodotto, contratto. L'osservazione è invece l'unità sulla quale stiamo formulando una conclusione. A volte coincidono; spesso no.

Consideriamo una tabella come questa:

| order_id | customer_id | product_id | quantity | price |
|---|---|---|---:|---:|
| 1001 | C17 | P8 | 2 | 35.00 |
| 1001 | C17 | P4 | 1 | 12.00 |

Il nome `order_id` può indurre a leggere ogni riga come un ordine. La ripetizione dello stesso identificatore rivela però che la riga rappresenta più probabilmente **un prodotto all'interno dell'ordine**. Due righe, quindi, non significano due ordini. Questa differenza sembra piccola finché non costruiamo un KPI; a quel punto può raddoppiare conteggi, replicare importi e cambiare denominatori.

Lo stesso meccanismo ricorre continuamente: un cliente può avere più contratti, un ticket più eventi di stato, un pagamento più tentativi, un prodotto uno snapshot per magazzino e giorno. Il record fisico descrive il modo in cui il sistema ha scelto di rappresentare il processo, non necessariamente il modo in cui la nostra domanda analitica vuole osservarlo.

Per questo la frase più utile è ancora:

> **Una riga di questa tabella rappresenta...**

Finché non possiamo completarla senza ambiguità, qualsiasi aggregazione resta sospetta.

## Il grain fisico non decide da solo l'unità analitica

Una sorgente può essere a livello di riga d'ordine mentre la domanda riguarda l'ordine nel suo complesso. Per studiare il valore medio degli ordini dovremo ricostruire il livello ordine; per analizzare il mix di prodotto, invece, il grain della riga d'ordine può essere proprio quello corretto. Per una retention dovremo probabilmente risalire a cliente e coorte.

Il passaggio tra grain fisico e unità logica deve quindi essere una trasformazione esplicita, non un effetto collaterale della query. Ogni volta che cambiamo livello stiamo decidendo quali record appartengono alla stessa osservazione e quali misure possono essere aggregate senza perdere significato.

Questo collega direttamente la struttura del dataset al brief del Capitolo 2: l'unità di analisi non nasce dal nome della tabella, ma dalla domanda.

## Una colonna ha una storia, non soltanto un tipo

Lo stesso vale per le variabili. Sapere che `age` è un intero o che `status` è una stringa ci dice come il database memorizza il valore, non che cosa il valore significhi.

`age = 37` può essere l'età dichiarata alla registrazione, quella calcolata oggi o quella valida al momento dell'evento. `status = active` può indicare un contratto non cancellato, un login recente, un account non disabilitato o un cliente che continua a generare ricavi. Tutte queste definizioni possono essere tecnicamente legittime e analiticamente incompatibili.

Per una variabile critica dobbiamo quindi conoscere il significato di business, il tipo tecnico, il dominio dei valori ammessi, l'unità di misura quando esiste, il momento a cui il valore è valido e il processo che lo produce. Non serve compilare una scheda perfetta per ogni colonna; serve farlo per quelle da cui dipendono metriche e conclusioni.

Un esempio rende il problema concreto. In un sistema di assistenza `status = closed` sembra una misura naturale dei ticket risolti. Il domain expert spiega però che il sistema chiude automaticamente dopo quattordici giorni anche i ticket senza risposta del cliente. Il campo è valido e correttamente popolato, ma non rappresenta il concetto che l'analista aveva in mente.

È questo il movimento centrale del data understanding:

**struttura fisica → significato semantico → unità analitica**.

Solo dopo questa traduzione possiamo iniziare a trattare una riga come evidenza e una colonna come misura.
