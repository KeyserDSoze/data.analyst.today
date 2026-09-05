## 11.18 Esercizi: SQL e data modeling come preservazione del significato

Gli esercizi restano volutamente strutturati: qui la forma operativa è parte dell’apprendimento. L’obiettivo non è soltanto scrivere query, ma dichiarare **quali proprietà devono restare vere** e trasformarle in un Analytical Data Contract verificabile.

### Esercizio 1 — Revenue duplicata

Una tabella `orders` contiene una riga per ordine. `payments` può contenere più transazioni per ordine. Dopo un join diretto, la revenue cresce del 12%.

Costruisci una diagnosi che includa:

1. grain delle due tabelle;
2. cardinalità attesa;
3. row multiplier osservato;
4. business key;
5. modello intermedio necessario;
6. invariant di riconciliazione prima/dopo il join.

Poi scrivi il blocco `keys/relationships` dell’Analytical Data Contract.

### Esercizio 2 — Il paese storico

Un cliente vive in Italia nel 2024 e in Francia nel 2025. La dimensione cliente contiene solo il paese corrente. Il management chiede:

> Quanto revenue abbiamo generato in Italia nel 2024?

Definisci due domande diverse: attribuzione secondo il paese storico e riclassificazione secondo il paese corrente. Per ciascuna specifica time semantics, dimension semantics, join e conseguenza sul reporting. Spiega perché non esiste una singola query “giusta” finché non sappiamo quale storia vogliamo raccontare.

### Esercizio 3 — Deduplicazione o distruzione di eventi?

```text
customer_id | event_id | status | updated_at | ingestion_at
C1          | E1       | trial  | 10:00      | 10:01
C1          | E1       | active | 12:00      | 12:01
C1          | E1       | active | 12:00      | 12:04
```

Definisci tre output possibili: stato corrente, storia delle versioni, event log deduplicato per evento/versione. Per ciascuno indica grain, key, winner/conservation rule, tie-break e invariant.

### Esercizio 4 — Conversion rate

La definizione richiesta è:

> quota di sessioni web eligible che generano almeno un ordine valido.

Prima di scrivere SQL completa:

```text
output grain:
eligible population:
numerator:
denominator:
session identity:
order validity:
timezone:
bot policy:
join behavior:
NULL policy:
```

Poi proponi una trasformazione a step e almeno cinque test automatici.

### Esercizio 5 — Costi cloud

Un analyst esegue ogni ora:

```sql
SELECT *
FROM fact_events
LIMIT 1000;
```

La tabella è enorme e non clusterizzata. Spiega perché `LIMIT 1000` può non ridurre il costo della scansione in BigQuery, come esploreresti i dati con meno lavoro, quali colonne e filtri servono davvero, quale guardrail sui byte imposteresti e quando materializzeresti un modello più piccolo.

### Esercizio 6 — Modello incrementale e late changes

Gli ordini vengono creati oggi, ma il 70% dei refund arriva entro 7 giorni, il 95% entro 30 giorni, alcuni chargeback dopo 90 giorni e alcuni delete amministrativi arrivano dal source system.

Progetta:

```text
change detection:
unique key:
lookback:
late-arrival policy:
delete policy:
backfill:
full refresh:
reconciliation:
```

Dichiara anche quale rischio rimane fuori dalla lookback scelta.

### Esercizio 7 — AI-generated SQL

Un assistente genera una query che calcola churn per piano tariffario. La query compila e restituisce numeri plausibili.

Costruisci prima il contract minimo: account vs subscription grain, definizione churn, eligibility, cancellazioni e riattivazioni, data di churn, piano corrente vs piano all’evento, censura, denominator e join semantics. Poi scrivi un prompt di review per un secondo agente AI che confronti query e contract senza modificare dati.

### Esercizio 8 — Many-to-many con due bridge

Un ordine può usare tre coupon e avere due campagne marketing associate. Un join diretto produce fino a sei combinazioni per ordine.

Devi supportare tre domande:

1. quali coupon compaiono negli ordini?
2. quanta revenue viene allocata alle campagne?
3. qual è la revenue totale senza duplicazioni?

Progetta fact principale, bridge coupon, bridge campaign, eventuali allocation weights e invarianti di conservazione. Spiega perché coupon e campagne potrebbero richiedere policy differenti.

### Esercizio 9 — Il dashboard che migliora troppo

Da un giorno all’altro:

- conversion rate: 4,1% → 5,3%;
- ordini: quasi invariati;
- sessioni: -23%;
- revenue: +1%.

Costruisci i controlli nell’ordine **population → instrumentation → grain → join → denominator → time → reconciliation** e assegna a ciascuno severity `BLOCK`, `WARN` o `MONITOR`.

### Esercizio 10 — Contribution margin per categoria

Devi costruire:

```text
contribution margin =
net revenue
- COGS
- payment fees
- fulfillment variable cost
- outbound shipping
```

Hai `order_lines` a line grain, più refund per line, più payment per order, più shipment per order, una bridge shipment-line, `dim_product` SCD Type 2 e più valute.

Completa un Analytical Data Contract includendo grain, allocation policies, point-in-time product category, FX semantics, refund lateness, incremental strategy, reconciliation e service envelope.

### Esercizio 11 — Il contract cambia

Finance decide che `net_revenue` deve escludere una nuova categoria di fee prima inclusa. Elenca quali campi del contract cambiano, quali consumer possono essere impattati, quali test devono evolvere, se il passato va ricalcolato e come distingueresti una modifica backward-compatible da una breaking semantic change.

### Esercizio 12 — Leadership review

Il COO vuole cambiare fornitore logistico perché `on_time_delivery_rate` è sceso di 4 punti. Hai 24 ore.

Non partire dalla query. Produci un contract preliminare con decisione, shipment vs order grain, promise/delivered date, split shipment, timezone, carrier eligibility, product/geography mix, cambi di promise policy, quality invariants, reconciliation con il sistema operativo e output finale. Indica esplicitamente quali campi non puoi completare senza Operations.

### Autovalutazione

Alla fine del capitolo dovresti riuscire a spiegare, senza rifugiarti nella sintassi, perché un join cambia il peso delle osservazioni, una ratio richiede un denominatore esplicito, una window function aggiunge contesto senza collassare il grain, una dimensione corrente può riscrivere il passato, `DISTINCT` non definisce una policy di dedup, una many-to-many può richiedere allocazione e un modello incrementale deve osservare modifiche tardive.

Dovresti anche saper collegare queste scelte a test, freshness, costo, lineage e AI-assisted SQL.

Il passaggio mentale del capitolo è:

```text
non:
"quale query devo scrivere?"

ma:
"quale rappresentazione del business devo costruire,
quali proprietà deve preservare
e come dimostro che le preserva?"
```

Quando il contract è chiaro, spesso la query finale diventa più semplice. Quando il contract è assente, anche SQL sofisticato può produrre una risposta molto convincente a una domanda mai davvero definita.

Il Capitolo 12 allargherà ora l’inquadratura. Una trasformazione semanticamente corretta non appare dal nulla: il dato deve nascere, essere catturato, trasportato, memorizzato e servito. Dopo aver definito **che cosa** il dataset deve significare, dovremo capire **quale percorso architetturale rende quella promessa disponibile con la freshness, il recovery e il costo necessari alla decisione**.
