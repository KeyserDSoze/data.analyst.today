## 5.7 Intuizione bayesiana: aggiornare ciò che crediamo quando arriva nuova evidenza

Il ragionamento bayesiano parte da un'idea semplice: **prima di osservare una nuova informazione abbiamo una certa convinzione; dopo averla osservata, dovremmo aggiornarla**.

In forma compatta:

\[
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
\]

La formula di Bayes permette di invertire una probabilità condizionata e combina tre elementi:

- una probabilità iniziale, o *prior*;
- quanto l'evidenza è compatibile con l'ipotesi, cioè la *likelihood*;
- una probabilità aggiornata, o *posterior*.

NIST presenta la formula di Bayes proprio come un modo per esprimere la probabilità condizionata di un evento in funzione della probabilità inversa e della probabilità di base.[^1]

### Caso realistico: un alert antifrode non significa frode

Riprendiamo un sistema di pagamento.

Supponiamo che:

- lo 0,5% delle transazioni sia realmente fraudolento;
- il sistema segnali il 92% delle frodi;
- il 3% delle transazioni legittime venga segnalato comunque.

Una transazione genera un alert.

Qual è la probabilità che sia davvero una frode?

Partiamo da 100.000 transazioni.

Frodi reali:

\[
100.000 \times 0,005 = 500
\]

Alert corretti:

\[
500 \times 0,92 = 460
\]

Transazioni legittime:

\[
99.500
\]

Falsi positivi:

\[
99.500 \times 0,03 = 2.985
\]

Alert complessivi:

\[
460+2.985=3.445
\]

La probabilità che un alert corrisponda a una frode reale è quindi:

\[
\frac{460}{3.445}\approx13,4\%
\]

L'alert aumenta enormemente il rischio rispetto allo 0,5% iniziale, ma non porta la probabilità al 92%.

Il prior conta.

### Il prior non è un'opinione arbitraria

Nel lavoro analitico un prior può essere basato su:

- storico dello stesso processo;
- dati di un segmento comparabile;
- benchmark;
- esperienza precedente formalizzata;
- una distribuzione volutamente ampia quando abbiamo poca informazione.

Il punto non è “credere” senza dati.

Il punto è riconoscere che raramente partiamo davvero da zero.

### Caso realistico: un nuovo prodotto che parte fortissimo

Una piattaforma subscription lancia un nuovo piano premium.

Nei primi 20 visitatori della landing page, 8 acquistano.

Conversion rate osservato:

\[
40\%
\]

Il product manager propone immediatamente di aumentare il budget media perché il vecchio piano converte intorno al 12%.

L'analista è più prudente.

Venti osservazioni sono poche. Inoltre i primi visitatori provengono da una mailing list di clienti ad alto engagement.

L'evidenza è positiva, ma non sufficiente per comportarsi come se il vero conversion rate fosse certamente 40%.

Il ragionamento bayesiano suggerisce esattamente questo atteggiamento: il dato nuovo aggiorna fortemente le nostre aspettative, ma l'intensità dell'aggiornamento dipende da quanta informazione avevamo prima e da quanta evidenza nuova abbiamo raccolto.

### Evidenza forte ed evidenza debole

Se un processo storico mostra un failure rate dell'1% su due milioni di eventi e in una mattina osserviamo 2 failure su 50 eventi, il 4% osservato merita attenzione, ma non dobbiamo automaticamente dichiarare che il nuovo failure rate è 4%.

Se invece osserviamo 4.000 failure su 100.000 eventi, il nuovo dato ha un peso completamente diverso.

L'evidenza non è soltanto il valore osservato. È anche la sua quantità e affidabilità.

### Bayesian thinking senza fare Bayesian statistics

Un analyst può applicare questa intuizione anche senza costruire un modello bayesiano formale.

Prima di una nuova analisi può scrivere:

- cosa mi aspetto sulla base di ciò che so già?
- quale evidenza mi farebbe cambiare idea?
- quanto è forte la nuova evidenza?
- sto ignorando il base rate?

Queste domande migliorano il ragionamento anche in analisi descrittive normali.

### AI e aggiornamento delle ipotesi

Un LLM può generare dieci spiegazioni plausibili per un'anomalia.

Questo non rende le dieci ipotesi equivalenti.

L'analista deve assegnare priorità sulla base di:

- frequenza storica;
- compatibilità con il dominio;
- evidenza già disponibile;
- costo della verifica;
- capacità dell'ipotesi di spiegare simultaneamente più segnali.

Poi deve aggiornare la propria valutazione quando arrivano nuovi dati.

Usata in questo modo, l'AI aiuta a esplorare lo spazio delle ipotesi; il ragionamento probabilistico impedisce di trattare ogni spiegazione generata come ugualmente plausibile.

### La lezione

La probabilità non è statica.

Quando arriva nuova evidenza, una buona analisi dovrebbe cambiare ciò che riteniamo plausibile.

La domanda non è:

> “Avevo ragione o torto?”

È:

> “Quanto dovrebbe cambiare la mia convinzione alla luce di ciò che ho appena osservato?”

Questo è uno dei passaggi più importanti dal reporting al vero ragionamento analitico.

---

[^1]: NIST/SEMATECH, *Assessing Product Reliability - Bayes Formula*: https://www.itl.nist.gov/div898/handbook/apr/section1/apr1a.htm
