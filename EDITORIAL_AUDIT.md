# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review completata: **Capitoli 0–15**.
- Da revisionare: **Capitoli 16–19**.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.

### Ultima build validata

Dopo la review del Capitolo 15:

- **20 capitoli**;
- **321 file Markdown**;
- **226.446 parole stimate**;
- **1.667.461 caratteri**;
- **174 URL esterni distinti**;
- **8 file con LaTeX**;
- **1.032 pagine PDF**;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità è la densità di valore per pagina.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
python scripts/build.py
```

Il lint verifica, tra le altre cose:

- continuità dei capitoli;
- prefissi file duplicati/mancanti;
- heading incoerenti;
- file vuoti;
- `TODO`, `FIXME`, `TBD`;
- `utm_source=chatgpt.com`;
- grafie ASCII legacy;
- URL esterni;
- formule/LaTeX;
- conteggio parole.

### Warning residuo

Resta un solo warning globale:

- notazione matematica/LaTeX in **8 file**.

Prima della release bisognerà decidere se usare notazione testuale o un vero renderer matematico per le formule residue.

## 3. Convenzione casi e fonti

### Caso reale documentato

Deve avere:

- organizzazione/evento identificabile;
- fonte pubblica attendibile;
- claim proporzionato alla fonte;
- nessuna trasformazione indebita di associazione in causalità.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Fonti

La review privilegia standard e governi, documentazione ufficiale, letteratura accademica riconosciuta e fonti primarie per i casi pubblici.

Prima della release resta un audit globale dei **174 URL** per link, redirect, supporto del claim e uniformità delle note.

## 4. Stato capitolo per capitolo

| Capitolo | Stato | Deliverable / funzione |
|---|---|---|
| 0 — Al timone | **Revisionato** | Manifesto: responsabilità, delega, verifica, stop condition, trust levels. |
| 1 — Tutto è cambiato | **Revisionato** | Catena analitica canonica e tipi di domanda. |
| 2 — Problema business → analitico | **Revisionato** | **Analytical Brief**. |
| 3 — Capire i dati | **Revisionato** | **Data Readiness Review**. |
| 4 — Statistica descrittiva ed EDA | **Revisionato** | **EDA Evidence Map**. |
| 5 — Probabilità e incertezza | **Revisionato** | **Uncertainty Brief**. |
| 6 — Lifecycle analysis | **Revisionato** | **Lifecycle Diagnostic Map**. |
| 7 — Time series e forecasting | **Revisionato** | **Temporal Decision Brief**. |
| 8 — Causalità | **Revisionato** | **Causal Identification Brief**. |
| 9 — Experimentation | **Revisionato** | **Experiment Contract**. |
| 10 — Predictive modeling | **Revisionato** | **Predictive Decision Card**. |
| 11 — SQL e data modeling | **Revisionato** | **Analytical Data Contract**. |
| 12 — Data architecture | **Revisionato** | **Data Flow Architecture Map**. |
| 13 — Tool selection | **Revisionato** | **Tooling Decision Record**. |
| 14 — AI-assisted analytics | **Revisionato** | **AI Analysis Control Sheet**. |
| 15 — Insight e decisione | **Revisionato** | **Decision Record**. |
| 16 — Storytelling/dashboard | **Da revisionare** | Comunicazione e visual evidence. |
| 17 — Casi end-to-end | **Da revisionare** | Laboratorio integrato. |
| 18 — Sistema analitico che scala | **Da revisionare** | Operating model, reliability, data products, governance. |
| 19 — Data Analyst 2026–2035 | **Da revisionare** | Skill, agent management, deskilling, carriera. |

## 5. Deliverable canonici

```text
Analytical Brief
→ Data Readiness Review
→ EDA Evidence Map
→ Uncertainty Brief
→ Lifecycle Diagnostic Map
→ Temporal Decision Brief
→ Causal Identification Brief
→ Experiment Contract
→ Predictive Decision Card
→ Analytical Data Contract
→ Data Flow Architecture Map
→ Tooling Decision Record
→ AI Analysis Control Sheet
→ Decision Record
```

Non ogni analisi richiede tutti gli artefatti. Sono un vocabolario operativo per rischi differenti.

## 6. Confini concettuali principali

### 0 / 14 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** workflow operativo, context/data/tool boundary, eval, privacy, auditability;
- **19:** conseguenze su skill, ruoli e carriera.

### 3 / 4 / 5 — qualità, pattern, inferenza

- **3:** il dato è utilizzabile?
- **4:** quale struttura mostra?
- **5:** quanto possiamo generalizzare e con quale incertezza?

### 5 / 8 / 9 — inferenza, identificazione, esperimento

- **5:** teoria inferenziale;
- **8:** identification assumptions;
- **9:** preservare il confronto in un esperimento reale.

### 6 / 8 / 9 / 10 — comportamento, intervento, prediction

- **6:** localizzare il lifecycle risk;
- **8:** identificare effetti;
- **9:** testare interventi;
- **10:** anticipare eventi e trasformare score in policy.

### 11 / 12 / 13 — significato, flusso, strumento

- **11:** che cosa deve significare il dataset → **Analytical Data Contract**;
- **12:** da dove arriva e con quali garanzie → **Data Flow Architecture Map**;
- **13:** quale ambiente è proporzionato al lavoro → **Tooling Decision Record**.

### 14 / 15 — evidence control vs decision quality

- **14:** stabilisce se un output ha il diritto di sostenere un determinato claim;
- **15:** confronta alternative e decide quale azione è giustificata da evidenza, rischio e incertezza.

### 15 / 16 — decisione vs comunicazione

- **15:** cosa dovremmo decidere e perché → **Decision Record**;
- **16:** come rendere quella decisione e la sua evidenza comprensibili senza alterare claim, incertezza o priorità.

Il Capitolo 16 deve derivare dal Decision Record, non inventare una nuova narrativa indipendente.

### 13 / 18 — workflow locale vs operating model

- **13:** scelta/migrazione del singolo workflow;
- **18:** standard e ownership organizzativi che permettono di scalare.

## 7. Note review Capitoli 14–15

### Capitolo 14

Il centro è la **AI Analysis Control Sheet**:

```text
decision
→ analytical contract
→ Context Pack
→ data/tool boundary
→ AI generation/execution
→ Verification Bundle
→ method-specific gate
→ eval
→ claim gate
→ human control
→ action
→ audit trace
```

Aurelia Travel e DeltaHome sono marcati esplicitamente come casi simulati/compositi; i casi pubblici sono sostenuti da fonti primarie.

### Capitolo 15

Il capitolo converge nel **Decision Record**:

```text
decision
→ objective
→ constraints
→ alternatives + business as usual
→ evidence
→ uncertainty
→ value + downside
→ reversibility
→ switching values
→ analytics recommendation
→ chosen decision
→ guardrails
→ review / learning
```

Concetti rafforzati:

- finding, insight, explanation hypothesis, recommendation e decisione sono livelli distinti;
- una raccomandazione deve essere confrontata con alternative reali e con il business as usual;
- `ACT / PILOT / WAIT / BUY INFORMATION / ABANDON` come classi di mossa decisionale;
- evidence threshold distinto da switching threshold;
- one-way sensitivity, scenari coerenti, stress test e robustness of ranking;
- analytics recommendation distinta dalla chosen decision del decision owner;
- pre-mortem e learning contract;
- **Decision quality ≠ Execution quality ≠ Outcome quality**;
- Decision Quality Gate: **DECIDE / PILOT-STAGE / WAIT FOR X / NO ACTION-ABANDON**.

Aurora Home è marcato come caso simulato/composito. Le fonti di riferimento includono HM Treasury Green Book 2026 e NASA Decision Analysis.

## 8. Arco complessivo

```text
mentalità
→ domanda
→ dati
→ statistica
→ comportamento
→ tempo
→ causalità
→ esperimenti
→ modelli
→ semantica/SQL
→ architettura
→ strumenti
→ AI
→ decisione
→ comunicazione
→ casi completi
→ scala
→ futuro
```

## 9. Lavori ancora necessari prima della release

- review Capitoli 16–19;
- audit link/fonti globale;
- formula rendering;
- frontespizio, copyright/licenza, autore e bio;
- “come usare il libro” e indice automatico;
- glossario/bibliografia/indice fonti;
- ringraziamenti e numero/versione release;
- proofread ortografico finale;
- controllo tabelle, code block, footnote e page break nel PDF/DOCX.

## 10. Release gate

Prima di una release candidata:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di indice, formule, tabelle, codice, fonti, casi reali/compositi, ripetizioni, ortografia, footnote, page break e continuità dei deliverable canonici.

## 11. Prossimo blocco

La review continua dal **Capitolo 16 — Data storytelling, dashboard ed executive communication**.

Direzione editoriale:

```text
Decision Record
→ audience
→ decision question
→ headline
→ evidence hierarchy
→ visual encoding
→ uncertainty / context
→ decision requested
→ appendix / provenance
```

Deliverable previsto: **Decision Communication Pack**.

Il Capitolo 16 non deve insegnare a “rendere i dati belli”. Deve insegnare a preservare il significato mentre riduce il costo cognitivo della decisione.