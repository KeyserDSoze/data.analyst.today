## 11.5 Fact, dimension e star schema: progettare un modello che protegga il significato

I sistemi operativi sono progettati per far funzionare processi. I modelli analitici sono progettati per rendere quei processi interrogabili.

Le due esigenze non coincidono.

Un CRM può essere perfettamente normalizzato per aggiornare account, contatti, contratti, indirizzi e preferenze. Copiare quella struttura direttamente in una dashboard può però costringere ogni analyst a ricostruire la stessa semantica attraverso molti join fragili.

Lo **star schema** separa due ruoli:

- **fact tables** — eventi, transazioni, snapshot o misure;
- **dimension tables** — contesto descrittivo con cui filtrare, raggruppare e interpretare i fatti.

Microsoft Learn sottolinea che, nei modelli dimensionali, le dimensioni servono tipicamente a filtrare e raggruppare mentre le fact vengono riepilogate; raccomanda inoltre che le fact table abbiano un grain coerente.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

### Il modello non inizia dalle tabelle: inizia dal processo di business

Prima domanda:

> quale processo stiamo misurando?

Esempi:

- vendita;
- pagamento;
- spedizione;
- utilizzo prodotto;
- subscription lifecycle;
- inventario;
- ticket di supporto.

Poi definiamo il grain della fact:

> `fact_sales`: una riga per linea di vendita confermata.

> `fact_subscription_events`: una riga per evento contrattuale.

> `fact_inventory_snapshot`: una riga per prodotto-magazzino-giorno a fine giornata.

Solo dopo scegliamo dimensioni e misure.

### Caso simulato/composito — Meridian Retail e il mart che copiava l’ERP

Meridian Retail ha 180 negozi e un e-commerce europeo.

Il primo data mart commerciale copia quasi integralmente l’ERP. Per ottenere revenue mensile per categoria e regione servono join tra nove tabelle operative.

Dopo pochi mesi emergono tre problemi:

1. dashboard differenti assegnano negozi a regioni diverse;
2. categorie prodotto storiche vengono reinterpretate con la classificazione corrente;
3. alcune query duplicano revenue attraverso relazioni molti-a-molti.

Il team ridisegna il modello:

```text
                 dim_date
                    |
dim_store --- fact_sales --- dim_product
                    |
               dim_customer
```

`fact_sales` ha una riga per linea di vendita confermata e conserva misure atomiche come:

- quantity;
- gross revenue;
- discount amount;
- return amount quando attribuibile;
- net revenue;
- cost.

Le dimensioni forniscono il contesto business.

Il vantaggio non è soltanto una query più corta. È che lo stesso processo viene rappresentato con un **grain e relazioni condivise**.

### Event fact e snapshot fact rispondono a domande diverse

Per l’inventario possiamo avere:

**event fact**

```text
+10 ricezione
-3 vendita
-1 danneggiato
```

oppure:

**periodic snapshot**

```text
2026-08-01 → stock 84
2026-08-02 → stock 80
2026-08-03 → stock 91
```

Gli eventi descrivono i movimenti.

Gli snapshot descrivono lo stato a un momento.

Le due strutture possono coesistere, ma non sono intercambiabili.

Se sommiamo stock giornaliero nel tempo, stiamo trattando uno stato come un flusso.

### La dimensione tempo non è una sola data

Una vendita può avere:

- `order_date`;
- `payment_date`;
- `ship_date`;
- `delivery_date`;
- `recognition_date`;
- `return_date`.

Queste date non sono duplicati tecnici. Rappresentano eventi business differenti.

Un modello dimensionale robusto deve permettere di rispondere a domande come:

> revenue ordinato questo mese?

> cash incassato questo mese?

> revenue riconosciuto questo mese?

senza fingere che siano la stessa metrica temporale.

### Dimensioni correnti e dimensioni storiche

Supponiamo che un prodotto passi dalla categoria `Accessories` a `Premium Accessories`.

Esistono almeno due domande legittime:

1. come classificheremmo oggi le vendite storiche?
2. come era classificato il prodotto quando la vendita avvenne?

Se sovrascriviamo semplicemente il valore corrente, la seconda domanda diventa impossibile.

Le Slowly Changing Dimensions servono proprio a preservare, quando necessario, versioni storiche degli attributi.

Microsoft Learn include le slowly changing dimensions tra i concetti chiave del modeling a stella e mostra il ruolo delle surrogate keys nel distinguere versioni diverse della stessa entità business.

### Surrogate key e business key

Una fact può conservare:

```text
customer_sk = 912837
```

mentre la business key resta:

```text
customer_id = C10482
```

Se il segmento del cliente cambia nel tempo, due versioni della dimensione possono condividere `customer_id` ma avere surrogate key differenti.

La fact storica punta così alla versione valida nel momento dell’evento.

Il beneficio analitico è importante:

> il contesto storico non viene ricostruito accidentalmente usando lo stato corrente.

### Star schema non significa “una tabella larga per tutto”

Una tabella unica può sembrare comoda, ma può introdurre:

- attributi ripetuti su milioni di righe;
- logiche di aggiornamento duplicate;
- difficoltà nel preservare storia;
- inconsistenze tra domini;
- misure a grain differenti nello stesso dataset.

Il modello dimensionale cerca invece un confine leggibile tra:

```text
fatto osservato
+
contesto dell’osservazione
```

### Il grain della fact è un contratto di aggregazione

Se `fact_sales` è una riga per linea di vendita, allora possiamo chiedere:

- revenue per prodotto;
- revenue per negozio;
- unità per giorno;
- margine per categoria.

Ma non possiamo inserire nella stessa riga, senza cautela, metriche che esistono a grain ordine o cliente e poi sommarle come se fossero line-level.

Il modello fisico deve rendere difficile commettere errori semantici comuni, non soltanto possibile ottenere il risultato corretto.

### Star schema nell’Analytical Data Contract

Per ogni fact importante documentiamo:

| Campo | Esempio |
|---|---|
| processo | vendita |
| grain | linea di vendita confermata |
| business key | `order_id + line_number` |
| date roles | order, payment, ship, recognition |
| misure additive | quantity, net revenue, cost |
| semi/non additive | margin %, unit price medio |
| dimensioni | date, product, store, customer |
| history policy | categoria prodotto as-of vendita |
| late-arriving policy | aggiornamento dimensionale/reconciliation |

> **Il modello dati migliore non è quello che riproduce fedelmente il database operativo. È quello che rende semplici, coerenti e verificabili le domande analitiche importanti.**
