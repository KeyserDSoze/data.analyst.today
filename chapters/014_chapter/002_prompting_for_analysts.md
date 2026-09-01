## 14.1 Dal prompt alla specifica: dare all'AI il contesto che può usare e quello che non può inventare

Il prompting è utile, ma il termine rischia di portarci nella direzione sbagliata.

Sembra suggerire che la qualità dipenda principalmente da **come formuliamo una frase**.

Nel lavoro analitico dipende soprattutto da **quale specifica rendiamo disponibile al sistema**.

Confrontiamo:

> Analizza le vendite.

con:

> Confronta il net revenue delle ultime 8 settimane con le 8 precedenti, a perimetro negozi comparabile. Usa `payment_captured_at` come data economica, escludi ordini cancellati e refund completi, separa volume/prezzo/mix, segnala segmenti con contributo assoluto > €50k. Prima di interpretare verifica freshness e reconciliation con la misura certificata. Non formulare causal claim.

La seconda richiesta non è migliore perché è “più dettagliata”.

È migliore perché esplicita **decisioni che altrimenti il modello dovrebbe indovinare**.

### Il prompt è una view dei contratti precedenti

Non dovremmo riscrivere nel prompt tutto il libro.

Se esistono già:

- Analytical Brief;
- Data Readiness Review;
- metric definitions;
- Analytical Data Contract;
- Data Flow Architecture Map;

l'AI dovrebbe ricevere o poter recuperare le parti pertinenti.

Il prompt diventa allora una **work order** sopra contesto governato.

```text
Task
+ relevant certified context
+ allowed assumptions
+ constraints
+ expected evidence
+ output contract
```

Questo è molto più robusto di una raccolta di “prompt perfetti” copiati da un documento.

## 14.1.1 Il Context Pack

Per task non banali usiamo un **Context Pack**.

Può includere:

```text
Decision:
Question:
Population:
Grain:
Metric definitions:
Time semantics:
Certified sources:
Known data limitations:
Allowed method:
Forbidden inference:
Expected output:
Required checks:
```

Non tutti i campi devono essere scritti a mano ogni volta.

Possono provenire da metadata, semantic layer, catalogo o documentazione versionata.

### Caso simulato/composito — “perché il churn è salito?”

Un SaaS osserva logo churn da 3,8% a 4,6%.

Richiesta debole:

> Analizza perché il churn è aumentato.

Un sistema generativo può proporre:

- pricing;
- onboarding;
- supporto;
- competizione.

Sono spiegazioni plausibili.

Non sono ancora evidenze.

Un Context Pack migliore stabilisce:

```text
Decision:
capire dove investire capacità di retention investigation

Metric:
logo churn mensile
numeratore = account che terminano la relazione nel mese
base = account attivi a inizio mese

Comparison:
Q2 vs Q1

Required slices:
cohort, plan, country, tenure, activation status

Pre-check:
verificare cambi di tracking/definizione

Claim rule:
association ≠ cause

Output:
contribution-to-delta table
observed facts
candidate hypotheses
next evidence needed
```

Ora il sistema non riceve solo una domanda.

Riceve **i confini epistemici del lavoro**.

## 14.1.2 Known / Unknown / Must Ask

Un pattern utile è obbligare il workflow a classificare ciò che incontra.

**Known**

Informazione presente nel contesto autorizzato.

**Unknown**

Informazione non disponibile ma non bloccante.

**Must Ask / Must Escalate**

Ambiguità che cambia materialmente il risultato.

Esempio:

> “Calcola ARPU per mercato.”

Il sistema trova `gross_revenue`, `net_revenue` e tre possibili definizioni di active user.

La risposta matura non è scegliere quella che sembra più probabile.

È:

```text
MUST ASK:
ARPU non è univoco nel contesto disponibile.
Servono definizione revenue e denominator policy.
```

> **Chiedere chiarimento può essere un output corretto.**

Questa regola diventa ancora più importante nei workflow agentici, perché un'assunzione implicita può propagarsi per dieci step.

## 14.1.3 Assumption budget

Possiamo dichiarare anche un **assumption budget**.

Per esempio:

```text
May infer:
- formato della tabella finale
- naming di alias temporanei

Must not infer:
- KPI definition
- population exclusions
- causal mechanism
- write target
- privacy classification
```

L'obiettivo non è impedire ogni inferenza.

È distinguere **convenzioni innocue** da assunzioni che cambiano il significato o il rischio.

## 14.1.4 Piano prima dell'esecuzione quando il costo di errore è alto

Per task complessi può essere utile separare:

```text
1. plan
2. review
3. execute
4. verify
5. interpret
```

Esempio:

> Proponi il piano di investigazione. Non eseguire query e non formulare conclusioni.

Dopo la review umana:

> Esegui soltanto gli step 1–3 usando le fonti certificate indicate. Se una cardinalità non corrisponde alle attese, fermati.

Questo introduce un **commit point** prima che il sistema consumi risorse o propaghi decisioni sbagliate.

## 14.1.5 Fatti, inferenze, ipotesi e raccomandazioni

La forma dell'output deve separare livelli diversi.

| Livello | Esempio |
|---|---|
| Osservazione | mobile conversion 4,2% → 3,5% |
| Localizzazione | 74% del delta è su Android 14 |
| Ipotesi | possibile problema nel payment flow |
| Evidenza mancante | error code / release telemetry |
| Causal claim | non consentito con i dati correnti |
| Recommendation | investigare build X prima di modificare pricing |

Un testo fluente tende a comprimere queste categorie in una storia unica.

Un output contract le mantiene separate.

## 14.1.6 Caso reale documentato — preparare la semantica per l'AI

Microsoft ha introdotto in Power BI strumenti specifici per preparare un semantic model all'uso AI: AI data schemas, AI instructions e verified answers.[^ms-prep-ai]

La documentazione sulle AI instructions descrive esplicitamente la possibilità di fornire business context, terminology e analytical guidance sul modello e raccomanda di testare le risposte prima della pubblicazione.[^ms-ai-instructions]

La lezione generale è importante:

> **il contesto utile all'AI dovrebbe diventare un asset governato del sistema, non un segreto custodito nella memoria di chi scrive il prompt migliore.**

## 14.1.7 Campo della AI Analysis Control Sheet

```text
Task:
Decision:
Context Pack version:
Certified sources:
Known ambiguities:
Allowed assumptions:
Must-ask conditions:
Forbidden inference:
Expected output schema:
Required checks before interpretation:
```

### Regola operativa

> **Un buon prompt non rende intelligente una richiesta vaga. Una buona specifica rende visibili le decisioni che non vogliamo lasciare all'improvvisazione del modello.**

[^ms-prep-ai]: Microsoft Learn, *Prepare your data for AI to improve Copilot results*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
[^ms-ai-instructions]: Microsoft Learn, *Prepare your data for AI - AI instructions*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-instructions
