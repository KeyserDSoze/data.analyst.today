# data.analyst.today

Un libro open source, costruito capitolo per capitolo, sull'analisi dati nell'era dell'AI.

L'obiettivo non è insegnare una collezione di tool. Il progetto parte dal ragionamento analitico: capire il problema, definire le metriche, verificare i dati, scegliere il metodo, usare lo strumento giusto e trasformare l'analisi in decisioni. SQL, Excel, Python, Power BI, cloud e AI sono strumenti dentro questo processo.

## Struttura del repository

```text
data.analyst.today/
├── README.md
├── requirements.txt
├── book.yml
├── chapters/
│   ├── 001_chapter/
│   │   ├── 001_introduction.md
│   │   ├── 002_what_changed.md
│   │   └── 003_what_did_not_change.md
│   ├── 002_chapter/
│   │   └── ...
│   └── ...
├── scripts/
│   └── build.py
└── build/
    ├── data-analyst-today.md
    ├── data-analyst-today.docx
    └── data-analyst-today.pdf
```

Ogni capitolo ha una cartella numerata. Dentro la cartella, ogni sezione o paragrafo importante è un file Markdown separato. L'ordine è determinato dai prefissi numerici dei nomi di cartella e file.

Questo ci permette di lavorare su un paragrafo alla volta senza dover modificare un unico file enorme da centinaia di pagine.

## Convenzioni editoriali

- Cartelle dei capitoli: `001_chapter`, `002_chapter`, `003_chapter`, ...
- File delle sezioni: `001_nome.md`, `002_nome.md`, `003_nome.md`, ...
- Il primo heading del capitolo usa `#`.
- Le sezioni interne usano `##`, `###`, ecc.
- Citazioni e fonti vengono inserite direttamente nel Markdown.
- Il testo sorgente rimane sempre in Markdown; DOCX e PDF sono artefatti generati.
- Non modificare manualmente i file dentro `build/`: vengono ricreati dallo script.

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

## Costruire il libro

Dalla root del repository:

```bash
python scripts/build.py
```

Lo script:

1. trova tutte le cartelle `chapters/*_chapter`;
2. le ordina numericamente;
3. ordina i file `.md` dentro ogni capitolo;
4. crea un unico Markdown completo;
5. genera il file Word `.docx`;
6. genera il file PDF `.pdf`.

Gli output vengono scritti in `build/`.

## Output

Dopo il build troverai:

```text
build/data-analyst-today.md
build/data-analyst-today.docx
build/data-analyst-today.pdf
```

Il Markdown aggregato è utile anche per controllare esattamente quale testo è entrato nella build.

## Aggiungere un nuovo capitolo

Esempio:

```text
chapters/002_chapter/
├── 001_introduction.md
├── 002_business_question.md
├── 003_metrics.md
└── 004_case_study.md
```

Poi basta rilanciare:

```bash
python scripts/build.py
```

Non è necessario modificare lo script.

## Filosofia del progetto

Il libro distingue continuamente tre livelli:

1. **Execution** — produrre query, formule, grafici, trasformazioni e report.
2. **Analysis** — formulare ipotesi, scegliere metriche e confronti, interpretare risultati e incertezza.
3. **Decision intelligence** — capire quale problema vale la pena risolvere e trasformare l'evidenza in una decisione.

L'AI rende il primo livello sempre più economico. Per questo il libro dedica particolare attenzione ai livelli due e tre, senza rinunciare alla conoscenza tecnica necessaria per dirigere e verificare strumenti, automazioni e agenti AI.

## Roadmap editoriale

Il progetto è pensato per crescere fino a un libro di almeno 400 pagine, con capitoli dedicati a:

- mentalità analitica e problem framing;
- metriche e KPI;
- data quality;
- SQL ed esplorazione dei dati;
- statistica e probabilità applicate;
- EDA;
- analisi di funnel, coorti, retention e churn;
- sperimentazione e A/B testing;
- causalità;
- forecasting e serie temporali;
- data visualization e storytelling;
- Excel, Python e BI come strumenti di analisi;
- modellazione dati e semantic layer;
- data warehouse, lake e lakehouse;
- cloud analytics e modern data stack;
- automazione e pipeline;
- AI-assisted analytics;
- verifica e auditing degli output AI;
- architettura analytics;
- case study end-to-end.

## Licenza

La licenza del progetto verrà definita prima della pubblicazione della prima release stabile.
