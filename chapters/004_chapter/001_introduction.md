# Capitolo 4 - Statistica descrittiva ed Exploratory Data Analysis

> **Prima di spiegare un fenomeno, dobbiamo imparare a descriverlo senza distruggerne la struttura.**

Nel Capitolo 3 ci siamo guadagnati il diritto di usare il dataset. Abbiamo ricostruito che cosa rappresentano le righe, quali identità e tempi contiene, quali limiti rimangono e per quali domande il dato è realmente *fit for purpose*. Da questo punto in avanti il problema cambia: non dobbiamo più chiederci soltanto se il dato è credibile, ma **che forma assume il fenomeno quando lo osserviamo senza forzarlo troppo presto dentro una storia**.

La statistica descrittiva nasce dalla necessità di comprimere. Milioni di osservazioni non possono essere lette una per una, quindi le trasformiamo in medie, mediane, percentili, tassi e misure di dispersione. Ogni compressione, però, conserva alcune proprietà e ne perde altre. Una media può rappresentare bene un totale economico e male l'esperienza tipica; un tasso aggregato può essere corretto e nascondere un cambiamento di composizione; una correlazione può riassumere un movimento congiunto e occultare la forma che lo produce.

L'**Exploratory Data Analysis**, o EDA, serve precisamente a governare questo rischio. NIST la descrive come un approccio che usa soprattutto tecniche grafiche per massimizzare la comprensione di un dataset, scoprirne la struttura, individuare anomalie e verificare assunzioni prima di imporre un modello formale.[^nist-eda] Esplorare, quindi, non significa generare grafici senza direzione. Significa usare più rappresentazioni dello stesso fenomeno per distinguere ciò che i dati mostrano da ciò che stiamo iniziando a immaginare.

Questa distinzione è il filo del capitolo. Durante una buona EDA dobbiamo riuscire a tenere separati tre livelli: **l'osservazione**, cioè il pattern direttamente sostenuto dai dati; **l'ipotesi**, cioè una possibile spiegazione che quel pattern rende plausibile; e **la conclusione non ancora guadagnata**, soprattutto quando il linguaggio comincia a suggerire causalità.

## Una sintesi corretta può essere insufficiente

Immaginiamo che una società di logistica comunichi un miglioramento del tempo medio di consegna da 3,8 a 3,1 giorni. Il numero è corretto e, preso da solo, suggerisce che il servizio sia migliorato. Quando però separiamo urbano e rurale scopriamo che l'urbano passa da 2,1 a 1,8 giorni, il rurale da 5,6 a 6,4 e, nello stesso periodo, la quota di ordini urbani cresce dal 58% al 74%.

La media complessiva non mentiva. Stava combinando due fenomeni: un miglioramento urbano e un peggioramento rurale, con un mix sempre più spostato verso il segmento veloce. La domanda analitica non è quindi quale dei numeri sia “vero”, ma **quale struttura dobbiamo rendere visibile per evitare che una sintesi corretta venga trasformata in una spiegazione sbagliata**.

## Il quartetto di Anscombe: stessa sintesi, strutture incompatibili

Il caso classico è il **quartetto di Anscombe**, pubblicato da Francis Anscombe nel 1973 e ripreso dal NIST come esempio del ruolo dell'analisi grafica.[^anscombe-original][^nist-anscombe] I quattro dataset hanno praticamente la stessa media di `X` e `Y`, la stessa retta di regressione, una deviazione residua quasi identica e una correlazione intorno a `0,816`. Se osservassimo soltanto quei riepiloghi, sembrerebbero equivalenti.

Gli scatter plot mostrano invece quattro mondi diversi: una relazione lineare plausibile, una relazione curva, un insieme dominato da un outlier e un caso in cui quasi tutta la relazione dipende da un singolo punto ad alta leva. Il punto non è che le statistiche sintetiche siano inutili. È che **ogni sintesi elimina informazione**, e l'analista deve capire se l'informazione eliminata può cambiare la decisione.

Per questo il percorso del capitolo non sarà una lista di tecniche statistiche indipendenti. Partiremo dal centro di una distribuzione e aggiungeremo progressivamente ciò che il centro non riesce a raccontare: dispersione, code e forma. Useremo poi confronti, segmentazioni, denominatori e popolazioni di riferimento per capire se un pattern aggregato sopravvive alla composizione. Passeremo infine a relazioni, tempo e sensitivity analysis per stressare l'interpretazione prima di promuoverla a insight.

Il deliverable che raccoglie questo lavoro sarà la **EDA Evidence Map**. Non una galleria di grafici, ma una mappa che dica che cosa osserviamo, dove si concentra il fenomeno, quali pattern sono robusti, quali sono fragili, quali spiegazioni restano aperte e quale metodo serve per andare oltre la descrizione.

Il Capitolo 5 partirà esattamente da questo confine. Quando avremo descritto bene ciò che abbiamo osservato, potremo chiederci quanto la stima sia incerta e quanto possiamo generalizzare oltre quei dati.

> **L'EDA non deve produrre la storia più convincente. Deve rendere più difficile che una storia prematura sopravviva al confronto con la struttura dei dati.**

---

### Fonti

[^nist-eda]: NIST/SEMATECH, *Exploratory Data Analysis*. https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
[^anscombe-original]: F. J. Anscombe, *Graphs in Statistical Analysis*, The American Statistician, 27(1), 1973, pp. 17–21. https://doi.org/10.1080/00031305.1973.10478966
[^nist-anscombe]: NIST/SEMATECH, *An EDA/Graphics Example*. https://www.itl.nist.gov/div898/handbook/eda/section1/eda16.htm
