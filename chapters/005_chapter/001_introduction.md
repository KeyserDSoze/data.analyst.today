# Capitolo 5 — Probabilità, campionamento e incertezza

> **Un numero senza incertezza può sembrare più preciso di quanto la realtà consenta.**

Nel Capitolo 4 abbiamo costruito una **EDA Evidence Map**: abbiamo imparato a descrivere ciò che osserviamo, a localizzare un pattern, a stressarlo contro segmenti, baseline e osservazioni influenti e, soprattutto, a separare ciò che i dati mostrano dalle spiegazioni che restano soltanto candidate.

Ora dobbiamo fare un passo diverso. Non basta più chiedere **che cosa mostrano i dati che abbiamo raccolto**. Dobbiamo capire quanto quella descrizione dipenda dal particolare insieme di casi che abbiamo osservato, quanto potrebbe cambiare se il processo producesse altri esiti e fino a dove possiamo generalizzare la stima.

L'incertezza entra quindi nel lavoro analitico in almeno due modi distinti.

Il primo è la **variabilità del processo**. Anche se conoscessimo perfettamente un sistema, il prossimo esito non sarebbe necessariamente deterministico. Se un corriere ha il 6% di consegne oltre SLA, non sappiamo quali saranno in ritardo domani. Se un gruppo di clienti ha churn rate del 12%, non sappiamo quale singolo cliente rinnoverà. La probabilità descrive questa variabilità degli esiti possibili.

Il secondo è l'**incertezza della stima**. Spesso non conosciamo nemmeno con precisione quel 6% o quel 12%: li stimiamo da un campione, da una finestra storica limitata, da una survey, da un esperimento o da un sottoinsieme della popolazione. Se osserviamo 500 clienti e 60 churnano, il 12% è una realizzazione possibile del processo di raccolta. Un altro campione comparabile avrebbe potuto produrre 10,8%, 12,6% o 13,4%. L'inferenza statistica cerca di quantificare questa seconda incertezza.

Le due cose possono muoversi in direzioni opposte. Un processo può essere molto variabile e tuttavia conosciuto con grande precisione perché abbiamo milioni di osservazioni indipendenti. Oppure può essere relativamente stabile ma conosciuto male perché il campione è piccolo, selezionato o poco rappresentativo.

## Due numeri entrambi uguali al 91%

Immaginiamo una società e-commerce. Negli ultimi sei mesi il **91% delle spedizioni** è arrivato entro 48 ore. Nello stesso trimestre una survey su 620 clienti mostra che il **91% dei rispondenti** si dichiara soddisfatto della consegna.

I due numeri sono identici. La loro qualità inferenziale non lo è.

Il primo descrive quasi tutte le spedizioni concluse nel periodo. Per raccontare quel periodo l'incertezza di campionamento può essere minima, mentre resta aperta un'altra domanda: il processo sarà altrettanto stabile domani, con un diverso mix di ordini, vettori o condizioni operative?

Il secondo 91% nasce invece da persone che hanno avuto una certa probabilità di essere invitate, raggiunte e di scegliere di rispondere. Prima di generalizzarlo all'intera customer base dobbiamo capire come sono stati selezionati i 620 clienti, quanti sono stati invitati, chi non ha risposto e se il meccanismo di raccolta lascia fuori proprio le esperienze più problematiche.

AAPOR distingue esplicitamente il **margin of sampling error** da altre componenti del total survey error, tra cui coverage, measurement e nonresponse.[^aapor-definitions] Questo significa che un intervallo strettissimo può quantificare bene la variabilità casuale della stima e, nello stesso tempo, non dire quasi nulla su un bias di selezione.

È uno dei principi centrali del capitolo:

> **Più osservazioni possono ridurre il rumore casuale. Non trasformano automaticamente un campione sbagliato nella popolazione giusta.**

La catena costruita fin qui nel libro diventa quindi:

**domanda ben specificata → dato fit for purpose → struttura esplorata → incertezza quantificata**.

Saltare uno dei passaggi precedenti rende fragile quello successivo. Un confidence interval non ripara una metrica definita male; un p-value non rende comparabili due gruppi che non lo sono; un milione di risposte non corregge un meccanismo di selezione sistematicamente distorto.

## Tre movimenti, una sola domanda

La prima parte del capitolo costruisce il linguaggio con cui modelliamo un processo incerto: evento, probabilità, condizionamento, dipendenza, distribuzione, valore atteso e aggiornamento dell'evidenza. Non sono formule da memorizzare in sequenza; sono strumenti per rendere esplicito **quali esiti consideriamo possibili e quali assunzioni ci permettono di assegnare loro un peso**.

La seconda parte sposta l'attenzione dal processo al campione. Vedremo perché una statistica osservata è soltanto una delle stime che avremmo potuto ottenere, come lo standard error quantifica quella variabilità, quale ruolo svolge il Central Limit Theorem e perché un intervallo di confidenza descrive la precisione del metodo senza includere automaticamente ogni possibile fonte di errore. NIST descrive proprio l'intervallo di confidenza come un modo per rappresentare quanto bene una statistica campionaria approssima un parametro di popolazione e ne lega il livello di confidenza alla copertura del procedimento su campionamenti ripetuti.[^nist-ci]

La terza parte riguarda il momento in cui l'incertezza incontra una decisione. Test di ipotesi, p-value, errori di tipo I e II, power, materialità e multiple testing devono impedirci di trasformare una procedura statistica in un semaforo automatico. L'American Statistical Association ricorda che un p-value non misura la probabilità che l'ipotesi studiata sia vera, non misura la dimensione dell'effetto e non dovrebbe essere l'unica base di una decisione.[^asa-pvalue] Nel 2021 una task force dell'ASA ha ribadito un principio ancora più generale: nessuna singola misura di incertezza serve a tutti gli scopi e le fonti di variazione considerate — e quelle non considerate — dovrebbero essere rese visibili.[^asa-taskforce]

Per questo il capitolo non culminerà in una formula. Culminerà in un **Uncertainty Brief**, un artefatto che mette nello stesso posto stima, popolazione, precisione, assunzioni, bias non quantificati, dimensione dell'effetto e soglia decisionale.

Alla fine dovremmo essere capaci di prendere una frase come:

> “Il conversion rate osservato è 8,4%.”

E trasformarla in una valutazione molto più adulta: 8,4% su quale popolazione? Con quale meccanismo di raccolta? Quanto oscillerebbe la stima? Quale parte dell'errore non è dentro l'intervallo? Quanto è grande l'effetto rispetto alla baseline? Quanto dovrebbe essere grande per cambiare una decisione? Quante analisi abbiamo provato prima di trovare proprio questo risultato?

> **L'incertezza non è una debolezza da nascondere nel footer. È una proprietà dell'evidenza che determina quanto forte può essere la conclusione.**

---

### Fonti

[^aapor-definitions]: AAPOR, *Standard Definitions*, 10th edition e risorse sul Total Survey Error. https://aapor.org/standards-and-ethics/standard-definitions/
[^nist-ci]: NIST/SEMATECH, *What are confidence intervals?*. https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
[^asa-pvalue]: American Statistical Association, *Statement on Statistical Significance and P-Values*. https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
[^asa-taskforce]: ASA President's Task Force, *Statement on Statistical Significance and Replicability*. https://magazine.amstat.org/blog/2021/08/01/task-force-statement-p-value/
