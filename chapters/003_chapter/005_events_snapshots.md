## 3.4 Eventi, stati e snapshot: che cosa significa il tempo nel dato

Due dataset possono contenere timestamp e raccontare storie temporali completamente diverse. Un pagamento è un **evento**: qualcosa è accaduto in un momento specifico. Lo stock di magazzino è uno **stato**: descrive una condizione valida in un certo istante. Uno snapshot giornaliero è invece una fotografia periodica di quello stato.

Questa distinzione non è terminologica. Determina quali aggregazioni hanno significato e quali trasformano più fotografie della stessa realtà in un totale inesistente.

Consideriamo uno snapshot di inventario:

| date | warehouse | product | stock |
|---|---|---|---:|
| 2026-08-01 | A | P1 | 100 |
| 2026-08-02 | A | P1 | 95 |
| 2026-08-03 | A | P1 | 110 |

La somma `100 + 95 + 110 = 305` non rappresenta lo stock del periodo. Le tre righe sono fotografie successive della stessa quantità. Possiamo invece voler conoscere lo stock finale, la media, il minimo, il massimo, la variazione o il numero di giorni sotto soglia. La misura è quindi **semi-additiva**: può essere sommata lungo alcune dimensioni — per esempio tra magazzini — ma non necessariamente lungo il tempo.

Una fact table transazionale funziona diversamente. Dieci ordini creati lunedì e dodici martedì possono essere sommati in ventidue nuovi ordini, purché ogni riga rappresenti davvero un evento distinto. Ancora una volta grain e tempo non possono essere separati: dieci eventi di stato dello stesso ordine non sono dieci ordini.

## La struttura decide quale storia resta ricostruibile

Un sistema può conservare soltanto lo stato corrente:

```text
order_id | status
A17      | delivered
```

oppure l'intera sequenza degli eventi:

```text
order_id | status       | event_time
A17      | created      | 10:01
A17      | paid         | 10:04
A17      | shipped      | 15:20
A17      | delivered    | 09:12 +2d
```

Nel primo caso sappiamo dove si trova l'ordine oggi, ma non possiamo necessariamente ricostruire quanto tempo abbia trascorso nelle fasi precedenti. Nel secondo possiamo calcolare durate e transizioni, ma dobbiamo capire se gli eventi sono completi, ordinati e correttamente associati all'ordine.

La modellazione del tempo definisce quindi anche **ciò che non possiamo più sapere**. Se il sistema sovrascrive lo stato senza conservarne la storia, nessuna query successiva potrà recuperare eventi che non sono stati registrati.

## Un record può avere più tempi validi

Un altro errore frequente consiste nel trattare tutti i timestamp come equivalenti. Un ordine può avere `created_at`, `paid_at`, `updated_at`, `event_time`, `ingested_at` e `processed_at`, ciascuno legato a una fase diversa del processo.

Se l'ordine avviene alle 23:58 e arriva nel warehouse alle 00:06, il giorno commerciale può dipendere da `event_time`, mentre un controllo di pipeline è interessato a `ingested_at`. Confondere i due sposta record tra giorni o mesi e diventa particolarmente pericoloso durante chiusure contabili, backfill e ritardi di sincronizzazione.

Lo stesso vale per dati che arrivano tardi. Un'app mobile offline, una coda o una pipeline in recovery possono aggiornare oggi ciò che è accaduto ieri. Il numero di “ieri” può quindi cambiare dopo la prima pubblicazione. L'analista deve conoscere la latenza normale, sapere quando un periodo è sufficientemente maturo e capire se lo storico viene riscritto retroattivamente.

Per ogni dataset temporale dobbiamo riuscire a formulare tre frasi:

> **Questo record descrive un evento / uno stato / uno snapshot di...**

> **Il tempo rilevante per la nostra domanda è...**

> **Il dato può arrivare o essere corretto fino a...**

Queste non sono tre voci di checklist indipendenti. Insieme definiscono quale sequenza di realtà il dataset è effettivamente in grado di raccontare.
