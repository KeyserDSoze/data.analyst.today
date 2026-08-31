## 1.1 Cosa è cambiato davvero

Per capire il ruolo del Data Analyst nell'era dell'AI bisogna separare due livelli:

- **il lavoro analitico** — definire problemi, scegliere evidenze, interpretare risultati, supportare decisioni;
- **il modo in cui quel lavoro viene eseguito** — strumenti, interfacce, linguaggi, automazioni e infrastruttura.

Il primo cambia lentamente.

Il secondo cambia molto velocemente.

Per anni una parte significativa del vantaggio tecnico di un analista è derivata dalla capacità di eseguire attività che richiedevano conoscenze operative specifiche: SQL, formule, DAX, trasformazioni, scripting, dashboard, configurazioni di strumenti.

Queste competenze restano importanti. Ma cambia il loro ruolo, perché il costo di produrre una prima versione di molti artefatti tecnici si sta abbassando.

### 1. Dalla sintassi all'intento

Per molto tempo l'interazione con i sistemi analitici è stata dominata dalla sintassi.

Per interrogare un database serviva SQL. Per automatizzare un'analisi serviva Python o R. Per costruire determinate metriche in Power BI serviva DAX. Per trasformare un foglio elettronico bisognava conoscere formule, pivot, Power Query o macro.

L'AI generativa aggiunge un'altra interfaccia: **l'intento espresso in linguaggio naturale**.

Un analista può chiedere:

> “Calcola il fatturato mensile per categoria, confrontalo con lo stesso mese dell'anno precedente e segnala le categorie con una diminuzione superiore al 15%.”

Un sistema può trasformare la richiesta in SQL, Python, DAX o una sequenza di operazioni.

Questo sposta parte del lavoro da:

> “Come si scrive?”

verso:

> “Che cosa voglio ottenere, e come verifico che l'implementazione corrisponda davvero all'intento?”

Il cambiamento è reale. Ma non elimina l'ambiguità.

Che cosa significa “fatturato”? Lordo o netto? Con resi? Quale data? Quale valuta? Il confronto è valido se il perimetro aziendale è cambiato?

L'AI riduce il costo della traduzione tra intento e codice. Non definisce automaticamente l'intento corretto.

### 2. Iterare costa meno

Se una query, un grafico o uno script richiedono meno tempo, possiamo esplorare più ipotesi.

Questo è uno dei cambiamenti più utili per l'analista.

Un'ipotesi secondaria che in passato avremmo ignorato per mancanza di tempo può essere controllata. Possiamo confrontare definizioni alternative, generare rapidamente sanity check, prototipare più visualizzazioni o testare una seconda decomposizione del problema.

Il vantaggio non è soltanto “fare prima”.

È poter costruire un processo più iterativo.

Ma l'abbondanza di output crea anche un nuovo vincolo: **la capacità di produrre alternative cresce più velocemente della capacità di valutarle tutte con la stessa profondità**.

Il Capitolo 0 ha affrontato questo problema dal punto di vista della supervisione. Qui ci basta registrare il cambiamento economico: quando l'esecuzione costa meno, diventano relativamente più preziosi priorità, semantica e verifica.

### 3. I confini tra ruoli diventano più permeabili

In molte organizzazioni il lavoro era tradizionalmente suddiviso in passaggi molto netti:

business request → analyst → data engineer → BI developer → report.

Le specializzazioni non scompaiono, soprattutto nei sistemi complessi. Ma diventa più economico attraversarne i confini.

Un analista può generare codice più facilmente. Un business user può interrogare un modello semantico in linguaggio naturale. Un data engineer può produrre documentazione rapidamente. Un data scientist può prototipare una visualizzazione senza passare subito da un altro team.

Questo aumenta il valore di una competenza trasversale: **capire abbastanza bene l'intero percorso da sapere quando procedere, quando verificare e quando coinvolgere uno specialista.**

### 4. La semantica diventa infrastruttura

Uno dei cambiamenti meno visibili ma più importanti è che il significato dei dati viene formalizzato sempre di più dentro i sistemi analitici.

Metriche, relazioni, descrizioni, sinonimi e logiche di business possono vivere in semantic layer e modelli condivisi invece che soltanto nella testa degli analisti o in documenti separati.

L'AI rende questa formalizzazione ancora più importante.

Microsoft, nella documentazione dedicata alla preparazione dei semantic model di Power BI per Copilot, raccomanda schemi mirati, terminologia aziendale, descrizioni e istruzioni che riducano l'ambiguità. La piattaforma prevede anche meccanismi per configurare risposte validate in aree specifiche.[^ms-ai-schema][^ms-ai-faq]

È un caso reale documentato di una dinamica generale:

> **quando l'interfaccia diventa più semplice, il modello semantico sottostante deve diventare più rigoroso.**

Se l'utente non deve più conoscere il nome esatto della tabella o della misura, il sistema deve conoscere con maggiore precisione che cosa significano “revenue”, “cliente attivo” o “retention”.

### Che cosa cambia, quindi, per l'analista?

La competenza tecnica non scompare. Cambia la sua funzione.

Studiamo SQL non soltanto per digitare una `JOIN`, ma per capire grain, cardinalità, aggregazioni e possibili duplicazioni.

Studiamo statistica non per calcolare ogni formula a mano, ma per sapere quale conclusione è giustificata dall'evidenza.

Studiamo visualizzazione non per produrre più grafici, ma per riconoscere quali rappresentazioni chiariscono o distorcono un fenomeno.

Studiamo architettura non perché ogni analista debba amministrare un warehouse, ma perché raccolta, trasformazione e modellazione determinano ciò che possiamo osservare.

In breve:

> **si riduce il premio per la pura esecuzione e aumenta il premio per il giudizio informato sull'esecuzione.**

La sezione successiva affronta l'altra metà della tesi: ciò che, nonostante tutti questi cambiamenti, è rimasto sorprendentemente stabile.

---

### Fonti

[^ms-ai-schema]: Microsoft Learn, *Prepare your data for AI - AI data schemas*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-data-schema
[^ms-ai-faq]: Microsoft Learn, *Frequently Asked Questions about Preparing Data for AI - Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq
