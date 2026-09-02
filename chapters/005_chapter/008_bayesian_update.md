## 5.7 Intuizione bayesiana: aggiornare ciò che riteniamo plausibile

Il ragionamento bayesiano parte da un'idea semplice:

> **prima di osservare una nuova evidenza abbiamo una certa valutazione; dopo averla osservata dovremmo aggiornarla in modo proporzionato alla forza dell'evidenza.**

La formula di Bayes è:

`P(A|B) = P(B|A) × P(A) / P(B)`

Combina:

- una probabilità iniziale, o **prior**;
- quanto l'evidenza osservata è compatibile con l'ipotesi, la **likelihood**;
- la probabilità aggiornata, o **posterior**.

NIST presenta la formula di Bayes come relazione tra una probabilità condizionata, la probabilità inversa e la probabilità di base.[^nist-bayes]

La sezione 5.2 ci ha già mostrato perché la base rate conta. Qui facciamo il passo successivo: usiamo nuove evidenze per **rivedere una valutazione precedente**, invece di ripartire ogni volta da zero.

### Caso simulato/composito — Un crollo della conversione e quattro ipotesi

Una piattaforma e-commerce vede il checkout conversion rate scendere dal 4,1% al 3,2% in meno di un'ora.

Il team formula quattro ipotesi:

1. problema di tracking;
2. cambiamento nel mix di traffico;
3. bug della nuova release;
4. problema del payment provider.

Negli ultimi 40 incidenti con un pattern iniziale simile, le cause erano state approssimativamente:

| Causa | Frequenza storica |
|---|---:|
| Tracking / telemetry | 40% |
| Traffic mix / campagne | 25% |
| Product bug | 20% |
| Payment provider | 15% |

Queste frequenze non sono verità universali. Sono un possibile **prior operativo**: prima di ulteriori evidenze, tracking è semplicemente una causa storicamente più frequente.

### Prima evidenza: gli ordini reali sono scesi

Finance e il database transazionale confermano che non è soltanto un problema di tracking.

L'ipotesi 1 perde molto peso.

Non è necessario dire che la sua probabilità diventa zero. Ma la nuova evidenza è poco compatibile con “solo telemetry”.

### Seconda evidenza: il problema è quasi esclusivamente su iOS

Web e Android sono stabili. Su iOS il calo è forte.

L'ipotesi di traffic mix generale diventa meno plausibile. Product bug sale di priorità.

### Terza evidenza: il calo inizia con la versione 8.42

La segmentazione per app version mostra:

- iOS 8.41: conversione normale;
- iOS 8.42: forte perdita nel passaggio payment → confirmation.

Ora l'evidenza è molto più compatibile con una regressione specifica della release che con un problema generale del payment provider.

Il team controlla i log e trova un errore nella gestione delle carte salvate introdotto proprio nella 8.42.

### Questo è Bayesian thinking anche senza calcolare il posterior

Nel caso non abbiamo costruito un modello bayesiano completo con distribuzioni formali.

Abbiamo però seguito la logica:

**prior → nuova evidenza → rivalutazione relativa delle ipotesi → nuova evidenza → ulteriore aggiornamento**.

È una disciplina molto diversa da:

> “Ho avuto una prima intuizione e ora cerco dati che la confermino.”

Un buon aggiornamento deve consentire a un'ipotesi favorita inizialmente di perdere peso quando i dati la contraddicono.

### Il prior non è un'opinione resa matematica

Un prior può derivare da:

- storico dello stesso processo;
- dati di segmenti comparabili;
- risultati di studi precedenti;
- conoscenza di dominio formalizzata;
- una distribuzione volutamente ampia quando sappiamo poco.

Il prior deve essere **difendibile e aggiornabile**.

Se scegliamo un prior soltanto perché rende il risultato finale più vicino a ciò che desideriamo, non stiamo usando Bayes per imparare: lo stiamo usando per decorare una conclusione già scelta.

### Evidenza nuova: valore osservato e quantità di informazione

Supponiamo che un nuovo piano abbia conversion rate storico atteso vicino al 12%.

Nei primi 20 visitatori osserviamo 8 acquisti: 40%.

È un segnale interessante, ma venti osservazioni contengono poca informazione. Inoltre potrebbero provenire da early adopter molto selezionati.

Se osserviamo invece 8.000 acquisti su 20.000 visitatori comparabili, la stessa percentuale del 40% ha un peso completamente diverso.

Quindi una buona domanda non è soltanto:

> “Qual è il dato nuovo?”

ma:

> **“Quanta informazione nuova contiene rispetto a ciò che sapevamo già?”**

### Bayesian thinking e AI

Un sistema AI può generare rapidamente venti possibili spiegazioni di un'anomalia.

La generazione di ipotesi, però, non assegna loro la stessa plausibilità.

L'analista deve usare:

- frequenza storica;
- compatibilità con il dominio;
- evidenza disponibile;
- capacità esplicativa;
- costo e velocità della verifica;

per decidere quali ipotesi testare prima e come aggiornarle.

Questo collega il Capitolo 5 al principio di **Al timone**: l'AI può ampliare lo spazio delle ipotesi; la responsabilità di pesare evidenza e revisione delle convinzioni rimane umana.

### La domanda finale

Il ragionamento bayesiano non chiede:

> “Avevo ragione o torto fin dall'inizio?”

Chiede:

> **“Data ciò che sapevo prima e ciò che ho osservato adesso, quanto deve cambiare ciò che considero plausibile?”**

È una delle competenze più profonde dell'analisi: essere abbastanza strutturati da avere un'ipotesi e abbastanza disciplinati da cambiarla.

[^nist-bayes]: NIST/SEMATECH, *Assessing Product Reliability — Bayes Formula*: https://www.itl.nist.gov/div898/handbook/apr/section1/apr1a.htm
