## 19.1 Task exposure e responsibility moat

Dire che “SQL diventa commodity” è utile fino a un certo punto.

Rischia di farci pensare che alcune competenze spariscano mentre altre restino intatte.

La realtà è più interessante.

Un'attività può diventare molto più economica da eseguire senza rendere economica **la responsabilità di sapere se quell'attività è stata eseguita correttamente per il problema giusto**.

Per questo separiamo due concetti.

## Task exposure

È quanto un'attività può essere assistita, compressa o automatizzata da AI e software.

L'esposizione tende a essere maggiore quando:

- l'input è relativamente ben specificato;
- l'output ha pattern ricorrenti;
- esistono molti esempi;
- il risultato è verificabile rapidamente;
- il failure cost è limitato;
- il contesto necessario può essere fornito al sistema.

Nel lavoro analitico rientrano spesso in questa categoria:

- generazione di SQL standard;
- traduzione tra dialect;
- formule di spreadsheet;
- boilerplate Python/R;
- visualizzazioni di base;
- profiling iniziale;
- refactoring semplice;
- generazione di documentazione;
- prime bozze di test;
- sintesi di report;
- ricerca tecnica;
- costruzione di query candidate.

Queste attività non smettono di servire.

Semplicemente **costano meno**.

## Responsibility moat

È la parte della responsabilità professionale che resta difficile comprimere perché richiede una combinazione di:

- contesto non completamente formalizzato;
- scelta tra obiettivi in conflitto;
- semantica business;
- valutazione del rischio;
- responsabilità sugli effetti downstream;
- capacità di riconoscere quando la specifica stessa è sbagliata;
- coordinamento con stakeholder;
- judgment sotto incertezza.

Esempi:

- decidere quale definizione di churn è adatta a una decisione;
- stabilire se un confronto è semanticamente valido;
- riconoscere che il dato disponibile non identifica una causal claim;
- scegliere se il valore di altra informazione giustifica aspettare;
- decidere quale guardrail impedisce a un'ottimizzazione locale di danneggiare il sistema;
- stabilire quando un agente deve perdere autorità;
- difendere una recommendation davanti a Finance, Product e Operations con incentivi diversi.

Questa è la zona in cui il valore umano può restare elevato anche se l'esecuzione materiale viene automatizzata.

## Caso simulato/composito: una query da tre minuti e un errore da tre mesi

Un analyst deve calcolare la repeat purchase rate a 90 giorni per paese e canale.

Con semantic context e AI, una prima query arriva in tre minuti.

La sintassi è corretta.

Ma la richiesta nasconde almeno sette decisioni:

- la coorte parte dal primo ordine creato o pagato?
- i refund annullano il primo acquisto?
- un guest che poi crea un account è la stessa persona?
- i 90 giorni sono dalla data ordine o consegna?
- il denominatore include clienti che non hanno ancora avuto 90 giorni completi di osservazione?
- il canale è acquisition channel o repeat-order channel?
- le acquisizioni recenti vengono censurate correttamente?

Supponiamo che l'AI includa nel denominatore anche clienti con solo 20 giorni di osservazione.

La query continuerà a girare perfettamente.

La metrica resterà depressa per mesi.

Qui il task di scrittura SQL era altamente esposto.

La responsabilità semantica no.

## Una matrice più utile

| Attività | Task exposure | Responsibility moat |
|---|---:|---:|
| scrivere una query standard | alta | bassa-media |
| verificare grain/cardinality | media-alta | alta |
| generare un grafico | alta | media |
| scegliere quale evidenza mostrare al CEO | media | alta |
| produrre un forecast candidate | alta | media |
| decidere quale forecast è utilizzabile per staffing | media | alta |
| creare uno score churn | alta | media |
| definire chi trattare dato uplift, costo e capacity | bassa-media | molto alta |
| generare un causal DAG candidate | alta | media |
| decidere se l'effetto è identificato | media | molto alta |
| creare un executive summary | alta | media |
| scegliere claim level e caveat decision-critical | media | molto alta |

Il punto non è cercare la casella “impossibile da automatizzare”.

Probabilmente quella casella cambierà continuamente.

Il punto è costruire capacità che restano preziose quando **l'automazione sale di livello**.

## La tecnica cambia funzione

Da qui nasce un errore opposto:

> “Se l'AI scrive SQL, non devo più capire SQL.”

È falso.

Per verificare un output dobbiamo possedere un modello mentale abbastanza profondo del sistema.

Un analyst che non capisce:

- grain;
- join;
- leakage;
- randomizzazione;
- standard error;
- baseline;
- backtest;
- unit economics;

non diventa più strategico grazie all'AI.

Diventa più dipendente.

La tecnica quindi passa almeno attraverso tre ruoli.

### Execution skill

So produrre l'output.

### Verification skill

So capire se l'output è plausibile, coerente e metodologicamente valido.

### Design skill

So progettare il problema, il metodo e i controlli in modo che l'output abbia una possibilità reale di essere utile.

L'AI riduce soprattutto il premio relativo sulla prima.

Può aumentare quello sulle altre due.

## La fonte pubblica: esposizione non equivale a sostituzione

L'ILO, nel rapporto 2025 sulla GenAI e il lavoro, studia l'esposizione a livello di task e conclude che la trasformazione dei lavori è generalmente più plausibile della completa automazione, proprio perché le occupazioni contengono mix diversi di attività e continuano a richiedere input umano.

Fonte: https://www.ilo.org/publications/generative-ai-and-jobs-2025-update

Questo è un buon antidoto a due narrazioni semplicistiche:

- “l'AI cancellerà il ruolo”;
- “non cambierà nulla”.

Più probabilmente cambierà **la composizione del ruolo e il premio relativo associato alle diverse capacità**.

## Il test personale

Per ogni attività importante del proprio lavoro possiamo chiedere:

1. quanto sta scendendo il costo di esecuzione?
2. quale parte richiede ancora giudizio o contesto?
3. che cosa succede se l'output è plausibile ma sbagliato?
4. quale competenza mi serve per verificarlo?
5. quale responsabilità posso imparare a possedere a un livello superiore?

Queste cinque domande sono più utili di chiedere semplicemente:

> “L'AI può fare questa cosa?”

> **La carriera resiliente non si costruisce difendendo i task costosi di ieri. Si costruisce diventando più forti nelle responsabilità che emergono quando quei task diventano economici.**
