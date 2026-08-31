## 12.10 Orchestrazione e dipendenze: una pipeline è un sistema, non una query

Una trasformazione SQL può essere corretta e fallire comunque come prodotto dati se viene eseguita nel momento sbagliato, prima che una sorgente sia aggiornata o senza che un passaggio precedente sia terminato.

Questa è la funzione dell'**orchestrazione**: coordinare task, dipendenze, tempi, retry e fallimenti.

### Caso realistico: Meridian Foods

Meridian Foods aggiorna ogni mattina un dashboard commerciale alle 07:00.

Il flusso è composto da:

1. estrazione ERP;
2. caricamento ordini;
3. caricamento resi;
4. aggiornamento dimensione clienti;
5. calcolo margine;
6. refresh semantic model;
7. refresh dashboard.

Per mesi il processo funziona con job indipendenti schedulati a orari fissi:

```text
ERP export      04:00
orders load     04:30
returns load    04:40
customers       04:50
margin model    05:10
BI refresh      06:00
```

Poi una mattina l'ERP termina alle 05:05 per un rallentamento.

Il job `orders load`, partito comunque alle 04:30, legge il file del giorno precedente.

Il dashboard delle 07:00 è tecnicamente "verde" ma contiene dati parzialmente vecchi.

### Scheduling non è orchestrazione

Un semplice calendario dice **quando provare a partire**.

Un orchestratore dovrebbe anche sapere:

- da cosa dipende un task;
- se gli input sono pronti;
- cosa fare se un task fallisce;
- quante volte ritentare;
- quando fermare il downstream;
- come notificare il problema;
- come riprendere senza duplicare dati.

La differenza è sostanziale.

### DAG: pensare in dipendenze

Molti orchestratori rappresentano una pipeline come un **Directed Acyclic Graph (DAG)**.

Esempio:

```text
              orders ----\
                         -> revenue_model -> semantic_model -> dashboard
              returns ---/

customers ----------------/
```

Il vantaggio concettuale è che il sistema non dice soltanto "esegui alle 05:00". Dice:

> esegui `revenue_model` solo quando `orders`, `returns` e `customers` sono completati correttamente.

### Caso: retry senza idempotenza

Un task fallisce dopo aver scritto meta' dei dati. L'orchestratore lo ritenta automaticamente.

Se il task usa un semplice `INSERT`, il secondo tentativo può duplicare la parte già scritta.

Il retry, quindi, non è sempre una soluzione innocua.

Serve progettare task:

- idempotenti;
- transazionali quando possibile;
- con checkpoint;
- con upsert/merge coerenti;
- con stati chiaramente osservabili.

### Backfill

Un'altra responsabilita' importante è il **backfill**: ricalcolare periodi storici quando cambia una regola o quando un job precedente era errato.

Supponiamo che il margine netto sia stato calcolato male per 45 giorni.

Un sistema maturo deve permettere di ricalcolare:

```text
2026-05-01 -> 2026-06-14
```

senza rompere il dato corrente e senza duplicazioni.

### Cosa deve capire un Data Analyst

Quando un numero manca o cambia improvvisamente, la causa può non essere nella query finale.

Può essere:

- una dipendenza non completata;
- un input vecchio;
- un retry incompleto;
- un backfill parziale;
- una pipeline downstream partita troppo presto.

Quindi una buona domanda non è solo:

> La query è giusta?

ma anche:

> Quali processi devono essere completati prima che questo numero sia affidabile?

### Metodo operativo

Per ogni dataset critico documentare almeno:

- sorgenti;
- task upstream;
- dipendenze;
- orario atteso;
- retry policy;
- comportamento in caso di failure;
- ownership;
- procedura di backfill.

**Una pipeline affidabile non è una collezione di script. È una sequenza esplicita di dipendenze e garanzie.**
