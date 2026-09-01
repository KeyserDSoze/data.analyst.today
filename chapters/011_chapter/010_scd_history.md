## 11.9 Slowly Changing Dimensions: decidere se il passato può cambiare

Le dimensioni descrivono entità: clienti, prodotti, territori, dipendenti, account, negozi.

Ma le entità cambiano.

Un cliente cambia segmento. Un venditore cambia regione. Un prodotto cambia categoria. Un punto vendita cambia area commerciale.

La domanda analitica è:

> **quando analizziamo il passato, vogliamo usare la classificazione corrente o quella valida nel momento dell’evento?**

Questa è una scelta semantica prima di essere una scelta tecnica.

### Type 1: correggere o reinterpretare il passato

Con una Slowly Changing Dimension di tipo 1, il nuovo valore sovrascrive quello precedente.

È appropriato quando:

- il valore precedente era un errore;
- la storia non ha valore analitico;
- vogliamo intenzionalmente reinterpretare il passato con la classificazione corrente.

Esempio:

```text
Acme Srl
```

corretto in:

```text
ACME S.p.A.
```

Se si tratta soltanto di una correzione anagrafica, conservare la vecchia grafia può non servire.

### Type 2: preservare il contesto storico

Con una SCD Type 2, un cambiamento rilevante crea una nuova versione della riga.

Una struttura tipica può contenere:

```text
customer_sk
customer_id
segment
valid_from
valid_to
is_current
```

Per esempio:

| customer_sk | customer_id | segment | valid_from | valid_to | is_current |
|---:|---|---|---|---|---|
| 4102 | C884 | SMB | 2024-01-01 | 2025-10-01 | false |
| 9177 | C884 | Enterprise | 2025-10-01 | 9999-12-31 | true |

La business key `customer_id` identifica l’entità. La surrogate key identifica una **versione storica** di quell’entità.

Microsoft documenta la SCD Type 2 come un pattern in cui i cambiamenti dimensionali producono nuove versioni della riga per preservare la storia.

Fonte: https://learn.microsoft.com/en-us/fabric/data-factory/slowly-changing-dimension-type-two

### Caso simulato/composito — NovaParts e l’Enterprise che sembrava crescere del 74%

NovaParts, distributore industriale, presenta:

- vendite Enterprise 2024: €18,2M;
- vendite Enterprise 2025: €31,7M;
- crescita apparente: +74%.

L’analista scopre che `dim_customer` contiene soltanto il segmento corrente.

Nel 2025 molti clienti Mid-Market sono stati riclassificati Enterprise dopo aver superato una soglia di fatturato.

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

attribuisce retroattivamente al segmento Enterprise anche vendite del 2024 generate quando quei clienti erano Mid-Market.

Ricostruendo il segmento `as-of sale date`:

- Enterprise 2024: €24,9M;
- Enterprise 2025: €31,7M;
- crescita comparabile: +27%.

La crescita resta positiva. Cambia però la storia strategica raccontata dal KPI.

### Il join point-in-time

La logica concettuale per associare una fact alla versione dimensionale corretta è:

```sql
fact.event_at >= dim.valid_from
AND fact.event_at < dim.valid_to
```

La convenzione `[valid_from, valid_to)` evita sovrapposizioni ai confini se viene applicata in modo coerente.

Ma il vero invariant è:

> **per ogni fact e business key deve esistere al massimo una versione dimensionale valida al momento dell’evento.**

Se due versioni si sovrappongono, un join temporale può duplicare la fact.

### Test sulle SCD

Una dimensione Type 2 dovrebbe avere controlli come:

- una sola riga `is_current = true` per business key;
- nessun intervallo con `valid_from >= valid_to`;
- nessuna sovrapposizione temporale tra versioni della stessa key;
- continuità degli intervalli quando richiesta;
- surrogate key unica;
- fact storiche collegate a una versione valida.

La storicizzazione senza test può creare più ambiguità di quanta ne risolva.

### Type 1 e Type 2 possono convivere

Nella stessa dimensione:

- typo nel nome → Type 1;
- segmento commerciale → Type 2;
- account manager → Type 2 se serve analisi storica per ownership;
- email di contatto → dipende dall’uso;
- classificazione prodotto → Type 2 se il confronto storico deve preservare la tassonomia dell’epoca.

Il contratto va quindi definito **per attributo**, non soltanto per tabella.

### Current view e historical view possono essere entrambe corrette

Una direzione commerciale può voler sapere:

> quanto revenue storico generano oggi i clienti che oggi sono Enterprise?

Finance o Strategy possono invece chiedere:

> quanto revenue generava il segmento Enterprise secondo la classificazione valida in ciascun periodo?

La prima è una **current-state reclassification**.

La seconda è una **historical as-of analysis**.

Il problema nasce quando entrambe vengono chiamate “Enterprise revenue” senza specificare la policy.

### Late-arriving dimensions

A volte la fact arriva prima dell’attributo dimensionale corretto.

Esempio:

- vendita caricata oggi;
- classificazione cliente aggiornata domani ma valida già da ieri.

Il modello deve avere una policy:

- unknown member temporaneo;
- backfill della surrogate key;
- restatement controllato;
- quarantena della fact.

Anche qui la domanda è semantica: **quanto siamo disposti a cambiare il passato quando arriva informazione migliore?**

### History policy nell’Analytical Data Contract

Per gli attributi che cambiano documentiamo:

| Campo | Domanda |
|---|---|
| business key | quale entità cambia? |
| attribute | quale proprietà storicizziamo? |
| history policy | Type 1, Type 2 o altra policy? |
| event date | quale timestamp sceglie la versione? |
| restatement | il passato viene corretto? |
| late-arriving policy | cosa succede se la dimensione arriva tardi? |
| invariant | una sola versione valida per momento |

La domanda pratica da ricordare è:

> **Se questo attributo cambia domani, voglio che anche il report di ieri cambi?**

Se la risposta è no, la storia deve esistere da qualche parte nel modello.
