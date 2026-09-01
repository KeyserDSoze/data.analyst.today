## 12.7 Lineage: trasformare il flusso in una dependency map

La Data Flow Architecture Map descrive il percorso logico del dato.

La **lineage** rende quel percorso interrogabile:

```text
source
  ↓
ingestion
  ↓
raw/curated models
  ↓
serving layer
  ↓
dashboard / API / ML / agent
```

Per un analyst, il valore principale non è vedere un diagramma elegante.

È poter rispondere rapidamente a domande come:

- da quale sorgente nasce questo KPI?
- quale trasformazione lo modifica?
- se questa tabella cambia, quali dashboard sono impattate?
- quale upstream failure spiega il dato incompleto?
- dove devo iniziare la root-cause analysis?

### Caso reale documentato — lineage come troubleshooting

Microsoft Purview descrive la data lineage come il lifecycle del dato dalla sua origine attraverso i passaggi del data estate e cita tra i principali use case il troubleshooting, la ricerca della root cause nelle pipeline e il debugging.

Fonte: https://learn.microsoft.com/en-us/azure/purview/concept-data-lineage

Questo è esattamente il ruolo che ci interessa nel capitolo.

### Caso simulato/composito — NordRail e il KPI che cambia senza un guasto operativo

NordRail modifica una trasformazione:

```text
prima:
status = CANCELLED

poi:
status IN (CANCELLED, ABORTED_AFTER_DEPARTURE)
```

Due settimane dopo il cancellation rate appare molto più alto.

Senza lineage, l'indagine parte da:

- treni;
- regioni;
- staffing;
- manutenzione.

Con lineage e change history il team vede che:

```text
executive_cancellation_rate
        ↑
semantic measure
        ↑
gold_trip_status
        ↑
status_normalization_v34  ← change deployed
```

Il salto non dimostra che il nuovo dato sia sbagliato. Dimostra che **la metrica non è più direttamente comparabile con la storia precedente senza dichiarare il cambio di definizione**.

### Upstream lineage e downstream impact

La stessa mappa deve funzionare in due direzioni.

**Upstream tracing**

> Da dove arriva questo numero?

**Downstream impact analysis**

> Chi si rompe o cambia significato se modifico questo asset?

Esempio:

```text
customer_country semantics change
         ↓
customer mart
         ↓
revenue by country
         ↓
board dashboard
         ↓
territory planning model
```

Questo rende una schema/semantic change molto più gestibile.

### Column-level lineage: utile quando il dataset è grande

Sapere che una dashboard dipende da una tabella da 300 colonne può non bastare.

Per alcuni use case serve capire che:

```text
board.margin_pct
```

dipende precisamente da:

```text
fact_order_lines.net_revenue
fact_order_lines.cogs
shipment_cost_allocated
```

La granularità necessaria dipende dal rischio e dalla complessità.

Non serve costruire column-level lineage perfetta per ogni tabella esplorativa.

### Lineage non è automaticamente governance

La lineage ci dice **come gli asset sono collegati**.

Non risponde da sola a:

- chi può accedere;
- quale asset è certificato;
- chi approva una modifica;
- quanto a lungo conserviamo i dati.

Questi sono temi di governance che torneranno soprattutto nel Capitolo 18.

Qui annotiamo soltanto ciò che serve al funzionamento della mappa:

- owner;
- sensitivity se rilevante;
- certification state;
- dependency.

### Il problema della lineage incompleta

Una parte significativa del lavoro analitico può vivere fuori dalla piattaforma ufficiale:

```text
warehouse
→ CSV export
→ spreadsheet locale
→ slide del board
```

La lineage automatica può fermarsi al CSV.

Per questo una mappa tecnica perfetta non elimina la necessità di conoscere i veri consumer decisionali.

I dataset più critici richiedono anche disciplina d'uso.

### Lineage e incident response

Quando un KPI è anomalo, una sequenza efficace può essere:

```text
1. consumer / semantic layer
2. final model
3. upstream transforms
4. ingestion/capture
5. source
```

oppure partire dal punto in cui freshness/volume ha iniziato a divergere.

Senza dipendenze visibili, ogni incidente diventa archeologia.

### Campo della Data Flow Architecture Map

Per ogni asset critico annotiamo:

```text
upstream dependencies:
downstream consumers:
transformation/version:
owner:
certification state:
last change:
lineage coverage:
```

### Regola operativa

Una buona prova di maturità è prendere un KPI executive e chiedere:

> **Riusciamo a tornare dalla cifra mostrata sullo schermo fino alle sorgenti e, nella direzione opposta, sappiamo chi deve essere avvisato se una di quelle sorgenti cambia?**

> **La lineage è utile quando trasforma il percorso del dato da conoscenza tribale in una dependency map utilizzabile per debugging, impact analysis e recovery.**
