## 11.8 Date e temporalità: il tempo non è una colonna qualsiasi

In analisi dati, una delle fonti più comuni di errori non è il calcolo. È la scelta della **data sbagliata**.

Un ordine può avere molte date:

- `created_at`: quando il cliente ha creato l'ordine;
- `paid_at`: quando il pagamento è stato autorizzato;
- `shipped_at`: quando il magazzino ha spedito;
- `delivered_at`: quando il cliente ha ricevuto;
- `returned_at`: quando è stato restituito;
- `recognized_revenue_date`: quando il ricavo è stato riconosciuto contabilmente.

Tutte sono corrette. Ma rispondono a domande diverse.

### Caso realistico: il trimestre che sembrava crescere del 14%

Una piattaforma B2B, **ForgeMarket**, presenta al board una crescita Q4 del 14%.

La query del team commerciale usa:

```sql
SELECT
    DATE_TRUNC('quarter', created_at) AS quarter,
    SUM(order_value) AS bookings
FROM orders
GROUP BY 1;
```

Il CFO usa invece la data di fatturazione e ottiene +6%.

Il team Operations usa `delivered_at` e ottiene +2%.

Nessuno sta necessariamente sbagliando SQL. Stanno misurando **tre fenomeni diversi**:

- domanda commerciale;
- ricavo/fatturazione;
- esecuzione operativa.

Il problema nasce quando il nome della metrica è semplicemente `revenue`.

### Data dell'evento vs data di reporting

Una buona modellazione temporale distingue almeno:

1. quando l'evento è accaduto nel mondo reale;
2. quando è stato registrato nel sistema;
3. quando è diventato disponibile nel warehouse;
4. a quale periodo di reporting appartiene.

Questa distinzione diventa decisiva in presenza di:

- late-arriving data;
- timezone diverse;
- backfill;
- rettifiche contabili;
- eventi aggiornati retroattivamente.

### Timezone: un dettaglio che può cambiare il KPI

Un marketplace globale registra gli eventi in UTC.

Una campagna italiana parte alle 00:00 ora locale. Se l'analista raggruppa direttamente per `DATE(event_timestamp_utc)`, le prime due ore della campagna finiscono nel giorno precedente durante l'ora legale.

La conversione giornaliera può quindi sembrare peggiore proprio nel giorno di lancio.

Il controllo corretto non è solo:

```sql
DATE(event_timestamp)
```

ma qualcosa concettualmente equivalente a:

```sql
DATE(event_timestamp AT TIME ZONE 'Europe/Rome')
```

La sintassi esatta cambia tra database, ma la domanda non cambia:

> **Qual è la timezone con cui il business interpreta questo evento?**

### Snapshot e point-in-time correctness

Un altro errore frequente consiste nell'analizzare il passato usando attributi aggiornati oggi.

Esempio: un cliente era `SMB` nel 2024 e diventa `Enterprise` nel 2026.

Se una dimensione cliente contiene soltanto lo stato corrente, una query sulle vendite 2024 può attribuire quelle vendite al segmento Enterprise.

Il dato storico viene così riscritto semanticamente.

Questo problema porta direttamente alle Slowly Changing Dimensions, che vedremo nella sezione successiva.

### Regola operativa

Prima di scrivere una query temporale, esplicitare sempre:

- quale evento definisce il periodo;
- quale timezone usare;
- se serve event time o processing time;
- se gli attributi devono essere quelli correnti o quelli validi all'epoca;
- come trattare eventi tardivi e rettifiche.

**La data corretta non è la colonna più comoda. È quella coerente con la decisione che stiamo cercando di prendere.**
