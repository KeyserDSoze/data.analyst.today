## 15.4 Expected value e priorità: utile quando illumina le assunzioni, pericoloso quando le nasconde

Quando abbiamo più alternative, serve un modo per confrontare valore, probabilità, costo e rischio.

L'**expected value** può essere molto utile.

Ma una formula semplice non rende automaticamente comparabili opzioni complesse.

Una versione didattica è:

```text
expected net value
≈ somma(probabilità dello scenario × valore dello scenario)
− costi incrementali
```

Il punto non è ottenere un euro “scientifico”.

È costringerci a dichiarare:

- quali esiti stiamo considerando;
- quali probabilità stiamo assumendo;
- quali costi includiamo;
- quale downside stiamo accettando.

### Caso simulato/composito — cinque iniziative, una sola squadra

Un prodotto fintech ha cinque iniziative possibili:

| Iniziativa | Upside annuo plausibile | Evidenza | Costo | Time to value | Downside |
|---|---:|---|---:|---|---|
| Ridurre payment failures | €1,8M | forte | €220k | 6 settimane | basso-medio |
| Nuovo referral program | €2,5M | debole | €500k | 4 mesi | medio |
| Migliorare onboarding KYC | €1,1M | forte | €140k | 5 settimane | basso |
| Nuova dashboard merchant | €600k | media | €250k | 3 mesi | basso |
| Pricing optimization | €3,4M | media | €800k | 6 mesi | alto |

Guardando soltanto all'upside, pricing sembra vincere.

Ma il team ha capacità limitata e il problema payment failures è:

- già localizzato;
- reversibile;
- economicamente materiale;
- tecnicamente vicino alla soluzione;
- misurabile in poche settimane.

La priorità può quindi essere payment failures anche se non ha il numero più grande nella colonna “opportunità”.

### Probability × impact è un modello, non un fatto

Supponiamo:

```text
beneficio se funziona: €1M
probabilità di successo: 70%
costo: €200k
```

Una scorciatoia produce:

```text
€1M × 70% − €200k = €500k
```

Ma da dove arriva il 70%?

Potrebbe derivare da:

- un esperimento precedente;
- base rate di progetti simili;
- forecast calibrato;
- judgment di esperti;
- semplice impressione del proponente.

Il numero può avere lo stesso formato e qualità epistemica completamente diversa.

Per questo il Decision Record deve registrare anche **source of probability / confidence**.

### Quando non abbiamo probabilità credibili

Non sempre è sensato assegnare 23%, 47% e 71% a scenari che conosciamo poco.

Alternative più oneste:

- range;
- scenario analysis;
- ordinal confidence `low / medium / high` con motivazione;
- break-even analysis;
- switching values;
- dominance analysis.

È spesso meglio sapere:

> “L'opzione A resta preferibile finché l'uplift supera 1,8%.”

che fingere:

> “La probabilità di uplift è 63,7%.”

### Downside asimmetrico

Due opzioni possono avere lo stesso expected value e profili di rischio molto diversi.

```text
Opzione A
50%: +€2M
50%: -€1M
expected: +€0,5M

Opzione B
100%: +€0,5M
expected: +€0,5M
```

Non sono equivalenti per un'organizzazione che non può assorbire una perdita da €1M.

Dobbiamo considerare:

- maximum plausible loss;
- cash/liquidity constraint;
- customer harm;
- reputazione;
- irreversibilità;
- concentrazione del rischio;
- correlated downside con altri progetti.

L'expected value è una dimensione della decisione, non l'intera decisione.

### Guardrail e vincoli possono dominare il valore atteso

Se una opzione viola un vincolo non negoziabile, non viene salvata da un EV positivo.

Esempio:

```text
EV stimato: +€3M
ma
probabilità di violare requisito regolatorio non accettabile
```

La scelta è fuori shortlist finché quel rischio non viene mitigato.

Allo stesso modo, un progetto può avere valore positivo ma richiedere capacità che non esiste.

### Expected value e capacità operativa

Un modello identifica 40.000 clienti ad alto rischio di churn.

Customer Success può intervenire su 2.000.

La decisione non è:

> “Quali clienti hanno il rischio più alto?”

È:

> “Quali 2.000 interventi hanno il miglior valore incrementale atteso entro la capacità disponibile?”

Questa distinzione collega il Capitolo 15 ai Capitoli 8–10 senza ripeterli:

- risk ≠ treatment effect;
- score ≠ decision;
- expected value deve includere **azione disponibile e capacità reale**.

### Portfolio effect: le decisioni non vivono sempre isolate

Cinque progetti individualmente interessanti possono insieme creare:

- troppo rischio sullo stesso team;
- dipendenza dalla stessa piattaforma;
- concentrazione sullo stesso mercato;
- picco di change management;
- correlazione del downside.

Quindi una priorità può cambiare quando la guardiamo dentro il portafoglio.

Il Decision Record può annotare:

```text
shared dependencies:
capacity consumed:
correlated risks:
projects displaced:
```

### Do nothing deve avere un valore

Anche business as usual ha:

- benefici;
- costi;
- rischi;
- optionality;
- costo dell'inazione.

Se il problema costa €50k l'anno e la soluzione richiede €700k, “non fare nulla per ora” può dominare.

Se invece il costo dell'inazione cresce di €100k a settimana, il timing diventa parte dell'expected value.

### Caso pubblico documentato — la preferred option non è una gara a un solo numero

Il Green Book 2026 di HM Treasury richiede una valutazione complessiva di costi, benefici, rischi e incertezze e chiarisce che metriche sintetiche non devono essere usate meccanicamente come unico criterio per selezionare l'opzione preferita. Include inoltre analisi distributive e impatti non monetizzabili quando rilevanti.

Fonte: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

Il principio è utile anche fuori dall'appraisal pubblico:

> **una metrica di valore serve a strutturare il trade-off, non a sostituire la responsabilità della scelta.**

### Decision Scorecard senza falsa precisione

Per una shortlist possiamo usare una tabella come questa:

| Dimensione | A | B | C |
|---|---|---|---|
| expected economic value | | | |
| evidence strength | | | |
| downside severity | | | |
| reversibility | | | |
| time to value | | | |
| capacity fit | | | |
| strategic fit | | | |
| non-monetizable impact | | | |
| key switching assumption | | | |

Non sommiamo automaticamente tutto in “82,4 punti”.

La tabella serve a rendere visibile **perché le alternative differiscono**.

### Campo del Decision Record

```text
expected outcomes:
probability/confidence source:
expected value if meaningful:
plausible downside:
non-monetizable impacts:
capacity constraint:
portfolio/opportunity cost:
business-as-usual cost:
```

### Regola operativa

Usa expected value quando:

- gli esiti sono abbastanza definiti;
- le probabilità o range hanno una base difendibile;
- i costi sono realmente incrementali;
- il downside è rappresentato.

Preferisci switching values o scenari quando le probabilità puntuali sarebbero soprattutto decorazione numerica.

> **Il valore atteso è potente quando rende esplicita l'incertezza. Diventa pericoloso quando trasforma supposizioni fragili in decimali che sembrano fatti.**
