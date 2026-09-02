# Editorial audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto. Markdown resta la source of truth.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review editoriale capitolo-per-capitolo: **COMPLETATA**.
- Source/factual audit globale: **COMPLETATO**; dettaglio in `SOURCE_FACTUAL_AUDIT.md`.
- Normalizzazione delle formule/LaTeX residue: **COMPLETATA**.
- Casi pubblici e casi simulati/compositi distinti esplicitamente.
- CI attiva su `main` con normalizzazione, lint e build Markdown/DOCX/PDF.
- Fase corrente: **release editorial pass — front matter, navigazione e reference layer**.

### Ultima build validata

Run Book CI sull'head `bec7f6b3ef9b4f92cdbe8e8597759f87191d2b00`: **SUCCESS**.

- **20 capitoli**;
- **321 file Markdown**;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con notazione matematica/LaTeX rilevata dal linter**;
- **0 file con accenti ASCII legacy**;
- **1.178 pagine PDF**;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità resta densità di valore, affidabilità editoriale e leggibilità della release.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
python scripts/build.py
```

Il lint verifica continuità dei capitoli, prefissi, heading, file vuoti, TODO/FIXME/TBD, URL contaminati, grafie ASCII legacy, formule/LaTeX e conteggi strutturali.

### Warning editoriali globali

Alla build validata del 2 settembre 2026 il precedente warning sui **7 file LaTeX** è stato eliminato mediante normalizzazione editoriale in notazione leggibile dal builder corrente.

File normalizzati:

- `chapters/004_chapter/016_boxplot_iqr.md`;
- `chapters/005_chapter/003_conditional_probability.md`;
- `chapters/005_chapter/004_independence.md`;
- `chapters/005_chapter/006_expected_value_variance.md`;
- `chapters/005_chapter/008_bayesian_update.md`;
- `chapters/005_chapter/011_standard_error.md`;
- `chapters/005_chapter/013_confidence_intervals.md`.

La scelta è stata volutamente conservativa: formule semplici in notazione Unicode/inline code, senza introdurre una nuova dipendenza di rendering matematico.

## 3. Source/factual audit — completato

L'audit globale dei riferimenti è stato eseguito per:

- raggiungibilità e destinazione;
- autorità della fonte;
- supporto reale del claim;
- livello del claim: associazione, previsione, esposizione, causalità, outcome;
- distinzione tra casi reali documentati e casi simulati/compositi;
- freshness per fonti time-sensitive;
- canonicalizzazione degli URL.

Il pass ha incluso sia blocchi tematici sia uno sweep bottom-up delle sezioni `Fonte:` / `Fonti:` e controlli di source hygiene.

Correzioni principali emerse durante l'audit:

- aggiornamento di path Microsoft Research legacy verso URL canonici;
- sostituzione del vecchio static link Duolingo con la copia primaria SEC dello shareholder letter;
- canonicalizzazione del riferimento Vertex AI già individuato nel pass precedente;
- canonicalizzazione del link scikit-learn per classification threshold da path versionato a `/stable/`;
- verifica dei casi reali documentati e calibrazione dei claim causali senza necessità di nuove riscritture sostantive nell'ultimo sweep.

Non risultano link con `utm_source=chatgpt.com` nel manoscritto né URL `http://` residui.

### Recheck al release gate

Non serve ripetere l'intero audit. Prima della release candidata vanno ricontrollate soltanto le fonti con freshness o stato editoriale variabile, in particolare:

- Government Analysis Function, *Communicating quality, uncertainty and change*, attualmente pubblicata ma indicata come pagina sotto revisione;
- fonti 2025–2026 usate per trend sul lavoro/AI quando il claim dipende dalla loro attualità.

## 4. Convenzione casi e fonti

### Caso reale documentato

Richiede organizzazione/evento identificabile, fonte pubblica attendibile, claim proporzionato e nessuna promozione indebita di associazione a causalità.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Fonti

La review privilegia standard/governi, documentazione ufficiale, letteratura accademica riconosciuta e fonti primarie per i casi pubblici.

## 5. Stato capitolo per capitolo

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

## 6. Vocabolario operativo del libro

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

