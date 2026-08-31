## 1.7 I tre livelli del lavoro analitico

Per orientarci nel resto del libro useremo un modello semplice a tre livelli.

Non sono tre ruoli separati e non sono una classificazione universale della professione. Sono tre tipi di lavoro tra i quali un analista si muove continuamente.

### Livello 1 — Execution

È l'esecuzione tecnica necessaria a produrre un artefatto o un calcolo.

Comprende, per esempio:

- scrivere query;
- creare formule;
- pulire e trasformare dati;
- costruire grafici;
- preparare script;
- esportare report;
- documentare trasformazioni.

Queste competenze restano importanti perché permettono autonomia e verifica.

Ma sono anche le attività sulle quali l'automazione esercita la pressione maggiore.

Il valore di conoscere SQL, Python o un foglio elettronico non sta soltanto nella velocità con cui ricordiamo la sintassi. Sta nella capacità di capire l'implementazione, modificarla e riconoscere quando è sbagliata.

### Livello 2 — Analysis

È il livello in cui i dati vengono trasformati in evidenza.

Comprende:

- scegliere metriche e popolazioni;
- decidere il grain;
- costruire confronti;
- segmentare;
- esplorare distribuzioni;
- distinguere trend e rumore;
- formulare e testare ipotesi;
- valutare bias e confondenti;
- interpretare risultati statistici;
- quantificare l'incertezza.

Qui non basta che un calcolo sia corretto.

Deve essere anche **adatto alla domanda**.

### Livello 3 — Decision Intelligence

Con questo termine indicheremo il lavoro che collega l'evidenza a una scelta.

Le domande diventano:

- quale problema vale la pena affrontare?
- quanto vale economicamente risolverlo?
- quale evidenza sarebbe sufficiente per cambiare decisione?
- quali alternative abbiamo?
- quali rischi comportano?
- quale azione è reversibile?
- come misureremo l'effetto dopo l'intervento?

A questo livello statistica e dati incontrano vincoli operativi, economia e strategia.

### Un esempio: churn dal 4% al 6%

**Execution.** Calcoliamo correttamente il churn mensile e costruiamo il grafico.

**Analysis.** Scopriamo che l'aumento è concentrato nei clienti acquisiti da un canale specifico e soprattutto nei primi 60 giorni.

**Decision Intelligence.** Stimiamo la dimensione economica del problema, identifichiamo interventi possibili e progettiamo un test per capire se un onboarding diverso riduca il churn in modo sufficiente da giustificarne il costo.

Il grafico è necessario.

Ma il valore non è il grafico.

### Dove si sposta il valore

Possiamo sintetizzare la trasformazione tecnologica così:

> **L'automazione agisce soprattutto sull'execution; il vantaggio professionale cresce quando sappiamo trasformare execution in analysis e analysis in decisione.**

Questo non significa saltare il livello tecnico.

Se non comprendiamo abbastanza bene l'execution, non possiamo verificarla. Se non sappiamo fare analysis, produciamo calcoli senza evidenza. Se non comprendiamo la decisione, produciamo evidenza che nessuno sa usare.

Il libro svilupperà tutti e tre i livelli.

Gli strumenti verranno studiati quando servono, ma sempre dentro questa gerarchia:

**eseguire correttamente → interpretare correttamente → decidere meglio.**
