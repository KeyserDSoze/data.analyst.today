# Release Candidate — RC1

Data: **2 settembre 2026**

Stato: **release candidate editoriale**

Questo file definisce la prima release candidate del progetto `data.analyst.today` senza introdurre una versione SemVer, una licenza o un copyright non ancora scelti.

## Cosa significa RC1

RC1 è il punto in cui il manoscritto smette di essere in editing continuo e diventa una build candidata alla pubblicazione.

Da questo momento una modifica al corpo è giustificata solo da:

- errore fattuale dimostrato;
- fonte diventata inaffidabile o irraggiungibile;
- errore grammaticale o tipografico reale;
- difetto di rendering;
- problema di navigazione/accessibilità;
- regressione rilevata dalla CI.

Non sono motivi sufficienti:

- preferenza stilistica marginale;
- desiderio di aggiungere un altro esempio senza una lacuna dimostrata;
- aggiornamento cosmetico di tool o terminologia già corretti;
- espansione del corpo perché “si potrebbe dire di più”.

## Gate editoriali

| Gate | Stato |
|---|---|
| Capitoli 0–19 completi | **PASS** |
| Review capitolo-per-capitolo | **PASS** |
| Source/factual audit globale | **PASS** |
| Freshness recheck release-gate | **PASS** |
| Formula/LaTeX cleanup | **PASS** |
| Front matter + navigazione | **PASS** |
| Reference layer | **PASS** |
| Proofread + consistency pass | **PASS** |
| Layout QA PDF | **PASS** |
| Layout QA DOCX | **PASS** |
| CI strict + build-output guardrails | **PASS** sulla baseline validata |

## Baseline tecnica validata

La baseline di build verificata prima della dichiarazione RC1 è l'head:

`ccff96add69f53af5393e03918068a164288fb83`

La Book CI su quella baseline è **SUCCESS** e riporta:

- **20 capitoli**;
- **321 file Markdown** nel corpo;
- **251.126 parole stimate**;
- **1.860.230 caratteri**;
- **190 URL esterni distinti**;
- **0 file con LaTeX residuo**;
- **0 file con grafie ASCII legacy**;
- **1.209 pagine PDF**;
- **389 bookmark PDF**;
- **213/213 tabelle DOCX** con repeating header;
- nessuna footnote Markdown `[^...]` irrisolta negli output;
- frontespizio PDF senza numero pagina stampato;
- frontespizio DOCX senza footer visibile.

I commit successivi alla baseline che aggiornano esclusivamente audit, README e questo manifest non modificano il corpo del libro o il renderer. Devono comunque mantenere CI verde prima di essere considerati parte della candidate.

## Controllo automatico

Il gate della candidate è:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

La Book CI verifica inoltre gli output generati:

- footnote risolte;
- outline PDF presente;
- repeating header delle tabelle DOCX;
- first-page footer DOCX vuoto;
- generazione riuscita di Markdown, DOCX e PDF.

## Source/factual freeze

L'audit dei **190 URL distinti** è chiuso. Il freshness recheck del 2 settembre 2026 ha ricontrollato le fonti più time-sensitive e quelle esplicitamente sotto revisione.

Esito: **nessuna correzione al manoscritto richiesta**.

Non va ripetuto un audit globale prima della release stabile salvo cambiamenti sostantivi al testo o regressioni delle fonti.

## Layout freeze

Il PDF e il DOCX sono stati controllati sugli artifact prodotti dalla CI.

Sono stati corretti e verificati:

- footnote/endnote;
- indice dei casi reali;
- bookmark PDF;
- frontespizio PDF;
- frontespizio DOCX;
- tabelle DOCX multipagina;
- reference layer e ultime pagine;
- campioni di code block, tabelle e sezioni ad alta densità.

## Tesi da non alterare nella candidate

Definizione finale:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## Metadata ancora aperti

Questi elementi sono decisioni di pubblicazione e non bloccano la qualità editoriale di RC1:

- versione pubblica/numero di release definitivo;
- copyright definitivo;
- licenza definitiva;
- eventuale tag Git;
- eventuale GitHub Release e canali di distribuzione.

`book.yml` resta intenzionalmente privo di un numero di versione finché non viene scelta una convenzione di release.

## Criterio di promozione

RC1 può essere promossa a release stabile quando:

1. il commit candidato ha Book CI verde;
2. non sono emerse regressioni dopo il freeze;
3. i metadata di pubblicazione necessari sono stati scelti;
4. gli artifact da distribuire provengono dalla stessa pipeline validata.

Se emerge un difetto sostantivo, si corregge il problema e si crea una nuova candidate. Non si riapre automaticamente l'intero ciclo editoriale.
