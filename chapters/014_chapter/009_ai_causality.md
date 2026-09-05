## 14.8 AI e causalità: moltiplicare le obiezioni, non certificare l'effetto

Il Capitolo 8 ha già costruito il framework di causal identification. Qui non ripetiamo matching, RDD, IV o Difference-in-Differences. La domanda è diversa: che cosa cambia quando un sistema generativo può produrre in pochi secondi decine di spiegazioni causali plausibili?

Il rischio principale è la **causal fluency**. Un modello può passare molto rapidamente da una differenza osservata a una storia sul meccanismo. Per esempio:

```text
webinar attendees churn:     5,8%
non-attendees churn:         12,4%
observed difference:         -6,6 pp
```

Da qui un summary può facilmente diventare: "I webinar riducono il churn di 6,6 punti percentuali." Ma dai dati sappiamo soltanto che due gruppi differiscono. Non sappiamo ancora se i clienti più engaged scelgano di partecipare, se i CSM invitino popolazioni particolari, se dimensione e piano differiscano o se altri interventi accompagnino il webinar.

L'AI non ha necessariamente sbagliato aritmetica. Ha **saltato un livello di claim**.

### Causal Claim Gate

Ogni volta che un output usa parole come *causa, effetto, impatto, driver, ha generato, ha ridotto*, la AI Analysis Control Sheet deve poter collegare il claim a un Causal Identification Brief:

```text
estimand:
treatment / exposure:
outcome:
comparison / counterfactual:
assignment mechanism:
key confounders:
post-treatment variables:
identification strategy:
diagnostics:
scope of effect:
claim allowed:
```

Se questi campi non possono essere difesi, il risultato resta descrittivo o diagnostico.

### L'AI come red-team dell'identification strategy

La capacità generativa è particolarmente utile quando la usiamo per attaccare la nostra spiegazione. Possiamo chiedere quali common causes potrebbero produrre l'associazione, quali variabili disponibili sono potenzialmente post-treatment, quale selection mechanism distorcerebbe il confronto, quali placebo/falsification test indebolirebbero l'ipotesi o quali DAG alternativi sono compatibili con lo stesso pattern.

In altre parole, l'AI crea valore quando **moltiplica le alternative da escludere**, non quando produce la storia più convincente.

### Il coupon "miracoloso"

Un retailer osserva, su 2,4 milioni di clienti, spesa nei 30 giorni dopo coupon `+19%` rispetto a clienti senza coupon. Il marketing, però, invia il coupon soprattutto a chi ha visitato il sito nelle ultime 72 ore, ha prodotti in wishlist, ha aperto due email recenti e mostra già alta propensity all'acquisto. Queste variabili influenzano sia l'assegnazione sia l'outcome.

Il `+19%` è quindi una differenza osservata tra popolazioni selezionate. Il team introduce un holdout randomizzato **tra gli eleggibili** e trova un effetto incrementale molto più piccolo ma ancora economicamente interessante. Il numero esatto non è importante; lo è la sequenza:

```text
association
→ reconstruct assignment
→ define eligible population
→ create credible counterfactual
→ estimate effect
→ decide economics
```

### "Controllare tutto" può peggiorare il design

Un suggerimento generativo frequente è aggiungere tutte le variabili disponibili alla regressione "per controllare i confondenti". La disponibilità di una colonna, però, non è un criterio causale. Tra le feature possono esserci mediatori, collider, variabili misurate dopo il trattamento o proxy che cambiano la popolazione analizzata. Ogni covariata deve essere giustificata dalla **causal structure**, non dalla facilità con cui il modello la trova.

Un prompt utile quindi non chiede "qual è l'effetto di X?". Chiede di non stimare ancora l'effetto, ricostruire i possibili meccanismi di assegnazione, identificare common causes e variabili post-treatment, proporre design compatibili con i dati e dichiarare esplicitamente ciò che non è identificabile.

### Claim ladder e experiment design

La Control Sheet può distinguere livelli progressivi:

```text
L0: non interpretabile
L1: associazione osservata
L2: pattern robusto a segmentazioni / robustness check
L3: meccanismo plausibile, non identificato causalmente
L4: effetto causale identificato sotto assunzioni esplicite
L5: effetto replicato / sperimentale con scope operativo definito
```

Un executive-summary agent non può promuovere un L2 a L4. Se la soluzione migliore è un esperimento, l'AI può aiutare a proporre popolazione eleggibile, randomization unit, spillover, guardrail, outcome ed eterogeneità pre-specificata; poi il design rientra nell'**Experiment Contract** del Capitolo 9.

La continuità è essenziale: l'AI non introduce un metodo causale alternativo. Accelera il lavoro dentro metodi che mantengono intatte le proprie assunzioni.

La World Bank, in *Impact Evaluation in Practice*, struttura l'impact evaluation intorno alla costruzione di un controfattuale credibile e alla comprensione del meccanismo di assegnazione.

Fonte: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice

> **L'AI può moltiplicare le ipotesi causali e i modi di attaccarle. Non può trasformare la plausibilità narrativa in identificazione causale.**
