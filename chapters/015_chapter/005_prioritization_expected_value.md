## 15.4 Expected value e priorità: rendere visibili le assunzioni, non nasconderle nei decimali

Quando più alternative competono per capitale, capacità e attenzione, serve un modo per confrontare valore, probabilità, costo e rischio. L'**expected value** può essere molto utile, a patto di ricordare che è un modello del ragionamento, non una macchina che trasforma automaticamente supposizioni in fatti.

Una forma didattica è:

```text
expected net value
≈ somma(probabilità dello scenario × valore dello scenario)
− costi incrementali
```

Il valore principale della formula è costringerci a dichiarare quali esiti stiamo considerando, da dove arrivano le probabilità, quali costi sono veramente incrementali e quale downside stiamo accettando.

### La priorità non coincide con l'upside più grande

Un prodotto fintech ha cinque iniziative possibili:

| Iniziativa | Upside annuo plausibile | Evidenza | Costo | Time to value | Downside |
|---|---:|---|---:|---|---|
| Ridurre payment failures | €1,8M | forte | €220k | 6 settimane | basso-medio |
| Nuovo referral program | €2,5M | debole | €500k | 4 mesi | medio |
| Migliorare onboarding KYC | €1,1M | forte | €140k | 5 settimane | basso |
| Nuova dashboard merchant | €600k | media | €250k | 3 mesi | basso |
| Pricing optimization | €3,4M | media | €800k | 6 mesi | alto |

Se leggiamo soltanto la colonna dell'upside, pricing sembra il vincitore. Ma payment failures è già localizzato, reversibile, economicamente materiale, tecnicamente vicino alla soluzione e misurabile in poche settimane. Con una squadra limitata, può essere la priorità migliore anche senza avere il numero più grande.

Questo è il primo limite dell'expected value: la decisione vive dentro **time to value, capacity, reversibility ed evidence strength**, non soltanto dentro una stima centrale.

### La probabilità deve avere una provenienza

Supponiamo:

```text
beneficio se funziona: €1M
probabilità di successo: 70%
costo: €200k
```

La scorciatoia produce:

```text
€1M × 70% − €200k = €500k
```

Ma il 70% può provenire da un esperimento precedente, dal base rate di progetti simili, da un forecast calibrato, dal judgment di esperti oppure dalla semplice impressione del proponente. Il formato numerico è identico; la qualità epistemica no.

Per questo il Decision Record conserva anche:

```text
source of probability / confidence:
```

Quando non abbiamo probabilità credibili, è spesso più onesto usare range, scenario analysis, confidence ordinali motivate, break-even e switching values. Sapere che “l'opzione A resta preferibile finché l'uplift supera 1,8%” può essere molto più utile che scrivere “probabilità di uplift 63,7%” senza una base seria.

### Stesso expected value, rischio diverso

Consideriamo:

```text
Opzione A
50%: +€2M
50%: -€1M
expected: +€0,5M

Opzione B
100%: +€0,5M
expected: +€0,5M
```

Le due opzioni non sono equivalenti per un'organizzazione che non può assorbire una perdita da €1M. Maximum plausible loss, liquidità, customer harm, reputazione, irreversibilità, concentrazione del rischio e downside correlato con altri progetti possono dominare l'EV medio.

Lo stesso vale per vincoli e guardrail. Un progetto con EV +€3M non resta in shortlist se viola un requisito regolatorio non negoziabile o richiede una capacità operativa che non esiste.

### Il valore deve incorporare l'azione realmente disponibile

Un modello identifica 40.000 clienti ad alto rischio di churn; Customer Success può intervenire su 2.000. La decisione non è “quali clienti hanno il rischio più alto?”, ma:

> **quali 2.000 interventi hanno il miglior valore incrementale atteso entro la capacità disponibile?**

Questo collega i Capitoli 8–10 al problema decisionale senza confonderli: risk non è treatment effect, score non è policy e un vantaggio predittivo non genera valore se l'azione downstream non può essere eseguita o non cambia l'outcome.

Anche il portafoglio conta. Cinque iniziative individualmente attraenti possono creare insieme dipendenza dalla stessa piattaforma, saturazione dello stesso team, concentrazione sullo stesso mercato o downside correlato. Il Decision Record può quindi annotare:

```text
shared dependencies:
capacity consumed:
correlated risks:
projects displaced:
```

### Business as usual ha un valore e un costo

`Do nothing` non è zero. Ha benefici, costi, rischi, optionality e costo dell'inazione. Se il problema vale €50k l'anno e la soluzione costa €700k, business as usual può dominare. Se il costo dell'inazione cresce di €100k a settimana, il timing diventa parte del valore atteso.

Il *Green Book 2026* tratta le metriche sintetiche come supporto all'appraisal, non come criterio meccanico unico: costi, benefici, rischi, incertezze, impatti distributivi e non monetizzabili restano parte del giudizio sull'opzione preferita.[^green-book-ev]

Per una shortlist aziendale possiamo usare una Decision Scorecard senza trasformarla in un punteggio artificiale:

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

La tabella serve a rendere visibile **perché le alternative differiscono**, non a produrre automaticamente “82,4 punti”.

Nel Decision Record conserviamo:

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

> **Il valore atteso è potente quando rende esplicita l'incertezza. Diventa pericoloso quando trasforma assunzioni fragili in decimali che sembrano fatti.**

[^green-book-ev]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
