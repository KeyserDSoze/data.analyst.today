## 1.6 L'AI riduce il costo dell'esecuzione, non quello dell'errore

L'intelligenza artificiale generativa introduce un cambiamento economico importante nel lavoro analitico: abbassa il costo marginale di molte attività.

Scrivere una prima versione di una query SQL può richiedere pochi secondi. Lo stesso vale per una formula DAX, uno script Python, una spiegazione di una regressione o una bozza di visualizzazione.

Questo permette a un analista di esplorare più ipotesi, iterare più velocemente e automatizzare attività ripetitive.

Ma esiste un effetto collaterale.

Se produrre un'analisi costa meno, costa meno anche produrre un'analisi sbagliata.

### Il paradosso della velocità

Supponiamo che due analisti ricevano la stessa richiesta.

Il primo impiega un'ora per costruire manualmente una query complessa.

Il secondo utilizza un assistente AI e produce dieci varianti della stessa analisi nello stesso tempo.

Se la domanda iniziale è corretta e i dati sono ben compresi, il secondo analista ha un enorme vantaggio.

Se invece la domanda iniziale è sbagliata, il secondo analista può produrre dieci risultati fuorvianti invece di uno.

La produttività tecnica non coincide quindi con la qualità analitica.

### Una query corretta può rispondere alla domanda sbagliata

Immaginiamo che venga chiesto:

> "Qual è il prodotto più redditizio?"

L'AI genera rapidamente:

```sql
SELECT product_id, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 1;
```

La query può essere perfettamente valida.

Ma `revenue` non è `profit`.

Per rispondere alla domanda servono probabilmente costi diretti, sconti, resi, costi logistici e forse una logica di allocazione dei costi indiretti.

Il problema non è SQL.

Il problema è la semantica.

### Verificare diventa una competenza primaria

Con l'aumento della capacità degli strumenti AI, il ruolo dell'analista si sposta progressivamente dalla produzione manuale alla supervisione.

Dobbiamo verificare almeno quattro livelli:

1. **Intento:** l'analisi risponde alla domanda corretta?
2. **Semantica:** metriche, dimensioni e filtri rappresentano ciò che pensiamo?
3. **Tecnica:** query, formule e trasformazioni sono implementate correttamente?
4. **Interpretazione:** le conclusioni sono realmente supportate dall'evidenza?

Saltare uno di questi livelli può produrre una risposta apparentemente convincente ma sbagliata.

### Il caso dei sistemi BI con AI

La documentazione Microsoft su Copilot per i modelli semantici in Power BI è particolarmente utile perché esplicita un principio generale: senza preparazione dei dati, del modello e degli utenti, gli output possono essere di bassa qualità, inaccurati o fuorvianti. Microsoft raccomanda inoltre di testare il comportamento del modello e di addestrare gli utenti a valutare criticamente gli output.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

La documentazione sulla preparazione dei dati per l'AI insiste sullo stesso punto: contesto aziendale, terminologia e struttura semantica riducono l'ambiguità ma non eliminano la natura non deterministica del sistema.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

### Il nuovo collo di bottiglia

Per molti anni il collo di bottiglia dell'analytics è stato l'esecuzione tecnica.

Non sapevi SQL? Non potevi interrogare direttamente il database.

Non sapevi programmare? Alcune analisi erano difficili da automatizzare.

Non conoscevi lo strumento BI? Costruire report richiedeva supporto specialistico.

L'AI riduce parte di queste barriere.

Il collo di bottiglia si sposta quindi verso competenze più difficili da automatizzare completamente:

- formulare bene il problema;
- comprendere il dominio;
- definire metriche coerenti;
- riconoscere dati inaffidabili;
- valutare causalità e confondenti;
- stimare l'incertezza;
- verificare gli output;
- collegare il risultato a una decisione.

In altre parole, più diventa facile produrre analisi, più diventa prezioso saper giudicare quali analisi meritano fiducia.
