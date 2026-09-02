# Editorial audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review editoriale capitolo-per-capitolo: **COMPLETATA, Capitoli 0–19**.
- Nessun capitolo resta nello stato `Da revisionare`.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.
- Fase corrente del progetto: **release editorial pass**.

### Ultima build validata

Dopo la review del Capitolo 19:

- **20 capitoli**;
- **321 file Markdown**;
- **251.152 parole stimate**;
- **1.860.563 caratteri**;
- **190 URL esterni distinti**;
- **7 file con LaTeX**;
- **1.178 pagine PDF**;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità resta la densità di valore per pagina e la qualità editoriale della release.

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

- notazione matematica/LaTeX in **7 file**.

Prima della release bisognerà usare un renderer matematico o normalizzare editorialmente le formule residue.

## 3. Convenzione casi e fonti

### Caso reale documentato

Richiede organizzazione/evento identificabile, fonte pubblica attendibile, claim proporzionato e nessuna promozione indebita di associazione a causalità.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Fonti

La review privilegia standard/governi, documentazione ufficiale, letteratura accademica riconosciuta e fonti primarie per i casi pubblici.

Prima della release resta un audit globale dei **190 URL** per:

- raggiungibilità;
- redirect;
- supporto reale del claim;
- preferenza per fonte primaria;
- data/freshness quando rilevante;
- uniformità della presentazione delle fonti.

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
| 19 — Data Analyst 2026–2035 | **Revisionato** | **Personal Career Operating Plan**. |

## 5. Vocabolario operativo del libro

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

Il Capitolo 18 introduce l'**Analytics Operating Contract**, che entra in gioco quando una capacità ricorrente merita di diventare un servizio operativo.

Il Capitolo 19 porta la stessa logica sul professionista attraverso il **Personal Career Operating Plan**.

Questi artefatti non sono una checklist obbligatoria da applicare sempre. Sono un vocabolario operativo per rischi differenti.

## 6. Confini concettuali principali

### 0 / 14 / 18 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** progettazione e verifica del singolo workflow AI-assisted;
- **18:** agenti ricorrenti come servizi operativi con lifecycle, monitoring e revoke/retire;
- **19:** conseguenze su skill, delegation boundary, deskilling, seniority e carriera.

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

### 18 / 19 — capacità organizzativa vs capacità professionale

- **18:** come l'organizzazione rende affidabile e riutilizzabile una promessa analitica;
- **19:** come il professionista costruisce un portafoglio di capacità robusto quando cambia il costo dei task e aumenta la delega all'AI.

## 7. Note review Capitoli 17–19

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

Punti chiave:

- method gate: ogni tecnica deve chiudere un rischio decisionale esplicito;
- deliverable necessari vs volutamente saltati;
- Evidence Ledger: `observed / inferred / still unknown`;
- stop state: `DECIDE / PILOT / WAIT FOR X / BUY INFORMATION / NO ACTION / NOT IDENTIFIED`;
- outcome review distinta dalla decision quality ex ante.

### Capitolo 18 — Analytics Operating Contract

Percorso:

```text
recurring decision
→ promotion gate
→ criticality tier
→ product boundary
→ ownership
→ reliability contract
→ testing pyramid
→ serving/degraded states
→ incident/recovery
→ change/semantic diff
→ self-service
→ adoption ladder
→ cost-to-serve
→ agent lifecycle
→ review/retirement
```

Punti chiave:

- `T0 Exploratory / T1 Team / T2 Business-critical / T3 High-consequence`;
- decision/semantic/product/source/governance ownership separate;
- SLI/SLO ed error budget legati al consumer;
- `READY / READY WITH CAVEATS / STALE BUT SERVABLE / PARTIAL / BLOCKED`;
- semantic diff e Compatibility Contract;
- testing pyramid basata sui failure mode;
- adoption ladder: `availability → discoverability → usage → effective use → decision embedding → outcome`;
- Agent Operating Profile: register, evaluate, deploy, monitor, incident, change, revoke/retire;
- retirement come parte del lifecycle.

Il caso Helios Mobility è simulato/composito.

### Capitolo 19 — Personal Career Operating Plan

Il capitolo finale è stato trasformato da previsione sul mercato del lavoro a **career operating model robusto all'incertezza tecnologica**.

Percorso:

```text
task exposure
→ responsibility moat
→ delegation boundary
→ semantic leverage
→ Capability Portfolio
→ career optionality
→ decision span
→ specialization direction
→ seniority spans
→ verification reserve
→ scenario stress test
→ Personal Career Operating Plan
```

