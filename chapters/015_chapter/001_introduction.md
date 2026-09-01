# Capitolo 15 — Dall'analisi all'insight e alla decisione

## 15.0 Un numero interessante non è ancora una decisione

Molte analisi finiscono nel momento sbagliato.

Il team trova un pattern, costruisce un grafico e scrive:

> “La conversion mobile è diminuita del 7%.”

Il numero può essere corretto.

Ma nessuna scelta è ancora avvenuta.

Una decisione esiste quando qualcuno deve scegliere **tra almeno due corsi d'azione**, incluso continuare come oggi.

```text
finding
→ decision context
→ alternatives
→ evidence
→ uncertainty/risk
→ trade-offs
→ choice
→ action
→ outcome review
```

Questo capitolo riguarda il passaggio più importante e più sottovalutato dell'analytics:

> **trasformare evidenza incompleta in una scelta esplicita senza fingere di avere più certezza di quella disponibile.**

### Finding, insight, recommendation e decisione

Usiamo quattro parole con ruoli differenti.

**Finding**

Che cosa osserviamo?

> “Il churn è salito dal 4,2% al 5,1%.”

**Insight**

Quale parte del finding cambia la comprensione del problema?

> “Quasi tutto il deterioramento è concentrato nei primi 90 giorni e negli account con activation incompleta.”

**Recommendation**

Quale alternativa appare preferibile date evidenza, costi, rischi e vincoli?

> “Testare un intervento di activation sui nuovi account è preferibile a una campagna di retention sull'intera base.”

**Decision**

Quale alternativa viene effettivamente scelta, da chi e con quali condizioni?

> “Allocare €200k al pilot, partire sul 20% degli account eleggibili e rivalutare dopo sei settimane.”

Le quattro cose possono essere collegate, ma non sono intercambiabili.

### Un insight non deve necessariamente “spiegare la causa”

Un insight utile può cambiare una decisione anche senza identificare il meccanismo causale definitivo.

Esempio:

```text
finding:
errori checkout +40%

insight:
91% del delta è concentrato su un solo PSP

decision implication:
spostare temporaneamente traffico verso provider alternativo
```

Possiamo avere evidenza sufficiente per una mitigazione reversibile anche se la root cause tecnica non è ancora nota.

Questo evita un errore frequente:

> rimandare ogni decisione finché non possediamo una spiegazione perfetta.

Il livello di evidenza necessario dipende dalla decisione.

### Una decisione non è “fare qualcosa”

Anche queste sono decisioni:

- non intervenire;
- aspettare 24 ore;
- raccogliere un dato specifico;
- fare un pilot;
- ridurre lo scope;
- scegliere un'opzione reversibile;
- interrompere un progetto.

L'analista non deve produrre azione per giustificare il proprio lavoro.

Deve migliorare la scelta.

### Caso simulato/composito — il churn small business

> **Nota:** caso costruito a fini didattici.

Una società subscription osserva:

```text
churn small business:
5,6% → 7,2%

population:
180.000 account
```

La prima proposta del management è:

> “Facciamo una campagna retention su tutti i clienti small business.”

Costo stimato: circa €1,1M.

L'analisi successiva mostra:

- il deterioramento è quasi interamente nei primi 90 giorni;
- il 74% del delta proviene da account con onboarding incompleto;
- gli account pienamente attivati sono sostanzialmente stabili;
- un intervento mirato sull'activation costa circa €190k;
- il team Customer Success non ha capacità per contattare tutta la popolazione.

Il finding iniziale era corretto.

La prima raccomandazione era però costruita sull'aggregato sbagliato.

Le alternative reali diventano:

```text
A — campagna sull'intero segmento
B — intervento onboarding mirato
C — pilot mirato prima di scalare
D — business as usual / nessun intervento immediato
```

Ora possiamo decidere.

### Il benchmark “do nothing”

Ogni Decision Record importante dovrebbe includere esplicitamente:

**business as usual / do nothing**.

Se non lo facciamo, rischiamo di confrontare soltanto varianti di intervento e dimenticare che l'intervento stesso deve guadagnarsi il diritto di esistere.

Il Green Book 2026 di HM Treasury, guida ufficiale UK per l'appraisal di alternative, richiede di generare opzioni reali e porta il **business as usual** fino alla shortlist come benchmark di confronto. Richiede inoltre di considerare costi, benefici, rischi, incertezze e alternative non puramente monetarie.

Fonte: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

Il contesto pubblico è diverso da quello di un team analytics aziendale, ma il principio è generale:

> **una raccomandazione non è forte perché ha molti numeri; è forte quando ha battuto alternative credibili.**

### Risk-informed decision making

NASA distingue il risk management operativo dal **Risk-Informed Decision Making**, usato per informare scelte tra alternative con dati, obiettivi, rischi e incertezza.

Fonte: https://www.nasa.gov/reference/6-4-technical-risk-management/

Anche qui il settore è diverso, ma il pattern è utile:

```text
objectives
→ alternatives
→ evidence
→ uncertainty/risk
→ trade-off
→ selection
```

È la stessa struttura che useremo nel Decision Record.

### Il deliverable del capitolo: Decision Record

Il Decision Record non è soltanto una memoria di ciò che abbiamo deciso.

È il posto in cui **la scelta viene costruita prima di essere presa**.

Template iniziale:

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

Nelle sezioni successive lo costruiremo pezzo per pezzo.

### Il criterio fondamentale

Una buona analisi non si misura dal numero di grafici, query o modelli prodotti.

Si misura da quanto modifica la qualità della scelta:

- quale alternativa scegliamo;
- quanto investiamo;
- chi trattiamo;
- quanto aspettiamo;
- quale rischio accettiamo;
- quale informazione decidiamo di comprare prima di impegnarci.

> **Un insight è decision-relevant quando cambia una scelta, una soglia, uno scope, un timing o il livello di fiducia con cui siamo disposti ad agire.**
