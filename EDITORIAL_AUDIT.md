# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review completata: **Capitoli 0–17**.
- Da revisionare: **Capitoli 18–19**.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.

### Ultima build validata

Dopo la review del Capitolo 17:

- **20 capitoli**;
- **321 file Markdown**;
- **238.362 parole stimate**;
- **1.758.682 caratteri**;
- **181 URL esterni distinti**;
- **8 file con LaTeX**;
- **1.093 pagine PDF**;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità è la densità di valore per pagina.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
python scripts/build.py
```

Il lint verifica continuità dei capitoli, prefissi, heading, file vuoti, TODO/FIXME/TBD, URL contaminati, grafie ASCII legacy, formule/LaTeX e conteggio parole.

### Warning residuo

Resta un solo warning globale:

- notazione matematica/LaTeX in **8 file**.

Prima della release bisognerà usare un renderer matematico o normalizzare editorialmente le formule residue.

## 3. Convenzione casi e fonti

### Caso reale documentato

Richiede organizzazione/evento identificabile, fonte pubblica attendibile, claim proporzionato e nessuna promozione indebita di associazione a causalità.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Fonti

La review privilegia standard/governi, documentazione ufficiale, letteratura accademica riconosciuta e fonti primarie per i casi pubblici.

Prima della release resta un audit globale dei **181 URL** per link, redirect, supporto del claim e uniformità delle note.

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
| 16 — Storytelling/dashboard | **Revisionato** | **Decision Communication Pack**. |
| 17 — Casi end-to-end | **Revisionato** | **Capstone Routing Canvas / Capstone Case File**. |
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
→ Decision Communication Pack
```

Il Capitolo 17 non aggiunge un deliverable tecnico obbligatorio alla catena: introduce il **Capstone Routing Canvas**, che serve a selezionare quali artefatti attivare in base a decisione, failure cost, claim necessario, readiness e stop rule.

Non ogni analisi richiede tutti gli artefatti. Sono un vocabolario operativo per rischi differenti.

## 6. Confini concettuali principali

### 0 / 14 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** workflow operativo, boundary, verification, eval, privacy e auditability;
- **19:** conseguenze su skill, ruoli e carriera.

### 3 / 4 / 5 — qualità, pattern, inferenza

- **3:** il dato è utilizzabile?
- **4:** quale struttura mostra?
- **5:** quanto possiamo generalizzare e con quale incertezza?

### 5 / 8 / 9 — inferenza, identificazione, esperimento

- **5:** teoria inferenziale;
- **8:** identification assumptions;
- **9:** preservare il confronto in un esperimento reale.

### 11 / 12 / 13 — significato, flusso, strumento

- **11:** che cosa deve significare il dataset → Analytical Data Contract;
- **12:** da dove arriva e con quali garanzie → Data Flow Architecture Map;
- **13:** quale ambiente è proporzionato → Tooling Decision Record.

### 14 / 15 / 16 — controllo, decisione, comunicazione

- **14:** quale claim ha diritto di uscire dal workflow;
- **15:** quale alternativa scegliere e perché;
- **16:** come comprimere il Decision Record senza rafforzare il claim, nascondere l'incertezza o perdere le alternative.

```text
AI Analysis Control Sheet
→ Decision Record
→ Decision Communication Pack
```

### 16 / 17 — comunicazione vs capstone

- **16:** progetta la superficie con cui la decisione viene capita;
- **17:** seleziona e integra soltanto le evidenze necessarie in problemi end-to-end senza dire in anticipo quale tecnica usare.

### 17 / 18 — singola decisione vs sistema ricorrente

- **17:** come risolvere bene una decisione complessa una volta;
- **18:** quando e come quella capacità deve diventare un sistema ripetibile con ownership, reliability, change management e cost control.

### 13 / 18 — workflow locale vs operating model

- **13:** scelta/migrazione del singolo workflow;
- **18:** standard e ownership organizzativi che permettono di scalare.

## 7. Note review Capitoli 15–17

### Capitolo 15 — Decision Record

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

Punti chiave: alternative reali, ACT/PILOT/WAIT/BUY INFORMATION/ABANDON, evidence threshold distinto da switching threshold, robustness of ranking, pre-mortem, learning contract e distinzione decision/execution/outcome quality.

### Capitolo 16 — Decision Communication Pack

