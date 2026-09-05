## 11.9 Slowly Changing Dimensions: decidere se il passato può cambiare

Le dimensioni descrivono entità che cambiano: clienti, prodotti, territori, dipendenti, account, negozi. La domanda analitica non è soltanto come memorizzare l’aggiornamento, ma **se il report di ieri deve cambiare quando oggi cambia l’attributo**.

Questa scelta viene prima della tecnica. Una **SCD Type 1** sovrascrive il valore precedente ed è adatta quando stiamo correggendo un errore, quando la storia non serve o quando vogliamo intenzionalmente reinterpretare il passato con la classificazione corrente. Una **SCD Type 2** crea invece una nuova versione della riga e preserva l’attributo storico. Microsoft Fabric documenta Type 2 proprio come il pattern in cui il cambiamento produce una nuova versione, con surrogate key, intervallo di validità e indicatore della versione corrente.

Fonte: https://learn.microsoft.com/en-us/fabric/data-factory/slowly-changing-dimension-type-two

Una struttura tipica è:

```text
customer_sk
customer_id
segment
valid_from
valid_to
is_current
```

La business key continua a identificare il cliente; la surrogate key identifica una versione storica di quel cliente.

### NovaParts: crescita reale, storia sbagliata

NovaParts presenta vendite Enterprise 2024 pari a **€18,2M** e 2025 pari a **€31,7M**, una crescita apparente del 74%. L’analista scopre che `dim_customer` conserva soltanto il segmento corrente. Nel 2025 molti clienti Mid-Market sono stati riclassificati Enterprise dopo aver superato una soglia di fatturato.

La query:

```sql
SELECT
    d.segment,
    SUM(f.revenue)
FROM fact_sales f
JOIN dim_customer d
  ON f.customer_id = d.customer_id
GROUP BY 1;
```

attribuisce retroattivamente al segmento Enterprise anche vendite 2024 generate quando quei clienti erano Mid-Market. Ricostruendo il segmento valido al momento della vendita, Enterprise 2024 diventa **€24,9M**; il 2025 resta **€31,7M** e la crescita comparabile scende a **+27%**.

La crescita non scompare. Cambia la spiegazione strategica.

### Il join point-in-time deve avere una sola risposta

La logica concettuale è:

```sql
fact.event_at >= dim.valid_from
AND fact.event_at < dim.valid_to
```

La convenzione `[valid_from, valid_to)` evita ambiguità ai confini, ma il vero invariant è più importante: **per ogni business key e momento deve esistere al massimo una versione valida**. Se due intervalli si sovrappongono, il join storico può moltiplicare la fact.

Una dimensione Type 2 dovrebbe quindi controllare almeno: una sola versione corrente per business key, `valid_from < valid_to`, nessuna sovrapposizione temporale, surrogate key unica e copertura delle fact storiche. Quando richiesta, può essere utile anche verificare la continuità degli intervalli.

Type 1 e Type 2 possono convivere nella stessa dimensione. Un typo nel nome può essere corretto con Type 1; segmento commerciale, account manager o classificazione prodotto possono richiedere Type 2 se il reporting deve preservare il contesto dell’epoca. La history policy va quindi pensata per attributo, non soltanto per tabella.

### Current view e historical view sono entrambe legittime

La direzione commerciale può chiedere: “quanto revenue storico generano i clienti che **oggi** sono Enterprise?”. Strategy può invece chiedere: “quanto revenue generava il segmento Enterprise secondo la classificazione valida in ogni periodo?”. La prima è una current-state reclassification; la seconda una historical as-of analysis.

Il problema nasce quando entrambe vengono chiamate `Enterprise revenue`.

Anche i late-arriving dimension records richiedono una policy. Se una vendita arriva oggi e la classificazione cliente corretta arriva domani ma è valida già da ieri, possiamo usare un unknown member temporaneo, backfill della surrogate key, restatement controllato o quarantena. La scelta dice quanto siamo disposti a cambiare il passato quando arriva informazione migliore.

### History policy nell’Analytical Data Contract

| Campo | Domanda |
|---|---|
| business key | quale entità cambia? |
| attribute | quale proprietà storicizziamo? |
| history policy | Type 1, Type 2 o altra policy? |
| event date | quale timestamp sceglie la versione? |
| restatement | il passato viene corretto? |
| late-arriving policy | cosa succede se la dimensione arriva tardi? |
| invariant | una sola versione valida per momento |

> **Se un attributo cambia domani, dobbiamo sapere in anticipo se vogliamo che cambi anche il report di ieri. La storicizzazione è la risposta tecnica a una decisione semantica.**
