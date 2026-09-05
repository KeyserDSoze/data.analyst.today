## 10.16 Predictive Decision Card: il contratto operativo del sistema predittivo

Il modello non è il deliverable finale. Il deliverable è una specifica che permetta a una persona diversa da chi ha costruito il notebook di capire **che cosa viene previsto, con quale informazione, come la generalizzazione è stata verificata, come lo score diventa una decisione e che cosa faremo quando il sistema degrada**.

Lo chiameremo **Predictive Decision Card**. Non sostituisce model registry, documentazione tecnica o governance regolatoria. Collega in una sola vista prediction task, evidence, operating policy e monitoring.

La forma strutturata è intenzionale: questa sezione deve poter essere riusata come gate di progetto.

## 1. Decisione e capacità

```text
Decisione:
Azione disponibile:
Capacità minima/massima:
Costo dell'azione:
Costo FP / FN o altra business loss:
Valore a rischio:
Owner della decisione:
```

Scrivere prima l'azione evita di costruire score senza uso. Se il team può gestire 2.000 casi, una policy che ne genera 6.000 non è pronta anche con metriche eccellenti.

## 2. Prediction specification

```text
Prediction unit:
Technical identity key:
Prediction time:
Target:
Horizon:
Label maturity:
Population / eligibility:
Scope geografico/prodotto:
Casi non coperti / out-of-distribution:
```

Il prediction time definisce la frontiera informativa. Horizon e label maturity impediscono di valutare troppo presto un batch e chiamare “negativi” outcome che non hanno ancora avuto tempo di maturare.

## 3. Feature availability e lineage `as-of`

Per ogni famiglia critica documentare:

| Campo | Domanda |
|---|---|
| source of truth | da dove nasce la feature? |
| semantic timestamp | a quale momento del mondo si riferisce? |
| availability | esiste al prediction time? |
| historical `as-of` | possiamo ricostruirla correttamente nel passato? |
| serving latency | quanto ritarda online/batch? |
| fallback | che cosa succede se manca? |
| owner | chi risponde della definizione? |

Una feature che “esiste oggi” ma non ha history `as-of` affidabile non può sostenere una validation storica onesta.

## 4. Baseline e candidato

```text
Baseline semplice:
Candidate model / version:
Feature set / version:
Training window:
Complexity justification:
Costo aggiuntivo di serving/maintenance:
```

La complexity justification dovrebbe poter essere espressa con una frase concreta, per esempio:

> “Il gradient boosting porta precision@2000 dal 31% al 39% rispetto al logit, con latency compatibile con il batch settimanale.”

Il nome dell'algoritmo non è una giustificazione.

## 5. Validation design

Scrivere prima una frase in linguaggio business:

> **“Il test è out-of-time e lascia fuori interi account perché il modello dovrà generalizzare sia a clienti nuovi sia a periodi futuri.”**

Poi documentare:

```text
Train:
Validation / CV:
Final test:
Temporal ordering:
Grouping:
Anti-leakage pipeline:
Slices critiche:
Baseline nello stesso split/fold:
Worst-case performance:
```

Lo split deve rappresentare il deployment, non soltanto dividere righe.

## 6. Performance: separare errore, ranking e probabilità

Per target continui:

```text
Primary error metric:
Median / P90 / P95 error:
Bias medio:
Errori per slice critiche:
Business loss, se disponibile:
```

Per classification/ranking:

```text
Base rate:
ROC-AUC, se pertinente:
PR-AUC / Average Precision, se evento raro:
Precision@K / recall@capacity:
Confusion matrix agli operating point:
Performance per segmenti critici:
```

Se gli score vengono trattati come probabilità, aggiungere:

```text
Calibration globale:
Reliability per segmenti:
Brier/log loss o proper score scelto:
Recalibration method:
Dataset usato per fit del calibratore:
```

Uno score utile al ranking non va venduto come probabilità se la calibration non è stata verificata.

## 7. Operating policy

```text
Threshold / top-K / ranking rule:
Dataset usato per scegliere la soglia:
Capacity constraint:
Economic weighting:
Human review / override:
Policy version:
Fallback policy:
```

La soglia è parte della policy e deve essere versionata come il modello. Se un modello produce probabilità corrette ma la soglia rende la coda ingestibile, il sistema decisionale è comunque sbagliato.

## 8. Interpretabilità e causal caveat

```text
Explanation / feature importance method:
Dataset su cui è calcolato:
Stabilità tra periodi/fold:
Gruppi correlati/proxy:
Feature non modificabili:
Leve con evidenza causale separata:
```

Frase obbligatoria quando pertinente:

> **Feature importance descrive ciò che il modello usa per predire; non dimostra l'effetto di modificare quella feature.**

Se lo score attiva una chiamata, sconto, ispezione o altro trattamento, la card deve inoltre indicare come verrà valutata la policy — randomized holdout, esperimento o altro disegno causale appropriato. Predictive quality risponde a *chi è a rischio*; policy evaluation risponde a *l'azione cambia davvero l'outcome e crea valore netto?*

## 9. Monitoring, retraining e rollback

Il monitoring deve coprire il sistema, non soltanto il modello:

| Layer | Esempi |
|---|---|
| data | schema, missing, freshness, categorie nuove |
| serving | training-serving skew, feature latency |
| score | distribuzione, volume sopra soglia, top-K composition |
| predictive | ranking/error, calibration quando maturano le label |
| operations | selected, contacted, capacity, time-to-action |
| business | outcome, incremental value, costi, guardrail |

Per ciascuno definire:

```text
Metrica:
Frequenza:
Trigger:
Owner:
Azione:
```

Distinguere sempre:

- **recalibration** — corregge score → probabilità;
- **retraining** — riapprende il modello;
- **redesign** — cambia target, feature o policy;
- **rollback/fallback** — torna a una versione o euristica stabile.

I trigger possono essere calendar-based, performance-triggered, drift-triggered o event-triggered dopo cambi di prodotto/policy. Non ogni drift giustifica un retrain.

## 10. Release status, owner e versioni

Registrare almeno:

```text
Model owner:
Business owner:
Data/feature owner:
Model version:
Feature version:
Policy/threshold version:
Training window:
Validation date:
Code/query/pipeline lineage:
```

Uno stato operativo utile può essere:

```text
NOT READY — validation insufficiente
NOT READY — leakage/serving issue
SHADOW MODE
PILOT / HUMAN-IN-THE-LOOP
PRODUCTION WITH CONSTRAINTS
PRODUCTION
FREEZE / RECALIBRATE
ROLLBACK
RETIRED
```

Le limitazioni che cambiano l'uso devono restare visibili, per esempio: *validato solo su Italia e Francia; DACH non verificato; label maturity 60 giorni; calibration instabile per tenure <30 giorni*.

## Template compatto

```text
PREDICTIVE DECISION CARD

Decision / capacity:
Prediction unit / identity:
Prediction time:
Target / horizon / label maturity:
Population / scope:
Feature sources / as-of availability:
Baseline:
Candidate model / version:
Complexity justification:
Validation design:
Ranking / error metrics:
Calibration:
Operating policy / threshold / top-K:
Cost assumptions:
Interpretability / causal caveats:
Policy-effect evaluation:
Monitoring contract:
Retraining / recalibration triggers:
Fallback / rollback:
Owners / lineage:
Release status:
Known limitations:
```

La card dovrebbe permettere a una persona che non ha costruito il sistema di completare questa frase:

> **“Questo sistema produce questa previsione in questo momento, per questa popolazione, usando soltanto queste informazioni; è stato validato in questo modo; attiva questa policy; se degrada o fallisce, faremo questo.”**

> **La Predictive Decision Card documenta la promessa che facciamo quando lasciamo che uno score influenzi una decisione.**