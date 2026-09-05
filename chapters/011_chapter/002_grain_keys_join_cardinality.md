## 11.1 Grain, chiavi e cardinalità: il contratto invisibile di ogni join

Il **grain** dice che cosa rappresenta una singola riga. Sembra una definizione elementare, ma governa quasi tutto ciò che viene dopo: quali chiavi possono essere uniche, quale join è legittimo, quali misure possono essere sommate e quale peso implicito riceve ogni entità.

Scrivere “una riga per ordine”, “una riga per `order_id + line_number`” o “una riga per `customer_id + snapshot_date`” non è documentazione accessoria. È la prima specifica eseguibile del modello. Se non riusciamo a pronunciare il grain di una sorgente e dell’output desiderato, non siamo ancora pronti a combinarli.

### Helix Travel: la prenotazione media ponderata per errore

Helix Travel vuole il valore medio delle prenotazioni per canale. Le sorgenti hanno grain differenti:

| Tabella | Grain |
|---|---|
| `bookings` | una riga per prenotazione |
| `booking_passengers` | una riga per passeggero nella prenotazione |
| `payment_transactions` | una riga per transazione di pagamento |

La query seguente è perfettamente valida:

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

Ma una prenotazione con quattro passeggeri e tre movimenti di pagamento può contribuire dodici volte. La metrica non è più “una prenotazione = un’osservazione”: è una media accidentalmente ponderata dalla molteplicità delle tabelle figlie.

Il problema nasce perché la chiave del join e l’identità analitica non sono la stessa cosa. Una **technical row key** identifica una riga fisica; una **business key** identifica un’entità nel sistema operativo; l’**analytical identity** stabilisce che cosa vogliamo contare o seguire nella domanda. Per un cliente potremmo avere `customer_row_id`, `account_id`, `person_id`, `household_id` o `workspace_id`. Chiedere “quanti clienti?” non diventa una domanda tecnica finché non scegliamo quale identità rappresenta davvero il concetto business.

### La cardinalità è una previsione sul risultato del join

Prima di eseguire un join dovremmo dichiarare quale relazione ci aspettiamo: 1:1, 1:N, N:1 o N:M. Nessuna di queste è automaticamente sbagliata. La domanda è che cosa accadrà al grain e alle misure.

Possiamo verificare l’ipotesi prima del join:

```sql
SELECT
    COUNT(*) AS rows,
    COUNT(DISTINCT booking_id) AS distinct_keys
FROM payment_transactions;
```

E localizzare le molteplicità:

```sql
SELECT
    booking_id,
    COUNT(*) AS n
FROM payment_transactions
GROUP BY booking_id
HAVING COUNT(*) > 1
ORDER BY n DESC;
```

Questi controlli non chiedono se la query “gira”, ma se la cardinalità reale coincide con quella presunta dal nostro modello mentale.

Se l’output deve restare a grain ordine, una strategia coerente è normalizzare prima la sorgente figlia allo stesso grain:

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

La CTE non rende il join “sicuro” per magia. Rende visibile la decisione: una tabella a grain movimento viene portata a grain ordine prima di essere combinata con `orders`.

### Un join cambia anche la popolazione

Consideriamo:

```sql
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
```

Se partiamo da tutti i clienti, dopo il join restano soltanto quelli con almeno un ordine. Il join ha quindi cambiato il denominatore. Se la domanda era il tasso di acquisto tra tutti gli eleggibili, abbiamo eliminato proprio gli zeri che servono alla metrica.

Per questo il semplice row-count delta non basta. Un join può mantenere il numero totale di righe e restare sbagliato: alcuni record possono moltiplicarsi mentre altri scompaiono; una dimensione storica può restituire la versione sbagliata; una chiave può collegare entità semanticamente diverse.

Il gate utile combina almeno tre controlli: **cardinality**, per sapere quanti match produce ogni chiave; **coverage**, per sapere quali entità non trovano corrispondenza; **reconciliation**, per verificare che misure e conteggi critici cambino solo nel modo previsto.

### Join gate nell’Analytical Data Contract

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

> **Ogni join è una trasformazione del significato del dataset. La cardinalità dice quante righe produrrà; il grain dice che cosa quelle righe significheranno.**
