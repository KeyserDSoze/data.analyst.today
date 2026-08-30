## 4.13 Una checklist operativa per l'EDA

L'Exploratory Data Analysis non è una sequenza rigida, ma avere una struttura riduce il rischio di saltare controlli essenziali.

Prima di arrivare a una conclusione, un analista dovrebbe essere in grado di rispondere almeno a queste domande.

### Struttura

- Qual è l'unità di analisi?
- Qual è la granularità reale?
- Quante osservazioni abbiamo?
- Quali variabili sono quantitative, categoriche, temporali o identificative?

### Distribuzioni

- Quali sono media, mediana, quantili e dispersione?
- La distribuzione è simmetrica o fortemente asimmetrica?
- Esistono code lunghe, multimodalità o cluster visibili?
- Gli outlier sono errori o fenomeni reali?

### Segmenti

- Il risultato aggregato cambia per paese, prodotto, canale, customer type o coorte?
- Un gruppo molto grande sta dominando la media?
- Esiste un possibile Simpson's paradox?

### Relazioni

- Le variabili si muovono insieme?
- La relazione è lineare?
- È guidata da pochi punti?
- Esiste una terza variabile plausibile che può spiegare entrambe?

### Tempo

- Esiste trend?
- Esiste stagionalità?
- Il confronto temporale usa una baseline sensata?
- Un singolo giorno o periodo anomalo sta guidando la conclusione?
- Una media mobile aiuta a separare rumore e movimento di fondo?

### Sensitivity check

Una delle abitudini più utili è ripetere l'analisi con assunzioni leggermente diverse.

Se il risultato sparisce quando:

- si rimuove un singolo outlier;
- si cambia la finestra temporale;
- si controlla per un segmento;
- si usa la mediana invece della media;
- si esclude una settimana promozionale;

allora l'insight è fragile e va comunicato come tale.

### L'output dell'EDA

L'EDA non dovrebbe produrre soltanto grafici. Dovrebbe produrre una lista di ciò che sappiamo, ciò che sospettiamo e ciò che deve ancora essere verificato.

Un buon output può avere questa forma:

**Osservazione:** il churn è aumentato dal 6,2% all'8,1%.

**Concentrazione:** l'aumento è quasi interamente nel segmento SMB acquisito negli ultimi sei mesi.

**Pattern:** i clienti coinvolti mostrano forte crescita dei ticket nei primi 30 giorni.

**Ipotesi:** onboarding insufficiente o mismatch tra aspettative commerciali e prodotto.

**Non dimostrato:** i ticket causano churn.

**Prossimo passo:** analizzare categorie ticket, canale di acquisizione, onboarding completion e, se possibile, progettare una verifica causale.

Questa distinzione è fondamentale: **l'EDA deve restringere lo spazio delle spiegazioni, non fingere di averle già dimostrate**.

IBM descrive l'EDA come un processo che usa tecniche statistiche e visuali per analizzare pattern, anomalie e relazioni prima di costruire conclusioni o modelli più formali.[^ibm-eda]

[^ibm-eda]: IBM, *What is Exploratory Data Analysis?*: https://www.ibm.com/think/topics/exploratory-data-analysis