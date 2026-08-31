# Editorial audit — data.analyst.today

Ultimo aggiornamento: 31 agosto 2026.

Questo documento registra lo stato della revisione del manoscritto dopo il completamento del corpo principale, Capitoli 0–19.

## 1. Struttura del repository

### Corretto

- Il libro parte da `chapters/000_chapter/` con **Capitolo 0 — Al timone**.
- I capitoli proseguono in modo continuo fino a `019_chapter`.
- I prefissi numerici duplicati presenti in diversi capitoli sono stati normalizzati.
- `scripts/build.py` usa ora un ordinamento deterministico `(prefisso numerico, nome file)` come ulteriore protezione.
- Gli artefatti generati `.md`, `.docx` e `.pdf` dentro `build/` sono ignorati da Git.

### Regola

Per ogni capitolo:

- `001_*.md` contiene il titolo del capitolo;
- `002_*.md` corrisponde alla sezione `X.1`;
- `003_*.md` corrisponde alla sezione `X.2`;
- e così via.

I prefissi devono essere univoci e contigui.

## 2. Build Markdown → DOCX/PDF

### Corretto

Il builder ora:

- ordina le sorgenti in modo deterministico;
- abilita le tabelle Markdown;
- evita la duplicazione dei blockquote;
- conserva grassetto, corsivo e codice inline nei principali output;
- gestisce le tabelle anche in DOCX e PDF;
- non trasforma ogni separatore orizzontale in un page break;
- protegge la build da sezioni legacy scritte accidentalmente come H1;
- crea page break sui veri titoli di capitolo.

### Da completare prima della release tipografica

- rendering professionale delle formule matematiche attualmente scritte con notazione LaTeX;
- indice/TOC con page number nella versione impaginata;
- verifica della resa di tabelle molto larghe;
- controllo di widows/orphans, code block lunghi e page break;
- eventuale stile definitivo per note, fonti e callout.

## 3. Lint automatico

È stato aggiunto:

```bash
python scripts/lint_book.py
```

Il controllo verifica:

- continuità dei capitoli;
- prefissi duplicati o mancanti;
- corrispondenza tra filename e numero della sezione;
- H1 usati accidentalmente per sezioni interne;
- file vuoti;
- `TODO`, `FIXME`, `TBD`;
- presenza di `utm_source=chatgpt.com`;
- numero di URL esterni;
- presenza di formule/LaTeX;
- ortografia ASCII come `e'`, `piu'`, `puo'`;
- conteggio di parole e stima indicativa delle pagine.

Per una release:

```bash
python scripts/lint_book.py --strict
```

dovrebbe terminare senza errori e, idealmente, senza warning editoriali.

## 4. Heading Markdown

### Problema rilevato

Le sezioni dei capitoli più recenti, in particolare **Capitolo 0 e Capitoli 13–19**, sono state in parte create con heading H1 del tipo:

```markdown
# 14.8 AI e causalità
```

La convenzione corretta è:

```markdown
## 14.8 AI e causalità
```

Il builder oggi riconosce una heading numerata `X.Y` e la tratta correttamente come H2, quindi la build non crea più page break errati.

### Da fare

Normalizzare anche le sorgenti Markdown, non soltanto la resa in build. È un intervento meccanico, da fare prima della release stabile.

## 5. Formule matematiche

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

## 6. Qualità linguistica

### Problema rilevato

Alcune sezioni più vecchie contengono grafie ASCII:

- `e'` invece di `è`;
- `piu'` invece di `più`;
- `puo'` invece di `può`;
- forme analoghe.

La sorgente è UTF-8, quindi non esiste una ragione tecnica per mantenerle.

### Da fare

Eseguire una normalizzazione linguistica controllata, evitando sostituzioni cieche dentro:

- SQL;
- Python;
- URL;
- nomi propri;
- stringhe di codice.

Dopo la normalizzazione, rileggere almeno le frasi modificate.

