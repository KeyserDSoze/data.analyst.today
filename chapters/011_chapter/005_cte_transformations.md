## 11.4 CTE e trasformazioni leggibili: rendere verificabile il percorso del dato

Una query lunga non è necessariamente complessa dal punto di vista analitico. Una query corta non è necessariamente semplice.

La domanda professionale è un’altra:

> **posso verificare, passaggio per passaggio, come cambiano grain, popolazione e metrica?**

Le Common Table Expressions, o CTE, sono utili quando rendono queste trasformazioni esplicite.

Un buon flusso può essere letto così:

```text
raw events
→ eligibility filter
→ deduplication
→ grain normalization
→ dimension enrichment
→ metric components
→ final aggregation
```

Ogni freccia dovrebbe avere una ragione analitica, non soltanto tecnica.

### Caso simulato/composito — BrightCart e la conversione che cambiava ogni lunedì

BrightCart calcola la conversione settimanale con una query di circa 230 righe piena di subquery annidate.

Il risultato differisce regolarmente di qualche decimo di punto dal dashboard Product.

La query viene riscritta così:

```sql
WITH eligible_sessions AS (...),
orders_deduped AS (...),
orders_by_session AS (...),
session_outcomes AS (...),
weekly_metrics AS (...)
SELECT *
FROM weekly_metrics;
```

Durante la riscrittura emerge il problema: le sessioni riconosciute come bot venivano filtrate **dopo** il join con gli ordini. Alcuni eventi avevano già moltiplicato le righe.

La nuova query non è corretta perché contiene CTE. È più affidabile perché ogni blocco ha una responsabilità dichiarabile.

### Una CTE dovrebbe avere un grain pronunciabile

Un test editoriale e tecnico molto semplice:

> riesco a descrivere l’output di questa CTE in una frase?

Per esempio:

- `eligible_sessions`: una riga per sessione eleggibile;
- `orders_deduped`: una riga per ordine logico;
- `orders_by_session`: una riga per sessione con componenti ordine aggregati;
- `session_outcomes`: una riga per sessione con conversion flag;
- `weekly_metrics`: una riga per settimana e canale.

Se una CTE:

- filtra;
- deduplica;
- cambia grain;
- calcola una metrica;
- assegna una categoria;
- e unisce altre quattro sorgenti;

tutto insieme, sarà difficile capire quale passaggio ha modificato il numero finale.

### Nomi semantici, non procedurali

Meglio:

```text
eligible_customers
orders_by_customer
active_subscriptions
recognized_revenue
```

che:

```text
cte1
tmp2
final_data
base_new
```

Il nome dovrebbe dire **che cosa rappresenta il dataset**, non soltanto dove si trova nella query.

### Gli invarianti tra uno step e il successivo

Una trasformazione auditabile non mostra soltanto l’output. Dichiara anche che cosa deve rimanere vero.

Esempio:

```text
raw_orders
→ orders_deduped
```

Invariant possibili:

- `COUNT(DISTINCT logical_order_id)` invariato;
- nessun `logical_order_id` duplicato dopo la dedup;
- gross order amount riconciliato entro la policy dichiarata.

Altro esempio:

```text
eligible_sessions
→ session_outcomes
```

Invariant:

- una riga per sessione;
- nessuna sessione eleggibile persa;
- `converted_flag` ∈ {0,1};
- `converted_sessions <= eligible_sessions`.

Questo trasforma la query da testo eseguibile a **pipeline verificabile**.

### Idempotenza e riproducibilità

Una trasformazione dovrebbe produrre lo stesso risultato partendo dagli stessi input e dalle stesse regole.

Questo requisito sembra banale finché una query contiene:

```sql
WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
```

oppure usa una dimensione che viene sovrascritta retroattivamente.

La stessa query eseguita domani può ricostruire un passato differente.

Per analisi importanti conviene rendere espliciti:

- `as_of_timestamp`;
- observation window;
- source snapshot/version;
- timezone;
- versione della logica;
- policy sui dati arrivati in ritardo.

### Caso simulato/composito — Atlas Mobility e quattro definizioni di “active rider”

Growth, Finance, Product e Operations riportano numeri diversi per gli utenti attivi mensili.

Le logiche sono:

1. almeno un login;
2. almeno una ricerca di corsa;
3. almeno una corsa iniziata;
4. almeno una corsa completata.

Il problema non è trovare la query “vera”.

Sono quattro concetti differenti con lo stesso nome.

La soluzione è rendere esplicite le entità:

- `monthly_logged_in_users`;
- `monthly_trip_searchers`;
- `monthly_trip_starters`;
- `monthly_completed_riders`.

Poi il business decide quale concetto supporta quale decisione.

### Quando promuovere una query ad hoc

Una query esplorativa può restare locale.

La logica dovrebbe invece diventare condivisa quando:

- alimenta più dashboard;
- viene rieseguita periodicamente;
- definisce una KPI ufficiale;
- viene usata da più team;
- contiene join o storicizzazione difficili;
- supporta una decisione ad alto rischio;
- diventa feature per modelli o input per sistemi AI.

La promozione implica almeno:

```text
logica esplicita
→ test
→ owner
→ versione
→ documentazione
→ refresh definito
```

### Transformation path nell’Analytical Data Contract

Per una pipeline importante possiamo documentare:

| Step | Grain | Operazione | Popolazione | Invariant |
|---|---|---|---|---|
| `eligible_sessions` | sessione | filtra eligibility | sessioni umane | chiave unica |
| `orders_by_session` | sessione | aggrega ordini | sessioni con/senza ordine | max 1 riga/sessione |
| `session_outcomes` | sessione | deriva conversion | tutte le eleggibili | flag 0/1 |
| `weekly_metrics` | settimana-canale | aggrega componenti | tutte le eleggibili | numerator ≤ denominator |

Questa tabella permette a un reviewer di capire la trasformazione anche prima di leggere SQL.

> **Una buona CTE non serve a nascondere complessità. Serve a darle confini che possiamo verificare.**
