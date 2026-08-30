## 3.1 Osservazioni, variabili e unità di analisi

Ogni dataset tabellare può essere letto attraverso due domande fondamentali:

1. che cosa rappresenta ogni riga?
2. che cosa rappresenta ogni colonna?

Le righe sono normalmente **osservazioni**. Le colonne sono **variabili** o attributi dell'osservazione. Ma questa definizione diventa utile solo quando specifichiamo l'unità di analisi.

Consideriamo una tabella con queste colonne:

| order_id | customer_id | product_id | quantity | price |
|---|---|---|---:|---:|
| 1001 | C17 | P8 | 2 | 35.00 |
| 1001 | C17 | P4 | 1 | 12.00 |

Se guardiamo superficialmente la tabella potremmo dire che contiene ordini. Ma `order_id = 1001` compare due volte. La vera unità di osservazione non è quindi l'ordine: è probabilmente **la riga d'ordine**, cioè la combinazione tra ordine e prodotto acquistato.

Questa distinzione modifica immediatamente i calcoli.

Se facciamo:

```sql
SELECT COUNT(*) FROM order_lines;
```

stiamo contando righe d'ordine, non ordini.

Per contare gli ordini potremmo avere bisogno di:

```sql
SELECT COUNT(DISTINCT order_id) FROM order_lines;
```

Lo stesso principio vale in qualsiasi dominio. Una riga può rappresentare:

- un cliente;
- una transazione;
- una visita web;
- una sessione;
- una riga di fattura;
- un prodotto in un magazzino in un dato giorno;
- una misurazione di un sensore;
- una risposta a un questionario;
- un ticket di assistenza;
- uno stato di un'entità in un determinato momento.

Prima di aggregare qualsiasi dato, l'analista deve poter completare senza esitazione la frase:

> **Una riga di questa tabella rappresenta...**

Se la risposta non è chiara, non è ancora il momento di analizzare.

### La variabile non è solo il tipo tecnico

Una colonna può essere `INTEGER`, `VARCHAR`, `DATE` o `BOOLEAN`, ma il tipo tecnico non ci dice ancora il suo significato analitico.

`age = 37` può rappresentare l'età al momento della registrazione, l'età attuale calcolata oggi o l'età al momento dell'acquisto.

`status = active` può significare che il cliente ha un abbonamento pagante, che ha effettuato login negli ultimi trenta giorni o semplicemente che non è stato cancellato dal database.

Per questo ogni variabile importante dovrebbe essere compresa lungo almeno quattro dimensioni:

- significato di business;
- tipo tecnico;
- dominio dei valori possibili;
- momento o processo con cui viene prodotta.

La prima competenza di data understanding consiste quindi nel passare dalla struttura fisica della tabella alla sua struttura semantica.
