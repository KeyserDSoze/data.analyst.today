# Editorial audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review completata: **Capitoli 0–18**.
- Da revisionare: **Capitolo 19**.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.

### Ultima build validata

Dopo la review del Capitolo 18:

- **20 capitoli**;
- **321 file Markdown**;
- **246.711 parole stimate**;
- **1.824.203 caratteri**;
- **190 URL esterni distinti**;
- **8 file con LaTeX**;
- **1.148 pagine PDF**;
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

Prima della release resta un audit globale dei **190 URL** per link, redirect, supporto del claim e uniformità delle note.

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
| 18 — Sistema analitico che scala | **Revisionato** | **Analytics Operating Contract**. |
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

Il Capitolo 17 introduce il **Capstone Routing Canvas**, che seleziona quali artefatti attivare in base a decisione, failure cost, claim necessario, readiness e stop rule.

Il Capitolo 18 introduce l'**Analytics Operating Contract**, che entra in gioco quando una capacità analitica ricorrente merita di diventare un servizio operativo.

```text
recurring decision
→ criticality tier
→ product boundary
→ ownership
→ SLI/SLO
→ tests/observability
→ serving/degraded state
→ incident/recovery
→ change/compatibility
→ adoption
→ cost-to-serve
→ AI/agent lifecycle
→ review / retirement
```

Non ogni analisi richiede tutti gli artefatti. Sono un vocabolario operativo per rischi differenti.

## 6. Confini concettuali principali

### 0 / 14 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** workflow operativo, boundary, verification, eval, privacy e auditability;
- **19:** conseguenze su skill, ruoli, apprendimento e carriera.

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
- **18:** quando e come quella capacità deve diventare un sistema ripetibile con ownership, reliability, change management, adoption e cost control.

### 12 / 18 — architettura vs operating contract

- **12:** come il dato si muove dalla sorgente al consumer e con quali failure boundary;
- **18:** quale promessa operativa facciamo al consumer, chi ne risponde e come gestiamo failure/change/lifecycle.

### 13 / 18 — workflow locale vs operating model

- **13:** scelta/migrazione del singolo workflow;
- **18:** standard e ownership organizzativi che permettono di scalare.

### 14 / 18 — AI workflow vs AI service

- **14:** progettare e verificare una singola analisi AI-assisted;
- **18:** operare agenti ricorrenti con registry, eval, deploy, monitoring, incident, change, revoke e retirement.

### 18 / 19 — capacità organizzativa vs carriera

- **18:** come l'organizzazione rende l'analytics affidabile e riutilizzabile;
- **19:** come il professionista costruisce competenze resilienti dentro un sistema sempre più automatizzato.

## 7. Note review Capitoli 17–18

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

- il titolo del caso non suggerisce automaticamente la tecnica;
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
- outcome review separata da decision quality ex ante.

### Capitolo 18 — Analytics Operating Contract

Il capitolo è stato separato dall'architettura del Capitolo 12 e dall'AI workflow governance del Capitolo 14.

Percorso:

```text
recurring decision
→ promotion gate
→ criticality tier
→ product boundary
→ ownership
→ reliability contract
→ testing pyramid
→ serving / degraded states
→ incident / recovery
→ change / semantic diff
→ self-service
→ adoption ladder
→ cost-to-serve
→ agent lifecycle
→ review / retirement
```

Concetti rafforzati:

- `T0 Exploratory / T1 Team / T2 Business-critical / T3 High-consequence`;
- ownership separata in decision, semantic, product/technical, source e governance owner;
- SLI/SLO analitici ed error budget legati al consumer;
- stati `READY / READY WITH CAVEATS / STALE BUT SERVABLE / PARTIAL / BLOCKED`;
- pipeline health distinta da data/decision readiness;
- change classification: technical, structural, semantic, operating;
- Compatibility Contract e semantic diff;
- self-service come autonomia entro product boundary e standard condivisi;
- CI/CD con shadow/parallel run e recovery/replay;
- testing pyramid basata sui failure mode;
- cost allocation, freshness economics e cost-to-serve;
- adoption ladder: `availability → discoverability → usage → effective use → decision embedding → outcome`;
- Agent Operating Profile: register, evaluate, deploy, monitor, incident, change, revoke/retire;
- human approval distinto da approval theater;
- retirement come parte del lifecycle.

Il caso finale Helios Mobility è simulato/composito e dimostra un sistema che degrada esplicitamente durante un failure di sorgente, gestisce un semantic breaking change e riduce temporaneamente l'autorità di un agente dopo un failure di dipendenza.

Fonti principali: Google SRE, Microsoft Fabric Adoption Roadmap, NIST AI RMF/Generative AI Profile, AWS data-product/data-mesh guidance e FinOps Foundation.

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

- review Capitolo 19;
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

La review continua dal **Capitolo 19 — Il Data Analyst nel 2026–2035**.

Direzione editoriale:

```text
stable responsibility
→ task exposure
→ human/agent comparative advantage
→ skill portfolio
→ verification depth
→ domain leverage
→ learning system
→ deskilling safeguards
→ career optionality
→ personal operating plan
```

Il Capitolo 19 non deve prevedere quali tool vinceranno nel 2035 e non deve ripetere il Capitolo 0. Deve aiutare il lettore a costruire un **career operating model** robusto all'incertezza tecnologica: quali attività delegare, quali competenze preservare per poter verificare, come allenare judgment e come misurare il proprio valore rispetto agli outcome invece che alla quantità di output prodotto.