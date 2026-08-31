## 11.12 Data quality tests: trasformare le assunzioni in controlli eseguibili

Ogni modello analitico contiene assunzioni.

Spesso sono implicite:

- `order_id` dovrebbe essere unico;
- `customer_id` non dovrebbe essere nullo;
- `status` dovrebbe appartenere a un insieme noto;
- ogni `product_id` dovrebbe esistere nella dimensione prodotto;
- la revenue non dovrebbe duplicarsi da un giorno all'altro;
- una percentuale dovrebbe stare tra 0 e 1.

Finché queste assunzioni restano nella testa dell'analista, il sistema è fragile.

Un modello più maturo le trasforma in **test automatici**.

### Quattro famiglie di test fondamentali

#### Unicità

Se il grain è una riga per ordine:

```sql
SELECT order_id
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
```

La query dovrebbe restituire zero righe.

#### Not null

```sql
SELECT COUNT(*)
FROM fact_orders
WHERE order_id IS NULL;
```

#### Accepted values

```sql
SELECT DISTINCT status
FROM fact_orders
WHERE status NOT IN ('created', 'paid', 'shipped', 'delivered', 'cancelled');
```

#### Referential integrity

```sql
SELECT COUNT(*)
FROM fact_orders f
LEFT JOIN dim_customer d
  ON f.customer_sk = d.customer_sk
WHERE d.customer_sk IS NULL;
```

### Ma la qualità non è soltanto vincoli riga-per-riga

Molti problemi emergono solo a livello aggregato.

Esempi:

- ordini giornalieri -63% rispetto alla media recente;
- tasso di `NULL` su `country` da 0,4% a 18%;
- una sorgente smette improvvisamente di inviare dati;
- revenue raddoppia esattamente alle 02:00;
- un evento che arrivava entro 20 minuti comincia ad arrivare dopo 7 ore.

Servono quindi anche test su:

- volume;
- freshness;
- distribuzioni;
- range;
- riconciliazione con fonti operative;
- continuità temporale.

### Caso realistico: il conversion rate record

**BlueBasket**, e-commerce europeo, vede il conversion rate passare dal 3,7% al 5,1% in un giorno.

Il dashboard viene condiviso con entusiasmo.

Gli ordini sono stabili. Sono le sessioni a essere diminuite del 27%.

Un nuovo consent banner ha impedito il tracking di parte delle visite anonime, ma non degli acquisti finali.

Il KPI è quindi migliorato perché il denominatore è diventato incompleto.

Un test di volume avrebbe potuto segnalare:

```text
sessions_today < 0.85 * median_sessions_same_weekday_last_8_weeks
```

prima che il risultato arrivasse al management.

### Data quality e semantica

Un test può passare e il dato può comunque essere sbagliato.

Supponiamo che `net_revenue` sia sempre non-null, positivo e numericamente plausibile.

Se da ieri include l'IVA mentre prima la escludeva, i test tecnici di base possono non accorgersene.

Per questo servono anche **semantic checks** e riconciliazioni:

```text
warehouse net revenue
vs
finance ledger
vs
payment processor
```

Non devono necessariamente coincidere al centesimo, ma le differenze devono essere spiegabili.

### Severity: non tutti i test devono bloccare tutto

Una strategia utile distingue:

- **error**: il modello non deve essere pubblicato;
- **warning**: il modello viene pubblicato ma va investigato;
- **monitoring**: si registra una deviazione senza bloccare.

Esempio:

- duplicato su `order_id` → error;
- freshness 20 minuti oltre SLA → warning;
- mix geografico insolito → monitoring.

### Il principio importante

Un test di qualità non serve a dimostrare che i dati sono perfetti.

Serve a rendere visibili le condizioni sotto cui siamo disposti a fidarci del modello.

**Ogni assunzione importante che può essere verificata automaticamente dovrebbe, prima o poi, diventare un test.**
