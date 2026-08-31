## 6.8 Survival e retention curves: guardare il tempo come una variabile

Molte analisi di retention vengono ridotte a pochi punti: Day 1, Day 7, Day 30. È utile, ma spesso insufficiente.

Una retention curve considera l'intero percorso temporale. Per ogni istante \(t\), ci chiediamo quale quota della popolazione iniziale è ancora attiva, abbonata, non churnata o comunque “sopravvissuta” secondo la definizione scelta.

In statistica questa idea è formalizzata dalla **survival function**:

\[
S(t) = P(T > t)
\]

cioè la probabilità che il tempo fino all'evento sia superiore a \(t\). NIST usa la stessa definizione nella reliability analysis: la survival function è il complemento della distribuzione cumulativa di failure.[^nist-survival]

### Caso: Streamly e il problema nascosto al giorno 21

Streamly è un servizio in abbonamento per corsi video professionali. La dashboard mostra:

- retention D7: 76%;
- retention D30: 58%;
- retention D90: 43%.

Il Product Manager conclude che il principale problema sia nelle prime settimane.

L'analista costruisce invece una curva giornaliera per le ultime sei coorti. Nota un pattern quasi identico: la discesa è moderata fino al giorno 18, poi accelera tra il giorno 19 e il giorno 24.

Il team controlla cosa succede in quel periodo. La prova gratuita dura 21 giorni e la prima fatturazione avviene automaticamente al termine del trial.

Quando la coorte viene divisa tra utenti che hanno completato almeno un corso e utenti che hanno solo guardato video sparsi, le curve divergono nettamente:

- completamento corso prima del giorno 14: retention D45 = 71%;
- nessun corso completato: retention D45 = 29%.

Il problema non è semplicemente “retention bassa”. Il punto critico è **arrivare alla prima fatturazione senza aver sperimentato abbastanza valore**.

### Hazard: dove aumenta il rischio di churn?

La survival curve dice quanti utenti restano. La **hazard rate** aiuta a ragionare su quando aumenta il rischio di uscita, condizionatamente al fatto che l'utente sia ancora presente.

NIST definisce l'hazard rate come il tasso istantaneo di failure per le unità che sono sopravvissute fino al tempo \(t\).[^nist-hazard]

Trasposto in un prodotto digitale, possiamo pensarlo come:

> tra gli utenti ancora attivi oggi, in quali momenti del lifecycle il rischio di churn aumenta maggiormente?

Questa prospettiva cambia la priorità operativa. In Streamly il picco non è al signup. È poco prima della prima fatturazione.

### Censoring: gli utenti che non hanno ancora avuto il tempo di churnare

Un errore molto comune è confrontare coorti con diversa maturità. Una coorte entrata 20 giorni fa non può ancora avere una retention a 90 giorni osservata.

Questo è un caso di **right censoring**: sappiamo che un utente è sopravvissuto almeno fino a oggi, ma non conosciamo ancora il suo futuro.

Per questo, quando si lavora con curve di retention o survival, bisogna distinguere tra utenti che hanno realmente concluso il periodo di osservazione e utenti ancora in corso.

### Cosa deve imparare l'analista

Una curva temporale costringe a smettere di trattare il churn come un numero statico. Fa emergere transizioni, soglie, eventi di lifecycle e momenti di rischio.

E soprattutto ricorda che **il tempo non è solo una colonna del dataset: spesso è parte del meccanismo che vogliamo capire**.

[^nist-survival]: NIST/SEMATECH Engineering Statistics Handbook, *Reliability or survival function*, https://www.itl.nist.gov/div898/handbook/apr/section1/apr122.htm
[^nist-hazard]: NIST/SEMATECH Engineering Statistics Handbook, *Failure (or hazard) rate*, https://www.itl.nist.gov/div898/handbook/apr/section1/apr123.htm
