## 3.11 Lineage e provenance: da quale storia nasce questo numero?

Un dato senza storia è difficile da interpretare.

Per **lineage** intendiamo il percorso che il dato compie attraverso sorgenti, trasformazioni e modelli. Per **provenance** intendiamo più in generale l'origine e il contesto in cui quel dato è stato generato.

Nel lavoro dell'analista non serve ricostruire ogni dettaglio dell'infrastruttura. Serve conoscere abbastanza del percorso da capire **quali assunzioni sono state introdotte prima che il dato arrivasse a noi**.

### Caso simulato/composito — Due dashboard, due margini

**Orion Foods** utilizza due dashboard per monitorare il margine lordo.

La dashboard commerciale mostra **34,8%**.

La dashboard Finance mostra **31,6%**.

Le formule sembrano entrambe corrette.

Il conflitto si risolve ricostruendo il lineage.

La dashboard commerciale utilizza vendite aggiornate ogni notte e **costo standard** del prodotto.

Finance utilizza invece un dataset mensile riconciliato con l'ERP e **costo effettivo**, comprensivo di alcune rettifiche logistiche e di acquisto.

Le due metriche avevano lo stesso nome: `gross_margin_pct`.

Ma non rappresentavano la stessa costruzione economica.

Il problema non era scegliere quale dashboard "avesse ragione" in assoluto. Era rendere esplicito il significato:

- `gross_margin_standard_pct` per monitoraggio commerciale rapido;
- `gross_margin_actual_pct` per consuntivo finanziario.

### Ricostruire il percorso minimo

Per una metrica critica vogliamo almeno una mappa del tipo:

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

A ogni passaggio possono comparire decisioni che modificano il significato:

- filtri;
- deduplicazioni;
- cambi di grain;
- mapping di categorie;
- conversioni di valuta;
- gestione dei null;
- regole temporali;
- esclusione di stati o record;
- rettifiche retroattive.

L'architettura completa di questi passaggi sarà il tema del Capitolo 12. Qui ci interessa il loro effetto epistemico: **che cosa dobbiamo sapere per interpretare il dato finale?**

### Cinque domande di lineage per l'analista

Quando una metrica conta davvero, dovremmo poter rispondere almeno a:

1. **Qual è la sorgente più vicina al fenomeno reale?**
2. **Quali trasformazioni importanti separano la sorgente dal dataset che sto usando?**
3. **La logica è cambiata nel tempo?**
4. **Il dato può essere corretto retroattivamente?**
5. **Chi conosce o possiede la definizione?**

Se nessuno sa rispondere, il problema non è soltanto documentale. Stiamo usando una misura di cui non conosciamo completamente la genealogia.

### Lineage e AI

Un assistente AI può interrogare molto velocemente un warehouse o un semantic model.

Ma se esistono cinque colonne chiamate `revenue`, la velocità non ci dice quale sia quella corretta per la domanda.

La semantica deve già essere disponibile attraverso nomi, documentazione, lineage o contesto fornito dall'analista.

L'AI può aiutare a esplorare dipendenze e codice. Non può dedurre in modo affidabile una definizione di business che l'organizzazione non ha chiarito.

### Una scheda sufficiente, non una burocrazia perfetta

Per una metrica critica può bastare una documentazione sintetica:

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

Questa scheda non sostituisce un catalogo o un sistema di lineage quando l'organizzazione cresce. Ma permette già all'analista di sapere quale numero sta usando e perché.

> **Prima di fidarti di una metrica, cerca di raccontarne la storia dalla realtà al report. Se manca un passaggio decisivo, manca anche una parte della tua evidenza.**