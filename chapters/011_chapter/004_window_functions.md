## 11.3 Window functions: aggiungere contesto senza perdere il grain

Le window functions sono particolarmente importanti per un Data Analyst perché permettono di calcolare informazioni relative a un gruppo **senza collassare le righe del dataset**.

PostgreSQL descrive esplicitamente questa differenza: una window function opera su righe correlate alla riga corrente, ma a differenza di una normale aggregazione non raggruppa quelle righe in un solo output. Le righe mantengono la propria identità.

Questo ci dà un criterio semantico molto utile:

- `GROUP BY` cambia il grain;
- una window function, in generale, aggiunge contesto mantenendo il grain dell’output.

Fonte: https://www.postgresql.org/docs/current/tutorial-window.html

### Caso simulato/composito — Luma Fashion e il cliente che “stava spendendo di più”

Luma Fashion vuole individuare clienti con valore economico crescente.

Una cliente, `C10482`, mostra revenue mensile:

- aprile: €420;
- maggio: €610;
- giugno: €790.

Il CRM propone di spostarla nel segmento premium.

Prima della decisione l’analista guarda gli ordini in sequenza:

```sql
SELECT
    customer_id,
    order_date,
    order_id,
    order_value,
    LAG(order_value) OVER (
        PARTITION BY customer_id
        ORDER BY order_date, order_id
    ) AS previous_order_value
FROM orders;
```

Giugno contiene un unico ordine da €790 seguito da un reso quasi totale di €720 registrato il mese successivo.

La crescita della fatturazione lorda esiste, ma non equivale automaticamente a crescita del valore netto del cliente.

La window function non “scopre la verità”. Permette però di mantenere il dettaglio dell’evento mentre aggiungiamo il contesto della storia dello stesso cliente.

### `PARTITION BY` definisce la popolazione di confronto

Considera:

```sql
AVG(order_value) OVER (
    PARTITION BY customer_id
)
```

La domanda incorporata è:

> quanto vale questo ordine rispetto alla storia degli ordini dello stesso cliente?

Se usiamo invece:

```sql
AVG(order_value) OVER (
    PARTITION BY country
)
```

la domanda diventa:

> quanto vale questo ordine rispetto agli ordini dello stesso Paese?

`PARTITION BY` non è quindi semplice sintassi. Definisce **il gruppo di riferimento**.

### `ORDER BY` definisce la storia

Con funzioni come `LAG`, `LEAD`, running total e ranking, l’ordine non è un dettaglio.

Se due eventi condividono lo stesso timestamp e non esiste un tie-break deterministico, questa query:

```sql
LAG(status) OVER (
    PARTITION BY order_id
    ORDER BY event_at
)
```

può non avere una definizione univoca della sequenza.

In processi event-driven è spesso necessario aggiungere:

- event sequence;
- ingestion id;
- transaction id;
- timestamp con precisione sufficiente.

Il contratto temporale deve dire **che cosa significa “prima”**.

### `ROW_NUMBER`, `RANK` e `DENSE_RANK`: la policy sui pari merito

Valori: 100, 100, 90.

- `ROW_NUMBER`: 1, 2, 3;
- `RANK`: 1, 1, 3;
- `DENSE_RANK`: 1, 1, 2.

La scelta dipende dalla decisione.

Se dobbiamo assegnare esattamente tre slot promozionali, `ROW_NUMBER` richiede un tie-break esplicito.

Se vogliamo rappresentare performance equivalenti, `RANK` o `DENSE_RANK` possono essere semanticamente più corretti.

### Ranking top-N: prima si definisce il grain, poi si ordina

Per trovare i tre prodotti con più revenue in ogni categoria:

```sql
WITH product_revenue AS (
    SELECT
        category_id,
        product_id,
        SUM(net_revenue) AS revenue
    FROM order_lines
    GROUP BY category_id, product_id
), ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY category_id
            ORDER BY revenue DESC, product_id
        ) AS rn
    FROM product_revenue
)
SELECT *
FROM ranked
WHERE rn <= 3;
```

La sequenza è importante:

1. `product_revenue` cambia il grain a una riga per categoria-prodotto;
2. `ROW_NUMBER` mantiene quel grain e aggiunge una posizione relativa.

Questo è esattamente il modo in cui dovremmo leggere una trasformazione analitica: **dove cambia il grain e dove no?**

### Running total e informazione disponibile “fino a quel momento”

```sql
SUM(net_revenue) OVER (
    PARTITION BY customer_id
    ORDER BY order_date, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS revenue_to_date
```

Questa colonna rappresenta il revenue cumulato disponibile **fino alla riga corrente**.

È diversa dal lifetime revenue finale copiato retroattivamente su tutti gli eventi del cliente.

La distinzione diventa critica per feature predittive e analisi storiche: il secondo approccio può introdurre informazione futura e leakage.

### Il frame è parte della metrica

Una media mobile come:

```sql
AVG(daily_orders) OVER (
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
)
```

usa sette **righe**, non necessariamente sette giorni di calendario.

Se la tabella non contiene giorni a volume zero, sette righe possono coprire dieci o dodici giorni.

### Caso simulato/composito — GridPay e la crescita creata dai giorni mancanti

GridPay monitora il volume giornaliero con una media mobile a sette righe.

A causa di un problema di ingestione, due domeniche a basso volume non vengono caricate.

La moving average sale.

Il team interpreta inizialmente il movimento come crescita organica.

Il problema non si risolve cambiando funzione finestra. Serve costruire prima una **calendar spine** completa e rappresentare anche i giorni senza eventi.

La serie analitica deve dichiarare se l’assenza di una riga significa:

- zero;
- dato mancante;
- giorno non eleggibile;
- pipeline non aggiornata.

Sono quattro semantiche diverse.

### Window contract

Per ogni window function importante, l’Analytical Data Contract dovrebbe rendere espliciti:

| Campo | Domanda |
|---|---|
| grain input/output | resta una riga per che cosa? |
| partition | qual è il gruppo di confronto? |
| order | qual è la sequenza e come gestiamo i pari timestamp? |
| frame | quali righe entrano nel calcolo? |
| time completeness | le unità temporali mancanti sono rappresentate? |
| as-of safety | stiamo usando solo informazione disponibile fino a quel momento? |

> **Una window function è potente non perché evita un `GROUP BY`, ma perché permette di aggiungere contesto senza perdere l’identità analitica della riga.**
