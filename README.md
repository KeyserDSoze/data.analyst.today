# data.analyst.today

Un libro open source sull'analisi dati nell'era dell'AI.

L'obiettivo non è insegnare una collezione di tool. Il progetto parte dal ragionamento analitico: capire il problema, definire le metriche, verificare i dati, scegliere il metodo, usare lo strumento giusto e trasformare l'analisi in decisioni. SQL, Excel, Python, BI, cloud e AI sono strumenti dentro questo processo.

Il corpo principale del manoscritto comprende oggi i **Capitoli 0–19** ed è entrato nella fase di revisione editoriale, tecnica e di impaginazione.

## Struttura del repository

```text
data.analyst.today/
├── README.md
├── EDITORIAL_AUDIT.md
├── requirements.txt
├── book.yml
├── chapters/
│   ├── 000_chapter/        # Al timone
│   ├── 001_chapter/
│   ├── 002_chapter/
│   ├── ...
│   └── 019_chapter/
├── scripts/
│   ├── build.py
│   ├── lint_book.py
│   └── normalize_sources.py
└── build/
    ├── data-analyst-today.md
    ├── data-analyst-today.docx
    └── data-analyst-today.pdf
```

Ogni capitolo ha una cartella numerata. Dentro la cartella, ogni sezione importante è un file Markdown separato. L'ordine è determinato dai prefissi numerici delle cartelle e dei file.

Questo permette di lavorare su una sezione alla volta senza trasformare il manoscritto in un unico file enorme.

## Indice attuale

0. **Al timone** — lavorare con l'AI senza delegare la responsabilità.
1. **Tutto è cambiato. Il problema è rimasto lo stesso** — mentalità analitica nell'era AI.
2. **Dal problema di business al problema analitico** — analytical brief, metriche, ipotesi e priorità.
3. **Capire i dati prima di analizzarli** — grain, chiavi, qualità, lineage e contratti.
4. **Statistica descrittiva ed EDA** — distribuzioni, dispersione, correlazioni, trend e anomalie.
5. **Probabilità e incertezza** — campionamento, intervalli, test e A/B testing fundamentals.
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

## Convenzioni editoriali

- Cartelle dei capitoli: `000_chapter`, `001_chapter`, `002_chapter`, ...
- File delle sezioni: `001_nome.md`, `002_nome.md`, `003_nome.md`, ...
- I prefissi dei file devono essere univoci e contigui all'interno di ogni capitolo.
- Il primo heading del capitolo usa `#`.
- Le sezioni interne usano `##`, `###`, ecc.
- Il file introduttivo può contenere una sezione `X.0` e, quando editorialmente utile, anche la prima sezione numerata `X.1`; il lint ricava quindi la sequenza effettiva dal contenuto del capitolo invece di assumere rigidamente che `002_*.md` sia sempre `X.1`.
- Citazioni e fonti vengono inserite direttamente nel Markdown.
- Il testo sorgente rimane sempre in Markdown; DOCX e PDF sono artefatti generati.
- Non modificare manualmente i file dentro `build/`: vengono ricreati dallo script.

### Casi reali e casi simulati

Il libro distingue esplicitamente:

- **caso reale documentato**: organizzazione, evento o pratica sostenuti da una fonte pubblica attendibile;
- **caso simulato/composito**: scenario costruito a fini didattici, con nomi, numeri o circostanze che possono essere inventati.

I casi con aziende fittizie devono essere interpretati come simulati/compositi. La distinzione serve a non confondere evidenza documentata e ricostruzione pedagogica.

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

Poi installa le dipendenze:

```bash
pip install -r requirements.txt
```

## Controllare il manoscritto

Prima della build:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
```

`normalize_sources.py --check` impedisce di reintrodurre heading numerati interni come H1 e alcune vecchie grafie ASCII (`e'`, `piu'`, `puo'`, ecc.) nel testo italiano.

Il lint controlla, tra le altre cose:

- continuità delle cartelle dei capitoli;
- prefissi duplicati o mancanti;
- corrispondenza tra ordine dei file e numero delle sezioni;
- heading interni scritti accidentalmente come H1;
- file vuoti;
- placeholder editoriali `TODO`, `FIXME` o `TBD`;
- link contenenti `utm_source=chatgpt.com`;
- presenza di notazione matematica ancora da tipografare;
- conteggio indicativo di parole e pagine.

Per trasformare anche i warning editoriali in errori:

```bash
python scripts/lint_book.py --strict
```

## Costruire il libro

Dalla root del repository:

```bash
python scripts/build.py
```

Lo script:

1. trova tutte le cartelle `chapters/*_chapter`;
2. le ordina numericamente con un tie-break deterministico;
3. ordina le sezioni;
4. crea un unico Markdown completo;
5. interpreta heading, liste, citazioni, codice e tabelle Markdown;
6. genera il file Word `.docx`;
7. genera il file PDF `.pdf`.

Gli output vengono scritti in `build/`:

```text
build/data-analyst-today.md
build/data-analyst-today.docx
build/data-analyst-today.pdf
```

Il Markdown aggregato è utile anche per controllare esattamente quale testo è entrato nella build.

## Dimensione misurata del manoscritto

L'audit automatico del 31 agosto 2026 ha misurato:

- **20 capitoli** (`0–19`);
- **321 file Markdown**;
- circa **166.160 parole**;
- **119 URL esterni distinti**;
- una build PDF tecnica corrente di **745 pagine**.

Le 745 pagine non sono ancora il page count editoriale definitivo: font, formule, tabelle, indice e impaginazione finale potranno modificarlo. Dimostrano però che il progetto ha già superato ampiamente l'obiettivo iniziale di un libro da 400+ pagine.

## Filosofia del progetto

Il libro distingue continuamente tre livelli:

1. **Execution** — produrre query, formule, grafici, trasformazioni e report.
2. **Analysis** — formulare ipotesi, scegliere metriche e confronti, interpretare risultati e incertezza.
3. **Decision intelligence** — capire quale problema vale la pena risolvere e trasformare l'evidenza in una decisione.

L'AI rende il primo livello sempre più economico. Per questo il libro dedica particolare attenzione ai livelli due e tre, senza rinunciare alla conoscenza tecnica necessaria per dirigere e verificare strumenti, automazioni e agenti AI.

## Stato editoriale

Il manoscritto principale è completo nei Capitoli 0–19. La pipeline CI verifica ora normalizzazione delle sorgenti, struttura, lint, build Markdown/DOCX/PDF e page count del PDF.

La fase corrente riguarda soprattutto:

- revisione di coerenza e riduzione delle ripetizioni;
- verifica puntuale delle fonti e della distinzione tra casi documentati e simulati;
- tipografia delle formule matematiche;
- revisione visiva di DOCX/PDF, tabelle e blocchi di codice;
- front matter, indice e apparati editoriali;
- preparazione della prima release stabile.

## Licenza

La licenza del progetto verrà definita prima della pubblicazione della prima release stabile.
