## 5.2 Probabilità condizionata: il rischio cambia quando cambia il contesto

Molte probabilità utili nel business non sono marginali, ma **condizionate**.

Non chiediamo soltanto:

> “Qual è la probabilità di churn?”

Chiediamo:

> “Qual è la probabilità di churn **dato che** il cliente non ha effettuato login negli ultimi 21 giorni?”

Oppure:

> “Qual è la probabilità di reso **dato che** il prodotto appartiene alla categoria calzature?”

La probabilità condizionata di `A` dato `B` si può leggere così:

> **tra tutti i casi in cui B è vero, quanto spesso osserviamo A?**

La formula è:

`P(A|B) = P(A ∩ B) / P(B)`

quando `P(B) > 0`.

Il calcolo è semplice. La parte difficile è ricordare che **cambiando il denominatore cambia la domanda**.

### Caso simulato/composito — Il churn che sembrava diffuso

Una società SaaS B2B ha 18.400 clienti attivi. Il churn complessivo sembra distribuito su tutta la base.

Prima di costruire un modello predittivo, l'analista segmenta i clienti in base all'attività degli ultimi 30 giorni.

| Attività ultimi 30 giorni | Clienti | Churn nei 90 giorni successivi |
|---|---:|---:|
| Alta | 6.900 | 2,4% |
| Media | 7.100 | 6,8% |
| Bassa | 3.200 | 17,9% |
| Nessuna attività | 1.200 | 41,5% |

Il rischio cambia radicalmente quando conosciamo il livello di utilizzo.

Possiamo quindi dire:

`P(Churn | Nessuna attività) ≈ 41,5%`

mentre:

`P(Churn | Attività alta) ≈ 2,4%`.

Questo non dimostra che la bassa attività **causi** il churn. Può essere un segnale precoce di insoddisfazione, una conseguenza di un problema già in corso o entrambe le cose.

Ma la probabilità condizionata ha comunque trasformato un rischio aggregato in una struttura molto più informativa.

### La probabilità inversa è un'altra domanda

Supponiamo che 1.000 clienti abbiano aperto almeno tre ticket in un mese e che 180 facciano churn nei 90 giorni successivi.

Allora:

`P(Churn | 3+ ticket) = 18%`.

Supponiamo anche che, tra tutti i 900 clienti che hanno fatto churn, 180 avessero aperto almeno tre ticket.

Allora:

`P(3+ ticket | Churn) = 20%`.

Le due frasi possono sembrare quasi equivalenti in una riunione. Non lo sono.

- “Il 20% dei churner aveva molti ticket” guarda **indietro partendo dai churner**.
- “Il 18% dei clienti con molti ticket farà churn” guarda **in avanti partendo dai clienti con ticket**.

Confondere `P(A|B)` con `P(B|A)` è uno degli errori più comuni nel ragionamento probabilistico.

### Il base-rate problem: un alert accurato può avere molti falsi positivi

Consideriamo un caso simulato di fraud detection.

La frode reale riguarda lo **0,4%** delle transazioni.

Un sistema ha:

- sensibilità: 95%;
- false-positive rate: 2%.

Una transazione viene segnalata. Quanto è probabile che sia davvero fraudolenta?

L'intuizione può suggerire un valore vicino al 95%.

Usiamo invece **frequenze naturali** su 100.000 transazioni:

| Gruppo | Casi | Segnalati |
|---|---:|---:|
| Frodi reali | 400 | 380 |
| Transazioni legittime | 99.600 | 1.992 |
| **Totale alert** |  | **2.372** |

Tra 2.372 alert, soltanto 380 sono frodi reali.

Quindi:

`P(Frode | Alert) ≈ 380 / 2.372 ≈ 16%`.

Il sistema può avere un'ottima capacità di intercettare le frodi e, allo stesso tempo, produrre molti falsi positivi perché la frode è molto rara.

Questo è il **base-rate problem**.

### Perché le frequenze naturali aiutano

Percentuali come “sensibilità 95%” e “false-positive rate 2%” sono corrette ma facili da combinare male mentalmente.

Tradurre il problema in un gruppo concreto — per esempio 100.000 transazioni — rende visibili i denominatori.

È una tecnica molto utile anche fuori dalla frode:

- screening;
- alert di sicurezza;
- churn prediction;
- lead scoring;
- anomaly detection;
- sistemi di qualità.

### Un ponte verso Bayes e i modelli predittivi

La base rate è ciò che il ragionamento bayesiano formalizzerà nella sezione 5.7: una nuova evidenza deve essere interpretata insieme alla probabilità di partenza.

Nel Capitolo 10 ritroveremo lo stesso problema attraverso precision, recall, calibration e scelta della soglia.

Per ora basta una regola mentale:

> **Ogni volta che qualcuno dice “tra quelli che fanno X, molti fanno Y”, scrivi esplicitamente `P(Y|X)` e controlla che non stia usando come prova la probabilità inversa `P(X|Y)`.**
