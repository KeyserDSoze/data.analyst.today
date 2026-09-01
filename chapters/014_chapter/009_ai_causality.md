## 14.8 AI e causalità: usare il modello per attaccare le ipotesi, non per certificare l'effetto

Il Capitolo 8 ha già costruito il framework di causal identification. Qui non ripetiamo matching, RDD, IV o Difference-in-Differences.

La domanda è diversa:

> **come cambia il nostro modo di lavorare quando un sistema generativo può produrre in pochi secondi decine di spiegazioni causali plausibili?**

Il rischio principale è la **causal fluency**: l'AI può trasformare molto rapidamente una differenza osservata in una storia che suona come un meccanismo.

### Pattern, mechanism e effect sono tre cose diverse

Immaginiamo:

```text
webinar attendees churn:     5,8%
non-attendees churn:         12,4%
observed difference:         -6,6 pp
```

Un summary generativo potrebbe diventare:

> “I webinar riducono il churn di 6,6 punti percentuali.”

Ma dai dati sopra sappiamo soltanto che i due gruppi differiscono.

Non sappiamo ancora se:

- i clienti più engaged scelgano autonomamente di partecipare;
- i CSM invitino clienti con caratteristiche particolari;
- dimensione account e piano differiscano;
- esistano interventi concomitanti;
- il webinar sia causa, mediatore, proxy o semplice correlato.

L'AI non ha commesso necessariamente un errore aritmetico.

Ha **saltato un livello di claim**.

### Il Causal Claim Gate

Ogni volta che un output AI usa parole come:

- causa;
- effetto;
- impatto;
- driver;
- ha generato;
- ha fatto aumentare;
- ha ridotto;

la AI Analysis Control Sheet richiede un gate.

```text
causal estimand:
treatment/exposure:
outcome:
comparison/counterfactual:
assignment mechanism:
key confounders:
post-treatment variables:
identification strategy:
diagnostics:
scope of effect:
claim allowed:
```

Se questi campi non possono essere compilati, l'output deve restare descrittivo o diagnostico.

### Cosa l'AI può fare molto bene

L'AI è utile come **red-team dell'identification strategy**.

Possiamo chiederle:

- “Quali common causes potrebbero spiegare questa associazione?”
- “Quali variabili sto controllando che potrebbero essere post-treatment?”
- “Quale selection mechanism renderebbe il confronto distorto?”
- “Quali placebo test o falsification test indebolirebbero la mia spiegazione?”
- “Quale dato, se osservato, renderebbe questa ipotesi meno credibile?”
- “Proponi tre DAG alternativi compatibili con la stessa correlazione.”

Queste richieste usano bene la capacità generativa: **moltiplicare le alternative che dobbiamo cercare di escludere**.

### Caso simulato/composito — il coupon “miracoloso”

Un retailer analizza 2,4 milioni di clienti.

Un agente trova:

```text
spesa 30 giorni dopo coupon: +19% vs clienti senza coupon
```

Il primo summary propone:

> “Il coupon aumenta la spesa del 19%.”

L'analista ricostruisce però la policy di targeting.

Il marketing invia il coupon soprattutto a clienti che:

- hanno visitato il sito negli ultimi 72 ore;
- hanno almeno un prodotto in wishlist;
- hanno aperto due email recenti;
- hanno già mostrato alta propensity all'acquisto.

Queste variabili influenzano sia l'assegnazione del coupon sia la probabilità di comprare.

Il +19% è quindi una differenza osservata tra popolazioni selezionate.

Il team introduce un holdout randomizzato tra i clienti eleggibili e trova un effetto incrementale molto più piccolo ma ancora economicamente interessante.

Nel caso didattico non importa il valore esatto dell'effetto.

Importa la sequenza:

```text
association
→ reconstruct assignment
→ define eligible population
→ create credible counterfactual
→ estimate effect
→ decide economics
```

### Il pericolo dell'AI che “controlla tutto”

Un'altra scorciatoia frequente è:

> “Aggiungi tutte le variabili disponibili alla regressione così controlliamo i confondenti.”

Questo può peggiorare il problema.

Tra le variabili disponibili potrebbero esserci:

- mediatori;
- collider;
- feature misurate dopo il trattamento;
- proxy rumorosi;
- variabili che cambiano la popolazione analizzata.

La disponibilità di una colonna non è un criterio causale per includerla.

L'AI può suggerire covariate; l'identification logic deve spiegare **perché** ciascuna variabile appartiene al modello.

### Prompt utile: chiedere una critica, non una risposta causale

Invece di:

> “Qual è l'effetto della feature X sulla retention?”

meglio:

> “Non stimare ancora un effetto. Ricostruisci i possibili meccanismi di assegnazione a X, elenca common causes plausibili, identifica variabili potenzialmente post-treatment e proponi il design più credibile tra quelli compatibili con i dati disponibili. Indica esplicitamente ciò che non è identificabile.”

La qualità del prompt qui non sostituisce il design.

Serve a impedire che il modello **salti direttamente alla conclusione**.

### Claim ladder per causalità

La Control Sheet può autorizzare livelli diversi.

```text
L0: non interpretabile
L1: associazione osservata
L2: pattern robusto a segmentazioni/robustness check
L3: spiegazione compatibile con un meccanismo, non identificata causalmente
L4: effetto causale identificato sotto assunzioni esplicite
L5: effetto replicato / sperimentale con scope operativo definito
```

Un executive summary non può salire da L2 a L4 soltanto perché un LLM ha reso il testo più fluido.

### AI come generatore di esperimenti

Un uso molto produttivo è chiedere:

- quale popolazione rendere eleggibile;
- quale unità randomizzare;
- quali spillover aspettarsi;
- quale guardrail usare;
- quale outcome misurare;
- quale eterogeneità pre-specificare.

Poi il design viene riportato dentro l'**Experiment Contract** del Capitolo 9.

Questa continuità è importante: l'AI non crea un metodo causale alternativo. **Accelera il lavoro dentro metodi che mantengono le loro assunzioni.**

### Fonte metodologica

La World Bank, in *Impact Evaluation in Practice*, struttura l'impact evaluation intorno alla costruzione di un controfattuale credibile e alla comprensione del meccanismo di assegnazione, non alla sola presenza di correlazioni nei dati.

Fonte: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice

### Campo della AI Analysis Control Sheet

Per richieste causali:

```text
observed association:
causal language requested?:
estimand:
assignment understood?:
credible counterfactual?:
confounders / mediators / post-treatment risks:
identification design:
falsification/robustness checks:
claim level approved:
human reviewer:
```

> **L'AI può moltiplicare le ipotesi causali e i modi di attaccarle. Non può trasformare la plausibilità narrativa in identificazione causale.**
