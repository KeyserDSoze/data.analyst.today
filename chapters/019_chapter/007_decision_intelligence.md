# 19.6 Decision intelligence: dal dato alla qualità della decisione

Se una parte crescente dell'esecuzione tecnica può essere delegata a sistemi AI, il valore dell'analista tende a spostarsi ancora di più verso la qualità del processo decisionale.

Questo significa che il futuro del Data Analyst non è semplicemente “fare analytics più velocemente”.

È contribuire a sistemi che collegano in modo esplicito:

**domanda → evidenza → alternative → trade-off → decisione → azione → feedback**

Questa idea viene spesso ricondotta al concetto di **decision intelligence**.

Il termine può essere usato in modi diversi, ma per questo libro ci interessa una definizione operativa: progettare e migliorare il modo in cui un'organizzazione prende decisioni usando dati, modelli, esperimenti, conoscenza del dominio e feedback.

## Dal reporting alla decisione

Un sistema di reporting risponde bene a domande come:

- quanto abbiamo venduto?
- quanto è il churn?
- come sta andando la conversione?
- dove stanno aumentando i costi?

Un sistema orientato alla decisione deve andare oltre:

- quali opzioni abbiamo?
- quale decisione cambia davvero in funzione di questo dato?
- quali conseguenze ci aspettiamo?
- quale rischio accettiamo?
- cosa osserviamo dopo l'azione?
- quando cambiamo idea?

La differenza è sostanziale.

Una dashboard può mostrare perfettamente un problema e non aiutare affatto a decidere.

## Caso realistico: il churn è al 7,8%. E quindi?

Una società SaaS monitora il churn mensile.

La dashboard mostra:

- churn: 7,8%;
- target: 6,5%;
- segmento Enterprise: 4,1%;
- SMB: 10,9%;
- clienti con basso product usage: 18,3%.

L'analisi è corretta.

Ma il management continua a chiedere:

> “Che cosa dobbiamo fare?”

Un approccio di decision intelligence ristruttura il problema.

Prima identifica le azioni disponibili:

1. customer-success call;
2. onboarding aggiuntivo;
3. sconto;
4. technical review;
5. nessun intervento.

Poi associa a ciascuna azione:

- costo;
- capacità disponibile;
- probabilità di successo;
- effetto incrementale atteso;
- valore economico del cliente;
- rischio di effetti collaterali.

A quel punto il problema non è più “chi ha churn risk alto?”.

Diventa:

> **Su quali clienti, con quale intervento, il valore atteso dell'azione supera il costo e il rischio?**

Questa è una trasformazione decisiva.

## Prediction non è decision

Un modello può stimare:

\[
P(Churn \mid X) = 0.82
\]

Ma questo non dice ancora se dobbiamo intervenire.

Per decidere servono almeno altre quantità:

- valore economico del cliente;
- costo dell'intervento;
- probabilità che l'intervento cambi davvero il comportamento;
- capacità operativa;
- effetti collaterali.

Una rappresentazione semplificata potrebbe essere:

\[
EV(intervento) = P(successo\ incrementale) \times valore\ salvato - costo\ intervento
\]

Il cliente con churn risk più alto non è necessariamente quello con il più alto expected value dell'intervento.

## L'AI rende questa distinzione più importante

Un agente può generare in pochi secondi:

- segmentazioni;
- propensity scores;
- forecast;
- scenari;
- raccomandazioni.

Proprio perché produrre alternative diventa facile, aumenta il valore di chi sa costruire un **sistema di decisione**.

Il compito dell'analista diventa sempre meno:

> “Posso produrre questa analisi?”

e sempre più:

> “Quale decisione deve migliorare, quali evidenze servono e come sapremo se la decisione è stata buona?”

## Decision intelligence e feedback loop

Un'organizzazione matura non considera la decisione come punto finale.

La tratta come una nuova fonte di dati.

Dopo una decisione bisogna osservare:

- quale azione è stata scelta;
- per chi;
- con quali condizioni;
- quale risultato è seguito;
- quali assunzioni erano corrette;
- quali erano sbagliate.

Questo crea un ciclo:

**Decisione → Azione → Outcome → Apprendimento → Decisione successiva**

Nel tempo il sistema non migliora soltanto i modelli.

Migliora il modo in cui l'organizzazione decide.

## Il Data Analyst come designer del processo decisionale

Questo ruolo richiede competenze che il libro ha già costruito:

- business understanding;
- semantica;
- probabilità;
- causalità;
- forecasting;
- experimentation;
- unit economics;
- comunicazione;
- governance;
- AI orchestration.

Non significa che ogni analista debba diventare un teorico delle decisioni.

Significa riconoscere che il prodotto finale dell'analytics non è il grafico.

È una decisione migliore.

> **Quando la produzione di analisi diventa economica, la progettazione delle decisioni diventa una delle competenze più preziose.**
