## 5.6 Legge dei grandi numeri: più osservazioni stabilizzano il rumore, non il bias

Uno dei fenomeni che confonde più spesso l'interpretazione dei KPI è la volatilità dei **piccoli denominatori**.

Un conversion rate può passare dal 4% al 9% e sembrare un cambiamento enorme. Se però deriva da poche decine di visite, bastano pochissimi acquisti in più per produrre il salto.

La **legge dei grandi numeri** formalizza un'intuizione importante: sotto condizioni appropriate, quando aumentano le osservazioni indipendenti e comparabili, una media o una frequenza osservata tende a stabilizzarsi attorno al proprio valore atteso.

Non dice che “big data = verità”.

Dice qualcosa di molto più limitato e utile:

> **aumentando il numero di osservazioni riduciamo in genere una parte della variabilità casuale.**

### Caso simulato/composito — Il negozio migliore della rete

Una catena retail confronta 84 punti vendita.

| Negozio | Visitatori | Acquisti | Conversion rate |
|---|---:|---:|---:|
| Aosta | 42 | 16 | 38,1% |
| Milano Centrale | 4.920 | 1.181 | 24,0% |

Aosta è prima nella classifica settimanale.

La settimana precedente aveva però registrato:

- 37 visitatori;
- 7 acquisti;
- conversion rate 18,9%.

Il tasso è quasi raddoppiato senza che il team abbia cambiato promozioni, layout o processo commerciale.

Con 42 visitatori, pochi esiti muovono enormemente la percentuale. Con quasi 5.000 visitatori, la stima di Milano è molto meno volatile.

Questo non significa che Milano abbia “il valore vero” e Aosta no. Significa che le due percentuali hanno **precisione diversa**.

Le sezioni su standard error e intervalli di confidenza quantificheranno esattamente questa differenza.

### La classifica crea estremi anche quando non c'è una storia speciale

Se confrontiamo decine o centinaia di negozi, campagne, seller o account executive, alcuni finiranno inevitabilmente molto in alto e altri molto in basso anche per semplice variabilità casuale.

Questo rende pericolose frasi come:

> “Studiamo il top performer del mese e copiamo ciò che fa.”

Prima dobbiamo capire quanto della performance estrema sia persistente.

Un modo semplice è verificare:

- più settimane o mesi;
- numerosità della base;
- intervalli di incertezza;
- stabilità del ranking;
- performance dopo il periodo in cui il soggetto è stato selezionato come estremo.

### Regressione verso la media

I casi selezionati perché estremi tendono spesso a essere meno estremi alla misurazione successiva.

Non necessariamente perché il processo sia migliorato o peggiorato. Una parte del valore precedente può essere stata rumore.

Un negozio scelto come “peggiore” dopo una settimana eccezionalmente negativa può migliorare anche senza intervento. Il migliore può peggiorare senza aver perso competenza.

Questo fenomeno, **regressione verso la media**, è una ragione in più per non attribuire automaticamente ogni movimento successivo all'azione appena implementata.

Lo ritroveremo nei capitoli su causalità ed experimentation.

### Più dati non correggono una selezione sbagliata

Supponiamo di avere un sondaggio con un milione di risposte volontarie.

La numerosità può rendere piccolissimo l'errore casuale **all'interno di quel gruppo di rispondenti**. Ma se chi risponde è sistematicamente diverso dalla popolazione che vogliamo descrivere, l'estrema precisione non risolve il problema.

AAPOR distingue infatti l'errore di campionamento da altre fonti di errore come coverage, measurement e nonresponse.[^aapor-definitions]

Il principio è fondamentale:

> **un campione enorme può stimare con grandissima precisione la popolazione sbagliata.**

Nella sezione 5.8 vedremo un caso storico famoso proprio su questo punto.

### Sensore sbagliato, miliardi di righe

Lo stesso vale fuori dai survey.

Se un sensore sovrastima sistematicamente la temperatura di 2 °C, aumentare da mille a un miliardo di misurazioni non elimina il bias. Riduce l'incertezza attorno a una misura sistematicamente spostata.

Quindi:

- **sample size** aiuta contro il rumore casuale;
- **design, misurazione e rappresentatività** affrontano altre fonti di errore.

Confondere questi livelli è uno degli errori più costosi della statistica applicata.

### La domanda operativa

Quando vediamo un KPI estremo chiediamoci:

1. qual è il denominatore?
2. quante osservazioni sostengono il numero?
3. quanto oscilla normalmente una stima di questa dimensione?
4. il risultato persiste nel tempo?
5. stiamo riducendo incertezza casuale o abbiamo anche ragioni per credere che il dato rappresenti bene la popolazione?

> **Più dati possono rendere una stima più precisa. Solo un buon processo di raccolta può renderla anche più credibile.**

[^aapor-definitions]: AAPOR, *Standard Definitions*: https://aapor.org/standards-and-ethics/standard-definitions/
