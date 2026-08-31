## 11.3 Window functions: confrontare senza distruggere il dettaglio

Le funzioni finestra sono uno dei punti in cui SQL diventa particolarmente potente per l'analisi, perché permettono di calcolare aggregazioni relative senza perdere il grain originale.

Con `GROUP BY`, se partiamo da una riga per ordine e raggruppiamo per cliente, otteniamo una riga per cliente.

Con una window function possiamo invece mantenere una riga per ordine e aggiungere, per esempio:

- totale speso dal cliente;
- ranking dell'ordine;
- valore dell'ordine precedente;
- media mobile;
- quota sul totale;
- cumulato progressivo.

### Caso simulato — Luma Fashion e il cliente che “sta spendendo di più”

Luma Fashion vuole individuare clienti il cui valore d'ordine sta crescendo.

Una semplice query aggregata per mese mostra che una cliente, `C10482`, ha speso:

- aprile: €420;
- maggio: €610;
- giugno: €790.

Il CRM decide di inserirla in un segmento premium.

Analizzando gli ordini singoli con `LAG`, emerge però un quadro diverso:

```sql
SELECT
    customer_id,
    order_date,
    order_value,
    LAG(order_value) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_value
FROM orders;
```

Il mese di giugno contiene un solo ordine da €790, seguito da un reso quasi totale di €720 registrato il mese successivo.

La crescita mensile era reale dal punto di vista della fatturazione lorda, ma non dal punto di vista del valore economico netto del cliente.

La window function non risolve automaticamente il problema, ma rende più facile analizzare la sequenza degli eventi senza perdere dettaglio.

### Ranking e top-N per gruppo

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
            ORDER BY revenue DESC
        ) AS rn
    FROM product_revenue
)
SELECT *
FROM ranked
WHERE rn <= 3;
```

Questo pattern è utile perché separa chiaramente due grain:

1. una riga per prodotto-categoria;
2. ranking all'interno della categoria.

### `ROW_NUMBER`, `RANK` e `DENSE_RANK`

La differenza emerge in presenza di pari merito.

Valori: 100, 100, 90.

- `ROW_NUMBER`: 1, 2, 3;
- `RANK`: 1, 1, 3;
- `DENSE_RANK`: 1, 1, 2.

La scelta non è estetica. Dipende dalla domanda business.

Se dobbiamo assegnare esattamente tre slot promozionali, `ROW_NUMBER` può essere necessario, con una regola di tie-break esplicita.

Se vogliamo classificare performance equivalenti, `RANK` o `DENSE_RANK` possono essere più coerenti.

### Running total e cumulative metrics

```sql
SUM(net_revenue) OVER (
    PARTITION BY customer_id
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS lifetime_revenue_to_date
```

Questa metrica risponde a una domanda temporale precisa: quanto revenue cumulato aveva generato il cliente **fino a quel momento**?

È molto diversa dal lifetime revenue finale associato retroattivamente a tutti gli eventi passati.

La distinzione è cruciale quando costruiamo feature per modelli predittivi: usare informazioni future crea leakage.

### Medie mobili

```sql
AVG(daily_orders) OVER (
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS moving_avg_7d
```

Una media mobile di sette righe non coincide necessariamente con sette giorni se mancano date.

Se la serie contiene solo giorni in cui esiste almeno un ordine, sei righe precedenti potrebbero coprire dieci giorni di calendario.

Ancora una volta: la sintassi può essere corretta e la semantica sbagliata.

### Caso simulato — GridPay e il falso aumento delle transazioni

GridPay monitora il volume giornaliero con una media mobile a sette righe. Durante un problema di ingestione, due domeniche non vengono caricate perché hanno volume molto basso.

La media mobile sale artificialmente.

Il team inizialmente interpreta il movimento come crescita organica.

La soluzione non è cambiare la window function, ma costruire prima una calendar spine completa e fare un `LEFT JOIN` degli eventi sulle date attese.

### Regola operativa

Le window functions sono particolarmente utili quando la domanda contiene parole come:

- precedente;
- successivo;
- cumulato;
- ultimo;
- primo;
- ranking;
- quota;
- media mobile;
- rispetto al gruppo;
- rispetto alla storia dello stesso soggetto.

Ma prima di usarle dobbiamo sempre definire:

- `PARTITION BY`: qual è il gruppo analitico?
- `ORDER BY`: qual è l'ordine temporale o logico?
- frame: quali righe entrano davvero nel calcolo?

---

**Riferimento**

PostgreSQL Documentation, *Window Functions*: https://www.postgresql.org/docs/current/tutorial-window.html
