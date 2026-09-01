# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento è la dashboard editoriale del manoscritto.

## 1. Stato attuale

- Corpo principale completo: **Capitoli 0–19**.
- Review completata: **Capitoli 0–13**.
- Da revisionare: **Capitoli 14–19**.
- Markdown è la source of truth.
- CI attiva su `main` con lint + build Markdown/DOCX/PDF.
- Casi pubblici e casi simulati/compositi devono essere distinti esplicitamente.

### Ultima build validata

Dopo la review del Capitolo 13:

- **20 capitoli**;
- **321 file Markdown**;
- **213.785 parole stimate**;
- **1.566.819 caratteri**;
- **166 URL esterni distinti**;
- **8 file con LaTeX**;
- **966 pagine PDF**;
- build Markdown, DOCX e PDF: **SUCCESS**.

Il page count non è un obiettivo da massimizzare. La priorità è la densità di valore per pagina.

## 2. Controlli automatici

La pipeline esegue:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
python scripts/build.py
```

Il lint verifica, tra le altre cose:

- continuità dei capitoli;
- prefissi file duplicati/mancanti;
- heading incoerenti;
- file vuoti;
- `TODO`, `FIXME`, `TBD`;
- `utm_source=chatgpt.com`;
- grafie ASCII legacy;
- URL esterni;
- formule/LaTeX;
- conteggio parole.

### Warning residuo

Resta un solo warning globale:

- notazione matematica/LaTeX in **8 file**.

Prima della release bisognerà decidere se usare notazione testuale o un vero renderer matematico per le formule residue.

## 3. Convenzione casi e fonti

### Caso reale documentato

Deve avere:

- organizzazione/evento identificabile;
- fonte pubblica attendibile;
- claim proporzionato alla fonte;
- nessuna trasformazione indebita di associazione in causalità.

### Caso simulato/composito

Può usare nomi, numeri e circostanze costruiti per la didattica, ma deve essere riconoscibile come tale.

### Fonti

La review privilegia:

- standard e governi;
- documentazione ufficiale;
- letteratura accademica riconosciuta;
- fonti primarie di aziende/istituzioni per i casi pubblici.

Prima della release resta un audit globale dei **166 URL** per link, redirect, supporto del claim e uniformità delle note.

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
| 14 — AI-assisted analytics | **Da revisionare** | Workflow AI verificabile, valutato e governato. |
| 15 — Insight e decisione | **Da revisionare** | Decision quality, trade-off, expected value, reversibilità. |
| 16 — Storytelling/dashboard | **Da revisionare** | Comunicazione e visual evidence. |
| 17 — Casi end-to-end | **Da revisionare** | Laboratorio integrato. |
| 18 — Sistema analitico che scala | **Da revisionare** | Operating model, reliability, data products, governance. |
| 19 — Data Analyst 2026–2035 | **Da revisionare** | Skill, agent management, deskilling, carriera. |

## 5. Deliverable canonici

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
```

Non ogni analisi richiede tutti gli artefatti. Sono un vocabolario operativo per rischi differenti.

## 6. Confini concettuali principali

### 0 / 14 / 19 — AI

- **0:** ownership e supervisione umana;
- **14:** workflow operativo, eval, privacy, permission boundary, auditability;
- **19:** conseguenze su skill e carriera.

### 2 / 3 — specifica vs readiness

- **2:** cosa serve per rispondere;
- **3:** se i dati disponibili sono davvero fit for purpose.

### 3 / 4 / 5 — qualità, pattern, inferenza

- **3:** il dato è utilizzabile?
- **4:** quale struttura mostra?
- **5:** quanto possiamo generalizzare e con quale incertezza?

### 4 / 7 / 8 — tempo e causalità

- **4:** descrizione temporale;
- **7:** struttura temporale, anomalie e forecast;
- **8:** attribuzione causale e controfattuale.

### 5 / 8 / 9 — inferenza, identificazione, esperimento

- **5:** teoria inferenziale;
- **8:** identification assumptions;
- **9:** preservare il confronto in un esperimento reale.

### 6 / 8 / 9 / 10 — comportamento, intervento, prediction

- **6:** localizzare il lifecycle risk;
- **8:** identificare effetti;
- **9:** testare interventi;
- **10:** anticipare eventi e trasformare score in policy.

### 10 / 15 — policy predittiva vs decision framework

