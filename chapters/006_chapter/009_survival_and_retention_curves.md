## 6.8 Survival e retention curves: capire quando aumenta il rischio di uscita

Molte dashboard comprimono la retention in pochi punti: D1, D7, D30, M3, M6.

Sono snapshot utili, ma possono nascondere **la forma del decadimento**.

Due coorti possono avere entrambe retention D30 del 50% e comportarsi in modo completamente diverso: una può perdere utenti quasi tutti nei primi tre giorni e poi stabilizzarsi; l'altra può scendere lentamente per tutto il mese.

La curva racconta quindi qualcosa che il singolo punto non può mostrare: **quando il lifecycle diventa fragile**.

### Survival function: il tempo fino all'evento

In survival analysis si considera una variabile `T`: il tempo fino a un evento, per esempio cancellazione, mancato rinnovo o guasto.

La survival function è:

`S(t) = P(T > t)`

cioè la probabilità di superare il tempo `t` senza aver ancora osservato l'evento.

NIST usa la stessa definizione nella reliability analysis: la survival function è la probabilità che un'unità sopravviva oltre un certo tempo.[^nist-survival]

Nel mondo prodotto possiamo tradurla come:

> quale quota della popolazione iniziale è ancora presente dopo `t` giorni, settimane o mesi?

### Caso simulato/composito: Streamly e il giorno 21

**Streamly** è un servizio subscription di corsi video professionali. La dashboard mostra:

- retention D7: 76%;
- D30: 58%;
- D90: 43%.

Il Product Manager interpreta il problema come un generico deterioramento nelle prime settimane.

L'analista costruisce una curva giornaliera per coorte.

Il pattern è molto più specifico: la discesa è relativamente regolare fino al giorno 18, poi accelera tra il giorno 19 e il giorno 24.

La prova gratuita dura 21 giorni.

La curva suggerisce quindi una domanda nuova:

> che cosa succede agli utenti quando si avvicina la prima fatturazione?

Segmentando per comportamento precedente:

- almeno un corso completato entro D14 → retention D45 71%;
- nessun corso completato → retention D45 29%.

Il problema non appare più come “gli utenti si stancano”. Una quota rilevante arriva al momento del pagamento senza aver accumulato abbastanza esperienza di valore.

È ancora una diagnosi osservazionale, ma localizza un momento del lifecycle molto preciso.

### Hazard: il rischio tra chi è ancora presente

La survival curve ci dice quanti rimangono. La **hazard rate** risponde a una domanda diversa:

> tra coloro che sono ancora presenti al tempo `t`, quanto è elevato il rischio di uscita proprio in quel momento?

NIST definisce l'hazard come il tasso istantaneo di failure condizionato al fatto che l'unità sia sopravvissuta fino a `t`.[^nist-hazard]

Nel prodotto digitale, pensare in termini di hazard aiuta a individuare:

- fine del trial;
- primo rinnovo;
- scadenza della carta;
- fine di un onboarding assistito;
- periodi stagionali;
- momenti in cui cambia il prezzo o il contratto.

Il rischio di churn raramente è uniforme per tutto il lifecycle.

### Il problema degli utenti che non hanno ancora avuto il tempo di uscire

Una coorte entrata venti giorni fa non può ancora avere una retention D90 osservata.

Questo introduce il **right censoring**: sappiamo che alcuni utenti sono rimasti almeno fino alla fine della nostra osservazione, ma non sappiamo ancora quando o se avverrà l'evento futuro.

NIST tratta il censoring come una caratteristica centrale dei dati di reliability e lifetime.[^nist-censoring]

Ignorarlo produce confronti distorti.

### Esempio di confronto sbagliato

A settembre il team confronta:

- coorte gennaio: 1.200 clienti, osservati per otto mesi;
- coorte agosto: 2.100 clienti, osservati per un solo mese.

Se calcola “percentuale churnata fino a oggi”, gennaio sembrerà quasi inevitabilmente peggiore: ha avuto molto più tempo per accumulare uscite.

La soluzione è confrontare le coorti **alla stessa età** oppure utilizzare metodi di survival che tengano conto delle osservazioni censurate.

### Kaplan-Meier: intuizione pratica

Il Kaplan-Meier estimator permette di stimare una survival curve anche quando alcuni casi sono censurati.

Per un Data Analyst non è necessario derivarne immediatamente la matematica. È però importante capire il principio:

- utilizziamo le informazioni disponibili fino al momento in cui ogni soggetto è osservabile;
- non trattiamo come “retained per sempre” chi semplicemente non ha ancora raggiunto la fine del periodo;
- aggiorniamo la probabilità di sopravvivenza quando si verificano eventi.

Questo rende il confronto tra lifecycle incompleti molto più corretto di una semplice percentuale cumulata.

### Survival non è solo churn

Lo stesso approccio può essere usato per studiare il tempo fino a:

- activation;
- primo acquisto;
- secondo acquisto;
- upgrade;
- guasto;
- recupero da inattività;
- completamento di un processo.

La domanda diventa:

> non solo *se* l'evento avviene, ma *quando* avviene e come cambia il rischio nel tempo.

### La domanda operativa

Quando retention o churn vengono trattati come un singolo numero, chiediamoci:

**Dove cambia la pendenza della curva? Quali eventi di lifecycle coincidono con quel punto? Le coorti sono abbastanza mature da essere confrontate?**

È qui che il tempo smette di essere una semplice colonna e diventa parte del meccanismo analitico.

[^nist-survival]: NIST/SEMATECH Engineering Statistics Handbook, “Reliability or survival function”, https://www.itl.nist.gov/div898/handbook/apr/section1/apr122.htm
[^nist-hazard]: NIST/SEMATECH Engineering Statistics Handbook, “Failure (or hazard) rate”, https://www.itl.nist.gov/div898/handbook/apr/section1/apr123.htm
[^nist-censoring]: NIST/SEMATECH Engineering Statistics Handbook, “Censoring”, https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm
