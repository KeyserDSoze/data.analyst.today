## 12.13 Failure e recovery: tornare a uno stato affidabile, non soltanto far ripartire il job

Una pipeline affidabile non è quella che non fallisce mai.

È quella che, quando fallisce:

- rende il problema visibile;
- limita la propagazione;
- sa quale stato è ancora valido;
- può recuperare senza duplicare o perdere dati;
- dimostra che il risultato recuperato è di nuovo affidabile.

### Caso simulato/composito — Helix Pharma e il caricamento parziale

Helix riceve ogni notte dati da 42 mercati.

Il flusso è:

```text
files
→ schema validation
→ currency normalization
→ warehouse load
→ commercial mart
```

Durante il mercato brasiliano il job si interrompe dopo aver scritto una parte delle righe.

La domanda operativa non è soltanto:

> come rilanciamo il task?

È:

> **quale parte dell'output è visibile, quale è completa e quale stato possiamo ancora considerare valido?**

### Failure boundary: impedire che il problema diventi una verità pubblicata

Un buon design separa quando possibile:

```text
processing area
→ validation
→ publish boundary
```

Se la trasformazione fallisce prima del publish, il consumer continua a vedere:

```text
last known good version
```

oppure uno stato esplicitamente stale.

È spesso meglio di esporre metà della nuova giornata insieme a metà della vecchia.

### Atomicità e checkpoint

L'ideale è che una pubblicazione importante sia atomica:

```text
old valid version
→ new valid version
```

senza uno stato intermedio visibile.

Quando non è possibile, servono checkpoint affidabili.

Esempio:

```text
partition=BR/date=2026-08-30
last_successful_chunk=0187
```

Ma un checkpoint è utile soltanto se il task che riprende è coerente con ciò che era già stato scritto.

### Retry taxonomy

Non tutti i failure sono uguali.

**Transient**

- network timeout;
- temporary rate limit;
- short service outage.

Può meritare retry automatico con backoff.

**Deterministic/data failure**

- schema incompatibile;
- chiave mancante;
- violazione contract;
- file corrotto.

Ritentare cento volte lo stesso input non aiuta.

**Partial-write failure**

Richiede capire se il retry è idempotente o deve prima pulire/rollbackare lo stato incompleto.

### Quarantena: continuare senza nascondere la perdita

Un flusso può separare:

```text
valid records   → curated output
invalid records → quarantine
```

Questa scelta può mantenere disponibile il servizio quando pochi record sono problematici.

Ma la quarantena deve avere un suo contract:

- volume massimo tollerato;
- motivo;
- owner;
- tempo massimo di permanenza;
- backfill dopo correzione.

Se il 15% delle righe è in quarantena e il dashboard resta verde, abbiamo semplicemente nascosto il failure.

### Partial availability: BLOCK, DEGRADE o LAST KNOWN GOOD

Per ogni prodotto critico serve una policy.

**BLOCK**

Non pubblicare nulla se manca una regione.

Adatto quando l'aggregato sarebbe fuorviante.

**DEGRADE**

Pubblicare subset validi con caveat visibile.

Adatto quando i consumer possono lavorare per regione indipendentemente.

**LAST KNOWN GOOD**

Servire la versione precedente, marcandola come stale.

Adatto quando un dato vecchio è più utile di un dato parziale.

La scelta dipende dalla decisione.

### RPO e RTO

Due concetti classici di disaster recovery aiutano anche nei sistemi dati.

**RPO — Recovery Point Objective**

Quanta storia recente possiamo permetterci di non recuperare immediatamente?

**RTO — Recovery Time Objective**

Quanto tempo possiamo impiegare per ripristinare il servizio?

Un fraud pipeline e un report settimanale possono avere obiettivi radicalmente diversi.

Questi parametri devono essere coerenti con retention dei source logs, snapshot e capacità di replay.

### Recovery verification

Una recovery non è conclusa quando il job torna verde.

Dobbiamo verificare almeno:

```text
uniqueness
completeness
freshness
reconciliation
partition coverage
no duplicate replay
```

Se abbiamo riprocessato una finestra, confrontiamo anche:

```text
before incident
vs
recovered result
```

sui componenti sensibili.

### Caso silenzioso: 41 mercati su 42

Il failure più pericoloso può non generare exception.

Se arrivano solo 41 file su 42 e il codice processa semplicemente ciò che trova, il task può terminare `SUCCESS`.

Per questo il recovery design dipende anche da **expected completeness**, non soltanto dagli errori tecnici.

### Runbook: cosa facciamo alle 03:00?

Per asset importanti è utile avere un runbook che risponda a:

```text
symptom:
likely failure boundaries:
checks:
last known good state:
safe retry procedure:
rollback:
backfill:
consumer communication:
recovery validation:
```

Il valore del runbook emerge quando la persona che interviene non è l'autore originale della pipeline.

### Campo della Data Flow Architecture Map

Per ogni nodo critico annotiamo:

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

### Regola operativa

Quando qualcuno dice:

> “La pipeline è stata ripristinata.”

la domanda dell'analista è:

> **Abbiamo ripristinato il processo o abbiamo dimostrato di aver ripristinato uno stato del dato sufficientemente completo, corretto e riconciliato per essere usato di nuovo?**

> **Recovery non significa riaccendere il sistema. Significa tornare a una versione dell'evidenza di cui possiamo nuovamente difendere l'affidabilità.**
