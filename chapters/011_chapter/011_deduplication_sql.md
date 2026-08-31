## 11.10 Deduplication SQL: quando due righe non sono due eventi

La deduplicazione sembra semplice finché non chiediamo:

> **Duplicato rispetto a cosa?**

Due righe identiche byte per byte possono essere davvero duplicate. Ma due righe con lo stesso `order_id` e timestamp diversi possono rappresentare:

- aggiornamenti successivi dello stesso ordine;
- retry tecnici;
- eventi diversi;
- errori di ingestion;
- versioni legittime di uno stesso record.

Deduplicare senza una definizione di identità può distruggere informazione corretta tanto facilmente quanto può eliminare rumore.

### Caso realistico: revenue +8% senza vendere nulla in più

**LumaShop** nota che la revenue giornaliera è cresciuta dell'8% dopo una migrazione ETL.

Gli ordini sul sistema operativo non mostrano alcuna crescita simile.

La tabella raw contiene:

```text
order_id   updated_at           status      amount
A102       10:02:11             paid        120
A102       10:04:38             paid        120
A102       10:04:38             paid        120
```

La pipeline ha acquisito sia una versione aggiornata sia un retry identico.

Una semplice:

```sql
SELECT DISTINCT *
```

rimuove solo le due righe perfettamente uguali, ma lascia due versioni dello stesso ordine.

La revenue resta quindi sovrastimata.

### Deduplicare richiede una business key e una regola di precedenza

Se il modello analitico vuole **una riga per ordine nello stato più recente**, la logica può essere:

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

La window function non è il punto importante. Il punto è aver deciso:

- l'entità: `order_id`;
- la versione vincente: quella con `updated_at` più recente;
- il tie-breaker: `ingestion_at`;
- il significato finale: una riga per ordine corrente.

### Ma attenzione: gli eventi non vanno deduplicati come gli stati

Consideriamo una tabella di pagamenti:

```text
payment_id | order_id | event_type | amount
P1         | A102     | capture    | 120
P2         | A102     | refund     | -120
```

Deduplicare per `order_id` significherebbe cancellare un evento economico reale.

Quindi la domanda fondamentale è:

**questa tabella rappresenta entità, versioni o eventi?**

### Idempotenza

Una pipeline robusta dovrebbe poter essere rieseguita senza moltiplicare i dati.

Se caricare due volte lo stesso file produce due volte gli stessi ordini, il sistema non è idempotente.

Una deduplicazione a valle può limitare il danno, ma non sostituisce una strategia di ingestion corretta.

### Test utili

Per una tabella che dovrebbe avere una riga per ordine:

```sql
SELECT order_id, COUNT(*)
FROM orders_clean
GROUP BY order_id
HAVING COUNT(*) > 1;
```

Il risultato dovrebbe essere vuoto.

Ma anche un risultato vuoto non prova che il modello sia corretto: potremmo aver eliminato troppe righe.

Conviene quindi controllare anche:

- conteggio raw vs clean;
- numero di chiavi duplicate;
- valore economico rimosso;
- distribuzione dei duplicati per sorgente e giorno;
- pattern dei retry.

### Metodo operativo

Prima di deduplicare:

1. definire il grain desiderato;
2. identificare la business key;
3. capire se le righe rappresentano eventi o versioni;
4. definire la precedenza tra versioni;
5. rendere il tie-break deterministico;
6. misurare cosa viene eliminato;
7. testare che la deduplicazione non cancelli eventi reali.

**`DISTINCT` è un operatore SQL. La deduplicazione è una decisione semantica.**
