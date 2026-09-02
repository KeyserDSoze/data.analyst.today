## 9.6 Peeking, monitoring e fixed-horizon stopping: guardare non significa decidere

Un team può — e spesso deve — guardare un esperimento mentre gira.

Deve monitorare:

- crash;
- errori;
- SRM;
- missing telemetry;
- latency;
- frodi;
- guardrail gravemente danneggiati.

Il problema nasce quando ogni refresh della dashboard diventa anche una nuova occasione per dichiarare una vittoria statistica con una procedura progettata per una sola analisi finale.

### Caso simulato/composito — Il bottone verde che vince alle 36 ore

| Ore | Lift conversione | p-value nominale |
|---|---:|---:|
| 12 | +1,1% | 0,31 |
| 24 | +1,7% | 0,12 |
| 36 | +2,2% | 0,048 |
| 48 | +1,4% | 0,11 |
| 72 | +0,8% | 0,29 |

Se il team avesse una regola implicita:

> “Controlliamo spesso e fermiamo appena `p < 0,05`”

avrebbe selezionato una fluttuazione favorevole.

Il Capitolo 5 ha già spiegato il significato del p-value. Qui il problema è **procedurale**: il metodo di decisione non corrisponde più al piano statistico.

### Tre tipi di osservazione durante il test

È utile separare:

#### 1. Safety monitoring

Serve a proteggere utenti e business.

Può portare a stop immediato.

Esempi:

- checkout fatal errors +50%;
- pagamenti persi;
- severe crash;
- security incident;
- fraud rate fuori range.

#### 2. Experiment health monitoring

Serve a sapere se il test è interpretabile.

Esempi:

- SRM;
- exposure rate;
- missing telemetry;
- identifier quality;
- latency dei dati;
- invariant metrics.

Può portare a restart o invalidazione.

#### 3. Efficacy decision

Serve a decidere se la variante migliora il prodotto secondo il piano inferenziale.

Qui dobbiamo rispettare la procedura scelta prima del test.

Mescolare questi tre piani crea confusione.

### Fixed horizon

La strategia più semplice è definire ex ante:

```text
MDE / sample requirement
minimum duration
outcome maturity
analysis date
primary metric
alpha / interval procedure
ship threshold
```

La dashboard può essere visibile durante il test, ma la **decisione confermativa** avviene al punto previsto.

Questo è diverso dal fingere che nessuno abbia mai guardato i dati.

È governance: il team sa quali osservazioni autorizzano quale azione.

### Stop per danno e stop per vittoria non sono simmetrici

Se la variante causa un bug grave, non dobbiamo aspettare il sample size.

Uno stop di sicurezza può essere definito come:

```text
if payment_error_rate_B > payment_error_rate_A × 1.20
and absolute excess > threshold
then auto-shutdown
```

Microsoft ExP descrive meccanismi di alert e auto-shutdown per test egregi, proprio per evitare che un feature team debba attendere manualmente mentre gli utenti subiscono un danno.[^ms-during]

Questo non autorizza a usare la stessa logica per fermarsi alla prima oscillazione positiva della primary metric.

### Futility

In alcuni contesti il team può voler fermare un test perché la probabilità di ottenere una conclusione utile è diventata molto bassa.

Ma anche una futility rule deve appartenere al piano statistico.

Non significa:

> “Non ci piace come sta andando, chiudiamo.”

### Formal sequential testing viene dopo

Esistono procedure progettate per prendere decisioni a checkpoint intermedi mantenendo controllato l'errore statistico.

Le approfondiremo nella sezione dedicata al sequential testing.

Qui fissiamo soltanto la regola:

> **se la decisione è sequenziale, anche il metodo inferenziale deve essere sequenziale.**

### Monitoring plan

```text
Safety metrics:
Auto-stop thresholds:
Experiment-health metrics:
SRM policy:
Fixed-horizon or sequential?
If fixed horizon:
  minimum N
  minimum duration
  maturity lag
  final analysis time
Who can stop for safety?
Who can invalidate for data quality?
Who owns efficacy decision?
```

### Un errore organizzativo comune

Il PM guarda conversione.

Engineering guarda crash.

Risk guarda fraud.

Analytics guarda SRM.

Se nessuno ha definito prima **quale segnale ha autorità su quale decisione**, il test può diventare una negoziazione dopo i risultati.

L'Experiment Contract serve anche a questo.

> **La dashboard può essere real-time. La regola decisionale non deve essere improvvisata in real-time.**

[^ms-during]: Microsoft Research, *Patterns of Trustworthy Experimentation: During-Experiment Stage*: https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/
