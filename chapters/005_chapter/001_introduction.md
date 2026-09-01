# Capitolo 5 — Probabilità, campionamento e incertezza

> **Un numero senza incertezza può sembrare più preciso di quanto la realtà consenta.**

Nel Capitolo 4 abbiamo costruito una **EDA Evidence Map**: ciò che osserviamo, dove si concentra il fenomeno, quanto è robusto il pattern e quali spiegazioni restano soltanto ipotesi.

Ora cambia la domanda.

Non vogliamo più sapere soltanto:

> **Che cosa mostrano i dati che abbiamo osservato?**

Vogliamo anche sapere:

> **Quanto possiamo fidarci della stima? Quanto potrebbe cambiare se osservassimo altri casi? Che cosa possiamo generalizzare oltre il campione? Quanto è plausibile un risultato sotto determinate assunzioni?**

Questa è la funzione del Capitolo 5.

## 5.0 Due tipi di incertezza che l'analista incontra continuamente

Nel lavoro reale la parola *incertezza* nasconde almeno due problemi distinti.

### 1. Variabilità del processo

Anche se conoscessimo perfettamente il processo, il prossimo risultato non sarebbe necessariamente deterministico.

Un corriere può avere il 6% di consegne oltre SLA. Non sappiamo in anticipo quali saranno le prossime consegne in ritardo.

Un cliente può appartenere a un gruppo con churn rate del 12%. Non sappiamo con certezza se quel singolo cliente rinnoverà.

Qui la probabilità descrive **la variabilità degli esiti**.

### 2. Incertezza della stima

Spesso non conosciamo nemmeno perfettamente quel 6% o quel 12%.

Lo stimiamo da:

- un campione;
- una finestra storica limitata;
- una survey;
- un esperimento;
- un sottoinsieme di utenti;
- dati soggetti a nonresponse, selezione o rumore.

Se osserviamo 500 clienti e 60 churnano, il 12% è una stima. Un altro campione della stessa popolazione potrebbe produrre 10,8%, 12,6% o 13,4%.

Qui l'inferenza statistica cerca di quantificare **quanto è precisa la nostra conoscenza del parametro**.

Le due incertezze non sono la stessa cosa.

Un processo può essere molto variabile ma stimato con grande precisione grazie a milioni di osservazioni. Oppure può essere relativamente stabile ma conosciuto male perché abbiamo pochi dati o un campione distorto.

### Caso simulato/composito — Due numeri entrambi “91%”

Una società e-commerce osserva che, negli ultimi sei mesi, il **91% delle spedizioni** è arrivato entro 48 ore.

Nello stesso trimestre conduce una survey su 620 clienti e il **91% dei rispondenti** dichiara di essere soddisfatto della consegna.

I due `91%` sembrano simili. Statisticamente non lo sono.

Il primo deriva da quasi tutte le spedizioni concluse nel periodo. Per descrivere quel periodo l'incertezza di campionamento è minima, anche se rimane incertezza su ciò che accadrà domani e su quanto il processo resterà stabile.

Il secondo deriva da un campione di rispondenti. Prima di generalizzare alla customer base dobbiamo chiederci:

- come sono stati selezionati i 620 clienti?
- quanti sono stati invitati e quanti hanno risposto?
- i non rispondenti differiscono dai rispondenti?
- qual è la precisione dovuta al campionamento?
- la domanda misura davvero la soddisfazione che ci interessa?

AAPOR sottolinea un punto essenziale: il margine di campionamento quantifica soltanto una parte dell'errore e non incorpora automaticamente problemi come nonresponse bias o errori di copertura.[^aapor-accuracy]

Lo stesso valore percentuale può quindi avere **qualità inferenziale completamente diversa**.

## Più dati non significa automaticamente meno incertezza

Se il campione è rappresentativo e le assunzioni sono ragionevoli, più osservazioni riducono spesso l'incertezza di campionamento.

Ma un miliardo di osservazioni selezionate male può stimare con enorme precisione la popolazione sbagliata.

Questo principio tornerà più volte:

> **La numerosità riduce il rumore casuale. Non corregge automaticamente bias, definizioni sbagliate o campioni non rappresentativi.**

Per questo probabilità e inferenza devono sempre restare collegate ai Capitoli 2–4:

**domanda ben specificata → dato fit for purpose → struttura esplorata → incertezza quantificata**.

## Il percorso del capitolo

Il capitolo è organizzato in tre movimenti.

### Parte I — Modellare l'incertezza

Costruiremo il linguaggio di base:

**evento → probabilità → probabilità condizionata → indipendenza → distribuzione → valore atteso → variabilità → aggiornamento bayesiano**.

L'obiettivo non è memorizzare formule, ma imparare a tradurre un processo reale in eventi e assunzioni esplicite.

### Parte II — Dal campione alla popolazione

Passeremo poi a:

**campionamento → sampling distribution → standard error → Central Limit Theorem → intervallo di confidenza → margin of error → sample size**.

Qui la domanda sarà:

> **Se ripetessimo il processo di raccolta, quanto oscillerebbe la nostra stima?**

NIST descrive l'intervallo di confidenza proprio come uno strumento per esprimere l'incertezza con cui una statistica campionaria approssima un parametro di popolazione.[^nist-ci]

### Parte III — Valutare evidenza senza trasformare un test in una sentenza

Infine affronteremo:

**ipotesi nulla → test → p-value → errori di tipo I e II → power → significatività statistica vs rilevanza economica → multiple testing**.

Qui fisseremo una regola editoriale e professionale importante.

L'American Statistical Association ricorda che un p-value non misura la probabilità che l'ipotesi studiata sia vera, non misura la dimensione dell'effetto e non dovrebbe essere l'unica base per una decisione.[^asa-pvalue]

Quindi:

> **`p < 0,05` non è una decisione di business. È un pezzo di evidenza prodotto sotto un insieme di assunzioni.**

## Il filo logico

Alla fine del capitolo dovremmo essere in grado di passare da:

> “Il conversion rate osservato è 8,4%.”

A domande molto più mature:

- 8,4% su quale campione e quale popolazione?
- quanto è precisa la stima?
- quali fonti di bias non sono rappresentate dal margine di errore?
- qual è l'intervallo di valori compatibile con i dati e il metodo?
- se confrontiamo 8,4% con 8,0%, la differenza è abbastanza grande da contare?
- quante osservazioni servono per rilevare un effetto che abbia valore economico?
- quante metriche o segmentazioni abbiamo provato prima di trovare quella “significativa”? 

Questo è il vero salto dall'EDA all'inferenza.

> **L'incertezza non è una debolezza da nascondere nel footer. È una proprietà dell'evidenza che determina quanto forte può essere la conclusione.**

[^aapor-accuracy]: AAPOR, *Polling Accuracy*: https://aapor.org/polling-accuracy/
[^nist-ci]: NIST/SEMATECH, *What are confidence intervals?*: https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
[^asa-pvalue]: American Statistical Association, *Statement on Statistical Significance and P-Values*: https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
