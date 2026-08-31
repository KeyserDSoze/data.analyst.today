## 11.2 Aggregare è scegliere: somme, medie e denominatori

`GROUP BY` sembra innocuo. In realtà è uno dei punti in cui l'analyst prende più decisioni implicite.

Ogni aggregazione risponde a tre domande:

1. cosa sto contando o sommando?
2. su quale popolazione?
3. con quale denominatore?

### Caso simulato — NovaCare e il tempo medio di risposta

NovaCare gestisce un customer service multicanale. Il management riceve un report:

- tempo medio di prima risposta: 4,8 ore;
- mese precedente: 5,6 ore;
- miglioramento: 14%.

Il numero sembra positivo.

La query è:

```sql
SELECT
    AVG(first_response_minutes) / 60.0 AS avg_hours
FROM tickets
WHERE created_at >= '2026-07-01'
  AND created_at < '2026-08-01';
```

Ma nel mese corrente è stata introdotta una nuova regola: i ticket ancora aperti senza risposta hanno `first_response_minutes = NULL`.

`AVG` ignora i `NULL`.

Quindi i casi peggiori spariscono dal denominatore.

Il team non ha migliorato davvero di 14%. Ha cambiato implicitamente la popolazione su cui calcola la media.

### Conteggi che sembrano uguali ma non lo sono

```sql
COUNT(*)
```

conta le righe.

```sql
COUNT(customer_id)
```

conta le righe in cui `customer_id` non è NULL.

```sql
COUNT(DISTINCT customer_id)
```

conta clienti distinti non nulli.

Queste tre espressioni possono produrre numeri molto diversi.

### Media delle medie: un errore classico

Immaginiamo due negozi:

| Negozio | Ordini | AOV |
|---|---:|---:|
| A | 100 | €40 |
| B | 10.000 | €52 |

La media semplice tra 40 e 52 è 46 euro.

Ma l'AOV complessivo corretto è:

```text
(100 × 40 + 10.000 × 52) / 10.100 ≈ 51,88 euro
```

Una media di metriche aggregate spesso introduce un peso implicito sbagliato.

### Ratio of sums vs average of ratios

Consideriamo il return rate.

Metodo A:

```sql
SUM(returned_units) * 1.0 / SUM(sold_units)
```

Metodo B:

```sql
AVG(returned_units * 1.0 / sold_units)
```

Non sono equivalenti.

Il secondo assegna lo stesso peso a ogni riga o gruppo, indipendentemente dal volume.

### Caso simulato — PeakSports e il venditore “peggiore”

Un marketplace sportivo misura il tasso di reso per seller.

Seller Alpha:

- 8 resi;
- 100 ordini;
- return rate 8%.

Seller Beta:

- 240 resi;
- 6.000 ordini;
- return rate 4%.

Se osserviamo solo i resi assoluti, Beta sembra il problema principale.

Se osserviamo il tasso, Alpha è peggiore.

Ma se Alpha vende quasi esclusivamente scarponi da sci, categoria con baseline di reso al 12%, il suo 8% potrebbe essere eccellente.

L'aggregazione corretta dipende dal confronto corretto.

### Metriche additive, semi-additive e non additive

Una distinzione utile:

- **additive**: revenue, units, costi; si possono sommare su molte dimensioni;
- **semi-additive**: saldo conto, inventory level; si possono sommare tra clienti o prodotti, ma non nel tempo senza attenzione;
- **non additive**: percentuali, medie, ratio; spesso devono essere ricalcolate dai componenti.

Un saldo giornaliero di magazzino di 10, 12 e 9 unità non significa che abbiamo avuto 31 unità di stock.

### Pattern robusto: conservare numeratore e denominatore

Invece di materializzare solo:

```text
conversion_rate = 3,7%
```

è spesso meglio conservare:

- `converted_sessions`;
- `eligible_sessions`.

La ratio può essere ricalcolata in modo coerente a diversi livelli di aggregazione.

> **Le percentuali sono spesso il risultato finale di un calcolo. Numeratore e denominatore sono invece dati analiticamente riusabili.**
