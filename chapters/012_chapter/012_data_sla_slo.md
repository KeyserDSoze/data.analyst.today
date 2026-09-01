## 12.11 SLI, SLO e SLA del dato: definire che cosa significa essere affidabile

“Il dashboard viene aggiornato ogni mattina” non è una garanzia misurabile.

Per un prodotto dati critico dobbiamo tradurre l'aspettativa in proprietà osservabili.

Il vocabolario SRE è utile:

- **SLI — Service Level Indicator**: ciò che misuriamo;
- **SLO — Service Level Objective**: il target che vogliamo rispettare;
- **SLA — Service Level Agreement**: un impegno formale verso un consumer, eventualmente con conseguenze definite.

Google SRE sottolinea che la scelta degli SLO non è puramente tecnica: deve riflettere bisogni degli utenti, costi e trade-off, e un target del 100% è spesso indesiderabile oltre che irrealistico.

Fonte:
https://sre.google/sre-book/service-level-objectives/

### Partire dalla user journey del dato

Per un servizio web una user journey può essere “caricare una pagina”.

Per un prodotto dati può essere:

> **Alle 08:00 il finance analyst apre il report e deve poter prendere una decisione usando dati completi fino alla chiusura di ieri.**

Da qui derivano indicatori più utili di “pipeline verde”.

### Caso simulato/composito — Solaria Energy e il report disponibile ma incompleto

Solaria raccoglie letture da contatori intelligenti.

Il requisito informale è:

> il report deve essere pronto entro le 08:00.

Alle 07:55 il dashboard è interrogabile.

Ma solo il 93% dei meter attesi ha contribuito alla giornata.

Il serving layer è disponibile.

Il prodotto dati non è abbastanza completo per l'uso previsto.

Il team separa quindi gli indicatori.

### Freshness

Domanda:

> Quanto è recente il dato disponibile rispetto al periodo che dovrebbe coprire?

Possibile SLI:

```text
freshness_lag = now - latest_expected_business_time_processed
```

SLO esempio:

```text
99% dei giorni:
dati fino alle 23:59 di T-1 pubblicati entro le 07:30
```

### Completeness

Domanda:

> Quanto dell'input atteso è arrivato ed è stato accettato?

Esempio:

```text
meter_partitions_received / meter_partitions_expected
```

SLO:

```text
>= 99,2% entro le 08:00
```

Freshness e completeness sono indipendenti.

Possiamo avere:

```text
A: timestamp molto recente, 83% completo
B: 60 minuti più vecchio, 99,9% completo
```

La decisione determina quale situazione è tollerabile.

### Availability

Il dataset può essere corretto e completo ma non interrogabile.

Possibile SLI:

```text
successful valid read windows / expected read windows
```

È importante misurarlo dal punto di vista del consumer, non soltanto dalla disponibilità del cluster.

### Correctness / reconciliation

Per alcuni prodotti esiste una reference più autorevole.

Esempio:

```text
warehouse recognized revenue
vs
finance ledger
```

Possiamo definire una tolleranza e misurare quante finestre la rispettano.

Non ogni metrica dispone di una ground truth immediata; in quel caso si usano indicatori di qualità più indiretti.

### Recovery

Quando lo SLO viene violato interessa anche:

> quanto velocemente torniamo a uno stato affidabile?

Possiamo misurare:

- time to detect;
- time to acknowledge;
- time to restore valid serving;
- time to complete reconciliation/backfill.

Il job che riparte non coincide necessariamente con il dato recuperato.

### Error budget: non pretendere affidabilità infinita

Se un SLO è 99,9%, una piccola quota di violazioni è implicitamente tollerata.

Google SRE chiama questa quota **error budget** e la usa per bilanciare affidabilità e velocità di cambiamento.

Fonte:
https://sre.google/sre-book/service-level-objectives/

Nel data system possiamo usare lo stesso principio con prudenza.

Esempio:

```text
SLO: 99% dei daily mart pronti entro 07:30
```

non significa che il restante 1% sia irrilevante.

Significa che abbiamo dichiarato una tolleranza e possiamo decidere cosa fare quando il budget viene consumato troppo rapidamente.

### SLO diversi per consumer diversi

Lo stesso dominio può avere due serving path.

**Operations**

```text
freshness < 10 min
completeness >= 95%
provisional data accettato
```

**Finance close**

```text
freshness T+1
completeness ~100%
reconciliation obbligatoria
nessun dato provisional
```

Non è incoerenza.

Sono user journey differenti.

Google SRE evidenzia proprio che workload e classi di utenti differenti possono richiedere obiettivi distinti.

### Dashboard status: mostrare lo stato del dato

Un pattern pericoloso è:

```text
BI refresh completed → green
```

anche se l'upstream è incompleto.

Un consumer dovrebbe poter distinguere almeno:

```text
READY
DEGRADED
STALE
INCOMPLETE
FAILED
```

con timestamp e caveat visibili.

Lo stato del serving dovrebbe derivare dalle garanzie dell'intero percorso, non dall'ultimo job.

### Campo della Data Flow Architecture Map

Per ogni prodotto critico annotiamo:

```text
consumer journey:
SLI:
SLO target:
measurement point:
compliance window:
error budget / allowed misses:
alert threshold:
degraded behavior:
recovery owner:
```

### Regola operativa

Non chiedere:

> questo dataset è affidabile?

Chiedi:

> **Affidabile per quale consumer, entro quale finestra, con quale livello di completezza e quale comportamento quando l'obiettivo non viene rispettato?**

> **Un dataset affidabile non è quello che “di solito funziona”. È quello per cui abbiamo definito cosa significa funzionare dal punto di vista della decisione che deve supportare.**
