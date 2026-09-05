# Editorial audit — data.analyst.today

Ultimo aggiornamento: **5 settembre 2026**.

Questo documento è la dashboard editoriale del manoscritto. Markdown resta la source of truth; `SOURCE_FACTUAL_AUDIT.md` conserva il ledger delle verifiche esterne.

## 1. Stato corrente

- Corpo principale **Capitoli 0–19**: **COMPLETO**.
- Review prose-first capitolo-per-capitolo: **COMPLETATA su tutti i capitoli**.
- Front matter: **RICONTROLLATO E ALLINEATO** dopo la revisione finale.
- Reference layer: **RICONTROLLATO E ALLINEATO** dopo la revisione finale.
- Source/factual audit globale: **CHIUSO**, con recheck mirato del 5 settembre 2026.
- Caso NXP del Capitolo 17: **RITIRATO** perché il customer-story URL non era più verificabile in modo affidabile; sostituito con documentazione AWS corrente su cost allocation e unit metrics.
- Normalizzazione sorgenti: **PASS**.
- Lint editoriale strict: **PASS**.
- Build Markdown / DOCX / PDF / EPUB: **PASS**.
- Output QA automatico: **PASS**.
- Pubblicazione GitHub Release: **NON ESEGUITA** in questo pass; gli step release-specific sono stati correttamente saltati.

### Baseline di contenuto validata

La build di contenuto e apparati validata dopo il pass editoriale finale è:

- head: `470ad51bd762c912a15addbce40619f03e42c415`;
- Book CI run: `33980921004`;
- esito `validate-and-build`: **SUCCESS**;
- esito `publish-release`: **SUCCESS**, con publishing step `skipped` perché il release manifest non è stato modificato.

Questa dashboard può ricevere commit documentali successivi; i conteggi sotto si riferiscono alla baseline di contenuto indicata.

## 2. Statistiche della build finale verificata

Dal lint e dall'output inspection della stessa CI:

| Indicatore | Valore |
|---|---:|
| Capitoli | 20 |
| File Markdown corpo | 321 |
| File apparati scansionati | 5 |
| Parole stimate corpo | 247.697 |
| Caratteri corpo | 1.772.827 |
| URL esterni distinti nel corpo | 189 |
| File corpo con LaTeX residuo | 0 |
| File corpo con accenti ASCII da normalizzare | 0 |
| Front matter | 3 file |
| Reference layer | 2 file |
| PDF | 723 pagine |
| PDF outline | 344 voci |
| Tabelle DOCX con repeating header | 232 |
| EPUB | 30 documenti XHTML |
| Metadata autore PDF/DOCX/EPUB | Alessandro Rapiti |

La CI ha inoltre confermato:

- nessuna footnote Markdown `[^...]` irrisolta nell'assemblato;
- nessuna footnote Markdown irrisolta nel DOCX;
- outline PDF presente;
- tutte le tabelle DOCX con repeating header;
- frontespizio DOCX con first-page footer separato e vuoto;
- gerarchia del titolo capitolo nel DOCX;
- EPUB con mimetype, package e stylesheet editoriali validi;
- autore corretto nei metadata dei formati distributivi.

Le dimensioni degli artifact della baseline validata sono:

- PDF: `2.001.145` byte;
- DOCX: `785.750` byte;
- EPUB: `687.074` byte;
- Markdown assemblato: `1.859.987` byte.

## 3. Criterio editoriale applicato

La revisione finale non ha perseguito la riduzione meccanica della lunghezza. Ha perseguito la rimozione della forma da documentazione/slide quando non era necessaria.

Il criterio adottato su tutti i capitoli è stato:

**prosa per ragionamento, causalità, trade-off e casi; struttura soltanto quando la struttura è informazione.**

Sono quindi rimasti intenzionalmente strutturati artefatti come contract, review gate, decision matrix, checklist operative, rubric, runbook, mappe, template ed esercizi. Sono invece stati ricomposti in paragrafi i cataloghi di concetti, le sequenze di micro-heading, le domande retoriche in serie e le liste che non avevano funzione operativa.

La riduzione del page count rispetto alle candidate precedenti è coerente con questa scelta: il corpo conserva **321 file Markdown**, ma presenta meno frammentazione, whitespace e densità da slide.

## 4. Architettura editoriale finale

Il libro ora segue un percorso leggibile dall'inizio alla fine:

