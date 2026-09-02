## 19.9 Deskilling: quali competenze devi mantenere per poter delegare

Uno dei rischi professionali più interessanti dell'AI non è la sostituzione immediata.

È il **deskilling graduale**.

Quando un sistema esegue bene una parte crescente del lavoro, possiamo perdere lentamente la capacità di:

- svolgerlo;
- valutarlo;
- diagnosticare quando cambia;
- intervenire quando l'automazione esce dai confini attesi.

Non ogni perdita di skill è negativa.

Nessuno ha bisogno di mantenere la capacità di consultare a memoria ogni funzione di un database.

Il problema nasce quando esternalizziamo **la competenza che ci serviva per controllare il sistema che stiamo delegando**.

## Tre categorie di competenze

Per evitare nostalgia eccessiva, distinguiamo.

### Categoria A — Must internalize

Modelli mentali che devono restare abbastanza forti da guidare verifica e decisione.

Per un Data Analyst:

- grain;
- cardinality;
- denominator;
- population;
- time semantics;
- distribution/uncertainty;
- causal vs predictive claim;
- leakage;
- randomization;
- baseline;
- cost asymmetry;
- unit economics;
- decision threshold.

Possiamo usare AI su questi temi.

Ma non possiamo permetterci di non capire quando vengono violati.

### Categoria B — Can delegate, must inspect

Attività che possono essere eseguite spesso dall'AI, purché resti la capacità di review.

Esempi:

- SQL complesso;
- feature pipeline;
- visualization code;
- experiment analysis;
- forecast code;
- documentation;
- test generation.

Non serve ricordare ogni dettaglio di sintassi.

Serve capire abbastanza da leggere struttura, failure mode e output.

### Categoria C — Safe to externalize

Conoscenza a basso responsibility moat che può essere recuperata on demand.

Esempi:

- flag di una CLI;
- nome preciso di una funzione;
- boilerplate di configurazione;
- sintassi rara;
- conversione meccanica tra formati.

Spendere molta memoria professionale qui può avere ritorno decrescente.

## Verification reserve

Introduciamo un concetto personale:

**verification reserve** = capacità residua di controllare un processo anche quando l'AI fa quasi tutta l'esecuzione.

Se un agente SQL lavora bene da un anno, la verification reserve include ancora saper chiedere:

- questa join può moltiplicare il grain?
- il filtro è pre o post aggregation?
- il denominator è coerente?
- la data è `as-of`?
- stiamo usando una snapshot o un event log?

Se il reserve scende a zero, la delega diventa dipendenza.

## Caso simulato/composito: l'agente SQL che diventa troppo affidabile

Un team usa un agente SQL da 18 mesi.

La qualità media è elevata.

Gradualmente gli analyst smettono di leggere la query e controllano soltanto il risultato finale.

Poi `customer_status` cambia modello:

prima:

> snapshot giornaliero;

dopo:

> event history.

L'agente continua a generare SQL sintatticamente corretto ma tratta la tabella come se ogni riga fosse lo stato corrente.

I customer count risultano duplicati.

L'errore resta invisibile per tre settimane.

Non perché il modello AI sia improvvisamente peggiorato.

Perché il sistema umano ha perso la routine di controllo che avrebbe riconosciuto il cambio di grain temporale.

## Un segnale dalla ricerca sul knowledge work

Uno studio Microsoft Research presentato a CHI 2025 ha intervistato 319 knowledge worker, raccogliendo 936 esempi di utilizzo della GenAI nel lavoro.

Lo studio rileva, nel campione auto-riferito, che maggiore fiducia nella GenAI è associata a minore enactment/effort di critical thinking, mentre l'uso dell'AI sposta parte del lavoro critico verso:

- verification;
- response integration;
- task stewardship.

Fonte: https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/

Va interpretato correttamente.

È uno studio survey/self-report e non dimostra causalmente che l'AI provochi deskilling.

Ma suggerisce un failure mode coerente con il nostro problema:

> quando la fiducia nell'automazione cresce, dobbiamo progettare deliberatamente il mantenimento del critical engagement.

## La palestra analitica

Non dobbiamo conservare artificialmente lavoro manuale inefficiente.

Dobbiamo creare **deliberate practice** sui modelli mentali che servono al controllo.

Una palestra analitica può includere:

### Bug hunt

Revisionare query o pipeline con failure nascosto.

### Semantic reconstruction

Partire da una definizione business e costruire grain, population, denominator e time rule.

### Causal critique

Prendere una recommendation e cercare confounding, selection, post-treatment e alternative explanation.

### Experiment review

Diagnosticare SRM, contamination, peeking, guardrail e metric contract.

### Forecast stress test

Cercare bias per horizon, regime change e cost asymmetry.

### AI red-team

Chiedere all'AI una soluzione e poi provare deliberatamente a falsificarla.

### Explain without tool

Spiegare a voce:

- cosa sta misurando;
- quale assunzione conta;
- quale risultato cambierebbe la decisione.

Se non sappiamo farlo, la comprensione può essere troppo legata all'interfaccia.

## Deliberate friction

Per imparare, a volte è utile introdurre **frizione volontaria**.

Non sempre.

Non in produzione se crea rischio inutile.

Ma in training possiamo:

- scrivere una query prima di chiedere la soluzione AI;
- stimare l'ordine di grandezza prima di vedere il risultato;
- definire il test plan prima di generare codice;
- formulare tre failure mode prima di chiedere una review all'agente;
- fare una prediction del risultato prima di eseguire l'analisi.

Questa frizione costringe il cervello a costruire un modello invece di limitarsi a riconoscere un output plausibile.

## AI come coach, non soltanto esecutore

Possiamo usare la stessa tecnologia anche per contrastare deskilling.

Chiedere all'AI di:

- generare casi con bug;
- criticare una nostra causal claim;
- fare domande socratiche;
- simulare uno stakeholder ostile;
- costruire edge case;
- confrontare due design;
- nascondere la soluzione finché non abbiamo formulato un'ipotesi.

Quindi AI non implica automaticamente meno apprendimento.

Dipende dal **learning design**.

## Una manutenzione delle competenze

Una possibile routine personale:

### Ogni settimana

Una review profonda di un output AI reale.

### Ogni mese

Un esercizio “senza scorciatoia” su una competenza fondamentale.

### Ogni trimestre

Un caso end-to-end fuori dalla propria comfort zone.

### Dopo ogni incidente

Aggiornare:

- failure-mode library;
- checklist;
- eval;
- cosa non avevamo capito.

### Ogni anno

Chiedersi quali skill sono diventate:

- più delegabili;
- più importanti per verification;
- obsolete;
- nuove responsabilità da costruire.

Non è necessario seguire queste cadenze alla lettera.

Il principio è importante: **le competenze critiche richiedono manutenzione, come un sistema operativo**.

## Il nuovo obiettivo dell'apprendimento

Nel mondo pre-AI potevamo confondere competenza con capacità di produrre.

Nel mondo AI dobbiamo aggiungere:

- capacità di specificare;
- capacità di verificare;
- capacità di falsificare;
- capacità di intervenire;
- capacità di spiegare il sistema senza dipenderne completamente.

> **Usare meno una competenza non significa poter smettere di possederla. Se quella competenza protegge il confine tra output plausibile ed evidenza affidabile, deve restare viva.**
