## 15.2 Dall'insight alla raccomandazione: confrontare alternative, non difendere la prima idea

Una raccomandazione debole nasce spesso da una catena molto persuasiva e molto incompleta:

```text
abbiamo trovato un problema
→ abbiamo immaginato una soluzione
→ abbiamo stimato il beneficio della soluzione
→ raccomandiamo la soluzione
```

Manca il confronto che rende una recommendation realmente decisionale: **rispetto a quali alternative?**

Per questo partiamo dall'obiettivo, non dalla soluzione. Se il checkout abandonment cresce quando compare il costo di spedizione, l'obiettivo non è “introdurre free shipping”. È aumentare contribution margin dagli utenti che raggiungono il checkout senza deteriorare economics e customer experience. A quel punto diventano plausibili più opzioni: mantenere la policy attuale, introdurre free shipping universale sopra €40, limitarla ai segmenti ad alto rischio di abbandono, differenziare la soglia per margine o categoria, ridurre la tariffa senza azzerarla oppure intervenire prima sul modo in cui il costo viene comunicato.

Il problema passa così da “free shipping sì/no?” a **quale trade-off tra alternative risponde meglio all'obiettivo**.

### Il beneficio incrementale non coincide con il valore totale toccato dalla policy

Un retailer osserva che il 21% degli utenti che abbandonano il checkout lo fa dopo aver visto il costo di spedizione. Una prima analisi stima che free shipping sopra €40 possa produrre +2,4 punti percentuali di conversion, circa 31.000 ordini incrementali annui, con €18 di contribution margin prima della shipping subsidy e un costo medio sovvenzionato di €6,20.

Una presentazione superficiale può enfatizzare:

```text
31.000 × €18 ≈ €558k
```

Ma la policy non sovvenziona soltanto gli ordini incrementali. Se centinaia di migliaia di ordini che sarebbero avvenuti comunque ricevono la spedizione gratuita, il trasferimento di margine sul comportamento esistente può superare il beneficio.

La struttura economica corretta diventa:

```text
incremental benefit
− incremental cost
− subsidy / cannibalization on existing behavior
− operational cost
− downside risk
```

La raccomandazione non è più rollout universale, ma un test mirato che permetta di misurare incrementalità e price sensitivity con blast radius limitato.

Questa logica vale anche fuori dalla causal inference formale. Ogni volta che diciamo “questa iniziativa vale €500k” stiamo implicitamente scegliendo un controfattuale operativo: business as usual, soluzione corrente, opzione più economica, opzione reversibile o altra iniziativa concorrente. La base di confronto deve essere visibile.

### I trade-off che contano non entrano tutti in euro

Una decisione può coinvolgere customer harm, sicurezza, compliance, reputazione, resilienza, fairness, workload umano, concentrazione del rischio o strategic option value. Forzare tutto in una conversione monetaria produce spesso falsa precisione.

Il *Green Book 2026* distingue esplicitamente costi e benefici monetizzabili da quelli che devono restare quantitativi o qualitativi e chiede che entrambi siano visibili nel confronto delle opzioni.[^green-book-tradeoffs] Il principio è trasferibile: **se un impatto può cambiare materialmente il ranking, deve apparire anche se non possediamo una conversione pulita in euro**.

### Una buona iniziativa può perdere contro un'alternativa migliore

L'opportunity cost entra nella decisione quando più opzioni competono per la stessa capacità. Consideriamo:

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

A può avere valore positivo e non meritare la priorità. Se lo stesso team può eseguire una sola iniziativa, il costo di A include anche l'opportunità rinunciata. Per questo il Decision Record conserva non solo l'opzione raccomandata, ma anche alternative considerate, opzioni escluse e motivo dell'esclusione.

Prima del ranking vengono i vincoli. Budget, capacità engineering, staffing, scadenze regolatorie, dipendenze tecniche, limiti di customer exposure o requisiti di rollback possono rendere un'opzione non praticabile. Non ha senso raffinare il business case di una soluzione che viola un vincolo non negoziabile.

Il flusso è quindi:

```text
objectives
→ constraints
→ longlist
→ eliminate non-viable options
→ compare shortlist
```

### Reversibilità e switching condition fanno parte della recommendation

Due alternative con expected value simile non sono equivalenti se una blocca capitale e opzioni future mentre l'altra consente di imparare e tornare indietro. La reversibilità non è un dettaglio di execution: è parte del valore della scelta.

Per ciascuna opzione shortlist possiamo mantenere una Recommendation Card:

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

La recommendation deve poi poter completare una frase precisa:

> **Preferiamo X a Y, Z e business as usual perché...**

E deve dichiarare ciò che la renderebbe obsoleta. Per esempio:

> Preferiamo il pilot mirato, a meno che il costo di implementazione superi €300k o il segmento eleggibile scenda sotto 40.000 utenti.

Questa è la **switching condition** che prepara le sezioni successive. Non indebolisce la raccomandazione: rende esplicito che la scelta dipende da assunzioni e vincoli osservabili.

> **Una raccomandazione senza alternative è spesso un'idea con una tabella di numeri. Una raccomandazione analitica spiega perché una scelta batte le altre nel contesto reale e quale cambiamento ci farebbe preferire diversamente.**

[^green-book-tradeoffs]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
