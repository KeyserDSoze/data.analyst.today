## 11.6 Metriche riusabili e semantic layer: la definizione deve vivere fuori dalla singola query

Quando un’organizzazione cresce, il problema non è più soltanto accedere ai dati. Diventa mantenere coerente il significato delle metriche tra persone, strumenti e momenti diversi.

Parole come:

- revenue;
- active customer;
- conversion;
- margin;
- churn;
- new customer;
- ARR;

sembrano semplici finché due team non le calcolano in modo diverso.

### Caso simulato/composito — Northwave SaaS e le tre versioni dell’ARR

Northwave SaaS presenta tre numeri di ARR nello stesso leadership meeting:

- Finance: €38,4M;
- Sales: €40,1M;
- Product Analytics: €39,2M.

Nessuna query contiene un errore sintattico.

Le definizioni sono diverse:

- Finance esclude contratti in grace period e applica i cambi di chiusura;
- Sales include contratti firmati ma non ancora attivati;
- Product Analytics considera account con workspace attivo.

Il problema non si risolve scegliendo “la query migliore”.

Le tre metriche rappresentano concetti differenti e dovrebbero avere nomi differenti, per esempio:

- `contracted_arr`;
- `activated_arr`;
- `recognized_arr`.

Poi si documenta quale metrica supporta quale decisione.

### Una metrica è un contratto, non una formula

Una definizione robusta dovrebbe includere almeno:

| Campo | Esempio |
|---|---|
| business meaning | revenue economicamente riconosciuto |
| base entity | linea di vendita / invoice line |
| grain | giorno × prodotto × mercato, o grain atomico |
| numerator | net recognized amount |
| denominator | se la metrica è una ratio |
| eligible population | transazioni incluse |
| exclusions | test, fraud, cancellation, internal traffic |
| time semantics | recognition date |
| currency policy | valuta reporting e FX rule |
| historical policy | restatement sì/no |
| owner | Finance Analytics |
| refresh | giornaliero entro 07:00 CET |
| lineage | fact e trasformazioni sorgente |

La formula è soltanto uno dei campi.

### Metriche base e metriche derivate

È utile separare componenti riusabili da metriche composte.

**Componenti/base measures**:

- gross revenue;
- discount amount;
- return amount;
- net revenue;
- orders;
- eligible sessions;
- converted sessions;
- actual COGS.

**Metriche derivate**:

- AOV;
- conversion rate;
- gross margin %;
- repeat purchase rate;
- revenue per active customer.

Una ratio dovrebbe derivare da componenti condivisi invece di essere materializzata come numero già aggregato ovunque.

Per esempio:

```text
conversion_rate
=
converted_sessions / eligible_sessions
```

Se i componenti hanno una semantica certificata, possiamo ricalcolare la metrica a diversi livelli senza ricostruirne ogni volta la definizione.

### Caso simulato/composito — Aeris Commerce e il margine che cambiava da dashboard a dashboard

Tre dashboard riportano gross margin:

- 31,4%;
- 29,8%;
- 34,1%.

Tutte dichiarano di usare:

```text
(revenue - COGS) / revenue
```

Il problema è nei termini.

`revenue` significa rispettivamente:

- gross revenue;
- net revenue dopo sconti;
- net revenue dopo resi.

Anche `COGS` cambia:

- costo standard;
- costo effettivo.

La soluzione non è aggiungere commenti alle tre query. È modellare componenti semanticamente distinti:

- `gross_revenue`;
- `discount_amount`;
- `return_amount`;
- `net_revenue_after_returns`;
- `standard_cogs`;
- `actual_cogs`.

Poi si certificano metriche diverse per decisioni diverse.

### Il semantic layer come infrastruttura di coerenza

Un semantic layer porta definizioni riusabili sopra le tabelle fisiche.

L’implementazione può cambiare da piattaforma a piattaforma, ma il principio resta:

```text
fonti fisiche
→ relazioni e grain
→ misure base
→ metriche certificate
→ dimensioni consentite
→ query/report/AI
```

Databricks descrive le metric views come un semantic layer che standardizza cosa misurare, come aggregarlo e come segmentarlo, così utenti diversi ottengono lo stesso KPI. I componenti espliciti includono source, join, filter, field e measure.

Fonte: https://docs.databricks.com/aws/en/uc-semantics/metric-views/basic-modeling

Il dettaglio tecnologico cambierà. La necessità semantica no.

### Perché il semantic layer diventa ancora più importante con l’AI

Un LLM può generare rapidamente:

```sql
SELECT SUM(amount)
FROM subscriptions;
```

ma non può dedurre in modo affidabile se `amount` significhi:

- invoice amount;
- contracted value;
- cash collected;
- MRR;
- annualized value;
- amount al netto di credit note.

Più l’accesso al dato diventa conversazionale e automatizzato, più serve una superficie semantica che renda espliciti:

- nomi;
- definizioni;
- join consentiti;
- grain;
- owner;
- freshness;
- lineage;
- filtri di default;
- caveat.

L’AI riduce il costo della sintassi. Aumenta quindi il valore relativo della semantica.

### Una metrica certificata non è necessariamente una metrica universale

È un errore cercare una sola definizione per ogni parola.

“Customer” può significare:

- persona registrata;
- account pagante;
- buyer con almeno un ordine;
- contratto attivo;
- workspace attivo.

Il semantic layer non dovrebbe cancellare queste differenze. Dovrebbe renderle **distinte e nominabili**.

Meglio avere:

```text
registered_users
paying_accounts
purchasing_customers_12m
active_contracts
active_workspaces
```

che un unico `customers` il cui significato cambia a seconda del report.

### Dimensioni consentite e non additività

Una metrica non è valida automaticamente a ogni slice.

Esempio: un headcount snapshot può essere aggregato per department nello stesso giorno, ma sommare headcount giornaliero su un mese produce “person-days”, non monthly headcount.

Una definizione semantica matura dovrebbe quindi dichiarare:

- dimensioni su cui la metrica è aggregabile;
- temporal grain;
- eventuale default aggregation;
- componenti da ricalcolare;
- filtri obbligatori.

### Metric semantics nell’Analytical Data Contract

Per ogni KPI importante il contratto dovrebbe poter rispondere:

1. qual è l’entità misurata?
2. qual è il grain atomico?
3. quali record sono eleggibili?
4. qual è la time semantics?
5. quali componenti entrano nella formula?
6. qual è il denominatore?
7. come gestiamo resi, cancellazioni e rettifiche?
8. quale valuta o unità usiamo?
9. il passato viene restated?
10. quali dimensioni sono valide?
11. chi possiede la definizione?
12. qual è la fonte certificata?

> **Una metrica condivisa non elimina il bisogno di ragionare. Elimina il bisogno di reinventare silenziosamente lo stesso significato in ogni query.**
