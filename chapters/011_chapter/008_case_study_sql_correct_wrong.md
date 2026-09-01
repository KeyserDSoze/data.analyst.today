## 11.7 Caso end-to-end intermedio: la query corretta che raccontava la storia sbagliata

### Caso simulato/composito — VelaHome

**VelaHome** è un retailer omnicanale di arredamento con negozi fisici e un e-commerce in sei Paesi europei.

A metà trimestre il COO vede nel dashboard operativo:

- late delivery rate: 12,6%;
- trimestre precedente: 8,9%;
- peggioramento: +3,7 punti percentuali.

La lettura immediata è:

> la rete logistica sta peggiorando rapidamente.

Operations propone di spostare volumi verso un nuovo corriere, con un costo incrementale stimato di €1,2M annui.

Prima della decisione, l’analista non parte dal corriere. Ricostruisce l’**Analytical Data Contract** del KPI.

### La query originale

```sql
SELECT
    DATE_TRUNC('month', order_date) AS month,
    AVG(
        CASE
            WHEN delivered_at > promised_delivery_at THEN 1.0
            ELSE 0.0
        END
    ) AS late_delivery_rate
FROM orders
WHERE order_date >= DATE '2026-01-01'
GROUP BY 1
ORDER BY 1;
```

La query è leggibile, sintatticamente corretta e riproduce il dashboard.

Questo non basta.

### Campo 1 — Business entity e grain

`orders` contiene una riga per ordine.

Ma un ordine può essere diviso in più spedizioni provenienti da magazzini diversi.

Esistono almeno tre metriche legittime:

1. **late order completion rate** — quota di ordini completamente consegnati dopo la promessa finale;
2. **late shipment rate** — quota di spedizioni arrivate in ritardo;
3. **late unit rate** — quota di unità arrivate in ritardo.

Sono metriche diverse perché assegnano peso a entità diverse.

Il KPI esistente era chiamato genericamente `late_delivery_rate`, quindi la definizione non rendeva visibile il grain.

### Campo 2 — Time semantics

La query raggruppa per `order_date`.

Un ordine creato il 29 giugno e consegnato il 5 luglio viene attribuito a giugno.

Questo è corretto per una **coorte di ordini creati**, ma non per una dashboard che vuole descrivere **le consegne avvenute nel mese**.

L’analista scopre inoltre che, prima di una migrazione recente, il dashboard usava `delivered_at`.

Una parte del salto è quindi un **definition drift**: lo stesso nome KPI ha cambiato semantica temporale.

### Campo 3 — Metric semantics

Durante il trimestre VelaHome ha reso più aggressiva la promessa di consegna mostrata nel checkout.

Prima:

- promised lead time medio: 5,2 giorni.

Dopo:

- promised lead time medio: 3,9 giorni.

Il transit time effettivo passa soltanto da 4,4 a 4,5 giorni.

Quindi due domande che sembravano equivalenti si separano:

> **la logistica è diventata più lenta?**

vs

> **stiamo rispettando meno spesso la promessa fatta al cliente?**

Il late rate risponde soprattutto alla seconda.

### Campo 4 — Population semantics e mix

La crescita del trimestre è concentrata in prodotti voluminosi e destinazioni rurali.

| Segmento | Late rate Q1 | Late rate Q2 |
|---|---:|---:|
| piccoli pacchi urbani | 6,2% | 6,4% |
| piccoli pacchi rurali | 9,1% | 9,3% |
| bulky urbani | 13,8% | 14,2% |
| bulky rurali | 19,5% | 20,1% |

All’interno dei segmenti il deterioramento è contenuto. L’aggregato peggiora molto anche perché cambia il mix.

Questa non è una prova che il problema sia irrilevante. Significa che l’intervento deve essere localizzato sulla parte del processo che genera il delta.

### La nuova fact

Il team costruisce una fact a grain spedizione:

```text
fact_shipments
- shipment_id
- order_id
- carrier_id
- warehouse_id
- destination_zone_id
- shipped_at
- promised_delivery_at
- delivered_at
- shipped_units
- shipping_cost
```

Le metriche vengono separate:

- `on_time_shipment_rate`;
- `on_time_order_completion_rate`;
- `avg_transit_days`;
- `promise_gap_days`;
- `shipping_cost_per_unit`.

### Il contratto ricostruito

| Campo | Definizione |
|---|---|
| business entity | spedizione |
| grain | una riga per `shipment_id` |
| key | `shipment_id` unico |
| population | spedizioni customer-facing non cancellate |
| operational time | `delivered_at` |
| cohort time | `order_date` quando serve analisi per coorte |
| promise metric | `delivered_at <= promised_delivery_at` |
| transit metric | `delivered_at - shipped_at` |
| invariants | una spedizione non può avere più di una consegna finale valida |
| reconciliation | spedizioni e unità riconciliate con OMS/WMS |

### La conclusione cambia

Prima:

> la rete logistica è peggiorata drasticamente; cambiamo corriere.

Dopo:

> il rispetto della promessa al cliente è peggiorato in modo rilevante, ma il transit time è quasi stabile. Il delta aggregato è spiegato soprattutto da una promessa più aggressiva e da un mix più difficile, con deterioramento operativo più marcato nel segmento bulky-rurale.

La decisione diventa:

1. promessa dinamica per area e tipologia prodotto;
2. test del nuovo carrier sul segmento bulky-rurale;
3. monitoraggio separato di transit time e promise adherence;
4. definizione certificata dei KPI per evitare nuovi definition drift.

### La lezione

La query iniziale non aveva un bug evidente.

Il problema nasceva da una catena semantica:

```text
grain ambiguo
→ data non coerente con la domanda
→ target commerciale cambiato
→ mix di popolazione diverso
→ una metrica usata per due decisioni
```

> **Una query può calcolare perfettamente una metrica definita male. Per questo la correttezza analitica deve essere verificata prima e oltre la correttezza SQL.**
