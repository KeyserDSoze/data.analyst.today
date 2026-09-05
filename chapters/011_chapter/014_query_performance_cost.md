## 11.13 Performance e costo: una trasformazione deve arrivare in tempo e con un costo proporzionato

Una query può essere semanticamente corretta e comunque essere un cattivo componente del sistema analitico. Se arriva dopo la decisione, costa troppo rispetto al valore che produce o ricostruisce inutilmente la stessa trasformazione centinaia di volte, il problema non è più soltanto SQL: è il **service envelope** del prodotto dati.

### TravelSphere: il dashboard da €27.000 al mese

TravelSphere costruisce un dashboard operativo aggiornato ogni 15 minuti. La query principale legge una grande tabella eventi:

```sql
SELECT *
FROM events
WHERE DATE(event_timestamp) >= CURRENT_DATE - 90;
```

Il dashboard usa soltanto 12 colonne su oltre 180, ma la trasformazione viene eseguita quattro volte l’ora, 24 ore al giorno, da più ambienti con filtri simili. Su un motore cloud a consumo la ripetizione trasforma una query innocua in una voce di costo rilevante.

Il problema non è “il cloud costa troppo”. È che il prodotto analitico paga continuamente per ricostruire lavoro già noto.

### Il lavoro letto non coincide con le righe restituite

BigQuery documenta un caso molto concreto: nel modello on-demand il costo dipende dai byte elaborati. Google raccomanda dry run/query validator, `maximum bytes billed` e di non usare `LIMIT` come controllo dei costi su tabelle non clusterizzate.

```sql
SELECT *
FROM huge_table
LIMIT 1000;
```

può restituire mille righe senza ridurre i byte letti. Il risultato visibile e il lavoro necessario per produrlo non sono la stessa cosa.

Fonte: https://docs.cloud.google.com/bigquery/docs/best-practices-costs

`SELECT *` ha inoltre una conseguenza semantica: lega il consumer a qualsiasi nuova colonna aggiunta alla sorgente. Una proiezione esplicita comunica meglio l’interfaccia del modello e, sui motori columnar, può ridurre il lavoro letto.

### Ottimizzare significa misurare, non applicare superstizioni

Regole come “CTE è sempre più lenta”, “subquery è sempre peggiore” o “filtra sempre nella prima riga possibile” non sono universali: gli optimizer possono riscrivere il piano. Quando performance e costo contano, osserviamo execution plan, bytes scanned, partizioni lette, righe input/output, shuffle, spill, scansioni ripetute e cardinalità dei join.

La competenza importante non è memorizzare trucchi, ma formulare un’ipotesi di costo e verificarla.

Partitioning, clustering e pruning diventano utili quando riflettono pattern di accesso reali e ricorrenti. Se quasi tutte le query leggono finestre temporali limitate, il layout fisico può ridurre scansioni inutili. Non significa partizionare ogni tabella: significa allineare la struttura fisica ai filtri che delimitano davvero il lavoro.

### Materializzare quando il riuso supera il costo di ricostruzione

Se venti dashboard ripetono:

```text
raw events
→ identity resolution
→ bot filtering
→ sessionization
→ customer-day aggregation
```

stiamo pagando più volte costo, latenza e superficie di errore. Può essere più sensato materializzare `clean_events` o `customer_daily_activity` e far consumare a dashboard, notebook e modelli una definizione condivisa. Google raccomanda anche la materializzazione di risultati intermedi per query grandi e ripetute quando riduce il volume riletto.

La scelta deve comunque bilanciare storage, freshness, complessità operativa, numero di consumer e frequenza di riuso.

### Costo relativo al valore della decisione

Un’analisi una tantum da €80 che supporta una decisione da €20 milioni può essere irrilevante dal punto di vista economico. Una dashboard consultata raramente che costa €800 al giorno è un problema diverso. Per questo “query costosa” non significa soltanto numero alto: significa costo non proporzionato a frequenza d’uso, rischio e valore della decisione.

### Service envelope nell’Analytical Data Contract

```text
refresh cadence:
expected completion time:
freshness target:
expected scanned volume/cost:
consumer concurrency:
materialization strategy:
performance owner:
alert threshold:
```

> **Un prodotto analitico non promette soltanto il numero corretto. Promette che quel numero sarà disponibile quando serve, con un costo proporzionato al suo uso e senza ricostruire inutilmente la stessa semantica.**
