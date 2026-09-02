## 14.11 Valutare i sistemi AI: dall'impressione di qualità a un claim supportato da evidenza

Quando un workflow incorpora l'AI, la frase:

> “nelle prove sembra funzionare bene”

non è un criterio di release.

Un eval serve a sostenere un **claim operativo specifico**.

Per esempio:

> “Su domande revenue nel perimetro Finance, il sistema usa la metrica certificata, rispetta la data economica, non oltrepassa i permessi e chiede escalation quando la richiesta è ambigua.”

Questa frase è molto più testabile di:

> “il nostro agente SQL è accurato al 94%.”

### Claim → failure modes → eval suite

Il design parte dal claim, non dalla metrica disponibile.

```text
claim
→ quali failure mode lo invaliderebbero?
→ quali casi li rappresentano?
→ quale ground truth serve?
→ quale scoring è appropriato?
→ quale soglia autorizza il rollout?
```

Esempio per un agente analitico:

| Failure mode | Caso di eval |
|---|---|
| metrica sbagliata | due misure `Revenue`, una certificata e una legacy |
| data errata | `order_created_at` vs `payment_captured_at` |
| join esplosivo | relazione many-to-many con promotion |
| dato immaturo | feed D+1 ancora incompleto |
| linguaggio causale improprio | confronto osservazionale tra trattati e non trattati |
| accesso non autorizzato | richiesta su tabella HR fuori scope |
| falsa sicurezza | schema ambiguo che dovrebbe produrre domanda/STOP |

### Prima i test deterministici

Non tutto deve essere valutato da un altro LLM.

Se possiamo verificare deterministicamente che:

- la tabella usata è autorizzata;
- la metrica id è quella certificata;
- la query non contiene un `DELETE`;
- il row count non viola un'invariante;
- l'output riconcilia entro tolleranza;

preferiamo un controllo deterministico.

Una gerarchia sana è:

```text
1. deterministic checks
2. reference/ground-truth comparisons
3. statistical metrics
4. model-based judge per aspetti qualitativi
5. human review
```

Non perché il livello 5 sia sempre “migliore”, ma perché diversi errori richiedono diversi tipi di evidenza.

### Caso reale documentato — quando il benchmark è il problema

Nel luglio 2026 OpenAI ha pubblicato un audit di SWE-Bench Pro.

L'analisi automatizzata ha segnalato il 27,4% dei task come problematici; una campagna di annotazione umana ne ha identificati il 34,1%. OpenAI ha quindi stimato che circa il 30% dei task fosse rotto.

Tra i problemi documentati:

- test troppo rigidi che imponevano dettagli non richiesti;
- prompt sottospecificati rispetto agli hidden test;
- test con coverage insufficiente;
- prompt fuorvianti o in conflitto con il comportamento atteso.

Fonte: OpenAI, *Separating signal from noise in coding evaluations*: https://openai.com/index/separating-signal-from-noise-coding-evaluations/

La lezione per un Data Analyst va ben oltre il coding:

> **se il gold standard è sbagliato, un punteggio perfettamente calcolato può aumentare la nostra fiducia in una misura invalida.**

### Validare anche l'eval

Prima di usare una suite come release gate chiediamo:

- il task rappresenta il lavoro reale?
- la distribuzione dei casi riflette frequenza o rischio?
- il ground truth è affidabile?
- la rubric premia davvero il comportamento desiderato?
- esistono shortcut o leakage?
- il sistema può capire di essere sotto eval e comportarsi diversamente?
- il test environment assomiglia abbastanza al deployment environment?
- abbiamo ispezionato manualmente successi e fallimenti?

Un eval è un modello del rischio reale. Anche lui ha assunzioni.

### Caso reale documentato — dichiarare cosa un'evaluation supporta

Nel 2026 OpenAI ha proposto un playbook per valutazioni affidabili di terze parti. Tra gli elementi richiesti per interpretare correttamente un'evaluation compaiono:

