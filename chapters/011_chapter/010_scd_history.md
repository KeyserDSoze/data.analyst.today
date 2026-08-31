## 11.9 Slowly Changing Dimensions: quando il passato deve restare passato

Le dimensioni descrivono entità: clienti, prodotti, territori, dipendenti, account, negozi.

Ma le entità cambiano.

Un cliente cambia segmento. Un venditore cambia regione. Un prodotto cambia categoria. Un punto vendita cambia area commerciale.

La domanda è: **quando analizziamo il passato, vogliamo usare la classificazione di oggi o quella che era valida allora?**

Questa non è una scelta tecnica. È una scelta analitica.

### Type 1: sovrascrivere il passato

Con una Slowly Changing Dimension di tipo 1, quando un attributo cambia, il valore precedente viene sovrascritto.

È appropriato quando il vecchio valore era semplicemente sbagliato oppure quando non interessa mantenere la storia.

Esempio:

`customer_name = "Acme Srl"`

viene corretto in:

`customer_name = "ACME S.p.A."`

Se si tratta di una correzione anagrafica, mantenere la vecchia grafia può non avere valore analitico.

### Type 2: conservare versioni storiche

Con una SCD Type 2, ogni cambiamento rilevante produce una nuova riga della dimensione.

Una struttura tipica può contenere:

```text
customer_sk
customer_id
segment
valid_from
valid_to
is_current
```

Per esempio:

| customer_sk | customer_id | segment | valid_from | valid_to | is_current |
|---:|---:|---|---|---|---|
| 4102 | C884 | SMB | 2024-01-01 | 2025-09-30 | false |
| 9177 | C884 | Enterprise | 2025-10-01 | 9999-12-31 | true |

Microsoft descrive proprio il Type 2 come un pattern in cui, quando un attributo dimensionale cambia, viene creata una nuova versione della riga mentre quella precedente viene mantenuta, così da preservare la storia e poter ricostruire lo stato del dato in un determinato momento.[^ms-scd2]

### Caso realistico: il segmento Enterprise che sembrava aver triplicato le vendite

**NovaParts**, distributore industriale, presenta questo risultato:

- vendite Enterprise 2024: €18,2M;
- vendite Enterprise 2025: €31,7M;
- crescita: +74%.

Il management conclude che la strategia Enterprise funziona in modo straordinario.

L'analista controlla il modello e scopre che `dim_customer` contiene solo il segmento corrente.

Nel 2025 molte aziende sono state riclassificate da Mid-Market a Enterprise dopo aver superato una soglia di fatturato.

La query storica:

```sql
SELECT
    d.segment,
    SUM(f.revenue)
FROM fact_sales f
JOIN dim_customer d
  ON f.customer_id = d.customer_id
GROUP BY 1;
```

attribuisce retroattivamente anche le vendite 2024 di quei clienti al segmento Enterprise.

Dopo una ricostruzione point-in-time con SCD Type 2:

- Enterprise 2024: €24,9M;
- Enterprise 2025: €31,7M;
- crescita reale comparabile: +27%.

La crescita rimane positiva, ma la storia strategica cambia completamente.

### Business key e surrogate key

La business key identifica l'entità nel sistema sorgente:

`customer_id = C884`

La surrogate key identifica una specifica versione storica:

`customer_sk = 4102` oppure `9177`.

Le fact table storiche dovrebbero tipicamente puntare alla surrogate key appropriata per il momento dell'evento.

Così una vendita del 2024 rimane collegata alla versione `SMB`, mentre una vendita del 2026 può essere collegata alla versione `Enterprise`.

### Il join point-in-time

Quando si ricostruisce la chiave dimensionale durante un load, la logica concettuale è:

```sql
fact.event_date >= dim.valid_from
AND fact.event_date < dim.valid_to
```

Il dettaglio delle convenzioni su estremi inclusivi/esclusivi varia, ma deve essere coerente e testato.

### Type 1 e Type 2 possono convivere

Non tutti gli attributi della stessa dimensione devono avere la stessa politica.

Per un cliente:

- correzione typo nel nome → Type 1;
- segmento commerciale → Type 2;
- account manager → forse Type 2;
- email di contatto → dipende dal caso d'uso.

### Domanda operativa

Per ogni attributo chiedere:

> Se questo valore cambia domani, voglio che anche i report di ieri cambino?

Se la risposta è no, probabilmente serve storia.

[^ms-scd2]: Microsoft Learn, *Slowly changing dimension type 2*, https://learn.microsoft.com/en-us/fabric/data-factory/slowly-changing-dimension-type-two
