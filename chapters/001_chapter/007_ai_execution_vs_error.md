## 1.6 L'AI riduce il costo dell'esecuzione, non quello dell'errore

Il Capitolo 0 ha già stabilito il principio di responsabilità con cui useremo l'AI. Non serve ripeterlo qui in forma estesa.

In questo capitolo ci interessa una sola conseguenza analitica:

> **quando produrre un calcolo diventa più economico, non diventa più economica una decisione sbagliata presa sulla base di quel calcolo.**

### Un esempio minimo

La richiesta è:

> “Qual è il prodotto più redditizio?”

Un assistente genera:

```sql
SELECT product_id, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 1;
```

La query può essere valida.

Ma `revenue` non significa `profit`.

Per rispondere alla domanda potrebbero servire costi del prodotto, sconti, resi, logistica, commissioni e regole di allocazione.

L'errore non nasce dalla sintassi.

Nasce dal passaggio non verificato tra un concetto di business — **redditività** — e una variabile disponibile — **revenue**.

Questa distinzione riapparirà continuamente nel libro.

### Quattro livelli da tenere separati

Quando un sistema AI produce un artefatto analitico, possiamo controllare quattro livelli diversi:

1. **Intento** — stiamo rispondendo alla domanda corretta?
2. **Semantica** — metriche, popolazioni, date e filtri significano ciò che crediamo?
3. **Implementazione** — query, formule e trasformazioni sono corrette?
4. **Interpretazione** — la conclusione è proporzionata all'evidenza?

Un controllo tecnico può validare il terzo livello e lasciare completamente sbagliati i primi due.

Per questo il collo di bottiglia non scompare quando il codice viene generato più velocemente. Si sposta verso la qualità della domanda e della verifica.

### Dove approfondiremo l'AI

Il rapporto operativo con agenti, controlli, stop condition e accountability è trattato nel **Capitolo 0 — Al timone**.

Il **Capitolo 14 — AI-assisted analytics** entrerà invece nei workflow tecnici: prompting, SQL e Python generati, EDA, debugging, privacy, valutazione e auditabilità.

Qui manteniamo soltanto la regola che serve per comprendere il mestiere:

> **l'automazione può diminuire il costo di produrre una risposta; non diminuisce automaticamente il costo di credere alla risposta sbagliata.**
