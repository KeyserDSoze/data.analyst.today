## 11.7 Caso end-to-end intermedio: la query corretta che raccontava la storia sbagliata

### VelaHome: dal KPI al fenomeno che il KPI rappresenta

VelaHome è un retailer omnicanale di arredamento con negozi fisici e un e-commerce in sei Paesi europei. A metà trimestre il COO vede un late delivery rate del **12,6%**, contro **8,9%** nel trimestre precedente: +3,7 punti percentuali. Operations propone di spostare volumi verso un nuovo corriere, con un costo incrementale stimato di **€1,2M annui**.

La query del dashboard sembra innocua:

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

È leggibile, compila e riproduce il numero. L’analista non parte però dal corriere: ricostruisce l’**Analytical Data Contract** del KPI.

Il primo problema emerge dal grain. `orders` contiene una riga per ordine, ma un ordine può essere diviso in più spedizioni provenienti da magazzini diversi. Esistono almeno tre metriche legittime: **late order completion rate**, che pesa ogni ordine; **late shipment rate**, che pesa ogni spedizione; **late unit rate**, che pesa le unità. Chiamarle tutte `late_delivery_rate` nasconde una scelta di rappresentazione.

Poi emerge il tempo. La query raggruppa per `order_date`: un ordine creato il 29 giugno e consegnato il 5 luglio appartiene a giugno. Questo è corretto se stiamo seguendo coorti di ordini creati; non lo è se il dashboard vuole descrivere le consegne avvenute nel mese. Prima di una migrazione recente, inoltre, il dashboard usava `delivered_at`. Una parte del salto è quindi **definition drift**: lo stesso nome KPI ha cambiato semantica temporale.

L’indagine prosegue sulla metrica. Durante il trimestre VelaHome ha reso più aggressiva la promessa mostrata al checkout. Il promised lead time medio passa da **5,2** a **3,9 giorni**, mentre il transit time effettivo passa soltanto da **4,4** a **4,5 giorni**. Le domande “la logistica è più lenta?” e “rispettiamo meno spesso la promessa?” non sono più equivalenti. Il late rate descrive soprattutto la seconda.

Infine cambia la composizione. La crescita del trimestre è concentrata in prodotti voluminosi e destinazioni rurali:

| Segmento | Late rate Q1 | Late rate Q2 |
|---|---:|---:|
| piccoli pacchi urbani | 6,2% | 6,4% |
| piccoli pacchi rurali | 9,1% | 9,3% |
| bulky urbani | 13,8% | 14,2% |
| bulky rurali | 19,5% | 20,1% |

All’interno dei segmenti il deterioramento è contenuto. L’aggregato peggiora molto anche perché aumenta il peso delle spedizioni più difficili. Questo non rende il problema irrilevante: indica dove cercare la causa e dove localizzare l’intervento.

### Ricostruire il modello prima di ricostruire il KPI

Il team crea una fact a grain spedizione:

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

E separa le metriche: `on_time_shipment_rate`, `on_time_order_completion_rate`, `avg_transit_days`, `promise_gap_days` e `shipping_cost_per_unit`.

Il contratto diventa:

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

La conclusione cambia senza negare il dato iniziale. Il rispetto della promessa è peggiorato in modo rilevante, ma il transit time è quasi stabile; gran parte del delta aggregato nasce da una promessa più aggressiva e da un mix più difficile, con deterioramento operativo più marcato nel segmento bulky-rurale.

La decisione non è quindi “cambiare corriere per tutta la rete”. Diventa: usare una promessa dinamica per area e tipologia prodotto, testare il nuovo carrier sul bulky-rurale, monitorare separatamente transit time e promise adherence e certificare le definizioni per impedire nuovi definition drift.

La query iniziale non aveva un bug evidente. Il failure mode era una catena:

```text
grain ambiguo
→ tempo non coerente con la domanda
→ promessa commerciale cambiata
→ mix diverso
→ una metrica usata per due decisioni
```

> **Una query può calcolare perfettamente una metrica definita male. La correttezza SQL viene dopo la correttezza della rappresentazione che abbiamo deciso di materializzare.**
