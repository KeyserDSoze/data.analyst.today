## 11.14 Modelli incrementali: processare meno senza perdere cambiamenti reali

Quando i dati crescono, ricalcolare tutto da zero può diventare lento, costoso e inutile.

Un modello incrementale aggiorna soltanto la parte che può aver cambiato il risultato.

La frase importante è l'ultima.

Non:

> “elabora solo le righe nuove”.

Ma:

> **“elabora tutte le righe che possono ancora modificare lo stato analitico corretto”.**

### Append-only e dati mutabili

Se una sorgente è veramente append-only, l'incrementalità può essere semplice.

Esempio:

```sql
WHERE event_timestamp > last_processed_event_timestamp
```

Ma molti domini non sono immutabili.

Un ordine può essere creato oggi e rimborsato fra tre settimane. Un pagamento può fallire e poi essere recuperato. Un ticket cambia stato. Una fattura viene rettificata. Una spedizione riceve un nuovo evento dopo giorni.

Se selezioniamo soltanto i record “creati oggi”, perdiamo gli aggiornamenti.

### Caso simulato/composito — ModaLane e i refund invisibili

ModaLane materializza ogni notte il net revenue selezionando:

```sql
WHERE order_created_at >= CURRENT_DATE - 1
```

La pipeline è veloce.

Dopo due mesi Finance osserva che il warehouse sovrastima sistematicamente il net revenue.

L'indagine mostra che:

- molti refund arrivano diversi giorni dopo l'ordine;
- alcuni ordini vecchi vengono aggiornati;
- la pipeline non riapre più quelle business key.

Il modello è incrementale rispetto alla **data di creazione**, ma non rispetto al **processo che modifica il valore economico**.

### Caso reale documentato — incremental load nei modelli dimensionali Microsoft Fabric

Microsoft raccomanda, quando possibile, il caricamento incrementale delle fact table perché è più scalabile e riduce il lavoro sui sistemi sorgente e di destinazione. La documentazione sottolinea però che è necessario riuscire a identificare in modo affidabile i record nuovi o modificati, per esempio tramite identificatori, timestamp, change tracking o CDC.

Fonte: https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-load-tables

La lezione non è specifica di Fabric:

> **l'incrementalità dipende dalla capacità di osservare i cambiamenti, non soltanto dalla capacità di filtrare per data.**

### Tre tempi da distinguere

Per molti dataset servono almeno:

- `event_time`: quando il fatto è accaduto;
- `updated_at`: quando il record business è cambiato;
- `ingestion_time`: quando la piattaforma analitica lo ha ricevuto.

Esempio:

```text
evento reale:       1 agosto 14:20
record aggiornato:  1 agosto 14:21
dispositivo offline
ingestione:          4 agosto 09:03
```

Filtrare per `event_date = CURRENT_DATE` il 4 agosto può perdere definitivamente quell'evento.

### High watermark: utile solo se la watermark è affidabile

Una strategia classica mantiene un valore come:

```text
last_processed_updated_at = 2026-08-31 23:59:59
```

e legge ciò che viene dopo.

Funziona se:

- la colonna è aggiornata correttamente;
- i record non arrivano con timestamp più vecchi;
- clock e timezone sono coerenti;
- delete e correzioni sono osservabili.

Se queste condizioni non valgono, la watermark crea una falsa sensazione di completezza.

### Lookback window: pagare un po' di ricalcolo per maggiore sicurezza

Una strategia pragmatica può rielaborare una finestra recente:

```sql
WHERE updated_at >= CURRENT_DATE - 30
```

Se il 95% delle modifiche tardive arriva entro 30 giorni, la finestra cattura gran parte dei cambiamenti.

Ma dobbiamo dichiarare cosa succede al restante 5%.

Possibili risposte:

- CDC;
- reconciliation periodica;
- backfill mirato;
- full refresh programmato;
- coda delle business key tardive.

La lookback window è una policy di rischio, non un numero magico.

### Unique key e merge

Quando un record può essere modificato, serve spesso una chiave stabile:

```text
unique_key = order_id
```

Il pattern concettuale è:

```text
new/changed rows
→ match on key
→ insert new
→ update existing
```

Ma la unique key deve rappresentare il grain finale.

Se il modello è una riga per `order_id + line_id`, usare solo `order_id` come merge key distrugge righe legittime.

### Delete: il caso dimenticato

Molte pipeline incrementali gestiscono insert e update ma non delete.

Che cosa succede se una sorgente elimina un record?

Possibili semantiche:

- hard delete anche nel modello analitico;
- soft delete con `is_deleted`;
- evento di cancellazione separato;
- mantenimento storico per audit.

Non esiste una risposta universale. Deve esistere una risposta esplicita.

### Full refresh e replayability

Incrementale non significa che il full refresh diventa inutile.

Può servire per:

- correggere bug storici;
- cambiare una business rule;
- ricostruire una SCD;
- applicare uno schema nuovo;
- verificare drift accumulato.

La domanda critica è:

> **possiamo ricostruire il modello da una fonte di verità, oppure il risultato dipende da uno stato incrementale irripetibile?**

Un sistema che non può essere ricostruito è veloce finché non deve essere corretto.

### Reconciliation: incremental e full dovrebbero convergere

Per modelli importanti è utile verificare periodicamente:

```text
incremental result
vs
recomputed reference result
```

Non necessariamente su tutta la storia ogni notte. Può bastare:

- un campione di periodi;
- una finestra recente;
- checksum/aggregati;
- full refresh periodico.

L'obiettivo è intercettare errori cumulativi prima che diventino storia ufficiale.

### Campo del contract: update semantics

L'Analytical Data Contract dovrebbe dichiarare:

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

Questa è la vera specifica di un modello incrementale.

### Regola operativa

Prima di rendere un modello incrementale chiediamo:

1. quali record possono cambiare dopo la creazione?
2. come osserviamo quei cambiamenti?
3. quanto tardi possono arrivare?
4. qual è il grain della merge key?
5. come gestiamo delete e correzioni?
6. possiamo fare backfill?
7. possiamo ricostruire tutto da zero?
8. come dimostriamo che incremental e full refresh convergono?

> **Incrementale non significa elaborare meno dati possibile. Significa evitare lavoro inutile senza perdere nessuna modifica che possa cambiare la risposta analitica.**
