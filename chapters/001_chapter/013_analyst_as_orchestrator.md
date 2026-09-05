## 1.12 Il Data Analyst come orchestratore del sistema analitico

Il Capitolo 0 ha presentato l'analista come manager di agenti AI. Il concetto, però, è più ampio della tecnologia generativa.

Anche senza AI, un Data Analyst lavora al centro di un sistema composto da persone, applicazioni, fonti dati, trasformazioni, definizioni, strumenti e processi decisionali. Nessuna singola persona deve costruire tutto. Ma qualcuno deve capire abbastanza bene il percorso end-to-end da riconoscere **dove può rompersi il significato**.

Questa è una forma di orchestrazione molto concreta.

### Un numero executive eredita tutta la sua storia

Immaginiamo una dashboard che mostra il `Monthly Recurring Revenue`.

Il numero appare come un singolo oggetto, ma prima di arrivare sullo schermo un cliente ha sottoscritto o modificato un piano; un'applicazione ha registrato eventi e stati; una pipeline li ha portati in un ambiente analitico; trasformazioni hanno gestito upgrade, downgrade e cancellazioni; qualcuno ha definito regole per valute, crediti e rimborsi; un modello semantico ha esposto una metrica; infine un processo di business ha deciso di usare quel numero per pianificare o valutare la performance.

Ogni passaggio può modificare ciò che il numero significa.

Se una regola di downgrade cambia nella pipeline, il dashboard può cambiare senza che il comportamento dei clienti sia cambiato. Se il semantic layer definisce MRR in modo diverso da Finance, due team possono discutere dello stesso concetto usando numeri incompatibili. Se la pipeline è in ritardo, un calcolo perfetto può descrivere il passato come se fosse il presente.

L'analista non deve necessariamente gestire l'applicazione, l'infrastruttura e il modello semantico. Deve però saper ricostruire abbastanza della lineage da capire **quale assunzione introdotta a monte possa spiegare ciò che vede a valle**.

Questa capacità diventa più importante con la seniority perché molti problemi analitici non si trovano nel notebook in cui vengono scoperti.

### A volte il problema che arriva ad Analytics non è un problema di analisi

Una richiesta può sembrare analitica e richiedere in realtà un intervento altrove nel sistema.

Se manca una sorgente affidabile, non serve costruire una dashboard più sofisticata: probabilmente serve data engineering. Se la stessa metrica viene implementata in dieci modi, la soluzione può essere un semantic layer o analytics engineering. Se la domanda richiede un confronto causale complesso, può servire una competenza specifica di experimentation o data science. Se il dashboard è corretto ma nessuno modifica il proprio comportamento quando cambia, il problema può essere nel processo decisionale o nell'adozione, non nei dati.

Riconoscere il tipo di problema è una competenza tecnica quanto sapere risolverlo. Evita di trattare ogni richiesta con lo strumento che conosciamo meglio.

### La tecnologia dovrebbe seguire il costo del problema

Un approccio fragile parte dal tool:

> “Ho Power BI: come risolvo questo problema in Power BI?”

oppure:

> “Sto studiando Python: devo usare Python per questa analisi.”

Un approccio maturo parte invece dalla domanda:

> **“Qual è il modo più semplice, affidabile e sostenibile per ottenere l'evidenza necessaria?”**

Una tabella di duemila righe analizzata una sola volta può essere perfettamente gestibile in un foglio elettronico. Miliardi di righe già presenti in un warehouse dovrebbero probabilmente essere aggregate vicino alla sorgente. Una metrica consultata ogni giorno da molti manager richiede più governance di un notebook esplorativo che vive per due ore. Una trasformazione che alimenta decine di processi ogni mattina non è più “la query dell'analista”: sta diventando un prodotto operativo e deve essere trattata di conseguenza.

Il Capitolo 13 svilupperà un framework completo per la scelta degli strumenti. Qui ci basta vedere quali dimensioni fanno cambiare categoria al problema:

| Dimensione | Domanda che cambia la scelta |
|---|---|
| **Volume** | quanti dati devono essere elaborati e dove vivono già? |
| **Frequenza** | è un'analisi una tantum o un processo ricorrente? |
| **Complessità** | basta una trasformazione semplice o servono logiche articolate e modelli? |
| **Audience** | il risultato serve a una persona o diventa un servizio condiviso? |
| **Governance** | quanto contano accessi, lineage, riproducibilità e definizioni certificate? |

Costo, latenza, sicurezza, mantenibilità e competenze del team completano il quadro. La regola non è scegliere sempre il tool più potente. È evitare sia di costruire una piattaforma per risolvere un problema usa-e-getta, sia di affidare un processo critico a un artefatto personale fragile.

> **La maturità tecnica non consiste nell'usare sempre lo strumento più avanzato, ma nel riconoscere il livello di tecnologia necessario al problema e alla sua vita operativa.**

### L'analista traduce fra sistemi di significato diversi

Il business parla di clienti, ricavi, costi, rischi e decisioni. I sistemi dati parlano di eventi, chiavi, timestamp e stati. La statistica parla di popolazioni, distribuzioni, assunzioni e incertezza. L'architettura parla di pipeline, storage, latenza e affidabilità. L'AI aggiunge un ulteriore strato capace di eseguire e coordinare attività, con i requisiti di supervisione discussi nel Capitolo 0.

Nessuno di questi linguaggi è sufficiente da solo. L'analista crea valore quando riesce ad attraversarli senza confonderli: sa che una colonna non è automaticamente un concetto di business, che una correlazione non è una decisione e che una demo tecnica non è ancora un processo affidabile.

Possiamo allora estendere la definizione introdotta nella sezione 1.3:

> **Un Data Analyst riduce l'incertezza attorno a decisioni reali trasformando problemi in domande, dati in evidenza ed evidenza in azioni verificabili, orchestrando persone e strumenti nella misura necessaria al problema.**

Nessun singolo software definisce il mestiere. A definirlo è la capacità di mantenere coerente la catena tra realtà, dato, metodo e decisione anche quando quella catena attraversa sistemi che l'analista non ha costruito personalmente.
