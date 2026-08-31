## 5.8 Campionamento: quando non osserviamo tutta la popolazione

Nella vita reale l'analista raramente dispone di una popolazione perfettamente osservata. A volte i dati esistono solo per un sottoinsieme. A volte la raccolta completa sarebbe troppo lenta o costosa. A volte il processo stesso produce osservazioni solo su una parte dei casi.

Il campionamento non è quindi un dettaglio statistico. È una parte del disegno dell'analisi.

Supponiamo che una catena retail con 1.240 punti vendita voglia stimare il tempo medio che un cliente trascorre in coda alla cassa. Installare sensori e osservatori in ogni negozio per un mese sarebbe costoso. Il team decide quindi di misurare 80 negozi.

Il primo impulso potrebbe essere: scegliamo gli 80 negozi che ci rispondono più velocemente.

È una pessima idea.

I negozi più disponibili potrebbero essere quelli con processi migliori, manager più organizzati e minore pressione operativa. Il campione diventerebbe comodo ma non necessariamente rappresentativo.

### Caso realistico: il sondaggio che diceva che il nuovo prodotto piaceva al 91%

Un'azienda di servizi finanziari lancia una nuova app mobile. Dopo due settimane invia una survey direttamente dentro l'app agli utenti che hanno effettuato almeno tre accessi.

Rispondono 4.800 persone.

Il 91% dichiara di essere soddisfatto.

Il dato viene presentato al management come prova del successo del lancio.

Il problema emerge un mese dopo: il tasso di attivazione degli utenti invitati era solo del 48%, e una parte rilevante degli utenti che avevano aperto l'app una sola volta non era mai arrivata alla survey.

La popolazione di interesse era:

> tutti gli utenti invitati a usare la nuova app.

Il campione osservato era invece:

> utenti abbastanza attivi da aver effettuato almeno tre accessi e abbastanza motivati da completare una survey.

Le 4.800 risposte non erano poche. Il problema non era la dimensione del campione. Era **chi poteva entrare nel campione**.

Questo è un principio fondamentale:

**un campione grande può essere molto preciso nel descrivere la popolazione sbagliata.**

### Random non significa automaticamente rappresentativo

Un campione casuale semplice assegna a ogni unità della popolazione una probabilità nota di essere selezionata. È un buon punto di partenza, ma non risolve ogni problema.

Se la popolazione contiene segmenti molto diversi, può essere utile stratificare.

Nel caso dei negozi, per esempio, potremmo dividere la popolazione per:

- dimensione del punto vendita;
- area geografica;
- formato urbano o extraurbano;
- volume di transazioni;
- presenza o assenza di casse self-service.

Poi potremmo campionare all'interno di ogni strato.

Questo evita che 80 negozi selezionati casualmente finiscano, per puro caso, con l'essere quasi tutti piccoli punti vendita del Nord.

### Il bias non scompare aumentando n

Se il metodo di campionamento è distorto, aumentare il numero di osservazioni non elimina il bias.

Possiamo intervistare 100.000 clienti, ma se intervistiamo solo quelli che hanno rinnovato il contratto non stiamo misurando la soddisfazione di tutti i clienti.

Il campionamento deve quindi essere pensato prima della formula.

La domanda corretta non è soltanto:

> Quante osservazioni abbiamo?

ma anche:

> Da quale meccanismo sono state generate queste osservazioni e chi è rimasto fuori?

### Una regola pratica per l'analista

Prima di utilizzare un campione, scrivi esplicitamente quattro cose:

1. popolazione target;
2. frame di campionamento, cioè l'insieme da cui puoi effettivamente estrarre;
3. metodo di selezione;
4. principali modi in cui una parte della popolazione può essere esclusa.

Questa breve disciplina evita molti errori che nessun test statistico successivo potrà correggere.

### Fonti

[^nist-clt]: NIST/SEMATECH e-Handbook of Statistical Methods, *Normal Distribution and Central Limit Theorem*, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
