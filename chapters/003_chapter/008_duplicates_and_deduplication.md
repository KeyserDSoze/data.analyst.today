## 3.7 Duplicati: quando una rappresentazione in più diventa un fatto economico in più

Un duplicato non è necessariamente una riga identica a un'altra. I casi più pericolosi sono spesso **duplicati semantici**: record differenti che rappresentano lo stesso evento economico o la stessa entità.

Per questo la deduplicazione viene dopo grain e identità. Prima dobbiamo sapere che cosa dovrebbe essere unico; soltanto allora possiamo giudicare se due rappresentazioni descrivono lo stesso fatto oppure eventi legittimamente distinti.

### Caso simulato/composito — Il fatturato cresciuto durante la notte

Nordline Retail vende arredamento online in quattro Paesi europei. Il lunedì mattina la dashboard mostra che il fatturato del weekend è cresciuto del **7,2%** rispetto al weekend precedente. La campagna lanciata venerdì sembra funzionare.

Prima di interpretare il risultato, un'analista confronta il numero di righe con il numero di ordini distinti:

```text
righe nella tabella orders:       184.223
order_id distinti:                171.906
```

La differenza contraddice il grain dichiarato, una riga per ordine. L'indagine mostra che durante una migrazione una finestra di circa tre ore è stata caricata due volte. Le righe non sono copie byte-per-byte perché `load_timestamp` differisce; un `SELECT DISTINCT *` non le eliminerebbe. Dal punto di vista economico, però, rappresentano lo stesso ordine.

Dopo la correzione, la crescita passa dal **7,2% all'1,1%**. Non abbiamo “ripulito” un dataset: abbiamo corretto una storia di business che sembrava plausibile proprio perché il duplicato non aveva generato alcun errore tecnico.

## La stessa chiave ripetuta può raccontare storie diverse

Tre righe con lo stesso `order_id` possono essere copie accidentali, versioni successive dello stesso record, eventi di stato, pagamenti parziali oppure rettifiche. La frequenza della chiave segnala un'incompatibilità con l'assunzione iniziale, ma non decide da sola che cosa eliminare.

Anche una regola apparentemente robusta come:

```sql
ROW_NUMBER() OVER (
    PARTITION BY order_id
    ORDER BY updated_at DESC
)
```

ha senso soltanto se `order_id` identifica davvero l'entità da deduplicare, `updated_at` ordina correttamente le versioni e la versione più recente sostituisce le precedenti. Se invece le righe sono eventi storici con significato proprio, la stessa query cancella informazione reale.

Il codice quindi applica una regola di deduplica; non può giustificarla.

## Deduplicare entità è ancora più delicato

Con i clienti il problema si sposta dall'evento all'identità. Due record con email diverse possono appartenere alla stessa persona; due record con la stessa email possono rappresentare persone differenti. Un account può essere condiviso e un indirizzo può cambiare.

Una regola come `stessa email = stesso cliente` riduce la complessità, ma può introdurre false merge. Una regola troppo prudente produce invece false split. Entrambi gli errori alterano clienti unici, repeat purchase, retention e lifetime value.

Per questo il controllo minimo su una tabella critica deve osservare non soltanto il numero di duplicati perfetti, ma la cardinalità della chiave attesa, la distribuzione delle righe per chiave, l'evoluzione temporale delle ripetizioni e gli attributi che differiscono tra record con la stessa identità presunta.

Se una tabella “una riga per ordine” passa improvvisamente al 6% di `order_id` ripetuti dopo una release, il dato sta raccontando un cambiamento del processo. La domanda non è ancora quali righe cancellare, ma **che cosa ha reso possibile una seconda rappresentazione dello stesso identificatore**.

> **Deduplicare non significa rendere il dataset più corto. Significa stabilire quando più record descrivono la stessa realtà e applicare una regola riproducibile che non cancelli eventi legittimi.**
