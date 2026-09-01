## 15.8 Sensitivity e scenario analysis: quanto è robusto il ranking delle alternative?

Una raccomandazione può sembrare forte soltanto perché abbiamo fissato molte assunzioni su un singolo valore.

La sensitivity analysis pone una domanda più professionale:

> **se le nostre assunzioni fossero diverse ma ancora plausibili, sceglieremmo la stessa alternativa?**

Il suo oggetto non è soltanto il business case.

È il **ranking delle opzioni**.

### Sensitivity non significa cambiare tutto a caso

Partiamo dalle variabili che:

- hanno maggiore incertezza;
- hanno maggiore impatto;
- sono vicine a uno switching value;
- derivano da judgment debole;
- potrebbero cambiare insieme.

Esempi:

```text
uplift
adoption
CAC
unit margin
implementation cost
volume growth
churn
failure probability
```

Non serve variare cinquanta parametri se la decisione è governata da tre.

### One-way sensitivity: isolare il driver

Cambiamo una variabile alla volta mantenendo le altre al caso base.

Esempio:

| Assunzione | Base | Low | High | Switching value |
|---|---:|---:|---:|---:|
| conversion uplift | 6% | 2% | 9% | 3,1% |
| project cost | €400k | €300k | €650k | €590k |
| margin/order | €48 | €35 | €55 | €29 |

Il risultato utile non è soltanto un range di valore.

È capire:

> **quale assunzione ha la distanza minore dal punto in cui cambieremmo decisione?**

Quella merita più attenzione analitica.

### Scenario analysis: cambiare insieme assunzioni coerenti

Le variabili del mondo reale non cambiano sempre indipendentemente.

Se la domanda rallenta, possono muoversi insieme:

- volumi;
- pricing power;
- CAC;
- churn;
- working capital.

Per questo uno scenario non dovrebbe essere:

```text
tutti i parametri -20%
```

se quella combinazione non rappresenta un mondo credibile.

Uno scenario è una **storia coerente del sistema**.

Esempio espansione commerciale:

**Scenario: competitor enters aggressively**

- CAC +30%;
- win rate -20%;
- sales cycle +25%;
- ARPA stabile;
- churn leggermente peggiore.

**Scenario: strong product-market fit**

- CAC vicino al base;
- win rate +20%;
- referral maggiore;
- retention migliore;
- hiring più difficile per crescita rapida.

La coerenza conta più dell'etichetta “pessimistico/ottimistico”.

### Caso simulato/composito — Aster Logistics e il nuovo hub

> **Nota:** caso didattico simulato/composito.

Aster Logistics valuta un hub per servire il Centro Italia.

Caso centrale:

- capex: €4,8M;
- risparmio annuo trasporti: €1,45M;
- delivery time: -0,7 giorni;
- crescita volume: +8% annuo.

Il progetto sembra interessante.

Ma le alternative sono:

```text
A — business as usual
B — nuovo hub completo
C — hub più piccolo/modulare
D — capacità in outsourcing per 24 mesi
```

Il team costruisce scenari coerenti.

### Scenario 1 — domanda debole

- crescita volume: +1%;
- fuel cost stabile;
- saving hub: €0,85M;
- capex completo: €5,5M;
- outsourcing relativamente più attraente.

### Scenario 2 — base

- crescita: +8%;
- saving: €1,45M;
- capex: €4,8M.

### Scenario 3 — domanda forte + fuel inflation

- crescita: +12%;
- fuel più caro;
- saving hub: €1,9M;
- capacità del piccolo hub diventa un vincolo.

Il punto non è scegliere quale scenario “succederà”.

È vedere:

- B domina soltanto in base/upside?
- C mantiene valore in tutti e tre?
- D costa di più nel base ma compra 24 mesi di informazione?

Questa è una decisione molto più ricca del solo payback centrale.

### Robust choice vs optimal choice

L'opzione con valore massimo nello scenario centrale non è sempre quella più robusta.

Una **robust choice** può:

