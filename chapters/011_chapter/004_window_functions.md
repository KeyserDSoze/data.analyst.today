## 11.3 Window functions: aggiungere contesto senza perdere il grain

Una window function è preziosa perché permette di aggiungere informazione relativa a un gruppo senza collassare le righe. PostgreSQL descrive proprio questa differenza: una normale aggregazione raggruppa più righe in un output; una window function lascia invece alle righe la propria identità e calcola il contesto attraverso `OVER`.

Fonte: https://www.postgresql.org/docs/current/tutorial-window.html

Questo ci dà una regola semantica utile: `GROUP BY` cambia il grain; una window function, salvo trasformazioni successive, lo conserva. La domanda diventa allora non “quale funzione finestra usare?”, ma **quale gruppo di riferimento, quale ordine e quale porzione di storia stiamo aggiungendo alla riga?**

### Luma Fashion: mantenere l’evento mentre leggiamo la storia

Luma Fashion vuole individuare clienti con valore economico crescente. La cliente `C10482` mostra revenue mensile di €420 ad aprile, €610 a maggio e €790 a giugno. Il CRM propone di spostarla nel segmento premium.

L’analista guarda però gli ordini in sequenza:

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

Giugno contiene un unico ordine da €790 seguito da un reso quasi totale di €720 registrato nel mese successivo. La crescita del fatturato lordo è reale; non equivale automaticamente a crescita del valore netto. La window function non “scopre la verità”, ma consente di tenere la riga-evento e aggiungerle la storia dello stesso cliente.

`PARTITION BY` definisce chi appartiene al confronto. Una media partizionata per `customer_id` confronta l’ordine con la storia dello stesso cliente; partizionata per `country`, con gli ordini dello stesso Paese. `ORDER BY` definisce invece che cosa significa “prima”. Se due eventi condividono `event_at` e non esiste un tie-break deterministico, anche una semplice `LAG(status)` può avere una sequenza ambigua. In sistemi event-driven servono quindi, quando disponibili, `event_sequence`, transaction id, ingestion id o timestamp con precisione sufficiente.

Lo stesso vale per `ROW_NUMBER`, `RANK` e `DENSE_RANK`: la differenza non è cosmetica. Con valori 100, 100, 90 producono rispettivamente `1,2,3`, `1,1,3` e `1,1,2`. Se dobbiamo assegnare esattamente tre slot, `ROW_NUMBER` richiede una policy esplicita sui pari merito; se vogliamo rappresentare performance equivalenti, `RANK` o `DENSE_RANK` possono essere semanticamente più adatti.

### Prima il grain, poi il ranking

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

`product_revenue` cambia il grain a una riga per categoria-prodotto. `ROW_NUMBER` mantiene quel grain e aggiunge una posizione relativa. Leggere una query in questo modo — **dove cambia il grain e dove viene soltanto aggiunto contesto** — è più utile che memorizzare una lista di funzioni.

### Frame e frontiera informativa

Una running sum come:

```sql
SUM(net_revenue) OVER (
    PARTITION BY customer_id
    ORDER BY order_date, order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS revenue_to_date
```

rappresenta il revenue noto fino a quel punto della sequenza. È diversa dal lifetime revenue finale copiato retroattivamente su tutti gli eventi: la seconda versione può introdurre informazione futura nelle feature predittive del Capitolo 10.

Anche il frame è parte della metrica. Una media mobile con `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` usa sette righe, non necessariamente sette giorni di calendario. Se mancano due domeniche a basso volume, come nel caso simulato GridPay, una moving average a sette righe può salire semplicemente perché il calendario è incompleto. Prima della window serve quindi una calendar spine che distingua zero, dato mancante, giorno non eleggibile e pipeline non aggiornata.

### Window contract

| Campo | Domanda |
|---|---|
| grain input/output | resta una riga per che cosa? |
| partition | qual è il gruppo di confronto? |
| order | qual è la sequenza e come gestiamo i pari timestamp? |
| frame | quali righe entrano nel calcolo? |
| time completeness | le unità temporali mancanti sono rappresentate? |
| as-of safety | usiamo solo informazione disponibile fino a quel momento? |

> **Una window function aggiunge contesto senza cancellare l’identità analitica della riga. Proprio per questo partition, order e frame sono parte della definizione, non dettagli di sintassi.**
