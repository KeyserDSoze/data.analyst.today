## 11.17 Analytical Data Contract: prima di fidarsi di una trasformazione

Una query può essere elegante, veloce e sintatticamente perfetta. Il deliverable di questo capitolo non è quindi una checklist di sintassi, ma un **Analytical Data Contract**: una specifica compatta che rende esplicite le proprietà che una trasformazione deve preservare.

Non è necessariamente un file YAML o un prodotto specifico. Può vivere in documentazione, codice, metadata o tooling dedicato.

La cosa importante è che le decisioni semantiche non restino nascoste dentro SQL.

### 1. Business meaning

```text
business question:
metric/use case:
decision supported:
owner:
```

Domande:

- quale decisione deve supportare il dataset?
- quale fenomeno business rappresenta?
- esiste una definizione certificata della metrica?

### 2. Grain e popolazione

```text
output grain:
source grains:
eligible population:
exclusions:
```

Controllare:

- cosa rappresenta una riga;
- se il grain cambia durante le trasformazioni;
- quali entità devono sopravvivere anche senza match;
- se filtri e `NULL` cambiano il denominatore.

### 3. Keys e relationship semantics

```text
business key:
record/event key:
expected uniqueness:
join cardinality:
many-to-many bridge:
allocation policy:
```

Controllare:

- unicità reale delle chiavi;
- one-to-one / one-to-many / many-to-many;
- row multiplier atteso;
- conservazione dei totali dopo allocazioni.

### 4. Time semantics

```text
business/event date:
reporting date:
timezone:
point-in-time attributes:
late-arrival policy:
```

Chiedere:

- quale data risponde alla domanda?
- quale timezone interpreta il business?
- gli attributi devono essere correnti o storici?
- come trattiamo backfill, rettifiche e lateness?

### 5. Identity e version semantics

```text
entity/event/version model:
version timestamp:
winner rule:
tie-break:
```

Controllare:

- cosa significa “duplicato”;
- se le righe sono eventi o versioni;
- se la deduplicazione è deterministica;
- quanto valore viene rimosso.

### 6. Metric semantics

```text
base measures:
numerator:
denominator:
additivity:
refund/cancellation policy:
FX policy:
```

Controllare:

- ratio of sums vs average of ratios;
- stock vs flow;
- metriche additive, semi-additive e non additive;
- componenti condivisi del semantic layer.

### 7. Transformation path

```text
source
→ normalization
→ dedup/version handling
→ enrichment
→ aggregation/allocation
→ final model
```

Ogni step dovrebbe avere:

- grain in ingresso;
- grain in uscita;
- cosa cambia;
- perché cambia;
- test associati.

### 8. Quality invariants

```text
invariant:
tolerance:
severity:
failure behavior:
```

Includere dove rilevante:

- uniqueness;
- not null;
- accepted values;
- referential integrity;
- volume/freshness;
- join coverage;
- allocation conservation;
- reconciliation.

### 9. Update semantics

```text
source mutability:
change detection:
unique/merge key:
lookback:
delete policy:
backfill:
full refresh:
reconciliation:
```

Un modello incrementale deve dichiarare come continua a vedere modifiche tardive e se può essere ricostruito.

### 10. Service envelope

```text
refresh cadence:
expected ready time:
freshness target:
expected cost/scan:
performance threshold:
consumer pattern:
```

La qualità include anche arrivare in tempo e con un costo proporzionato.

### 11. Lineage e ownership

```text
upstream sources:
downstream consumers:
metric owner:
technical owner:
version/change log:
```

Se una modifica rompe una definizione, dobbiamo sapere chi viene impattato.

Il Capitolo 18 porterà questa logica a livello organizzativo. Qui ci basta rendere la trasformazione auditabile.

### 12. AI execution boundary

Se SQL viene generato o modificato da AI:

```text
allowed sources:
read-only boundary:
required tests:
required reconciliations:
human approval for writes:
```

L'AI deve ricevere più semantica possibile e operare dentro confini verificabili.

### Un esempio compatto

```text
MODEL: fct_valid_order_lines

PURPOSE
net revenue e margin analysis

GRAIN
una riga per order_line_id valido

POPULATION
ordini confirmed/delivered; cancelled esclusi; refund sottratti

TIME
order_business_date in timezone locale del mercato

KEYS
order_line_id unico
order_id many-to-one rispetto alle linee

PRODUCT DIMENSION
versione valida alla order_business_date

QUALITY
order_line_id unique [BLOCK]
product dimension coverage >= 99.9% [BLOCK]
Finance net revenue reconciliation ±0.3% [BLOCK]
freshness entro 07:30 [WARN]

UPDATE
mutable; updated_at + 45d lookback; late queue; full rebuild disponibile

OWNER
Analytics Engineering / Finance
```

Questa specifica permette a un analyst, a un reviewer o a un agente AI di capire ciò che il modello promette senza reverse-engineering completo della query.

### La domanda finale

Prima di pubblicare un dataset o KPI importante chiediamo:

> **Quali proprietà devono restare vere affinché il risultato continui a significare ciò che promettiamo? Sono documentate? Sono testate? Sappiamo che cosa succede quando si rompono?**

La maturità SQL di un Data Analyst non si misura dal numero di funzioni che conosce.

Si misura dalla capacità di costruire trasformazioni che **preservano significato, rendono visibili le assunzioni e possono essere comprese, testate e modificate senza affidarsi alla memoria dell'autore**.
