## 12.7 Lineage: trasformare il flusso in una dependency map

La Data Flow Architecture Map descrive il percorso logico del dato. La **lineage** rende quel percorso interrogabile: da quale sorgente nasce un KPI, quale trasformazione lo modifica, quali consumer dipendono da un asset e dove iniziare una root-cause analysis quando qualcosa cambia.

Microsoft Purview descrive la lineage come il lifecycle del dato dalla sua origine attraverso il data estate e la collega esplicitamente a troubleshooting, root-cause analysis, debugging e impact analysis.

Fonte: https://learn.microsoft.com/en-us/azure/purview/concept-data-lineage

### Caso simulato/composito — NordRail e il KPI che cambia senza un guasto operativo

NordRail modifica una normalizzazione di stato:

```text
prima: status = CANCELLED
poi:   status IN (CANCELLED, ABORTED_AFTER_DEPARTURE)
```

Due settimane dopo il cancellation rate appare molto più alto. Senza lineage, l'indagine parte da treni, regioni, staffing e manutenzione. Con lineage e change history il percorso diventa:

```text
executive_cancellation_rate
        ↑
semantic measure
        ↑
gold_trip_status
        ↑
status_normalization_v34  ← change deployed
```

Il salto non dimostra che la nuova definizione sia sbagliata. Dimostra che **la serie non è più direttamente comparabile con la storia precedente senza dichiarare il cambio semantico**.

### Tracciare a monte e misurare l'impatto a valle

La stessa mappa deve funzionare in entrambe le direzioni. L'upstream tracing risponde a “da dove arriva questo numero?”. Il downstream impact analysis risponde a “chi cambia significato o si rompe se modifico questo asset?”.

Per alcuni asset basta lineage a livello di tabella; per altri serve arrivare a colonne specifiche, per esempio capire che `board.margin_pct` dipende da `net_revenue`, `cogs` e `shipment_cost_allocated`. La granularità deve essere proporzionata al rischio: non serve column-level lineage perfetta per ogni tabella esplorativa.

Lineage non equivale automaticamente a governance. Dice come gli asset sono collegati, non chi può accedere, quale asset è certificato o chi approva una modifica. Qui ci basta associare alle dipendenze owner, stato di certificazione, ultima modifica e copertura della lineage.

Resta inoltre un limite pratico: una parte del vero flusso decisionale può uscire dalla piattaforma ufficiale:

```text
warehouse
→ CSV export
→ spreadsheet locale
→ slide del board
```

La lineage automatica può fermarsi prima del consumer reale. Per gli asset critici serve quindi anche disciplina d'uso.

Nella Data Flow Architecture Map annotiamo:

```text
upstream dependencies:
downstream consumers:
transformation/version:
owner:
certification state:
last change:
lineage coverage:
```

> **La lineage è utile quando trasforma il percorso del dato da conoscenza tribale in una dependency map utilizzabile per debugging, impact analysis e recovery.**
