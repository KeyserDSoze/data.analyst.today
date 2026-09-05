## 5.1 Eventi e probabilità: prima del numero viene il processo

La probabilità non comincia da una formula. Comincia da una frase abbastanza precisa da stabilire **che cosa può accadere, a chi e entro quando**.

“Cliente perso”, per esempio, sembra un evento evidente finché non dobbiamo misurarlo. Può significare mancato rinnovo alla scadenza, cancellazione formale, nessun utilizzo per 90 giorni oppure contrazione del contratto. Le quattro definizioni descrivono quattro eventi diversi e produrranno probabilità diverse anche sullo stesso insieme di clienti.

Il Capitolo 2 ci ha insegnato a trattare una metrica come una definizione. Qui aggiungiamo una conseguenza: una probabilità ha senso soltanto rispetto a **evento, popolazione e orizzonte temporale espliciti**. Dire che “il churn risk è 12%” senza specificare questi elementi equivale a dare un numero prima di aver dichiarato la domanda.

## Da una frequenza storica a un processo incerto

Consideriamo una piattaforma SaaS che riceve circa 2.500 ticket al giorno. Negli ultimi tre mesi il 3,2% dei ticket comparabili è stato escalato al team specialistico. Il responsabile support vuole dimensionare la capacità per domani.

Moltiplicando volume atteso e frequenza storica otteniamo:

`2.500 × 3,2% = 80 escalation attese`.

L'80 non è però una promessa. È il centro di un processo incerto sotto alcune assunzioni: che il volume di domani sia davvero vicino a 2.500, che la composizione dei ticket resti comparabile, che non siano cambiate release o categorie di problema e che il tasso di escalation non dipenda da un mix che domani sarà diverso.

Domani potremmo osservare 68, 83 o 97 escalation senza che nessuno dei tre valori implichi automaticamente un cambiamento strutturale. La probabilità serve proprio a separare il **valore atteso** dall'idea ingenua che il futuro debba ripetere esattamente la frequenza storica.

Lo stesso vale quando trasformiamo una frequenza osservata in una stima futura. Se 14.000 ordini su 200.000 sono stati restituiti, il 7% descrive correttamente lo storico. Per usarlo come probabilità di reso dei prossimi ordini introduciamo una clausola implicita: **le condizioni rilevanti devono restare sufficientemente simili**. Un nuovo mix di prodotto, una diversa politica di reso o l'ingresso in un altro Paese possono rendere il 7% storico perfettamente corretto e, allo stesso tempo, poco utile per ciò che verrà.

## Quando gli eventi si combinano

Supponiamo ora che in una customer base il 46% utilizzi il prodotto almeno quattro volte a settimana, il 78% rinnovi e il 42% faccia entrambe le cose. Stiamo descrivendo tre quantità diverse:

`P(Uso alto) = 46%`

`P(Rinnovo) = 78%`

`P(Uso alto ∩ Rinnovo) = 42%`

Le prime due probabilità riguardano eventi considerati singolarmente. La terza riguarda la loro intersezione. Questa distinzione sarà importante nella sezione successiva, perché passare da “quanto spesso accade A?” a “quanto spesso accade A **tra i casi in cui è vero B**?” significa cambiare denominatore e quindi domanda.

Anche il complemento può essere analiticamente utile. Se l'82% rinnova, il 18% non rinnova:

`P(non rinnovo) = 1 - P(rinnovo)`.

Le due frasi contengono la stessa informazione matematica, ma possono sostenere conversazioni operative diverse. “L'82% rinnova” descrive la continuità; “quasi un cliente su cinque non rinnova” rende più visibile il rischio. L'analista dovrebbe saper usare entrambi i frame senza trasformare il framing in manipolazione.

## Probabilità individuale e frequenza di gruppo

Un ultimo equivoco diventerà ancora più importante quando parleremo di modelli predittivi. Se un modello assegna a un cliente il 70% di probabilità di churn, quel cliente non “churnerà al 70%”: produrrà un solo esito osservato.

Il significato della probabilità diventa verificabile su molti casi comparabili. Se il modello è ben calibrato, tra gruppi di clienti a cui assegna circa il 70% dovremmo osservare, nel lungo periodo e sotto condizioni coerenti, una quota di churn vicina a quel valore. È così che una probabilità individuale acquista significato empirico.

Per evitare che un numero ben formattato nasconda una definizione incompleta, vale la pena conservare una piccola scheda operativa:

```text
Evento:
Popolazione eleggibile:
Orizzonte temporale:
Fonte della stima:
Condizioni assunte stabili:
Decisione che usa la probabilità:
```

Questo non è un esercizio burocratico. È il contratto minimo che ci permette di sapere **che cosa significa davvero il numero** prima di discutere quanto sia preciso.

> **Una probabilità precisa applicata all'evento sbagliato resta una risposta sbagliata.**