- **10:** soglia/top-K, capacità e costi degli errori;
- **15:** confronto generale tra alternative e trade-off.

### 11 / 12 / 13 — significato, flusso, strumento

**Capitolo 11**

> Che cosa deve significare il dataset?

→ **Analytical Data Contract**

**Capitolo 12**

> Da dove arriva e con quali garanzie?

→ **Data Flow Architecture Map**

**Capitolo 13**

> Quale ambiente è proporzionato alla parte di lavoro che dobbiamo eseguire o servire?

→ **Tooling Decision Record**

### 13 / 14 — AI economics vs AI governance

- **13:** l'AI abbassa build/switching cost;
- **14:** come verificare e governare gli output prodotti con AI.

Il Capitolo 14 non deve ripetere il manifesto del Capitolo 0 né la tool economics del 13.

### 13 / 18 — workflow locale vs operating model

- **13:** scelta/migrazione del singolo workflow;
- **18:** standard e ownership organizzativi che permettono di scalare.

## 7. Note review Capitoli 11–13

### Capitolo 11

Il capitolo non è più un tutorial SQL. Grain, join, aggregazioni, window functions, CTE, star schema, temporalità, dedup, many-to-many, test, incrementalità e AI-assisted SQL convergono nell'**Analytical Data Contract**.

Il caso finale usa contribution margin per categoria, evitando un'ulteriore ripetizione dei casi retention.

### Capitolo 12

Il capitolo non è più un glossario di tecnologie. Usa la **Data Flow Architecture Map**:

```text
source → capture → transport → storage → transform → serve → consume
```

Ogni boundary considera latency, freshness/completeness, ownership, failure, replay/backfill, recovery e costo.

Il semantic layer resta serving boundary, senza duplicare il Capitolo 11. Batch/streaming distingue event time, processing time, watermark, late data e output provisional/reconciled. Orchestration considera readiness del dato e non soltanto job `SUCCESS`.

### Capitolo 13

La domanda non è più “Excel vs SQL vs Python vs BI”.

Il **Tooling Decision Record** valuta:

```text
problem shape
→ stage
→ rischio
→ riproducibilità
→ candidate
→ TCO
→ ownership
→ scelta minima sufficiente
→ exit condition
```

Concetti introdotti/rafforzati:

- spreadsheet come reasoning surface vs hidden production system;
- compute near data / pushdown vs pull-out;
- notebook come laboratorio con hidden state;
- BI come superficie di consumo per domande stabilizzate;
- shared/managed compute come scelta operativa, non badge “cloud”;
- complexity budget per no-code;
- AI: build cost ≠ ownership cost;
- livelli di riproducibilità R0–R4;
- livelli prototipo-produzione P0–P3;
- promotion gate, shadow run/parity test;
- TCO = build + run + maintenance + coordination + skills + reliability + migration + error + delay;
- **exit condition** obbligatoria per sapere quando rivalutare il tool.

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
→ casi completi
→ scala
→ futuro
```

## 9. Lavori ancora necessari prima della release

- review Capitoli 14–19;
- audit link/fonti globale;
- formula rendering;
- frontespizio;
- copyright/licenza;
- autore e bio;
- “come usare il libro”;
- indice automatico;
- glossario opzionale;
- bibliografia/indice fonti;
- indice analitico opzionale;
- ringraziamenti;
- numero/versione release;
- proofread ortografico finale;
- controllo tabelle, code block, footnote e page break nel PDF/DOCX.

## 10. Release gate

Prima di una release candidata:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di:

1. indice e ordine capitoli;
2. formule;
3. tabelle;
4. blocchi di codice;
5. fonti e link;
6. casi reali vs compositi;
7. ripetizioni inter-capitolo;
8. ortografia/punteggiatura;
9. footnote;
10. page break e pagine di apertura/chiusura;
11. continuità dei deliverable canonici.

## 11. Prossimo blocco

La review continua dal **Capitolo 14 — AI-assisted analytics: accelerare senza perdere rigore**.

Direzione editoriale:

```text
task
→ context
→ permission boundary
→ generation
→ verification
→ evaluation
→ escalation
→ decision
→ audit trail
```

Il Capitolo 0 resta il manifesto della responsabilità umana. Il Capitolo 13 spiega l'effetto dell'AI sull'economia del tooling. Il Capitolo 14 deve insegnare come produrre **evidenza verificabile** con sistemi AI senza abbassare lo standard professionale.
