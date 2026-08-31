## 11.1 Grain, chiavi e cardinalità: il contratto invisibile di ogni query

Il grain descrive cosa rappresenta una singola riga.

Può sembrare una definizione elementare, ma è uno dei concetti più importanti dell'intera disciplina analitica.

Una riga può rappresentare:

- un ordine;
- una linea d'ordine;
- un pagamento;
- una sessione;
- un cliente al giorno;
- un saldo a fine mese;
- un evento di login;
- una relazione cliente-prodotto;
- una modifica di stato.

Due tabelle possono condividere una chiave e tuttavia non essere direttamente compatibili per una somma.

### Caso simulato — Helix Travel e le prenotazioni duplicate

Helix Travel vuole calcolare il valore medio delle prenotazioni per canale.

Il modello operativo contiene:

| Tabella | Grain |
|---|---|
| `bookings` | una riga per prenotazione |
| `booking_passengers` | una riga per passeggero nella prenotazione |
| `payment_transactions` | una riga per transazione di pagamento |

Una prenotazione può avere quattro passeggeri e tre transazioni: autorizzazione, cattura e rimborso parziale.

Un analyst junior scrive:

```sql
SELECT
    b.channel,
    AVG(b.total_booking_value) AS avg_booking_value
FROM bookings b
JOIN booking_passengers bp
    ON b.booking_id = bp.booking_id
JOIN payment_transactions pt
    ON b.booking_id = pt.booking_id
GROUP BY b.channel;
```

La query produce numeri plausibili.

Sono però ponderati implicitamente dal numero di passeggeri e transazioni. Una prenotazione con più passeggeri e più movimenti contribuisce più volte alla media.

Il risultato non misura più la prenotazione media. Misura qualcosa che non ha una definizione business utile.

### Prima regola: dichiarare il grain a parole

Prima di ogni trasformazione importante, scrivere una frase:

> `bookings`: una riga per booking_id.

> `payment_transactions`: una riga per transaction_id, più transazioni per booking_id.

Questa abitudine rende visibili assunzioni che altrimenti rimangono dentro la query.

### Chiave primaria e chiave analitica

Una chiave tecnica non coincide sempre con l'identità business.

Esempio:

- `customer_row_id`: chiave tecnica di riga;
- `customer_id`: identificatore cliente nel CRM;
- `email_hash`: possibile identità cross-system;
- `household_id`: identità utile per alcune analisi;
- `account_id`: identità contrattuale B2B.

La domanda “quanti clienti abbiamo?” non può essere risolta finché non sappiamo quale concetto di cliente stiamo contando.

### Test operativo della cardinalità

Prima del join possiamo misurare:

```sql
SELECT
    COUNT(*) AS rows,
    COUNT(DISTINCT booking_id) AS unique_bookings
FROM payment_transactions;
```

Se `rows` è molto maggiore di `unique_bookings`, sappiamo che `booking_id` non è unico.

Poi possiamo cercare le molteplicità:

```sql
SELECT
    booking_id,
    COUNT(*) AS transaction_count
FROM payment_transactions
GROUP BY booking_id
HAVING COUNT(*) > 1
ORDER BY transaction_count DESC;
```

Questi controlli sono spesso più importanti della query finale.

### Join uno-a-molti non significa automaticamente errore

Un join uno-a-molti è perfettamente corretto se il grain desiderato diventa il lato “molti”.

Se vogliamo una riga per linea d'ordine, unire `orders` a `order_lines` è naturale.

Diventa pericoloso quando continuiamo a trattare una misura dell'ordine come se esistesse ancora una sola volta.

### Il pattern sicuro: aggregare prima del join

Se vogliamo aggiungere l'ammontare incassato a una tabella a grain ordine:

```sql
WITH payments_by_order AS (
    SELECT
        order_id,
        SUM(CASE WHEN status = 'captured' THEN amount ELSE 0 END) AS captured_amount
    FROM payments
    GROUP BY order_id
)
SELECT
    o.order_id,
    o.order_total,
    p.captured_amount
FROM orders o
LEFT JOIN payments_by_order p
    ON o.order_id = p.order_id;
```

La CTE non è importante perché “rende il codice bello”. È importante perché rende esplicito il cambio di grain.

### Metodo operativo

Per ogni join rilevante:

1. dichiarare grain di sinistra e destra;
2. verificare l'unicità delle chiavi;
3. prevedere la cardinalità attesa;
4. confrontare il numero di righe prima e dopo;
5. controllare metriche sensibili prima e dopo;
6. investigare le chiavi che generano molteplicità inattese.

> **Ogni join è una trasformazione del significato del dataset, non soltanto una trasformazione del numero di righe.**
