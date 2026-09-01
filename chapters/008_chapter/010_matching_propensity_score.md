## 8.9 Matching e propensity score: comparabilità sulle variabili osservate

Quando il trattamento non è randomizzato, una strategia possibile è costruire un gruppo di confronto che assomigli ai trattati **prima dell'intervento**.

Matching e propensity score provano a fare questo usando covariate osservate.

La parola decisiva è **osservate**.

### Caso simulato/composito — Onboarding premium

Un SaaS offre onboarding premium ai clienti considerati più promettenti.

Dopo sei mesi:

- churn premium: 6,8%;
- churn non premium: 12,9%.

Il gap grezzo è `-6,1 pp`.

Ma i clienti premium avevano già:

- ARR più alto;
- team più grandi;
- maggiore maturità digitale;
- activation iniziale migliore;
- account manager dedicati.

Il comparison group grezzo è quindi poco credibile.

### Matching: confrontare unità simili dove esiste comparabilità

Possiamo cercare, per ogni cliente trattato, clienti non trattati simili su variabili **pre-treatment** come:

- ARR;
- mercato;
- industry;
- tenure;
- dimensione account;
- utilizzo prima dell'onboarding.

Dopo matching:

- churn trattati: 6,8%;
- matched controls: 8,4%.

L'effetto apparente scende da `-6,1 pp` a `-1,6 pp`.

Non significa che `-1,6 pp` sia automaticamente causale.

Significa che una parte importante della differenza iniziale era spiegata da covariate osservate che rendevano i gruppi diversi.

### Propensity score: probabilità di trattamento, non “causal score”

Il propensity score è:

`P(T = 1 | covariate pre-treatment)`

È un modo per sintetizzare molte covariate nella probabilità osservata di ricevere il trattamento.

Può essere usato per:

- matching;
- stratification;
- weighting;
- diagnostics di overlap.

Ma un propensity model con AUC elevata non è necessariamente migliore causalmente.

Se predice quasi perfettamente il trattamento, può anzi rivelare **scarso overlap**: trattati e non trattati appartengono a mondi molto diversi.

### Il vero diagnostic è il balance

Dopo matching o weighting la domanda non è:

> “Quanto bene il modello predice chi è trattato?”

È:

> **“Le covariate pre-treatment rilevanti sono ora sufficientemente bilanciate tra i gruppi?”**

Controlli utili includono:

- standardized mean differences;
- distribuzioni delle covariate;
- overlap del propensity score;
- unità estreme con pesi molto grandi;
- dimensione effettiva del campione dopo weighting;
- balance per covariate ritenute causalmente importanti.

### Common support: non inventare il controfattuale

Supponiamo che tutti gli account enterprise sopra 500.000 € di ARR ricevano onboarding premium.

Non esistono enterprise comparabili non trattati in quella zona.

Nessun nearest-neighbor algorithm può creare informazione che il dataset non contiene.

Possiamo:

- restringere la popolazione all'area di overlap;
- cambiare estimand;
- cercare un altro design;
- progettare nuova raccolta dati o un esperimento.

Ma non dovremmo extrapolare silenziosamente.

### Trimming cambia la domanda

Escludere unità senza common support può migliorare la comparabilità.

Ma cambia anche la popolazione a cui si riferisce l'effetto.

Se rimuoviamo tutti gli account estremi, la stima potrebbe non rispondere più a:

> “Qual è l'effetto su tutti i clienti?”

ma a:

> “Qual è l'effetto tra clienti per cui esistono trattati e controlli comparabili?”

Questo cambiamento deve entrare nel Causal Identification Brief.

### Solo covariate pre-treatment

Usare nel propensity score una variabile generata dal trattamento — per esempio utilizzo del prodotto **dopo** l'onboarding — può introdurre post-treatment bias.

Una buona regola è costruire una timeline e congelare le covariate prima del momento di assignment.

### Il limite fondamentale: unobserved confounding

La World Bank presenta matching e propensity score come strumenti per costruire gruppi comparabili sulle caratteristiche osservate e sottolinea che il metodo richiede forti assunzioni quando variabili rilevanti non sono osservate.[^worldbank-matching]

Se la decisione di assegnare onboarding premium dipende da una valutazione qualitativa del sales team non registrata, il matching non può bilanciarla direttamente.

Per questo l'output dovrebbe includere una discussione esplicita dei confondenti non misurati plausibili.

### Matching non “dimostra” l'effetto

Una frase prudente è:

> **“Tra clienti comparabili sulle covariate pre-treatment osservate e nell'area di common support, l'onboarding premium è associato a circa 1,6 pp di churn in meno. L'interpretazione causale richiede che non rimangano confondenti non osservati materialmente importanti.”**

È meno spettacolare di “l'onboarding riduce il churn del 6,1%”.

È molto più difendibile.

### Matching card

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

[^worldbank-matching]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitolo sul matching: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
