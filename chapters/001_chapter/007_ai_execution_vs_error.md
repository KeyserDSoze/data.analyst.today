## 1.6 L'AI riduce il costo dell'esecuzione, non quello dell'errore

Il Capitolo 0 ha già stabilito il principio di responsabilità con cui useremo l'AI. Qui non serve ripeterlo. Ci interessa una conseguenza più specifica per il metodo analitico:

> **quando produrre un calcolo diventa più economico, non diventa più economica una decisione sbagliata presa sulla base di quel calcolo.**

La distinzione sembra ovvia, ma cambia il punto in cui dobbiamo concentrare l'attenzione.

### Una query può essere corretta e rispondere alla domanda sbagliata

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

La query può essere sintatticamente valida, eseguirsi senza errori e ordinare correttamente i risultati. Eppure non sappiamo ancora se abbia risposto alla domanda.

`revenue` non significa `profit`. Per parlare di redditività potrebbero servire costo del prodotto, sconti, resi, logistica, commissioni, costi variabili e regole di allocazione. Il fallimento non è nell'SQL. Nasce dal passaggio non verificato tra un concetto di business — **redditività** — e una variabile disponibile — **revenue**.

L'AI rende questo tipo di errore particolarmente interessante perché può rendere impeccabile l'implementazione di un'idea sbagliata. Più il codice appare professionale, più diventa facile smettere di interrogare la semantica che lo precede.

### Quattro livelli di correttezza

Quando valutiamo un artefatto analitico conviene separare quattro livelli, perché un controllo che funziona su uno non protegge automaticamente dagli altri.

| Livello | Domanda di controllo | Esempio di fallimento |
|---|---|---|
| **Intento** | Stiamo rispondendo al problema giusto? | ottimizziamo revenue quando la decisione riguarda profitto |
| **Semantica** | Metriche, popolazioni, date e filtri significano ciò che crediamo? | `customer` identifica account invece di persone |
| **Implementazione** | Query, formule e trasformazioni realizzano correttamente la definizione? | un join many-to-many duplica gli importi |
| **Interpretazione** | La conclusione è proporzionata all'evidenza? | trasformiamo un'associazione in una causa |

Un test automatico può dimostrare che la query è valida e lasciare completamente irrisolto l'intento. Una code review può trovare il join sbagliato e non accorgersi che la metrica è stata definita sulla popolazione sbagliata. Un numero può riconciliare perfettamente e tuttavia essere usato per una conclusione che i dati non sostengono.

Per questo il collo di bottiglia non scompare quando il codice viene generato più velocemente. **Si sposta verso la qualità della domanda, della semantica e della verifica.**

### Dove approfondiremo l'AI

Il rapporto operativo con agenti, controlli, stop condition e accountability è trattato nel **Capitolo 0 — Al timone**. Il **Capitolo 14 — AI-assisted analytics** entrerà invece nei workflow tecnici: prompting, SQL e Python generati, EDA, debugging, privacy, valutazione e auditabilità.

Qui manteniamo soltanto la regola necessaria per comprendere il mestiere:

> **l'automazione può diminuire il costo di produrre una risposta; non diminuisce automaticamente il costo di credere alla risposta sbagliata.**
