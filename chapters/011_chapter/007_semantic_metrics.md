## 11.6 Metriche riusabili e semantic layer: la definizione deve vivere fuori dalla singola query

Quando un’organizzazione cresce, il problema non è più soltanto accedere ai dati. Diventa evitare che parole come revenue, conversion, margin, churn, ARR o active customer cambino significato da team a team e da dashboard a dashboard.

### Northwave SaaS: tre ARR, tre decisioni

Northwave presenta nello stesso leadership meeting tre numeri di ARR:

- Finance: €38,4M;
- Sales: €40,1M;
- Product Analytics: €39,2M.

Nessuna query è sintatticamente sbagliata. Finance esclude contratti in grace period e applica i cambi di chiusura; Sales include contratti firmati ma non ancora attivati; Product Analytics considera account con workspace attivo.

Il problema non si risolve scegliendo “la query vera”. I tre numeri descrivono concetti differenti e dovrebbero essere nominati come tali, per esempio `contracted_arr`, `activated_arr` e `recognized_arr`, dichiarando quale supporta quale decisione.

Questo mostra perché una metrica è un contratto, non una formula. Una definizione robusta comprende almeno business meaning, base entity, grain, popolazione eleggibile, esclusioni, time semantics, componenti, valuta, history policy, owner, refresh e lineage. La formula è soltanto una parte.

### Base measures prima delle metriche derivate

È utile distinguere componenti atomici come `gross_revenue`, `discount_amount`, `return_amount`, `orders`, `eligible_sessions`, `converted_sessions` e `actual_cogs` da metriche derivate come AOV, conversion rate o gross margin %.

Per esempio:

```text
conversion_rate
=
converted_sessions / eligible_sessions
```

Se i componenti hanno semantica certificata, la ratio può essere ricalcolata coerentemente a diversi livelli senza materializzare percentuali incompatibili.

Aeris Commerce rende evidente il problema. Tre dashboard riportano gross margin 31,4%, 29,8% e 34,1%, pur dichiarando tutte `(revenue - COGS) / revenue`. La formula è uguale; cambiano i termini. Una usa gross revenue, una net revenue dopo sconti, una net revenue dopo resi. Anche COGS cambia tra costo standard ed effettivo. La soluzione è modellare componenti distinti e certificare metriche diverse, non aggiungere un commento alle tre query.

### Il semantic layer come infrastruttura di coerenza

Un semantic layer porta definizioni riusabili sopra le tabelle fisiche:

```text
fonti fisiche
→ relazioni e grain
→ misure base
→ metriche certificate
→ dimensioni consentite
→ query / report / AI
```

Databricks descrive le metric views proprio come un semantic layer che standardizza che cosa misurare, come aggregarlo e come segmentarlo; i componenti espliciti includono source, join, filter, field e measure.

Fonte: https://docs.databricks.com/aws/en/uc-semantics/metric-views/basic-modeling

Il dettaglio tecnologico può cambiare. La necessità semantica no: definire una volta la metrica, rendere visibili le dimensioni consentite e riusarla senza riscrivere la stessa logica in ogni consumer.

Questo diventa ancora più importante con l’AI. Un LLM può produrre rapidamente:

```sql
SELECT SUM(amount)
FROM subscriptions;
```

ma `amount` può significare invoice amount, contracted value, cash collected, MRR, annualized value o amount al netto di credit note. Più l’accesso diventa conversazionale, più serve una superficie che renda espliciti nomi, grain, join consentiti, filtri, owner, freshness, lineage e caveat. L’AI abbassa il costo della sintassi; aumenta il valore relativo della semantica.

### Certificare non significa rendere universale

“Customer” può voler dire persona registrata, account pagante, buyer con almeno un ordine, contratto attivo o workspace attivo. Un semantic layer maturo non dovrebbe cancellare queste differenze ma renderle nominabili:

```text
registered_users
paying_accounts
purchasing_customers_12m
active_contracts
active_workspaces
```

Lo stesso vale per l’additività. Un headcount snapshot può essere aggregato per department nello stesso giorno, ma sommare headcount giornaliero sul mese produce person-days, non monthly headcount. La definizione deve quindi dichiarare anche temporal grain, dimensioni valide, default aggregation e componenti che devono essere ricalcolati.

### Metric semantics nell’Analytical Data Contract

Per ogni KPI importante dovremmo poter rispondere a queste domande: qual è l’entità misurata? Qual è il grain atomico? Chi è eleggibile? Quale tempo governa la metrica? Quali componenti entrano? Qual è il denominatore? Come trattiamo resi, cancellazioni e rettifiche? Quale valuta usiamo? Il passato viene restated? Quali dimensioni sono valide? Chi possiede la definizione? Qual è la fonte certificata?

> **Una metrica condivisa non elimina il bisogno di ragionare. Elimina il bisogno di reinventare silenziosamente lo stesso significato in ogni query.**
