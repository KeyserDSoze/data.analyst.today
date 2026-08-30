## 3.12 Caso studio end-to-end — Il dataset che sembrava pronto

Questo caso riassume molti dei concetti del capitolo.

> **Nota:** il caso è simulato, ma costruito per riprodurre problemi realistici di un progetto analytics.

### La richiesta

La società immaginaria **LuceNova Home**, e-commerce di illuminazione e arredamento, vuole capire perché il tasso di riacquisto a 90 giorni è diminuito.

Il responsabile CRM consegna all'analista tre file:

- `customers.csv`
- `orders.csv`
- `order_items.csv`

La richiesta sembra semplice:

> "Confronta i clienti acquisiti quest'anno con quelli dell'anno scorso e dimmi perché tornano meno."

Il primo impulso potrebbe essere aprire Python, fare qualche join e calcolare la retention.

L'analista sceglie invece di capire prima i dati.

### Passo 1 — Quante righe abbiamo?

```text
customers.csv      1.284.410 righe
orders.csv         3.918.771 righe
order_items.csv   11.705.442 righe
```

Il numero sembra plausibile.

Poi controlla le chiavi.

```text
customers: 1.241.882 customer_id distinti
orders:    3.901.114 order_id distinti
```

Ci sono quindi decine di migliaia di identificatori duplicati.

### Passo 2 — Il duplicato clienti

Analizzando `customers`, emerge che molti clienti compaiono più volte perché il CRM mantiene una nuova riga a ogni modifica del profilo.

Una cliente, per esempio, compare così:

```text
customer_id | email                  | city     | updated_at
C81922      | sara@example.com       | Torino   | 2025-01-10
C81922      | sara@example.com       | Milano   | 2025-09-02
C81922      | sara@example.com       | Milano   | 2026-02-14
```

Non sono tre clienti.

Sono tre versioni dello stesso cliente.

La tabella è una slowly changing history, non una semplice anagrafica corrente.

### Passo 3 — Gli ordini duplicati

In `orders`, una parte dei duplicati deriva da un bug di ingestion avvenuto per due settimane.

Le righe duplicate hanno lo stesso `order_id` ma `ingested_at` differente.

Se non corretto, il fatturato del periodo risulta sovrastimato del 2,8%.

### Passo 4 — Il significato di `order_date`

La colonna `order_date` sembra ovvia.

Non lo è.

Per gli ordini più vecchi rappresenta la data di creazione del carrello confermato. Dopo una migrazione del 2025 rappresenta invece la data del pagamento autorizzato.

Il cambiamento di definizione crea uno slittamento temporale particolarmente visibile nei periodi promozionali.

### Passo 5 — Il cliente senza cliente

Il 14% degli ordini possiede `customer_id = NULL`.

Il team CRM sostiene che si tratti di guest checkout.

L'analista verifica e scopre che il campo email è disponibile nel 92% di questi ordini.

Quindi parte degli acquisti apparentemente anonimi può essere ricondotta a clienti esistenti attraverso una procedura di identity resolution.

Ma attenzione: un'email non equivale sempre a una persona.

Famiglie, account condivisi e indirizzi aziendali possono produrre falsi match.

### Passo 6 — Il reso che sembra un acquisto

In `order_items`, i resi vengono registrati come quantità negative.

```text
order_id | sku      | quantity | unit_price
A1001    | LAMP-44  | 1        | 120.00
A1001    | LAMP-44  | -1       | 120.00
```

Se si conta semplicemente il numero di righe o di SKU, il reso può sembrare una seconda attività di acquisto.

### Passo 7 — La retention era davvero diminuita?

Dopo aver ricostruito:

- cliente corrente;
- identità cliente;
- ordini unici;
- regole temporali coerenti;
- ordini cancellati;
- resi;
- finestra di osservazione completa;

il risultato cambia.

La dashboard iniziale mostrava una riduzione del repeat purchase rate a 90 giorni dal 28,4% al 22,1%.

La misura corretta mostra invece:

```text
Cohort 2025: 27,6%
Cohort 2026: 25,9%
```

Il peggioramento esiste, ma è molto inferiore a quanto sembrasse.

A quel punto l'analisi può finalmente cominciare.

### Il punto del caso

Per arrivare alla domanda interessante — **perché i clienti tornano meno?** — è stato necessario prima risolvere domande molto meno glamour:

- cosa rappresenta una riga?
- qual è la chiave?
- quali record sono duplicati?
- che cosa significa NULL?
- quale data stiamo usando?
- come vengono rappresentati i resi?
- possiamo identificare correttamente un cliente?
- la finestra temporale è comparabile?

Questo è uno dei paradossi del lavoro analitico.

Le conclusioni strategiche dipendono spesso da dettagli tecnici apparentemente banali.

### Checklist del caso

Prima di dichiarare un dataset "pronto", verifica almeno:

- [ ] unità di analisi;
- [ ] granularità;
- [ ] chiavi e cardinalità;
- [ ] duplicati tecnici e semantici;
- [ ] missing values;
- [ ] tipi e domini;
- [ ] valori impossibili e outlier;
- [ ] copertura temporale;
- [ ] significato dei timestamp;
- [ ] eventi di cancellazione e rettifica;
- [ ] lineage;
- [ ] cambiamenti di definizione nel tempo;
- [ ] riconciliazione con almeno una fonte indipendente.

Solo dopo questa fase il dataset diventa una base credibile per l'analisi.