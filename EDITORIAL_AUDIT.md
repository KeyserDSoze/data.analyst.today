# Editorial audit — data.analyst.today

Ultimo aggiornamento: 1 settembre 2026.

Questo documento registra lo stato della revisione del manoscritto dopo il completamento del corpo principale, Capitoli 0–19.

## 1. Struttura del repository

### Stato corretto

- Il libro parte da `chapters/000_chapter/` con **Capitolo 0 — Al timone**.
- I capitoli proseguono senza interruzioni fino a `019_chapter`.
- I prefissi numerici duplicati presenti in diversi capitoli sono stati normalizzati.
- `scripts/build.py` usa ordinamento deterministico `(prefisso numerico, nome file)`.
- Gli artefatti generati `.md`, `.docx` e `.pdf` dentro `build/` sono ignorati da Git.
- Le sezioni interne sono normalizzate a `##`/`###`; non restano H1 spurii nel manoscritto.
- Le grafie ASCII come `e'`, `piu'`, `puo'` sono state normalizzate nelle sorgenti evitando codice e URL.

### Regola strutturale

Per ogni capitolo:

- `001_*.md` contiene il titolo del capitolo;
- i file successivi seguono ordine numerico univoco e contiguo;
- il primo heading del capitolo usa `#`;
- le sezioni interne usano `##`, `###`, ecc.

## 2. Build Markdown → DOCX/PDF

Il builder:

- ordina le sorgenti in modo deterministico;
- abilita tabelle Markdown;
- evita duplicazioni nei blockquote;
- conserva grassetto, corsivo e codice inline nei principali output;
- gestisce tabelle in DOCX e PDF;
- non trasforma ogni separatore orizzontale in un page break;
- crea page break sui veri titoli di capitolo.

La CI costruisce automaticamente Markdown aggregato, DOCX e PDF a ogni modifica del `main`.

### Ultima build validata

Dopo la revisione editoriale dei Capitoli **0–10**:

- **20 capitoli**;
- **321 file Markdown**;
- **203.538 parole stimate**;
- **1.481.229 caratteri**;
- **148 URL esterni distinti**;
- **909 pagine PDF**;
- build Markdown, DOCX e PDF completata con successo.

Il numero di pagine non è una metrica da massimizzare. La revisione può comprimere ripetizioni o ampliare esempi che aumentano la comprensione. L'obiettivo è massimizzare **densità di valore per pagina**.

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
- H1 accidentali;
- file vuoti;
- `TODO`, `FIXME`, `TBD`;
- presenza di `utm_source=chatgpt.com`;
- numero di URL esterni;
- formule/LaTeX;
- grafie ASCII;
- conteggio parole e pagine indicative.

### Warning residuo

La struttura è valida e le sorgenti risultano normalizzate.

Resta **un solo warning globale**:

- notazione matematica/LaTeX presente in **8 file**, da gestire nella pipeline tipografica.

Il numero è sceso da 25 a 8 durante la revisione: formule semplici vengono rese in notazione testuale quando il typesetting non aggiunge valore; quelle con reale funzione didattica restano invece in sorgente matematica.

## 4. Formule matematiche

Nel manoscritto restano formule in blocchi del tipo:

```text
\[
...
\]
```

Il contenuto matematico è corretto come sorgente, ma il builder non dispone ancora di un vero motore di typesetting matematico.

Prima della release tipografica scegliere tra:

1. notazione testuale per formule semplici;
2. renderer matematico nelle build DOCX/PDF;
3. pipeline tipografica dedicata.

Per le formule con funzione didattica sono preferibili la seconda o la terza opzione.

## 5. Casi reali e casi simulati

Convenzione fissata nel Capitolo 0 e nel README:

- **caso reale documentato**: supportato da fonte pubblica attendibile;
- **caso simulato/composito**: costruito a fini didattici.

Durante la revisione i casi fittizi vengono marcati esplicitamente quando potrebbero essere letti come eventi realmente accaduti.

Ogni caso reale importante deve avere:

