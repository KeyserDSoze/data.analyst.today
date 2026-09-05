## 14.14 AI Analysis Control Sheet: collegare delega, evidenza e responsabilità

I capitoli precedenti hanno costruito artefatti diversi per problemi diversi: Analytical Brief, Data Readiness Review, EDA Evidence Map, Uncertainty Brief, Temporal Decision Brief, Causal Identification Brief, Experiment Contract, Predictive Decision Card, Analytical Data Contract, Data Flow Architecture Map e Tooling Decision Record.

L'AI non sostituisce nessuno di questi oggetti. **Li attraversa.** La AI Analysis Control Sheet serve a documentare dove entra la delega, quali boundary la limitano, quali artefatti produce, quali gate devono passare e quale livello di decisione resta sotto responsabilità umana.

La domanda non è:

> L'analisi è stata fatta con AI?

È:

> **Quale parte è stata delegata, dentro quale perimetro, con quali controlli e con quale responsabilità residua?**

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

La scheda è deliberatamente più ampia di un prompt template, perché il prompt è soltanto una parte del sistema. Non tutti i campi vanno compilati con lo stesso dettaglio per ogni task: è il **rischio** a determinare la profondità del controllo.

### Stati finali

**APPROVED** significa che i controlli richiesti dal contesto sono superati e il claim è adatto alla decisione prevista. Non significa "vero per sempre"; significa evidenza sufficiente per questo uso, in questo momento.

**APPROVED WITH CAVEATS** significa che il risultato è utilizzabile ma deve viaggiare con limitazioni esplicite, per esempio un forecast valido per capacity planning con intervallo insolitamente ampio in un regime instabile.

**PROVISIONAL** consente di orientare attenzione o investigazione, non di prendere ancora la decisione finale. Un esempio tipico è una revenue intraday ancora incompleta: alert diagnostico sì, comunicazione Finance finale no.

**BLOCKED** significa che manca una condizione necessaria: dato non autorizzato, metrica ambigua, source non riconciliata, causal claim senza identification, critical eval failure, permission boundary troppo ampia o owner assente. `BLOCKED` non è un fallimento dell'analista. È il sistema di controllo che funziona.

### Risk tier e autonomy level sono dimensioni diverse

Una classificazione semplice del rischio può essere:

| Tier | Esempio | Controllo tipico |
|---|---|---|
| R0 | spiegare una funzione SQL | review leggera |
| R1 | query/EDA interna reversibile | sanity check + trace minimo |
| R2 | KPI o recommendation management | reconciliation + peer/human review |
| R3 | denaro, persone, compliance o grande blast radius | eval formale + approval + audit + rollback |

Il risk tier non coincide con l'autonomy level. Un task R3 può essere gestito da un sistema A0 che propone soltanto; un task a rischio minore può arrivare ad A3 se policy, reversibilità ed eval lo consentono.

### Claim gate

La Control Sheet mantiene separata anche la scala del claim:

```text
C0 — output non verificato
C1 — calculation verified
C2 — descriptive finding
C3 — diagnostic interpretation con alternative considerate
C4 — predictive/forecast claim validato per deployment scope
C5 — causal claim con identification adeguata
C6 — action recommendation con economics, guardrail e owner
```

Un executive-summary agent può comprimere un C2, ma non trasformarlo in C5. Per causalità, forecasting, experimentation o predictive modeling la Control Sheet richiama gli artefatti specialistici già costruiti: non li duplica.

### Verification Bundle minimo

Per SQL o analytics generato, il percorso minimo è:

```text
schema exists
→ grain preserved
→ cardinality checked
→ metric/date/filter semantics verified
→ totals reconciled
→ edge cases tested
→ independent reference compared
```

Per un modello aggiungiamo la Predictive Decision Card; per causalità il Causal Identification Brief; per forecasting il Temporal Decision Brief; per un esperimento l'Experiment Contract. L'AACS collega il passaggio AI al gate metodologico che gli compete.

### Human review deve dire che cosa guardare

`human review: yes` è un controllo troppo vago. Una review reale dichiara, per esempio:

```text
reviewer: Finance Analytics Lead
must inspect:
- metric id
- reconciliation delta
- READY / PROVISIONAL status
- claim wording
- action exposure
```

Questo riduce l'approval theater e rende la responsabilità verificabile.

### Esempio compatto

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

La scheda non esiste per produrre burocrazia. Esiste per rendere visibile **perché un sistema ha avuto o non ha avuto il diritto di passare dall'evidenza all'azione**.

> **Se una conclusione fosse sbagliata, dobbiamo sapere quali boundary, assunzioni, verifiche e gate avrebbero dovuto intercettarla. Se non sappiamo rispondere, il workflow non è ancora sufficientemente controllato.**
