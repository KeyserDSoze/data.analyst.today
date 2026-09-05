## 5.2 Probabilità condizionata: il rischio cambia quando cambia il contesto

Una probabilità marginale descrive il fenomeno sull'intera popolazione considerata. Molte decisioni reali, però, iniziano quando scopriamo che quella popolazione non è omogenea.

Non chiediamo più soltanto “qual è la probabilità di churn?”, ma “qual è la probabilità di churn **tra i clienti che non effettuano login da 21 giorni?**”. Non chiediamo soltanto il return rate, ma il return rate **tra le calzature**, o tra gli ordini acquistati in promozione, o tra i nuovi clienti.

La probabilità condizionata formalizza esattamente questo cambio di prospettiva:

`P(A|B) = P(A ∩ B) / P(B)`

quando `P(B) > 0`.

La formula è breve. La trasformazione concettuale è più importante: **B ridefinisce il denominatore**. Stiamo chiedendo quanto spesso osserviamo A all'interno dei casi in cui B è vero.

## Dal churn aggregato a una struttura di rischio

Una società SaaS B2B ha 18.400 clienti attivi. Il churn complessivo è utile per descrivere il portafoglio, ma racconta poco su dove il rischio sia concentrato. L'analista segmenta quindi la base in funzione dell'attività degli ultimi 30 giorni e osserva il churn nei 90 giorni successivi.

| Attività ultimi 30 giorni | Clienti | Churn nei 90 giorni successivi |
|---|---:|---:|
| Alta | 6.900 | 2,4% |
| Media | 7.100 | 6,8% |
| Bassa | 3.200 | 17,9% |
| Nessuna attività | 1.200 | 41,5% |

Ora possiamo scrivere:

`P(Churn | Nessuna attività) ≈ 41,5%`

mentre:

`P(Churn | Attività alta) ≈ 2,4%`.

Il risultato non dimostra che la bassa attività **causi** il churn. Potrebbe essere una causa, un sintomo di insoddisfazione già in corso o il risultato di un terzo fattore. Ma descrittivamente abbiamo fatto qualcosa di molto importante: un rischio aggregato è diventato una struttura condizionata abbastanza precisa da suggerire dove investigare.

## Invertire il condizionamento cambia la domanda

Supponiamo che 1.000 clienti abbiano aperto almeno tre ticket in un mese e che 180 facciano churn nei 90 giorni successivi. Allora:

`P(Churn | 3+ ticket) = 18%`.

Se, tra tutti i 900 clienti che hanno fatto churn, gli stessi 180 avevano aperto almeno tre ticket, otteniamo invece:

`P(3+ ticket | Churn) = 20%`.

“Il 20% dei churner aveva molti ticket” e “il 18% dei clienti con molti ticket farà churn” sembrano frasi quasi intercambiabili in una riunione. Non lo sono. La prima parte dai churner e guarda indietro; la seconda parte dai clienti con ticket e guarda in avanti. Confondere `P(A|B)` con `P(B|A)` significa confondere due popolazioni di riferimento diverse.

## Il base rate può dominare un alert apparentemente ottimo

Il problema diventa ancora più evidente quando l'evento che cerchiamo è raro. Immaginiamo un sistema di fraud detection su transazioni in cui la frode reale riguarda soltanto lo **0,4%** dei casi. Il sistema intercetta il 95% delle frodi e segnala erroneamente il 2% delle transazioni legittime.

Una transazione viene segnalata. Quanto è probabile che sia davvero fraudolenta?

L'intuizione può aggrapparsi al 95%. Ma quella percentuale è `P(Alert | Frode)`, non `P(Frode | Alert)`. Traduciamo quindi il problema in 100.000 transazioni:

| Gruppo | Casi | Segnalati |
|---|---:|---:|
| Frodi reali | 400 | 380 |
| Transazioni legittime | 99.600 | 1.992 |
| **Totale alert** |  | **2.372** |

Tra 2.372 alert, soltanto 380 sono frodi reali:

`P(Frode | Alert) ≈ 380 / 2.372 ≈ 16%`.

Il sistema può quindi essere molto sensibile alle frodi e produrre, nello stesso tempo, una grande quantità di falsi positivi. La ragione non è un paradosso: la popolazione legittima è enormemente più grande della popolazione fraudolenta.

Le **frequenze naturali** rendono questo tipo di problema più leggibile perché costringono a visualizzare i denominatori. La stessa tecnica è utile in screening, anomaly detection, churn prediction, lead scoring e sistemi di qualità: ogni alert deve essere interpretato insieme alla prevalenza dell'evento che stiamo cercando.

La sezione bayesiana formalizzerà questo aggiornamento. Per ora basta un riflesso operativo:

> **Quando qualcuno dice “tra quelli che fanno X, molti fanno Y”, scrivi esplicitamente `P(Y|X)` e verifica che la prova presentata non sia in realtà `P(X|Y)`.**