```text
responsabilità
→ framing
→ dato e semantica
→ EDA / incertezza
→ lifecycle / tempo
→ causalità / experimentation
→ prediction
→ SQL / architecture / tooling
→ AI-assisted analytics
→ decisione / comunicazione
→ routing end-to-end
→ analytics operating model
→ career operating model
```

Il Capitolo 17 impedisce che gli artefatti diventino una nuova pipeline obbligatoria attraverso **Capstone Routing Canvas** e **Method Budget**. Il Capitolo 18 decide quando un workflow ricorrente merita un **Analytics Operating Contract**. Il Capitolo 19 chiude il libro con **Personal Career Operating Plan** e ritorna alla tesi di *Al timone*.

Definizione finale mantenuta:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## 5. Source/factual audit

Il ledger dettagliato è in `SOURCE_FACTUAL_AUDIT.md`.

Il recheck finale del 5 settembre 2026 ha incluso in particolare:

- ILO, *Generative AI and jobs: A 2025 update*;
- World Economic Forum, *Future of Jobs Report 2025*;
- Microsoft, *2026 Work Trend Index*;
- Microsoft Research CHI 2025 sul critical thinking;
- Microsoft Learn, *Prepare your data for AI*;
- AWS Cloud Intelligence Dashboards guidance per cost allocation/unit metrics;
- Government Analysis Function sulla comunicazione di qualità/incertezza;
- NIST AI RMF 1.0 e stato della revisione in corso.

È stata applicata una correzione sostantiva di source hygiene: il precedente customer case NXP e i claim quantitativi `75% / 90%` sono stati rimossi dal Capitolo 17 e dall'audit. Il principio didattico resta supportato da documentazione AWS corrente, senza attribuire risultati aziendali non verificabili.

## 6. Front matter e reference layer

Front matter corrente:

- `front_matter/001_come_usare_questo_libro.md`;
- `front_matter/002_legenda_editoriale.md`;
- `front_matter/003_nota_autore_edizione.md`.

Il reading guide include ora anche Capstone Routing Canvas, Analytics Operating Contract e Personal Career Operating Plan e chiarisce che i casi non seguono una ricetta unica.

Reference layer corrente:

- `reference/001_glossario.md`;
- `reference/002_artefatti_operativi.md`.

Il glossario include i concetti introdotti nei capitoli finali — criticality tier, serving state, Method Budget, task exposure, responsibility moat, decision span, Delegation Boundary e verification reserve. L'indice degli artefatti non usa più la nozione di “catena canonica”: distingue la progressione didattica del libro dal routing di un caso reale.

## 7. CI e guardrail di build

La pipeline valida:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build_release.py
python scripts/build_epub.py
```

Il lint controlla continuità dei capitoli, heading, file vuoti, TODO/FIXME/TBD, URL contaminati, grafie ASCII legacy, formule/LaTeX, termini canonici e struttura editoriale. Gli output sono poi ispezionati per footnote, outline PDF, repeating header DOCX, first-page footer, author metadata, gerarchia del titolo ed EPUB structure/style.

## 8. Candidate storiche e prossimo release gate

`v1.0.0-rc1` e `v1.0.0-rc2` restano candidate storiche. RC2 era principalmente una revisione di identità editoriale e impaginazione e dichiarava esplicitamente di non modificare il contenuto sostantivo.

Il pass prose-first completato il 5 settembre 2026 è invece **sostantivo** e rende quelle candidate non più una baseline del manoscritto corrente. Non vengono sovrascritte e non viene pubblicata automaticamente una nuova release.

La prossima candidate pubblica, se scelta, dovrà quindi:

1. partire dall'head corrente con CI verde;
2. avere un nuovo identificatore di candidate, senza riutilizzare RC1/RC2;
3. produrre PDF/DOCX/EPUB dalla stessa pipeline validata;
4. aggiornare metadata e release notes senza riaprire il contenuto salvo difetti dimostrati.

Copyright, licenza definitiva, tag e promozione a release stabile restano decisioni di pubblicazione separate.

## 9. Stato editoriale finale

Il **manoscritto e i suoi apparati editoriali sono completi e validati** sulla baseline indicata. Non resta un capitolo successivo da revisionare.

Eventuali lavori successivi appartengono a una delle seguenti categorie: bug fattuale o tipografico, regressione di build, source decay, metadata di pubblicazione o nuova edizione sostantiva. Non costituiscono la continuazione del pass editoriale appena chiuso.