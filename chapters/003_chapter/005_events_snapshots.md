## 3.4 Eventi, stati e snapshot: capire che cosa significa il tempo nel dato

Non tutti i dataset temporali raccontano il tempo nello stesso modo.

Un pagamento è un **evento**: qualcosa è accaduto in un momento specifico.

Uno stock di magazzino è uno **stato**: descrive una condizione valida in un certo istante.

Uno snapshot giornaliero è invece una fotografia periodica di quello stato.

Questa distinzione determina quali aggregazioni sono sensate.

### Eventi: qualcosa è successo

Esempi tipici:

- ordine creato;
- pagamento autorizzato;
- login;
- click;
- spedizione partita;
- ticket aperto;
- stato cambiato;
- lettura prodotta da un sensore.

Molte misure evento sono additive nel tempo. Se lunedì abbiamo 10 nuovi ordini e martedì 12, possiamo dire che nei due giorni sono stati creati 22 ordini.

Ma anche qui bisogna capire il grain: dieci righe di stato associate allo stesso ordine non sono dieci nuovi ordini.

### Snapshot: la stessa realtà fotografata più volte

Consideriamo:

| date | warehouse | product | stock |
|---|---|---|---:|
| 2026-08-01 | A | P1 | 100 |
| 2026-08-02 | A | P1 | 95 |
| 2026-08-03 | A | P1 | 110 |

La somma `100 + 95 + 110 = 305` non rappresenta lo stock del periodo. Stiamo sommando tre fotografie successive della stessa quantità.

Possiamo invece voler conoscere:

- stock finale;
- stock medio;
- minimo o massimo;
- variazione tra inizio e fine;
- numero di giorni sotto una determinata soglia.

Le misure di stock sono spesso **semi-additive**: possono essere sommate lungo alcune dimensioni, per esempio tra magazzini, ma non necessariamente lungo il tempo.

### Uno stato può essere memorizzato o ricostruito

Un sistema può conservare soltanto lo stato corrente:

```text
order_id | status
A17      | delivered
```

oppure l'intera storia degli eventi:

```text
order_id | status       | event_time
A17      | created      | 10:01
A17      | paid         | 10:04
A17      | shipped      | 15:20
A17      | delivered    | 09:12 +2d
```

Le due rappresentazioni consentono domande differenti. Dal solo stato corrente sappiamo dove si trova l'ordine oggi, ma potremmo non essere in grado di misurare quanto tempo ha trascorso nelle fasi precedenti.

La struttura del dato definisce quindi non soltanto ciò che sappiamo, ma anche **ciò che non possiamo più ricostruire**.

### Event time, processing time e ingestion time

Un record può avere molti timestamp:

- `created_at`;
- `event_time`;
- `paid_at`;
- `updated_at`;
- `ingested_at`;
- `processed_at`.

Il timestamp rilevante dipende dalla domanda.

Se un ordine viene effettuato alle 23:58 ma arriva nel warehouse alle 00:06, l'analisi commerciale per giorno potrebbe usare il momento dell'ordine, mentre un controllo di pipeline potrebbe interessarsi al momento di ingestion.

Confondere i due produce errori soprattutto vicino a fine giornata, fine mese e durante backfill o ritardi.

### Late-arriving data e numeri che cambiano dopo la pubblicazione

Nei sistemi reali alcuni eventi arrivano in ritardo. Un'app mobile può restare offline, una sorgente può avere una coda, una pipeline può effettuare un backfill.

Di conseguenza, il dato di "ieri" può non essere definitivo oggi.

L'analista dovrebbe sapere:

- qual è la latenza normale;
- quando un periodo può considerarsi sufficientemente completo;
- se i dati storici vengono riscritti;
- quale timestamp stabilisce l'appartenenza al periodo analitico.

### Regola operativa

Per ogni dataset temporale, completa queste frasi:

> **Questo record descrive un evento / uno stato / uno snapshot di...**

> **Il tempo rilevante per la nostra domanda è...**

> **Il dato può arrivare o essere corretto fino a...**

Capire il tempo nel dato significa capire **quale storia il sistema è effettivamente in grado di raccontare**.