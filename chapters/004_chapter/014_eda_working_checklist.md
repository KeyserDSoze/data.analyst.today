## 4.13 L'output dell'EDA: una mappa dell'evidenza, non una cartella di grafici

Durante l'esplorazione possiamo produrre decine di tabelle, scatter plot, distribuzioni e segmentazioni. Sono strumenti di lavoro, non necessariamente il deliverable. Conservare tutto equivale spesso a trasferire allo stakeholder il costo di ricostruire il ragionamento che l'analista avrebbe dovuto sintetizzare.

Il prodotto finale dovrebbe invece mostrare **come è cambiata la nostra comprensione del fenomeno**. Per questo useremo una **EDA Evidence Map**: un artefatto breve che separa il fatto osservato dalla sua concentrazione, la robustezza del pattern dalle ipotesi e ciò che possiamo descrivere da ciò che richiede un metodo più forte.

La struttura si è guadagnata il diritto di restare esplicita perché serve a impedire che, nella sintesi, i livelli di evidenza tornino a mescolarsi.

### 1. Fenomeno osservato

Il punto di partenza è una frase quantitativa con baseline esplicita:

> Il churn mensile è passato dal 6,2% all'8,1% negli ultimi quattro mesi, +1,9 pp rispetto alla media dei sei mesi precedenti.

Questa è un'osservazione. “Il nuovo onboarding sta facendo aumentare il churn” è già una spiegazione e richiede altra evidenza.

### 2. Concentrazione e composizione

Il secondo blocco spiega dove vive il fenomeno e quanto del totale riusciamo a localizzare. Possiamo scoprire, per esempio, che **circa il 72% dell'aumento assoluto di churn proviene da SMB con meno di sei mesi di tenure, mentre Enterprise è stabile**. La frase restringe il problema senza attribuirgli ancora una causa.

Qui entrano anche mix, denominatori, code e differenze tra media e percentili. Un movimento aggregato è più interpretabile quando sappiamo se è generalizzato oppure prodotto da pochi segmenti, da una popolazione che cambia composizione o da una parte estrema della distribuzione.

### 3. Robustezza

Ogni pattern importante dovrebbe sopravvivere ad almeno un controllo ragionevole della lente con cui lo abbiamo osservato. Possiamo confrontare media e mediana, baseline temporali alternative sensate, tasso e volume, totale e segmentazioni motivate, dataset completo e sensitivity analysis sui punti influenti.

Una classificazione informale può essere sufficiente:

- **robusto** — resta sostanzialmente invariato nelle letture plausibili;
- **moderatamente sensibile** — cambia in ampiezza ma non nella direzione o nella sostanza;
- **fragile** — dipende fortemente da una scelta, un periodo o poche osservazioni.

Non è un test statistico. È memoria della dipendenza del pattern dalle scelte esplorative.

### 4. Ipotesi candidate e alternative

Una piccola tabella evita che le interpretazioni diventino fatti per ripetizione:

| Pattern | Ipotesi candidata | Alternativa plausibile | Evidenza mancante |
|---|---|---|---|
| churn alto nei nuovi SMB | onboarding insufficiente | acquisition mix | completion e canale |
| P95 delivery alto nel weekend | capacity insufficiente | mix geografico | volume per zona |
| AOV alto nel social | effetto canale | product mix premium | confronto a mix costante |

L'EDA è utile proprio perché riduce lo spazio delle storie possibili **senza chiuderlo artificialmente**.

### 5. Prossimo metodo o stop

L'ultima parte deve chiarire che cosa non può più essere risolto con un altro grafico. La risposta può essere inferenza statistica, nuova raccolta dati, analisi di coorte, forecasting, modello predittivo, esperimento o metodo causale. Può anche essere “nessun altro lavoro”: se la domanda era puramente descrittiva e l'evidenza è sufficiente per la decisione, fermarsi è una conclusione professionale.

## Template operativo

```text
Domanda:

Fatto principale:

Baseline:

Distribuzione:

Segmenti che spiegano il delta:

Composizione / denominatori rilevanti:

Pattern principali:

Sensitivity checks:

Pattern robusti:

Pattern fragili:

Ipotesi candidate:

Spiegazioni alternative:

Cosa NON è dimostrato:

Prossimo metodo / decisione:
```

La differenza rispetto a una consegna del tipo “correlazione ticket-churn = 0,54” è sostanziale. Una Evidence Map può dire che il churn è aumentato dal 6,2% all'8,1%, quasi tutto nei nuovi SMB; in quel gruppo chi apre almeno tre ticket nei primi 30 giorni mostra churn maggiore; la relazione resta visibile per canale ma si riduce molto controllando per product tier; non sappiamo se i ticket siano causa, sintomo di problemi di prodotto o entrambe le cose. A quel punto il prossimo controllo — categorie ticket e sequenza temporale — nasce direttamente dall'evidenza.

Prima di chiudere l'EDA, quindi, vogliamo aver descritto centro, dispersione e forma dove servono, conservato volumi e denominatori, verificato composizione e tempo, guardato la forma prima dei coefficienti e stressato i pattern principali. Soprattutto, dobbiamo saper dire quali frasi sono fatti, quali ipotesi e quali ancora non abbiamo il diritto di sostenere.

NIST descrive l'EDA come un approccio orientato alla scoperta della struttura e al controllo delle assunzioni, non come una procedura meccanica.[^nist-eda]

> **Una buona EDA riduce il numero di storie compatibili con i dati e rende esplicito quale metodo serve per ridurlo ancora.**

[^nist-eda]: NIST/SEMATECH, *Exploratory Data Analysis*. https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
