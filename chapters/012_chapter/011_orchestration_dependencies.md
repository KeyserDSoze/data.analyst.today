## 12.10 Orchestrazione: dipendere dalla readiness, non soltanto dall'orologio

Una pipeline può contenere trasformazioni corrette e pubblicare comunque dati sbagliati se un task parte prima che i suoi input siano realmente pronti. Per questo **scheduling** e **orchestration** rispondono a domande diverse: il primo decide quando provare a partire; la seconda decide quando il downstream è autorizzato a procedere.

### Caso simulato/composito — Meridian Foods e il job puntuale che legge dati vecchi

Meridian Foods usa questo calendario:

```text
ERP export      04:00
orders load     04:30
returns load    04:40
customer load   04:50
margin model    05:10
BI refresh      06:00
```

Per mesi funziona. Poi una mattina l'ERP termina alle 05:05. `orders load` parte comunque alle 04:30 e trova ancora l'estrazione precedente. Tutti i task finiscono `SUCCESS`; il dashboard è puntuale e vecchio.

Il sistema ha scambiato **clock readiness** per **data readiness**.

### Una dipendenza è una condizione di validità

Un DAG può rendere esplicito che `net_revenue_model` dipende da orders, returns e customers. Ma la freccia non dovrebbe significare soltanto “il job upstream è terminato”. Un task può chiudersi tecnicamente pur avendo ricevuto 24 file su 28, quarantinato il 18% delle righe o prodotto zero record per una regione.

La readiness può quindi richiedere:

```text
job complete
AND freshness OK
AND completeness OK
AND schema OK
AND critical invariants OK
```

L'orchestrazione diventa così il punto in cui le garanzie del dato autorizzano il passaggio allo stato successivo.

### Retry e publish boundary

Un timeout di rete può meritare retry automatico; una schema incompatibility no. E un task che ha scritto metà output può diventare pericoloso se viene rilanciato senza idempotenza.

Per questo è utile separare:

```text
compute candidate output
→ validate
→ publish atomically
```

Finché la nuova versione non supera il gate, il consumer vede l'ultima versione valida oppure uno stato esplicitamente stale. Quando l'atomicità completa non è possibile, checkpoint e stati di pubblicazione devono rendere visibile ciò che è completo e ciò che non lo è.

### Backfill: orchestrare anche il passato

Se una business rule era sbagliata dal 1 maggio al 14 giugno, il sistema deve poter riprocessare quella finestra senza duplicare righe, sovrascrivere partizioni non coinvolte o pubblicare risultati parziali prima della validazione.

Lo stesso vale per readiness per partizione. Se Italia e Francia sono pronte ma Germania manca, il comportamento del consumer — bloccare, degradare o pubblicare subset espliciti — è una decisione di prodotto, non un dettaglio dell'orchestratore.

Nella Data Flow Architecture Map documentiamo:

```text
upstream dependencies:
readiness condition:
run trigger:
retry policy:
idempotent? sì/no
checkpoint/publish boundary:
downstream behavior on failure:
backfill support:
owner:
```

> **Una pipeline affidabile non è una sequenza di job che partono all'ora giusta. È una sequenza di stati sufficientemente validi che autorizzano il downstream a procedere.**
