## 3.7 Duplicati: quando una riga in più cambia il risultato economico

Un duplicato non è necessariamente una riga identica a un'altra.

I casi più pericolosi sono spesso duplicati **semantici**: record diversi che rappresentano lo stesso evento economico o la stessa entità.

Prima di deduplicare dobbiamo quindi sapere che cosa dovrebbe essere unico al grain corrente.

### Caso simulato/composito — Il fatturato cresciuto durante la notte

**Nordline Retail** vende arredamento online in quattro Paesi europei.

Il lunedì mattina la dashboard segnala che il fatturato del weekend è cresciuto del **7,2%** rispetto al weekend precedente. La campagna promozionale lanciata venerdì sera sembra aver funzionato.

Un'analista, però, esegue il controllo che precede qualsiasi interpretazione: confronta il numero di righe con il numero di ordini distinti.

```text
righe nella tabella orders:       184.223
order_id distinti:                171.906
```

La differenza non è compatibile con il grain dichiarato: una riga per ordine.

Indagando, il team scopre che durante una migrazione il caricamento di una finestra di circa tre ore è stato eseguito due volte.

I record non sono copie perfette perché `load_timestamp` è diverso. Un ingenuo `SELECT DISTINCT *` non li eliminerebbe.

Il fatto economico, però, è lo stesso: stesso `order_id`, stesso importo, stesso ordine reale.

Dopo la correzione, la crescita del fatturato passa dal **7,2% all'1,1%**.

La storia raccontata dalla dashboard cambia completamente.

### Duplicato tecnico, versione o evento legittimo?

Trovare la stessa chiave più volte non basta per decidere che cosa fare.

Tre righe con lo stesso `order_id` potrebbero essere:

- tre copie accidentali dello stesso ordine;
- tre versioni successive dello stesso record;
- tre eventi di stato associati all'ordine;
- tre pagamenti parziali;
- un ordine e due rettifiche.

La deduplicazione è corretta soltanto dopo aver identificato quale di queste storie descrive il processo reale.

### La regola di deduplica deve essere dimostrabile

Una strategia comune consiste nel mantenere la versione più recente:

```sql
ROW_NUMBER() OVER (
    PARTITION BY order_id
    ORDER BY updated_at DESC
)
```

Ma questa regola è valida solo se:

- `order_id` identifica davvero l'entità da deduplicare;
- `updated_at` ordina correttamente le versioni;
- la versione più recente sostituisce le precedenti;
- non stiamo cancellando eventi storici che hanno significato proprio.

Il codice non può decidere queste assunzioni al posto nostro.

### Duplicati di entità: ancora più difficili

Per i clienti la situazione può essere più complessa.

Due record con email differenti possono essere la stessa persona. Due record con la stessa email possono essere persone diverse. Un indirizzo può cambiare. Un account può essere condiviso.

Questo è il motivo per cui la deduplicazione di identità non dovrebbe essere ridotta a una singola regola del tipo:

```text
stessa email = stesso cliente
```

Una regola troppo aggressiva produce **false merge**. Una regola troppo prudente produce **false split**.

Entrambi possono distorcere metriche come clienti unici, retention e lifetime value.

### Un controllo minimo

Per ogni tabella critica confrontiamo almeno:

- numero totale di righe;
- cardinalità della chiave attesa;
- distribuzione del numero di righe per chiave;
- andamento temporale dei duplicati;
- attributi che differiscono tra record con la stessa chiave.

Se una tabella dichiarata "una riga per ordine" mostra improvvisamente il 6% di `order_id` ripetuti dopo una release, abbiamo un segnale molto più informativo di un generico controllo sui duplicati perfetti.

### Regola operativa

Non chiederti soltanto:

> "Ci sono righe duplicate?"

Chiediti:

> **"Esistono più rappresentazioni dello stesso fatto o della stessa entità, e qual è la regola che stabilisce quale rappresentazione usare?"**

Deduplicare non significa rendere il dataset più corto. Significa evitare che la stessa realtà venga contata più volte.