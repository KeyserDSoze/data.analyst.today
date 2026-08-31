## 12.15 Checklist operativa: leggere un'architettura come un Data Analyst

Quando entri in un nuovo progetto dati, non serve diventare subito data engineer. Serve pero' costruire rapidamente una mappa mentale del sistema.

Usa questa checklist.

### 1. Sorgenti

- quali sistemi producono i dati?
- sono OLTP, file, API, eventi, SaaS?
- qual e' la system of record per ogni entita'?
- esistono copie o shadow source non ufficiali?

### 2. Acquisizione

- full load, incrementale o CDC?
- batch o streaming?
- quali chiavi identificano i cambiamenti?
- come vengono gestiti delete e late-arriving events?

### 3. Trasformazioni

- dove avviene la logica business?
- quali layer esistono: raw, curated, business?
- quali trasformazioni sono riusabili?
- come vengono testate?

### 4. Orchestrazione

- quali sono le dipendenze?
- cosa succede se un task upstream ritarda?
- esistono retry, checkpoint e backfill?
- il downstream viene bloccato quando il dato e' incompleto?

### 5. Qualita' e affidabilita'

- esistono SLO di freshness e completeness?
- chi riceve gli alert?
- quali controlli sono automatici?
- come viene misurata la qualita' del dato, non solo la riuscita dei job?

### 6. Modello analitico

- quali fact e dimension esistono?
- qual e' il grain delle fact?
- come viene gestita la storia?
- esiste una semantic layer?
- le metriche sono centralizzate o replicate nei dashboard?

### 7. Evoluzione

- esistono data contract?
- cosa succede se cambia uno schema?
- quali modifiche sono breaking?
- come vengono versionate?

### 8. Lineage e governance

- posso risalire dalla metrica alla sorgente?
- chi possiede dataset e definizioni?
- quali dati sono sensibili?
- quali accessi sono consentiti?

### 9. Recovery

- qual e' l'ultimo stato valido?
- il processo e' idempotente?
- come viene eseguito un backfill?
- cosa succede ai record in errore?

### 10. Costi

- quali workload sono piu' costosi?
- quali query scansiscono molti dati?
- la freshness richiesta giustifica il costo?
- esistono componenti sovradimensionati?

### 11. Domanda finale

Dopo aver raccolto queste informazioni, prova a descrivere il sistema in una frase:

> I dati nascono in ___, vengono acquisiti tramite ___, trasformati in ___, pubblicati tramite ___, con una freshness di ___ e controlli di qualita' su ___.

Se non riesci a farlo, probabilmente la mappa del sistema non e' ancora abbastanza chiara.

### Il principio da portare via

**L'analista non deve conoscere ogni dettaglio infrastrutturale, ma deve sapere abbastanza architettura da capire provenienza, trasformazioni, affidabilita', limiti e costo del dato che usa.**
