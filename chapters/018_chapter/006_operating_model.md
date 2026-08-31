## 18.5 Operating model: chi fa cosa quando l'analytics scala
Quando il numero di dashboard, pipeline, metriche e modelli cresce, la domanda organizzativa diventa inevitabile:

> chi è responsabile di cosa?

Molti problemi di analytics vengono diagnosticati come problemi tecnici quando in realtà sono problemi di operating model.

Una pipeline può fallire perché nessuno sa chi deve mantenerla.

Una metrica può divergere perché due team si sentono entrambi autorizzati a cambiarla.

Un dataset può diventare inutilizzabile perché chi lo produce non conosce i consumer downstream.

## Ruoli diversi, responsabilità diverse

In un'organizzazione moderna possiamo trovare:

- data analyst;
- analytics engineer;
- data engineer;
- data scientist;
- ML engineer;
- product manager;
- business owner;
- platform engineer;
- governance/security.

Le etichette variano da azienda ad azienda.

Il punto non è difendere confini rigidi.

È evitare zone grigie senza owner.

## Un possibile modello di responsabilità

### Data Analyst

- formula domande;
- interpreta metriche;
- conduce analisi;
- verifica semantica;
- traduce evidenze in decisioni.

### Analytics Engineer

- trasforma logica analitica ricorrente in modelli riutilizzabili;
- testa trasformazioni;
- mantiene semantic layer e data mart;
- gestisce dipendenze analitiche.

### Data Engineer

- garantisce ingestion, orchestrazione, affidabilità e scalabilità delle pipeline;
- gestisce integrazione tra sistemi.

### Business Owner

- definisce il significato delle metriche critiche;
- decide priorità e trade-off business;
- accetta cambiamenti semantici.

### Platform/Governance

- definisce standard comuni;
- controlla accessi, lineage, policy e osservabilità;
- riduce duplicazioni infrastrutturali.

## La matrice RACI può aiutare, ma non basta

Per un prodotto analitico critico possiamo definire:

- **Responsible** — chi esegue;
- **Accountable** — chi risponde del risultato;
- **Consulted** — chi deve essere coinvolto;
- **Informed** — chi deve essere avvisato.

Ma una matrice scritta non risolve automaticamente il problema.

Serve che gli owner abbiano davvero:

- autorità;
- tempo;
- accesso;
- incentivi;
- conoscenza del prodotto.

## Caso realistico: tutti owner, nessun owner

Una società fintech ha una metrica critica: approval rate dei pagamenti.

Payments Engineering gestisce il gateway.

Risk modifica regole antifrode.

Finance guarda l'impatto economico.

Analytics mantiene la dashboard.

Quando l'approval rate scende di 4 punti percentuali, ogni team indaga la propria parte.

Nessuno però possiede il KPI end-to-end.

Il risultato:

- tre dashboard;
- quattro definizioni;
- escalation lenta;
- diagnosi frammentata.

L'azienda introduce un metric owner cross-functional per approval rate e un incident protocol comune.

Il cambiamento tecnico è minimo.

La velocità decisionale migliora drasticamente.

## Centralizzare o federare?

Un team centrale può garantire standard, ma diventa facilmente collo di bottiglia.

Una struttura totalmente federata aumenta velocità locale, ma rischia duplicazione e incoerenza.

Una soluzione comune è un modello federato:

- standard e piattaforma centrali;
- ownership dei data product nei domini;
- semantic governance condivisa;
- meccanismi comuni di discovery e accesso.

La documentazione recente di Microsoft e Databricks insiste proprio sul combinare responsabilità per dominio con standard di publishing, governance, lineage e qualità comuni.

## Il ruolo dell'analista cambia

In questo operating model, l'analista non scompare dietro l'automazione.

Diventa spesso il punto di connessione tra:

- business meaning;
- comportamento dei dati;
- metriche;
- decisioni;
- requisiti tecnici.

È una posizione molto potente perché l'analista vede sia la domanda sia il modo in cui la realtà viene rappresentata nel sistema.

## Con l'AI il problema diventa ancora più importante

Se agenti e copiloti possono generare query, modelli e dashboard, serve sapere quali asset sono autorevoli e chi ne risponde.

Un agente capace di interrogare tutto senza governance non crea necessariamente più valore.

Può semplicemente amplificare più velocemente incoerenze già presenti.

Per questo data governance e AI governance stanno convergendo: gli stessi concetti di accesso, lineage, policy e ownership devono estendersi anche agli asset AI.

## Una regola organizzativa

> **Ogni output che influenza una decisione ricorrente dovrebbe avere un owner riconoscibile, anche quando il lavoro è distribuito tra più team e più agenti.**

Scalare non significa eliminare la responsabilità individuale.

Significa renderla esplicita in un sistema più complesso.

## Fonti

- Microsoft, *Data Processing Standards for AI and Analytics*: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/data/operational-standards-data-processing-standards-unify-data-platform
- Databricks, *Guiding principles*: https://docs.databricks.com/gcp/en/lakehouse-architecture/guiding-principles
- Microsoft, *Data governance with Unity Catalog*: https://learn.microsoft.com/en-us/azure/databricks/data-governance/
