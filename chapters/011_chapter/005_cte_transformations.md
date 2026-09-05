## 11.4 CTE e trasformazioni leggibili: rendere verificabile il percorso del dato

Una query lunga non è necessariamente complessa dal punto di vista analitico e una query corta non è necessariamente semplice. La domanda professionale è un’altra: **possiamo verificare, passaggio per passaggio, come cambiano grain, popolazione e metrica?**

Le Common Table Expressions sono utili quando danno confini espliciti a queste trasformazioni. Un flusso analitico può essere letto così:

```text
raw events
→ eligibility filter
→ deduplication
→ grain normalization
→ dimension enrichment
→ metric components
→ final aggregation
```

Ogni freccia dovrebbe avere una ragione semantica e un effetto osservabile.

### BrightCart: la conversione che cambiava ogni lunedì

BrightCart calcola la conversione settimanale con una query di circa 230 righe, piena di subquery annidate. Il risultato differisce regolarmente di qualche decimo di punto dal dashboard Product. La logica viene riscritta in blocchi:

```sql
WITH eligible_sessions AS (...),
orders_deduped AS (...),
orders_by_session AS (...),
session_outcomes AS (...),
weekly_metrics AS (...)
SELECT *
FROM weekly_metrics;
```

Durante la riscrittura emerge il problema: le sessioni bot venivano filtrate dopo il join con gli ordini, quando alcuni eventi avevano già moltiplicato le righe. La nuova query non è più affidabile perché usa CTE. È più auditabile perché ogni blocco ha una responsabilità dichiarabile.

Un buon test è riuscire a descrivere ogni output in una frase: `eligible_sessions` è una riga per sessione eleggibile; `orders_deduped`, una riga per ordine logico; `orders_by_session`, una riga per sessione con componenti ordine aggregati; `weekly_metrics`, una riga per settimana e canale. Se un blocco filtra, deduplica, cambia grain, arricchisce, assegna categorie e calcola metriche contemporaneamente, diventa difficile capire quale scelta abbia modificato il risultato.

Per lo stesso motivo, nomi come `eligible_customers`, `recognized_revenue` o `active_subscriptions` sono più utili di `cte1`, `tmp2` o `final_data`: il nome dovrebbe dichiarare **che cosa rappresenta il dataset**, non la sua posizione nella query.

### Gli invarianti trasformano il percorso in una specifica

Consideriamo:

```text
raw_orders
→ orders_deduped
```

Se la deduplicazione preserva l’identità logica degli ordini, possiamo aspettarci che `COUNT(DISTINCT logical_order_id)` resti invariato, che dopo il passaggio non esistano duplicati sulla chiave finale e che il valore economico rimosso sia spiegabile dalla policy.

Oppure:

```text
eligible_sessions
→ session_outcomes
```

possiamo richiedere una riga per sessione, nessuna sessione eleggibile persa, `converted_flag ∈ {0,1}` e `converted_sessions <= eligible_sessions`.

Questi invarianti cambiano la natura della query: da testo eseguibile a **pipeline verificabile**.

### Riproducibilità: la stessa logica deve ricostruire lo stesso passato

Una trasformazione non è davvero riproducibile se dipende implicitamente dal momento in cui viene eseguita. Una condizione come:

```sql
WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
```

può essere corretta per un job operativo, ma non basta per ricostruire un’analisi storica. Lo stesso vale per dimensioni sovrascritte retroattivamente. Per analisi importanti conviene rendere espliciti `as_of_timestamp`, observation window, source snapshot/version, timezone, versione della logica e policy sui dati tardivi.

Atlas Mobility rende bene il problema. Growth, Finance, Product e Operations riportano quattro “monthly active users” differenti: almeno un login, una ricerca, una corsa iniziata o una corsa completata. Nessuna CTE può scegliere quale sia la definizione vera. Sono quattro concetti differenti con lo stesso nome; vanno nominati, per esempio, `monthly_logged_in_users`, `monthly_trip_searchers`, `monthly_trip_starters` e `monthly_completed_riders`, e poi collegati alle decisioni appropriate.

### Quando una query smette di essere ad hoc

Una logica merita di diventare condivisa quando alimenta più consumer, viene rieseguita periodicamente, definisce una KPI ufficiale, contiene join/storicizzazione difficili o diventa input per modelli e sistemi AI. La promozione non richiede soltanto più codice: richiede una catena esplicita di logica, test, owner, versione, documentazione e refresh.

Per questo il transformation path dell’Analytical Data Contract può essere sintetizzato così:

| Step | Grain | Operazione | Popolazione | Invariant |
|---|---|---|---|---|
| `eligible_sessions` | sessione | filtra eligibility | sessioni umane | chiave unica |
| `orders_by_session` | sessione | aggrega ordini | sessioni con/senza ordine | max 1 riga/sessione |
| `session_outcomes` | sessione | deriva conversion | tutte le eleggibili | flag 0/1 |
| `weekly_metrics` | settimana-canale | aggrega componenti | tutte le eleggibili | numerator ≤ denominator |

> **Una buona CTE non nasconde la complessità: la divide in passaggi di cui possiamo dichiarare grain, scopo ed invarianti.**
