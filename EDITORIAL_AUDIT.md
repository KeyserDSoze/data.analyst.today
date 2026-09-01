# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento registra lo stato della revisione del manoscritto dopo il completamento del corpo principale, Capitoli 0–19.

## 1. Struttura del repository

### Corretto

- Il libro parte da `chapters/000_chapter/` con **Capitolo 0 — Al timone**.
- I capitoli proseguono in modo continuo fino a `019_chapter`.
- I prefissi numerici duplicati presenti in diversi capitoli sono stati normalizzati.
- `scripts/build.py` usa un ordinamento deterministico `(prefisso numerico, nome file)`.
- Gli artefatti generati `.md`, `.docx` e `.pdf` dentro `build/` sono ignorati da Git.
- Le sezioni interne sono state normalizzate a `##`/`###`; non restano H1 spurii nel manoscritto.
- Le grafie ASCII come `e'`, `piu'`, `puo'` sono state normalizzate nelle sorgenti, evitando codice e URL.

### Regola

Per ogni capitolo:

- `001_*.md` contiene il titolo del capitolo;
- i file successivi seguono un ordine numerico univoco e contiguo;
- il primo heading del capitolo usa `#`;
- le sezioni interne usano `##`, `###`, ecc.

## 2. Build Markdown → DOCX/PDF

### Corretto

Il builder:

- ordina le sorgenti in modo deterministico;
- abilita le tabelle Markdown;
- evita la duplicazione dei blockquote;
- conserva grassetto, corsivo e codice inline nei principali output;
- gestisce tabelle in DOCX e PDF;
- non trasforma ogni separatore orizzontale in un page break;
- crea page break sui veri titoli di capitolo.

La CI costruisce automaticamente Markdown aggregato, DOCX e PDF a ogni modifica del `main`.

### Ultima build validata

Dopo la revisione editoriale dei Capitoli 0–7:

- **20 capitoli**;
- **321 file Markdown**;
- **189.667 parole stimate**;
- **1.368.385 caratteri**;
- **131 URL esterni distinti**;
- **836 pagine PDF**;
- build Markdown, DOCX e PDF completata con successo.

Il numero di pagine non è una metrica editoriale da massimizzare. Può salire o scendere durante la revisione: alcuni passaggi vengono compressi perché ridondanti, altri vengono resi più chiari con esempi, tabelle, casi operativi e fonti reali più forti.

### Da completare prima della release tipografica

- rendering professionale delle formule matematiche ancora scritte con notazione LaTeX;
- indice/TOC con numeri di pagina nella versione impaginata;
- verifica della resa di tabelle molto larghe;
- controllo di widows/orphans, code block lunghi e page break;
- stile definitivo per note, fonti e callout.

## 3. Lint e normalizzazione automatica

