## 1.3 Il vero lavoro dell'analista

La parte più visibile del lavoro di un Data Analyst è spesso la meno importante.

Una dashboard è visibile. Una query SQL è visibile. Un notebook è visibile. Una presentazione è visibile.

Molto meno visibili sono le decisioni che determinano se quegli output abbiano valore:

- quale domanda merita una risposta;
- quale fenomeno stiamo davvero cercando di misurare;
- quale metrica lo rappresenta abbastanza bene;
- quale confronto è legittimo;
- quali dati sono affidabili;
- quali assunzioni stiamo introducendo;
- quale metodo è sufficiente;
- quale livello di incertezza è accettabile;
- quale evidenza cambierebbe una decisione.

Queste scelte sono il lavoro analitico.

Il resto è implementazione necessaria.

### L'output non è il prodotto finale

Se definiamo il lavoro in base all'artefatto, rischiamo di confondere il mezzo con il fine.

Un analyst può consegnare:

- una tabella;
- un dashboard;
- una query;
- un modello;
- un forecast;
- un memo;
- una raccomandazione.

Ma nessuno di questi oggetti è utile in modo automatico.

Una tabella diventa utile se chiarisce una domanda. Un forecast diventa utile se supporta una scelta di capacità o budget. Un dashboard diventa utile se aiuta qualcuno a rilevare un cambiamento e reagire. Una raccomandazione diventa utile se l'evidenza che la sostiene è abbastanza forte rispetto al costo dell'errore.

Il prodotto finale dell'analisi è quindi meglio descritto come **una riduzione dell'incertezza utilizzabile da qualcuno**.

### Il lavoro invisibile

Due analisti possono produrre lo stesso grafico finale e avere svolto lavori molto diversi.

Il primo ha preso una tabella già pronta, scelto una visualizzazione e riportato il trend.

Il secondo ha verificato la definizione della metrica, controllato un cambio di schema, escluso una duplicazione da join, scelto una baseline stagionale, segmentato il fenomeno e verificato che il pattern non dipendesse da un cambiamento nel mix dei clienti.

Il grafico può sembrare identico.

La qualità dell'evidenza no.

Questa differenza è una delle ragioni per cui il lavoro analitico è difficile da valutare soltanto osservando il deliverable.

### Business understanding e data understanding

CRISP-DM formalizza due passaggi che nel lavoro reale tendono a intrecciarsi continuamente:

1. capire il problema e gli obiettivi di business;
2. capire i dati disponibili e i loro limiti.

IBM descrive la fase di *Business Understanding* come il momento in cui obiettivi e requisiti vengono tradotti in un problema analitico, mentre la fase di *Data Understanding* riguarda raccolta iniziale, esplorazione e valutazione della qualità del dato.

Fonti:
- https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview
- https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview

La distinzione è utile perché impedisce due errori opposti:

- costruire un'analisi tecnicamente impeccabile che non risponde a una decisione reale;
- formulare una domanda interessante senza verificare se i dati possano rappresentarla in modo credibile.

### Una definizione di lavoro

Useremo quindi questa definizione lungo tutto il libro:

> **Un Data Analyst utilizza dati, metodi quantitativi, conoscenza del dominio e strumenti tecnologici per ridurre l'incertezza attorno a decisioni reali.**

La definizione è volutamente indipendente da Excel, SQL, Python, Power BI o AI.

Gli strumenti determinano come possiamo lavorare.

Non determinano perché il lavoro abbia valore.
