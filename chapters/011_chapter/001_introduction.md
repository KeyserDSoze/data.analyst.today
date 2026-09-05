# Capitolo 11 — SQL, trasformazione del dato e data modeling per l’analisi

## 11.0 Una query può essere corretta e il numero può essere sbagliato

SQL viene spesso insegnato come una sequenza di costrutti — `SELECT`, `JOIN`, `GROUP BY`, funzioni finestra, CTE — ma nel lavoro reale la difficoltà più importante viene prima della sintassi. Una query può essere valida, veloce, produrre numeri plausibili e alimentare una dashboard perfettamente funzionante, e tuttavia rispondere alla domanda sbagliata.

Succede quando durante la trasformazione cambia silenziosamente il significato del dato. Una riga per ordine diventa più righe dopo un join; un `INNER JOIN` elimina dal denominatore chi non ha avuto un evento; una data di ordine sostituisce una data di competenza; una dimensione corrente riscrive retroattivamente il passato; uno stock viene sommato nel tempo come se fosse un flusso; una deduplicazione sceglie arbitrariamente quale versione sopravvive; un modello incrementale dimentica refund o rettifiche tardive.

Il principio guida del capitolo è quindi questo:

> **SQL non serve soltanto a interrogare tabelle. Serve a rendere eseguibile una definizione analitica senza modificarne il significato lungo il percorso.**

### Aurora Market: 3,8 milioni di euro apparsi dal nulla

Aurora Market, marketplace europeo di prodotti per la casa, prepara il board meeting trimestrale. Il dashboard commerciale mostra revenue Q2 pari a **48,6 milioni di euro**; Finance chiude invece il trimestre a **44,8 milioni**. La differenza è troppo grande per essere attribuita ad arrotondamenti o timing di chiusura.

La query del dashboard contiene un join apparentemente innocuo:

```sql
SELECT
    SUM(ol.quantity * ol.unit_price) AS revenue
FROM orders o
JOIN order_lines ol
    ON o.order_id = ol.order_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_date >= DATE '2026-04-01'
  AND o.order_date <  DATE '2026-07-01';
```

Il problema non è `SUM`. È il grain delle sorgenti:

| tabella | grain |
|---|---|
| `orders` | una riga per ordine |
| `order_lines` | una riga per linea d’ordine |
| `payments` | una riga per movimento di pagamento |

Un ordine con quattro linee e due movimenti di pagamento diventa otto righe. Il valore delle linee viene ripetuto due volte. La query calcola correttamente ciò che il join le ha consegnato; è la rappresentazione costruita prima dell’aggregazione a essere sbagliata.

Questo esempio contiene quasi tutto il capitolo. Prima di scrivere codice dobbiamo sapere quale entità stiamo rappresentando, quale grain deve avere l’output, quali chiavi sono uniche, quali relazioni moltiplicano righe, quale popolazione deve sopravvivere, quale tempo appartiene alla domanda e quali misure possono essere aggregate senza perdere significato.

### L’Analytical Data Contract

Per rendere queste scelte verificabili useremo un **Analytical Data Contract**. Non è un contratto legale e non richiede un prodotto specifico: è una specifica condivisa che rende esplicite le proprietà che una trasformazione deve preservare.

| Campo | Domanda |
|---|---|
| Business entity | Che cosa rappresentiamo: ordine, cliente, sessione, contratto, evento? |
| Grain | Che cosa rappresenta esattamente una riga? |
| Keys | Quali colonne identificano univocamente una riga o entità? |
| Expected cardinality | Cosa ci aspettiamo da ogni join: 1:1, 1:N, N:M? |
| Population semantics | Chi o cosa entra nel dataset e chi resta fuori? |
| Time semantics | Quale timestamp/data determina appartenenza al periodo e validità storica? |
| Metric semantics | Quali componenti, esclusioni e denominatori definiscono la metrica? |
| Transformation path | Quali cambi di grain avvengono tra sorgente e output? |
| Quality invariants | Quali proprietà devono restare vere dopo ogni trasformazione? |
| Refresh / latency | Quanto deve essere aggiornato il dato? |
| Cost / performance | Quanto costa produrlo e a quale frequenza? |
| Lineage / owner | Da dove arriva e chi risponde della definizione? |

Il contratto non sostituisce SQL. Rende SQL revisionabile da chi non ha scritto la query e permette di trasformare le assunzioni più importanti in test.

Il percorso operativo costruito fin qui nel libro diventa:

```text
Analytical Brief
→ Data Readiness Review
→ Analytical Data Contract
→ dataset analitico
→ analisi / modello / dashboard
```

L’**Analytical Brief** definisce quale realtà vogliamo conoscere e quale decisione supportare. La **Data Readiness Review** verifica se le fonti possono sostenere quella pretesa. L’**Analytical Data Contract** specifica come trasformare quelle fonti senza perdere la semantica necessaria. Questo ultimo passaggio è essenziale perché proprio durante join, filtri, aggregazioni, storicizzazione e incrementalità una definizione apparentemente stabile può cambiare.

### Il confine con i capitoli vicini

Il Capitolo 3 chiedeva se i dati fossero adatti alla domanda. Questo capitolo chiede come trasformarli preservandone il significato. Il Capitolo 12 allargherà ancora l’inquadratura: quale architettura produce, trasporta e serve queste trasformazioni con freshness, recovery, sicurezza e costi adeguati?

L’obiettivo non è quindi “saper scrivere query complesse”. È poter difendere una frase più forte:

> **So che questo numero rappresenta ciò che diciamo che rappresenta, e posso mostrare dove grain, popolazione, tempo e metrica vengono preservati nel codice e nei test.**

L’AI rende questa disciplina ancora più importante. Un assistente può generare in pochi secondi un join sintatticamente perfetto; non può decidere da solo che cosa significhi `revenue Q2`, quale versione storica di un cliente usare o quale denominatore il business intenda, se queste informazioni non sono state rese esplicite.

### Riferimenti

Microsoft Learn, *Understand star schema and the importance for Power BI*: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

Databricks, *Model metric views*: https://docs.databricks.com/aws/en/uc-semantics/metric-views/basic-modeling
