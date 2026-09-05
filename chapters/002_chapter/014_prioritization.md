## 2.13 Prioritizzare: scegliere quale incertezza merita capacità analitica

Un team analytics può ricevere molte più domande di quante ne possa affrontare bene. Per questo la prioritizzazione non è soltanto gestione del backlog: è una conseguenza dello stesso principio che guida il brief. Se l'analisi serve a ridurre incertezza attorno a decisioni, allora due richieste non hanno lo stesso valore solo perché richiedono lo stesso numero di ore.

Una richiesta può essere urgente ma avere conseguenze trascurabili. Un'altra può riguardare milioni di euro ma essere già compresa abbastanza bene da non richiedere nuova analisi. Una terza può contenere grande incertezza, ma nessun owner è in grado di agire sul risultato. Il costo opportunità nasce proprio qui: ogni ora spesa su una domanda sottrae capacità a un'altra.

## Impatto, urgenza, incertezza riducibile e costo

Una scorecard semplice può rendere questa discussione più esplicita. Le quattro dimensioni più utili sono **impatto decisionale**, **urgenza**, **incertezza riducibile** e **costo**.

L'impatto chiede quanto potrebbe cambiare un risultato economico, operativo o strategico. L'urgenza dipende da quando la decisione deve essere presa, non da quanto spesso il requester sollecita il team. L'incertezza riducibile distingue problemi su cui l'analisi può realmente aggiungere informazione da problemi già abbastanza compresi. Il costo include non soltanto le ore per produrre una query, ma anche dipendenze, qualità dei dati, manutenzione, review e aspettative di supporto futuro.

La tabella serve a rendere confrontabili richieste diverse, non a produrre un punteggio pseudo-scientifico:

| Richiesta | Impatto | Urgenza | Incertezza riducibile | Costo | Priorità |
|---|---:|---:|---:|---:|---:|
| churn enterprise +20% | alto | alta | alta | medio | alta |
| redesign grafico report stabile | basso | bassa | bassa | basso | bassa |
| forecast capacità Q4 | alto | media | media | alto | media/alta |

Il vantaggio è organizzativo: la priorità diventa discutibile in termini di decisione e costo opportunità, invece di seguire automaticamente la seniority o l'insistenza del requester.

## Prima di finanziare l'analisi completa, compra informazione a basso costo

Prioritizzare non significa scegliere soltanto fra “sì” e “no”. Spesso il modo migliore per ridurre rischio è costruire una versione minima dell'indagine: un sanity check, una singola decomposizione, un campione, una metrica proxy dichiarata o una fase diagnostica offline prima di investire in una dashboard o in un modello.

Questa prima tranche di lavoro ha una funzione precisa: capire se esiste abbastanza segnale da giustificare il costo successivo. Un controllo di trenta minuti può mostrare che l'anomalia deriva da un cambio di tracking; in quel caso costruire un prodotto ricorrente sarebbe spreco. Al contrario, un controllo rapido può rivelare che il churn enterprise sta aumentando proprio prima di un rinnovo annuale e rendere razionale spostare capacità da richieste meno materiali.

## Dire no protegge il valore del team

Una richiesta merita di essere deprioritizzata quando nessun risultato plausibile cambierebbe una decisione, quando il costo analitico supera l'impatto ragionevole, quando manca un owner disposto ad agire o quando un prodotto esistente risponde già abbastanza bene. Lo stesso vale quando i dati necessari non esistono e nessuno intende raccoglierli, oppure quando un controllo semplice elimina già l'incertezza che motivava la richiesta.

In questi casi dire no non significa essere meno orientati al business. Significa riconoscere che la capacità analitica è una risorsa scarsa e deve essere allocata come qualsiasi altra risorsa.

L'AI rende questo problema più sottile. Se query, grafici e memo diventano economici, aumenta il numero di richieste che sembrano “facili”. Ma una query generata in trenta secondi può creare ore di interpretazione, review, supporto e manutenzione. Il costo marginale dell'esecuzione non coincide con il **costo totale del prodotto analitico**.

> **Un team analytics non dovrebbe massimizzare quante richieste chiude. Dovrebbe massimizzare il valore delle incertezze che riesce a ridurre con la capacità disponibile.**
