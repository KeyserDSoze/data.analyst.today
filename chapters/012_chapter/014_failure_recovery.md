## 12.13 Failure e recovery: tornare a uno stato affidabile, non soltanto far ripartire il job

Una pipeline affidabile non è quella che non fallisce mai. È quella che rende il failure visibile, limita la propagazione, sa quale versione è ancora valida e può recuperare senza perdere o duplicare dati.

Soprattutto, sa dimostrare che il risultato recuperato è di nuovo utilizzabile.

### Caso simulato/composito — Helix Pharma e il caricamento parziale

Helix riceve ogni notte dati da **42 mercati**:

```text
files
→ schema validation
→ currency normalization
→ warehouse load
→ commercial mart
```

Durante il mercato brasiliano il job si interrompe dopo aver scritto una parte delle righe. La domanda operativa non è soltanto “come rilanciamo il task?”, ma:

> **Quale parte dell'output è visibile, quale è completa e quale stato possiamo ancora considerare valido?**

### Il publish boundary protegge il consumer

Quando possibile separiamo:

```text
processing area
→ validation
→ publish boundary
```

Se il nuovo output non supera il gate, il consumer continua a vedere la **last known good version** oppure uno stato esplicitamente stale. È spesso preferibile a un dataset che mescola metà giornata nuova e metà vecchia.

L'atomicità rende semplice il passaggio `old valid → new valid`. Quando non è disponibile servono checkpoint e scritture idempotenti, perché un retry su output parziale non trasformi il recovery in duplicazione.

### Il tipo di failure determina la risposta

Un network timeout è transient e può meritare retry con backoff. Una schema incompatibility o una violazione di contract è deterministica: riprovare cento volte non la risolve. Un partial-write failure richiede invece sapere se il task può essere rigiocato in sicurezza o se serve rollback/cleanup.

Anche la quarantena va trattata come stato esplicito. Separare pochi record invalidi può mantenere il servizio disponibile, ma se il 15% delle righe è in quarantine e il dashboard resta verde abbiamo soltanto nascosto il failure.

### BLOCK, DEGRADE o LAST KNOWN GOOD

Il comportamento deve dipendere dalla decisione. Possiamo bloccare la pubblicazione se un aggregato globale sarebbe fuorviante, degradare servendo soltanto subset validi con caveat, oppure mostrare l'ultima versione affidabile marcandola come stale.

La stessa logica vale per **RPO** e **RTO**. Un sistema antifrode e un report settimanale non possono avere gli stessi obiettivi di perdita tollerabile e tempo di ripristino. Gli obiettivi devono essere compatibili con retention, snapshot e capacità di replay.

### Recovery verification

La recovery non termina quando il job torna verde. Dopo il ripristino dobbiamo verificare almeno:

```text
uniqueness
completeness
freshness
reconciliation
partition coverage
no duplicate replay
```

Un caso particolarmente pericoloso è ricevere **41 mercati su 42** senza alcuna exception: il job può terminare `SUCCESS` mentre il dato è incompleto. Per questo la recovery dipende anche dalle aspettative di completeness.

Per asset critici serve un runbook che indichi sintomo, failure boundary probabili, controlli, last known good, safe retry, rollback, backfill, comunicazione ai consumer e recovery validation.

Nella Data Flow Architecture Map annotiamo:

```text
failure modes:
partial-write behavior:
retry class:
idempotent? sì/no
checkpoint:
last known good state:
degraded serving policy:
RPO:
RTO:
replay/backfill source:
recovery validation:
owner/on-call:
```

> **Recovery non significa riaccendere la pipeline. Significa tornare a una versione dell'evidenza di cui possiamo nuovamente difendere completezza, correttezza e provenienza.**
