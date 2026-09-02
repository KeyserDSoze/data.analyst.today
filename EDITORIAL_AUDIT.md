# Editorial audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto. Markdown resta la source of truth.

## 1. Stato attuale

- Corpo principale **Capitoli 0–19**: **COMPLETO**.
- Review editoriale capitolo-per-capitolo: **COMPLETATA**.
- Source/factual audit globale: **COMPLETATO**; dettaglio in `SOURCE_FACTUAL_AUDIT.md`.
- Normalizzazione delle formule/LaTeX residue: **COMPLETATA**.
- Front matter e navigazione: **COMPLETATI**.
- Reference layer: **COMPLETATO** nella struttura iniziale di release.
- CI attiva su `main` con normalizzazione, lint e build Markdown/DOCX/PDF.
- Fase corrente: **release editorial pass — proofread globale e consistency pass**.

### Ultima build validata

Run Book CI sull'head `6eb347630ba2f283bf79a6b2303ed8f9d37ce8c5`: **SUCCESS**.

Corpo principale:

- **20 capitoli**;
- **321 file Markdown**;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con notazione matematica/LaTeX rilevata dal linter**;
- **0 file con accenti ASCII legacy**.

Apparati di release:

- **3 file front matter**;
- **2 file reference curati**;
- indice capitoli generato automaticamente;
- indice casi reali documentati generato automaticamente;
- indice delle **190 fonti URL distinte** generato automaticamente;
- **1.210 pagine PDF** nella build tecnica corrente;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità resta densità di valore, affidabilità editoriale e leggibilità della release.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
python scripts/build.py
```

Il lint del corpo verifica continuità dei capitoli, prefissi, heading, file vuoti, TODO/FIXME/TBD, URL contaminati, grafie ASCII legacy, formule/LaTeX e conteggi strutturali.

Il builder:

```text
book.yml / frontespizio
→ front_matter/
→ indice capitoli generato
→ chapters/
→ reference/
→ indice casi reali generato
→ indice fonti generato
→ Markdown / DOCX / PDF
```

## 3. Formula cleanup — completato

Il precedente warning globale sui **7 file LaTeX** è stato eliminato senza introdurre un renderer matematico aggiuntivo.

File normalizzati:

- `chapters/004_chapter/016_boxplot_iqr.md`;
- `chapters/005_chapter/003_conditional_probability.md`;
- `chapters/005_chapter/004_independence.md`;
- `chapters/005_chapter/006_expected_value_variance.md`;
- `chapters/005_chapter/008_bayesian_update.md`;
- `chapters/005_chapter/011_standard_error.md`;
- `chapters/005_chapter/013_confidence_intervals.md`.

La convenzione è notazione Unicode leggibile in inline code, per esempio `P(A|B)`, `Σ`, `√n`, `x̄`, senza dipendenze tipografiche nuove.

## 4. Source/factual audit — completato

L'audit globale ha verificato:

1. raggiungibilità e destinazione;
2. autorità della fonte;
3. supporto reale del claim;
4. livello del claim;
5. caso reale documentato vs simulato/composito;
6. freshness quando rilevante;
7. canonicalizzazione degli URL.

Il pass ha combinato audit tematico, sweep bottom-up delle sezioni `Fonte:` / `Fonti:` e source hygiene globale.

Correzioni principali:

- path Microsoft Research legacy → URL canonici;
- vecchio static link Duolingo → copia primaria SEC;
- canonicalizzazione Vertex AI;
- link scikit-learn classification threshold versionato → `/stable/`;
- verifica dei casi pubblici e dei claim causali senza nuove riscritture sostantive nell'ultimo sweep.

Non risultano URL `http://` nel manoscritto né link contaminati da `utm_source=chatgpt.com`.

### Recheck al release gate

Non va ripetuto l'intero audit. Prima della release candidata vanno ricontrollate soltanto fonti con freshness o stato editoriale variabile, soprattutto:

- Government Analysis Function, *Communicating quality, uncertainty and change*, attualmente pubblicata ma indicata come pagina sotto revisione;
- fonti 2025–2026 usate per trend AI/lavoro quando il claim dipende dall'attualità.

## 5. Front matter e navigazione — completati

Sorgenti curate:

- `front_matter/001_come_usare_questo_libro.md`;
- `front_matter/002_legenda_editoriale.md`;
- `front_matter/003_nota_autore_edizione.md`.

La build genera inoltre l'**Indice dei capitoli** direttamente dai primi H1 delle introduzioni, evitando un indice manuale che possa divergere dal manoscritto.

Restano volutamente non definiti fino al release gate:

- copyright definitivo;
- licenza definitiva.

Non vengono inventate condizioni di utilizzo nel front matter.

## 6. Reference layer — completato nella struttura di release

Sorgenti curate:

- `reference/001_glossario.md` — glossario dei concetti operativi ricorrenti;
- `reference/002_artefatti_operativi.md` — indice dei deliverable canonici con capitolo e rischio protetto.

Sezioni generate:

- **Indice dei casi reali documentati** — derivato dagli heading effettivi del manoscritto;
- **Indice delle fonti** — derivato dai 190 URL distinti del corpo e ordinato per dominio.

Questa scelta evita di mantenere manualmente una seconda bibliografia scollegata dalle citazioni nel testo.

## 7. Convenzione casi e claim

### Caso reale documentato

Richiede organizzazione/evento identificabile, fonte pubblica attendibile e claim proporzionato.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Claim level

Il proofread deve preservare la distinzione:

