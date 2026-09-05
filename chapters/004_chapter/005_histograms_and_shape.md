## 4.4 Istogrammi e forma: vedere ciò che le statistiche hanno compresso

Media, mediana, dispersione e percentili descrivono punti o regioni della distribuzione. Non ci mostrano però **come le osservazioni occupano lo spazio tra quei punti**. È qui che l'istogramma diventa uno strumento centrale dell'EDA: non aggiunge nuovi dati, ma restituisce parte della struttura che le statistiche sintetiche avevano compresso.

NIST include gli istogrammi tra le tecniche fondamentali dell'analisi esplorativa proprio perché forme simmetriche, asimmetriche, bimodali o a coda lunga possono avere implicazioni molto diverse pur condividendo alcuni riepiloghi numerici.[^nist-hist]

Immaginiamo una catena retail con un average basket value di **47,80 euro**. La media invita a immaginare un ordine tipico vicino a 50 euro. L'istogramma mostra invece due concentrazioni: molti acquisti tra 15 e 30 euro e un secondo gruppo tra 75 e 110. La distribuzione è **bimodale**. Approfondendo scopriamo che il primo gruppo acquista prodotti di consumo ricorrente, mentre il secondo compra bundle e linee premium.

La media continua a essere corretta come rapporto tra ricavi e ordini, ma non rappresenta bene nessuno dei due comportamenti. La forma della distribuzione ha fatto emergere una domanda che nessun valore centrale poteva formulare da solo: **stiamo osservando una popolazione unica o due processi di acquisto differenti mescolati insieme?**

## La forma è una pista sul processo

Una distribuzione simmetrica tende a portare media e mediana vicine. Una forte asimmetria a destra, frequente in ricavi per cliente, importi o durate, indica invece molte osservazioni moderate e poche molto grandi. Una bimodalità può suggerire segmenti o regimi differenti; una distribuzione troncata può segnalare una soglia di processo, censura o un limite di misurazione.

Anche accumuli apparentemente banali possono essere informativi. Se in una survey molti dipendenti dichiarano di lavorare esattamente 40, 45 o 50 ore a settimana, la distribuzione potrebbe raccontare non soltanto il fenomeno ma il modo in cui viene ricordato e registrato. Questo **heaping** è un buon esempio del confine tra Capitolo 3 e Capitolo 4: la Data Readiness Review cerca problemi già noti nella rappresentazione; l'EDA può far emergere strutture inattese che ci obbligano a tornare sul processo di misurazione.

## Anche l'istogramma contiene scelte

La forma che vediamo dipende in parte dalla larghezza dei bin. Intervalli troppo larghi possono cancellare una bimodalità o una coda; intervalli troppo stretti possono trasformare rumore campionario in una sequenza di picchi apparentemente significativi. Non esiste quindi una visualizzazione neutrale in senso assoluto. Se una conclusione dipende fortemente da una particolare scelta dei bin, quella fragilità deve entrare nell'interpretazione.

Per la stessa ragione l'istogramma non dovrebbe diventare un rituale per decidere se i dati “sono normali”. Molti fenomeni di business sono naturalmente asimmetrici, troncati o multimodali. Il compito dell'EDA non è forzare il mondo verso una campana, ma capire **quale processo potrebbe produrre la forma osservata**.

Una distribuzione interessante genera quindi domande successive: quali segmenti producono i diversi picchi? La coda appartiene a pochi clienti o a un'intera categoria? Il limite osservato deriva da una regola operativa? La forma è stabile nel tempo? Media e mediana raccontano esperienze diverse perché la popolazione si è mescolata in modo diverso?

È a questo punto che la descrizione univariata incontra il confronto tra gruppi. Se una forma aggregata nasconde processi differenti, la segmentazione può renderli visibili — ma solo se scegliamo gruppi che abbiano un significato analitico.

> **La distribuzione è il fenomeno osservato; le statistiche descrittive sono prospettive parziali su quella distribuzione.**

[^nist-hist]: NIST/SEMATECH, *Histogram*. https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm
