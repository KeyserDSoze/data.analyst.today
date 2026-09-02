# data.analyst.today

Un libro open source sull'analisi dati nell'era dell'AI, scritto da **Alessandro Rapiti**. Il repository è pubblicato attraverso l'account GitHub **KeyserDSoze**.

L'obiettivo non è insegnare una collezione di tool. Il progetto parte dal ragionamento analitico: capire il problema, definire metriche e popolazione, verificare i dati, scegliere il metodo, calibrare il claim e trasformare l'evidenza in una decisione. SQL, Excel, Python, BI, cloud e AI sono strumenti dentro questo processo.

Il corpo principale comprende i **Capitoli 0–19**. Review capitolo-per-capitolo, source/factual audit, formula cleanup, front matter, reference layer, proofread/consistency pass, layout QA PDF/DOCX e freshness recheck sono completati. La fase corrente è **release candidate**.

## Struttura del repository

```text
data.analyst.today/
├── README.md
├── EDITORIAL_AUDIT.md
├── SOURCE_FACTUAL_AUDIT.md
├── RELEASE_CANDIDATE.md
├── release.json                 # manifest che attiva la pubblicazione di una release
├── release-notes/
├── book.yml
├── requirements.txt
├── front_matter/
│   ├── 001_come_usare_questo_libro.md
│   ├── 002_legenda_editoriale.md
│   └── 003_nota_autore_edizione.md
├── chapters/
│   ├── 000_chapter/        # Al timone
│   ├── 001_chapter/
│   ├── 002_chapter/
│   ├── ...
│   └── 019_chapter/
├── reference/
│   ├── 001_glossario.md
│   └── 002_artefatti_operativi.md
├── scripts/
│   ├── build.py
│   ├── build_release.py
│   ├── build_epub.py
│   ├── lint_book.py
│   └── normalize_sources.py
└── build/
    ├── data-analyst-today.md
    ├── data-analyst-today.docx
    ├── data-analyst-today.pdf
    └── data-analyst-today.epub
```

Markdown è la source of truth. DOCX, PDF ed EPUB sono artefatti generati e non vanno modificati manualmente.

## Indice del corpo principale

0. **Al timone** — lavorare con l'AI senza delegare la responsabilità.
1. **Tutto è cambiato. Il problema è rimasto lo stesso** — mentalità analitica nell'era AI.
2. **Dal problema di business al problema analitico** — Analytical Brief, metriche, ipotesi e priorità.
3. **Capire i dati prima di analizzarli** — Data Readiness Review, grain, qualità e comparabilità.
4. **Statistica descrittiva ed EDA** — distribuzioni, dispersione, correlazioni, trend e anomalie.
5. **Probabilità e incertezza** — campionamento, intervalli, test e decisione sotto incertezza.
6. **Segmentazione, coorti, funnel, retention e churn**.
7. **Serie temporali, anomalie e forecasting**.
8. **Causalità, confondenti e ragionamento controfattuale**.
9. **Experimentation e A/B testing nel mondo reale**.
10. **Regressione e modelli predittivi per Data Analyst**.
11. **SQL, trasformazione del dato e data modeling per l'analisi**.
12. **Data architecture per Data Analyst**.
13. **Scegliere lo strumento giusto senza diventarne dipendenti**.
14. **AI-assisted analytics: accelerare senza perdere rigore**.
15. **Dall'analisi all'insight e alla decisione**.
16. **Data storytelling, dashboard ed executive communication**.
17. **Casi end-to-end di Data Analysis**.
18. **Costruire un sistema analitico che scala**.
19. **Il Data Analyst nel 2026–2035**.

La build genera automaticamente un **Indice dei capitoli**, un **Indice dei casi reali documentati**, le sezioni **Note e fonti** e un **Indice delle fonti** consolidato dai riferimenti presenti nel corpo.

## Convenzioni editoriali

- Cartelle capitoli: `000_chapter`, `001_chapter`, ... `019_chapter`.
- File sezione: `001_nome.md`, `002_nome.md`, ...
- I prefissi devono essere univoci e contigui nel capitolo.
- Il primo heading del capitolo usa `#`; le sezioni interne usano `##`, `###`, ecc.
- Citazioni e fonti rimangono vicino al claim che sostengono.
- Non vengono accettati URL con `utm_source=chatgpt.com`.
- Le fonti privilegiano documentazione ufficiale, standard, governi, fonti primarie e letteratura accademica riconosciuta quando disponibili.

### Casi reali e casi simulati

Il libro distingue esplicitamente:

- **caso reale documentato** — organizzazione, evento o pratica sostenuti da una fonte pubblica attendibile e con claim proporzionato;
- **caso simulato/composito** — scenario costruito a fini didattici, con nomi, numeri o circostanze che possono essere inventati.

La distinzione impedisce di confondere evidenza documentata e ricostruzione pedagogica.

## Il vocabolario operativo

Il libro costruisce una serie di artefatti riutilizzabili:

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

Il Capitolo 17 aggiunge il **Capstone Routing Canvas**, il Capitolo 18 l'**Analytics Operating Contract** e il Capitolo 19 il **Personal Career Operating Plan**.

Non sono una checklist obbligatoria: sono un vocabolario di rischi e controlli da attivare quando servono.

## Installazione

Serve Python 3.11+.

```bash
python -m venv .venv
```

Su Linux/macOS:

```bash
source .venv/bin/activate
```

Su Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Poi:

```bash
pip install -r requirements.txt
```

## Controllare il manoscritto

