# Capitolo 15 — Dall'analisi all'insight e alla decisione

## 15.0 Un numero interessante non è ancora una decisione

Molte analisi finiscono nel momento sbagliato. Il team trova un pattern, costruisce un grafico e scrive che la conversion mobile è diminuita del 7%. Il numero può essere corretto, ma nessuna scelta è ancora avvenuta.

Una decisione esiste quando qualcuno deve scegliere tra almeno due corsi d'azione, incluso continuare come oggi. È questo il passaggio che ci interessa:

```text
finding
→ decision context
→ alternatives
→ evidence
→ uncertainty / risk
→ trade-offs
→ choice
→ action
→ outcome review
```

Il Capitolo 14 ha chiuso la catena di verifica chiedendo quale claim abbiamo il diritto di sostenere. Qui facciamo il passo successivo: **come trasformiamo quel claim, inevitabilmente incompleto, in una scelta esplicita senza fingere di possedere più certezza di quella disponibile?**

Un *finding* descrive ciò che osserviamo: il churn è salito dal 4,2% al 5,1%. Un *insight* cambia la rappresentazione del problema: quasi tutto il deterioramento è concentrato nei primi 90 giorni e negli account con activation incompleta. Una *recommendation* confronta alternative alla luce di evidenza, costi, rischi e vincoli: testare un intervento di activation sui nuovi account appare preferibile a una campagna di retention sull'intera base. La *decisione* è infine la scelta assunta da un owner: allocare €200k al pilot, partire sul 20% degli account eleggibili e rivalutare dopo sei settimane.

Queste quattro cose sono collegate, ma non sono intercambiabili. In particolare, un insight utile non deve necessariamente spiegare il meccanismo causale definitivo. Se gli errori checkout aumentano del 40% e il 91% del delta è concentrato su un solo PSP, può essere razionale spostare temporaneamente traffico verso un provider alternativo prima di conoscere la root cause completa. Il livello di evidenza necessario dipende anche dal costo, dal blast radius e dalla reversibilità della decisione.

Per la stessa ragione, decidere non significa sempre “fare qualcosa”. Non intervenire, aspettare 24 ore, comprare una specifica informazione, lanciare un pilot, ridurre lo scope o interrompere un progetto sono tutte decisioni. L'analista non deve produrre azione per giustificare il proprio lavoro: deve migliorare la scelta.

### Un aggregato corretto può generare la decisione sbagliata

Consideriamo un caso simulato/composito. Una società subscription osserva il churn small business passare dal 5,6% al 7,2% su una popolazione di 180.000 account. La prima proposta del management è una campagna retention su tutto il segmento, con un costo stimato di circa €1,1M.

L'analisi successiva cambia però la struttura del problema. Il deterioramento è quasi interamente nei primi 90 giorni; il 74% del delta proviene da account con onboarding incompleto; gli account pienamente attivati sono sostanzialmente stabili. Un intervento mirato sull'activation costa circa €190k e Customer Success non ha comunque capacità per contattare l'intera popolazione.

Il finding iniziale era corretto. Era la scelta implicita costruita sopra l'aggregato a essere fragile. Le alternative reali diventano allora:

```text
A — campagna sull'intero segmento
B — intervento onboarding mirato
C — pilot mirato prima di scalare
D — business as usual / nessun intervento immediato
```

Ora possiamo confrontare una decisione, non soltanto commentare un KPI.

### Business as usual è un'alternativa, non il vuoto

Ogni Decision Record importante dovrebbe includere esplicitamente **business as usual / do nothing**. Altrimenti confrontiamo soltanto varianti di intervento e dimentichiamo che anche l'intervento deve guadagnarsi il diritto di esistere.

Il *Green Book 2026* di HM Treasury, pur nel diverso contesto dell'appraisal pubblico, porta il business as usual fino alla shortlist proprio come benchmark rispetto al quale confrontare le altre opzioni. Chiede inoltre di rendere visibili costi, benefici, rischi, incertezze e impatti che non possono essere monetizzati in modo sensato.[^green-book-15]

NASA formula lo stesso principio da un'altra prospettiva. La Decision Analysis serve a caratterizzare e confrontare alternative coerenti con le priorità del decision-maker **dato lo stato di conoscenza disponibile**, includendo costo, performance, schedule e incertezza.[^nasa-da-15] La qualità del lavoro non consiste quindi nel trovare il numero più convincente, ma nel rendere esplicito il passaggio:

```text
objectives
→ alternatives
→ evidence
→ uncertainty / risk
→ trade-offs
→ selection
```

### Il deliverable del capitolo: Decision Record

Il **Decision Record** non è soltanto la memoria di ciò che abbiamo scelto. È il luogo in cui la scelta viene costruita prima che sia presa, quando le alternative e l'incertezza sono ancora visibili.

Una versione iniziale è:

```text
decision:
decision owner:
deadline:
objective:
constraints:

alternatives:
- business as usual
- option A
- option B
- ...

evidence:
key uncertainties:
expected upside:
downside / guardrails:
reversibility:
switching threshold:

recommendation:
why this beats alternatives:
what could change the recommendation:

chosen option:
review date:
outcome metrics:
```

Nelle sezioni successive costruiremo questi campi come parti di un unico ragionamento. Finding, expected value, sensitivity, switching threshold e pre-mortem non saranno tecniche indipendenti: serviranno tutte a rispondere alla stessa domanda, **quanto è robusto il motivo per cui preferiamo un'alternativa alle altre?**

Una buona analisi, a questo punto del libro, non si misura dal numero di grafici, query o modelli prodotti. Si misura da quanto cambia la qualità della scelta: quale alternativa preferiamo, quanto investiamo, chi trattiamo, quanto aspettiamo, quale rischio accettiamo e quale informazione vale la pena comprare prima di impegnarci.

> **Un insight è decision-relevant quando cambia una scelta, una soglia, uno scope, un timing o il livello di fiducia con cui siamo disposti ad agire.**

[^green-book-15]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
[^nasa-da-15]: NASA, *6.8 Decision Analysis*, https://www.nasa.gov/reference/6-8-decision-analysis/
