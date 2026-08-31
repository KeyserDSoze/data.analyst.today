## 11.18 Esercizi: SQL e data modeling come ragionamento

Gli esercizi di questo capitolo non chiedono soltanto di scrivere query. Chiedono di decidere **cosa dovrebbe significare la query**.

### Esercizio 1 — Revenue duplicata

Una tabella `orders` contiene una riga per ordine. Una tabella `payments` può contenere più transazioni per ordine.

Dopo un join diretto, la revenue cresce del 12%.

Domande:

1. Qual è il grain delle due tabelle?
2. Perché il join può moltiplicare la revenue?
3. Come verificheresti la cardinalità prima e dopo il join?
4. Quale modello intermedio costruiresti?
5. In quali casi sarebbe corretto mantenere più righe per ordine?

### Esercizio 2 — Il paese storico

Un cliente vive in Italia nel 2024 e si trasferisce in Francia nel 2025.

La dimensione cliente contiene solo il paese corrente.

Il management chiede:

> Quanto revenue abbiamo generato in Italia nel 2024?

Spiega perché un join alla dimensione corrente può riscrivere il passato e progetta una soluzione point-in-time.

### Esercizio 3 — Deduplicazione

La tabella raw contiene:

```text
customer_id | status   | updated_at
C1          | trial    | 10:00
C1          | active   | 12:00
C1          | active   | 12:00
```

Definisci almeno tre possibili grain analitici e spiega come cambierebbe la deduplicazione in ciascun caso.

### Esercizio 4 — Repeat Purchase Rate

Definizione richiesta:

> quota di clienti che effettuano un secondo acquisto valido entro 60 giorni dal primo acquisto valido.

Scrivi prima la specifica semantica, senza SQL:

- grain;
- definizione di cliente;
- primo acquisto;
- acquisto valido;
- finestra temporale;
- trattamento dei refund;
- guest checkout;
- timezone.

Solo dopo proponi la struttura della query.

### Esercizio 5 — Costi cloud

Un analyst esegue ogni ora:

```sql
SELECT *
FROM fact_events
LIMIT 1000;
```

La tabella è molto grande e non clusterizzata.

Spiega perché `LIMIT 1000` potrebbe non ridurre il costo della scansione in un motore come BigQuery e proponi alternative più sicure per esplorare i dati.

### Esercizio 6 — Modello incrementale

Gli ordini vengono creati oggi, ma:

- il 70% dei refund arriva entro 7 giorni;
- il 95% entro 30 giorni;
- alcuni chargeback arrivano dopo 90 giorni.

Progetta una strategia incrementale indicando:

- colonna di aggiornamento;
- lookback window;
- merge key;
- gestione dei casi oltre finestra;
- riconciliazione con Finance;
- politica di full refresh.

### Esercizio 7 — AI-generated SQL

Un assistente genera una query che calcola churn per piano tariffario.

La query compila e restituisce numeri plausibili.

Costruisci una review checklist specifica per verificare:

- definizione di churn;
- grain account vs subscription;
- cancellazioni e riattivazioni;
- date;
- piano corrente vs piano al momento del churn;
- join;
- denominatore;
- clienti censurati.

### Esercizio 8 — Many-to-many

Un ordine può avere tre coupon e due campagne attribuite.

Un join diretto tra ordini, coupon e campagne produce fino a sei righe per ordine.

Progetta un modello che permetta di analizzare:

1. utilizzo coupon;
2. attribution marketing;
3. revenue totale senza duplicazioni.

Spiega quando useresti bridge separate e quando un peso di allocazione.

### Esercizio 9 — Il dashboard che migliora troppo

Da un giorno all'altro:

- conversion rate: 4,1% → 5,3%;
- ordini: quasi invariati;
- sessioni: -23%;
- revenue: +1%.

Elenca le prime dieci verifiche che faresti prima di comunicare un miglioramento reale della conversione.

### Esercizio 10 — Caso da leadership meeting

Sei l'analista responsabile del KPI `on_time_delivery_rate`.

Il COO sostiene che il corriere principale è peggiorato e vuole cambiare fornitore.

Hai 24 ore.

Definisci un piano di analisi che copra:

- definizione esatta di on-time;
- data promessa;
- data effettiva;
- grain shipment vs order;
- split shipment;
- timezone;
- carrier mix;
- prodotto/area geografica;
- cambiamenti recenti nelle promise date;
- riconciliazione con sistemi operativi;
- test di qualità;
- output finale per il COO.

### Sintesi del capitolo

SQL è importante, ma non è il centro del mestiere.

Il centro è la capacità di trasformare una domanda in una rappresentazione affidabile dei dati.

Questo richiede di ragionare su:

**grain → chiavi → join → tempo → storia → qualità → costo → riuso → verifica**.

Quando questi elementi sono corretti, spesso la query finale diventa sorprendentemente semplice.

Quando sono sbagliati, anche la query più sofisticata può produrre una risposta molto convincente alla domanda sbagliata.
