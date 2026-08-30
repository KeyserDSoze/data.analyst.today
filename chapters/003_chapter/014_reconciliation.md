## 3.13 Riconciliazione: quando due sistemi raccontano numeri diversi

Una delle situazioni più comuni nel lavoro reale è questa: due report mostrano numeri diversi per la stessa metrica.

Il problema non è necessariamente che uno dei due sia sbagliato. Spesso i sistemi stanno usando definizioni diverse, finestre temporali diverse o fonti diverse.

### Caso simulato: il fatturato che non coincide

Una società retail riceve ogni mattina due report:

- il gestionale ERP riporta **€1.842.310** di vendite nette nel mese;
- il dashboard commerciale riporta **€1.917.480**.

La differenza è di **€75.170**, circa il 4,1%.

Il primo impulso potrebbe essere cercare un bug nella pipeline.

L'analista ricostruisce invece il percorso delle due metriche.

Scopre che:

1. l'ERP contabilizza il ricavo alla data di spedizione;
2. il dashboard attribuisce il ricavo alla data dell'ordine;
3. l'ERP esclude ordini annullati prima della spedizione;
4. il dashboard li rimuove solo quando lo stato viene aggiornato;
5. il dashboard include il contributo spedizione, mentre il report contabile no;
6. alcuni resi del mese precedente sono stati contabilizzati nel mese corrente.

La riconciliazione non consiste quindi nel forzare i due numeri a coincidere. Consiste nel capire **perché differiscono**.

### Una procedura pratica di riconciliazione

Quando due numeri non coincidono, procedi per livelli:

1. **Definizione** — la metrica significa davvero la stessa cosa?
2. **Popolazione** — vengono incluse le stesse righe?
3. **Tempo** — viene usata la stessa data di riferimento?
4. **Granularità** — si sta aggregando allo stesso livello?
5. **Stati** — cancellazioni, resi e rettifiche sono trattati allo stesso modo?
6. **Valuta e tasse** — importi lordi o netti? conversioni a quale cambio?
7. **Aggiornamento** — i sistemi sono sincronizzati nello stesso momento?
8. **Trasformazioni** — ci sono filtri o join che cambiano la popolazione?

### La reconciliation table

Una tecnica molto utile è costruire una tabella che scompone la differenza.

| Voce | Impatto |
|---|---:|
| Totale dashboard | €1.917.480 |
| Ordini non ancora spediti | -€31.800 |
| Spese di spedizione | -€19.420 |
| Cancellazioni tardive | -€8.650 |
| Resi contabilizzati nel mese | -€15.300 |
| Totale ERP | €1.842.310 |

Questo tipo di tabella ha un valore enorme perché trasforma una discussione del tipo "il dato è sbagliato" in una spiegazione verificabile.

### Lezione operativa

> Se due sistemi mostrano numeri diversi, non scegliere subito quale sia quello giusto. Prima ricostruisci le regole con cui ciascun numero è stato prodotto.

La riconciliazione è una delle competenze più sottovalutate di un Data Analyst, perché costringe a conoscere insieme semantica, processo di business, pipeline e struttura del dato.
