## 3.15 Controlli automatici: il dato deve dimostrare di essere plausibile

Controllare manualmente un dataset una volta non basta. Se quel dato alimenta ogni giorno dashboard, modelli o decisioni operative, i controlli devono diventare parte del processo.

I controlli automatici non dimostrano che un dato sia vero. Possono però intercettare molte condizioni incompatibili con ciò che ci aspettiamo.

### Cinque famiglie di controlli

**1. Schema checks**

Verificano che colonne, tipi e struttura siano coerenti.

Esempi:

- `order_id` deve esistere;
- `order_date` deve essere una data;
- `revenue` deve essere numerico;
- una colonna critica non deve sparire dopo una release.

**2. Constraint checks**

Verificano regole locali.

Esempi:

- quantità > 0;
- sconto tra 0 e 100%;
- paese in una lista ammessa;
- `order_id` univoco nella tabella ordine.

**3. Referential checks**

Verificano le relazioni tra tabelle.

Esempio: ogni `product_id` presente nelle vendite dovrebbe esistere nella dimensione prodotto, salvo eccezioni note.

**4. Volume e freshness checks**

Controllano se il dataset arriva nei tempi previsti e con volumi plausibili.

**5. Distribution checks**

Confrontano la distribuzione corrente con quella attesa o storica.

### Caso simulato: 420.000 clienti "spariti"

Una società SaaS possiede circa **2,4 milioni di account**. Ogni notte una pipeline aggiorna la tabella clienti usata dal CRM e dai dashboard.

Alle 7:20 di martedì mattina un controllo automatico segnala:

```text
row_count(customer_daily) = 1,981,442
expected range = 2,300,000 - 2,550,000
STATUS: FAIL
```

Il dashboard non è ancora stato consultato dal management.

Il team scopre che una modifica alla query di ingestione ha introdotto accidentalmente un `INNER JOIN` con la tabella dei consensi marketing. Gli account privi di consenso sono quindi scomparsi dal dataset analitico.

Il dato sarebbe sembrato perfettamente plausibile riga per riga. Nessuna colonna era nulla, nessuna chiave duplicata, nessun errore SQL.

Era la popolazione ad essere sbagliata.

Un semplice controllo sul volume ha impedito che il dataset venisse pubblicato.

### Non usare soglie casuali

Un controllo del tipo:

```text
row_count > 0
```

è quasi inutile.

Una pipeline che passa da 2,4 milioni di righe a 12.000 soddisfa comunque il test.

Le soglie devono derivare dal comportamento del processo.

Per un flusso stabile potremmo usare intervalli stretti. Per un business fortemente stagionale potremmo confrontare il volume con lo stesso giorno della settimana o con una baseline dinamica.

### Alert fatigue

Se ogni giorno arrivano cinquanta alert irrilevanti, presto nessuno li leggerà.

Un buon sistema di data quality distingue almeno tra:

- **warning**: variazione insolita ma compatibile con un evento reale;
- **failure**: condizione che rende il dataset non affidabile;
- **critical failure**: dato da bloccare prima della pubblicazione.

### Il principio del circuito chiuso

Un controllo utile deve avere:

**regola → rilevazione → owner → investigazione → decisione → correzione → documentazione**.

Un test che fallisce ma non ha nessuno responsabile è soltanto rumore automatizzato.
