## 12.6 Semantic layer: definire una volta, usare molte volte

Più cresce l'organizzazione, più diventa pericoloso lasciare che ogni dashboard o notebook reinventi le metriche.

Il **semantic layer** nasce per ridurre questo problema.

L'idea è separare il dato fisico dalle definizioni di business che devono essere condivise.

In un semantic layer possiamo centralizzare concetti come:

- revenue;
- gross margin;
- active customer;
- churn;
- conversion rate;
- fiscal calendar;
- geography;
- product hierarchy.

Il vantaggio non è soltanto tecnico. È organizzativo.

## Caso realistico: tre conversion rate corretti

**SkyShop** ha tre dashboard:

- Marketing: conversion = orders / sessions;
- Product: conversion = purchasers / users;
- Finance: conversion = paid orders / checkout starts.

Tutte e tre le formule sono matematicamente corrette.

Ma una riunione executive confronta i tre numeri come se misurassero la stessa cosa.

Il problema non si risolve scegliendo una formula universale. Si risolve rendendo esplicite le semantiche:

```text
session_to_order_conversion
user_to_purchase_conversion
checkout_to_paid_conversion
```

Ogni metrica ha:

- definizione;
- grain;
- numeratore;
- denominatore;
- filtri;
- owner;
- casi esclusi;
- versione.

## Metriche come prodotti riusabili

Una metrica importante dovrebbe poter essere interrogata da più strumenti senza essere riscritta ogni volta.

Questo permette:

- coerenza;
- auditabilità;
- governance;
- minore duplicazione;
- onboarding più rapido degli analyst;
- AI più affidabile quando genera query.

Databricks, ad esempio, descrive le metric views come oggetti che centralizzano metriche riusabili separando le definizioni delle misure dai raggruppamenti dimensionali. Microsoft usa semantic models per concetti analoghi nel mondo BI.

## Il semantic layer non sostituisce il warehouse

Non dobbiamo confondere i livelli.

Il warehouse o lakehouse gestisce dati, storia, trasformazioni e modelli.

Il semantic layer rappresenta la business logic in una forma consumabile.

Se il dato sottostante è sbagliato, una definizione elegante non lo salva.

## Caso realistico: ARR definito una volta, sbagliato ovunque

**BluePeak SaaS** centralizza l'ARR nel semantic layer.

Dopo sei mesi scopre che la formula include anche contratti cancellati con data futura ma già completamente rimborsati.

Il vantaggio della centralizzazione diventa evidente proprio quando emerge l'errore:

- una sola definizione da correggere;
- lineage dei dashboard impattati;
- backfill controllato;
- comunicazione coerente.

Se la logica fosse stata duplicata in 27 report, la correzione avrebbe richiesto settimane.

Il semantic layer non garantisce che la metrica sia corretta. Garantisce che **la responsabilità della definizione sia visibile e gestibile**.

## AI e semantica

L'AI generativa rende il semantic layer ancora più importante.

Un modello può generare SQL molto rapidamente. Ma se non conosce:

- quale tabella è certificata;
- come definiamo active customer;
- quale calendario fiscale usiamo;
- quali refund escludere;

può produrre una query plausibile ma non coerente con l'organizzazione.

In un mondo di natural-language analytics, la qualità della risposta dipende sempre più dalla qualità della semantica resa disponibile alla macchina.

### Regola pratica

Le metriche usate per decisioni ricorrenti dovrebbero avere almeno:

```text
nome
business definition
formula
grain
owner
source
refresh SLA
known limitations
```

Questo è molto più prezioso di cento formule nascoste dentro cento dashboard.
