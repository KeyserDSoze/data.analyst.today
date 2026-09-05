## 11.17 Analytical Data Contract: rendere verificabile una trasformazione prima di pubblicarla

L’**Analytical Data Contract** è il deliverable operativo del capitolo. Qui la struttura a campi è intenzionale: deve essere scansionabile durante design, review e incident analysis. Non è una checklist di sintassi e non richiede necessariamente YAML o un prodotto specifico; può vivere in metadata, documentazione o codice. Ciò che conta è che grain, popolazione, tempo, metriche e policy di aggiornamento non restino nascosti dentro SQL.

### 1. Business meaning

```text
business question:
metric/use case:
decision supported:
owner:
```

Il dataset deve avere un fenomeno e una decisione riconoscibili. Prima di modellarlo verifichiamo se la metrica esiste già in una fonte certificata e chi possiede la definizione.

### 2. Grain e popolazione

```text
output grain:
source grains:
eligible population:
exclusions:
```

Controllare che il grain sia pronunciabile, che ogni cambio di grain sia esplicito e che filtri, `INNER JOIN` e `NULL` non eliminino silenziosamente casi necessari al denominatore.

### 3. Keys e relationship semantics

```text
business key:
record/event key:
expected uniqueness:
join cardinality:
many-to-many bridge:
allocation policy:
```

Verificare unicità reale, cardinalità 1:1 / 1:N / N:M, row multiplier e conservazione dei totali quando una misura viene allocata.

### 4. Time semantics

```text
business/event date:
reporting date:
timezone:
point-in-time attributes:
late-arrival policy:
```

La data deve rappresentare l’evento richiesto dalla decisione. Dichiarare inoltre timezone, current-state vs as-of history, backfill e restatement.

### 5. Identity e version semantics

```text
entity/event/version model:
version timestamp:
winner rule:
tie-break:
```

Specificare che cosa significa “duplicato”, se le righe sono eventi o versioni e quale regola deterministica produce l’eventuale stato corrente.

### 6. Metric semantics

```text
base measures:
numerator:
denominator:
additivity:
refund/cancellation policy:
FX policy:
```

Controllare ratio of sums vs average of ratios, stock vs flow, componenti condivisi, denominatori zero, resi/rettifiche e valuta.

### 7. Transformation path

```text
source
→ normalization
→ dedup/version handling
→ enrichment
→ aggregation/allocation
→ final model
```

Per ogni passaggio dichiarare grain in ingresso e uscita, ciò che cambia, perché cambia e quale test rende verificabile il cambiamento.

### 8. Quality invariants

```text
invariant:
tolerance:
severity:
failure behavior:
```

Includere dove rilevante uniqueness, not null, accepted values, referential integrity, volume/freshness, join coverage, allocation conservation e reconciliation. Severity e failure behavior devono riflettere il rischio della decisione.

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

Un modello incrementale deve spiegare come continua a osservare modifiche tardive e se può essere ricostruito dalla fonte di verità.

### 10. Service envelope

```text
refresh cadence:
expected ready time:
freshness target:
expected cost/scan:
performance threshold:
consumer pattern:
```

La correttezza perde valore se il dato arriva dopo la decisione o richiede un costo sproporzionato al suo uso.

### 11. Lineage e ownership

```text
upstream sources:
downstream consumers:
metric owner:
technical owner:
version/change log:
```

Una breaking semantic change deve avere owner e consumer identificabili. Il Capitolo 18 allargherà questa disciplina a governance e observability organizzative.

### 12. AI execution boundary

```text
allowed sources:
read-only boundary:
required tests:
required reconciliations:
human approval for writes:
```

Un agente AI dovrebbe implementare un contract già esplicito e operare dentro confini proporzionati al rischio dell’azione.

### Esempio compatto

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

Questa specifica permette a un analyst, a un reviewer o a un agente AI di capire ciò che il modello promette senza dover prima fare reverse-engineering dell’intera query.

La domanda finale prima della pubblicazione è semplice:

> **Quali proprietà devono restare vere affinché questo risultato continui a significare ciò che promettiamo? Sono documentate, testate e associate a un comportamento quando si rompono?**

La maturità SQL non si misura dal numero di funzioni conosciute, ma dalla capacità di costruire trasformazioni che preservano significato e possono essere comprese, verificate e modificate senza dipendere dalla memoria dell’autore.
