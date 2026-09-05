## 11.15 AI-assisted SQL: accelerare la sintassi senza delegare il contratto

Gli assistenti AI possono già generare SQL da linguaggio naturale, completare query, tradurre dialetti, spiegare codice legacy, suggerire test e proporre correzioni. Questo riduce davvero il costo della sintassi. Non riduce però la difficoltà della domanda più importante:

> **che cosa deve significare il risultato?**

Una `ROW_NUMBER()` può essere corretta e implementare una winner rule sbagliata. Un `JOIN` può compilare e moltiplicare una misura. Una query può essere velocissima e usare la data o il denominatore sbagliati. Più la generazione diventa economica, più serve dare all’AI una specifica semantica invece di chiederle di indovinarla.

### Microsoft Fabric Copilot: produttività con review esplicita

Microsoft Fabric documenta Copilot per SQL con natural language to T-SQL, completamento, explain e fix. La stessa documentazione avverte che le risposte possono essere inaccurate e devono essere testate, revisionate e validate da persone in grado di valutarne correttezza e appropriatezza prima dell’uso o di modifiche al database.

Fonti:

- https://learn.microsoft.com/en-us/fabric/database/sql/copilot-sql-database
- https://learn.microsoft.com/en-us/fabric/database/sql/copilot-faq

Questo è coerente con il principio del Capitolo 0: l’esecuzione può essere delegata; la responsabilità sulla semantica e sull’approvazione no.

### HelioTravel: SQL perfetto per un requisito ambiguo

Un analyst chiede:

> Mostrami il revenue medio per cliente per paese negli ultimi 12 mesi.

L’assistente produce:

```sql
SELECT
    c.country,
    SUM(o.net_revenue) / COUNT(DISTINCT o.customer_id) AS avg_revenue_per_customer
FROM orders o
JOIN customers c
  ON o.customer_id = c.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY c.country;
```

La query risponde letteralmente al prompt. Il business intendeva però il net revenue medio generato **nei primi 365 giorni dalla acquisizione** per cliente acquisito in ciascun Paese. Cambiano almeno quattro elementi: finestra relativa alla `acquisition_date`, popolazione delle coorti, trattamento dei clienti senza ordini successivi e paese al momento dell’acquisizione anziché paese corrente.

L’AI non ha commesso un errore SQL. Ha materializzato fedelmente un requisito ambiguo.

### Dal prompt libero alla generazione contract-driven

“Calcola la conversione per paese” lascia all’assistente troppe decisioni implicite. Un input migliore può dichiarare:

```text
output grain: una riga per acquisition_country e acquisition_month
population: sessioni web eligible, bot esclusi
conversion numerator: sessioni con almeno un ordine valido
conversion denominator: eligible sessions
order validity: net amount > 0 dopo cancellation/refund
session date: local business date Europe/Rome
join: preservare sessioni senza ordine
country: country_at_session_time
```

Questo non garantisce la correttezza. Sposta però il problema da “indovinare il significato” a “implementare e verificare una specifica”.

### Review: confrontare il codice con ciò che promette

Una review AI-assisted dovrebbe seguire il contract. Prima controlliamo se la query produce il grain dichiarato e preserva la popolazione; poi se cardinalità e row multiplier sono coerenti; quindi time semantics, point-in-time history, `NULL`, denominatori e many-to-many. Alcuni record conosciuti ed edge case dovrebbero essere ricostruiti manualmente, e i componenti economici riconciliati con fonti certificate.

L’AI può essere utile anche come seconda passata indipendente:

```text
Confronta questa query con l'Analytical Data Contract.
Cerca failure mode su grain, cardinalità, popolazione, date/timezone,
NULL, denominatori, SCD, dedup e many-to-many.
Non modificare dati. Segnala assunzioni non dimostrate.
```

Il vero asset da conservare non è il testo SQL generato oggi, ma:

```text
specifica semantica
+ implementazione versionata
+ test
+ lineage
+ owner
```

### Il confine di esecuzione cambia con il rischio

Una `SELECT` sbagliata può produrre una conclusione errata. `UPDATE`, `DELETE`, `MERGE`, `DROP` o `CREATE OR REPLACE` possono invece modificare lo stato del sistema. Per operazioni mutative servono guardrail più forti: ambiente corretto, least privilege, preview delle righe, transazione quando disponibile, backup/versioning, rollback e approvazione umana.

L’AI crea valore soprattutto dove la semantica è già abbastanza esplicita: boilerplate, sintassi rara, traduzione di dialetti, refactoring in CTE leggibili, generazione di test dal contract, documentazione e prima lettura di execution plan.

### AI execution boundary

```text
allowed sources:
allowed operations:
read-only? sì/no
required tests:
required reconciliations:
human approval threshold:
production write permissions:
```

> **L’AI può generare SQL in pochi secondi. Il vantaggio professionale dell’analista è sapere quali proprietà quella query deve preservare prima di poterla considerare una risposta.**
