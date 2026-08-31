# 17.4 Caso end-to-end: marketing attribution e incrementalità

Un retailer omnicanale, **Helio Market**, investe 18 milioni di euro l'anno in advertising digitale.

Il CMO chiede:

> “Quale canale ci porta davvero più vendite?”

La dashboard last-click risponde immediatamente: branded search è il canale migliore.

Ma la domanda è sbagliata.

Il problema non è sapere quale touchpoint compare per ultimo. È capire quanto business **non sarebbe avvenuto** senza una parte della spesa.

## 1. Attribution ≠ causalità

Un cliente vede un video, visita il sito da social, riceve una newsletter, cerca il brand su Google e compra.

Chi ha causato la vendita?

Il last-click assegna tutto alla ricerca branded. Il first-click tutto al primo touchpoint. Un modello data-driven può distribuire il credito in modo più sofisticato.

Ma nessuno di questi meccanismi, da solo, garantisce incrementalità causale.

## 2. Collegare online e offline

Helio Market ha anche negozi fisici. Molti utenti vedono advertising online e comprano in store.

Prima della nuova analisi, queste vendite erano quasi invisibili al marketing digitale.

Il team costruisce quindi identity resolution e collega, quando possibile e nel rispetto delle regole privacy:

- campaign exposure;
- web sessions;
- app events;
- loyalty identity;
- ecommerce orders;
- store purchases.

## 3. Un caso reale documentato: Hoff

Google Cloud documenta il caso del retailer Hoff, che voleva collegare attività online e vendite nei negozi fisici. L'azienda costruì un sistema end-to-end di analytics e nuovi modelli di attribution, collegando dati provenienti da più sorgenti. Secondo il case study pubblicato da Google Cloud, questo lavoro contribuì a un aumento del 17% del ROI della pubblicità online.

Fonte: https://cloud.google.com/customers/hoff

Il punto didattico non è che “BigQuery aumenta il ROI”. È che un modello di misurazione migliore può cambiare radicalmente l'allocazione del budget quando il customer journey attraversa canali diversi.

## 4. Il problema del branded search

Nel caso Helio Market, branded search mostra ROAS 11,8x.

Ma molti utenti che cliccano annunci branded stavano già cercando esplicitamente il marchio.

Il team esegue un geo experiment riducendo temporaneamente la pressione paid branded in alcuni mercati confrontabili.

Risultato:

- una parte rilevante dei click paid migra verso organic;
- le vendite totali diminuiscono molto meno dei click pubblicitari;
- l'incremental ROAS è molto inferiore al ROAS attribuito.

Il canale non è inutile. Ma il valore incrementale è diverso dal credito attribuito.

## 5. Prospecting e ritardo temporale

Il contrario accade per video prospecting.

Last-click lo sottovaluta perché molte conversioni arrivano giorni dopo tramite direct o search.

Gli esperimenti geografici mostrano un effetto incrementale più forte di quanto suggerisse l'attribution dashboard.

## 6. Decisione

Il budget non viene riallocato sulla base di un unico modello.

L'organizzazione distingue:

- attribution per descrivere il percorso;
- experiments per misurare incrementalità quando possibile;
- MMM per decisioni aggregate di lungo periodo;
- marginal ROI per allocare il prossimo euro, non il credito dell'euro passato.

## 7. Misurazione

Il nuovo framework include:

- attributed revenue;
- incremental revenue;
- marginal ROAS;
- CAC;
- payback period;
- new-customer rate;
- contribution margin;
- effetti di cannibalizzazione tra paid e organic.

Google Cloud documenta anche Freshworks come esempio di infrastruttura analitica usata per misurare ROI delle campagne, attribuzione delle conversioni e revenue associata alle conversioni.

Fonte: https://cloud.google.com/customers/freshworks

> **Attribution racconta chi era presente nel percorso. Incrementality cerca di capire chi ha cambiato il percorso.**