- organizzazione identificabile;
- fonte leggibile;
- claim proporzionato a ciò che la fonte documenta;
- nessuna confusione tra correlazione, causalità e risultato dichiarato.

## 6. Fonti e link

### Stato corretto

- Nessun link nel manoscritto contiene `utm_source=chatgpt.com`.
- Le revisioni privilegiano fonti primarie, standard, documentazione ufficiale e letteratura riconosciuta.
- Il Capitolo 3 usa il Government Data Quality Framework e il Mars Climate Orbiter.
- Il Capitolo 4 usa NIST, quartetto di Anscombe e Berkeley 1973.
- Il Capitolo 5 usa NIST, AAPOR, ASA e Literary Digest 1936.
- Il Capitolo 6 usa Duolingo, Canal+, Microsoft Learn, Google Analytics, Stripe e NIST.
- Il Capitolo 7 usa NIST, Hyndman & Athanasopoulos e Google Flu Trends.
- Il Capitolo 8 usa World Bank / Inter-American Development Bank per counterfactuals e impact evaluation, Stanford per causal inference e il Premio Nobel 2021 per natural experiments e contributi metodologici di Card, Angrist e Imbens.
- Il Capitolo 9 usa Microsoft Experimentation Platform / Microsoft Research per SRM, metric sensitivity, variance reduction/CUPED, A/A'/B, experimentation health e test di modifiche infrastrutturali.
- Il Capitolo 10 usa la documentazione ufficiale scikit-learn per leakage, pipeline, calibration, threshold tuning, permutation importance e model evaluation; usa Google *Rules of Machine Learning* e le guide Production ML per baseline semplici, test cronologici, training-serving skew e monitoring del sistema reale.

### Da fare prima della release

- controllare sistematicamente link rotti e redirect;
- verificare che ogni fonte supporti il claim associato;
- uniformare sezioni `Fonti`, `Riferimenti` e `Approfondimenti`;
- valutare bibliografia generale o indice delle fonti;
- registrare data di accesso solo dove editorialmente utile.

## 7. Revisione editoriale capitolo per capitolo

Obiettivi:

- togliere ridondanze senza assottigliare il contenuto;
- dare a ogni sezione un ruolo distinto;
- preferire rimandi interni alla ripetizione integrale;
- rafforzare `teoria → esempio → errore → metodo`;
- rendere esplicita la natura simulata/composita dei casi fittizi;
- preservare e migliorare i casi reali documentati;
- uniformare terminologia, tono e profondità.

### Stato

| Capitolo | Stato editoriale | Deliverable / ruolo |
|---|---|---|
| 0 — Al timone | **Revisionato** | Manifesto operativo: orchestrazione, accountability, verifica, stop condition, deskilling, trust levels. |
| 1 — Tutto è cambiato. Il problema è rimasto lo stesso | **Revisionato** | Una sola catena analitica canonica, cinque tipi di domanda, confine chiaro con AI e tool. |
| 2 — Dal problema di business al problema analitico | **Revisionato** | **Analytical Brief**. |
| 3 — Capire il dato prima di analizzarlo | **Revisionato** | **Data Readiness Review** con verdetto PRONTO / CON CAVEAT / NON PRONTO. |
| 4 — Statistica descrittiva ed EDA | **Revisionato** | **EDA Evidence Map**. |
| 5 — Probabilità, campionamento e incertezza | **Revisionato** | **Uncertainty Brief**. |
| 6 — Segmentazione, coorti e lifecycle analysis | **Revisionato** | **Lifecycle Diagnostic Map**. |
| 7 — Serie temporali, anomalie e forecasting | **Revisionato** | **Temporal Decision Brief**. |
| 8 — Causalità, confondenti e ragionamento controfattuale | **Revisionato** | **Causal Identification Brief**: estimand → assignment → causal model → counterfactual → identification → diagnostics → effect → scope → claim. |
| 9 — Experimentation e A/B testing nel mondo reale | **Revisionato** | **Experiment Contract**: decision → treatment → eligibility/unità → metric contract → MDE/feasibility → inference plan → health gate → decision matrix → rollout/rollback → learning record. |
| 10 — Regressione e modelli predittivi per Data Analyst | **Revisionato** | **Predictive Decision Card**: decision → prediction unit/time → target/horizon → feature `as-of` → baseline → validation → ranking/calibration → policy/capacity → monitoring → policy-effect evaluation. |
| 11–19 | **Da revisionare** | Procedere in ordine, controllando anche le sovrapposizioni inter-capitolo. |

