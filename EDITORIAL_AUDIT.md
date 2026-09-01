# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review completata: **Capitoli 0–16**.
- Da revisionare: **Capitoli 17–19**.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.

### Ultima build validata

Dopo la review del Capitolo 16:

- **20 capitoli**;
- **321 file Markdown**;
- **230.523 parole stimate**;
- **1.699.234 caratteri**;
- **177 URL esterni distinti**;
- **8 file con LaTeX**;
- **1.051 pagine PDF**;
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

Prima della release resta un audit globale dei **177 URL** per link, redirect, supporto del claim e uniformità delle note.

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
| 17 — Casi end-to-end | **Da revisionare** | Capstone: selezionare e integrare i deliverable necessari. |
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
- **16:** come comprimere quel Decision Record senza rafforzare il claim, nascondere l'incertezza o perdere le alternative.

```text
AI Analysis Control Sheet
→ Decision Record
→ Decision Communication Pack
```

### 16 / 17 — comunicazione vs capstone

- **16:** progetta la superficie con cui la decisione viene capita;
- **17:** mette insieme framing, dati, metodi, decisione e comunicazione in problemi end-to-end senza dire in anticipo quale tecnica usare.

### 13 / 18 — workflow locale vs operating model

- **13:** scelta/migrazione del singolo workflow;
- **18:** standard e ownership organizzativi che permettono di scalare.

## 7. Note review Capitoli 15–16

### Capitolo 15

Il **Decision Record** usa:

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

### Capitolo 16

Il centro è la **Decision Communication Pack**:

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

Concetti rafforzati:

- discovery artifacts vs decision artifacts ed **evidence promotion**;
- ruoli `orient / compare / diagnose / decide / verify`;
- dashboard operative, diagnostiche e decisionali separate per cadence;
- salience budget e precision budget;
- uncertainty comunicata rispetto allo switching value;
- executive summary derivato dal Decision Record;
- annotazioni di eventi distinte da spiegazioni causali;
- Visual Integrity Gate: scale, periodi, denominatori, dual axis, cumulative/run-rate, opposite framing;
- table-first per lookup/audit e small multiples per pattern comparabili;
- dashboard anti-pattern inclusi KPI wall, slicer cemetery, traffic-light theater, hover-only truth e dashboard-as-database;
- meeting communication: claim/evidence/caveat/ask e classificazione delle challenge;
- accessibilità come **redundant encoding**, con WCAG 2.2, alt text, keyboard, contrasto e alternative tabellari/testuali;
- Communication Readiness Gate: **READY / READY WITH CAVEATS / NOT READY**.

Il caso finale NorthRiver Logistics è simulato/composito e sostituisce il precedente caso margin/promotion per evitare sovrapposizione con il Capitolo 15.

Fonti principali: W3C WCAG 2.2, Government Analysis Function, Office for National Statistics e Microsoft Learn.

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

- review Capitoli 17–19;
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

La review continua dal **Capitolo 17 — Casi end-to-end di Data Analysis**.

Direzione editoriale:

```text
messy business question
→ risk/decision classification
→ choose only necessary deliverables
→ evidence production
→ competing explanations
→ decision
→ communication
→ measurement / learning
```

Il Capitolo 17 deve diventare un **capstone**, non un catalogo di tecniche. Il lettore non deve sapere dal titolo del caso se serviranno forecasting, causalità, experiment, predictive modeling o soltanto una buona decomposition.