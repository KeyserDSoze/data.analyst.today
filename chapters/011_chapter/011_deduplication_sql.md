## 11.10 Deduplicazione: scegliere quale realtà vogliamo rappresentare

La deduplicazione sembra un problema tecnico finché non chiediamo **quali righe descrivono lo stesso fenomeno e quale versione deve sopravvivere**. Due righe uguali possono essere un retry tecnico; due righe con la stessa business key possono essere versioni legittime; due righe dello stesso ordine possono essere eventi economici distinti. `SELECT DISTINCT` non risolve questa ambiguità: elimina soltanto righe identiche secondo le colonne selezionate.

Prima di deduplicare conviene capire se la sorgente rappresenta **entità correnti**, **versioni** o **eventi**. Se il modello finale deve essere `current_orders`, una riga per `order_id`, e la sorgente contiene versioni dello stato ordine, la winner rule deve entrare nell’Analytical Data Contract.

### LumaShop: revenue +8% senza ordini aggiuntivi

Dopo una migrazione ETL, LumaShop vede crescere la revenue giornaliera dell’8%, mentre il sistema operativo non mostra più ordini. Nel raw layer compare:

```text
order_id   updated_at   ingestion_at   status   amount
A102       10:02:11     10:02:20       paid     120
A102       10:04:38     10:04:45       paid     120
A102       10:04:38     10:05:02       paid     120
```

La seconda riga è una nuova versione; la terza è un retry della stessa versione. Poiché `ingestion_at` è diverso, `SELECT DISTINCT *` le conserva tutte.

Se vogliamo lo stato corrente dell’ordine, una possibile regola è:

```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY updated_at DESC, ingestion_at DESC
        ) AS rn
    FROM raw_orders
)
SELECT *
FROM ranked
WHERE rn = 1;
```

La parte decisiva non è `ROW_NUMBER()`. È il contratto che rende quella query legittima: identità `order_id`, output a una riga per ordine, priorità alla versione business più recente, tie-break sull’ultimo arrivo, output di current state e non di event history.

### Deduplicare può distruggere realtà

Consideriamo invece:

```text
payment_id | order_id | event_type | amount
P1         | A102     | capture    | 120
P2         | A102     | refund     | -120
```

Le due righe condividono l’ordine ma rappresentano eventi economici distinti. Deduplicare per `order_id` cancellerebbe parte del fenomeno. La domanda da fare è quindi se la chiave usata per la dedup identifica l’evento oppure soltanto l’entità a cui appartiene.

Anche il tie-break deve essere deterministico. Se più righe possono avere lo stesso `updated_at`, ordinare solo per quel campo lascia al database la scelta tra pari merito. Una sequenza completa come `updated_at DESC, ingestion_at DESC, source_sequence DESC` deve derivare da una semantica reale, non essere inventata soltanto per ottenere una riga.

### Dedup analitica e idempotenza di pipeline

La deduplicazione downstream può proteggere un modello, ma non sostituisce chiavi di idempotenza in ingestion, gestione dei retry, merge/upsert coerenti e audit delle versioni. Il Capitolo 12 allargherà il problema all’architettura. Qui basta riconoscere quando una tabella contiene versioni o retry e non osservazioni indipendenti.

Se il contract dice “una riga per ordine corrente”, possiamo testare l’unicità finale. Ma zero duplicati non basta: potremmo aver eliminato troppo. Conviene controllare anche righe raw vs finali, business key coinvolte, valore economico rimosso, distribuzione dei retry, percentuale di tie e riconciliazione con il sistema operativo.

### Identity/version rule

```text
business key:
record/event key:
version timestamp:
ingestion timestamp:
winner rule:
tie-break:
late update policy:
expected uniqueness after transformation:
```

> **Deduplicare significa scegliere quale rappresentazione del fenomeno conservare. Una tabella può essere perfettamente unica e continuare a essere semanticamente sbagliata.**
