## 12.10 Orchestrazione: dipendere dalla readiness, non soltanto dall'orologio

Una pipeline può contenere trasformazioni corrette e pubblicare comunque un risultato sbagliato se un task parte prima che i suoi input siano realmente pronti.

L'**orchestrazione** coordina:

- dipendenze;
- readiness;
- esecuzione;
- retry;
- failure;
- backfill;
- pubblicazione downstream.

La distinzione centrale è:

> **scheduling dice quando provare a partire; orchestration dice quando è sicuro procedere.**

### Caso simulato/composito — Meridian Foods e il job puntuale che legge dati vecchi

Meridian Foods ha questo calendario:

```text
ERP export      04:00
orders load     04:30
returns load    04:40
customer load   04:50
margin model    05:10
BI refresh      06:00
```

Per mesi funziona.

Una mattina l'ERP termina alle 05:05.

`orders load` parte comunque alle 04:30 e trova ancora l'estrazione precedente.

Tutti i job finiscono `SUCCESS`.

Il dashboard è puntuale e vecchio.

Il problema è che il sistema usa:

```text
clock readiness
```

al posto di:

```text
data readiness
```

### DAG: rendere esplicita la causalità operativa della pipeline

Un Directed Acyclic Graph può rappresentare:

```text
orders --------\
returns --------> net_revenue_model → semantic_model → dashboard
customers -----/
```

Il punto non è il disegno.

È la regola:

> `net_revenue_model` può partire soltanto quando gli input richiesti hanno raggiunto uno stato valido per quella partizione o finestra.

### Completion non significa quality-ready

Un task upstream può tecnicamente terminare anche se:

- ha ricevuto solo 24 file su 28;
- ha quarantinato il 18% delle righe;
- è quattro ore in ritardo;
- ha prodotto zero record per una regione.

Quindi la dependency condition può includere non soltanto:

```text
job_status = SUCCESS
```

ma anche:

```text
freshness OK
completeness OK
schema OK
critical invariants OK
```

Questo collega orchestrazione e SLO del dato.

### Retry: automatico non significa innocuo

Un timeout di rete può meritare un retry.

Una schema incompatibility probabilmente richiede intervento.

Un task che ha scritto metà output e poi fallisce può essere pericoloso da ritentare se non è idempotente.

Per ogni task dobbiamo sapere:

```text
can retry safely? sì/no
writes atomically? sì/no
checkpoint available? sì/no
replay duplicates? possible/impossible
```

### Idempotenza e publish boundary

Un pattern utile è separare:

```text
compute candidate output
→ validate
→ publish/replace atomically
```

In questo modo un failure intermedio non rende visibile metà dataset come se fosse la nuova versione ufficiale.

Quando l'atomicità completa non è disponibile, servono checkpoint e stati espliciti.

### Backfill: l'orchestrazione nel passato

Se scopriamo che una business rule era sbagliata dal 1 maggio al 14 giugno, il sistema deve poter eseguire:

```text
recompute 2026-05-01 ... 2026-06-14
```

senza:

- duplicare dati;
- sovrascrivere partizioni non coinvolte;
- utilizzare sorgenti incoerenti con il periodo;
- aggiornare i consumer prima che l'intero backfill sia validato.

Il backfill non è una funzione di emergenza opzionale. È parte della capacità di correggere l'evidenza storica.

### Partition readiness

In pipeline grandi può essere utile ragionare per partizione o finestra.

Esempio:

```text
country=IT/date=2026-08-31 READY
country=FR/date=2026-08-31 READY
country=DE/date=2026-08-31 MISSING
```

A questo punto il consumer deve sapere se può:

- pubblicare IT/FR separatamente;
- attendere DE;
- pubblicare globale con warning;
- bloccare tutto.

Questa è una decisione di prodotto, non solo di orchestratore.

### Failure propagation

Ogni nodo della Data Flow Architecture Map dovrebbe avere una policy:

```text
upstream fails
→ downstream BLOCK / DEGRADE / USE LAST KNOWN GOOD
```

Per un dashboard executive potrebbe essere meglio mostrare:

```text
Dati aggiornati al 31 agosto 07:00 — refresh odierno non completo
```

piuttosto che pubblicare silenziosamente dati parziali.

### Campo della Data Flow Architecture Map

Per ogni task critico annotiamo:

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

### Regola operativa

Quando un numero è in ritardo o anomalo, non chiediamo soltanto:

> la query finale è corretta?

Chiediamo anche:

> **Quali precondizioni dovevano essere vere prima che questa query fosse autorizzata a pubblicare il risultato?**

> **Una pipeline affidabile non è una sequenza di job che partono all'ora giusta. È una sequenza di stati validi che autorizzano il downstream a procedere.**
