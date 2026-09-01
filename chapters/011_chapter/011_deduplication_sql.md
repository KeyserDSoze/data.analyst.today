## 11.10 Deduplicazione: scegliere quale realtà vogliamo rappresentare

La deduplicazione sembra un problema tecnico finché non poniamo la domanda giusta:

> **Quali righe rappresentano lo stesso fenomeno e quale versione deve sopravvivere nel modello analitico?**

Due righe uguali possono essere un retry tecnico. Due righe con la stessa business key possono invece essere due versioni legittime di uno stato. Due righe dello stesso ordine possono essere eventi economici diversi che non devono essere eliminate.

Per questo `SELECT DISTINCT` non è una strategia di deduplicazione. È soltanto un operatore SQL.

### Tre tipi di tabella da non confondere

Prima di deduplicare conviene classificare il dato.

**Entità corrente**

Una riga finale per soggetto, per esempio lo stato corrente di un ordine.

**Versioni**

Più righe descrivono lo stesso soggetto in momenti successivi.

**Eventi**

Ogni riga rappresenta un accadimento che può avere valore autonomo.

Questa distinzione entra direttamente nell'**Analytical Data Contract**.

Se il contratto dice:

```text
model: current_orders
grain: una riga per order_id
source semantics: versioni dello stato ordine
winner rule: updated_at più recente, poi ingestion_at
```

la deduplicazione diventa verificabile.

### Caso simulato/composito — LumaShop e il revenue +8% senza vendite aggiuntive

Dopo una migrazione ETL, LumaShop vede crescere la revenue giornaliera dell'8%, mentre il sistema operativo non mostra più ordini.

Nel raw layer compare:

```text
order_id   updated_at   ingestion_at   status   amount
A102       10:02:11     10:02:20       paid     120
A102       10:04:38     10:04:45       paid     120
A102       10:04:38     10:05:02       paid     120
```

La seconda riga è una nuova versione. La terza è un retry della stessa versione.

`SELECT DISTINCT *` può eliminare soltanto righe perfettamente identiche; qui `ingestion_at` è diverso e quindi tutte e tre sopravvivono.

Se il modello desiderato è **lo stato corrente dell'ordine**, una possibile regola è:

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

La parte importante non è `ROW_NUMBER()`. Sono le decisioni che la rendono corretta:

- identità = `order_id`;
- grain finale = una riga per ordine;
- priorità = versione business più recente;
- tie-break = ultimo arrivo;
- output = stato corrente, non storia degli eventi.

### Quando deduplicare distrugge informazione

Consideriamo invece:

```text
payment_id | order_id | event_type | amount
P1         | A102     | capture    | 120
P2         | A102     | refund     | -120
```

Entrambe le righe riguardano lo stesso ordine, ma sono due eventi economici distinti.

Deduplicare per `order_id` cancellerebbe parte della realtà.

La domanda diventa quindi:

> **La chiave su cui sto deduplicando identifica l'evento o soltanto l'entità a cui l'evento appartiene?**

### Il tie-break deve essere deterministico

Un pattern fragile è:

```sql
ROW_NUMBER() OVER (
    PARTITION BY order_id
    ORDER BY updated_at DESC
)
```

se più righe possono avere lo stesso `updated_at`.

Il database è libero di scegliere tra i pari merito. Due esecuzioni potrebbero teoricamente selezionare righe diverse.

Serve quindi un ordine completo, per esempio:

```text
updated_at DESC,
ingestion_at DESC,
source_sequence DESC
```

Il criterio deve avere significato e non essere inventato solo per far sparire il duplicato.

### Idempotenza: il problema dovrebbe essere risolto anche a monte

Una pipeline è idempotente quando rieseguirla con gli stessi input non moltiplica il risultato.

La deduplicazione analitica può proteggere il modello downstream, ma non sostituisce:

- chiavi di idempotenza in ingestion;
- gestione dei retry;
- merge/upsert coerenti;
- audit delle versioni;
- capacità di backfill.

Il Capitolo 12 entrerà nell'architettura. Qui il punto è più limitato: **l'analista deve riconoscere quando la tabella che sta interrogando contiene versioni o retry e non eventi indipendenti**.

### Gli invarianti da trasformare in test

Se il contratto dice “una riga per ordine corrente”, allora possiamo testare:

```sql
SELECT order_id
FROM current_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Ma zero duplicati non basta. Potremmo aver eliminato troppo.

Controlliamo anche:

- righe raw vs righe finali;
- business key coinvolte;
- valore economico rimosso;
- distribuzione dei retry per sorgente;
- percentuale di record con tie;
- riconciliazione con il sistema operativo.

### Campo del contract: identity/version rule

Per un dataset soggetto a versionamento, l'Analytical Data Contract dovrebbe poter dichiarare:

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

A quel punto la deduplicazione non è più un trucco nascosto dentro una CTE.

Diventa una regola esplicita del prodotto dati.

> **Deduplicare significa scegliere quale rappresentazione del fenomeno vogliamo conservare. Se quella scelta non è dichiarata, il modello può essere unico e comunque essere sbagliato.**
