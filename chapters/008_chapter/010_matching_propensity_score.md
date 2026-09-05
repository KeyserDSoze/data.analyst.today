## 8.9 Matching e propensity score: comparabilità sulle variabili osservate

Quando il processo di assegnazione non offre una randomizzazione o una quasi-randomizzazione credibile, possiamo provare a costruire comparabilità **sulle caratteristiche osservate prima del trattamento**. Matching, weighting e propensity score lavorano in questo spazio. La parola decisiva è “osservate”: il metodo può correggere squilibri che misuriamo, non cause importanti che il dataset non registra.

### Caso simulato/composito — Onboarding premium

Un SaaS offre onboarding premium ai clienti considerati più promettenti. Dopo sei mesi il churn è **6,8%** tra i premium e **12,9%** tra i non premium: un gap grezzo di `-6,1 pp`. Ma i clienti premium avevano già ARR più alto, team più grandi, maggiore maturità digitale, activation iniziale migliore e account manager dedicati. Il confronto iniziale mescola quindi trattamento e selezione.

Il team cerca clienti non trattati simili su covariate pre-treatment — ARR, mercato, industry, tenure, dimensione account e utilizzo precedente — e costruisce un comparison group più comparabile. Dopo il matching, il churn dei controlli è **8,4%**: la differenza scende a `-1,6 pp`.

Questa riduzione è informativa. Mostra che una parte importante del gap iniziale era spiegata da caratteristiche osservate che distinguevano i gruppi. Non dimostra però che il residuo `-1,6 pp` sia causalmente attribuibile all'onboarding.

### Il propensity score non è un causal score

Il propensity score sintetizza la probabilità osservata di ricevere il trattamento date le covariate pre-treatment:

`P(T = 1 | covariate pre-treatment)`

Può essere usato per matching, stratification, weighting e diagnostics di overlap. La qualità causale del design, però, non si misura con l'AUC del propensity model. Un modello che predice quasi perfettamente il trattamento può indicare il problema opposto: trattati e non trattati appartengono a zone molto diverse dello spazio delle covariate e quindi esiste poco **common support**.

Il diagnostic centrale è il **balance** dopo matching o weighting. Dobbiamo verificare standardized mean differences, distribuzioni delle covariate, overlap del propensity score, pesi estremi, effective sample size e soprattutto equilibrio delle variabili che il causal model considera importanti.

Supponiamo che tutti gli account enterprise sopra **500.000 € di ARR** ricevano onboarding premium. In quella regione non esistono enterprise comparabili non trattati. Nessun nearest-neighbor algorithm può creare il controfattuale che il dataset non contiene. Possiamo restringere la popolazione all'area di overlap, cambiare estimand, cercare un altro design o generare nuovi dati. Non dovremmo extrapolare silenziosamente.

Questa scelta ha una conseguenza sostanziale: il **trimming cambia la domanda**. Se rimuoviamo le unità senza common support, la stima non descrive più necessariamente l'effetto su tutti i clienti, ma l'effetto tra clienti per cui esistono trattati e controlli comparabili. Lo scope deve essere dichiarato nel Causal Identification Brief.

### Il limite che nessun balance plot può eliminare

Le covariate devono essere pre-treatment. Inserire nel propensity score l'utilizzo del prodotto dopo l'onboarding può introdurre post-treatment bias, anche se migliora la capacità predittiva dell'assegnazione. Ancora una volta la timeline e il DAG vengono prima del modello.

La World Bank presenta matching e propensity score come strumenti per costruire gruppi comparabili sulle caratteristiche osservate e sottolinea la forza dell'assunzione necessaria quando variabili rilevanti non sono misurate.[^worldbank-matching] Se l'assegnazione dell'onboarding premium dipende dalla valutazione qualitativa del sales team e quella valutazione non è registrata, il matching non può bilanciarla direttamente.

Per questo una conclusione professionale deve conservare il limite:

> **Tra clienti comparabili sulle covariate pre-treatment osservate e nell'area di common support, l'onboarding premium è associato a circa 1,6 pp di churn in meno. L'interpretazione causale richiede che non rimangano confondenti non osservati materialmente importanti.**

La **matching card** resta un artefatto utile perché costringe a documentare ciò che il metodo ha realmente fatto:

```text
Estimand:
Covariate pre-treatment incluse e perché:
Variabili importanti non osservate:
Metodo di matching/weighting:
Overlap:
Unità escluse:
Balance prima/dopo:
Pesi estremi:
Popolazione finale:
Sensitivity a specifiche alternative:
Claim consentito:
```

> **Matching può rendere osservazionalmente simili i gruppi. Non rende casuale un processo che casuale non era.**

Quando invece l'assegnazione cambia bruscamente a una soglia, possiamo sfruttare una fonte di comparabilità molto diversa. È il caso della Regression Discontinuity.

[^worldbank-matching]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*, capitolo sul matching: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
