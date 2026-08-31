## 11.7 Caso studio: la query corretta che raccontava la storia sbagliata

### Il contesto

**VelaHome** è un retailer omnicanale di arredamento con negozi fisici e un e-commerce in sei Paesi europei.

A metà trimestre il COO vede un dato preoccupante nel dashboard operativo:

- ordini consegnati in ritardo: 12,6%;
- trimestre precedente: 8,9%;
- peggioramento: +3,7 punti percentuali.

La conclusione immediata è che la rete logistica stia deteriorando.

Il team Operations propone di spostare una parte dei volumi verso un nuovo corriere, con un costo incrementale stimato di 1,2 milioni di euro annui.

Prima di prendere la decisione viene chiesta una verifica analitica.

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
WHERE order_date >= '2026-01-01'
GROUP BY 1
ORDER BY 1;
```

La query è semplice, leggibile e sintatticamente corretta.

Il primo controllo conferma i numeri del dashboard.

### Prima domanda: qual è il grain?

`orders` è una riga per ordine.

Ma un ordine può essere diviso in più spedizioni provenienti da magazzini diversi.

Il business definisce “ordine consegnato” come completato quando arriva l'ultima spedizione.

Il cliente, però, percepisce il ritardo a livello di spedizione e articolo.

Quindi il KPI “late delivery rate” può essere costruito almeno in tre modi:

1. percentuale di ordini completamente consegnati oltre la promessa finale;
2. percentuale di spedizioni consegnate in ritardo;
3. percentuale di unità consegnate in ritardo.

Sono tre metriche diverse.

### Seconda domanda: quale data determina la coorte?

La query raggruppa per `order_date`.

Un ordine del 29 giugno consegnato il 5 luglio viene attribuito a giugno.

Questo può essere corretto per un'analisi per coorte di ordini, ma non per monitorare la performance operativa delle consegne avvenute a luglio.

Il team scopre che il dashboard precedente utilizzava `delivered_at`, mentre una recente migrazione lo ha sostituito con `order_date`.

Una parte del peggioramento è quindi un cambio di definizione temporale.

### Terza domanda: cosa significa `promised_delivery_at`?

Durante il trimestre l'e-commerce ha introdotto una nuova promessa di consegna più aggressiva per aumentare la conversione.

Prima:

- promessa media: 5,2 giorni.

Dopo:

- promessa media: 3,9 giorni.

Il tempo di consegna effettivo è passato da 4,4 a 4,5 giorni.

La logistica è peggiorata di circa 0,1 giorni.

Il late rate è aumentato molto di più perché il target promesso è diventato più stringente.

La domanda “la logistica sta peggiorando?” non è equivalente alla domanda “stiamo rispettando la promessa al cliente?”.

Entrambe sono utili, ma richiedono metriche diverse.

### Quarta domanda: sono cambiate le popolazioni?

La crescita del trimestre è concentrata in prodotti voluminosi e in aree rurali, dove le consegne sono strutturalmente più lente.

Segmentando:

| Segmento | Late rate Q1 | Late rate Q2 |
|---|---:|---:|
| piccoli pacchi urbani | 6,2% | 6,4% |
| piccoli pacchi rurali | 9,1% | 9,3% |
| bulky urbani | 13,8% | 14,2% |
| bulky rurali | 19,5% | 20,1% |

Dentro ogni segmento il deterioramento è contenuto.

Il mix Q2 contiene però molti più ordini bulky e rurali.

L'aggregato peggiora anche perché cambia la composizione.

### La ricostruzione

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

Poi aggiunge dimensioni per carrier, area, prodotto e data.

Le metriche vengono separate:

- `on_time_shipment_rate`;
- `on_time_order_completion_rate`;
- `avg_transit_days`;
- `promise_gap_days`;
- `shipping_cost_per_unit`.

### La conclusione

La prima lettura era:

> la rete logistica è peggiorata drasticamente; cambiamo corriere.

La conclusione analitica diventa:

> il rispetto della promessa al cliente è peggiorato in modo rilevante, ma solo una piccola parte è spiegata da un deterioramento della velocità logistica. Le cause principali sono una promessa commerciale più aggressiva e un mix di ordini più difficile. Il nuovo corriere potrebbe aumentare i costi senza risolvere il problema dominante.

La decisione cambia.

Invece di una migrazione generalizzata da 1,2 milioni di euro, VelaHome avvia tre interventi:

1. promessa dinamica per area e tipologia di prodotto;
2. test del nuovo carrier soltanto sul segmento bulky-rurale;
3. monitoraggio separato di transit time e promise adherence.

### Le lezioni del caso

La query iniziale non conteneva un bug evidente.

Il problema nasceva da una catena di decisioni semantiche:

- grain ordine invece di spedizione;
- data ordine invece di data consegna;
- KPI relativo a una promessa che era cambiata;
- mix di popolazione diverso;
- una sola metrica usata per rispondere a due domande diverse.

> **Il SQL affidabile non comincia da `SELECT`. Comincia dalla definizione del fenomeno che vogliamo misurare.**