```text
Decision Record
→ audience
→ decision question
→ decision requested
→ headline / claim level
→ evidence hierarchy
→ Visual Encoding Contract
→ Context Contract
→ uncertainty / switching value
→ alternatives
→ Visual Integrity Gate
→ Accessibility Gate
→ meeting plan
→ provenance
```

Punti chiave: evidence promotion, ruoli `orient / compare / diagnose / decide / verify`, dashboard per cadence, salience/precision budget, uncertainty rispetto allo switching value, Visual Integrity Gate, accessibility come redundant encoding e Communication Readiness Gate.

### Capitolo 17 — Capstone Routing Canvas

Il capitolo è stato trasformato da catalogo di tecniche a laboratorio di **evidence routing**.

Schema canonico:

```text
messy question
→ decision
→ failure cost
→ claim needed
→ readiness
→ competing explanations
→ method gate
→ evidence
→ alternatives
→ uncertainty
→ decision
→ communication
→ outcome review
```

Il **Capstone Routing Canvas** usa:

```text
decision
→ failure cost
→ claim needed
→ readiness
→ necessary deliverables
→ stop rule
```

Concetti rafforzati:

- il titolo del caso non suggerisce più automaticamente la tecnica;
- **method gate**: ogni tecnica deve chiudere un rischio decisionale esplicito;
- deliverable necessari vs deliverable volutamente saltati;
- Evidence Ledger: `observed / inferred / still unknown`;
- stop state: `DECIDE / PILOT / WAIT FOR X / BUY INFORMATION / NO ACTION / NOT IDENTIFIED`;
- prediction ≠ persuadibilità ≠ economics nel churn;
- elasticity estimate ≠ pricing policy;
- attribution ≠ incrementality ≠ marginal ROI;
- forecast accuracy ≠ decision loss;
- anomaly ≠ incident root cause e ruolo del semantic drift;
- experiment significance ≠ experiment trustworthiness ≠ rollout policy;
- unit economics richiede denominatore e cost boundary coerenti;
- outcome review separata da decision quality ex ante;
- Capstone Rubric su framing, semantica, hypothesis discipline, method selection, uncertainty, economics, stop rule, communication e outcome review.

Casi simulati/compositi dichiarati esplicitamente: Orion Living, NorthPeak, Vectora, Helio Market, Aster Components, PulseNote, Arcadia Parcel, VelaPay, Atlas Streaming, NovaCompute e OrbisMarket.

Casi/fonti pubbliche documentate usate con claim limitato alla fonte:

- Microsoft Customer Insights per transactional churn prediction;
- Google Cloud Hoff e Freshworks per integrazione marketing/attribution/ROI;
- BMW Group su AWS per shortage, semiconductor demand e supply allocation;
- Coca-Cola Andina su AWS per inventory/distribution/delivery visibility;
- AWS Cloud Financial Management per driver-based forecasting;
- Microsoft Research per Sample Ratio Mismatch;
- NXP su AWS per unit-cost analysis e FinOps.

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
→ capstone
→ scala
→ futuro
```

## 9. Lavori ancora necessari prima della release

- review Capitoli 18–19;
- audit link/fonti globale;
- formula rendering;
- frontespizio, copyright/licenza, autore e bio;
- “come usare il libro” e indice automatico;
- glossario/bibliografia/indice fonti;
- ringraziamenti e numero/versione release;
- proofread ortografico finale;
- controllo tabelle, code block, footnote e page break nel PDF/DOCX.

## 10. Release gate

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di indice, formule, tabelle, codice, fonti, casi reali/compositi, ripetizioni, ortografia, footnote, page break e continuità dei deliverable canonici.

## 11. Prossimo blocco

La review continua dal **Capitolo 18 — Costruire un sistema analitico che scala**.

Direzione editoriale:

```text
recurring decision
→ criticality
→ product boundary
→ metric/data ownership
→ reliability target
→ test/observability
→ change management
→ incident/recovery
→ self-service contract
→ cost-to-serve
→ adoption
→ operating model
→ review / retirement
```

Deliverable previsto: **Analytics Operating Contract**.

Il Capitolo 18 non deve ripetere l'architettura del Capitolo 12, la tool selection del 13 o l'AI governance del 14. Deve spiegare come una capacità analitica ricorrente diventa un prodotto operativo affidabile con ownership, SLO, change control, incident management, economics e criteri di retirement.