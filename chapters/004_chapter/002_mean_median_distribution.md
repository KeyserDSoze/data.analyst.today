## 4.1 Media e mediana: due idee diverse di “valore tipico”

Quando comprimiamo una distribuzione in un solo numero stiamo già scegliendo quale proprietà conservare. È per questo che chiedere semplicemente “qual è il valore medio?” può essere meno innocente di quanto sembri: prima dobbiamo capire **che cosa vogliamo che quel numero rappresenti**.

La **media aritmetica** divide il totale per il numero di osservazioni. È sensibile a ogni valore e conserva quindi il legame con il totale economico sottostante. La **mediana**, invece, è il punto che lascia metà delle osservazioni sotto e metà sopra; descrive la posizione centrale senza farsi trascinare allo stesso modo dalle code. Nessuna delle due domina l'altra in assoluto. Rispondono a domande diverse.

Consideriamo una startup tecnologica con 41 dipendenti. Lo stipendio medio annuo è **62.400 euro**, mentre la mediana è **46.800 euro**. La differenza nasce da una distribuzione molto asimmetrica: 18 persone guadagnano tra 32.000 e 40.000 euro, 13 tra 40.000 e 55.000, 6 tra 55.000 e 75.000, tre dirigenti superano 140.000 euro e il CEO arriva a 260.000.

Se dobbiamo stimare il costo salariale per dipendente, la media è precisamente ciò che ci serve: i salari elevati pesano davvero sul totale. Se invece vogliamo descrivere l'esperienza retributiva del dipendente centrale, la mediana è più vicina alla domanda. Il problema nasce quando entrambe vengono chiamate genericamente “stipendio tipico”, come se stessero cercando di rappresentare la stessa cosa.

La stessa tensione appare negli ordini. Con cinque importi da `€20, €25, €30, €35, €390`, la media è `€100` e la mediana `€30`. Dire che la media “è falsata dall'outlier” sarebbe troppo sbrigativo. L'ordine da 390 euro è reale e contribuisce al fatturato; la media registra correttamente quel peso. Semplicemente non descrive bene il singolo ordine più comune.

## Il centro dipende anche dall'unità su cui lo calcoliamo

Prima ancora di scegliere tra media e mediana dobbiamo ricordare il Capitolo 3: il grain determina ciò che stiamo mediando. “Ricavo medio” può significare ricavo per ordine, per cliente, per giorno, per prodotto o per sessione. Sono statistiche diverse anche se provengono dallo stesso warehouse.

Per questo una frase come “AOV medio = 100 euro” è già migliore di “ricavo medio = 100 euro”, ma non è ancora completa se non sappiamo quali ordini entrano nella popolazione, in quale periodo e con quali esclusioni. La statistica descrittiva non elimina la semantica costruita nei capitoli precedenti; la utilizza.

## Quando media e mediana divergono, la divergenza merita attenzione

Una distanza ampia tra le due misure è spesso il primo indizio che il centro non basta. Può indicare una coda lunga, forte asimmetria, concentrazione economica, più popolazioni mescolate o poche osservazioni molto influenti. Non dobbiamo decidere immediatamente quale numero “vince”. Dobbiamo guardare la distribuzione che li ha prodotti.

Supponiamo che un servizio di assistenza riporti un tempo medio di risposta di **3,2 ore**. Da solo, il numero lascia aperte molte interpretazioni. Se aggiungiamo mediana **1,1 ore** e `P90 = 8,7 ore`, scopriamo che la maggioranza riceve risposta rapidamente mentre una coda relativamente piccola ma molto lenta spinge il valore medio verso l'alto. Il secondo riepilogo non è migliore perché contiene più numeri; è migliore perché conserva più della struttura che conta per l'esperienza.

Questo porta direttamente alla prossima sezione. Una misura centrale ci dice dove si colloca la distribuzione. Non ci dice **quanto le osservazioni sono concentrate attorno a quel centro**.

> **Una media non è “il dato”. È una particolare compressione della distribuzione, utile soltanto quando sappiamo quale proprietà vogliamo preservare.**
