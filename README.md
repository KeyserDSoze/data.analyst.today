# data.analyst.today

Un libro open source sull'analisi dati nell'era dell'AI.

L'obiettivo non è insegnare una collezione di tool. Il progetto parte dal ragionamento analitico: capire il problema, definire metriche e popolazione, verificare i dati, scegliere il metodo, calibrare il claim e trasformare l'evidenza in una decisione. SQL, Excel, Python, BI, cloud e AI sono strumenti dentro questo processo.

Il corpo principale comprende i **Capitoli 0–19**. La review capitolo-per-capitolo, il source/factual audit globale, la normalizzazione delle formule residue, il front matter e il reference layer sono completati. La fase corrente è il **proofread globale e consistency pass**, seguito dal layout QA PDF/DOCX e dalla release candidate.

## Struttura del repository

```text
data.analyst.today/
├── README.md
├── EDITORIAL_AUDIT.md
├── SOURCE_FACTUAL_AUDIT.md
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
│   ├── lint_book.py
│   └── normalize_sources.py
└── build/
    ├── data-analyst-today.md
    ├── data-analyst-today.docx
    └── data-analyst-today.pdf
```

Markdown è la source of truth. DOCX e PDF sono artefatti generati e non vanno modificati manualmente.

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

La build genera inoltre automaticamente un **Indice dei capitoli**, un **Indice dei casi reali documentati** e un **Indice delle fonti** consolidato dai riferimenti presenti nel corpo.

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

Prima della build:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
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
- conteggio di parole, caratteri e URL distinti.

Per trattare anche i warning editoriali come errori:

```bash
python scripts/lint_book.py --strict
```

## Costruire il libro

Dalla root:

```bash
python scripts/build.py
```

Lo script:

1. assembla il frontespizio da `book.yml`;
2. inserisce i file di `front_matter/`;
3. genera l'indice dei capitoli dai titoli H1 correnti;
4. assembla i 321 file del corpo in ordine numerico;
5. inserisce glossario e indice degli artefatti da `reference/`;
6. genera l'indice dei casi reali documentati;
7. genera l'indice consolidato delle fonti a partire dagli URL del corpo;
8. produce Markdown, DOCX e PDF.

Output:

```text
build/data-analyst-today.md
build/data-analyst-today.docx
build/data-analyst-today.pdf
```

## Stato misurato — 2 settembre 2026

Il lint del corpo principale riporta:

- **20 capitoli** (`0–19`);
- **321 file Markdown** nel corpo;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con LaTeX residuo**;
- **0 file con grafie ASCII legacy**.

La build validata con front matter e reference layer contiene inoltre:

- **3 file front matter**;
- **2 file reference curati**;
- indice capitoli generato;
- indice casi reali generato;
- indice fonti generato;
- **1.210 pagine PDF** nella build tecnica corrente;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count è una misura tecnica della build, non un obiettivo editoriale. Potrà cambiare durante il layout QA.

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
- normalizzazione delle formule/LaTeX residue;
- front matter e navigazione;
- glossario e indice degli artefatti;
- indice automatico dei casi reali e delle fonti;
- build multiformato validata in CI.

Prossimi gate:

```text
proofread globale + consistency pass
→ layout QA PDF/DOCX
→ recheck fonti freshness-sensitive
→ release candidate
```

Il dettaglio operativo è mantenuto in `EDITORIAL_AUDIT.md`; il ledger delle fonti è in `SOURCE_FACTUAL_AUDIT.md`.

## Licenza

La licenza del progetto verrà definita prima della pubblicazione della prima release stabile.
