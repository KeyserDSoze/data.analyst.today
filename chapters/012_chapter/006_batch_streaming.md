## 12.5 Batch, micro-batch e streaming: progettare per time-to-decision

Molte discussioni architetturali partono da una domanda sbagliata:

> Possiamo avere il dato in real time?

La domanda professionale è:

> **Quanto ritardo possiamo tollerare prima che una decisione perda valore?**

Questa è una business requirement, non una preferenza tecnologica.

### Un continuum, non due scatole

Possiamo immaginare:

```text
mensile
→ giornaliero
→ orario
→ micro-batch 15 min
→ pochi minuti
→ secondi
→ sub-second
```

Ogni riduzione di latenza può aumentare:

- complessità;
- costo;
- stato da gestire;
- observability necessaria;
- difficoltà di recovery.

Per questo la frequenza deve essere giustificata dalla decisione.

### Caso simulato/composito — CasaNova e il real time senza un utente real time

CasaNova vuole una dashboard vendite “real time”.

Il discovery mostra però che:

- i regional manager intervengono sullo staffing una volta al giorno;
- il pricing cambia settimanalmente;
- replenishment gira alle 22:00;
- il board guarda i dati settimanalmente.

Un refresh ogni 15 minuti è già molto più fresco di qualsiasi processo decisionale downstream.

Ridurre la latenza da 15 minuti a 2 secondi non cambia nessuna azione.

Aumenta soltanto il costo del sistema.

### Quando la latenza ha valore immediato

In fraud detection la situazione può essere opposta.

Se una carta compromessa continua a effettuare transazioni, trenta minuti di attesa possono significare molte altre perdite.

Qui il requisito può essere:

```text
evento disponibile
→ scoring
→ decisione
→ blocco/review
```

entro pochi secondi.

La freshness non è un badge di modernità. È parte della funzione economica del sistema.

### Event time e processing time

In streaming dobbiamo distinguere:

**event time**

Quando il fenomeno è avvenuto nel mondo reale.

**processing time**

Quando la pipeline lo elabora.

Esempio:

```text
event_time:      10:01:12
processing_time: 10:08:43
```

Se la metrica è “transazioni tra 10:00 e 10:05”, usare processing time può attribuire l'evento alla finestra sbagliata.

Google Dataflow definisce la data freshness proprio come distanza tra processing time ed event time. citeturn694929search0

### Watermark: quando crediamo che una finestra sia sufficientemente completa

I dati streaming non arrivano necessariamente in ordine.

Google Dataflow descrive il **watermark** come una soglia che rappresenta il punto oltre il quale il sistema si aspetta che i dati di una finestra siano arrivati. Se un evento relativo a quella finestra arriva dopo il watermark, è late data. citeturn694929search1turn694929search7

Questo introduce una decisione che non esiste nello stesso modo nei batch finiti:

> quanto aspettiamo prima di pubblicare un risultato?

Più aspettiamo:

- maggiore completezza potenziale;
- maggiore latenza.

Meno aspettiamo:

- risultato più tempestivo;
- più correzioni tardive.

### Early result vs final result

Un sistema operativo può accettare una metrica preliminare:

```text
10:05 → stima quasi real time
10:20 → aggiornamento con late events
T+1   → riconciliazione finale
```

Questa struttura può essere più utile di fingere che esista un solo numero istantaneamente “definitivo”.

La Data Flow Architecture Map deve distinguere:

- provisional serving;
- final/reconciled serving.

### Caso reale documentato — testare la non-deterministicità dell'arrivo

Google raccomanda che i test delle pipeline streaming simulino dati early, on-time e late, perché le assunzioni sulla tempestività influenzano direttamente la correttezza. Dataflow/Apache Beam fornisce `TestStream` proprio per verificare il comportamento rispetto a watermark e lateness. citeturn694929search11

È una lezione generale:

> **se la correttezza dipende dall'ordine o dalla tempestività degli eventi, devi testare anche eventi fuori ordine e in ritardo.**

### Batch e streaming possono convivere

Un sistema può usare:

```text
streaming → alert operativo
batch     → riconciliazione finanziaria
```

oppure:

```text
micro-batch → dashboard operations
nightly     → storico certificato
```

Non è duplicazione inutile se le due strade hanno contratti differenti e una riconciliazione esplicita.

Diventa pericoloso quando producono due “verità” senza sapere quale prevale.

### Campo della Data Flow Architecture Map

Per ogni flusso temporale annotiamo:

```text
decision deadline:
processing mode:
event-time field:
processing/ingestion time:
expected lateness:
watermark/window policy:
late-data behavior:
provisional or final output:
reconciliation path:
```

### Regola operativa

Prima di chiedere real time:

1. chi agisce sul dato?
2. quanto spesso può agire davvero?
3. quale latenza modifica la decisione?
4. gli eventi possono arrivare fuori ordine?
5. quando consideriamo una finestra abbastanza completa?
6. accettiamo revisioni tardive?
7. esiste un risultato finale riconciliato?

> **Una buona architettura non minimizza la latenza. Minimizza il tempo tra un cambiamento rilevante e una decisione affidabile che può ancora fare la differenza.**