Sono disponibili:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py
```

La CI esegue entrambi prima della build.

Il lint controlla, tra le altre cose:

- continuità dei capitoli;
- prefissi duplicati o mancanti;
- corrispondenza tra filename e numero della sezione;
- H1 usati accidentalmente per sezioni interne;
- file vuoti;
- `TODO`, `FIXME`, `TBD`;
- presenza di `utm_source=chatgpt.com`;
- numero di URL esterni;
- presenza di formule/LaTeX;
- ortografia ASCII;
- conteggio di parole e stima indicativa delle pagine.

### Stato corrente del lint

La struttura è valida e le sorgenti risultano normalizzate.

Resta **un solo warning globale**:

- notazione matematica/LaTeX presente in **13 file**, da gestire nella pipeline tipografica.

Il numero è sceso progressivamente da 25 a 13 durante la revisione: formule semplici sono state rese leggibili in notazione testuale quando il typesetting non aggiungeva valore; le formule che hanno reale funzione didattica restano invece in sorgente matematica.

Per una release candidata:

```bash
python scripts/lint_book.py --strict
python scripts/build.py
```

dovrà terminare senza warning editoriali bloccanti.

## 4. Formule matematiche

Nel manoscritto restano formule in blocchi del tipo:

```text
\[
NRR = \frac{...}{...}
\]
```

Il contenuto matematico è corretto come sorgente testuale, ma il builder non dispone ancora di un vero motore di typesetting matematico.

### Decisione editoriale da prendere

Scegliere uno dei tre approcci:

1. mantenere formule semplici in notazione testuale leggibile;
2. aggiungere un renderer matematico alle build DOCX/PDF;
3. utilizzare una pipeline tipografica dedicata per la release finale.

Per un libro professionale la seconda o la terza opzione sono preferibili per le formule che hanno reale valore didattico.

## 5. Casi reali e casi simulati

### Convenzione fissata

Il Capitolo 0 e il README dichiarano esplicitamente:

- **caso reale documentato**: supportato da una fonte pubblica attendibile;
- **caso simulato/composito**: costruito a fini didattici.

Durante la revisione editoriale i casi fittizi vengono marcati esplicitamente quando possono essere letti come narrazioni reali.

### Da verificare in ogni capitolo

Ogni caso reale importante deve avere:

- organizzazione identificabile;
- fonte leggibile;
- claim proporzionato a ciò che la fonte documenta;
- nessuna confusione tra correlazione, causalità e risultato commerciale dichiarato.

## 6. Fonti e link

### Corretto

- Nessun link nel manoscritto contiene `utm_source=chatgpt.com`.
- Le revisioni mantengono la preferenza per documentazione ufficiale e fonti primarie.
- Il Capitolo 3 usa il Government Data Quality Framework britannico e include il Mars Climate Orbiter come caso reale documentato sulla semantica delle unità.
- Il Capitolo 4 usa NIST per EDA, scatter plot, time series, smoothing e box plot; include il quartetto di Anscombe e il caso Berkeley 1973 per composizione e Simpson's paradox.
- Il Capitolo 5 usa NIST per distribuzioni, CLT e confidence intervals; AAPOR per sampling, margin of sampling error e fonti di errore nelle survey; ASA per l'interpretazione del p-value; include il **Literary Digest 1936** come caso reale documentato sul fallimento di una grande numerosità ottenuta con un meccanismo di selezione inadeguato.
- Il Capitolo 6 usa Duolingo Q4/FY 2024 come caso reale documentato di engagement/retention, Canal+ per segmentazione comportamentale e retention, Microsoft Learn per cohort analysis, Google Analytics per funnel aperti/chiusi e sequenza degli step, Stripe per churn involontario/revenue recovery e NIST per survival, hazard e censoring.
- Il Capitolo 7 usa NIST per time-series structure, autocorrelation, stationarity e change-point; Hyndman & Athanasopoulos per baseline, time-series cross-validation, MASE e prediction intervals. Include **Google Flu Trends** come caso reale documentato: il paper di Lazer et al. mostra sovrastima in 100 settimane su 108 nella finestra agosto 2011–settembre 2013, struttura temporale negli errori e performance migliore di benchmark/combinazioni che incorporavano dati CDC e stagionalità.

### Da fare prima della release

- controllare sistematicamente link rotti e redirect;
- verificare che ogni fonte supporti davvero il claim a cui è associata;
- uniformare le sezioni `Fonti`, `Riferimenti` e `Approfondimenti`;
- valutare una bibliografia generale o un indice delle fonti;
- registrare data di accesso solo dove editorialmente utile.

## 7. Revisione editoriale capitolo per capitolo

Obiettivo della revisione:

- togliere ridondanze senza assottigliare il contenuto;
- dare a ogni sezione un ruolo distinto;
- preferire rimandi interni alla ripetizione integrale;
- rafforzare il percorso `teoria → esempio → errore → metodo`;
- rendere esplicita la natura simulata/composita dei casi fittizi;
- preservare e migliorare i casi reali documentati;
- uniformare terminologia, tono e profondità.

### Stato

| Capitolo | Stato editoriale | Nota |
|---|---|---|
| 0 — Al timone | **Revisionato** | Manifesto operativo: orchestrazione, accountability, verification by design, stop condition, deskilling, trust levels, caso multi-agent e manifesto finale. |
| 1 — Tutto è cambiato. Il problema è rimasto lo stesso | **Revisionato** | Eliminata duplicazione con Ch. 0; una sola catena analitica canonica; cinque tipi di domanda; caso vendite marcato simulato/composito; rimandi specialistici. |
| 2 — Dal problema di business al problema analitico | **Revisionato** | Converge sull'**Analytical Brief**: decision specification, stakeholder map, metric roles, hypothesis register, scope, baseline, segmentation plan, data requirements, Value of Information e stop rule. |
| 3 — Capire il dato prima di analizzarlo | **Revisionato** | Indagine di data readiness: record/grain → identità → tempo → qualità → missing/duplicati/outlier → unità → profiling → lineage → riconciliazione → contract/check automatici → verdetto **PRONTO / CON CAVEAT / NON PRONTO**. Caso ProntoVeloce e Mars Climate Orbiter. |
| 4 — Statistica descrittiva ed Exploratory Data Analysis | **Revisionato** | Processo di controllo dell'interpretazione: centro → dispersione → code/forma → confronti/Simpson → relazioni → tempo → sensitivity → denominatori/comparabilità → caso MercatoHub. Deliverable: **EDA Evidence Map**. |
| 5 — Probabilità, campionamento e incertezza | **Revisionato** | Rifondato come capitolo dell'incertezza. Distingue variabilità del processo e incertezza della stima; probabilità/condizionamento/dipendenza → distribuzioni/expected value/Bayes → sampling/sampling distribution/SE/CLT/CI → sample size → hypothesis test/p-value → Type I-II/power → materialità → multiple testing. Deliverable: **Uncertainty Brief**. Caso reale Literary Digest; ASA come riferimento centrale sul p-value. |
| 6 — Segmentazione, coorti e lifecycle analysis | **Revisionato** | Segmento = chi; coorte = quando/a quale età; funnel = dove; activation/TTV = primo valore; retention/survival = persistenza e momento fragile; churn = perdita di relazione/valore e involuntary churn; reactivation = ritorno vs recupero duraturo; cohort value/LTV = economics; prediction distinta da causalità/actionability. Deliverable: **Lifecycle Diagnostic Map**. Casi reali Duolingo e Canal+; Stripe e NIST come riferimenti operativi. |
| 7 — Serie temporali, anomalie e forecasting | **Revisionato** | Rifondato attorno alla disciplina temporale: baseline comparabile → trend/stagionalità/calendar → lag/autocorrelazione → stazionarietà/decomposizione → anomaly triage → target/origin/horizon → baseline forecast → backtest `as-of` → MAE/RMSE/MAPE/MASE + business loss → prediction interval/coverage → drift/regime/override. Deliverable: **Temporal Decision Brief**. Caso reale Google Flu Trends; caso ElectroOne esplicitamente simulato/composito. |
| 8–19 | **Da revisionare** | Procedere in ordine, controllando anche sovrapposizioni inter-capitolo. |

## 8. Sovrapposizioni concettuali da governare

Le ripetizioni principali devono diventare richiami intenzionali.

### Capitolo 0 / 14 / 19 — AI

- **0 — Al timone:** mentalità, responsabilità, delega, supervisione;
- **14 — AI-assisted analytics:** uso operativo, eval, privacy, auditability, workflow;
- **19 — 2026–2035:** conseguenze sul ruolo, skill e carriera.

Regola: non rispiegare integralmente il manifesto del Capitolo 0 nei capitoli successivi.

### Capitolo 1 / 2 — domanda analitica

- **1:** mentalità di base, cinque tipi di domanda e catena analitica canonica;
- **2:** trasformare formalmente la richiesta in un Analytical Brief operativo.

### Capitolo 2 / 3 — specifica e readiness

- **2:** dichiarare quali dati, popolazioni, metriche e confronti servono;
- **3:** verificare che i dati disponibili rappresentino davvero quelle proprietà.

Catena:

**Analytical Brief → Data Readiness Review → Analisi**.

### Capitolo 3 / 4 — qualità vs esplorazione

- **3:** “questo valore/record è valido per l'uso previsto?”;
- **4:** “dato che è valido, quanto influenza struttura e conclusione?”.

### Capitolo 4 / 5 — pattern vs incertezza inferenziale

- **4 — EDA:** che cosa mostra il campione osservato e quanto è robusto il pattern alle letture alternative?
- **5 — Inferenza:** quanto è precisa la stima, che cosa possiamo generalizzare oltre il campione e quali fonti di incertezza non sono incluse nel modello statistico?

Deliverable:

**EDA Evidence Map → Uncertainty Brief**.

### Capitolo 4 / 6 — segmentazione esplorativa vs lifecycle

- **4:** segmentare per verificare se un pattern aggregato cambia tra sottogruppi;
- **6:** segmentare per identificare popolazioni con traiettorie di activation, retention, churn o valore abbastanza diverse da richiedere diagnosi e azioni differenti.

Regola: il Capitolo 6 non deve rispiegare la segmentazione come tecnica EDA generale.

### Capitolo 5 / 9 — inferenza vs experimentation

- **5:** significato di effect size, CI, p-value, Type I/II, power, sample size e multiple testing;
- **9:** progettazione e conduzione di esperimenti reali: randomizzazione, unità, SRM, contaminazione, novelty, peeking, stopping, CUPED, metriche, rollout/rollback.

Regola: il Capitolo 5 insegna a leggere l'evidenza; il 9 insegna a costruire un esperimento affidabile che produca quell'evidenza.

### Capitolo 5 / 10 — probabilità vs modelli predittivi

- **5:** probabilità condizionata, base rate, calibrazione concettuale e incertezza della stima;
- **10:** score predittivi, discrimination, calibration, precision/recall, threshold, leakage, drift e deployment.

### Capitolo 5 / 15 — incertezza vs decisione

- **5:** quantificare incertezza, effect size e precisione;
- **15:** combinare evidenza, economia, scenari, expected value, soglie e reversibilità in una raccomandazione.

### Capitolo 6 / 8 / 9 / 10 — lifecycle, causalità, intervento e prediction

- **6:** localizzare dove il lifecycle differisce e distinguere rischio, valore e actionability;
- **8:** identificare effetti causali e ragionare sul controfattuale;
- **9:** testare interventi con esperimenti affidabili;
- **10:** costruire e monitorare modelli predittivi.

Regola: in Ch. 6 una feature associata a retention o churn è un segnale/ipotesi; non diventa automaticamente una leva causale.

### Capitolo 4 / 7 / 8 — tempo, forecast e causalità

- **4:** tempo come dimensione esplorativa e confronto descrittivo;
- **7:** dipendenza temporale, baseline, anomaly detection, forecast, backtest e regime change;
- **8:** controfattuale e attribuzione causale.

Regola: un'anomalia o un errore di forecast può indicare che il processo è cambiato, ma non identifica da solo la causa del cambiamento.

### Capitolo 7 / 10 — forecasting vs predictive modeling generale

- **7:** il tempo impone ordine, horizon, autocorrelazione, `as-of` validation, seasonal baselines e regime monitoring;
- **10:** valutazione e deployment di modelli predittivi più generali, inclusi classification/regression, calibration, threshold, leakage e drift.

Regola: non ripetere in Ch. 10 la disciplina specifica del backtest temporale; richiamarla quando il target è futuro o time-dependent.

### Capitolo 7 / 15 — forecast vs decisione

- **7:** produrre e validare una distribuzione di forecast credibile e collegarla a una funzione di errore/loss;
- **15:** scegliere tra alternative con expected value, scenari, soglie, reversibilità e trade-off.

Regola: il Temporal Decision Brief porta il forecast fino al punto in cui informa la decisione, ma non rispiega l'intero framework decisionale del Ch. 15.

### Capitolo 3 / 11 / 12 / 18 — qualità, semantica, governance

- **3:** fitness for purpose dal punto di vista dell'analista;
- **11:** grain, join, trasformazioni e metriche in SQL/modeling;
- **12:** architettura che produce e trasporta il dato;
- **18:** qualità, ownership, contract e observability come capacità organizzativa scalabile.

## 9. Arco narrativo complessivo

La sequenza resta coerente:

**mentalità → domanda → dati → statistica → comportamento → tempo → causalità → esperimenti → modelli → SQL → architettura → strumenti → AI → decisione → comunicazione → casi completi → scala → futuro**.

Nei primi otto capitoli il percorso operativo è ora esplicito:

**Analytical Brief → Data Readiness Review → EDA Evidence Map → Uncertainty Brief → Lifecycle Diagnostic Map → Temporal Decision Brief**.

Il Capitolo 7 porta la lettura del tempo dall'osservazione alla previsione disciplinata: la serie viene definita, la baseline scelta, la dipendenza temporale resa esplicita, gli alert triaggiati, il forecast confrontato con benchmark semplici e validato `as-of`, l'errore tradotto in loss e l'incertezza verificata attraverso prediction intervals e coverage. Il capitolo si ferma prima dell'attribuzione causale, che appartiene al Capitolo 8.

## 10. Lunghezza

La misura corrente viene dalla pipeline reale.

Dopo i Capitoli 0–7 revisionati il PDF è di **836 pagine**. La revisione può quindi continuare liberamente a comprimere ripetizioni o ad ampliare esempi e casi che aumentano la comprensione senza alcun rischio rispetto all'obiettivo minimo di 400+ pagine.

L'obiettivo è massimizzare **densità di valore per pagina**, non il page count.

## 11. Elementi editoriali ancora mancanti

Prima della prima release stabile valutare:

- frontespizio definitivo;
- copyright/licenza;
- autore e bio;
- introduzione al lettore / come usare il libro;
- indice automatico;
- eventuale glossario;
- bibliografia/indice delle fonti;
- indice analitico, se il formato finale lo permette;
- ringraziamenti;
- numero/versione della release.

## 12. Release gate

Una release candidata dovrebbe passare:

```bash
python scripts/normalize_sources.py --check
python scripts/lint_book.py --strict
python scripts/build.py
```

Poi controllo manuale di:

1. indice e ordine dei capitoli;
2. formule;
3. tabelle;
4. blocchi di codice;
5. fonti e link;
6. casi reali vs simulati;
7. ripetizioni tra capitoli;
8. ortografia e punteggiatura;
9. pagina iniziale/finale di ogni capitolo;
10. page count reale.

## Stato sintetico

Il contenuto principale del libro è strutturalmente completo.

La revisione editoriale ha completato i **Capitoli 0–7**. Il lavoro successivo continua dal Capitolo 8, con il compito di trasformare causalità e controfattuale da catalogo di metodi in un processo di identificazione: definire l'effetto, esplicitare il controfattuale, disegnare le assunzioni, scegliere il comparison group e dichiarare che cosa il design consente davvero di attribuire causalmente.
