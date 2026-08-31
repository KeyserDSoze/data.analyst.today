## 11.6 Metriche riusabili e semantic layer: una definizione, molte analisi

Quando un'organizzazione cresce, il problema non è più soltanto accedere ai dati. Diventa mantenere coerente il significato delle metriche.

“Revenue”, “active customer”, “conversion”, “margin”, “churn”, “new customer” sembrano parole semplici. In realtà sono contratti semantici.

### Caso simulato — Northwave SaaS e le tre versioni dell'ARR

Northwave SaaS presenta tre numeri diversi di ARR nello stesso meeting:

- Finance: 38,4 milioni;
- Sales: 40,1 milioni;
- Product analytics: 39,2 milioni.

Nessuna query contiene un errore sintattico.

Le differenze derivano dalle definizioni:

- Finance esclude contratti in grace period e valuta gli importi ai cambi mensili di chiusura;
- Sales include contratti firmati ma non ancora attivati;
- Product analytics considera solo account con workspace attivo.

Il problema non può essere risolto con una query “più furba”.

Serve distinguere le metriche.

Per esempio:

- `contracted_arr`;
- `activated_arr`;
- `recognized_arr`.

Poi si documenta quale metrica risponde a quale decisione.

### Una metrica è più di una formula

Una definizione robusta dovrebbe includere almeno:

- nome;
- significato business;
- numeratore;
- denominatore, se esiste;
- popolazione inclusa;
- esclusioni;
- grain;
- dimensione temporale;
- gestione di cancellazioni/resi/rimborsi;
- valuta e conversione;
- owner;
- frequenza di aggiornamento;
- fonte.

### Perché il semantic layer conta nell'era dell'AI

Se un LLM genera una query su un warehouse ambiguo, la velocità aumenta ma non la correttezza.

Un assistente può produrre perfettamente:

```sql
SELECT SUM(amount) FROM subscriptions;
```

ma non può sapere da solo se `amount` rappresenta MRR, invoice amount, contracted value o cash collected, a meno che il modello semantico e la documentazione non lo rendano esplicito.

L'AI rende quindi ancora più importante avere:

- nomi coerenti;
- metriche certificate;
- relazioni chiare;
- definizioni condivise;
- lineage;
- controlli automatici.

### Metriche base e metriche derivate

È utile distinguere:

**metriche base**

- revenue netta;
- ordini;
- clienti distinti;
- unità vendute;
- costi.

**metriche derivate**

- AOV;
- conversion rate;
- gross margin %;
- repeat purchase rate;
- revenue per active customer.

Le metriche derivate dovrebbero idealmente dipendere da componenti condivisi, non ricostruiti ogni volta.

### Caso simulato — Aeris Commerce e il margine che cambiava da dashboard a dashboard

Tre dashboard mostrano gross margin:

- 31,4%;
- 29,8%;
- 34,1%.

Le formule sono:

```text
(revenue - COGS) / revenue
```

ma il termine `revenue` cambia:

- gross revenue;
- net revenue dopo sconti;
- net revenue dopo resi.

Anche `COGS` cambia perché una dashboard usa costo standard, un'altra costo effettivo.

La soluzione è modellare componenti espliciti:

- `gross_revenue`;
- `discount_amount`;
- `return_amount`;
- `net_revenue`;
- `standard_cogs`;
- `actual_cogs`.

Poi definire metriche certificate.

> **Una metrica condivisa riduce il costo cognitivo dell'analisi. Non dobbiamo ridiscutere il significato ogni volta che apriamo un notebook.**
