## 11.18 Esercizi: SQL e data modeling come preservazione del significato

Gli esercizi di questo capitolo non chiedono soltanto di scrivere query.

Chiedono di decidere **quali proprietà la query deve preservare** e di trasformarle in un Analytical Data Contract verificabile.

### Esercizio 1 — Revenue duplicata

Una tabella `orders` contiene una riga per ordine. `payments` può contenere più transazioni per ordine.

Dopo un join diretto, la revenue cresce del 12%.

Costruisci una diagnosi che includa:

1. grain delle due tabelle;
2. cardinalità attesa;
3. row multiplier osservato;
4. business key;
5. modello intermedio necessario;
6. invariant di riconciliazione prima/dopo il join.

Poi scrivi il blocco `keys/relationships` dell'Analytical Data Contract.

### Esercizio 2 — Il paese storico

Un cliente vive in Italia nel 2024 e in Francia nel 2025.

La dimensione cliente contiene solo il paese corrente.

Il management chiede:

> Quanto revenue abbiamo generato in Italia nel 2024?

Definisci due possibili domande business:

- attribuzione secondo il paese storico;
- riclassificazione secondo il paese corrente.

Per ciascuna indica:

- time semantics;
- dimension semantics;
- join corretto;
- conseguenza sul reporting.

Spiega perché non esiste una singola query “giusta” finché la domanda non specifica quale storia vuole raccontare.

### Esercizio 3 — Deduplicazione o distruzione di eventi?

La tabella raw contiene:

```text
customer_id | event_id | status | updated_at | ingestion_at
C1          | E1       | trial  | 10:00      | 10:01
C1          | E1       | active | 12:00      | 12:01
C1          | E1       | active | 12:00      | 12:04
```

Definisci almeno tre output possibili:

- stato corrente cliente;
- storia delle versioni;
- event log deduplicato per evento/versione.

Per ciascuno specifica:

- grain;
- business/event key;
- winner rule o policy di conservazione;
- tie-break;
- invariant finale.

### Esercizio 4 — Conversion rate

Definizione richiesta:

> quota di sessioni web eligible che generano almeno un ordine valido.

Prima di scrivere SQL, completa:

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

La tabella è enorme e non clusterizzata.

Rispondi:

1. perché `LIMIT 1000` può non ridurre il costo della scansione in BigQuery?
2. come esploreresti i dati senza una scansione completa?
3. quali colonne servono davvero?
4. quale filtro temporale è coerente con il task?
5. quale `maximum bytes billed` o guardrail equivalente imposteresti?
6. quando materializzeresti un modello più piccolo?

### Esercizio 6 — Modello incrementale e late changes

Gli ordini vengono creati oggi, ma:

- 70% dei refund entro 7 giorni;
- 95% entro 30 giorni;
- alcuni chargeback dopo 90 giorni;
- alcuni delete amministrativi arrivano dal source system.

Progetta `update semantics` dichiarando:

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

Spiega quale rischio rimane dopo la lookback scelta.

### Esercizio 7 — AI-generated SQL

Un assistente genera una query che calcola churn per piano tariffario.

La query compila e restituisce numeri plausibili.

Costruisci prima il contract minimo:

- account vs subscription grain;
- definizione churn;
- eligibility;
- cancellazioni e riattivazioni;
- data di churn;
- piano corrente vs piano al momento dell'evento;
- clienti censurati;
- denominator;
- join semantics.

Poi scrivi un prompt di review per un secondo agente AI che debba confrontare query e contract senza modificare dati.

### Esercizio 8 — Many-to-many con due bridge

Un ordine può usare tre coupon e avere due campagne marketing associate.

Un join diretto produce fino a sei combinazioni per ordine.

Devi supportare tre domande:

1. quali coupon compaiono negli ordini?
2. quanta revenue viene allocata alle campagne?
3. qual è la revenue totale senza duplicazioni?

Progetta:

- fact principale;
- bridge coupon;
- bridge campaign;
- eventuali allocation weights;
- invarianti di conservazione dei totali.

Spiega perché coupon e campagne potrebbero richiedere policy diverse.

### Esercizio 9 — Il dashboard che migliora troppo

Da un giorno all'altro:

- conversion rate: 4,1% → 5,3%;
- ordini: quasi invariati;
- sessioni: -23%;
- revenue: +1%.

Costruisci una sequenza di controlli organizzata per:

**population → instrumentation → grain → join → denominator → time → reconciliation**.

Poi assegna a ogni controllo una severity `BLOCK`, `WARN` o `MONITOR`.

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

Hai:

- `order_lines`: line grain;
- `refunds`: più righe per line;
- `payments`: più righe per order;
- `shipments`: più righe per order;
- `shipment_lines`: bridge shipment-line;
- `dim_product`: SCD Type 2;
- più valute.

Completa un Analytical Data Contract includendo almeno:

- grain;
- allocation policies;
- point-in-time product category;
- FX semantics;
- refund lateness;
- incremental strategy;
- reconciliation tests;
- service envelope.

### Esercizio 11 — Il contract cambia

Il Finance team decide che `net_revenue` da domani deve escludere una nuova categoria di fee che prima era inclusa.

Elenca:

1. quali campi del contract cambiano;
2. quali modelli downstream possono essere impattati;
3. quali test devono cambiare;
4. se il passato va ricalcolato;
5. come distingueresti una modifica backward-compatible da una breaking semantic change.

Questo tema tornerà nei Capitoli 12 e 18.

### Esercizio 12 — Leadership review

Il COO vuole cambiare fornitore logistico perché `on_time_delivery_rate` è sceso di 4 punti.

Hai 24 ore.

Non scrivere subito la query.

Produci un contract preliminare con:

- decisione;
- shipment vs order grain;
- promise date;
- delivered date;
- split shipment;
- timezone;
- carrier eligibility;
- product/geography mix;
- promise-policy changes;
- quality invariants;
- reconciliation con il sistema operativo;
- output finale richiesto.

Indica quali campi non puoi ancora compilare senza parlare con Operations.

### Autovalutazione

Alla fine del capitolo dovresti saper spiegare perché:

- un join cambia il significato, non solo le righe;
- una percentuale richiede popolazione e denominatore;
- una window function mantiene il grain ma aggiunge contesto;
- una CTE può rendere auditabile una trasformazione;
- uno star schema separa fatti e contesto;
- una dimensione corrente può riscrivere il passato;
- `DISTINCT` non definisce la deduplicazione;
- una many-to-many può richiedere allocazione;
- un modello incrementale deve osservare modifiche tardive;
- costo e freshness sono proprietà del prodotto analitico;
- AI-generated SQL deve implementare un contract, non inventarlo.

Il cuore del capitolo è questa trasformazione mentale:

```text
non:
"quale query devo scrivere?"

ma:
"quale rappresentazione del business devo costruire,
quali proprietà deve preservare
e come dimostro che le preserva?"
```

Quando il contract è chiaro, spesso la query finale diventa più semplice.

Quando il contract è assente, anche SQL sofisticato può produrre una risposta estremamente convincente a una domanda che nessuno aveva davvero definito.
