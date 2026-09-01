# Capitolo 9 — Experimentation e A/B testing nel mondo reale

> **Un esperimento non è affidabile perché è randomizzato. È affidabile quando assignment, exposure, telemetria, metriche, analisi e decisione restano coerenti dall'inizio alla fine.**

Il Capitolo 8 ha spiegato perché la randomizzazione può costruire un controfattuale credibile.

Qui partiamo da un problema diverso.

Nel mondo reale un esperimento causalmente valido sulla lavagna può rompersi in produzione perché:

- l'identità usata per randomizzare non è stabile;
- alcuni utenti vedono entrambe le varianti;
- l'assegnazione è 50/50 ma l'esposizione non lo è;
- una variante genera eventi che la pipeline filtra diversamente;
- la metrica primaria cambia definizione durante il test;
- il test raggiunge il sample size in due giorni ma il comportamento si stabilizza in tre settimane;
- il team guarda il risultato ogni ora e si ferma alla prima fluttuazione favorevole;
- un marketplace randomizza buyer indipendenti in un sistema in cui seller e inventario reagiscono globalmente;
- una vittoria sulla primary metric nasconde un peggioramento su frodi, costi o qualità;
- il rollout al 100% modifica il sistema rispetto al test al 10%.

Questi non sono dettagli di implementazione separati dalla statistica.

Sono parte della **validità dell'esperimento**.

## 9.0 L'esperimento come sistema operativo

Un A/B test reale attraversa almeno questa catena:

```text
DECISIONE
    ↓
IPOTESI / TREATMENT
    ↓
ELIGIBILITY
    ↓
RANDOMIZATION UNIT + ASSIGNMENT
    ↓
EXPOSURE
    ↓
TELEMETRIA
    ↓
METRIC CONTRACT
    ↓
HEALTH CHECKS
    ↓
INFERENCE PLAN
    ↓
SHIP / NO-SHIP / ITERATE
    ↓
ROLLOUT + MONITORING
```

Una rottura a monte può rendere irrilevante la sofisticazione a valle.

Per esempio, un confidence interval calcolato perfettamente non salva un test in cui gli utenti più coinvolti della variante B sono spariti dal dataset.

### Il confine con il Capitolo 5

Nel Capitolo 5 abbiamo già imparato:

- effect size;
- confidence interval;
- p-value;
- Type I e Type II error;
- power;
- sample size;
- multiple testing.

Non li ripeteremo come teoria statistica generale.

Qui li useremo come **vincoli di un contratto sperimentale**:

> Quale effetto sarebbe materialmente importante? Quanto traffico serve? Quando possiamo leggere il risultato? Quante metriche possono guidare la decisione?

### Il confine con il Capitolo 8

Il Capitolo 8 ha spiegato perché un assignment randomizzato può identificare causalmente un effetto.

Qui chiediamo:

> **L'implementazione ha preservato davvero quella randomizzazione?**

Questo significa distinguere:

- unità di randomizzazione;
- unità di exposure;
- unità di analisi;
- compliance;
- contamination;
- missingness;
- sample ratio mismatch.

## Caso simulato/composito — QuickPay

Una grande piattaforma e-commerce europea vuole testare **QuickPay**, un pulsante che salta alcuni passaggi del checkout.

Situazione iniziale:

- conversion rate utente → ordine: 3,92%;
- traffico mensile eleggibile: circa 3,1 milioni di utenti;
- contribution margin medio per ordine: 17,40 €;
- chargeback rate: 0,42%;
- cancellation rate entro 24 ore: 2,8%.

La proposta del Product Manager è:

> “Facciamo 50/50 per una settimana. Se la conversione sale, ship.”

Prima di avviare il test, l'analista apre una serie di domande.

### Assignment

- randomizziamo sessione, user ID o device?
- lo stesso utente può vedere entrambe le esperienze?
- il bucket rimane stabile tra web e app?

### Exposure

- essere assegnato a QuickPay significa averlo realmente visto?
- utenti non eleggibili dopo l'assegnazione entrano comunque nell'analisi?
- crash o latency cambiano la probabilità di exposure?

### Metriche

- primary metric: conversion per sessione o per utente?
- ordini annullati entrano nel successo?
- chargeback e frodi sono guardrail?
- quale worsening massimo accettiamo?

### Durata e sensibilità

- qual è il Minimum Detectable Effect che cambia davvero la decisione?
- il traffico permette di rilevarlo?
- una settimana copre il ciclo weekday/weekend e il comportamento dei returning users?

### Decisione

- che cosa significa `SHIP`?
- rollout immediato al 100% o ramp progressivo?
- quali metriche possono generare rollback?

Queste domande **sono il disegno sperimentale**.

## Caso reale documentato — Microsoft tratta la qualità sperimentale come un gate

Microsoft Experimentation Platform descrive Sample Ratio Mismatch, data-quality checks e metric alerts come componenti strutturali della trustworthy experimentation. In particolare, Microsoft afferma che i test con SRM sono generalmente considerati non affidabili e non dovrebbero guidare decisioni finché la causa non è compresa.[^ms-data-quality]

Questo principio cambia l'ordine con cui guardiamo un dashboard sperimentale.

Non:

```text
lift -> p-value -> forse controlliamo i dati
```

ma:

```text
experiment health -> data validity -> effect estimate -> decision
```

## L'Experiment Contract

Il deliverable centrale del capitolo sarà un **Experiment Contract** scritto **prima** di guardare il risultato.

```text
DECISIONE
Quale scelta deve informare il test?

HYPOTHESIS / TREATMENT
Che cosa cambia tra controllo e trattamento?

POPOLAZIONE / ELIGIBILITY
Chi può entrare nel test?

RANDOMIZATION
Qual è l'unità? Come resta stabile l'assegnazione?

EXPOSURE
Che cosa significa essere realmente trattati?

METRIC CONTRACT
Primary/OEC, guardrail, diagnostics, data-quality metrics.

MATERIALITY
MDE e soglie business rilevanti.

DURATION
Sample requirement + cicli temporali + novelty/learning.

HEALTH CHECKS
SRM, telemetry, exposure, missingness, invariants.

INTERFERENCE
Può il trattamento di un'unità influenzarne un'altra?

INFERENCE PLAN
Fixed horizon o sequential design? Multiple metrics/variants?

DECISION RULE
SHIP / NO-SHIP / ITERATE / INCONCLUSIVE.

ROLLOUT
Ramp, holdout, rollback triggers, post-ship monitoring.
```

Il contratto non elimina l'incertezza.

Evita che il team **riscriva le regole dopo aver visto il risultato**.

> **La trustworthy experimentation non consiste nel calcolare correttamente una differenza. Consiste nel preservare la credibilità del confronto dal primo bucket fino alla decisione di ship.**

[^ms-data-quality]: Microsoft Research, *Data Quality: Fundamental Building Blocks for Trustworthy A/B testing Analysis*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis
