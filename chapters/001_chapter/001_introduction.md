# Capitolo 1 — Tutto è cambiato. Il problema è rimasto lo stesso

> La tecnologia dell'analisi dati cambia continuamente. Il nucleo del lavoro analitico molto meno.

## Introduzione

Negli ultimi trent'anni il lavoro sui dati ha cambiato interfaccia molte volte. Il foglio elettronico è diventato uno strumento universale; i database relazionali hanno portato SQL nel lavoro quotidiano; la business intelligence ha reso dashboard e reporting accessibili a un pubblico molto più ampio; Python e R hanno abbassato il costo dell'automazione e dell'analisi statistica; il cloud ha separato sempre di più il calcolo dalla macchina locale. Ora l'AI generativa aggiunge un'altra discontinuità: il linguaggio naturale può diventare un'interfaccia verso dati, codice, modelli e strumenti.

A ogni ondata tecnologica riappare la stessa sensazione: che il mestiere del Data Analyst debba essere riscritto da zero.

Poi arriva una domanda reale. Il churn è aumentato. Una campagna sembra aver funzionato. Il margine si sta comprimendo. Il management vuole sapere se può aumentare i prezzi. E improvvisamente il problema torna ad avere una forma molto familiare.

Prima di scegliere uno strumento dobbiamo ancora capire quale decisione deve essere presa, che cosa significhi esattamente la domanda, quale parte della realtà i dati riescano a rappresentare e quale confronto renda il fenomeno interpretabile. Dobbiamo scegliere un metodo adeguato alla forza dell'affermazione che vogliamo sostenere, distinguere un pattern da una causa e decidere quanta incertezza sia accettabile per l'azione che abbiamo davanti.

Una query corretta non salva una domanda sbagliata. Un dashboard elegante non rende utile una metrica irrilevante. Un modello sofisticato non corregge automaticamente un bias nei dati. Una correlazione forte non dimostra una relazione causale. L'AI può rendere più economico produrre ciascuno di questi artefatti; non rende meno costoso credere a quello sbagliato.

Il Capitolo 0 ha fissato il principio con cui useremo l'AI: possiamo delegare molta esecuzione, non la responsabilità di capire ciò che consegniamo. Qui facciamo un passo precedente e più generale. Prima di domandarci come debba lavorare un analista AI-native, dobbiamo chiarire **che cosa significhi fare analisi**.

### Prima il problema, poi il metodo

L'idea non nasce con l'AI. Metodologie come CRISP-DM iniziano dalla **Business Understanding**, seguita dalla comprensione dei dati, dalla preparazione, dalla modellazione e dalla valutazione.[^ibm-crisp] L'ordine conta: il metodo non può essere scelto correttamente prima di avere capito il problema che dovrebbe risolvere e i dati con cui quel problema può essere osservato.

Gli strumenti più moderni, paradossalmente, rendono ancora più evidente questa dipendenza dal contesto. La documentazione Microsoft per Copilot in Power BI insiste sulla preparazione del modello semantico, sulla terminologia di business, sulle descrizioni e sugli schemi che riducono l'ambiguità.[^ms-copilot-semantic] Quando un utente non deve più conoscere il nome esatto di una tabella o scrivere una formula per interrogare il sistema, diventa ancora più importante che il sistema sappia che cosa l'organizzazione intende per revenue, cliente attivo, retention o margine.

La semplificazione dell'interfaccia non elimina la semantica. **La sposta più in profondità nell'infrastruttura e rende più costosi gli errori di significato che rimangono nascosti.**

### Il filo conduttore del libro

Non costruiremo quindi la figura del Data Analyst come una lista di software da imparare. Excel, SQL, Python, BI, notebook, warehouse, lakehouse, cloud e AI entreranno nel libro quando servono a risolvere un problema, produrre un'evidenza o rendere un processo più affidabile. Nessuno di questi strumenti, da solo, definisce il mestiere.

La domanda centrale sarà un'altra:

> **Come si passa da un problema reale a una conclusione affidabile e a una decisione migliore, scegliendo ogni volta dati, metodo e strumenti adeguati?**

Questo capitolo costruisce le fondamenta di quella risposta. Partiremo da ciò che la tecnologia ha davvero cambiato e da ciò che invece è rimasto stabile. Poi seguiremo il percorso che trasforma una richiesta di business in una domanda analitica, i dati in una rappresentazione del fenomeno, le metriche in definizioni condivise, i pattern in evidenza e l'evidenza in una decisione proporzionata all'incertezza.

Il punto di partenza non è un tool.

È il **ragionamento analitico**.

---

### Fonti

[^ms-copilot-semantic]: Microsoft Learn, *Use Copilot with Semantic Models in Power BI* e documentazione sulla preparazione dei dati per l'AI. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^ibm-crisp]: IBM, documentazione CRISP-DM / SPSS Modeler, *Understanding and preparing data*. https://www.ibm.com/docs/en/ws-and-kc?topic=modeler-understanding-preparing-data