- il **claim** che si vuole sostenere;
- il contenuto e la distribuzione dei task;
- il sistema testato, inclusi modello, reasoning setting, tool access, harness e safeguards;
- il budget di turn, token, tentativi, tempo e costo;
- i metodi di elicitation;
- i validity check contro comportamenti che possono distorcere il risultato.

Fonte: OpenAI, *A shared playbook for trustworthy third party evaluations*: https://openai.com/index/trustworthy-third-party-evaluations-foundations/

Questo è particolarmente importante per gli agenti: **modello + tool + harness + budget** è il sistema effettivamente valutato.

### LLM-as-a-judge: utile, ma è un altro modello da validare

Un judge model può scalare valutazioni qualitative, per esempio:

- chiarezza;
- aderenza a una rubric;
- qualità della spiegazione;
- confronto pairwise tra due output.

Ma non dovrebbe diventare automaticamente il ground truth.

Google Cloud, nella documentazione per valutare un judge model, propone di preparare dataset con **human ratings come ground truth** e confrontare i punteggi del judge con quelle valutazioni.

Fonte: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluate-judge-model

Per il nostro workflow:

```text
human-labeled sample
→ calibrate judge
→ use judge at scale
→ periodic human audit
→ recalibrate after meaningful changes
```

### Eval set stratificato per rischio

Un accuracy medio può nascondere errori rari ma inaccettabili.

Supponiamo:

```text
990 task normali: 98% corretti
10 task sensibili: 50% corretti
```

L'accuracy globale è molto alta.

Ma il sistema fallisce metà delle richieste che non dovrebbe sbagliare.

La suite dovrebbe quindi distinguere:

- frequenza;
- severità;
- detectability;
- reversibilità.

Possiamo usare una matrice come:

| Classe | Esempio | Release tolerance |
|---|---|---|
| S0 | formattazione | alta |
| S1 | query esplorativa correggibile | moderata |
| S2 | KPI management | bassa |
| S3 | accesso non autorizzato / azione critica | prossima a zero |

### Misurare escalation e rifiuto, non solo risposta

Un buon sistema non deve sempre rispondere.

Dobbiamo valutare anche:

- quando chiede chiarimento;
- quando dichiara dato insufficiente;
- quando rifiuta una richiesta fuori scope;
- quando produce `PROVISIONAL`;
- quando esegue `STOP / ESCALATE`.

Per alcuni casi, **non procedere è la risposta corretta**.

### Regression eval dopo ogni cambiamento materiale

Cambiare:

- prompt;
- modello;
- tool;
- permessi;
- semantic model;
- retrieval corpus;
- orchestration logic;

può modificare il comportamento.

Ogni cambiamento materiale dovrebbe attivare almeno:

```text
smoke eval
→ critical regression suite
→ comparison vs current production
→ manual inspection of changed failures
→ release / rollback decision
```

### Production eval: il test non finisce al deploy

In produzione misuriamo anche:

- tasso di correzione umana;
- escalation rate;
- false escalation;
- semantic error rate;
- authorization violations;
- cost per successful task;
- latency;
- numero di tool call;
- failure severity;
- incidenti sfuggiti agli eval;
- drift nella distribuzione delle richieste.

Gli errori reali diventano nuovi casi della regression suite.

### Un esempio di Eval Card

```text
claim:
release candidate:
tested system:
tool/data permissions:
eval dataset version:
risk strata:
ground truth source:
deterministic checks:
judge model + calibration:
human audit sample:
critical failure tolerance:
results by severity:
known blind spots:
release decision:
```

Questa **Eval Card** entra nella AI Analysis Control Sheet per workflow riusabili o produttivi.

### Regola operativa

> **Non chiedere “quanto è bravo il modello?”. Chiedi “quale claim sul sistema vogliamo autorizzare, quale evidenza lo sostiene e quali errori non siamo ancora in grado di vedere?”.**
