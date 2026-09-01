## 15.2 Dall'insight alla raccomandazione: non difendere un'idea, confrontare alternative

Una raccomandazione debole spesso nasce così:

```text
abbiamo trovato un problema
→ abbiamo immaginato una soluzione
→ abbiamo stimato il beneficio della soluzione
→ raccomandiamo la soluzione
```

Manca il passaggio più importante:

> **rispetto a quali alternative?**

Una raccomandazione professionale non è un business case costruito per difendere la prima idea emersa.

È il risultato di un **option appraisal**.

### Partire dall'obiettivo, non dalla soluzione

Problema:

> checkout abandonment elevato quando compare il costo di spedizione.

Obiettivo:

> aumentare contribution margin dagli utenti che raggiungono il checkout senza peggiorare economics e customer experience.

Possibili alternative:

```text
A — business as usual
B — free shipping universale sopra €40
C — free shipping solo per segmenti ad alto rischio di abbandono
D — soglia differenziata per margine/categoria
E — ridurre tariffa ma non azzerarla
F — testare messaggio e trasparenza prima del checkout
```

Ora il problema non è più “free shipping sì/no?”.

È scegliere il miglior compromesso tra alternative reali.

### Caso simulato/composito — la free shipping che distrugge valore

Un retailer osserva che il 21% degli utenti che abbandonano il checkout lo fa dopo aver visto il costo di spedizione.

Una prima analisi propone free shipping sopra €40.

Stime iniziali:

- +2,4 punti percentuali di conversion;
- circa 31.000 ordini incrementali annui;
- contribution margin prima della shipping subsidy: €18 per ordine;
- costo medio shipping sovvenzionato: €6,20.

La prima presentazione enfatizza:

```text
31.000 × €18 ≈ €558k
```

Ma il costo della policy non ricade soltanto sui nuovi ordini.

Se centinaia di migliaia di ordini che sarebbero avvenuti comunque ricevono la sovvenzione, il trasferimento di margine agli ordini non incrementali può superare il beneficio.

Il punto non è trovare il calcolo “giusto” in astratto.

È distinguere:

```text
incremental benefit
− incremental cost
− cannibalization / subsidy on existing behavior
− operational cost
− downside risk
```

La raccomandazione diventa quindi un test mirato, non un rollout universale.

### Incrementalità: ogni alternativa ha un controfattuale

Quando diciamo:

> “questa iniziativa vale €500k”

stiamo implicitamente dicendo:

> “rispetto all'alternativa che avremmo seguito senza l'iniziativa.”

Questo vale anche quando non stiamo facendo causal inference formale.

La base di confronto deve essere esplicita:

- business as usual;
- soluzione corrente;
- opzione più economica;
- opzione reversibile;
- altra iniziativa concorrente.

### Non tutto deve essere monetizzato

Alcuni trade-off hanno una misura economica ragionevole.

Altri no.

Una decisione può coinvolgere:

- customer harm;
- sicurezza;
- compliance;
- reputazione;
- resilienza;
- fairness;
- strategic option value;
- concentrazione del rischio;
- workload umano.

Forzare tutto in euro può creare falsa precisione.

HM Treasury, nel Green Book 2026, richiede esplicitamente che l'appraisal consideri non soltanto costi e benefici monetizzabili ma anche impatti non monetizzabili, rischi e incertezze.

Fonte: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

Il principio trasferibile all'analytics è:

> **se qualcosa cambia materialmente la preferenza tra alternative, deve essere visibile anche quando non ha una conversione monetaria pulita.**

### Opportunity cost: il progetto buono che perde contro un progetto migliore

Una iniziativa può avere valore atteso positivo e comunque non meritare priorità.

Esempio:

```text
Project A
expected value: €300k
team effort: 6 mesi
high irreversibility

Project B
expected value: €250k
team effort: 3 settimane
low irreversibility
```

Se lo stesso team può fare soltanto uno dei due, il costo di A include anche il valore dell'alternativa rinunciata.

Per questo il Decision Record deve elencare **alternative considerate e alternative escluse**, non soltanto la raccomandazione finale.

### Constraints prima del ranking

Alcune alternative non sono realmente disponibili.

Vincoli possibili:

- budget massimo;
- capacità di engineering;
- disponibilità operativa;
- scadenza regolatoria;
- staffing;
- dipendenze tecniche;
- requisito di rollback;
- limite di customer exposure.

Non serve stimare con grande precisione il valore di un'opzione che viola un vincolo non negoziabile.

Il flusso diventa:

```text
objectives
→ constraints
→ longlist
→ eliminate non-viable options
→ compare shortlist
```

### Reversibilità come parte del valore

Due opzioni con uguale expected value non sono equivalenti se una:

- richiede investimento irreversibile;
- blocca alternative future;
- è difficile da rollbackare;

mentre l'altra consente di imparare e cambiare rotta.

Questa **option value** diventerà centrale nelle sezioni su uncertainty e sensitivity.

### Recommendation Card dentro il Decision Record

Per ciascuna alternativa shortlist registriamo:

```text
option:
objective fit:
expected upside:
expected downside:
implementation cost:
operational capacity:
time to value:
key uncertainty:
reversibility:
non-monetizable impacts:
evidence strength:
```

Poi la raccomandazione deve completare:

> **“Preferiamo X a Y e Z perché…”**

non soltanto:

> “X sembra una buona idea.”

### What would make us choose differently?

Ogni raccomandazione importante dovrebbe dichiarare almeno una **switching condition**.

Esempio:

> “Preferiamo il pilot mirato, a meno che il costo di implementazione superi €300k o il segmento eleggibile scenda sotto 40.000 utenti.”

Questa frase prepara il terreno per la sensitivity analysis.

Rende inoltre evidente che la raccomandazione dipende da assunzioni, non da una verità eterna.

### Regola operativa

Prima di consegnare una raccomandazione chiediamo:

1. qual è l'obiettivo?
2. qual è business as usual?
3. quali alternative credibili abbiamo considerato?
4. quali sono state escluse e perché?
5. quali costi e benefici sono incrementali?
6. quali impatti non sono monetizzabili?
7. quali vincoli cambiano la scelta?
8. quale alternativa preserva più flessibilità?
9. quale assunzione, se cambia, ribalta la raccomandazione?

> **Una raccomandazione senza alternative è spesso un'idea con una tabella di numeri. Una raccomandazione analitica spiega perché una scelta batte le altre nel contesto reale.**
