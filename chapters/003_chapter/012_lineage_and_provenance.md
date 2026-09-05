## 3.11 Lineage e provenance: la storia che separa la realtà dal numero

Un dato senza storia è difficile da interpretare. Per **lineage** intendiamo il percorso che il dato compie attraverso sorgenti, ingestion, trasformazioni, modelli e report. Per **provenance** intendiamo più in generale l'origine e il contesto in cui quel dato è stato generato.

L'analista non deve necessariamente ricostruire tutta l'architettura. Deve però conoscere abbastanza della genealogia di una metrica da capire **quali scelte sono state introdotte prima che il numero arrivasse sullo schermo**.

### Caso simulato/composito — Due dashboard, due margini

Orion Foods utilizza due dashboard per monitorare il margine lordo. La dashboard commerciale mostra **34,8%**; Finance mostra **31,6%**. Le formule sembrano corrette e il nome della metrica è lo stesso: `gross_margin_pct`.

Il conflitto diventa comprensibile soltanto ricostruendo il lineage. La dashboard commerciale usa vendite aggiornate ogni notte e **costo standard** del prodotto. Finance usa un dataset mensile riconciliato con l'ERP e **costo effettivo**, includendo alcune rettifiche logistiche e d'acquisto.

I due numeri non sono implementazioni concorrenti della stessa metrica. Sono due costruzioni economiche diverse. Il risultato della review non è scegliere un vincitore, ma nominare correttamente i concetti: `gross_margin_standard_pct` per il monitoraggio commerciale rapido e `gross_margin_actual_pct` per il consuntivo finanziario.

Il lineage ha quindi risolto un problema semantico, non soltanto tecnico.

## Ogni trasformazione può cambiare il significato

Per una metrica critica è sufficiente, almeno inizialmente, una mappa del tipo:

```text
evento reale
  ↓
sistema sorgente
  ↓
estrazione / ingestion
  ↓
trasformazioni e join
  ↓
tabella analitica
  ↓
semantic model / metrica
  ↓
report o analisi
```

A ogni passaggio possono comparire filtri, deduplicazioni, cambi di grain, conversioni di valuta, mapping di categorie, regole temporali, esclusioni di stati o rettifiche retroattive. Nessuna di queste operazioni è necessariamente sbagliata; diventa pericolosa quando resta invisibile al consumatore del dato.

Il punto epistemico del lineage è proprio questo: sapere **quale versione del fenomeno stiamo osservando** e quali decisioni di modellazione l'hanno prodotta.

Cinque domande aiutano a ricostruire il percorso minimo. Qual è la sorgente più vicina al fenomeno reale? Quali trasformazioni importanti ci separano da essa? La logica è cambiata nel tempo? Il dato può essere corretto retroattivamente? Chi possiede la definizione e può spiegare le eccezioni?

Se nessuno sa rispondere, il problema non è soltanto documentale. Stiamo usando una misura senza conoscere completamente la sua genealogia.

## Lineage, semantica e AI

Un assistente AI può interrogare molto rapidamente un warehouse o un semantic model. Ma se trova cinque colonne chiamate `revenue`, la velocità non gli dice quale sia quella corretta per la domanda. La semantica deve essere disponibile attraverso naming, documentazione, lineage, metric owner o contesto esplicito.

L'AI può aiutare a leggere codice e dipendenze. Non può inventare con affidabilità una source of truth che l'organizzazione non ha definito.

Per una metrica importante può bastare una scheda sintetica:

```text
Metrica: net_revenue
Owner: Finance
Sorgente primaria: ERP / invoice lines
Grain: una riga per invoice line
Aggiornamento: giornaliero
Tempo: data contabile
Cancellazioni: escluse
Resi: note di credito sottratte alla data di emissione
Valuta: EUR al cambio contabile
Rettifiche storiche: possibili fino alla chiusura mensile
```

Questa documentazione non sostituisce un catalogo o un sistema di lineage quando l'organizzazione cresce. Ma permette già di raccontare come il numero nasce e quali assunzioni porta con sé.

> **Prima di fidarti di una metrica, prova a raccontarne la storia dalla realtà al report. Se manca un passaggio decisivo, manca anche una parte della tua evidenza.**
