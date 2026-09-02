## 19.6 Decision span: quanto vicino lavori alla scelta?

Il Capitolo 15 ha già costruito il Decision Record e distinto finding, insight, recommendation e decisione.

Qui non serve ripetere quel metodo.

Ci interessa una conseguenza professionale.

Quando la produzione tecnica diventa più economica, una parte del valore dell'analista può spostarsi verso **quanto bene riesce a collegare evidenza, alternative, vincoli, azione e apprendimento**.

Chiamiamo questa ampiezza **decision span**.

## Cinque livelli di decision span

### Livello 1 — Output

Produco:

- query;
- report;
- dashboard;
- dataset;
- modello.

Il consumer decide che cosa farne.

### Livello 2 — Evidence

Produco un'analisi con:

- fenomeno;
- segmenti;
- incertezza;
- caveat;
- interpretazione.

Il lavoro riduce già ambiguità.

### Livello 3 — Alternatives

Collego l'evidenza alle opzioni disponibili.

Domande:

- quali leve abbiamo?
- che cosa costa ciascuna?
- quali guardrail servono?
- qual è lo switching value?

### Livello 4 — Decision design

Contribuisco a progettare:

- policy;
- experiment;
- rollout;
- allocation rule;
- escalation;
- feedback loop.

Non sto soltanto descrivendo il mondo.

Sto aiutando a costruire il meccanismo con cui l'organizzazione agirà.

### Livello 5 — Decision system

Lavoro sul processo ricorrente:

- quale evidenza entra;
- chi possiede la semantica;
- quali alternative vengono considerate;
- quale automazione è consentita;
- come viene misurato l'outcome;
- come il sistema impara.

Qui entriamo nella zona del Capitolo 18.

## Aumentare decision span non significa prendere il posto del manager

Questo punto è importante.

L'analista può migliorare il processo decisionale senza possedere tutte le conseguenze della decisione.

Un CFO, un Product VP o un COO può conoscere vincoli strategici, politici, contrattuali o organizzativi non interamente presenti nei dati.

Per questo il Decision Record distingue:

- analytics recommendation;
- chosen decision;
- decision owner.

La maturità dell'analista consiste nel portare **più struttura e meno ambiguità** alla decisione, non nell'usurpare authority che non possiede.

## Caso simulato/composito: churn 7,8%

Una SaaS company mostra:

- churn mensile 7,8%;
- target 6,5%;
- Enterprise 4,1%;
- SMB 10,9%;
- clienti low-usage 18,3%.

Un output-level analyst prepara un breakdown.

Un analyst con maggiore decision span chiede:

> “Quale decisione è realmente aperta?”

Le alternative operative includono:

1. Customer Success call;
2. onboarding intensivo;
3. technical review;
4. discount;
5. nessun intervento.

Poi collega ogni opzione a:

- costo;
- capacità;
- customer value;
- treatment opportunity;
- rischio di effetti collaterali;
- misurazione incrementale.

La domanda cambia da:

> “Chi ha churn risk alto?”

verso:

> **“Su quali account, con quale intervento e dato quale vincolo operativo, abbiamo sufficiente valore atteso per agire?”**

Il modello predittivo resta utile.

Ma è un input del sistema di decisione.

## Prediction → policy è un salto professionale

Una probabilità di churn dell'82% non contiene automaticamente una recommendation.

Servono anche:

- valore del cliente;
- costo dell'intervento;
- uplift plausibile;
- capacity;
- alternative;
- guardrail.

Questo vale oltre il churn.

### Forecast

Non basta prevedere la domanda.

Serve collegare la distribuzione prevista a staffing/inventory/capacity.

### Experiment

Non basta stimare un uplift.

Serve una rollout policy.

### Causal analysis

Non basta stimare un effetto medio.

Serve capire per quale popolazione e decisione è valido.

### AI agent

Non basta misurare task completion.

Serve definire authority, failure cost e escalation.

Aumentare decision span significa imparare a fare questi passaggi senza saltare le assunzioni.

## Outcome ownership vs outcome awareness

Un analyst non possiede necessariamente l'outcome finale.

Ma dovrebbe sviluppare **outcome awareness**.

Dopo una recommendation chiedere:

- quale decisione è stata presa?
- cosa è stato implementato davvero?
- quali guardrail si sono mossi?
- quale parte dell'outcome è attribuibile all'esecuzione?
- quale assunzione era sbagliata?
- cosa aggiorniamo la prossima volta?

Questo feedback trasforma il lavoro da produzione di analisi a apprendimento professionale.

## Il rischio dell'AI: saltare direttamente alla recommendation

Un agente può generare molto rapidamente:

- scenari;
- ranking;
- recommendation;
- executive summary.

La velocità crea una tentazione:

**output → recommendation**.

Il lavoro analitico maturo preserva invece i passaggi intermedi:

**evidence → alternatives → uncertainty → trade-off → recommendation**.

Quanto più facile diventa generare una recommendation, tanto più importante diventa saperne verificare il percorso.

## Una traiettoria di crescita

Per sviluppare decision span possiamo cercare progetti in cui passiamo progressivamente da:

- “mi dai i dati?”
- a “qual è la decisione?”
- a “quali alternative esistono?”
- a “cosa cambierebbe il ranking?”
- a “come misuriamo l'outcome?”
- a “come rendiamo il processo ricorrente?”.

Questo non richiede necessariamente una promozione formale.

Richiede che il nostro lavoro si avvicini alla struttura delle decisioni.

> **Quando produrre analisi diventa economico, una delle competenze più preziose è sapere quanto lontano possiamo accompagnare l'evidenza verso una decisione senza oltrepassare il claim o l'authority che possediamo.**
