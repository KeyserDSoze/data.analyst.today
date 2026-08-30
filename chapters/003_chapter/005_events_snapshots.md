## 3.4 Eventi, stati e snapshot: capire il tempo nel dato

Non tutti i dati descrivono il tempo nello stesso modo.

Una transazione è un evento: avviene in un momento specifico.

Un saldo di magazzino è invece uno stato: descrive una condizione valida in un certo istante o intervallo.

Questa differenza sembra semplice, ma determina quali aggregazioni sono corrette.

### Event data

Gli eventi rappresentano qualcosa che è accaduto:

- acquisto;
- login;
- click;
- pagamento;
- spedizione;
- apertura ticket;
- cambio stato;
- misurazione sensore.

Gli eventi sono spesso additivi nel tempo: se abbiamo 10 ordini lunedì e 12 martedì, possiamo dire che nei due giorni abbiamo avuto 22 ordini.

### Snapshot data

Gli snapshot descrivono invece uno stato in momenti successivi.

| date | warehouse | product | stock |
|---|---|---|---:|
| 2026-08-01 | A | P1 | 100 |
| 2026-08-02 | A | P1 | 95 |
| 2026-08-03 | A | P1 | 110 |

La somma `100 + 95 + 110 = 305` non rappresenta lo stock totale del periodo. Stiamo sommando tre fotografie successive dello stesso fenomeno.

Possiamo invece essere interessati a:

- stock alla fine del periodo;
- stock medio;
- minimo o massimo;
- variazione tra inizio e fine.

### Flow vs stock

Una distinzione utile è:

- **flow**: quantità che si accumula durante un intervallo, come vendite o nuovi ticket;
- **stock**: quantità esistente in un momento, come disponibilità, utenti attivi o saldo.

Le metriche stock sono spesso **semi-additive**: possono essere sommate lungo alcune dimensioni ma non lungo il tempo.

### Quale timestamp stiamo usando?

Un record può contenere molti tempi diversi:

- `created_at`;
- `updated_at`;
- `paid_at`;
- `shipped_at`;
- `event_time`;
- `ingested_at`;
- `processed_at`.

Se analizziamo vendite giornaliere usando `created_at` otteniamo una storia diversa rispetto a `paid_at`.

E nei sistemi moderni può esistere una differenza importante tra **event time**, il momento in cui il fenomeno è avvenuto, e **processing/ingestion time**, il momento in cui il sistema analitico lo ha ricevuto.

Questo spiega perché i numeri degli ultimi giorni possono cambiare retroattivamente quando arrivano eventi in ritardo.

### Domanda pratica

Per ogni dataset temporale dovremmo poter rispondere:

> Questo record descrive qualcosa che è successo, oppure lo stato di qualcosa in un dato momento?

E subito dopo:

> Quale timestamp rappresenta il tempo che interessa alla domanda di business?

Queste due domande evitano una quantità sorprendente di errori analitici.
