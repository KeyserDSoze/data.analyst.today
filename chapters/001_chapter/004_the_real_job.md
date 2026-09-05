## 1.3 Il vero lavoro dell'analista

La parte più visibile del lavoro di un Data Analyst è spesso quella che l'organizzazione scambia più facilmente per il lavoro stesso.

Una dashboard si vede. Una query SQL si può aprire. Un notebook lascia codice. Una presentazione arriva in riunione. Sono artefatti concreti e quindi facili da contare, mostrare e consegnare.

Molto meno visibile è il percorso che determina se quell'artefatto meriti fiducia.

Due analisti possono consegnare lo stesso grafico: stessa linea, stesso asse, stesso numero finale. Il primo può aver preso una tabella pronta e riportato il trend. Il secondo può aver scoperto che la definizione della metrica è cambiata a metà periodo, verificato il grain della tabella, escluso una duplicazione da join, scelto una baseline coerente con la stagionalità e controllato che il movimento aggregato non dipendesse soltanto da un cambiamento nel mix dei clienti.

Il deliverable è quasi identico. **La qualità dell'evidenza che contiene è completamente diversa.**

### Il prodotto non coincide con l'output

Definire il mestiere in base all'artefatto porta facilmente a confondere il mezzo con il fine. Un analyst può consegnare una tabella, un dashboard, una query, un modello, un forecast, un memo o una raccomandazione. Nessuno di questi oggetti produce valore per il semplice fatto di esistere.

Una tabella è utile se rende più chiara una domanda. Un forecast è utile se cambia una scelta di capacità, budget o rischio. Un dashboard è utile se permette a qualcuno di rilevare una deviazione e reagire. Una raccomandazione è utile se il livello di evidenza che la sostiene è proporzionato al costo di seguirla quando è sbagliata.

Per questo è più utile pensare al prodotto finale dell'analisi come a **una riduzione dell'incertezza utilizzabile da qualcuno**. L'artefatto è il veicolo attraverso cui quella riduzione diventa condivisibile, verificabile e, quando serve, operativa.

Questa distinzione cambia anche il modo in cui valutiamo il lavoro. Un analyst che produce molti dashboard può avere un impatto inferiore a chi elimina un equivoco semantico che alimentava dieci report. Una query di poche righe può valere più di un modello complesso se isola il driver che cambia una decisione. Un'analisi può persino concludere che non abbiamo evidenza sufficiente per agire e creare più valore di una raccomandazione molto sicura costruita su dati fragili.

### Il lavoro invisibile è fatto di scelte

Ciò che non compare nel deliverable sono spesso le decisioni più importanti: quale domanda valga la pena affrontare, quale fenomeno stiamo davvero cercando di misurare, quale proxy sia accettabile, quale baseline renda il confronto onesto, quale trasformazione possa cambiare il significato del dato e quale metodo sia sufficiente senza introdurre complessità inutile.

Poi arrivano scelte ancora più difficili: capire quali spiegazioni rivali meritino un controllo, quanta incertezza possiamo tollerare e quale evidenza sarebbe abbastanza forte da modificare una decisione.

È qui che si trova gran parte del mestiere. L'esecuzione tecnica serve a rendere queste scelte concrete; non le sostituisce.

### Business understanding e data understanding devono incontrarsi

CRISP-DM formalizza due momenti che nel lavoro reale si alimentano a vicenda. La *Business Understanding* chiarisce obiettivi e requisiti e li traduce in un problema analitico. La *Data Understanding* riguarda la raccolta iniziale, l'esplorazione e la valutazione della qualità del dato.

Fonti:
- https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview
- https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview

La distinzione è utile perché mostra due modi opposti di fallire. Possiamo costruire un'analisi tecnicamente impeccabile che non risponde a nessuna decisione reale. Oppure possiamo formulare una domanda importante e scoprire troppo tardi che i dati disponibili non rappresentano il fenomeno con sufficiente credibilità.

Un buon analista fa dialogare continuamente i due lati. Il business chiarisce che cosa conta; i dati chiariscono che cosa possiamo osservare; il metodo stabilisce quale inferenza sia possibile; la decisione determina quanto forte debba essere l'evidenza.

### Una definizione di lavoro

Useremo quindi questa definizione lungo tutto il libro:

> **Un Data Analyst utilizza dati, metodi quantitativi, conoscenza del dominio e strumenti tecnologici per ridurre l'incertezza attorno a decisioni reali.**

La definizione è volutamente indipendente da Excel, SQL, Python, Power BI o AI. Gli strumenti determinano che cosa possiamo fare, a quale costo e con quale affidabilità.

Non determinano, da soli, perché quel lavoro abbia valore.
