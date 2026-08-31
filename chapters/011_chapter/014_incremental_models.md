## 11.14 Modelli incrementali: non ricalcolare il mondo ogni notte

Quando i dati crescono, ricalcolare tutto da zero può diventare lento, costoso e inutile.

Un modello incrementale aggiorna soltanto la parte necessaria.

L'idea sembra semplice:

```text
ieri avevo 3 miliardi di righe
oggi ne sono arrivate 12 milioni
elaboro soprattutto quelle 12 milioni
```

Ma la difficoltà reale è capire **quali righe possono ancora cambiare**.

### Append-only vs dati mutabili

Se una sorgente è davvero append-only, la logica incrementale è relativamente semplice.

Esempio:

```sql
WHERE event_timestamp > max_timestamp_already_loaded
```

Ma molti dati di business non sono immutabili.

Un ordine può essere creato oggi e rimborsato tra tre settimane. Un pagamento può fallire e poi essere recuperato. Un ticket può cambiare stato. Una fattura può essere rettificata.

Se carichiamo solo i record "nuovi", perdiamo gli aggiornamenti.

### Caso realistico: il revenue model che smette di vedere i refund

**ModaLane** crea un modello incrementale sulle vendite.

Ogni notte carica:

```sql
WHERE order_created_at >= CURRENT_DATE - 1
```

La pipeline è veloce e sembra corretta.

Dopo due mesi il Finance team nota che il net revenue del warehouse è sistematicamente superiore al ledger.

La causa: i refund avvengono mediamente 9 giorni dopo l'ordine. Il modello non riapre mai gli ordini più vecchi.

La soluzione non è necessariamente un full refresh giornaliero. Può essere una **lookback window**:

```sql
WHERE updated_at >= CURRENT_DATE - 30
```

oppure una strategia CDC/change tracking, se disponibile.

### Unique key e merge

Un modello incrementale spesso necessita di una chiave stabile per decidere se:

- inserire una nuova riga;
- aggiornare una riga esistente.

Per un ordine:

```text
unique_key = order_id
```

Il pattern concettuale diventa:

```text
new or changed source rows
        ↓
match on business/unique key
        ↓
INSERT if new
UPDATE/MERGE if changed
```

La documentazione Microsoft sul caricamento di modelli dimensionali descrive una logica analoga: i record sorgente vengono confrontati tramite business key per identificare nuovi o modificati elementi, con gestione diversa a seconda del tipo di dimensione.[^ms-load]

### Late-arriving data

Gli eventi non arrivano sempre in ordine.

Esempio:

- evento accaduto: 1 agosto;
- dispositivo offline;
- evento ricevuto: 4 agosto.

Se il modello incrementale seleziona solo:

```sql
WHERE event_date = CURRENT_DATE
```

l'evento del 1 agosto potrebbe non essere mai caricato.

Per questo è utile distinguere:

- `event_time`;
- `ingestion_time`;
- `updated_at`.

### Full refresh non scompare

Anche con modelli incrementali, può servire periodicamente un full refresh per:

- correggere bug storici;
- applicare nuove business rules;
- ricostruire una dimensione;
- eliminare drift accumulato;
- gestire cambiamenti di schema.

La domanda importante è: **il modello è ricostruibile?**

Se il risultato dipende da uno stato incrementale che nessuno sa rigenerare, abbiamo guadagnato velocità ma perso affidabilità.

### Idempotenza e backfill

Una pipeline matura deve supportare:

- rerun senza duplicazioni;
- backfill di periodi storici;
- ripartenza dopo failure;
- gestione di record tardivi;
- audit di cosa è stato caricato.

### Regola operativa

Prima di rendere un modello incrementale chiedere:

1. i record possono cambiare dopo la creazione?
2. qual è la colonna affidabile di modifica?
3. quanto tardi possono arrivare gli eventi?
4. qual è la unique key?
5. cosa succede ai delete?
6. possiamo fare backfill?
7. possiamo ricostruire tutto da zero?
8. abbiamo riconciliazioni per verificare che incremental e full refresh convergano?

**Incrementale non significa processare meno dati a ogni costo. Significa processare solo i dati necessari senza perdere la storia reale.**

[^ms-load]: Microsoft Learn, *Load tables in a dimensional model*, https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-load-tables
