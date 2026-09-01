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

Dopo la revisione editoriale dei Capitoli 0–3:

- **20 capitoli**;
- **321 file Markdown**;
- **172.246 parole stimate**;
- **1.235.110 caratteri**;
- **118 URL esterni distinti**;
- **759 pagine PDF**;
- build Markdown, DOCX e PDF completata con successo.

Il numero di pagine non è una metrica editoriale da massimizzare. Può salire o scendere durante la revisione: alcuni passaggi vengono compressi perché ridondanti, altri vengono resi più chiari con esempi, tabelle, casi operativi e fonti reali più forti.

### Da completare prima della release tipografica

- rendering professionale delle formule matematiche attualmente scritte con notazione LaTeX;
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

- notazione matematica/LaTeX presente in 25 file, da gestire nella pipeline tipografica.

Per una release candidata:

```bash
python scripts/lint_book.py --strict
python scripts/build.py
```

dovrà terminare senza warning editoriali bloccanti.

## 4. Formule matematiche

Nel manoscritto sono presenti formule in blocchi del tipo:

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

Per un libro professionale la seconda o la terza opzione sono preferibili.

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
- Il Capitolo 3 usa ora il Government Data Quality Framework britannico come riferimento per fitness for purpose e dimensioni di qualità e include il Mars Climate Orbiter come caso reale documentato sulla semantica delle unità.

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
| 0 — Al timone | **Revisionato** | Ridisegnato come manifesto operativo: orchestrazione, accountability, verification by design, stop condition, deskilling, trust levels, caso multi-agent, manifesto finale. |
| 1 — Tutto è cambiato. Il problema è rimasto lo stesso | **Revisionato** | Eliminata la duplicazione con Ch. 0; fissata una sola catena analitica canonica; cinque tipi di domanda; caso vendite riscritto e marcato simulato/composito; rimandi ai capitoli specialistici. |
| 2 — Dal problema di business al problema analitico | **Revisionato** | Il capitolo converge ora su un unico deliverable: l'Analytical Brief. Decision specification, stakeholder map, metric roles, hypothesis register, scope, baseline, segmentation plan, data requirements, Value of Information e stop rule sono campi coerenti dello stesso piano. Caso Velora Home riscritto e marcato simulato/composito. |
| 3 — Capire il dato prima di analizzarlo | **Revisionato** | Riorganizzato come indagine di data readiness: record/grain → identità → tempo → qualità → missing/duplicati/outlier → unità → profiling → lineage → riconciliazione → contract/check automatici → verdetto PRONTO / CON CAVEAT / NON PRONTO. Caso end-to-end sostituito con ProntoVeloce per evitare sovrapposizione col Ch. 2; aggiunti Government Data Quality Framework e caso reale Mars Climate Orbiter. |
| 4–19 | **Da revisionare** | Procedere in ordine, controllando anche sovrapposizioni inter-capitolo. |

## 8. Sovrapposizioni concettuali da governare

Le ripetizioni principali devono diventare richiami intenzionali.

### Capitolo 0 / 14 / 19 — AI

Ruolo:

- **0 — Al timone:** mentalità, responsabilità, delega, supervisione;
- **14 — AI-assisted analytics:** uso operativo, eval, privacy, auditability, workflow;
- **19 — 2026–2035:** conseguenze sul ruolo, skill e carriera.

Regola: non rispiegare integralmente il manifesto del Capitolo 0 nei capitoli successivi.

### Capitolo 1 / 2 — domanda analitica

Ruolo:

- **1:** mentalità di base, cinque tipi di domanda e catena analitica canonica;
- **2:** trasformare formalmente la richiesta in un Analytical Brief operativo.

### Capitolo 2 / 3 — specifica e readiness

Ruolo:

- **2:** dichiarare quali dati, popolazioni, metriche e confronti servono per rispondere;
- **3:** verificare che i dati disponibili rappresentino davvero quelle proprietà e stabilire se siano pronti per l'analisi.

Catena editoriale:

**Analytical Brief → Data Readiness Review → Analisi**.

### Capitolo 2 / 15 — decisione

Ruolo:

- **2:** specificare decision owner, alternative, soglie note e profondità dell'analisi prima di eseguirla;
- **15:** trasformare evidenza e incertezza in raccomandazione, expected value e decisione.

### Capitolo 3 / 11 / 12 / 18 — qualità, semantica, governance

Ruolo:

- **3:** verificare fitness for purpose del dato dal punto di vista dell'analista;
- **11:** formalizzare grain, join, trasformazioni e metriche in SQL/modeling;
- **12:** capire l'architettura che produce e trasporta il dato;
- **18:** trasformare qualità, ownership, contract e osservabilità in capacità organizzativa scalabile.

## 9. Arco narrativo complessivo

La sequenza resta coerente:

**mentalità → domanda → dati → statistica → comportamento → tempo → causalità → esperimenti → modelli → SQL → architettura → strumenti → AI → decisione → comunicazione → casi completi → scala → futuro**.

Il Capitolo 0 funziona come contratto mentale iniziale e il Capitolo 19 chiude tornando al tema della responsabilità e delle competenze che restano preziose.

## 10. Lunghezza

Non usare il numero di capitoli come proxy della lunghezza.

La misura corrente viene dalla pipeline reale.

Dopo i primi quattro capitoli revisionati il PDF è di **759 pagine**. La revisione può quindi continuare liberamente a comprimere ripetizioni o ad ampliare esempi e casi che aumentano la comprensione senza alcun rischio rispetto all'obiettivo minimo di 400+ pagine.

L'obiettivo non è preservare un numero massimo di pagine. È massimizzare **densità di valore per pagina**.

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

La revisione editoriale ha completato i **Capitoli 0, 1, 2 e 3**. Il lavoro successivo continua dal Capitolo 4, con l'obiettivo di trasformare statistica descrittiva ed EDA da catalogo di tecniche a processo disciplinato per descrivere ciò che il dato mostra senza anticipare spiegazioni o causalità.