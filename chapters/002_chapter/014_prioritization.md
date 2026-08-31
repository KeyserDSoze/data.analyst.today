## 2.13 Prioritizzare le analisi: non tutte le domande meritano la stessa profondità

Un team analytics può ricevere molte più domande di quante ne possa affrontare bene.

La capacità di prioritizzare è quindi parte del metodo analitico, non soltanto della gestione del backlog.

Una richiesta può essere urgente ma irrilevante. Un'altra può essere economicamente importante ma già ben compresa. Una terza può contenere grande incertezza ma nessuna decisione imminente.

### Quattro dimensioni utili

Per ordinare le richieste possiamo ragionare almeno su:

1. **Impatto decisionale** — quanto può cambiare un risultato economico, operativo o strategico?
2. **Urgenza** — quando deve essere presa la decisione?
3. **Incertezza riducibile** — quanto poco sappiamo oggi e quanto l'analisi può davvero migliorare la situazione?
4. **Costo** — tempo, dati, dipendenze, complessità e manutenzione richiesti.

Non serve trasformare questi elementi in una formula pseudo-scientifica. Una scorecard qualitativa è spesso sufficiente.

| Richiesta | Impatto | Urgenza | Incertezza riducibile | Costo | Priorità |
|---|---:|---:|---:|---:|---:|
| churn enterprise +20% | alto | alta | alta | medio | alta |
| redesign grafico report stabile | basso | bassa | bassa | basso | bassa |
| forecast capacità Q4 | alto | media | media | alto | media/alta |

Il valore della tabella è rendere discutibile la priorità in termini di decisione, non di seniority del requester.

### La trappola del richiedente più rumoroso

In molte organizzazioni il backlog viene ordinato implicitamente da chi insiste di più o occupa la posizione più senior.

L'analista può riportare la conversazione a una domanda più utile:

> **“Quale decisione migliorerà se investiamo capacità qui invece che altrove?”**

Questo non elimina la politica organizzativa. Ma rende visibile il costo opportunità.

### Versione minima prima della versione completa

Prioritizzare non significa soltanto dire sì o no.

Possiamo ridurre il costo iniziale con:

- un sanity check di 30 minuti;
- un memo con una sola decomposizione;
- un campione;
- una metrica proxy;
- un'analisi offline prima di una dashboard;
- una fase 1 diagnostica prima di un modello.

La versione minima serve a capire se esiste abbastanza segnale da giustificare un investimento maggiore.

### Quando dire no

Una richiesta può essere deprioritizzata quando:

- nessun risultato plausibile cambierebbe una decisione;
- il costo dell'analisi supera l'impatto ragionevole;
- manca un owner disposto ad agire;
- la domanda richiede dati che non esistono e non c'è piano per raccoglierli;
- un prodotto analitico già esistente risponde abbastanza bene;
- un controllo semplice elimina già l'incertezza rilevante.

Dire no in questi casi significa proteggere capacità analitica per problemi più importanti.

### AI e abbondanza di output

Quando query, grafici e sintesi diventano più economici, può aumentare il numero di richieste che sembrano “facili”.

Ma una query da trenta secondi può creare ore di interpretazione, review, manutenzione e aspettative future.

Per questo il costo marginale dell'esecuzione non coincide con il **costo totale del prodotto analitico**.

> **Il team analytics non dovrebbe massimizzare il numero di domande a cui risponde. Dovrebbe massimizzare il valore delle incertezze che riesce a ridurre.**
