## 11.13 Performance e costo: una query corretta può essere troppo costosa

Nel lavoro analitico moderno, una query non viene valutata soltanto per il risultato.

Conta anche:

- quanto tempo impiega;
- quante risorse usa;
- quante volte viene eseguita;
- quanto costa;
- quanto scala quando il volume cresce.

Una query che funziona su 5 milioni di righe può diventare problematica su 5 miliardi.

### Caso realistico: il dashboard da 27.000 euro al mese

**TravelSphere** costruisce un dashboard operativo che aggiorna ogni 15 minuti.

La query principale legge una tabella eventi molto grande e contiene:

```sql
SELECT *
FROM events
WHERE DATE(event_timestamp) >= CURRENT_DATE - 90;
```

Il dashboard usa solo 12 colonne su oltre 180.

La query viene eseguita:

- 4 volte l'ora;
- 24 ore al giorno;
- da più ambienti;
- con filtri differenti.

In un sistema cloud a consumo, una query apparentemente innocua diventa una voce di costo significativa.

Su BigQuery, per esempio, il modello on-demand può fatturare in base ai byte elaborati; Google raccomanda di stimare il costo prima dell'esecuzione, usare dry run e limitare i byte massimi fatturabili. La documentazione sottolinea inoltre che `LIMIT` non riduce necessariamente i byte letti su tabelle non clusterizzate.[^bq-cost]

### `SELECT *` non è sempre innocuo

In un motore columnar, leggere colonne inutili può significare elaborare più dati del necessario.

Meglio:

```sql
SELECT
    user_id,
    event_timestamp,
    event_name,
    country,
    device_type
FROM events
WHERE ...;
```

Non perché `SELECT *` sia moralmente sbagliato, ma perché rende meno esplicito il contratto della query e può aumentare costo e fragilità.

### Filtrare presto, ma capire il motore

Una regola generale utile è ridurre il volume il prima possibile, ma l'ottimizzatore del database può riscrivere il piano.

Il punto non è applicare superstizioni del tipo "CTE è sempre più veloce" o "subquery è sempre più lenta".

Il punto è osservare:

- execution plan;
- bytes scanned;
- righe lette e prodotte;
- shuffle;
- spill su disco;
- scansioni ripetute;
- join cardinality.

### Partitioning e clustering

Se una tabella è interrogata quasi sempre per data, partizionarla temporalmente può evitare di leggere periodi irrilevanti.

Se viene filtrata spesso per alcune colonne ad alta utilità, il clustering o meccanismi equivalenti possono aiutare il pruning.

Google indica esplicitamente partitioning e clustering come strumenti per ridurre i dati elaborati e quindi, in molti scenari, il costo delle query.[^bq-pricing]

### Il filtro che rompe il pruning

Supponiamo che una tabella sia partizionata su `event_date`.

Una query chiara:

```sql
WHERE event_date >= DATE '2026-08-01'
```

può consentire un pruning diretto.

Trasformazioni inutilmente complesse sulla colonna di partizione possono rendere più difficile l'ottimizzazione in alcuni motori.

Per questo, quando performance e costo contano, è importante capire come il motore interpreta il predicato.

### Materializzare quando ha senso

Se una trasformazione molto pesante viene riutilizzata da 20 dashboard, ricalcolarla ogni volta può essere inefficiente.

Può essere più sensato materializzare un modello intermedio:

```text
raw events
    ↓
clean events
    ↓
daily customer activity
    ↓
dashboards
```

Google suggerisce anche di materializzare risultati intermedi in alcuni casi di query grandi e ripetute, così da interrogare poi dataset più piccoli.[^bq-cost]

### Performance come problema di prodotto analitico

Un dashboard che impiega 45 secondi a caricarsi viene usato meno.

Una query ad hoc che costa centinaia di euro viene eseguita meno liberamente.

Un modello che completa alle 10:30 invece che alle 07:00 può arrivare troppo tardi per la decisione.

Quindi performance e costo non sono soltanto ottimizzazione tecnica. Sono parte della qualità del prodotto analitico.

### Checklist rapida

Prima di ottimizzare chiedere:

- quali colonne servono davvero?
- qual è il periodo necessario?
- la tabella è partizionata coerentemente con l'uso?
- stiamo ripetendo la stessa trasformazione pesante?
- un join sta esplodendo il numero di righe?
- possiamo pre-aggregare?
- esiste un execution plan o un dry run da leggere?
- il costo è proporzionato al valore della decisione?

**La query più elegante non è necessariamente quella che crea il sistema analitico migliore.**

[^bq-cost]: Google Cloud Documentation, *Estimate and control costs*, https://docs.cloud.google.com/bigquery/docs/best-practices-costs
[^bq-pricing]: Google Cloud, *BigQuery pricing*, https://cloud.google.com/bigquery/pricing
