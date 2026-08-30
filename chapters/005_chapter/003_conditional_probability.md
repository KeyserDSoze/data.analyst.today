## 5.2 Probabilità condizionata: il contesto cambia il rischio

Molte probabilità utili nel business sono **condizionate**.

Non chiediamo semplicemente:

**“Qual è la probabilità di churn?”**

Chiediamo:

**“Qual è la probabilità di churn dato che il cliente non ha effettuato login negli ultimi 21 giorni?”**

Oppure:

**“Qual è la probabilità di reso dato che il prodotto appartiene alla categoria calzature?”**

La probabilità condizionata di \(A\) dato \(B\) si scrive:

\[
P(A|B)=\frac{P(A \cap B)}{P(B)}
\]

quando \(P(B)>0\).

La formula dice una cosa molto intuitiva: restringiamo il nostro universo ai casi in cui \(B\) è vero e, dentro quel sottoinsieme, misuriamo quanto spesso avviene \(A\).

### Caso realistico: il churn che sembrava casuale

Un'azienda SaaS B2B ha 18.400 clienti attivi e un churn annualizzato intorno al 9%.

Il management considera il churn relativamente diffuso e chiede al team analytics di costruire un modello predittivo.

Prima del modello, l'analista costruisce una tabella semplice.

Divide i clienti in base all'attività degli ultimi trenta giorni:

| Attività ultimi 30 giorni | Clienti | Churn nei 90 giorni successivi |
|---|---:|---:|
| Alta | 6.900 | 2,4% |
| Media | 7.100 | 6,8% |
| Bassa | 3.200 | 17,9% |
| Nessuna attività | 1.200 | 41,5% |

Il churn complessivo nasconde una struttura enorme.

La probabilità di churn cambia radicalmente quando conosciamo il livello di utilizzo.

In particolare:

\[
P(Churn|Nessuna\ attività) \approx 41,5\%
\]

mentre:

\[
P(Churn|Alta\ attività) \approx 2,4\%
\]

Il management non ha ancora un modello sofisticato, ma ha già una leva operativa molto più utile: monitorare il deterioramento dell'engagement.

### Il denominatore cambia

Supponiamo che 1.000 clienti abbiano aperto almeno tre ticket di supporto in un mese e che 180 di loro abbiano poi churnato.

Allora:

\[
P(Churn|3+\ ticket)=18\%
\]

Ma se 180 clienti churnati su 900 totali avevano tre o più ticket, allora:

\[
P(3+\ ticket|Churn)=20\%
\]

Le due probabilità non sono la stessa cosa.

Questo è uno degli errori più frequenti anche nelle conversazioni manageriali.

“Il 20% dei churner aveva molti ticket” non implica che “chi ha molti ticket ha il 20% di probabilità di churn”.

Il denominatore è diverso.

### Il problema della base rate

Immaginiamo un sistema che identifica transazioni potenzialmente fraudolente.

La frode reale riguarda soltanto lo 0,4% delle transazioni.

Il sistema ha:

- sensibilità del 95%;
- tasso di falsi positivi del 2%.

Una transazione viene segnalata.

Quanto è probabile che sia realmente fraudolenta?

L'intuizione può suggerire una probabilità vicina al 95%.

Ma consideriamo 100.000 transazioni.

Frodi reali: 400.

Il sistema identifica correttamente circa 380 di queste.

Transazioni legittime: 99.600.

Il 2% viene segnalato erroneamente: circa 1.992 transazioni.

Totale segnalazioni:

\[
380+1.992=2.372
\]

La quota di frodi reali tra le segnalazioni è quindi circa:

\[
\frac{380}{2.372}\approx16\%
\]

Un alert può essere molto informativo e allo stesso tempo avere una precisione apparentemente bassa, semplicemente perché l'evento di partenza è raro.

Questo è il **base-rate problem**.

### Perché è importante per l'AI e i modelli predittivi

Gli stessi errori compaiono quando valutiamo modelli di machine learning.

Un modello può avere accuracy del 99% e risultare quasi inutile se l'evento che vogliamo individuare avviene nello 0,5% dei casi.

Per questo non basta chiedere:

**“Quanto è accurato il modello?”**

Dobbiamo capire:

- prevalenza dell'evento;
- falsi positivi;
- falsi negativi;
- precision e recall;
- costo economico delle due tipologie di errore.

La probabilità condizionata non è quindi un capitolo preparatorio alla statistica. È già un modo operativo di pensare.

### Regola mentale

Ogni volta che leggiamo una frase del tipo:

> “Tra i clienti che fanno X, succede spesso Y”

proviamo a scriverla esplicitamente come:

\[
P(Y|X)
\]

Poi chiediamoci se qualcuno sta, volontariamente o meno, trasformandola nella probabilità inversa:

\[
P(X|Y)
\]

Sono domande diverse.