- non essere la migliore in nessun singolo scenario;
- ma evitare outcome molto cattivi in molti scenari;
- preservare possibilità di adattamento.

Esempio:

```text
Full hub:
ottimo se crescita forte
fragile se domanda debole

Modular hub:
meno upside
ma espandibile e downside minore
```

Se l'incertezza è alta e l'impegno irreversibile, la seconda opzione può essere preferibile.

### Dominance: alcune opzioni non meritano altra analisi

Un'opzione è **dominata** quando un'altra è almeno altrettanto buona sulle dimensioni importanti e migliore su almeno una, senza un compensating advantage credibile.

Esempio:

```text
Option A:
costo maggiore
stesso time-to-value
stessa capacità
meno reversibile

Option B:
costo minore
stessa performance
più reversibile
```

Non serve un modello sofisticato per continuare a confrontarle.

Eliminare opzioni dominate riduce la complessità della decisione.

### Correlated uncertainty: non sommare comfort indipendenti che indipendenti non sono

Supponiamo che un business case assuma:

- volume alto;
- margine alto;
- CAC basso.

Se tutti e tre dipendono dallo stesso scenario macro/competitivo, trattarli come rischi indipendenti sottostima il downside.

La sensitivity one-way può non mostrarlo.

Lo scenario analysis sì.

### Stress scenario: cosa succede fuori dal range “comodo”?

Per decisioni ad alto impatto aggiungiamo un caso di stress.

Non perché sia lo scenario più probabile.

Ma per capire:

- sopravvive l'organizzazione?
- esiste rollback?
- quale exposure massima accettiamo?
- quale guardrail viene superato?

Esempi:

- domanda -30%;
- fornitore critico indisponibile;
- rollout che raddoppia ticket support;
- costi cloud 3×;
- regime normativo più restrittivo.

Lo stress test aiuta a distinguere **upside uncertainty** da **ruin risk**.

### Optimism bias: usare la storia dell'organizzazione come dato

HM Treasury mantiene guidance specifica sull'**optimism bias**: costi e tempi possono essere sottostimati e benefici sovrastimati nelle stime iniziali.

Riferimenti:

- Green Book 2026: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
- supplementary guidance: https://www.gov.uk/government/publications/green-book-supplementary-guidance-optimism-bias

Un team analytics può applicare lo stesso principio in modo empirico.

Costruiamo una tabella storica:

```text
project
forecast cost
actual cost
forecast duration
actual duration
forecast benefit
observed benefit
```

Poi chiediamo:

- tendiamo sistematicamente a sottostimare delivery time?
- quali categorie di progetto hanno maggiore overrun?
- quale adjustment empirico è ragionevole?

Questo trasforma “siamo sempre troppo ottimisti” in un dato analizzabile.

### Caso pubblico documentato — NASA e robustness del ranking

La guida NASA sulla Decision Analysis raccomanda di valutare alternative rispetto a criteri e incertezze e di riportare al decision-maker la **robustezza del ranking**, inclusa la domanda se ridurre l'incertezza potrebbe credibilmente cambiare l'ordine delle alternative.

Fonte: https://www.nasa.gov/reference/6-8-decision-analysis/

È esattamente il ruolo della sensitivity analysis nel Decision Record:

> non soltanto “quanto può variare il risultato?”, ma “questa variazione può cambiare la scelta?”

### Campo del Decision Record

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

### Regola operativa

Prima di dichiarare robusta una raccomandazione:

1. identifica le 3–5 assunzioni che governano la scelta;
2. trova gli switching values;
3. costruisci scenari coerenti, non semplici percentuali uniformi;
4. cerca rischi correlati;
5. elimina opzioni dominate;
6. stressa il downside rilevante;
7. chiedi se nuova informazione plausibile potrebbe cambiare il ranking.

> **Una decisione robusta non è quella che massimizza il caso centrale. È quella di cui comprendiamo chiaramente le condizioni di successo, le condizioni di fallimento e la distanza dal punto in cui dovremmo scegliere diversamente.**