## 7. Casi reali e casi simulati

### Corretto

Il Capitolo 0 e il README dichiarano ora esplicitamente la convenzione:

- **caso reale documentato**: supportato da una fonte pubblica attendibile;
- **caso simulato/composito**: costruito a fini didattici.

I nomi aziendali fittizi devono essere interpretati come simulati/compositi.

### Da verificare

Durante la revisione finale, ogni caso reale importante deve avere:

- organizzazione identificabile;
- fonte leggibile;
- claim proporzionato a ciò che la fonte documenta;
- nessuna confusione tra correlazione, causalità e risultato commerciale dichiarato.

## 8. Fonti e link

### Corretto

La ricerca nel repository non rileva link contenenti `chatgpt.com` o `utm_source=chatgpt.com` nel manoscritto.

### Da fare

Prima della release:

- controllare link rotti o redirect permanenti;
- preferire documentazione ufficiale e fonti primarie;
- uniformare il modo in cui vengono presentate le sezioni `Fonti`;
- valutare una bibliografia generale o un indice delle fonti oltre alle fonti locali per capitolo;
- registrare data di accesso solo dove editorialmente utile.

## 9. Sovrapposizioni concettuali

Le ripetizioni principali non sono errori in sé, ma devono essere trasformate in richiami intenzionali.

### Capitolo 0 / 14 / 19 — AI

Ruolo consigliato:

- **0 — Al timone:** mentalità, responsabilità, delega, supervisione;
- **14 — AI-assisted analytics:** uso operativo, eval, privacy, auditability, workflow;
- **19 — 2026–2035:** conseguenze sul ruolo, skill e carriera.

Regola di revisione: evitare di rispiegare integralmente in 14 o 19 il manifesto del Capitolo 0; richiamarlo e aggiungere un livello nuovo.

### Capitolo 2 / 15 — decisione

Ruolo consigliato:

- **2:** tradurre la richiesta di business in problema analitico;
- **15:** trasformare evidenza e incertezza in raccomandazione e decisione.

### Capitolo 3 / 11 / 12 / 18 — qualità, semantica, governance

Ruolo consigliato:

- **3:** capire il dato prima di analizzarlo;
- **11:** formalizzare grain, join, trasformazioni e metriche in SQL/modeling;
- **12:** capire l'architettura che produce e trasporta il dato;
- **18:** rendere il sistema analitico affidabile e scalabile nell'organizzazione.

## 10. Arco narrativo complessivo

La sequenza attuale è coerente:

**mentalità → domanda → dati → statistica → comportamento → tempo → causalità → esperimenti → modelli → SQL → architettura → strumenti → AI → decisione → comunicazione → casi completi → scala → futuro**.

Il Capitolo 0 funziona come contratto mentale iniziale e il Capitolo 19 chiude tornando allo stesso principio di responsabilità.

## 11. Lunghezza

Non usare il numero di capitoli come proxy della lunghezza.

La misura da usare è il conteggio reale prodotto da:

```bash
python scripts/lint_book.py
```

La stima `parole / 250–300` è utile soltanto come ordine di grandezza. Il numero finale di pagine dipenderà molto da:

- formule;
- tabelle;
- codice;
- spaziatura;
- font;
- dimensione pagina;
- apertura dei capitoli;
- figure future.

La soglia di **400+ pagine** deve quindi essere verificata sulla build impaginata, non dichiarata sulla base del solo volume Markdown.

## 12. Elementi editoriali ancora mancanti

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

## 13. Release gate

Una release candidata dovrebbe passare questo percorso:

```bash
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

Il **contenuto principale del libro esiste ed è strutturalmente completo**.

Non siamo più nella fase “scrivere i capitoli mancanti”. Siamo nella fase in cui un manoscritto lungo deve diventare un libro: ridurre ridondanze, uniformare la lingua, verificare le fonti, rendere robusta la pipeline di build e curare la tipografia.
