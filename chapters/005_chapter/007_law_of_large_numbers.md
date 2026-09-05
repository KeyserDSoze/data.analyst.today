## 5.6 Legge dei grandi numeri: più osservazioni stabilizzano il rumore, non il bias

Un KPI su pochi casi può sembrare spettacolare perché bastano pochissimi esiti per spostarlo di molti punti. Questo non rende il numero falso. Significa che la sua **variabilità casuale è grande rispetto alla base che lo sostiene**.

La legge dei grandi numeri formalizza l'intuizione opposta: sotto condizioni appropriate, aumentando il numero di osservazioni indipendenti e comparabili una media o una frequenza tende a stabilizzarsi attorno al proprio valore atteso.

La formulazione va tenuta stretta. La legge non dice “big data = verità”. Dice che più osservazioni possono ridurre una componente specifica dell'incertezza: **il rumore casuale dovuto al fatto di aver osservato un insieme finito di esiti**.

## Il negozio migliore della settimana

Una catena retail confronta 84 punti vendita.

| Negozio | Visitatori | Acquisti | Conversion rate |
|---|---:|---:|---:|
| Aosta | 42 | 16 | 38,1% |
| Milano Centrale | 4.920 | 1.181 | 24,0% |

Se ordiniamo la classifica, Aosta sembra straordinaria. La settimana precedente, però, aveva registrato 37 visitatori, 7 acquisti e conversion rate del 18,9%. Il tasso è quasi raddoppiato senza cambiamenti noti di promozione, layout o processo commerciale.

Con 42 visitatori, pochi acquisti in più o in meno muovono enormemente la percentuale. Con quasi 5.000 visitatori, la stima di Milano è molto meno volatile. Non abbiamo un “numero vero” e uno falso: abbiamo due stime con **precisione molto diversa**.

Questo è il ponte verso standard error e confidence interval. Prima, però, vale la pena osservare una conseguenza pratica: quando classifichiamo molte unità, quelle con denominatori piccoli hanno più probabilità di comparire agli estremi proprio perché oscillano di più.

Per questo “studiamo il top performer del mese e copiamo ciò che fa” può essere una strategia ingenua. Il top può essere davvero eccellente, ma può anche essere stato selezionato nel momento in cui una componente casuale lo ha spinto molto in alto. Serve verificare se il ranking persiste su più periodi, quante osservazioni lo sostengono e quanto cambia quando la stima viene accompagnata dalla propria incertezza.

## Regressione verso la media: gli estremi non restano sempre estremi

Quando scegliamo un caso proprio perché è eccezionale, la misurazione successiva tende spesso a essere meno estrema. Una parte della performance precedente può essere stata rumore.

Un negozio scelto come “peggiore” dopo una settimana eccezionalmente negativa può migliorare senza che l'intervento appena introdotto sia la causa. Il migliore può peggiorare senza aver perso competenza. Questa **regressione verso la media** diventerà particolarmente importante nei capitoli sulla causalità: confrontare “prima” e “dopo” su unità selezionate perché erano estreme può attribuire all'intervento un movimento che sarebbe avvenuto in parte comunque.

## Un milione di risposte può essere un milione di risposte sbagliate per la domanda

La numerosità, però, non affronta ogni errore. Supponiamo di raccogliere un milione di risposte volontarie a una survey. Il sampling noise all'interno di quel gruppo può diventare minuscolo. Ma se chi risponde è sistematicamente diverso dalla popolazione che vogliamo descrivere, possiamo ottenere una stima estremamente precisa della popolazione sbagliata.

AAPOR separa proprio il margin of sampling error da componenti come coverage, measurement e nonresponse.[^aapor-definitions] La precisione campionaria può quindi aumentare senza che migliori la rappresentatività.

Lo stesso principio vale fuori dalle survey. Se un sensore sovrastima sistematicamente la temperatura di 2 °C, passare da mille a un miliardo di misurazioni non elimina il bias: restringe l'incertezza attorno a una misura sistematicamente spostata.

È utile tenere separate due leve:

> **sample size riduce soprattutto rumore casuale; design, misurazione e rappresentatività affrontano altri errori.**

Quando un KPI appare improvvisamente estremo, il controllo non dovrebbe quindi fermarsi al denominatore. Dobbiamo chiederci quante osservazioni sostengono il numero, quanto una stima di quella dimensione tende normalmente a oscillare, se il risultato persiste e se abbiamo ragioni indipendenti per credere che i dati rappresentino bene la popolazione che ci interessa.

La sezione sul campionamento mostrerà che questa ultima domanda viene logicamente **prima** di qualsiasi formula di precisione.

> **Più dati possono rendere una stima più precisa. Solo un processo di osservazione adeguato può renderla anche credibile per la popolazione che vogliamo descrivere.**

---

### Fonte

[^aapor-definitions]: AAPOR, *Standard Definitions*, 10th edition. https://aapor.org/standards-and-ethics/standard-definitions/
