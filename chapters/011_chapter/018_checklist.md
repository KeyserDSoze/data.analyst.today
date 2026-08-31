## 11.17 Checklist operativa: prima di fidarsi di una query

Una query può essere elegante, veloce e sintatticamente perfetta. Prima di usarla per una decisione importante, però, conviene attraversare una checklist più ampia.

### Domanda e metrica

- Quale decisione deve supportare questa query?
- La metrica è definita in modo non ambiguo?
- Numeratore e denominatore sono coerenti?
- Stiamo misurando stock, flow, evento o stato?

### Grain

- Qual è il grain di ogni tabella sorgente?
- Qual è il grain desiderato del risultato?
- Dopo ogni join, il grain cambia?
- Il numero di righe cresce più del previsto?

### Chiavi e join

- La chiave è unica sul lato che dovrebbe esserlo?
- Il join è one-to-one, one-to-many o many-to-many?
- Un `INNER JOIN` sta eliminando entità rilevanti?
- Un `LEFT JOIN` genera `NULL` che poi influenzano i calcoli?
- Stiamo unendo due fact table senza pre-aggregazione?

### Tempo

- Quale data risponde alla domanda?
- Quale timezone usa il business?
- Servono attributi correnti o point-in-time?
- Gli eventi possono arrivare tardi?
- Esistono backfill o rettifiche?

### Duplicati

- Cosa significa duplicato in questo modello?
- La business key è esplicita?
- Le righe sono eventi o versioni?
- La deduplicazione è deterministica?

### Dimensioni e storia

- Gli attributi dimensionali cambiano nel tempo?
- Serve SCD Type 1 o Type 2?
- Le fact puntano alla versione dimensionale corretta?

### Qualità

- Le chiavi obbligatorie sono non-null?
- Le chiavi che devono essere uniche lo sono davvero?
- I valori categorici appartengono ai domini previsti?
- La referential integrity regge?
- Volumi, freshness e distribuzioni sono plausibili?
- Il totale si riconcilia con una fonte affidabile?

### Performance e costo

- Stiamo leggendo solo colonne necessarie?
- Il periodo analizzato è quello necessario?
- Il motore può usare partition pruning/clustering/index?
- Una trasformazione pesante viene ripetuta inutilmente?
- Il costo è stato stimato prima dell'esecuzione quando possibile?

### Incrementalità

- I record possono cambiare dopo la creazione?
- Qual è la colonna di modifica affidabile?
- Qual è la lookback window?
- Come gestiamo delete e late-arriving data?
- Possiamo fare full refresh e backfill?

### AI-assisted SQL

- Abbiamo letto la query generata?
- Il prompt esplicitava grain, date, metriche e join?
- Abbiamo testato casi noti?
- Abbiamo controllato cardinalità e riconciliazioni?
- La query modifica dati o schema?
- Esiste una review umana prima dell'esecuzione distruttiva?

### Ultima domanda

Prima di pubblicare il risultato chiedere:

> **Se questo numero fosse sbagliato del 20%, quale decisione cambierebbe? E quali controlli abbiamo fatto per ridurre quella possibilità?**

La maturità SQL di un Data Analyst non si misura dal numero di funzioni che conosce.

Si misura dalla capacità di costruire query che rappresentano correttamente il business, falliscono in modo visibile quando le assunzioni si rompono e possono essere comprese e verificate anche da altri.
