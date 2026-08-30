## 5.6 Legge dei grandi numeri: perché i KPI piccoli oscillano tanto

Uno dei fenomeni che confonde più spesso manager e analisti junior è la volatilità dei piccoli numeri.

Un conversion rate può passare dal 4% al 9% in una giornata e sembrare un successo straordinario. Ma se quella giornata contiene soltanto 40 visite, il cambiamento può essere quasi interamente casuale.

La legge dei grandi numeri ci aiuta a capire perché, quando il numero di osservazioni cresce, una media o una frequenza osservata tende a stabilizzarsi attorno al suo valore atteso.

Non significa che grandi dataset eliminino tutti i problemi. Bias, errori di misura e confondenti possono rimanere perfettamente presenti anche con miliardi di righe.

Significa soltanto che la variabilità casuale di certe stime tende a ridursi quando aumentano le osservazioni indipendenti e comparabili.

### Caso realistico: il negozio “migliore” della rete

Una catena retail confronta il conversion rate di 84 negozi.

Il negozio di Aosta mostra il conversion rate più alto della settimana: 38%.

Milano Centrale è al 24%.

La classifica viene presentata nella riunione commerciale e qualcuno propone di studiare Aosta come best practice.

L'analista aggiunge però il volume:

| Negozio | Visitatori | Acquisti | Conversion rate |
|---|---:|---:|---:|
| Aosta | 42 | 16 | 38,1% |
| Milano Centrale | 4.920 | 1.181 | 24,0% |

La settimana precedente Aosta aveva avuto 37 visitatori e 7 acquisti: 18,9%.

Il tasso è quasi raddoppiato senza che sia cambiato nulla nel processo commerciale.

Con campioni così piccoli, pochi clienti cambiano drasticamente la percentuale.

Milano, con quasi cinquemila visitatori, ha invece un indicatore molto più stabile.

### Più dati, meno rumore casuale

Supponiamo che la probabilità reale di conversione sia 25%.

Con 20 visitatori, il valore atteso è 5 acquisti, ma ottenere 3 oppure 8 acquisti non è particolarmente sorprendente. I conversion rate osservati sarebbero rispettivamente 15% e 40%.

Con 20.000 visitatori, oscillazioni proporzionalmente così grandi diventano molto meno plausibili.

Questo è il motivo per cui dashboard con decine di micro-segmenti producono spesso “insight” spettacolari ma instabili.

### La trappola delle classifiche

Se confrontiamo centinaia di filiali, campagne o venditori, alcuni saranno inevitabilmente molto sopra o molto sotto la media semplicemente per variabilità casuale.

I valori estremi tendono inoltre a mostrare **regressione verso la media** nelle osservazioni successive.

Il “peggior negozio del mese” può migliorare il mese seguente anche senza alcun intervento, semplicemente perché una parte della performance precedente era rumore.

Lo stesso vale per il migliore.

### Caso realistico: il medico con il tasso di complicazioni più alto

Una rete sanitaria confronta il tasso di complicazioni post-operatorie tra strutture.

Una clinica piccola registra 3 complicazioni su 24 interventi: 12,5%.

Un grande ospedale ne registra 48 su 920: 5,2%.

Guardando soltanto le percentuali, la clinica sembra più che doppiare il rischio.

Ma tre soli casi determinano completamente il risultato. Un singolo caso in meno avrebbe portato il tasso a 8,3%.

Prima di trarre conclusioni sulla qualità clinica servono volumi, intervalli di incertezza, differenze nel case mix e aggiustamenti per il rischio.

Il principio è generale: **più il denominatore è piccolo, più dobbiamo diffidare delle percentuali estreme**.

### Big data non significa automatically good data

La legge dei grandi numeri non salva un dataset distorto.

Se un questionario online raccoglie un milione di risposte ma partecipano soprattutto clienti molto soddisfatti o molto insoddisfatti, aumentare il campione non elimina il selection bias.

Se un sensore è calibrato male, un miliardo di misurazioni può stimare con grandissima precisione il valore sbagliato.

Questa distinzione è fondamentale:

**più osservazioni riducono l'errore casuale, non necessariamente l'errore sistematico.**

### La domanda operativa

Quando vediamo un KPI estremo chiediamoci:

- qual è il denominatore?
- quante osservazioni sostengono il numero?
- quanto era volatile storicamente?
- il valore si replica su più periodi?
- stiamo osservando un segnale o semplicemente una realizzazione estrema del rumore?

La probabilità serve anche a questo: evitare di trasformare ogni oscillazione in una storia.
