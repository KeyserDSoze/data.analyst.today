## 15.5 Decision Record: congelare il ragionamento prima che l'esito riscriva la storia

Molte organizzazioni documentano bene dati e KPI, ma male il momento in cui una scelta viene costruita. Tre mesi dopo ricordiamo cosa abbiamo fatto e quale numero è salito o sceso; molto più difficilmente ricordiamo quali alternative erano disponibili, quali informazioni possedevamo, quale downside avevamo accettato e quale evidenza avrebbe dovuto farci cambiare idea.

Il **Decision Record** protegge questa memoria. Non è un documento da scrivere dopo per giustificare una scelta già presa. Va costruito **prima della decisione**, quando alternative, vincoli e incertezza sono ancora visibili.

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

La struttura è volutamente ampia, ma non ogni decisione richiede la stessa profondità. Una scelta reversibile e poco costosa può usare una versione compatta; pricing globale, capex pluriennale o una policy con impatto su persone richiedono più disciplina. Ciò che non cambia è la logica: **quale scelta, rispetto a quali alternative, con quale evidenza e quale rischio?**

### Recommendation e decisione non sono la stessa responsabilità

L'analista può raccomandare A e il decision owner scegliere B per ragioni legittime che il modello analitico non rappresenta completamente. Il record deve conservare entrambe le cose:

```text
analytics recommendation: A
chosen decision: B
reason: strategic partnership / capacity / legal constraint
```

Questo evita di riscrivere l'analisi come se avesse raccomandato ciò che poi è stato scelto e impedisce di attribuire all'analista una responsabilità che appartiene al business owner.

Consideriamo una piattaforma B2B che aumenta il prezzo del piano Pro del 12%. Sei mesi dopo il churn cresce e un nuovo team propone subito un rollback. Il Decision Record originale mostra però che il price change era stato approvato insieme a rimozione di un usage limit, supporto premium e migrazione graduale della base. L'obiettivo primario era aumentare contribution margin e ARPA; il guardrail dichiarato era churn non oltre +1,5 pp e un piccolo deterioramento era già presente nello scenario centrale.

Senza record, il team giudica la scelta con una metrica diversa da quella usata ex ante. Con il record, la domanda diventa: **il churn osservato supera il trade-off che avevamo dichiarato accettabile?**

### Il timestamp epistemico impedisce all'hindsight di riscrivere la decisione

Ogni Decision Record dovrebbe fissare un information cut-off:

```text
data as-of: 2026-09-01 07:00
forecast version: v18
customer research available: wave 3
known competitor move: no
```

Dopo l'esito, molte informazioni sembrano ovvie. La decision quality deve invece essere valutata rispetto a ciò che era ragionevolmente conoscibile **prima**.

Per lo stesso motivo registriamo l'incertezza, non soltanto la stima centrale. Invece di:

```text
expected revenue uplift: +8%
```

preferiamo:

```text
central: +8%
plausible range: +2% to +12%
main downside driver: adoption
switching value: +3,1%
```

Così una review futura può distinguere un outcome sorprendente da un esito che era già dentro il range accettato.

### “What would change our mind?” è una parte della scelta

Una decisione forte non dichiara soltanto ciò in cui crediamo. Dichiara quale evidenza ci farebbe aggiornare.

> Se il CAC pilot supera €2.100 dopo almeno 100 lead qualificati, l'espansione completa non è più preferita.

> Se contribution margin per visitor scende oltre il 2% per due settimane, il pricing test entra in review/rollback.

> Se la nuova fonte dati non riconcilia entro 0,5% con Finance, nessun rollout executive.

Queste non sono note accessorie. Sono il ponte tra decisione e learning.

Anche i guardrail hanno un ruolo diverso dall'obiettivo. Se l'obiettivo è contribution margin +8%, i guardrail possono essere churn < +1,5 pp, support tickets < +10% e nessun deterioramento materiale dell'enterprise NRR. Rendono visibile **quale costo non siamo disposti a pagare per ottenere il beneficio principale**.

### Il Decision Record collega, non duplica, gli artefatti precedenti

Il record rimanda ad Analytical Brief, Data Readiness Review, Uncertainty Brief, Causal Identification Brief, Experiment Contract, Predictive Decision Card, AI Analysis Control Sheet e agli altri deliverable che qualificano l'evidenza. Non deve ricopiare l'intero lavoro tecnico: deve portare nel confronto soltanto ciò che può cambiare la scelta.

Il **Decision Record** è quindi diverso dal **decision memo**. Il primo costruisce e conserva il ragionamento; il secondo ne sarà la superficie comunicativa, tema del Capitolo 16.

Prima dell'esecuzione il record si chiude con un learning contract: cosa osserveremo, quale baseline useremo, quando avverrà la review, quale range avevamo previsto e quali segnali richiederanno un cambio di rotta. Il ciclo diventa:

```text
evidence
→ decision
→ action
→ observation
→ compare with ex-ante expectations
→ update
```

non:

```text
evidence
→ decision
→ action
→ outcome
→ nuova storia ex post
```

> **Un buon Decision Record non prova che avevamo ragione. Prova che sapevamo quale scelta stavamo facendo, contro quali alternative, con quale evidenza, quali rischi e quali condizioni ci avrebbero fatto cambiare idea.**
