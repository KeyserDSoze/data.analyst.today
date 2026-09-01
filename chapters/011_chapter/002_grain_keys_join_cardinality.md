## 11.1 Grain, chiavi e cardinalità: il contratto invisibile di ogni join

Il **grain** descrive ciò che una singola riga rappresenta.

È una definizione semplice, ma è uno dei punti più importanti di tutto il lavoro analitico perché stabilisce quali operazioni hanno senso dopo.

Una riga può rappresentare:

- un ordine;
- una linea d’ordine;
- un pagamento;
- una sessione;
- un cliente-giorno;
- uno stock prodotto-magazzino a fine giornata;
- un evento di login;
- una relazione cliente-prodotto;
- una versione storica di un contratto.

Due tabelle possono condividere una colonna chiamata `customer_id` o `order_id` e tuttavia non essere direttamente combinabili senza cambiare il significato del dataset.

### Primo campo dell’Analytical Data Contract: una frase sul grain

Per ogni sorgente e per ogni trasformazione rilevante dovremmo poter scrivere una frase verificabile:

> `orders`: una riga per `order_id`.

> `order_lines`: una riga per coppia `order_id + line_number`.

> `customer_daily_snapshot`: una riga per `customer_id + snapshot_date`.

Se non riusciamo a completare questa frase, non siamo ancora pronti a fare il join.

### Caso simulato/composito — Helix Travel e la prenotazione media che non era media

Helix Travel vuole calcolare il valore medio delle prenotazioni per canale.

Il modello operativo contiene:

| Tabella | Grain |
|---|---|
| `bookings` | una riga per prenotazione |
| `booking_passengers` | una riga per passeggero nella prenotazione |
| `payment_transactions` | una riga per transazione di pagamento |

Un analyst scrive:

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

Il problema è che una prenotazione con quattro passeggeri e tre movimenti di pagamento può contribuire dodici volte alla media. Il peso implicito non è più “una prenotazione = un’osservazione”.

La metrica finale non è quindi l’average booking value. È una media ponderata accidentalmente dalla molteplicità dei record nelle tabelle figlie.

### Chiave tecnica, chiave business e chiave analitica

Una chiave non è soltanto una colonna su cui fare join.

È utile distinguere:

- **technical row key**: identifica una riga fisica;
- **business key**: identifica l’entità nel sistema operativo;
- **analytical identity**: identifica l’unità che vogliamo contare o seguire nell’analisi.

Esempio customer:

- `customer_row_id`: riga del CRM;
- `account_id`: contratto;
- `person_id`: individuo riconciliato tra sistemi;
- `household_id`: nucleo familiare;
- `workspace_id`: unità di utilizzo in un SaaS B2B.

La domanda “quanti clienti abbiamo?” non ha una risposta tecnica finché non decidiamo quale di queste identità rappresenta il concetto business richiesto.

### Cardinalità attesa prima del join

Prima di eseguire un join dovremmo dichiarare che relazione ci aspettiamo:

- **1:1** — ogni chiave compare al massimo una volta da entrambe le parti;
- **1:N** — una riga a sinistra può trovare più righe a destra;
- **N:1** — più righe a sinistra puntano a una dimensione unica;
- **N:M** — più righe da entrambe le parti possono corrispondere.

Il punto non è evitare ogni relazione 1:N o N:M. Il punto è sapere **quale grain produrrà il join** e quali misure verranno replicate.

### I test che devono precedere il join

Per una chiave candidata:

```sql
SELECT
    COUNT(*) AS rows,
    COUNT(DISTINCT booking_id) AS distinct_keys
FROM payment_transactions;
```

Poi identifichiamo le molteplicità:

```sql
SELECT
    booking_id,
    COUNT(*) AS n
FROM payment_transactions
GROUP BY booking_id
HAVING COUNT(*) > 1
ORDER BY n DESC;
```

Questi controlli rispondono a una domanda diversa da “la query gira?”:

> la cardinalità reale coincide con quella che il nostro modello mentale presume?

### Il pattern sicuro: normalizzare il grain prima del join

Se l’output deve restare a grain ordine, prima portiamo i pagamenti a grain ordine:

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

La CTE non “risolve i join” in generale. Rende esplicito che abbiamo trasformato una tabella a grain movimento in una tabella a grain ordine prima di combinarla con `orders`.

### Row-count delta non basta

Un controllo frequente è confrontare il numero di righe prima e dopo il join. È utile, ma non sufficiente.

Un join può mantenere lo stesso row count e comunque essere sbagliato se:

- la chiave collega l’entità sbagliata;
- una dimensione contiene record storici e scegliamo la versione corrente;
- alcune righe trovano più match e altre nessuno, compensandosi nel totale;
- un `INNER JOIN` elimina casi fuori dominio.

Per questo servono almeno tre famiglie di controllo:

1. **cardinality checks** — quante corrispondenze per chiave?
2. **coverage checks** — quali righe non trovano match?
3. **measure reconciliation** — somme/conti critici cambiano come previsto?

### Un join è anche una scelta di popolazione

Considera:

```sql
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
```

Se partiamo da tutti i clienti, dopo l’`INNER JOIN` restano soltanto quelli con almeno un ordine.

La query ha quindi modificato non solo il dataset, ma anche la **popolazione di riferimento**.

Se la domanda era “qual è il tasso di acquisto tra tutti i clienti eleggibili?”, quell’`INNER JOIN` può aver eliminato proprio il denominatore che ci serve.

### Il join gate dell’Analytical Data Contract

Per ogni join importante documentiamo:

| Campo | Esempio |
|---|---|
| grain sinistro | una riga per ordine |
| grain destro | una riga per pagamento |
| chiave | `order_id` |
| cardinalità attesa | 1:N |
| grain desiderato dopo join | una riga per ordine |
| strategia | aggregare pagamenti prima del join |
| unmatched consentiti | sì, ordini non ancora pagati |
| invariant | `COUNT(DISTINCT order_id)` non deve aumentare |
| reconciliation | total order value invariato |

Questa tabella è spesso più importante della sintassi finale.

> **Ogni join è una trasformazione del significato del dataset, non soltanto del numero di righe.**
