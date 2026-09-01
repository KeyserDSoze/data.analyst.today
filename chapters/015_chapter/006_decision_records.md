## 15.5 Decision Record: congelare il ragionamento prima che l'esito riscriva la storia

Molte organizzazioni documentano bene i dati e male le decisioni.

Tre mesi dopo ricordiamo:

- cosa è stato fatto;
- quale KPI è salito o sceso;

ma spesso non ricordiamo:

- quali alternative erano realmente disponibili;
- quali informazioni avevamo;
- quali assunzioni guidavano la scelta;
- quale downside avevamo accettato;
- quale evidenza avrebbe dovuto farci cambiare idea.

Il **Decision Record** serve a proteggere questa memoria.

Ma non è un documento da scrivere dopo per giustificare ciò che abbiamo già deciso.

> **Va costruito prima della decisione, quando l'incertezza è ancora visibile.**

### Il template canonico

```text
DECISION RECORD

1. DECISION
question / choice:
decision owner:
decision deadline:
decision date:

2. OBJECTIVE
primary objective:
secondary objectives:
constraints / non-negotiables:

3. ALTERNATIVES
business as usual:
option A:
option B:
option C:
options excluded + reason:

4. EVIDENCE AVAILABLE NOW
key findings:
claim level / evidence strength:
source deliverables:
data as-of:
known limitations:

5. ASSUMPTIONS & UNCERTAINTY
key assumptions:
uncertainty that dominates choice:
reducible before deadline?:
information that could flip choice:
cost/time to learn:
cost of waiting:

6. VALUE & DOWNSIDE
expected upside:
implementation/operating cost:
plausible downside:
non-monetizable impacts:
opportunity/portfolio cost:

7. REVERSIBILITY
what is reversible?:
what becomes locked in?:
pilot/staged option?:
rollback path:

8. SENSITIVITY
switching values:
critical assumptions:
scenarios where option loses:

9. RECOMMENDATION
preferred option:
why it beats alternatives:
what we are explicitly NOT claiming:
what would change our mind:

10. DECISION
chosen option:
reason if different from recommendation:
owner accepting trade-off:

11. EXECUTION & GUARDRAILS
first action:
guardrails:
stop/rollback conditions:

12. LEARNING PLAN
outcome metrics:
review date:
expected range / scenarios:
information to record for evaluation:
```

### Recommendation e decisione devono restare separate

L'analista può raccomandare A.

Il decision owner può scegliere B per ragioni legittime che il modello analitico non rappresenta completamente.

Il record dovrebbe conservare entrambe le cose:

```text
analytics recommendation: A
chosen decision: B
reason: strategic partnership / capacity / legal constraint
```

Questo evita due errori:

1. riscrivere l'analisi come se avesse raccomandato ciò che poi è stato scelto;
2. attribuire all'analista una decisione che apparteneva al business owner.

### Caso simulato/composito — il prezzo che “nessuno ricordava”

Una piattaforma B2B aumenta il prezzo del piano Pro del 12%.

Sei mesi dopo il churn cresce.

Un nuovo team propone immediatamente un rollback.

Il Decision Record originale mostra però che la scelta era stata approvata insieme a:

- rimozione di un usage limit;
- supporto premium;
- migrazione graduale della base;
- obiettivo primario di aumentare contribution margin e ARPA;
- guardrail: churn non oltre +1,5 pp;
- expectation: un piccolo aumento di churn era già incluso nello scenario centrale.

Senza il record, il team giudica la decisione con una metrica diversa da quella usata ex ante.

Con il record, la domanda diventa:

> “Il churn osservato supera il trade-off che avevamo dichiarato accettabile?”

È una discussione molto più rigorosa.

### Timestamp epistemico: cosa sapevamo allora?

Un Decision Record deve fissare un **information cut-off**.

```text
data as-of: 2026-09-01 07:00
forecast version: v18
customer research available: wave 3
known competitor move: no
```

Perché dopo l'esito molte informazioni diventano ovvie.

La qualità della decisione deve essere valutata usando ciò che era ragionevolmente conoscibile **prima**.

### Registrare l'incertezza, non soltanto la stima centrale

Debole:

```text
expected revenue uplift: +8%
```

Meglio:

```text
central: +8%
plausible range: +2% to +12%
main downside driver: adoption
switching value: +3,1%
```

Questo rende possibile una review futura senza fingere che il team avesse previsto esattamente l'esito.

### What would change our mind?

Questo è uno dei campi più importanti del record.

Esempi:

> “Se il CAC pilot supera €2.100 dopo almeno 100 lead qualificati, l'espansione completa non è più preferita.”

> “Se contribution margin per visitor scende oltre il 2% per due settimane, rollback del pricing test.”

> “Se la nuova fonte dati non riconcilia entro 0,5% con Finance, nessun rollout executive.”

Una decisione forte non dice soltanto ciò in cui crediamo.

Dichiara **quale evidenza ci farebbe aggiornare**.

### Guardrail ≠ obiettivo

Un progetto può raggiungere il KPI primario e fallire comunque.

Esempio pricing:

```text
objective:
contribution margin +8%

guardrails:
churn < +1,5 pp
support tickets < +10%
enterprise NRR non deteriora materialmente
```

I guardrail rendono visibile il costo che non siamo disposti a pagare per raggiungere l'obiettivo.

### Decision Record e deliverable precedenti

Il record non ricopia tutto il lavoro analitico.

Rimanda agli artefatti che qualificano l'evidenza:

```text
Analytical Brief
Data Readiness Review
Uncertainty Brief
Causal Identification Brief
Experiment Contract
Predictive Decision Card
AI Analysis Control Sheet
...
```

Nel Decision Record entra soltanto ciò che è necessario per confrontare le alternative.

### Decision Record ≠ decision memo

Il **Decision Record** è l'artefatto completo e strutturato.

Il **decision memo** è la sua superficie di comunicazione sintetica.

Il Capitolo 16 lavorerà su come comunicare evidenza e decisione.

Qui la priorità è costruire bene la scelta prima di raccontarla bene.

### La decisione va chiusa con un learning contract

Prima dell'esecuzione definiamo:

- cosa osserveremo;
- quando;
- con quale baseline;
- quale range ci aspettavamo;
- quali segnali richiedono review;
- chi decide un eventuale cambio di rotta.

Così il ciclo diventa:

```text
evidence
→ decision
→ action
→ observation
→ compare with ex-ante expectations
→ update
```

Non:

```text
evidence
→ decision
→ action
→ outcome
→ nuova storia ex post
```

### Regola operativa

> **Un buon Decision Record non prova che avevamo ragione. Prova che sapevamo quale scelta stavamo facendo, contro quali alternative, con quale evidenza, quali rischi e quali condizioni ci avrebbero fatto cambiare idea.**
