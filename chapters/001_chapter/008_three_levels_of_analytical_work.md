## 1.7 I tre livelli del lavoro analitico

Per orientarci nel resto del libro useremo un modello semplice a tre livelli: **execution, analysis e decision intelligence**.

Non sono tre ruoli separati, né una scala gerarchica universale. Uno stesso analista può attraversarli più volte nella stessa giornata. La distinzione serve a capire dove stiamo creando valore e quale tipo di errore stiamo cercando di evitare.

| Livello | Domanda centrale | Esempi di lavoro | Failure mode tipico |
|---|---|---|---|
| **Execution** | Il calcolo o l'artefatto è implementato correttamente? | query, formule, trasformazioni, grafici, script | produrre correttamente il numero sbagliato |
| **Analysis** | Il metodo trasforma i dati in evidenza adatta alla domanda? | metriche, confronti, segmentazioni, inferenza, ipotesi | usare un confronto o un modello non adeguato |
| **Decision Intelligence** | L'evidenza cambia una scelta in modo economicamente sensato? | alternative, costi, rischio, reversibilità, misurazione | produrre un insight che non guida nessuna azione utile |

### Execution: rendere concreta una definizione

L'execution comprende il lavoro tecnico necessario a interrogare, trasformare e presentare i dati. Scrivere SQL, creare una formula, pulire un dataset, automatizzare uno script o costruire una visualizzazione appartiene a questo livello.

L'automazione esercita qui la pressione più evidente perché molte attività possono essere generate o accelerate. Questo non rende superflua la competenza tecnica. Ne cambia il valore: conoscere SQL o Python serve sempre meno soltanto per ricordare sintassi e sempre più per leggere l'implementazione, modificarla, prevederne il comportamento e capire quando non realizza ciò che crediamo.

Se non comprendiamo abbastanza bene l'execution, non possiamo governarla. Ma una buona execution, da sola, non crea ancora evidenza.

### Analysis: decidere quale evidenza merita fiducia

Il secondo livello inizia quando chiediamo se il calcolo sia adatto alla domanda.

Qui scegliamo metriche e popolazioni, definiamo il grain, costruiamo baseline, segmentiamo, osserviamo distribuzioni, distinguiamo trend da rumore e valutiamo spiegazioni alternative. Se serve, introduciamo inferenza statistica, modelli predittivi o disegni causali.

Il criterio cambia. Non basta più chiedere *è stato calcolato correttamente?*; dobbiamo chiedere *questo calcolo ci permette davvero di sostenere la conclusione che ci interessa?*

Un churn perfettamente calcolato sull'intera base clienti può nascondere un problema concentrato in una coorte. Un modello molto accurato può essere inutile se prevede un evento troppo tardi per intervenire. Una regressione senza errori di codice può sostenere una spiegazione causale che il disegno osservazionale non giustifica.

L'analysis trasforma quindi output tecnici in **evidenza disciplinata**.

### Decision Intelligence: trasformare evidenza in scelta

Il terzo livello comincia quando l'evidenza incontra il mondo operativo.

Una conclusione analitica non sceglie da sola tra alternative che hanno costi, tempi, rischi e gradi di reversibilità diversi. Dobbiamo capire quanto vale risolvere il problema, quale soglia di evidenza sia sufficiente, quali interventi siano realisticamente disponibili e come misureremo ciò che accade dopo.

Qui entra anche il valore dell'informazione. Se una decisione è economica e reversibile, può essere razionale agire con evidenza ancora imperfetta e imparare dall'intervento. Se una scelta è costosa o quasi irreversibile, può valere la pena investire molto di più nel ridurre l'incertezza prima di muoversi.

Decision intelligence, nel senso in cui useremo il termine nel libro, è proprio questo passaggio: **non soltanto sapere che cosa indicano i dati, ma capire che cosa convenga fare dato ciò che sappiamo e ciò che ancora non sappiamo.**

### Lo stesso problema attraversa tutti e tre i livelli

Supponiamo che il churn mensile salga dal 4% al 6%.

A livello di execution dobbiamo essere certi che la metrica sia calcolata correttamente. A livello di analysis scopriamo che quasi tutto l'aumento è concentrato nei clienti acquisiti da un canale specifico e nei primi 60 giorni di vita. A livello decisionale stimiamo la dimensione economica del problema, confrontiamo possibili interventi sull'onboarding e progettiamo un test per capire se il beneficio atteso giustifichi il costo.

Il grafico del churn era necessario per vedere il problema. Ma non era ancora il valore finale dell'analisi.

### Dove si sposta il vantaggio professionale

La trasformazione tecnologica può essere sintetizzata così:

> **L'automazione agisce soprattutto sull'execution; il vantaggio professionale cresce quando sappiamo trasformare execution in analysis e analysis in decisione.**

Questo non significa saltare il livello tecnico. Senza execution comprensibile non possiamo verificare ciò che viene prodotto. Senza analysis otteniamo calcoli senza una teoria dell'evidenza. Senza il livello decisionale rischiamo di generare insight che nessuno sa usare.

Il libro svilupperà tutti e tre i livelli con strumenti diversi, ma seguendo sempre lo stesso movimento:

**eseguire correttamente → costruire evidenza credibile → decidere meglio.**
