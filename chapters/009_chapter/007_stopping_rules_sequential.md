## 9.6 Monitoring e stopping: guardare il test non significa ridisegnare la decisione

Un esperimento in produzione deve essere osservato mentre gira. Crash, pagamenti persi, SRM, missing telemetry, latency, frodi o guardrail gravemente danneggiati non possono aspettare il final read. Il problema nasce quando ogni refresh della dashboard diventa anche una nuova occasione per dichiarare una vittoria con una procedura inferenziale progettata per una sola analisi finale.

### Caso simulato/composito — Il bottone verde che vince alle 36 ore

| Ore | Lift conversione | p-value nominale |
|---|---:|---:|
| 12 | +1,1% | 0,31 |
| 24 | +1,7% | 0,12 |
| 36 | +2,2% | 0,048 |
| 48 | +1,4% | 0,11 |
| 72 | +0,8% | 0,29 |

Se la regola implicita è “controlliamo spesso e fermiamo appena `p < 0,05`”, il team seleziona una fluttuazione favorevole. Il problema non è che abbia guardato i dati: è che **la frequenza delle decisioni non corrisponde al metodo inferenziale dichiarato**.

Microsoft ExP, discutendo test event-based e monitoring durante gli esperimenti, richiama esplicitamente il rischio di p-hacking/peeking e la necessità di metodi sequential quando si vuole prendere decisioni ripetute durante il run.[^ms-event][^ms-during]

### Tre autorità diverse durante lo stesso test

Conviene separare tre tipi di monitoraggio.

Il **safety monitoring** protegge utenti e business: severe crash, payment loss, security incident o fraud fuori soglia possono giustificare uno stop immediato. L'**experiment-health monitoring** controlla se il confronto è ancora interpretabile: SRM, exposure, identity, missing telemetry e metric invariants possono portare a restart o invalidazione. La **efficacy decision** stabilisce invece se B produce il beneficio previsto dalla primary secondo il piano inferenziale.

Queste tre autorità non sono simmetriche. Un checkout che rompe i pagamenti può essere spento dopo un'ora; una primary metric positiva non ottiene automaticamente la stessa licenza di fermare il test dopo un'ora.

### Fixed horizon come governance

Nel regime fixed horizon il team dichiara ex ante:

```text
MDE / sample requirement
minimum duration
outcome maturity
final analysis time
primary metric
alpha / interval procedure
ship threshold
```

La dashboard può essere visibile durante tutto il run. La decisione confermativa, però, avviene al punto previsto. Non stiamo fingendo che nessuno abbia mai visto un numero; stiamo stabilendo quali segnali possono autorizzare quale azione.

Gli stop per safety possono avere regole dedicate, per esempio:

```text
if payment_error_rate_B > payment_error_rate_A × 1.20
and absolute excess > threshold
then auto-shutdown
```

Microsoft ExP documenta alert e auto-shutdown per regressioni severe proprio per ridurre il danno mentre il test è in corso.[^ms-during]

### Se vogliamo decidere più volte, cambiamo il design

Esistono procedure sequenziali progettate per checkpoint intermedi mantenendo il controllo dell'errore statistico. La sezione 9.13 le tratterà come un regime inferenziale distinto. Il principio da fissare qui è semplice:

> **se la decisione è sequenziale, anche l'inferenza deve essere sequenziale.**

Lo stesso vale per futility: fermarsi perché continuare non produrrà probabilmente informazione utile può essere sensato, ma la regola deve appartenere al design, non alla delusione del momento.

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

Questa separazione è anche organizzativa. Product può guardare conversione, Engineering crash, Risk frodi e Analytics SRM. Se non è stato deciso prima quale segnale ha autorità su quale azione, il test diventa una negoziazione dopo i risultati.

> **La dashboard può essere real-time. La regola che trasforma un numero in una decisione non deve essere improvvisata in real-time.**

[^ms-event]: Microsoft Research, *For Event-based A/B tests: why they are special*: https://www.microsoft.com/en-us/research/articles/for-event-based-a-b-tests-why-they-are-special/
[^ms-during]: Microsoft Research, *Patterns of Trustworthy Experimentation: During-Experiment Stage*: https://www.microsoft.com/en-us/research/?p=720145