Concetti principali:

- task exposure distinto da scomparsa della professione;
- **responsibility moat**: valore che resta in semantica, risk/judgment, stakeholder e outcome accountability;
- tecnica distinta in `execution / verification / design skill`;
- agentic leverage come evidenza utile per unità di attenzione, non output volume;
- Delegation Boundary `A–E`, da human execution a bounded autonomous service;
- delegation depth deve seguire verification depth;
- **semantic leverage**: l'interfaccia naturale aumenta il valore della formalizzazione del significato;
- Capability Portfolio: `breadth / depth / domain / operating responsibility`;
- **escalation literacy** come competenza senior;
- skill portfolio con half-life differenti e novelty/FOMO filter;
- **career optionality** su tool, domain, method, role e AI;
- **decision span** da output a decision system;
- specializzazioni espresse come `problema × metodo × operating responsibility`, non come previsione di job title;
- seniority attraverso `ambiguity span / failure span / coordination span / decision span`;
- experience compression apparente: output senior-looking non equivale a esperienza;
- **verification reserve** e deliberate practice contro il deskilling;
- scenario planning 2035: agent-rich, high-regulation, low-maturity/partial automation;
- Personal Career Operating Plan con stati `STRONG / DEVELOPING / DEPENDENT / UNKNOWN` e azioni `KEEP / DELEGATE MORE / REBUILD SKILL / SPECIALIZE / ESCALATE / RETIRE`.

Fonti principali: ILO *Generative AI and jobs: A 2025 update*, World Economic Forum *Future of Jobs Report 2025*, Microsoft *Work Trend Index 2026*, Microsoft Research CHI 2025 sul critical thinking nel knowledge work.

La conclusione finale torna al Capitolo 0 senza framing difensivo: il punto non è preservare il vecchio lavoro, ma usare più capacità senza perdere il controllo su intento, significato, evidenza, rischio e decisione.

Definizione finale mantenuta:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo principale:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

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
→ futuro / carriera
```

La review capitolo-per-capitolo è conclusa.

## 9. Release editorial pass — lavori ancora necessari

### A. Fonti e factual audit

- verificare tutti i **190 URL**;
- rimuovere link morti o redirect inutili;
- confermare che ogni claim sia effettivamente supportato;
- privilegiare fonti primarie quando disponibili;
- uniformare la presentazione delle fonti;
- verificare date e wording dei casi pubblici.

### B. Formula rendering

- individuare i **7 file LaTeX** residui;
- decidere se renderizzare matematicamente o convertire in notazione editoriale;
- controllare formula wrapping in PDF e DOCX.

### C. Front matter e navigazione

- frontespizio;
- autore e bio;
- copyright/licenza;
- versione/edizione;
- “come usare questo libro”;
- legenda casi reali/compositi;
- indice automatico;
- eventuale prefazione/introduzione editoriale.

### D. Reference layer

- glossario;
- bibliografia/indice fonti;
- eventuale indice dei casi reali;
- cross-reference tra deliverable canonici;
- elenco dei template operativi riutilizzabili.

### E. Proofread e consistency pass

- ortografia/punteggiatura;
- inglesismi e capitalizzazione;
- termini canonici;
- rimandi tra capitoli;
- ripetizioni residue;
- numeri e unità;
- caso reale vs composito;
- claim level e causal wording.

### F. Layout QA

- tabelle larghe;
- code block;
- formule;
- blockquote;
- heading/page break;
- widows/orphans dove possibile;
- footnote/link;
- indice;
- numerazione pagine;
- resa PDF e DOCX.

## 10. Release gate

Prima di una release candidata:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di:

- fonti;
- formule;
- tabelle;
- codice;
- casi reali/compositi;
- ortografia;
- footnote/link;
- page break;
- indice;
- continuità dei deliverable canonici.

## 11. Prossimo blocco

La fase di **chapter review è conclusa**.

Il prossimo lavoro editoriale raccomandato è il **source/factual audit globale**, perché può modificare claim e riferimenti prima dell'ultimo proofread tipografico.

Ordine consigliato:

```text
1. source/factual audit
2. formula rendering
3. front matter + indice + reference layer
4. proofread globale
5. layout QA PDF/DOCX
6. release candidate
```

Da questo punto l'obiettivo non è aggiungere altro corpo al libro, salvo lacune dimostrate dall'audit. È trasformare il manoscritto revisionato in una **release editoriale verificata e pubblicabile**.