## 8. Confini concettuali da governare

### Capitolo 0 / 14 / 19 — AI

- **0:** mentalità, responsabilità, delega, supervisione;
- **14:** uso operativo dell'AI, eval, privacy, auditability e workflow;
- **19:** conseguenze sul ruolo, skill e carriera.

Regola: non rispiegare integralmente il manifesto del Capitolo 0 nei capitoli successivi.

### Capitolo 1 / 2 — domanda analitica

- **1:** mentalità di base e tipi di domanda;
- **2:** trasformazione formale della richiesta in Analytical Brief.

### Capitolo 2 / 3 — specifica e readiness

- **2:** dichiarare dati, popolazioni, metriche e confronti necessari;
- **3:** verificare che i dati disponibili rappresentino davvero quelle proprietà.

Catena:

**Analytical Brief → Data Readiness Review → Analisi**.

### Capitolo 3 / 4 — qualità vs esplorazione

- **3:** “questo valore/record è valido per l'uso previsto?”;
- **4:** “dato che è valido, quanto influenza struttura e conclusione?”.

### Capitolo 4 / 5 — pattern vs inferenza

- **4:** che cosa mostra il campione osservato e quanto è robusto il pattern;
- **5:** quanto è precisa la stima e cosa possiamo generalizzare.

### Capitolo 4 / 6 — segmentazione vs lifecycle

- **4:** segmentazione come verifica di pattern aggregati;
- **6:** segmentazione come identificazione di traiettorie che richiedono diagnosi/azioni differenti.

### Capitolo 4 / 7 / 8 — tempo e causalità

- **4:** tempo come dimensione esplorativa;
- **7:** dipendenza temporale, anomaly detection e forecasting;
- **8:** controfattuale e attribuzione causale.

Un'anomalia o forecast error può indicare cambiamento, ma non identifica la causa.

### Capitolo 5 / 8 / 9 — inferenza, causal identification, experimentation

- **5:** effect size, CI, p-value, Type I/II, power, sample size, multiple testing;
- **8:** quale comparison group e quali assunzioni identificano un effetto causale;
- **9:** come progettare, eseguire, monitorare e decidere con un esperimento reale.

Regola: il Capitolo 9 richiama power e randomizzazione come requisiti del design, senza rispiegare da zero la teoria già consolidata nei Capitoli 5 e 8.

### Capitolo 8 / 9 — causal identification vs experiment operations

- **8:** perché il design randomizzato identifica un effetto e che cosa l'estimand significa;
- **9:** come preservare quel confronto attraverso assignment, exposure, telemetria, metriche, stopping e rollout.

Regola: un RCT causalmente valido sulla carta può diventare non interpretabile se il sistema di experimentation rompe il confronto in produzione.

### Capitolo 6 / 8 / 9 / 10 — lifecycle, causalità, esperimento, prediction

- **6:** localizzare lifecycle risk e actionability;
- **8:** identificare causal effect e treatment heterogeneity;
- **9:** testare interventi in sistemi reali;
- **10:** anticipare eventi/rischi e trasformare score in policy operative.

Una feature associata a churn è un segnale, non automaticamente una leva. Prediction identifica dove probabilmente avverrà un evento; causal inference ed experimentation stabiliscono se una specifica azione può modificarlo.

### Capitolo 5 / 10 — probabilità vs predictive probabilities

- **5:** probabilità, base rate e incertezza come concetti inferenziali;
- **10:** discrimination, calibration, threshold, ranking e deployment di score predittivi.

Regola: il Capitolo 10 usa la probabilità come output operativo e non ripete la teoria inferenziale del Capitolo 5.

### Capitolo 7 / 10 — forecasting vs predictive modeling generale

