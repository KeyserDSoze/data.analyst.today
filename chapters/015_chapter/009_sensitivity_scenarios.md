## 15.8 Sensitivity e scenario analysis: il ranking regge in futuri plausibili?

Una recommendation può sembrare robusta soltanto perché molte assunzioni sono state fissate su un singolo valore. La sensitivity analysis pone una domanda più utile:

> **Se alcune assunzioni fossero diverse ma ancora plausibili, sceglieremmo la stessa alternativa?**

Il suo oggetto non è soltanto il business case, ma il **ranking delle opzioni**.

Per iniziare non cambiamo tutto a caso. Cerchiamo le variabili che combinano incertezza elevata, forte impatto, vicinanza a uno switching value o una base di judgment debole. In un progetto possono essere uplift, adoption, CAC, unit margin, implementation cost, churn o failure probability. Se la scelta è governata da tre variabili, variarene cinquanta aggiunge rumore più che informazione.

Una one-way sensitivity isola un driver alla volta:

| Assunzione | Base | Low | High | Switching value |
|---|---:|---:|---:|---:|
| conversion uplift | 6% | 2% | 9% | 3,1% |
| project cost | €400k | €300k | €650k | €590k |
| margin/order | €48 | €35 | €55 | €29 |

Il risultato utile non è soltanto un range finale: è capire **quale assunzione si trova più vicina al punto in cui cambieremmo decisione**. Quella variabile merita più attenzione, oppure più informazione prima del commitment.

### Gli scenari devono essere mondi coerenti, non colonne ±20%

Le variabili reali spesso si muovono insieme. Se la domanda rallenta possono peggiorare contemporaneamente volume, pricing power, CAC, churn e working capital. Per questo uno scenario non è “tutti i parametri -20%”, ma una storia coerente del sistema.

Un competitor aggressivo, per esempio, può implicare CAC +30%, win rate -20%, sales cycle +25%, ARPA stabile e churn leggermente peggiore. Un caso di strong product-market fit può invece combinare CAC vicino al base, win rate +20%, più referral, migliore retention e maggiore difficoltà di hiring. La coerenza causale/operativa dello scenario conta più dell'etichetta ottimistico o pessimistico.

### Aster Logistics: massimo upside e robustezza non sono la stessa cosa

Aster Logistics valuta un nuovo hub per il Centro Italia. Il caso centrale prevede:

- capex: €4,8M;
- risparmio annuo trasporti: €1,45M;
- delivery time: -0,7 giorni;
- crescita volume: +8% annuo.

Le alternative sono:

```text
A — business as usual
B — nuovo hub completo
C — hub più piccolo / modulare
D — capacità in outsourcing per 24 mesi
```

Nel caso di **domanda debole**, la crescita è +1%, il saving del full hub scende a €0,85M, il capex sale a €5,5M e l'outsourcing diventa relativamente più attraente. Nel caso **base** restano crescita +8%, saving €1,45M e capex €4,8M. Nello scenario **domanda forte + fuel inflation**, la crescita arriva al 12%, il saving del full hub a €1,9M e la capacità del piccolo hub diventa un vincolo.

Il punto non è indovinare quale scenario accadrà. È osservare come cambia il ranking: B domina soltanto in base/upside? C mantiene valore in tutti e tre? D costa di più nel caso centrale ma compra 24 mesi di informazione?

L'opzione con massimo valore nel caso centrale non è necessariamente la più robusta. Il full hub ha più upside se la crescita è forte, ma è fragile in domanda debole; un hub modulare può avere meno upside e più option value perché espandibile e con downside inferiore.

### Dominance e correlated uncertainty riducono falsa complessità

Se un'opzione costa di più, arriva nello stesso tempo, offre la stessa capacità ed è meno reversibile senza alcun vantaggio compensativo, è dominata e può uscire dalla shortlist. Non serve un modello sofisticato per continuare a confrontarla.

Dobbiamo invece fare attenzione a rischi apparentemente diversi che dipendono dallo stesso mondo. Un business case con volume alto, margine alto e CAC basso può sembrare robusto se analizziamo ogni variabile separatamente, ma essere estremamente fragile se tutte dipendono dallo stesso scenario competitivo. La one-way sensitivity può nascondere questa correlazione; lo scenario analysis la rende visibile.

Per decisioni ad alto impatto aggiungiamo anche uno **stress scenario**: non per dichiararlo probabile, ma per capire se il sistema sopravvive, quale exposure massima accettiamo, quale guardrail viene superato e se esiste rollback. Domanda -30%, fornitore critico indisponibile, ticket support raddoppiati o costi cloud 3× possono distinguere una normale downside uncertainty da un ruin risk.

### Usare la storia dell'organizzazione contro l'optimism bias

Il *Green Book 2026* richiede aggiustamenti per **optimism bias**, cioè la tendenza sistematica a sottostimare costi e tempi e sovrastimare benefici.[^green-book-sensitivity] Un team analytics può trasformare questo principio in evidenza interna costruendo una base storica:

```text
project
forecast cost
actual cost
forecast duration
actual duration
forecast benefit
observed benefit
```

Se scopriamo che una certa classe di progetti supera sistematicamente tempi e costi, l'adjustment futuro non è più una frase generica tipo “siamo sempre troppo ottimisti”: diventa un prior empirico.

NASA chiede che la recommendation riporti anche la **robustezza del ranking**, in particolare se una riduzione plausibile dell'incertezza potrebbe cambiare l'ordine delle alternative.[^nasa-robustness] È esattamente ciò che sensitivity e scenario analysis devono consegnare al Decision Record.

Il blocco operativo è:

```text
critical assumptions:
one-way sensitivity:
switching values:
coherent scenarios:
stress scenario:
correlated uncertainties:
dominated options removed?:
ranking robust?: yes/no/partly
which new information could change ranking?:
```

> **Una decisione robusta non è quella che massimizza il caso centrale. È quella di cui comprendiamo le condizioni di successo, le condizioni di fallimento e la distanza dal punto in cui dovremmo scegliere diversamente.**

[^green-book-sensitivity]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
[^nasa-robustness]: NASA, *6.8 Decision Analysis*, https://www.nasa.gov/reference/6-8-decision-analysis/
