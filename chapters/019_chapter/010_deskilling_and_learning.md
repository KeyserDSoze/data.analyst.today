# 19.9 Deskilling, apprendimento e manutenzione delle competenze

Uno dei rischi più sottovalutati dell'AI è il **deskilling**.

Quando uno strumento esegue correttamente una parte crescente del lavoro, una persona può perdere gradualmente la capacità di svolgere o valutare quel lavoro senza assistenza.

Questo non è necessariamente un problema.

Nessuno considera grave non saper più calcolare manualmente una regressione lineare con carta e penna.

Il problema nasce quando perdiamo proprio le competenze necessarie a riconoscere che il sistema sta sbagliando.

## Quali competenze devono restare vive

Per un Data Analyst, alcune competenze non devono essere necessariamente esercitate ogni giorno, ma devono rimanere abbastanza solide da permettere controllo e giudizio:

- grain e cardinalità;
- logica dei join;
- denominatori;
- distribuzioni e variabilità;
- probabilità e incertezza;
- causalità;
- leakage;
- validazione temporale;
- metriche di performance;
- unit economics;
- semantica di business.

Un analista può chiedere all'AI di scrivere una query complessa.

Ma deve riuscire a guardarla e chiedersi:

> “Questa join può duplicare le righe?”

Può chiedere all'AI di costruire un modello.

Ma deve sapere chiedere:

> “Il target era disponibile davvero al momento della previsione?”

Può chiedere all'AI un A/B test.

Ma deve sapere chiedere:

> “Qual era l'unità di randomizzazione? C'è contaminazione?”

## Imparare nel 2030

Se l'AI è sempre disponibile, l'apprendimento non può più essere basato principalmente sulla memorizzazione di sintassi.

Una strategia più robusta potrebbe avere quattro livelli.

### 1. Costruire modelli mentali

Capire perché un metodo funziona, quali assunzioni richiede e come fallisce.

### 2. Eseguire abbastanza manualmente da capire

Non serve fare tutto senza AI, ma alcune volte è utile costruire da zero una query, un modello o un test per comprenderne la struttura.

### 3. Usare l'AI intensamente

Delegare davvero l'esecuzione e imparare a orchestrare sistemi più potenti.

### 4. Fare review deliberata

Confrontare output, cercare errori, creare controesempi, verificare assunzioni.

## Il principio della palestra analitica

Un atleta non si allena soltanto facendo la gara.

Allo stesso modo, un analista non dovrebbe allenare le proprie capacità soltanto producendo output di lavoro.

Serve una **palestra analitica**.

Per esempio:

- una volta al mese diagnosticare una query con bug nascosti;
- criticare un esperimento mal progettato;
- ricostruire una metrica a partire dalla definizione business;
- fare un pre-mortem di una decisione;
- confrontare una risposta AI con un'analisi indipendente;
- spiegare un modello senza usare gergo tecnico.

## Caso realistico: l'agente che diventa troppo bravo

Un team usa un agente SQL da 18 mesi.

La qualità media è molto alta.

Gradualmente gli analisti smettono di leggere le query complete e controllano solo l'output finale.

Poi cambia il modello dati: `customer_status` passa da snapshot giornaliero a tabella event-based.

L'agente continua a generare query sintatticamente corrette, ma interpreta il campo come se fosse ancora uno snapshot.

Il problema non viene rilevato per tre settimane.

Non perché l'AI sia improvvisamente peggiorata.

Perché il team ha smesso di esercitare la competenza necessaria a riconoscere il problema.

## Il nuovo obiettivo della formazione

L'obiettivo non è mantenere artificialmente lavori manuali.

È mantenere la capacità di:

- comprendere;
- verificare;
- criticare;
- intervenire quando il sistema esce dai confini attesi.

Il World Economic Forum, nel Future of Jobs Report 2025, colloca AI e big data tra le skill in più rapida crescita ma mantiene analytical thinking, systems thinking, curiosità e lifelong learning tra le competenze centrali verso il 2030. Il messaggio è coerente con questa idea: la capacità tecnica e quella cognitiva devono crescere insieme.

> **Usare meno una competenza non significa poter smettere di possederla. Se serve per controllare il sistema, deve restare viva.**

### Fonti

- World Economic Forum, *Future of Jobs Report 2025 — Skills outlook*: https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/3-skills-outlook/
