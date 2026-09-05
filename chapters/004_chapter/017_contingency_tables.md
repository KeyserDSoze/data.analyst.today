## 4.16 Tabelle di contingenza: il significato cambia con il denominatore

Molte domande di business mettono in relazione categorie, non grandezze continue: cliente nuovo o esistente, piano mensile o annuale, churn sì o no, canale organico o paid, ticket risolto al primo contatto oppure no. In questi casi una **tabella di contingenza** rende visibile come i casi si distribuiscono tra combinazioni di categorie.

Il punto analitico non è soltanto contare le celle. È decidere **rispetto a quale popolazione vogliamo leggerle**.

Consideriamo **CloudDesk**, società SaaS con 24.000 clienti. Nel totale osserviamo:

| Piano | Clienti | Churn | Churn rate |
|---|---:|---:|---:|
| Mensile | 14.000 | 2.240 | 16,0% |
| Annuale | 10.000 | 700 | 7,0% |

La differenza è abbastanza grande da suggerire al team commerciale una spinta aggressiva verso l'annuale. Prima di trasformare l'associazione in una strategia, però, l'analista aggiunge la **customer tenure**.

Tra i clienti con meno di sei mesi, il churn è 18,1% sul mensile e 16,4% sull'annuale. Tra quelli con almeno sei mesi, invece, è 12,8% contro 4,7%. L'associazione non scompare, ma cambia forma; inoltre il piano annuale contiene una quota molto più alta di clienti maturi.

Il totale iniziale stava quindi mescolando almeno due strutture: differenze tra piano mensile e annuale e diversa composizione per anzianità. L'EDA non deve ancora stabilire quale sia causalmente responsabile del churn. Deve rendere visibile **quanto l'associazione aggregata dipenda dalla popolazione che compone ciascun gruppo**.

## Riga, colonna e totale rispondono a domande diverse

La stessa tabella può essere normalizzata per riga, per colonna o sul totale, e ciascuna lettura cambia il denominatore. Se chiediamo “tra i clienti mensili, quale quota fa churn?”, il denominatore è il totale dei mensili. Se chiediamo “tra chi ha fatto churn, quale quota aveva il piano mensile?”, il denominatore è il totale dei churner.

Questa differenza sembra formale, ma corrisponde a due domande di business completamente diverse. Confonderle è un modo molto comune di ottenere una percentuale corretta e interpretarla male.

Anche numerosità e percentuale devono rimanere visibili insieme. Un churn del 30% può significare 3 casi su 10 oppure 3.000 su 10.000. La frequenza relativa coincide; la stabilità del pattern e l'impatto operativo no. L'EDA dovrebbe quindi conservare **tasso e base** ogni volta che segmenti piccoli rischiano di apparire prioritari soltanto perché producono percentuali estreme.

Dal caso CloudDesk possiamo concludere che piano, tenure e churn sono associati. Non possiamo ancora dire che convertire un cliente mensile all'annuale ridurrà il suo churn: chi sceglie un annuale può essere già più convinto del prodotto, più maturo o diverso per altre caratteristiche. Il Capitolo 5 introdurrà l'incertezza statistica dell'associazione; il Capitolo 8 affronterà la domanda causale.

Prima, però, dobbiamo consolidare il principio che regge anche questa tabella: **una percentuale eredita il significato dal suo denominatore**. È il tema della prossima sezione.

> **Una tabella di contingenza non dice soltanto quanti casi cadono in ogni cella. Costringe a dichiarare da quale popolazione stiamo guardando la relazione.**
