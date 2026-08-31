# Capitolo 1 — Tutto è cambiato. Il problema è rimasto lo stesso

> La tecnologia dell'analisi dati cambia continuamente. Il nucleo del lavoro analitico molto meno.

## Introduzione

Negli ultimi trent'anni il lavoro sui dati ha cambiato interfaccia molte volte. Il foglio elettronico è diventato uno strumento universale, i database relazionali sono entrati nel lavoro quotidiano, la business intelligence ha portato dashboard e reporting self-service, Python e R hanno reso più accessibili automazione e analisi statistiche, il cloud ha separato sempre di più calcolo e macchina locale e l'AI generativa ha trasformato il linguaggio naturale in una nuova interfaccia verso dati, codice e modelli.

A ogni ondata tecnologica sembra che il mestiere del Data Analyst debba essere riscritto da zero.

Eppure, quando un'organizzazione pone una domanda reale — “perché il churn è aumentato?”, “questa campagna ha funzionato?”, “possiamo alzare i prezzi?”, “dove stiamo perdendo margine?” — la difficoltà centrale rimane sorprendentemente stabile.

Prima di scegliere uno strumento bisogna capire:

- quale decisione deve essere presa;
- che cosa significa esattamente la domanda;
- quali dati rappresentano il fenomeno;
- quali definizioni e confronti sono legittimi;
- quale metodo è adeguato;
- quanto è forte l'evidenza;
- quali conclusioni possiamo sostenere senza andare oltre i dati.

Una query corretta non salva una domanda sbagliata. Un dashboard elegante non rende utile una metrica irrilevante. Un modello sofisticato non corregge automaticamente un bias nei dati. Una correlazione forte non dimostra una relazione causale.

Il Capitolo 0 ha fissato il principio con cui useremo l'AI: possiamo delegare molta esecuzione, non la responsabilità di capire ciò che consegniamo. Qui facciamo un passo precedente e più generale: **che cosa significa, esattamente, fare analisi?**

### Prima il problema, poi il metodo

L'idea non nasce con l'AI. Metodologie come CRISP-DM iniziano dalla **Business Understanding**, seguita dalla comprensione dei dati, dalla preparazione, dalla modellazione e dalla valutazione.[^ibm-crisp]

Il principio è semplice: il metodo non può essere scelto correttamente prima di avere capito il problema che dovrebbe risolvere.

Anche gli strumenti più moderni stanno rendendo esplicita la stessa dipendenza dal contesto. La documentazione Microsoft per Copilot in Power BI, per esempio, sottolinea che la qualità delle risposte dipende dalla preparazione del modello semantico, dalla terminologia di business e dalle definizioni disponibili.[^ms-copilot-semantic]

È un segnale importante: **più diventa facile interrogare i dati, più deve essere rigoroso il significato che assegniamo loro.**

### Il filo conduttore del libro

Non costruiremo quindi la figura del Data Analyst come una lista di software da imparare.

Excel, SQL, Python, BI, notebook, warehouse, lakehouse, cloud e AI saranno importanti, ma verranno trattati per quello che sono: strumenti all'interno di un processo analitico e decisionale.

La domanda centrale del libro non sarà:

> “Quale tecnologia devo imparare?”

ma:

> **“Come si passa da un problema reale a una conclusione affidabile e a una decisione migliore, scegliendo ogni volta dati, metodo e strumenti adeguati?”**

Questo capitolo costruisce le fondamenta di quella risposta: problema, rappresentazione dei dati, metriche, evidenza, causalità, incertezza e decisione.

Il punto di partenza non è un tool.

È il **ragionamento analitico**.

---

### Fonti

[^ms-copilot-semantic]: Microsoft Learn, *Use Copilot with Semantic Models in Power BI* e documentazione sulla preparazione dei dati per l'AI. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^ibm-crisp]: IBM, documentazione CRISP-DM / SPSS Modeler, *Understanding and preparing data*. https://www.ibm.com/docs/en/ws-and-kc?topic=modeler-understanding-preparing-data
