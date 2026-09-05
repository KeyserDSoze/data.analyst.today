## 11.14 Modelli incrementali: processare meno senza perdere cambiamenti reali

Quando i dati crescono, ricalcolare tutto da zero può diventare lento e costoso. Ma “incrementale” non dovrebbe significare semplicemente “leggi le righe nuove”. La definizione utile è più rigorosa:

> **processa tutte le righe che possono ancora modificare lo stato analitico corretto, evitando il resto.**

Questa differenza conta perché molti domini non sono append-only. Un ordine creato oggi può essere rimborsato fra tre settimane; un ticket cambia stato; una fattura viene rettificata; una spedizione riceve eventi tardivi. Se la pipeline riapre soltanto i record creati oggi, smette progressivamente di rappresentare il processo reale.

### ModaLane: refund invisibili in un modello velocissimo

ModaLane materializza ogni notte il net revenue selezionando:

```sql
WHERE order_created_at >= CURRENT_DATE - 1
```

La pipeline è veloce. Dopo due mesi Finance osserva però una sovrastima sistematica: molti refund arrivano giorni dopo e gli ordini vecchi non vengono più riaperti. Il modello è incrementale rispetto alla data di creazione, ma non rispetto al processo che modifica il valore economico.

Microsoft Fabric raccomanda il caricamento incrementale delle fact table quando possibile perché è più scalabile e riduce il lavoro su sorgente e destinazione; la condizione, però, è poter identificare in modo affidabile record nuovi **o modificati**.

Fonte: https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-load-tables

### Tre tempi per osservare il cambiamento

Per molti dataset è utile distinguere:

- `event_time`: quando il fatto è accaduto;
- `updated_at`: quando il record business è cambiato;
- `ingestion_time`: quando la piattaforma analitica lo ha ricevuto.

Un evento può accadere il 1° agosto, essere aggiornato subito ma arrivare il 4 agosto perché il dispositivo era offline. Filtrare per `event_date = CURRENT_DATE` il 4 agosto può perderlo definitivamente.

Una high watermark su `updated_at` funziona soltanto se quel timestamp viene aggiornato correttamente, non arriva in ritardo con valori più vecchi, usa clock coerenti e rende osservabili delete/correzioni. Altrimenti la watermark diventa una promessa di completezza che il source non può mantenere.

### Lookback window come policy di rischio

Una strategia pragmatica può rielaborare gli ultimi 30 giorni:

```sql
WHERE updated_at >= CURRENT_DATE - 30
```

Se il 95% delle modifiche tardive arriva entro quella finestra, catturiamo gran parte dei cambiamenti. Ma il restante 5% non scompare: deve avere una policy, per esempio CDC, reconciliation periodica, backfill mirato, full refresh programmato o coda delle business key tardive.

La lookback non è quindi un numero magico. È una scelta esplicita sul rischio residuo.

### Merge key, delete e replayability

Quando i record possono cambiare, la merge key deve rappresentare il grain finale. Se il modello è una riga per `order_id + line_id`, usare soltanto `order_id` come unique key distrugge linee legittime.

Anche i delete vanno definiti. La sorgente può richiedere hard delete, soft delete con `is_deleted`, evento di cancellazione o mantenimento storico per audit. Non esiste una regola universale, ma deve esistere una regola.

Infine, incrementalità non elimina il bisogno di full refresh. Ricostruire tutto può servire per correggere bug storici, cambiare business rule, ricostruire una SCD o verificare drift accumulato. La domanda importante è se il modello sia **replayable** da una fonte di verità o dipenda da uno stato incrementale irripetibile.

Per modelli critici è utile verificare periodicamente che:

```text
incremental result
≈
recomputed reference result
```

su finestre, campioni, checksum o full refresh programmati.

### Update semantics nell’Analytical Data Contract

```text
source mutability:
change detection field/mechanism:
unique key:
lookback window:
late-arrival policy:
delete policy:
merge behavior:
backfill procedure:
full-refresh capability:
reconciliation rule:
```

> **Incrementale non significa elaborare meno dati possibile. Significa evitare lavoro inutile senza perdere nessuna modifica che possa cambiare la risposta analitica.**
