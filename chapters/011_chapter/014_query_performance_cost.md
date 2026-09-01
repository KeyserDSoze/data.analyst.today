## 11.13 Performance e costo: una trasformazione deve arrivare in tempo e con un costo proporzionato

Una query può essere semanticamente corretta e comunque essere un cattivo componente del sistema analitico.

Conta anche:

- quanto tempo impiega;
- quante risorse usa;
- quante volte viene eseguita;
- quanto costa;
- se arriva prima della decisione;
- se scala quando il volume cresce.

Queste proprietà entrano nell'Analytical Data Contract perché **latenza e costo possono rendere inutilizzabile un dato perfettamente corretto**.

### Caso simulato/composito — TravelSphere e il dashboard da 27.000 euro al mese

TravelSphere costruisce un dashboard operativo aggiornato ogni 15 minuti.

La query principale legge una grande tabella eventi:

```sql
SELECT *
FROM events
WHERE DATE(event_timestamp) >= CURRENT_DATE - 90;
```

Il dashboard usa soltanto 12 colonne su oltre 180.

La trasformazione viene eseguita:

- quattro volte l'ora;
- 24 ore al giorno;
- da più ambienti;
- con filtri simili ma non identici.

Su un motore cloud a consumo, la ripetizione trasforma una query apparentemente innocua in una voce di costo significativa.

Il problema non è “il cloud costa troppo”. È che il prodotto analitico sta pagando continuamente per ricostruire lo stesso lavoro.

### Caso reale documentato — BigQuery e il costo per byte elaborati

Nel modello on-demand di BigQuery il costo delle query dipende dai byte letti. Google raccomanda di:

- stimare i byte prima dell'esecuzione;
- usare query validator o dry run;
- impostare `maximum bytes billed` quando appropriato;
- evitare di usare `LIMIT` come controllo dei costi su tabelle non clusterizzate;
- preferire le funzioni di preview quando si vuole soltanto ispezionare i dati.

In particolare, su una tabella non clusterizzata:

```sql
SELECT *
FROM huge_table
LIMIT 1000;
```

può restituire poche righe senza ridurre i byte letti dalla query.

Fonte: https://docs.cloud.google.com/bigquery/docs/best-practices-costs

Questo caso è utile perché mostra una differenza fondamentale:

> **numero di righe restituite e lavoro necessario per ottenerle non sono la stessa cosa.**

### `SELECT *`: il problema è anche il contratto

Su motori columnar, leggere colonne non necessarie può aumentare il volume elaborato.

Ma c'è un secondo problema.

```sql
SELECT *
```

lega implicitamente il consumer a qualunque nuova colonna venga aggiunta alla sorgente.

Una query più esplicita:

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

comunica anche quali campi appartengono davvero all'interfaccia analitica.

### Ottimizzare significa misurare il piano, non applicare superstizioni

Regole come:

- “CTE è sempre più lenta”;
- “subquery è sempre peggiore”;
- “filtra sempre nella prima riga possibile”;

non sono universali.

I motori possono riscrivere il piano.

Quando il costo conta, osserviamo ciò che il sistema esegue realmente:

- execution plan;
- bytes scanned;
- partizioni lette;
- righe input/output;
- shuffle;
- spill;
- scansioni ripetute;
- cardinalità dei join.

La competenza importante non è memorizzare trucchi. È saper formulare un'ipotesi di costo e verificarla.

### Partitioning, clustering e pruning

Se quasi tutte le query leggono periodi limitati, il layout fisico può aiutare a evitare scansioni inutili.

BigQuery documenta partitioning e clustering proprio come strumenti che possono ridurre la quantità di dati letti e quindi costo e latenza in molti workload.

La regola analitica da ricordare è:

> **la struttura fisica dovrebbe riflettere i pattern di accesso importanti e ricorrenti.**

Non significa partizionare ogni tabella. Significa capire quali filtri delimitano davvero il lavoro.

### Materializzare quando il riuso supera il costo di ricostruzione

Supponiamo che venti dashboard ripetano:

```text
raw events
→ identity resolution
→ bot filtering
→ sessionization
→ customer-day aggregation
```

Ricalcolare l'intera catena per ogni consumer aumenta:

- costo;
- latenza;
- possibilità di divergenza;
- superficie di errore.

Può essere più sensato materializzare:

```text
raw events
→ clean events
→ customer_daily_activity
→ dashboard / notebook / model
```

Google raccomanda anche, per query grandi e ripetute, di valutare la materializzazione di risultati intermedi in tabelle più piccole.

La decisione va comunque bilanciata con:

- storage;
- freshness;
- complessità operativa;
- numero di consumer;
- frequenza di riuso.

### Query budget: collegare costo e valore

Un'analisi una tantum che costa €80 ma supporta una decisione da €20 milioni può essere economicamente irrilevante.

Una dashboard consultata raramente che brucia €800 al giorno è un altro problema.

Perciò “query costosa” non dovrebbe significare semplicemente “numero grande”.

Serve un rapporto:

```text
costo di produrre il dato
vs
frequenza d'uso
vs
valore/rischio della decisione
```

Questo prepara il terreno al Capitolo 18, dove parleremo di cost management del sistema analitico nel suo complesso.

### Campo del contract: service envelope

Per un modello importante possiamo dichiarare:

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

Il modello non promette soltanto “il numero corretto”. Promette anche **quando** e **a quale costo operativo ragionevole** quel numero sarà disponibile.

### Metodo operativo

Prima di ottimizzare chiediamo:

1. quale decisione ha una deadline reale?
2. quali colonne e periodi servono davvero?
3. quante volte ricostruiamo la stessa trasformazione?
4. il layout fisico supporta i filtri ricorrenti?
5. possiamo stimare il lavoro prima di eseguire?
6. il join produce un'esplosione inutile?
7. materializzare ridurrebbe costo totale e divergenza?
8. il costo è proporzionato all'uso e al valore?

> **Performance e costo non sono un'appendice tecnica del SQL. Sono parte del contratto con cui un prodotto analitico promette di essere disponibile quando serve senza sprecare risorse.**
