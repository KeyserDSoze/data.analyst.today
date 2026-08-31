## 12.5 Batch vs streaming: quanto deve essere fresco il dato?

Molte discussioni architetturali diventano inutilmente astratte perché partono dalla tecnologia invece che dalla domanda:

> Quanto rapidamente deve essere disponibile questo dato per migliorare la decisione?

Questa è la domanda che separa spesso un'elaborazione **batch** da una **streaming** o near-real-time.

## Batch

Nel batch i dati vengono elaborati a intervalli:

- ogni notte;
- ogni ora;
- ogni 15 minuti;
- in base a un evento schedulato.

È spesso più semplice da:

- progettare;
- debuggare;
- riconciliare;
- rieseguire;
- controllare nei costi.

Per moltissimi KPI aziendali è più che sufficiente.

Il report mensile del conto economico non richiede un aggiornamento ogni 200 millisecondi.

## Streaming

Nello streaming gli eventi vengono elaborati mentre arrivano o con latenze molto basse.

Può essere necessario per:

- frodi;
- monitoring operativo;
- telemetria;
- personalizzazione;
- anomaly detection;
- sistemi di alert;
- applicazioni che reagiscono rapidamente a eventi.

Ma introduce complessità aggiuntiva:

- eventi duplicati;
- ordine non garantito;
- late-arriving events;
- finestre temporali;
- idempotenza;
- gestione dello stato;
- riconciliazione tra real time e batch storico.

## Caso realistico: real time che non serviva

**CasaNova**, catena retail con 240 negozi, vuole un dashboard vendite "real time" perché il management lo considera un segnale di modernità.

Il team propone una pipeline streaming completa.

L'analista intervista però gli utenti finali e scopre che:

- i regional manager prendono decisioni di staffing una volta al giorno;
- pricing viene aggiornato settimanalmente;
- inventory replenishment gira alle 22:00;
- il board guarda il dato una volta alla settimana.

Una pipeline aggiornata ogni 15 minuti soddisfa ampiamente le decisioni reali con una frazione della complessità.

La domanda corretta non era:

> Possiamo fare streaming?

Era:

> Qual è il costo decisionale di avere 15 minuti di ritardo?

In questo caso era praticamente nullo.

## Caso opposto: quando 15 minuti sono troppi

Una fintech monitora transazioni potenzialmente fraudolente.

Se il sistema analitico aggiorna ogni 30 minuti, una carta compromessa può effettuare decine di transazioni prima dell'intervento.

Qui la freschezza ha valore economico immediato.

La latenza è quindi parte della business requirement.

## Event time vs processing time

In sistemi streaming è utile distinguere:

- **event time**: quando l'evento è realmente accaduto;
- **processing time**: quando il sistema lo ha elaborato.

Un evento può arrivare in ritardo.

Esempio:

```text
event_time      10:01:12
ingestion_time  10:08:43
```

Se costruiamo metriche solo sul tempo di ingestion, potremmo attribuire l'evento alla finestra sbagliata.

## Architettura ibrida

Molte aziende usano entrambe le modalità:

- streaming per monitoraggio e decisioni immediate;
- batch per riconciliazione, reporting finanziario e ricostruzioni storiche.

Non è una contraddizione.

È la conseguenza del fatto che decisioni differenti hanno esigenze differenti.

### Checklist di freschezza

Prima di chiedere real time, definisci:

1. chi prende la decisione;
2. quanto spesso può agire;
3. quale ritardo cambia realmente l'azione;
4. quale costo ha una decisione tardiva;
5. quanto aumenta la complessità operativa riducendo la latenza.

Una buona architettura ottimizza **time-to-decision**, non la freschezza per principio.
