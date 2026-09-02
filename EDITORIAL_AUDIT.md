# Editorial audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto. Markdown resta la source of truth.

## 1. Stato attuale

- Corpo principale **Capitoli 0–19**: **COMPLETO**.
- Review editoriale capitolo-per-capitolo: **COMPLETATA**.
- Source/factual audit globale: **COMPLETATO**; dettaglio in `SOURCE_FACTUAL_AUDIT.md`.
- Recheck release-gate delle fonti freshness-sensitive: **COMPLETATO**.
- Normalizzazione delle formule/LaTeX residue: **COMPLETATA**.
- Front matter e navigazione: **COMPLETATI**.
- Reference layer: **COMPLETATO**.
- Proofread globale / consistency pass di release: **COMPLETATO**.
- Layout QA PDF/DOCX: **COMPLETATO**.
- CI attiva su `main` con normalizzazione, lint strict, build Markdown/DOCX/PDF e controlli sugli output generati.
- Fase corrente: **release candidate**.

### Ultima build validata

Run Book CI sull'head `ccff96add69f53af5393e03918068a164288fb83`: **SUCCESS**.

Corpo principale:

- **20 capitoli**;
- **321 file Markdown**;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con notazione matematica/LaTeX rilevata dal linter**;
- **0 file con accenti ASCII legacy**.

Apparati e output di release:

- **3 file front matter**;
- **2 file reference curati**;
- indice capitoli generato automaticamente;
- indice casi reali documentati generato automaticamente;
- indice delle **190 fonti URL distinte** generato automaticamente;
- note Markdown risolte in riferimenti numerici e sezioni **Note e fonti** a fine capitolo;
- **389 bookmark PDF** per navigazione a capitoli e sezioni numerate;
- **213/213 tabelle DOCX** con header ripetibile su page break;
- frontespizio PDF senza numero pagina stampato;
- frontespizio DOCX senza footer visibile;
- **1.209 pagine PDF** nella build tecnica corrente;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità resta densità di valore, affidabilità editoriale e leggibilità della release.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Il lint verifica continuità dei capitoli, prefissi, heading, file vuoti, TODO/FIXME/TBD, URL contaminati, grafie ASCII legacy, formule/LaTeX, termini canonici e conteggi strutturali. I warning editoriali sono errori in CI grazie a `--strict`.

Dopo la build, la CI verifica inoltre che:

- non restino footnote Markdown `[^...]` irrisolte nell'assemblato;
- il PDF contenga un outline di navigazione;
- il DOCX non contenga footnote Markdown irrisolte;
- tutte le tabelle DOCX abbiano repeating header;
- il frontespizio DOCX usi un first-page footer separato e vuoto.

Il builder:

