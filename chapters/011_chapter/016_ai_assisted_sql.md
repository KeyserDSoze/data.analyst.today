## 11.15 AI-assisted SQL: accelerare la sintassi senza delegare il contratto

Gli assistenti AI possono già:

- generare SQL da linguaggio naturale;
- completare query;
- tradurre tra dialetti;
- spiegare codice legacy;
- suggerire test;
- proporre correzioni.

Questo cambia davvero il costo della sintassi.

Non cambia però la domanda più difficile:

> **che cosa deve significare il risultato?**

Una `ROW_NUMBER()` corretta può implementare una deduplicazione sbagliata. Un `JOIN` perfetto può moltiplicare una misura. Una query velocissima può usare la data sbagliata.

Per questo l'AI-assisted SQL deve consumare, per quanto possibile, lo stesso **Analytical Data Contract** che userebbe un analyst umano.

### Caso reale documentato — Microsoft Fabric Copilot

Microsoft Fabric documenta funzionalità Copilot che trasformano richieste in linguaggio naturale in T-SQL, completano codice e offrono azioni di explain/fix.

La documentazione Microsoft avverte però che le risposte non sono perfette e devono essere **testate, revisionate e validate** prima di apportare cambiamenti a un database.

Fonti:

- https://learn.microsoft.com/en-us/fabric/database/sql/query
- https://learn.microsoft.com/en-us/fabric/database/sql/copilot-faq

Il principio è esattamente quello del Capitolo 0:

> la capacità di eseguire può essere delegata; la responsabilità di capire e approvare resta umana.

### Caso simulato/composito — una query perfetta per la domanda sbagliata

Un analyst di HelioTravel chiede:

> Mostrami il revenue medio per cliente per paese negli ultimi 12 mesi.

L'assistente produce:

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

La query compila e risponde letteralmente al prompt.

Ma il business intendeva:

> quanto net revenue genera mediamente, nei primi 365 giorni, un cliente acquisito in ciascun paese?

Cambiano almeno quattro cose:

- finestra relativa alla `acquisition_date` del singolo cliente;
- popolazione delle coorti;
- trattamento dei clienti senza ordini successivi;
- paese al momento dell'acquisizione, non necessariamente paese corrente.

L'AI non ha commesso un errore di SQL.

Ha trasformato fedelmente un requisito ambiguo in codice.

### Prompt libero vs contract-driven generation

Un prompt libero può dire:

```text
Calcola la conversione per paese.
```

Un input guidato dal contract può dire:

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

Non garantisce la correttezza, ma sposta l'AI da “indovinare la semantica” a “implementare una specifica”.

È un enorme miglioramento del problema.

### Protocollo di verifica in otto passaggi

**1. Confrontare query e contract**

La query produce il grain dichiarato?

**2. Controllare la popolazione**

`INNER JOIN`, filtri e `NULL` stanno eliminando entità che dovrebbero restare?

**3. Controllare cardinalità e row multiplier**

Prima e dopo join critici:

```text
COUNT(*)
COUNT(DISTINCT business_key)
```

**4. Verificare la semantica temporale**

La query usa event time, reporting time, timezone e attributi point-in-time corretti?

**5. Testare record conosciuti**

Ricostruire manualmente alcuni casi normali ed edge case.

**6. Riconciliare i componenti**

Revenue, ordini o clienti devono essere compatibili con modelli o fonti certificate.

**7. Chiedere una critica indipendente**

L'AI può essere utile anche per produrre una seconda passata:

```text
Cerca failure mode semantici in questa query.
Confrontala con il contract e controlla grain, join, date, NULL,
denominatori, SCD e many-to-many.
```

La critica automatica è un acceleratore, non una garanzia.

**8. Salvare query + contract + test**

Il vero asset non è il testo SQL generato oggi.

È:

```text
specifica semantica
+ implementazione versionata
+ test
+ lineage
+ owner
```

### AI e DDL/DML: il livello di rischio cambia

Una query `SELECT` sbagliata può produrre una conclusione errata.

Un `UPDATE`, `DELETE`, `MERGE`, `DROP` o `CREATE OR REPLACE` sbagliato può modificare lo stato del sistema.

Per operazioni mutative servono guardrail più forti:

- ambiente corretto;
- least privilege;
- preview delle righe coinvolte;
- transazione quando disponibile;
- backup/versioning;
- rollback;
- approvazione umana.

Il principio non dipende dallo strumento AI utilizzato.

### Dove l'AI crea valore reale

L'AI può essere particolarmente efficace per:

- boilerplate;
- sintassi rara;
- traduzione di dialetti;
- refactoring in CTE leggibili;
- spiegazione di query legacy;
- generazione di test a partire dal contract;
- confronto tra implementazione e specifica;
- documentazione;
- prima lettura di execution plan.

Più la sintassi diventa economica, più aumenta il valore di:

- semantica;
- test;
- review;
- ownership.

### Campo del contract: AI execution boundary

Per trasformazioni assistite da AI può essere utile dichiarare:

```text
allowed sources:
allowed operations:
read-only? sì/no
required tests:
required reconciliations:
human approval threshold:
production write permissions:
```

Questo anticipa temi che riprenderemo nel Capitolo 14 sugli AI workflow e nel Capitolo 18 sulla governance degli agenti.

> **L'AI può generare una query in pochi secondi. Il vantaggio competitivo dell'analista è sapere quali proprietà quella query deve preservare prima di potersi fidare del risultato.**
