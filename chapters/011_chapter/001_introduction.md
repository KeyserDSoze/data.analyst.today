# Capitolo 11 — SQL, trasformazione del dato e data modeling per l’analisi

## 11.0 Una query può essere corretta e il numero può essere sbagliato

SQL viene spesso insegnato come una sequenza di costrutti: `SELECT`, `JOIN`, `GROUP BY`, funzioni finestra, CTE. Sono strumenti necessari, ma non sono il vero problema professionale.

Nel lavoro reale una query può:

- essere sintatticamente valida;
- terminare senza errori;
- produrre numeri plausibili;
- essere veloce;
- alimentare una dashboard perfettamente funzionante;

e tuttavia rispondere alla domanda sbagliata.

Succede quando durante la trasformazione cambia silenziosamente il significato del dato:

- una riga per ordine diventa più righe per ordine dopo un join;
- il denominatore esclude casi che dovrebbero restare nella popolazione;
- la data di ordine viene usata al posto della data di competenza;
- una dimensione corrente viene applicata retroattivamente al passato;
- un saldo viene sommato nel tempo come se fosse un flusso;
- una metrica chiamata `revenue` incorpora una definizione diversa da quella di Finance;
- una deduplicazione sceglie arbitrariamente quale record conservare;
- un modello incrementale dimentica record arrivati in ritardo.

Il principio guida del capitolo è quindi:

> **SQL non serve soltanto a interrogare tabelle. Serve a rendere eseguibile una definizione analitica senza modificarne il significato lungo il percorso.**

### Caso simulato/composito — Aurora Market e i 3,8 milioni di euro apparsi dal nulla

Aurora Market, marketplace europeo di prodotti per la casa, prepara il board meeting trimestrale.

Il dashboard commerciale mostra revenue Q2 pari a **48,6 milioni di euro**. Finance chiude invece il trimestre a **44,8 milioni**.

La differenza è troppo grande per essere attribuita ad arrotondamenti o timing di chiusura.

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

Il modello operativo ha però tre grain differenti:

| tabella | grain |
|---|---|
| `orders` | una riga per ordine |
| `order_lines` | una riga per linea d’ordine |
| `payments` | una riga per movimento di pagamento |

Un ordine con quattro linee e due movimenti di pagamento diventa otto righe dopo il join. Il valore delle linee viene ripetuto due volte.

L’errore non nasce da `SUM`. Nasce prima: il team non ha dichiarato quale entità dovesse esistere una sola volta nel dataset finale.

Questa distinzione è fondamentale perché l’AI rende sempre più economico generare SQL. Un assistente può scrivere il join in pochi secondi. Non può però decidere automaticamente che cosa significhi “revenue Q2” per quell’organizzazione se grain, popolazione, tempo e definizione della metrica non sono espliciti.

### L’Analytical Data Contract

Il deliverable operativo del capitolo sarà l’**Analytical Data Contract**.

Prima che una trasformazione importante diventi una query ricorrente, un modello condiviso o una fonte per dashboard, dovremmo poter compilare almeno questi campi:

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

Il contratto non sostituisce SQL. Rende SQL verificabile.

### Il collegamento con i capitoli precedenti

Il percorso operativo del libro diventa:

```text
Analytical Brief
→ Data Readiness Review
→ Analytical Data Contract
→ dataset analitico
→ analisi / modello / dashboard
```

L’**Analytical Brief** specifica quale domanda dobbiamo supportare.

La **Data Readiness Review** verifica se le fonti sono adatte all’uso previsto.

L’**Analytical Data Contract** stabilisce come trasformare quelle fonti senza perdere il significato necessario alla domanda.

Questa sequenza evita un errore comune: credere che una volta trovate le tabelle “giuste” il problema semantico sia finito. In realtà è proprio durante join, filtri, aggregazioni e storicizzazione che molte definizioni cambiano.

### Le domande che vengono prima del codice

Prima di scrivere una query importante, dovremmo riuscire a rispondere a queste domande:

1. qual è l’entità business che voglio rappresentare?
2. qual è il grain desiderato dell’output?
3. qual è il grain di ogni sorgente?
4. quali chiavi sono uniche e in quale dominio?
5. quale popolazione entra nel calcolo?
6. quale tempo rappresenta la domanda: evento, competenza, stato, validità?
7. quali misure sono additive, semi-additive o non additive?
8. quali join possono moltiplicare righe?
9. quali trasformazioni cambiano il grain?
10. quali invarianti posso testare automaticamente?
11. la metrica esiste già in un layer condiviso?
12. come saprò se la stessa query domani sta ancora calcolando la stessa cosa?

### Il confine con il Capitolo 3 e il Capitolo 12

Questo capitolo non ripete la qualità dei dati del Capitolo 3 e non anticipa l’architettura del Capitolo 12.

- **Capitolo 3:** i dati sono adatti alla domanda?
- **Capitolo 11:** come trasformiamo quei dati preservandone il significato analitico?
- **Capitolo 12:** quale architettura produce, trasporta e serve quelle trasformazioni in modo affidabile e scalabile?

Il risultato a cui puntiamo non è “saper scrivere query complesse”.

È saper difendere questa frase:

> **So che questo numero rappresenta ciò che diciamo che rappresenta, e posso mostrare dove quella semantica viene preservata nel codice e nei test.**

### Riferimenti

Microsoft Learn, *Understand star schema and the importance for Power BI*: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

Databricks, *Model metric views*: https://docs.databricks.com/aws/en/uc-semantics/metric-views/basic-modeling