```text
book.yml / frontespizio
→ front_matter/
→ indice capitoli generato
→ chapters/
→ note e fonti risolte per capitolo
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

### Recheck release-gate — completato il 2 settembre 2026

Sono state ricontrollate soltanto le fonti con stato editoriale o freshness variabile, senza ripetere l'intero audit dei 190 URL.

Risultato:

- ILO, *Generative AI and jobs: A 2025 update*: ancora raggiungibile e coerente con il framing esposizione/trasformazione;
- World Economic Forum, *Future of Jobs Report 2025*: ancora raggiungibile e coerente con i claim sulle skill;
- Microsoft, *2026 Work Trend Index*: ancora raggiungibile e coerente con il framing su agenti, execution e human agency;
- Microsoft Research, CHI 2025 sul critical thinking: ancora raggiungibile; il manoscritto mantiene correttamente linguaggio associativo/self-report e non causale;
- Government Analysis Function, *Communicating quality, uncertainty and change*: ancora pubblicata e ancora marcata **under review**; continua a supportare il claim del libro e non richiede una sostituzione nella release corrente;
- NIST AI RMF 1.0 resta la versione pubblicata usata dal manoscritto; la revisione in corso non rende errato il riferimento alla versione 1.0.

**Esito: nessuna correzione al manoscritto richiesta dal freshness recheck.**

## 5. Front matter e navigazione — completati

Sorgenti curate:

- `front_matter/001_come_usare_questo_libro.md`;
- `front_matter/002_legenda_editoriale.md`;
- `front_matter/003_nota_autore_edizione.md`.

La build genera inoltre l'**Indice dei capitoli** direttamente dai primi H1 delle introduzioni, evitando un indice manuale che possa divergere dal manoscritto.

Restano volutamente non definiti fino alla pubblicazione:

- copyright definitivo;
- licenza definitiva.

Non vengono inventate condizioni di utilizzo nel front matter.

## 6. Reference layer — completato

Sorgenti curate:

- `reference/001_glossario.md` — glossario dei concetti operativi ricorrenti;
- `reference/002_artefatti_operativi.md` — indice dei deliverable canonici con capitolo e rischio protetto.

Sezioni generate:

- **Indice dei casi reali documentati** — derivato dagli heading effettivi del manoscritto;
- **Indice delle fonti** — derivato dai 190 URL distinti del corpo e ordinato per dominio;
- **Note e fonti** per capitolo — derivate dalle footnote Markdown sorgente.

L'indice dei casi è stato verificato per evitare che prefissi strutturali o trattini interni (`trade-off`) vengano alterati durante la generazione.

## 7. Convenzione casi e claim

### Caso reale documentato

Richiede organizzazione/evento identificabile, fonte pubblica attendibile e claim proporzionato.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Claim level

Il proofread preserva la distinzione:

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

## 10. Confini concettuali protetti nel proofread

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

## 11. Proofread + consistency pass — completato

Il pass globale di release ha incluso:

- grafie italiane ad alta probabilità di errore;
- branding e nomi tecnici ricorrenti;
- termini canonici dei deliverable;
- rimandi numerici e riferimenti ai capitoli;
- casing dei nomi propri degli artefatti;
- distinzione tra termini canonici e locuzioni generiche;
- protezione dei template fenced-code da falsi positivi del linter.

Il controllo dei termini canonici è ora parte della CI. Il linter ignora i fenced code block e non forza capitalizzazione quando una locuzione è semanticamente generica.

## 12. Layout QA PDF/DOCX — completato

Il QA è stato effettuato sugli artifact prodotti dalla CI, non su build locali divergenti.

### PDF

Sono stati verificati front matter, indice, inizi capitolo, tabelle, code block, note/fonti, reference layer e chiusura. Correzioni applicate:

- risoluzione delle footnote Markdown;
- aggiunta di bookmark PDF;
- riduzione dell'outline a capitoli + sezioni numerate;
- pulizia dell'indice dei casi reali;
- rimozione del numero pagina stampato dal frontespizio.

Stato corrente:

- **1.209 pagine**;
- **389 bookmark**;
- nessuna sintassi footnote `[^...]` residua;
- nessun markup Markdown grezzo rilevato nei controlli sull'output.

### DOCX

Il documento è stato anche convertito con LibreOffice per verificare una seconda catena di rendering. Il QA ha individuato e corretto:

- footer visibile sul frontespizio;
- mancata ripetizione della riga header nelle tabelle multipagina.

Stato corrente:

- **213/213 tabelle** con repeating header;
- frontespizio con first-page footer vuoto;
- nessuna footnote Markdown irrisolta;
- conversione LibreOffice completa e senza anomalie di pagine vuote nel controllo automatico;
- campionamento visuale delle zone ad alto rischio completato, inclusa la continuazione del Tooling Decision Record.

## 13. Tesi e chiusura da preservare

Definizione finale:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo principale:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## 14. Release editorial pass — stato finale

### A. Chapter review — **COMPLETATO**

### B. Source/factual audit — **COMPLETATO**

### C. Formula cleanup — **COMPLETATO**

### D. Front matter + navigazione — **COMPLETATO**

### E. Reference layer — **COMPLETATO**

### F. Proofread + consistency pass — **COMPLETATO**

### G. Layout QA PDF/DOCX — **COMPLETATO**

### H. Freshness recheck — **COMPLETATO**

### I. Release candidate — **FASE CORRENTE**

Non aggiungere altro corpo al libro salvo una lacuna dimostrata. Da questo punto le modifiche dovrebbero essere limitate a problemi di release, metadata o difetti verificabili.

## 15. Release gate

Il gate automatico corrente è:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
# + inspect outputs in Book CI
```

La run corrente verifica inoltre PDF outline, footnote risolte, repeating header DOCX e frontespizio DOCX.

Il release gate editoriale è **PASS** sull'head `ccff96add69f53af5393e03918068a164288fb83`.

Restano decisioni di pubblicazione, non debito editoriale del manoscritto:

- eventuale numero/versione di release;
- copyright definitivo;
- licenza definitiva;
- eventuale tag/release GitHub e distribuzione degli artifact.

## 16. Ordine aggiornato

```text
1. definire/registrare la release candidate
2. decidere metadata di pubblicazione ancora volontariamente aperti
3. creare tag/release quando desiderato
```

Il manoscritto ha superato il release editorial pass. Da qui l'obiettivo è congelare una build verificata e trasformarla in una release pubblicabile senza riaprire il lavoro editoriale già chiuso.