- **7:** ordine temporale, horizon, autocorrelazione, `as-of` validation, seasonal baselines e regime monitoring;
- **10:** validation generale per classification/regression, group split, leakage, calibration, threshold, class imbalance, interpretability e production monitoring.

Regola: il Capitolo 10 richiama la disciplina temporale quando il target è futuro, ma non ripete il backtesting specifico delle serie temporali.

### Capitolo 8 / 10 — causal effect vs predictive importance

- **8:** effect of intervention;
- **10:** feature contribution al ranking/score.

Feature importance, coefficienti e local explanations descrivono il comportamento del modello predittivo. Non diventano causal claims senza un identification design separato.

### Capitolo 9 / 10 — experiment policy vs predictive policy

- **9:** verificare causalmente un trattamento e governarne rollout/rollback;
- **10:** usare uno score per prioritizzare o attivare una policy.

Quando lo score determina chi riceve un trattamento, la Predictive Decision Card deve indicare come verrà valutato separatamente l'effetto incrementale della policy, per esempio tramite holdout o esperimento.

### Capitolo 10 / 15 — prediction economics vs decision framework

- **10:** scegliere operating threshold/top-K in funzione di capacità, costi degli errori e valore a rischio;
- **15:** confrontare alternative decisionali più ampie con expected value, scenari, reversibilità e trade-off.

Il Capitolo 10 porta lo score fino a una policy operativa; il Capitolo 15 resta il framework generale per la qualità della decisione.

### Capitolo 3 / 11 / 12 / 18 — qualità, semantica, governance

- **3:** fitness for purpose dal punto di vista dell'analista;
- **11:** grain, join, trasformazioni e metriche in SQL/modeling;
- **12:** architettura che produce e trasporta il dato;
- **18:** ownership, contract e observability come capacità organizzativa scalabile.

## 9. Arco narrativo complessivo

La sequenza resta coerente:

**mentalità → domanda → dati → statistica → comportamento → tempo → causalità → esperimenti → modelli → SQL → architettura → strumenti → AI → decisione → comunicazione → casi completi → scala → futuro**.

Il percorso operativo nei primi undici capitoli è ora:

**Analytical Brief → Data Readiness Review → EDA Evidence Map → Uncertainty Brief → Lifecycle Diagnostic Map → Temporal Decision Brief → Causal Identification Brief → Experiment Contract → Predictive Decision Card**.

Il Capitolo 10 rifonda il predictive modeling come sistema decisionale. Prima dell'algoritmo vengono fissati prediction unit, prediction time, horizon, label e azione; la feature set è vincolata da disponibilità `as-of`; la validation deve simulare il deployment; leakage e training-serving skew sono failure mode distinti; ranking, calibration e operating threshold vengono valutati separatamente; la complessità deve battere una baseline fuori campione; monitoring e retraining coprono dati, score, performance, operations e outcome. Il caso OrbitCom mostra perché model performance, policy execution e treatment effect non devono essere fusi nella stessa diagnosi.

## 10. Lunghezza

Dopo i Capitoli 0–10 revisionati il PDF è di **909 pagine**.

La revisione può quindi continuare a comprimere ripetizioni o ampliare esempi che aumentano la comprensione senza alcun rischio rispetto all'obiettivo minimo di 400+ pagine.

## 11. Elementi editoriali ancora mancanti

Prima della prima release stabile:

- frontespizio definitivo;
- copyright/licenza;
- autore e bio;
- introduzione al lettore / come usare il libro;
- indice automatico;
- eventuale glossario;
- bibliografia/indice delle fonti;
- eventuale indice analitico;
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

La revisione editoriale ha completato i **Capitoli 0–10**. Il lavoro successivo continua dal **Capitolo 11 — SQL, trasformazione del dato e data modeling per l'analisi**. Il compito editoriale sarà evitare un tutorial di sintassi e trasformare il capitolo nel ponte tra domanda analitica e dataset affidabile: grain, keys, join cardinality, temporal semantics, metric definitions, reusable transformations, tests e cost/performance devono diventare un contratto eseguibile tra significato e query.