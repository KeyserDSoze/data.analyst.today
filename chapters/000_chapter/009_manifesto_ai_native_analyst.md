## 0.8 Manifesto dell'analista AI-native

Il resto del libro entrerà in statistica, SQL, modeling, causalità, forecasting, architettura, strumenti, comunicazione e AI-assisted analytics.

Prima, però, serve un patto professionale.

L'AI può cambiare profondamente **come** lavoriamo. Non cambia il fatto che qualcuno debba capire che cosa sta succedendo e assumersi la responsabilità di ciò che viene consegnato.

### 1. Comando io l'obiettivo

Non chiedo semplicemente all'AI di “analizzare i dati”.

Definisco prima:

- la decisione;
- la domanda;
- il perimetro;
- la popolazione;
- le metriche;
- il livello di evidenza richiesto.

Se l'obiettivo è ambiguo, un'esecuzione velocissima produce soltanto ambiguità più velocemente.

### 2. Delego l'esecuzione, non la responsabilità

Posso delegare codice, query, ricerca, grafici, documentazione, esplorazione e prime bozze.

Posso delegare persino parte dei controlli.

Non delego la responsabilità di capire ciò che consegno.

Ogni processo importante deve avere un owner capace di spiegare che cosa è successo, quali dati sono stati usati, quali controlli sono passati, che cosa può andare storto e come fermare o correggere il sistema.

### 3. Chiedo evidenza, non soltanto risposte

Una conclusione importante deve poter essere ispezionata.

Cerco:

- dati e fonti;
- query e trasformazioni;
- definizioni;
- test;
- assunzioni;
- alternative;
- limiti.

Un output plausibile non è automaticamente un output corretto. Gli errori più pericolosi sono spesso quelli che sembrano ragionevoli.

### 4. Progetto la verifica

Non rifaccio manualmente tutto il lavoro dell'AI.

Costruisco controlli proporzionati al rischio:

- test deterministici;
- reconciliation;
- controlli statistici;
- review semantiche;
- campionamento;
- critic/red-team;
- audit;
- escalation.

E verifico soprattutto ciò che può rompere il significato del risultato: grain, join, metriche, denominatori, popolazioni, temporalità, leakage e causalità.

### 5. Se una storia mi convince troppo in fretta, cerco come potrebbe essere sbagliata

La conferma non è verifica.

Se io e l'AI arriviamo subito alla stessa conclusione, cerco comunque:

- spiegazioni alternative;
- segmenti contrari;
- controlli indipendenti;
- dati che potrebbero falsificare l'ipotesi;
- failure mode che renderebbero il risultato plausibile ma errato.

Il compito dell'analisi non è costruire la storia più elegante. È ridurre lo spazio delle spiegazioni incompatibili con l'evidenza.

### 6. L'autonomia cresce con i controlli, non con l'entusiasmo

Un agente che genera una bozza e un agente che può spostare denaro non sono la stessa cosa.

Più una decisione è costosa, irreversibile o impattante su persone e sistemi, più devono crescere:

- affidabilità dimostrata;
- osservabilità;
- limiti di autorità;
- approval;
- logging;
- rollback;
- stop condition.

Un buon agente deve poter dire “non lo so”, chiedere review e fermarsi.

### 7. Proteggo le competenze che mi permettono di governare

Non devo memorizzare ogni funzione o scrivere ogni riga a mano.

Devo però comprendere abbastanza bene i fondamentali da riconoscere quando qualcosa non torna.

Proteggo soprattutto capacità in:

- analytical thinking;
- business understanding;
- data semantics;
- statistica e incertezza;
- causalità;
- validazione;
- lettura di codice e query;
- comunicazione dei limiti.

L'AI deve amplificare il giudizio, non atrofizzarlo.

### 8. Misuro la produttività con la qualità, non con il volume

Produrre cento analisi non vale più che produrne dieci se le prime non meritano fiducia.

La metrica reale è:

> **output utile e affidabile per unità di tempo.**

Quando l'esecuzione costa meno, diventano più preziose semantica, verifica, priorità e decisione.

### Accountability e oversight non sono un'invenzione di questo libro

Le linee guida Microsoft sugli agenti insistono su accountability, owner identificabili, human oversight, audit logging e governance proporzionata al rischio. Il NIST AI RMF e il profilo dedicato alla Generative AI collocano identificazione, misurazione e gestione del rischio lungo il ciclo di vita dei sistemi AI.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## La regola da portare nel resto del libro

Possiamo riassumere tutto il capitolo così:

> **Puoi delegare all'AI l'esecuzione. Puoi delegare l'esplorazione. Puoi delegare la prima bozza. Puoi delegare persino parte della verifica. Non puoi delegare la responsabilità di capire ciò che stai consegnando.**

Essere al timone non significa fare tutto.

Significa sapere dove stiamo andando, che cosa sta facendo il sistema, quali segnali osservare, quando chiedere più evidenza, quando correggere la rotta e quando fermarsi.

Nel resto del libro useremo l'AI in questo modo.

Non come oracolo.

Non come alibi.

Come moltiplicatore di capacità sotto responsabilità umana.

> **Il nuovo standard professionale non è “l'ho fatto io”. È “posso difenderlo”.**
