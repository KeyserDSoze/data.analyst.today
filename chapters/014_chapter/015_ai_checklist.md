## 14.14 AI Analysis Control Sheet: il deliverable operativo del capitolo

I capitoli precedenti hanno costruito artefatti diversi per problemi diversi:

- Analytical Brief;
- Data Readiness Review;
- EDA Evidence Map;
- Uncertainty Brief;
- Temporal Decision Brief;
- Causal Identification Brief;
- Experiment Contract;
- Predictive Decision Card;
- Analytical Data Contract;
- Data Flow Architecture Map;
- Tooling Decision Record.

L'AI non sostituisce questi oggetti.

Li attraversa.

Per questo il deliverable del Capitolo 14 è una **AI Analysis Control Sheet**: una scheda che documenta **dove l'AI entra nella catena, cosa può fare, quale evidenza produce, come viene verificata e quale livello di decisione è autorizzato**.

### Il principio

Non chiediamo:

> “L'analisi è stata fatta con AI?”

Chiediamo:

> **“Quale parte è stata delegata, dentro quale perimetro, con quali controlli e con quale responsabilità residua?”**

### Template canonico

```text
AI ANALYSIS CONTROL SHEET

1. DECISION CONTEXT
business decision:
decision owner:
deadline:
risk tier:
reversibility:
blast radius:

2. ANALYTICAL CONTRACT
question type:
required metric / estimand / target:
population + grain:
time semantics:
claim level requested:

3. AI ROLE
AI task:
autonomy level A0/A1/A2/A3:
what is NOT delegated:
model/system:
agent/workflow owner:

4. CONTEXT PACK
approved sources:
metric definitions:
schema/grain/keys:
known constraints:
KNOWN:
UNKNOWN:
MUST ASK:
assumption budget:

5. DATA & PRIVACY BOUNDARY
data owner:
approved environment:
minimum fields:
personal/sensitive data:
redaction/pseudonymisation:
agent identity:
read/write scope:
third-party transfer:

6. TOOL / EXECUTION BOUNDARY
allowed tools:
forbidden actions:
data-readiness gate:
max steps/retries:
cost/runtime budget:
stop conditions:
escalation owner:
rollback:

7. GENERATED ARTIFACTS
plan:
queries/code:
intermediate evidence:
model/forecast if any:
summary/recommendation:

8. VERIFICATION BUNDLE
schema check:
grain/cardinality check:
metric/date/filter check:
reconciliation:
edge cases:
baseline:
independent calculation/source:
falsification/alternative hypotheses:

9. METHOD-SPECIFIC GATE
causal identification:
forecast/backtest:
predictive leakage/as-of:
experiment health:
uncertainty/calibration:
N/A fields explained:

10. EVALUATION
claim being evaluated:
eval suite version:
risk strata:
deterministic checks:
ground truth:
judge model + calibration:
human audit:
critical failures:
regression vs production:

11. CLAIM GATE
facts supported:
inferences supported:
causal claims supported:
known caveats:
claim level approved:

12. HUMAN CONTROL
required reviewer:
what reviewer must inspect:
approval point:
override reason if any:

13. AUDIT
run id:
model/config version:
instruction version:
context/semantic version:
data as-of:
tool calls / query trace:
human interventions:

14. FINAL STATUS
APPROVED / APPROVED WITH CAVEATS / PROVISIONAL / BLOCKED

final output/action:
owner accepting responsibility:
next monitoring/review:
```

### I quattro stati finali

#### APPROVED

I controlli richiesti dal rischio sono superati e il claim è adatto alla decisione prevista.

Non significa “vero per sempre”.

Significa **evidenza sufficiente per questo uso, in questo momento**.

#### APPROVED WITH CAVEATS

Il risultato è utilizzabile, ma alcune limitazioni devono accompagnarlo.

Esempio:

```text
forecast utilizzabile per capacity planning
ma intervallo più ampio del normale per regime instabile
```

#### PROVISIONAL

Il risultato può orientare l'attenzione ma non autorizza ancora la decisione finale.

Esempio:

```text
revenue intraday incompleta
→ alert diagnostico sì
→ comunicazione Finance finale no
```

#### BLOCKED

Manca una condizione necessaria.

Esempi:

- dato non autorizzato;
- metrica ambigua;
- source non riconciliata;
- causal claim senza identification;
- critical eval failure;
- tool permission troppo ampia;
- nessun owner per l'azione.

`BLOCKED` non è un fallimento dell'analista.

È il sistema di controllo che funziona.

### Risk tier: non controlliamo tutto allo stesso modo

Una classificazione semplice può essere:

| Tier | Esempio | Controllo |
|---|---|---|
| R0 | spiegare una funzione SQL | review leggera |
| R1 | query/EDA interna reversibile | sanity check + trace minimo |
| R2 | KPI o recommendation management | reconciliation + peer/human review |
| R3 | azione con denaro, persone, compliance o grande blast radius | eval formale + approval + audit + rollback |

La classificazione deve seguire il contesto reale, non il nome del tool.

### Claim level: l'AI non può salire la scala in fase di scrittura

Un'altra dimensione indipendente è il claim.

```text
C0 — output non verificato
C1 — calculation verified
C2 — descriptive finding
C3 — diagnostic interpretation con alternative considerate
C4 — predictive/forecast claim validato per deployment scope
C5 — causal claim con identification adeguata
C6 — action recommendation con economics, guardrail e owner
```

Un executive-summary agent può comprimere un C2.

Non può trasformarlo in C5.

### Verification Bundle minimo

Per SQL/analytics generato:

```text
schema exists
→ grain preserved
→ cardinality checked
→ metric/date/filter semantics verified
→ totals reconciled
→ edge cases tested
→ result compared with independent reference
```

Per un modello aggiungiamo la Predictive Decision Card.

Per causalità il Causal Identification Brief.

Per forecasting il Temporal Decision Brief.

L'AI Control Sheet **non duplica** questi deliverable: li collega al passaggio AI che li usa.

### La review umana deve avere una domanda precisa

Non scriviamo:

```text
human review: yes
```

Scriviamo:

```text
reviewer: Finance Analytics Lead
must inspect:
- metric id
- reconciliation delta
- provisional/final status
- claim wording
- action exposure
```

Questo riduce approval theater.

### Un esempio sintetico

```text
Decision:
pausare una campagna paid?

Risk tier:
R2

AI role:
A2 — prepara recommendation, non agisce

Data gate:
spend READY
revenue PROVISIONAL

Verification:
ROAS non maturo per stessa finestra

Claim gate:
“performance apparentemente debole” consentito
“campagna non profittevole” non consentito

Status:
PROVISIONAL

Action:
nessuna pausa; rivalutare T+1
```

La scheda non serve a produrre burocrazia.

Serve a rendere **visibile il motivo per cui non abbiamo agito troppo presto**.

### La domanda finale

Prima di consegnare un output AI-assisted chiediamoci:

> **Se questa conclusione fosse sbagliata, sappiamo indicare quali boundary, assunzioni, verifiche e gate avrebbero dovuto intercettare l'errore?**

Se la risposta è no, non abbiamo ancora un processo sufficientemente controllato.

> **L'AI può entrare in quasi ogni passaggio della catena analitica. La AI Analysis Control Sheet serve a impedire che la delega renda invisibile il passaggio in cui evidenza, claim e responsabilità smettono di essere allineati.**
