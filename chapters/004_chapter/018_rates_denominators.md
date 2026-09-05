## 4.17 Conteggi, proporzioni e tassi: il denominatore decide quale rischio stiamo descrivendo

Un conteggio dice quante volte è avvenuto qualcosa. Un tasso o una proporzione mette quell'evento in relazione con la popolazione o l'esposizione che avrebbe potuto produrlo. Il passaggio sembra elementare, ma può invertire completamente la priorità operativa.

**IronPeak Components** gestisce tre stabilimenti. Torino registra 18 incidenti, Verona 11 e Bari 9. Il primo report mette Torino in rosso perché ha il doppio degli incidenti di Bari. Quando però aggiungiamo le ore lavorate, la lettura cambia:

| Stabilimento | Incidenti | Ore lavorate | Incidenti per 100.000 ore |
|---|---:|---:|---:|
| Torino | 18 | 610.000 | 2,95 |
| Verona | 11 | 280.000 | 3,93 |
| Bari | 9 | 170.000 | 5,29 |

Torino produce più incidenti assoluti perché è lo stabilimento più grande; Bari mostra il rischio più alto per unità di esposizione. Se dobbiamo capire **dove il processo è più rischioso**, il tasso è centrale. Se dobbiamo dimensionare il numero totale di persone, investigazioni o giornate perse, il conteggio continua ad avere valore. Normalizzare non cancella il volume: risponde a una domanda diversa.

Il CDC usa lo stesso principio nell'epidemiologia descrittiva: i tassi rendono confrontabili conteggi provenienti da popolazioni o periodi di dimensione diversa soltanto quando il denominatore rappresenta in modo appropriato la popolazione da cui gli eventi sono emersi.[^cdc-rates]

## Il denominatore è una definizione del fenomeno

Prima di leggere una percentuale dobbiamo sapere chi era eleggibile a produrre l'evento, quanta esposizione aveva, se numeratore e denominatore coprono lo stesso periodo e quale unità stiamo contando.

Prendiamo un `return_rate`. Può significare ordini con almeno un reso diviso ordini consegnati, unità restituite diviso unità vendute oppure valore economico restituito diviso valore venduto. Tutte e tre le metriche possono essere corrette; rispondono a domande diverse su esperienza dell'ordine, qualità dei prodotti e impatto economico.

Lo stesso fenomeno appare nel tempo. Se le cancellazioni mensili passano da 900 a 1.100 mentre gli abbonati attivi crescono da 25.000 a 40.000, il conteggio aumenta del 22,2% ma il tasso scende dal 3,6% al 2,75%. Customer Success può preoccuparsi del carico assoluto di cancellazioni; chi valuta la salute della base può considerare positivo il rischio relativo. Nessuna delle due prospettive è completa senza sapere quale decisione stiamo supportando.

## Un denominatore corretto può ancora descrivere popolazioni non comparabili

Supponiamo che un marketplace osservi 240 reclami su 120.000 ordini per il seller A, cioè 2,0 per mille, e 90 su 18.000 per B, cioè 5,0 per mille. Il tasso normalizzato rende B apparentemente peggiore. Se però B vende quasi esclusivamente prodotti complessi con una probabilità intrinseca di reclamo molto maggiore, `reclami / ordini` può essere aritmeticamente corretto e analiticamente incompleto.

Il denominatore ha corretto la differenza di volume, ma non il **mix di rischio**. È per questo che normalizzazione e comparabilità devono rimanere concetti distinti.

Una frase semplice aiuta a proteggere il significato:

> **Il numeratore conta ________; il denominatore rappresenta ________; entrambi coprono il periodo ________ e la popolazione eleggibile ________.**

Se non possiamo completarla senza ambiguità, la percentuale non è ancora sufficientemente definita per sostenere un confronto.

La sezione successiva aggiunge l'ultimo pezzo: anche con numeratore e denominatore corretti, due gruppi possono operare in condizioni troppo diverse perché la stessa metrica produca una classifica sensata.

> **Una percentuale non è un numero autonomo. È una frase compressa su evento, esposizione, tempo e popolazione.**

[^cdc-rates]: CDC, *Describing Epidemiologic Data*, Field Epidemiology Manual. https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html
