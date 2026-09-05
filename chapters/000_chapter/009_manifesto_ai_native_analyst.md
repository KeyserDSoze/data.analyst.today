## 0.8 Manifesto dell'analista AI-native

Il resto del libro entrerà in statistica, SQL, modeling, causalità, forecasting, architettura, strumenti, comunicazione e AI-assisted analytics. Prima, però, serve un patto professionale.

L'AI può cambiare profondamente **come** lavoriamo. Può comprimere tempi, moltiplicare tentativi, distribuire l'esecuzione fra agenti specializzati e rendere accessibili capacità che prima richiedevano molto più lavoro manuale. Non cambia però il fatto che qualcuno debba capire che cosa sta succedendo e assumersi la responsabilità di ciò che viene consegnato.

Quello che segue è deliberatamente un manifesto. Qui la forma numerata è utile perché i principi devono poter essere ricordati, richiamati e usati come criterio di comportamento. Non è un riassunto dell'indice del capitolo: è il contratto operativo che porteremo nel resto del libro.

### 1. Comando io l'obiettivo

Non chiedo semplicemente all'AI di «analizzare i dati». Prima chiarisco quale decisione deve essere migliorata e traduco quella decisione in una domanda con un perimetro, una popolazione e metriche esplicite. Stabilisco anche quale livello di evidenza sarà necessario per considerare la risposta utilizzabile.

Questa preparazione non rallenta l'AI: evita di usare grande capacità di esecuzione su un obiettivo ambiguo. Se non sappiamo che cosa stiamo cercando, una risposta veloce produce soltanto ambiguità più velocemente.

### 2. Delego l'esecuzione, non la responsabilità

Posso delegare codice, query, ricerca, grafici, documentazione, esplorazione, prime bozze e perfino una parte dei controlli. Non delego la responsabilità di capire ciò che consegno.

Per ogni processo importante deve esistere un owner capace di ricostruire che cosa è successo, quali dati sono stati usati, quali controlli sono passati e quali failure mode restano plausibili. Quell'owner deve anche sapere come fermare o correggere il sistema. Se nessuno possiede questa capacità, l'automazione ha sostituito l'esecuzione ma ha anche creato un vuoto di accountability.

### 3. Chiedo evidenza, non soltanto risposte

Una conclusione importante deve poter essere ispezionata. Non mi basta che il risultato sia plausibile o espresso con sicurezza: devo poter risalire alle fonti, alle definizioni, alle trasformazioni, ai test e alle assunzioni che lo sostengono.

Cerco anche ciò che potrebbe indebolirlo. Alternative, limiti e controesempi non sono appendici pessimistiche dell'analisi; sono parte del percorso che rende una conclusione difendibile. Gli errori più pericolosi, infatti, non sono sempre quelli assurdi. Spesso sono quelli che assomigliano abbastanza alla realtà da non attirare l'attenzione.

### 4. Progetto la verifica

Non rifaccio manualmente tutto il lavoro dell'AI. Scelgo controlli proporzionati al rischio e, quando possibile, indipendenti dal percorso che ha prodotto il risultato.

Test deterministici e reconciliation possono proteggere l'integrità del dato; controlli statistici possono segnalare drift e anomalie; review semantiche possono mettere in discussione grain, metriche, denominatori, popolazioni e temporalità; critic agent, campionamento, audit ed escalation possono cercare errori che non emergono da un singolo test. La verifica è più utile quando non ripete semplicemente l'analisi, ma cerca i punti in cui il suo significato potrebbe rompersi: join, leakage, causalità, definizioni e assunzioni.

### 5. Se una storia mi convince troppo in fretta, cerco come potrebbe essere sbagliata

La conferma non è verifica. Se io e l'AI arriviamo subito alla stessa conclusione, non tratto l'accordo come prova aggiuntiva: potremmo condividere la stessa assunzione.

Cerco quindi spiegazioni alternative, segmenti contrari, controlli indipendenti e dati che potrebbero falsificare l'ipotesi. Provo a immaginare failure mode nei quali il risultato resterebbe plausibile pur essendo errato. Il compito dell'analisi non è costruire la storia più elegante, ma ridurre lo spazio delle spiegazioni che restano compatibili con l'evidenza.

### 6. L'autonomia cresce con i controlli, non con l'entusiasmo

Un agente che genera una bozza e un agente che può spostare denaro non appartengono alla stessa categoria di rischio. Più una decisione è costosa, irreversibile o impattante su persone e sistemi, più devono crescere affidabilità dimostrata, osservabilità, limiti di autorità, approval, logging, rollback e stop condition.

Un buon sistema non è quello che procede sempre. Deve poter dire «non lo so», chiedere review e fermarsi quando le condizioni minime non sono soddisfatte. L'autonomia è credibile soltanto quando include la capacità di non esercitarla.

### 7. Proteggo le competenze che mi permettono di governare

Non devo memorizzare ogni funzione o scrivere ogni riga a mano. Devo però comprendere abbastanza bene i fondamentali da riconoscere quando qualcosa non torna.

Proteggo soprattutto analytical thinking, business understanding, data semantics, statistica e incertezza, causalità, validazione, lettura di codice e query e comunicazione dei limiti. Queste competenze non competono con l'AI: sono ciò che mi permette di usarla senza trasformare l'automazione in dipendenza.

### 8. Misuro la produttività con la qualità, non con il volume

Produrre cento analisi non vale più che produrne dieci se le prime non meritano fiducia. Quando l'esecuzione costa meno, aumentano il valore della selezione, della semantica, della verifica e della decisione.

La metrica professionale diventa quindi:

> **output utile e affidabile per unità di tempo.**

Questa formulazione impedisce di confondere il throughput con il valore. Un sistema che produce più velocemente ma richiede correzioni continue, nasconde errori o aumenta il rischio decisionale non è necessariamente più produttivo.

### Accountability e oversight hanno basi esterne al libro

Questi principi non sono un'invenzione isolata di questo capitolo. Le linee guida Microsoft sugli agenti insistono su accountability, owner identificabili, human oversight, audit logging, limiti di autonomia e governance proporzionata al rischio. Il NIST AI RMF e il profilo dedicato alla Generative AI inquadrano l'identificazione, la misurazione e la gestione del rischio lungo il ciclo di vita dei sistemi AI.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## La regola da portare nel resto del libro

Tutto il capitolo converge su un principio che vale più del singolo tool o del singolo workflow:

> **Puoi delegare all'AI l'esecuzione. Puoi delegare l'esplorazione. Puoi delegare la prima bozza. Puoi delegare persino parte della verifica. Non puoi delegare la responsabilità di capire ciò che stai consegnando.**

Essere al timone non significa fare tutto. Significa sapere dove stiamo andando, che cosa sta facendo il sistema, quali segnali osservare, quando chiedere più evidenza, quando correggere la rotta e quando fermarsi.

Con questo patto possiamo entrare nel problema che viene prima di qualsiasi strumento: che cosa significa, esattamente, fare analisi? Il Capitolo 1 ripartirà da lì, mostrando perché la tecnologia può cambiare radicalmente mentre il nucleo del ragionamento analitico resta sorprendentemente stabile.

Nel resto del libro useremo l'AI in questo modo: non come oracolo, non come alibi, ma come moltiplicatore di capacità sotto responsabilità umana.

> **Il nuovo standard professionale non è “l'ho fatto io”. È “posso difenderlo”.**