Questi artefatti non sono una checklist obbligatoria. Sono un vocabolario operativo per rischi differenti.

## 7. Confini concettuali principali

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

```text
AI Analysis Control Sheet
→ Decision Record
→ Decision Communication Pack
```

- **14:** quale claim ha diritto di uscire dal workflow;
- **15:** quale alternativa scegliere e perché;
- **16:** come comprimere il Decision Record senza rafforzare il claim o nascondere l'incertezza.

### 17 / 18 / 19 — decisione, sistema, professionista

- **17:** evidence routing per una decisione complessa;
- **18:** trasformare una capacità ricorrente in servizio affidabile;
- **19:** costruire un portafoglio professionale robusto all'incertezza tecnologica.

## 8. Note finali Capitoli 17–19

### Capitolo 17 — Capstone Routing Canvas

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

Punti chiave: method gate, deliverable necessari vs volutamente saltati, Evidence Ledger `observed / inferred / still unknown`, stop state `DECIDE / PILOT / WAIT FOR X / BUY INFORMATION / NO ACTION / NOT IDENTIFIED`, outcome review distinta dalla decision quality ex ante.

### Capitolo 18 — Analytics Operating Contract

Punti chiave: tier `T0–T3`, ownership separate, SLI/SLO ed error budget legati al consumer, stati `READY / READY WITH CAVEATS / STALE BUT SERVABLE / PARTIAL / BLOCKED`, semantic diff, testing pyramid basata sui failure mode, adoption ladder, Agent Operating Profile e retirement come parte del lifecycle.

Il caso Helios Mobility è simulato/composito.

### Capitolo 19 — Personal Career Operating Plan

Concetti principali: task exposure distinto da scomparsa della professione, responsibility moat, execution/verification/design skill, delegation boundary `A–E`, semantic leverage, Capability Portfolio, career optionality, decision span, escalation literacy, seniority spans, verification reserve e scenario planning 2035.

Definizione finale mantenuta:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo principale:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## 9. Arco complessivo

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

## 10. Release editorial pass — stato

### A. Fonti e factual audit — **COMPLETATO**

Ledger: `SOURCE_FACTUAL_AUDIT.md`.

### B. Formula rendering / normalizzazione — **COMPLETATO**

Linter: `0` file con notazione matematica/LaTeX.

### C. Front matter e navigazione — **PROSSIMO BLOCCO**

- frontespizio;
- autore e bio;
- copyright/licenza;
- versione/edizione;
- “come usare questo libro”;
- legenda casi reali/compositi;
- indice automatico;
- eventuale prefazione/introduzione editoriale.

### D. Reference layer — **DA FARE**

- glossario;
- bibliografia/indice fonti;
- eventuale indice dei casi reali;
- cross-reference tra deliverable canonici;
- elenco dei template operativi riutilizzabili.

### E. Proofread e consistency pass — **DA FARE**

- ortografia/punteggiatura;
- inglesismi e capitalizzazione;
- termini canonici;
- rimandi tra capitoli;
- ripetizioni residue;
- numeri e unità;
- caso reale vs composito;
- claim level e causal wording.

### F. Layout QA — **DA FARE**

- tabelle larghe;
- code block;
- formule/notazione;
- blockquote;
- heading/page break;
- widows/orphans dove possibile;
- footnote/link;
- indice;
- numerazione pagine;
- resa PDF e DOCX.

## 11. Release gate

Prima di una release candidata:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di:

- fonti freshness-sensitive;
- notazione e tabelle;
- codice;
- casi reali/compositi;
- ortografia;
- footnote/link;
- page break;
- indice;
- continuità dei deliverable canonici.

## 12. Prossimo blocco

La fase di chapter review, il source/factual audit e la normalizzazione delle formule sono conclusi.

Ordine aggiornato:

```text
1. front matter + navigazione
2. reference layer
3. proofread globale
4. layout QA PDF/DOCX
5. release candidate
```

Da questo punto l'obiettivo non è aggiungere altro corpo al libro, salvo lacune dimostrate. È trasformare il manoscritto revisionato in una **release editoriale verificata e pubblicabile**.