Il release gate locale è:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build_release.py
python scripts/build_epub.py
```

Il lint controlla, tra le altre cose:

- continuità e numerazione dei capitoli;
- prefissi duplicati o mancanti;
- corrispondenza tra file e sezioni;
- heading interni H1 accidentali;
- file vuoti;
- placeholder `TODO`, `FIXME`, `TBD`;
- URL contaminati;
- grafie ASCII legacy;
- notazione LaTeX residua;
- casing dei deliverable canonici;
- conteggio di parole, caratteri e URL distinti.

In CI, dopo la build vengono verificati anche gli output: footnote risolte, outline PDF presente, repeating header delle tabelle DOCX, frontespizio DOCX senza footer visibile, autore **Alessandro Rapiti** nei metadata PDF/DOCX/EPUB e struttura EPUB valida.

## Costruire il libro

Dalla root, per ottenere la stessa resa della release:

```bash
python scripts/build_release.py
python scripts/build_epub.py
```

`scripts/build.py` contiene il renderer di base. `scripts/build_release.py` applica il layer tipografico della release e poi richiama il renderer:

1. assembla il frontespizio da `book.yml`;
2. inserisce i file di `front_matter/`;
3. genera l'indice dei capitoli dai titoli H1 correnti;
4. assembla i 321 file del corpo in ordine numerico;
5. risolve le footnote Markdown in riferimenti numerici e sezioni **Note e fonti** per capitolo;
6. inserisce glossario e indice degli artefatti da `reference/`;
7. genera l'indice dei casi reali documentati;
8. genera l'indice consolidato delle fonti a partire dagli URL del corpo;
9. produce Markdown, DOCX e PDF;
10. rende ogni nuovo capitolo una nuova pagina in PDF/DOCX, aumenta la gerarchia dei titoli e rifinisce il frontespizio.

`scripts/build_epub.py` usa il Markdown assemblato e produce un EPUB con documenti separati per gli H1 top-level, indice di navigazione e stile tipografico coerente con PDF/DOCX.

Output:

```text
build/data-analyst-today.md
build/data-analyst-today.docx
build/data-analyst-today.pdf
build/data-analyst-today.epub
```

## Pubblicare una release

La pipeline usa `release.json` come manifest esplicito di pubblicazione. Una normale push su `main` valida e costruisce i formati ma **non pubblica** una GitHub Release. La pubblicazione parte soltanto quando `release.json` viene creato o modificato nello stesso commit che si vuole rilasciare.

Esempio:

```json
{
  "tag": "v1.0.0-rc2",
  "name": "Data Analyst Today v1.0.0-rc2",
  "prerelease": true,
  "notes_file": "release-notes/v1.0.0-rc2.md"
}
```

Dopo che il job `validate-and-build` è verde, il job `publish-release`:

1. legge e valida il manifest;
2. scarica l'artifact costruito dalla stessa run;
3. crea il tag/release se non esiste;
4. allega alla GitHub Release i tre formati distributivi:
   - `data-analyst-today.docx`;
   - `data-analyst-today.pdf`;
   - `data-analyst-today.epub`.

Il Markdown assemblato rimane nell'artifact della CI, ma non viene allegato alla release pubblica.

## Stato misurato — 2 settembre 2026

Il lint del corpo principale riporta:

- **20 capitoli** (`0–19`);
- **321 file Markdown** nel corpo;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con LaTeX residuo**;
- **0 file con grafie ASCII legacy**.

La build tipografica della release contiene inoltre:

- **3 file front matter**;
- **2 file reference curati**;
- indice capitoli generato;
- indice casi reali generato;
- indice fonti generato;
- footnote risolte in **Note e fonti**;
- **389 bookmark PDF**;
- **213/213 tabelle DOCX** con repeating header;
- autore **Alessandro Rapiti** nel frontespizio e nei metadata distributivi;
- frontespizio PDF e DOCX centrato e privo di footer/numero pagina visibile;
- ogni capitolo inizia su una nuova pagina/sezione nei formati distributivi;
- titoli capitolo con gerarchia tipografica rafforzata;
- circa **1.235 pagine PDF** nella build tecnica corrente;
- build Markdown, DOCX, PDF ed EPUB validate in CI.

Il page count è una misura tecnica della build, non un obiettivo editoriale.

## Filosofia del progetto

Il libro distingue continuamente tre livelli:

1. **Execution** — produrre query, formule, grafici, trasformazioni e report.
2. **Analysis** — formulare ipotesi, scegliere metriche e confronti, interpretare risultati e incertezza.
3. **Decision intelligence** — capire quale problema vale la pena risolvere e trasformare l'evidenza in una decisione.

L'AI rende molte attività di execution più economiche. Questo aumenta, non riduce, l'importanza di semantica, verifica, judgment, risk management e accountability.

La definizione finale del libro è:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

## Stato editoriale

Completati:

- corpo Capitoli 0–19;
- review editoriale capitolo-per-capitolo;
- source/factual audit globale;
- canonicalizzazione delle fonti individuate;
- release-gate freshness recheck;
- normalizzazione delle formule/LaTeX residue;
- front matter e navigazione;
- glossario e indice degli artefatti;
- indice automatico dei casi reali e delle fonti;
- proofread globale / consistency pass;
- layout QA PDF/DOCX;
- build-output guardrails in CI;
- build multiformato Markdown/DOCX/PDF/EPUB validata in CI.

Fase corrente:

```text
release candidate
→ pubblicazione prerelease tramite release.json
→ feedback / eventuali bugfix
→ release stabile
```

Il dettaglio operativo è mantenuto in `EDITORIAL_AUDIT.md`; il ledger delle fonti è in `SOURCE_FACTUAL_AUDIT.md`; il manifest della candidate è in `RELEASE_CANDIDATE.md`.

## Licenza

La licenza del progetto verrà definita prima della pubblicazione della prima release stabile. La release candidate non inventa una licenza non ancora scelta.
