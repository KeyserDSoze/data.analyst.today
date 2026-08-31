## 11.5 Fact, dimension e star schema: modellare per le domande analitiche

I sistemi operativi sono progettati per far funzionare il business. I modelli analitici sono progettati per interrogare il business.

Queste due esigenze non coincidono.

Un CRM può avere decine di tabelle normalizzate per contatti, account, indirizzi, stati, contratti e preferenze. Copiare quella struttura direttamente in un modello BI spesso produce query fragili e difficili da comprendere.

Lo star schema nasce proprio per separare:

- **fact tables**, che rappresentano eventi o misure;
- **dimension tables**, che descrivono il contesto di quegli eventi.

Microsoft Learn descrive lo star schema come un approccio maturo e ampiamente adottato nei data warehouse relazionali, sottolineando che le dimensioni servono tipicamente a filtrare e raggruppare, mentre i fatti vengono riepilogati. Un principio fondamentale è che le fact table mantengano un grain coerente.

### Caso simulato — Meridian Retail e il modello impossibile da usare

Meridian Retail ha 180 negozi e un e-commerce europeo. Il primo data mart commerciale viene costruito copiando quasi integralmente l'ERP.

Per ottenere revenue per categoria, regione e mese servono join tra:

- `sales_header`;
- `sales_detail`;
- `product_master`;
- `product_category_history`;
- `store_master`;
- `store_address`;
- `region_mapping`;
- `calendar_periods`;
- `customer_master`.

Ogni dashboard ricostruisce una variante della stessa logica.

Dopo pochi mesi emergono tre problemi:

1. dashboard differenti assegnano negozi a regioni diverse;
2. le categorie prodotto storiche vengono reinterpretate con la classificazione corrente;
3. il revenue viene duplicato in alcune query per join molti-a-molti.

Il team ridisegna il modello:

```text
                 dim_date
                    |
dim_store --- fact_sales --- dim_product
                    |
                dim_customer
```

`fact_sales` ha una riga per linea di vendita.

Contiene:

- date key;
- store key;
- product key;
- customer key quando disponibile;
- quantity;
- gross revenue;
- discount;
- net revenue;
- cost.

Le dimensioni contengono gli attributi descrittivi.

La query per revenue mensile per categoria diventa molto più leggibile e, soprattutto, più coerente tra strumenti.

### Definire prima il grain della fact table

La frase più importante viene prima delle colonne:

> `fact_sales`: una riga per linea di vendita confermata.

Oppure:

> `fact_inventory_snapshot`: una riga per prodotto-magazzino-giorno a fine giornata.

Oppure:

> `fact_subscription_events`: una riga per evento contrattuale.

Il grain stabilisce cosa possiamo sommare e come possiamo fare join.

### Event facts e snapshot facts

Due modelli possono rappresentare lo stesso dominio da prospettive diverse.

Per l'inventario:

**event fact**

```text
+10 ricezione
-3 vendita
-1 danneggiato
```

**periodic snapshot**

```text
2026-08-01 → stock 84
2026-08-02 → stock 80
2026-08-03 → stock 91
```

Gli eventi spiegano i movimenti. Gli snapshot descrivono lo stato a un momento.

Usare uno come se fosse l'altro produce errori concettuali.

### Dimensioni e contesto storico

Una dimensione prodotto può descrivere:

- brand;
- categoria;
- segmento;
- supplier;
- fascia prezzo.

Ma cosa succede se un prodotto cambia categoria?

Se sovrascriviamo semplicemente il valore corrente, un report del 2024 può cambiare nel 2026.

Questo è il problema delle Slowly Changing Dimensions.

Non serve che ogni analyst implementi personalmente una SCD Type 2, ma deve capirne la conseguenza analitica: **il passato può essere riclassificato oppure preservato nella sua semantica storica**.

### Surrogate keys

Nei modelli dimensionali è comune usare chiavi surrogate invece di affidarsi solo alle chiavi operative.

Perché?

Un cliente può cambiare stato, segmento o attributi storicizzati. Due versioni della stessa entità business possono quindi avere chiavi dimensionali diverse.

Questo permette a una fact storica di puntare alla versione corretta della dimensione.

### Star schema non significa “una tabella enorme”

Denormalizzare tutto in una singola tabella larga può sembrare semplice, ma crea altri problemi:

- attributi duplicati su milioni di righe;
- logiche di aggiornamento difficili;
- maggiore rischio di inconsistenza;
- minore riusabilità delle dimensioni.

Lo star schema cerca un compromesso: abbastanza denormalizzato per essere analiticamente semplice, ma abbastanza strutturato da mantenere separati fatti e contesto.

### Regola operativa

Quando progettiamo un modello analitico, chiediamo:

1. quali processi di business vogliamo misurare?
2. qual è il grain di ogni fact?
3. quali dimensioni descrivono quei fatti?
4. quali misure sono additive?
5. quali cambiamenti storici dobbiamo preservare?
6. quali definizioni devono essere condivise da più report?

> **Il modello dati migliore non è quello che riproduce fedelmente il database operativo. È quello che rende semplici, coerenti e verificabili le domande analitiche importanti.**

---

**Riferimenti**

Microsoft Learn, *Understand star schema and the importance for Power BI*: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

Microsoft Learn, *Dimensional modeling in Microsoft Fabric Warehouse*: https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-overview
