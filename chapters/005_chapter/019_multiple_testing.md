## 5.18 Multiple testing: un segnale cambia significato quando sappiamo quante volte lo abbiamo cercato

L'analisi moderna rende quasi gratuito provare molte metriche, segmenti, finestre temporali, filtri e specificazioni. Questa abbondanza è preziosa in esplorazione. Diventa pericolosa quando il risultato più interessante trovato dopo decine di tentativi viene raccontato come se fosse l'unica ipotesi valutata dall'inizio.

La molteplicità non è quindi soltanto un problema di formule. È un problema di **storia del processo analitico**: quante opportunità avevamo di trovare qualcosa che sembrasse raro?

## Il segmento perfetto trovato dopo oltre cento tentativi

Una piattaforma subscription introduce una nuova offerta annuale. Nel totale il controllo converte al 6,21% e l'offerta al 6,28%: un movimento poco interessante.

Il team growth inizia allora a esplorare 8 paesi, 5 fasce d'età, 4 canali, 4 piattaforme, nuovi contro returning, 6 fasce di spesa storica e varie combinazioni. Dopo oltre cento confronti emerge un segmento molto promettente:

> **iOS, 25–34 anni, paid social, Spagna: +11,8% conversione relativa, `p < 0,05`.**

Il pattern potrebbe essere reale. Ma il p-value di quel confronto non contiene un promemoria automatico che dica “prima di arrivare qui avevamo avuto più di cento occasioni per osservare un risultato estremo”. Questa informazione fa parte dell'evidenza e deve essere aggiunta dall'analista.

Per vedere l'intuizione, immaginiamo 20 test indipendenti, tutti con null vero e `α = 0,05`. La probabilità di ottenere **almeno un falso positivo** è:

`1 - (1 - 0,05)^20 ≈ 64%`.

Nelle analisi reali i test possono essere correlati, quindi il 64% non è una formula universale da applicare meccanicamente. Il principio però resta: **più opportunità abbiamo di vedere un evento raro, meno sorprendente diventa osservarne almeno uno**.

## Esplorare e confermare sono due lavori diversi

Il Capitolo 4 ha difeso l'EDA proprio come spazio per generare ipotesi. La stessa distinzione deve sopravvivere quando iniziamo a calcolare p-value.

Se scopriamo a posteriori che un segmento reagisce molto bene, il linguaggio corretto è:

> **Segnale esplorativo: il segmento X mostra un effetto maggiore; da verificare su nuovi dati o in un'analisi pianificata.**

Non:

> “Abbiamo dimostrato che la variante funziona per X.”

La scoperta non perde valore perché viene chiamata esplorativa. Guadagna una procedura corretta per diventare, eventualmente, confermativa.

## La molteplicità vive anche nelle scelte che non chiamiamo “test”

Possiamo creare molte opportunità di ottenere un risultato favorevole cambiando a posteriori la metrica primaria, la finestra temporale, il criterio di esclusione, la trasformazione, il modello, il subset della popolazione o il momento in cui fermiamo l'analisi.

Ogni singola scelta può essere plausibile. Il problema nasce quando selezioniamo **dopo aver visto i dati** la combinazione che produce la storia più forte e poi dimentichiamo tutte le altre possibilità esplorate.

Per questo l'ASA include trasparenza e reporting completo tra i principi centrali per interpretare i p-value.[^asa-multiple] La trasparenza non è una formalità editoriale: permette al lettore di capire quanto il risultato sia stato cercato.

## Tre modi diversi di gestire il problema

La prima difesa è **pre-specificare ciò che conta**: metrica primaria, confronti principali, segmenti confermativi, guardrail e criterio di analisi. Non impedisce l'esplorazione successiva; impedisce di confondere ciò che era previsto con ciò che è stato scoperto.

Quando esiste una vera famiglia di confronti confermativi, possono servire procedure di correzione. Bonferroni controlla in modo semplice e spesso conservativo il family-wise error rate; Holm offre un controllo dello stesso tipo con maggiore flessibilità; Benjamini–Hochberg controlla il False Discovery Rate ed è utile quando l'obiettivo è gestire molte potenziali scoperte. La tecnica appropriata dipende dalla decisione: proteggere un singolo claim ad alto rischio non è lo stesso problema che fare screening di centinaia di segnali da approfondire.

Infine, un pattern scoperto esplorativamente può essere **confermato su informazione nuova**: un periodo futuro, un holdout non usato nella scoperta, una popolazione indipendente o un nuovo esperimento. È spesso il modo più intuitivo per separare generazione e conferma.

Consideriamo un dashboard con 60 metriche. La primaria non cambia in modo materialmente rilevante, mentre tre secondarie mostrano `p < 0,05`. Se mostriamo soltanto quelle tre verdi, trasformiamo un insieme di evidenza sostanzialmente misto in una storia selettivamente ottimista.

La conclusione corretta non è “le tre metriche sono sicuramente falsi positivi”. È:

> **Questi segnali sono emersi dentro una famiglia ampia di confronti; devono essere interpretati tenendo conto della molteplicità e, se importanti, confermati.**

Per questo ogni scoperta dovrebbe portarsi dietro una piccola traccia del proprio processo:

```text
Ipotesi pre-specificata o esplorativa?
Numero/famiglia dei confronti:
Correzione applicata, se necessaria:
Scelte analitiche effettuate dopo aver visto i dati:
Nuovi dati disponibili per conferma:
```

> **La trasparenza su come abbiamo cercato il segnale è parte dell'evidenza sul segnale stesso.**

---

### Fonte

[^asa-multiple]: American Statistical Association, *Statement on Statistical Significance and P-Values*. https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
