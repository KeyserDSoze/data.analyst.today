## 3.7 Duplicati: quando una riga in più diventa un milione di euro in più

Un duplicato non è sempre una riga identica a un'altra.

Nel lavoro reale, i duplicati più pericolosi sono spesso duplicati **semantici**: record diversi che rappresentano lo stesso evento economico, la stessa persona, lo stesso ordine o la stessa transazione.

### Caso studio simulato — Il fatturato cresciuto del 7% durante la notte

L'azienda immaginaria **Nordline Retail** vende arredamento online in quattro Paesi europei. Il lunedì mattina il direttore commerciale riceve una dashboard con una notizia sorprendente: il fatturato del weekend è cresciuto del 7,2% rispetto al weekend precedente.

Il dato sembra coerente con una campagna promozionale lanciata il venerdì sera. Il team marketing è pronto a rivendicare il risultato.

Un'analista, però, nota qualcosa di strano: il numero degli ordini è aumentato del 6,9%, mentre le sessioni del sito sono rimaste quasi stabili. La conversione apparente è salita troppo rapidamente.

Inizia quindi dal livello più basso: la tabella `orders`.

Trova 184.223 righe nel weekend. Il sistema di e-commerce, però, dichiara 171.906 ordini unici.

La differenza è enorme.

Il problema emerge poco dopo: durante una migrazione, un processo ETL è stato eseguito due volte su una finestra temporale di circa tre ore. I record non sono identici perché il campo `load_timestamp` è diverso. Per un semplice controllo `SELECT DISTINCT *` non risultano quindi duplicati.

La chiave naturale dell'evento è invece `order_id`.

Quando il team ricontrolla:

```sql
SELECT
    COUNT(*) AS rows,
    COUNT(DISTINCT order_id) AS unique_orders
FROM orders
WHERE order_date BETWEEN '2026-08-21' AND '2026-08-23';
```

emerge immediatamente il problema.

Il fatturato non era cresciuto del 7,2%.

Era cresciuto dell'1,1%.

La campagna non aveva prodotto il risultato sperato.

### La lezione

Prima di aggregare una misura bisogna sapere **che cosa identifica univocamente l'evento**.

Le domande minime sono:

- Qual è la chiave naturale del record?
- Può esistere più di una riga per quella chiave?
- Se sì, perché?
- Il duplicato è tecnico, funzionale o legittimo?
- Quale record va mantenuto?
- Esiste un ordine temporale affidabile tra i record?

### Deduplicare non significa cancellare alla cieca

Immaginiamo due righe con lo stesso `customer_id`.

Potrebbero essere un duplicato.

Oppure due versioni successive dello stesso cliente.

Oppure due clienti distinti ai quali è stato assegnato erroneamente lo stesso identificatore.

Prima di eliminare una riga dobbiamo capire il processo che l'ha prodotta.

Una strategia comune consiste nel mantenere il record più recente:

```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY updated_at DESC
        ) AS rn
    FROM orders
)
SELECT *
FROM ranked
WHERE rn = 1;
```

Ma questa query è corretta solo se `updated_at` rappresenta davvero una sequenza affidabile delle versioni.

### Regola operativa

Non chiederti soltanto:

> "Ci sono righe duplicate?"

Chiediti:

> "Esistono più rappresentazioni dello stesso fatto economico o della stessa entità?"

È una domanda molto più potente.

> **Nota editoriale:** i case study narrativi del libro sono simulati o compositi e sono costruiti per riprodurre situazioni realistiche di lavoro.