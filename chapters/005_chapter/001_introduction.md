# Capitolo 5 - Probabilità e incertezza

> La statistica descrive ciò che abbiamo osservato. La probabilità ci aiuta a ragionare su ciò che potrebbe accadere, su quanto siamo incerti e su quali decisioni siano sensate quando non possiamo conoscere tutto.

## Introduzione

Un Data Analyst lavora quasi sempre in condizioni di informazione incompleta.

Non conosce il comportamento futuro di ogni cliente. Non sa con certezza quante spedizioni arriveranno in ritardo domani. Non può osservare tutti i clienti possibili, tutti gli ordini futuri o tutte le condizioni di mercato che potrebbero verificarsi. Anche quando dispone di milioni di righe, rimane una parte della realtà che non ha ancora osservato.

Per questo la probabilità non è un argomento teorico separato dal lavoro quotidiano. È il linguaggio con cui si ragiona quando esistono **variabilità, rischio e incertezza**.

Nel capitolo precedente abbiamo imparato a descrivere i dati: medie, mediane, dispersione, percentili, correlazioni, trend, distribuzioni empiriche. Ora facciamo un passo diverso.

La domanda non è più soltanto:

**“Che cosa è successo?”**

Diventa anche:

**“Quanto è plausibile che succeda?”**

**“Quanto possiamo fidarci del risultato che vediamo?”**

**“Che cosa cambia se arriva una nuova informazione?”**

**“Quale decisione conviene prendere quando gli esiti possibili sono diversi?”**

### Un caso semplice: il problema non è la media

Immaginiamo una compagnia di e-commerce che promette consegna in 48 ore.

Negli ultimi sei mesi il tempo medio di consegna è stato di 31 ore.

Il responsabile operativo conclude:

> “Siamo tranquillamente dentro la promessa. Abbiamo diciassette ore di margine.”

Ma il team analytics guarda la distribuzione e scopre che:

- il 76% delle spedizioni arriva entro 36 ore;
- il 91% arriva entro 48 ore;
- il 7% arriva tra 48 e 72 ore;
- il 2% impiega più di 72 ore.

Il tempo medio è ottimo, ma circa una spedizione su undici viola la promessa.

Se domani partono 18.000 pacchi, il problema operativo non è sapere che il tempo medio atteso è vicino alle 31 ore. Il problema è capire quanti pacchi potrebbero superare le 48 ore, con quale variabilità e con quali conseguenze per customer care, rimborsi e reputazione.

Qui compare il ragionamento probabilistico.

Non perché serva una formula sofisticata, ma perché la decisione riguarda **eventi incerti**.

### La probabilità come modello, non come magia

Quando diciamo che un evento ha probabilità del 10%, non stiamo affermando che ogni gruppo di dieci casi conterrà esattamente un evento.

Stiamo costruendo un modello del processo.

Se il processo fosse sufficientemente stabile e ripetuto molte volte, ci aspetteremmo una frequenza vicina al 10%. Nel breve periodo, però, i risultati possono deviare anche in modo significativo.

Questa distinzione è fondamentale.

Un churn rate storico del 5% non significa che esattamente cinque dei prossimi cento clienti abbandoneranno. Significa che, sotto determinate condizioni e assunzioni, possiamo trattare il 5% come una stima della probabilità individuale o aggregata di churn.

Il lavoro dell'analista consiste nel capire se quelle condizioni sono plausibili.

### Dal dato osservato all'incertezza

Il percorso che seguiremo in questo capitolo è:

**Evento → probabilità → condizionamento → distribuzione → valore atteso → variabilità → aggiornamento dell'evidenza → decisione**

Vedremo che molti concetti apparentemente astratti diventano immediatamente concreti quando vengono collegati a problemi reali:

- probabilità condizionata per capire il rischio di churn dato un comportamento;
- indipendenza per evitare di moltiplicare probabilità che non sono indipendenti;
- distribuzione binomiale per ragionare sul numero di conversioni in una campagna;
- valore atteso per confrontare decisioni con esiti economici incerti;
- varianza per distinguere due strategie con la stessa media ma rischio diverso;
- legge dei grandi numeri per capire perché i KPI diventano più stabili all'aumentare dei volumi;
- ragionamento bayesiano per aggiornare una probabilità quando arriva nuova evidenza.

La probabilità diventa così una disciplina pratica: non serve a prevedere perfettamente il futuro, ma a **prendere decisioni razionali quando il futuro non è perfettamente prevedibile**.

### Una nota sulle distribuzioni

Le distribuzioni di probabilità sono modelli. Non sono la realtà.

NIST descrive le distribuzioni come strumenti fondamentali della statistica e sottolinea che, prima di utilizzare una tecnica basata su una particolare assunzione distributiva, occorre verificare che tale assunzione sia adeguata ai dati e al problema.[^1]

Questa idea accompagnerà tutto il capitolo.

Non useremo una distribuzione perché “è quella che si usa di solito”.

La useremo quando le assunzioni che la rendono sensata sono compatibili con il processo che stiamo studiando.

---

[^1]: NIST/SEMATECH, *e-Handbook of Statistical Methods - Probability Distributions*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda36.htm