```text
descrittivo
→ diagnostico
→ predittivo
→ causale
→ decisionale
```

La forza grammaticale deve restare coerente con il livello di evidenza.

## 8. Stato capitolo per capitolo

| Capitolo | Stato | Deliverable / funzione |
|---|---|---|
| 0 — Al timone | **Revisionato** | responsabilità, delega, verifica, stop condition, trust levels |
| 1 — Tutto è cambiato | **Revisionato** | catena analitica canonica e tipi di domanda |
| 2 — Problema business → analitico | **Revisionato** | **Analytical Brief** |
| 3 — Capire i dati | **Revisionato** | **Data Readiness Review** |
| 4 — Statistica descrittiva ed EDA | **Revisionato** | **EDA Evidence Map** |
| 5 — Probabilità e incertezza | **Revisionato** | **Uncertainty Brief** |
| 6 — Lifecycle analysis | **Revisionato** | **Lifecycle Diagnostic Map** |
| 7 — Time series e forecasting | **Revisionato** | **Temporal Decision Brief** |
| 8 — Causalità | **Revisionato** | **Causal Identification Brief** |
| 9 — Experimentation | **Revisionato** | **Experiment Contract** |
| 10 — Predictive modeling | **Revisionato** | **Predictive Decision Card** |
| 11 — SQL e data modeling | **Revisionato** | **Analytical Data Contract** |
| 12 — Data architecture | **Revisionato** | **Data Flow Architecture Map** |
| 13 — Tool selection | **Revisionato** | **Tooling Decision Record** |
| 14 — AI-assisted analytics | **Revisionato** | **AI Analysis Control Sheet** |
| 15 — Insight e decisione | **Revisionato** | **Decision Record** |
| 16 — Storytelling/dashboard | **Revisionato** | **Decision Communication Pack** |
| 17 — Casi end-to-end | **Revisionato** | **Capstone Routing Canvas / Capstone Case File** |
| 18 — Sistema analitico che scala | **Revisionato** | **Analytics Operating Contract** |
| 19 — Data Analyst 2026–2035 | **Revisionato** | **Personal Career Operating Plan** |

## 9. Vocabolario operativo

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

Il Capitolo 17 introduce il **Capstone Routing Canvas**, il Capitolo 18 l'**Analytics Operating Contract**, il Capitolo 19 il **Personal Career Operating Plan**.

Gli artefatti sono un vocabolario di rischi, non una checklist obbligatoria.

## 10. Confini concettuali da proteggere nel proofread

### 0 / 14 / 18 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** workflow AI-assisted e verifica del singolo output/processo;
- **18:** agenti ricorrenti come servizi operativi;
- **19:** skill, delegation boundary, deskilling, seniority e carriera.

### 3 / 4 / 5 — qualità, pattern, inferenza

- **3:** il dato è utilizzabile?
- **4:** quale struttura mostra?
- **5:** quanto possiamo generalizzare e con quale incertezza?

### 5 / 8 / 9 — inferenza, identificazione, esperimento

- **5:** teoria inferenziale;
- **8:** identification assumptions;
- **9:** preservare il confronto in un esperimento reale.

### 11 / 12 / 13 — significato, flusso, strumento

- **11:** che cosa deve significare il dataset;
- **12:** da dove arriva e con quali garanzie;
- **13:** quale ambiente è proporzionato.

### 14 / 15 / 16 — controllo, decisione, comunicazione

```text
AI Analysis Control Sheet
→ Decision Record
→ Decision Communication Pack
```

### 17 / 18 / 19 — decisione, sistema, professionista

- **17:** evidence routing per una decisione complessa;
- **18:** capacità ricorrente come servizio affidabile;
- **19:** portafoglio professionale robusto all'incertezza tecnologica.

## 11. Tesi e chiusura da preservare

Definizione finale:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo principale:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## 12. Release editorial pass — stato

### A. Chapter review — **COMPLETATO**

### B. Source/factual audit — **COMPLETATO**

### C. Formula cleanup — **COMPLETATO**

### D. Front matter + navigazione — **COMPLETATO**

### E. Reference layer — **COMPLETATO**

### F. Proofread + consistency pass — **IN CORSO / PROSSIMO BLOCCO**

Controllare in modo globale:

- ortografia e punteggiatura;
- inglesismi e capitalizzazione;
- termini canonici;
- rimandi tra capitoli;
- ripetizioni residue;
- numeri e unità;
- concordanze;
- caso reale vs composito;
- claim level e causal wording;
- coerenza dei nomi degli artefatti.

### G. Layout QA — **DA FARE**

Controllare:

- tabelle larghe;
- code block;
- notazione matematica Unicode;
- blockquote;
- heading/page break;
- widows/orphans dove possibile;
- link e note;
- indice;
- numerazione pagine;
- resa PDF e DOCX.

## 13. Release gate

Prima della release candidata:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di:

- fonti freshness-sensitive;
- tabelle e codice;
- casi reali/compositi;
- ortografia;
- link/note;
- page break e indice;
- continuità dei deliverable canonici;
- prime/ultime pagine del PDF e del DOCX.

## 14. Ordine aggiornato

```text
1. proofread globale + consistency pass
2. layout QA PDF/DOCX
3. recheck fonti freshness-sensitive
4. release candidate
```

Da questo punto l'obiettivo non è aggiungere altro corpo al libro, salvo lacune dimostrate. È ridurre attrito, inconsistenza e rischio residuo fino a una release editoriale verificata e pubblicabile.
