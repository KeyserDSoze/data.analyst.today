## 14.12 Versioning e auditability: ricostruire il sistema, non soltanto il prompt

Nei workflow AI il prompt è parte della logica, ma non è l'intera logica.

La stessa istruzione può produrre comportamenti diversi se cambiano:

- modello;
- reasoning configuration;
- tool disponibili;
- permessi;
- semantic model;
- retrieval corpus;
- dati;
- orchestration logic;
- budget di step o retry;
- evaluator;
- policy di approval.

Per questo il vero oggetto da versionare è il **sistema di esecuzione**.

### Dal prompt version al Execution Manifest

Per un'analisi ad alto impatto registriamo un manifest minimo.

```text
run_id:
timestamp:
user / triggering process:
model + configuration:
system/instruction version:
context pack version:
semantic model / metric version:
data snapshot or as-of timestamp:
retrieval sources:
tools enabled:
agent identity + permission scope:
step/retry/cost budget:
queries/tool calls:
checks executed:
human interventions:
final claim:
final action / output:
```

Questo non significa salvare ogni token per sempre.

Significa conservare abbastanza informazione da rispondere, quando serve:

> **“Quale sistema ha prodotto questa decisione e su quale evidenza?”**

### Caso simulato/composito — il KPI cambia senza cambiare la dashboard

Un team Finance usa un agente per generare ogni lunedì una sintesi automatica.

Per mesi l'istruzione contiene:

> “Usa la revenue riconosciuta nel periodo, metrica certificata Finance.”

Dopo una semplificazione diventa:

> “Analizza la revenue della settimana.”

Il modello seleziona `invoice_amount`.

Quel campo include importi emessi ma non ancora riconosciuti secondo la policy contabile interna.

La dashboard non cambia.

Il warehouse non cambia.

La pipeline di invio non cambia.

Eppure il CFO riceve un miglioramento apparente che non esiste secondo la definizione governata.

La modifica critica era una frase.

Senza versioning dell'istruzione e della metrica selezionata, l'incidente sembra inspiegabile.

### Versionare anche il Context Pack

Un prompt può restare identico mentre cambia il contesto recuperato.

Esempio:

```text
metric definition v17:
churn = cancellations / active-at-start
```

poi:

```text
metric definition v18:
churn include anche expiry > 30 giorni
```

Se l'agente usa retrieval dinamico, la stessa domanda può produrre una risposta diversa perché il corpus è cambiato.

Quindi registriamo almeno:

- document/version id;
- metric/version id;
- retrieval timestamp;
- eventuali verified answers utilizzate.

### Reproducibility non significa output identico parola per parola

I sistemi generativi possono essere non deterministici.

L'obiettivo di audit non è sempre ottenere la stessa identica frase.

È poter ricostruire:

- stesso perimetro di dati;
- stesse regole;
- stessa versione del sistema;
- stesso livello di autorizzazione;
- stesso set di controlli;
- una conclusione semanticamente compatibile.

Possiamo distinguere:

**execution reproducibility**

Riusciamo a ricostruire la configurazione e gli input della run?

**semantic reproducibility**

La stessa evidenza porta allo stesso livello di claim e alla stessa decision policy?

Per analytics, la seconda è spesso più importante della formulazione verbale identica.

### Un output senza provenance è più difficile da fidarsi

Ogni artefatto importante dovrebbe indicare almeno:

```text
metric/source version
as-of timestamp
status READY / PROVISIONAL
AI-assisted: yes
verification status
human owner
```

Non serve esporre dettagli tecnici a ogni executive.

Serve che il sistema li renda recuperabili.

### Prompt come “soft code”

Le istruzioni AI hanno proprietà simili al codice:

- modificano il comportamento;
- possono introdurre regressioni;
- hanno dipendenze;
- richiedono review;
- possono essere rollbackate.

Ma hanno anche una differenza importante: il comportamento può variare anche senza cambiare l'istruzione.

Per questo il promotion flow dovrebbe essere:

```text
change
→ diff semantico
→ regression eval
→ review dei failure case
→ staged rollout
→ monitoring
→ rollback se necessario
```

Non:

```text
prompt migliore nella demo
→ produzione
```

### Il diff che conta è comportamentale

Due prompt possono sembrare quasi identici ma cambiare fortemente l'output.

Viceversa, una modifica grande al testo può non cambiare il comportamento sui task rilevanti.

Quindi dopo un change chiediamo:

- quali eval cambiano esito?
- quali tool vengono chiamati diversamente?
- cambia la frequenza di escalation?
- cambia il tipo di metriche selezionate?
- aumenta il costo?
- compaiono nuovi failure mode?

Il diff testuale è soltanto un indizio.

Il vero diff è **nel comportamento osservato**.

### Audit trail per multi-agent

In una catena:

```text
planner
→ SQL agent
→ reviewer
→ executive writer
```

ogni output deve avere provenance.

Non basta sapere che “l'executive writer ha prodotto il memo”.

Dobbiamo poter risalire a:

```text
memo claim
→ evidence artifact
→ query
→ source snapshot
→ metric definition
```

Se un agente modifica o riassume un claim, il trace deve rendere visibile quel passaggio.

### Auditability proporzionata al rischio

Una sessione EDA personale può richiedere poco logging.

Un sistema che:

- pubblica KPI ufficiali;
- invia comunicazioni esterne;
- modifica budget;
- usa dati personali;
- produce raccomandazioni ad alto impatto;

richiede molto di più.

NIST struttura la gestione del rischio AI lungo l'intero lifecycle; Microsoft, per gli agenti, include esplicitamente action audit logging, identity, authorization e human oversight tra i controlli da governare.

Fonti:

- NIST, *Generative AI Profile*: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Microsoft, *AI agent shared responsibility model*: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

### Campo della AI Analysis Control Sheet

```text
run id:
system version:
model/config:
instruction version:
context/retrieval version:
metric/semantic version:
data as-of:
tools + permissions:
checks/eval version:
human interventions:
claim/output version:
rollback reference:
```

> **Auditability non significa conservare tutto. Significa conservare la catena minima necessaria per ricostruire perché un sistema ha avuto il diritto di produrre quel claim o quell'azione.**
