## 13.4 BI: industrializzare una domanda solo quando è abbastanza stabile

Il Capitolo 11 ha definito la semantica delle metriche e il Capitolo 12 il serving layer. Qui la domanda è più circoscritta: **quando un risultato deve smettere di essere un'analisi personale e diventare un'interfaccia ricorrente per altri utenti?**

È questo il contesto in cui gli strumenti di Business Intelligence acquistano valore. Non perché “fanno grafici”, ma perché rendono economico distribuire ripetutamente una domanda su dati, definizioni e refresh sufficientemente stabili.

Un dashboard affidabile è l'ultima superficie di una catena. Se a monte mancano metriche condivise, ownership o freshness, BI non risolve il problema: lo rende più visibile e, talvolta, più autorevole.

Consideriamo un SaaS con cinque dashboard che mostrano conversion rate tra **7,4% e 11,8%**. I numeri usano denominatori diversi: lead, qualified lead, opportunity, trial e activated account. Costruire un sesto dashboard “executive” non crea una definizione comune. Prima dobbiamo riconoscere che esistono domande differenti e nominarle, per esempio `lead_to_opportunity_conversion`, `trial_to_activation_conversion` e `checkout_to_paid_conversion`. Solo dopo BI può svolgere il proprio compito: distribuire coerentemente quelle definizioni.

### La domanda deve stabilizzarsi prima dell'interfaccia

Uno degli errori più costosi è industrializzare troppo presto una fase diagnostica. Strategy indaga un calo di contribution margin: il primo giorno guarda mix e sconti; il secondo emergono freight e resi; il terzo servono FX, marketplace fee e nuove coorti. Se formalizziamo subito tutto in un dashboard, ogni nuova ipotesi diventa manutenzione di prodotto.

In quella fase può essere molto più efficiente:

```text
SQL / notebook
→ investigazione
→ pattern stabile
→ BI / monitoraggio ricorrente
```

> **La BI industrializza una domanda. Non dovrebbe essere il costo necessario per scoprire quale domanda dobbiamo fare.**

Quando la domanda si stabilizza, invece, BI permette a utenti non tecnici di filtrare, segmentare, cambiare periodo e fare drill-down senza ricostruire ogni volta numeratori, denominatori, calendari e identity logic. Questo è self-service utile: libertà nel consumo, non anarchia nella definizione.

### Dashboard come prodotto decisionale

Una domanda utile prima di costruire la superficie è: *quale comportamento vogliamo rendere più facile?* Operations può dover vedere eccezioni e agire; Sales prioritizzare account; Finance confrontare actual vs plan; un executive capire scostamento, causa plausibile e decisione richiesta. Se il dashboard contiene tutto ciò che possiamo mostrare, probabilmente non abbiamo ancora definito il prodotto.

BI è quindi particolarmente adatta quando la domanda è ricorrente, il pubblico è ampio, gli stessi KPI vengono consultati ripetutamente, servono refresh e access control e la visualizzazione/interazione è parte del servizio. È molto meno naturale come ambiente primario per ricerca metodologica, domande una tantum, simulazioni sofisticate o debugging profondo.

Nel Tooling Decision Record una soluzione BI dovrebbe dichiarare la domanda ricorrente, i consumer, la frequenza d'uso, le metriche certificate, il refresh, il modello di accesso e soprattutto **quali esigenze esplorative restano deliberatamente fuori dal dashboard**. Anche qui serve una redesign condition: se la domanda cambia continuamente, se compaiono nuovi use case operativi o se il serving non soddisfa più freshness e interazione richieste, la superficie deve essere rivalutata.

> **Scegli BI quando devi rendere economico e coerente il consumo ripetuto di una domanda abbastanza stabile. Non costruire un dashboard per evitare di fare prima l'analisi.**
