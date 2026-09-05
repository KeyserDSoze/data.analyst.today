## 9.2 Metric Contract: decidere prima che cosa significa vincere

Un esperimento raramente sposta una sola cosa. QuickPay può aumentare conversione e, nello stesso momento, aumentare chargeback, cancellazioni impulsive, ticket di supporto o latency. La scorecard deve quindi rappresentare **la decisione completa**, non soltanto il comportamento locale che la feature vuole muovere.

Per questo le metriche hanno ruoli diversi. La **Primary / Overall Evaluation Criterion (OEC)** rappresenta il beneficio principale che giustificherebbe la decisione; i **guardrail** definiscono danni che non accettiamo oltre una soglia; le **diagnostic metrics** aiutano a capire il meccanismo; le **data-quality / experiment-health metrics** dicono se il confronto è interpretabile. Microsoft Experimentation Platform usa una tassonomia molto simile nelle proprie scorecard e nei pattern di trustworthy experimentation.[^ms-metric-patterns]

### QuickPay: una conversione migliore può essere un NO-SHIP

Dopo il periodo pianificato osserviamo:

| Metrica | Controllo | QuickPay | Delta |
|---|---:|---:|---:|
| Conversion user → order | 3,93% | 4,12% | +0,19 pp |
| Chargeback | 0,42% | 0,61% | +0,19 pp |
| Cancellazioni entro 24h | 2,8% | 3,6% | +0,8 pp |
| Support contacts / 1.000 ordini | 14,1 | 18,7 | +32,6% |

La frase “B è significativa sulla conversione” è statisticamente possibile e decisionariamente insufficiente. Se la feature genera più ordini ma una quota maggiore viene annullata, contestata o richiede supporto, la metrica locale sta descrivendo soltanto una parte del sistema.

La primary potrebbe quindi essere più vicina al valore, per esempio contribution margin per eligible user, net revenue per user o completed-and-not-cancelled orders per user. Ma una metrica molto vicina al valore può maturare lentamente o essere più rumorosa. Il design sperimentale deve trovare un compromesso tra **rilevanza business, sensibilità, latenza, tracking e interpretabilità**, dichiarandolo prima del test.

### Un guardrail deve avere autorità sulla decisione

“Monitoriamo frodi” non è ancora un guardrail. Serve una soglia che stabilisca quando il danno blocca lo ship. Per esempio:

```text
Primary:
conversion per eligible user
success threshold: almeno +0,10 pp

Guardrail 1:
chargeback rate
non-inferiority margin: peggioramento massimo +0,05 pp

Guardrail 2:
checkout fatal error
stop operativo se +20% relativo

Guardrail 3:
cancellation D1
ship blocked se peggiora oltre +0,30 pp
```

A quel punto un test con primary positiva può terminare correttamente come **NO-SHIP**. Per molti guardrail la domanda non è “esiste una differenza significativa?”, ma “possiamo escludere un peggioramento più grande della soglia che consideriamo materialmente dannosa?”. È una logica vicina alla non-inferiority e costringe il team a dichiarare il rischio accettabile prima di conoscere il delta.

### Le diagnostic metrics spiegano, non riscrivono la vittoria

Se la primary è piatta e una delle 35 metriche diagnostiche cresce molto, il pattern può generare una nuova ipotesi. Non dovrebbe però diventare retroattivamente la nuova definizione di successo. La distinzione tra confermativo ed esplorativo del Capitolo 5 vale anche nella scorecard sperimentale.

Lo stesso principio vale per le metriche di health. SRM, exposure rate, event completeness, missing identifiers e logging differences devono comparire **prima** del lift. Un test può avere un risultato business spettacolare e non meritare interpretazione se il sistema di misura ha costruito gruppi differenti da quelli previsti.

### Il denominatore è parte del trattamento analitico

`conversion_rate` non è una definizione sufficiente. Una specifica più robusta è:

```text
Nome: eligible-user conversion D7
Numeratore: utenti con >=1 ordine valido entro 7 giorni dalla prima eligibility
Denominatore: utenti randomizzati eleggibili
Deduplicazione: 1 per stable_user_id
Cancellazioni: ordine valido solo se non cancellato entro 24h
Late events: finestra di maturazione 48h
Timezone: UTC per event time
```

Questa precisione impedisce che A e B vengano calcolati con una semantica mobile. Nel Capitolo 11 torneremo sulle metriche come oggetti del semantic layer; qui ci interessa che la metrica resti congelata durante il test.

Microsoft ExP documenta anche alert e, per regressioni gravi, meccanismi di auto-shutdown su metriche business-critical. Il punto non è automatizzare ogni decisione, ma rendere i guardrail **controlli operativi** anziché commenti ex post.[^ms-alerting]

### Metric Contract

```text
Decisione:
Primary/OEC:
Definizione completa:
Unità/denominatore:
Success threshold / MDE:
Guardrail:
Margin per ogni guardrail:
Diagnostic metrics:
Data-quality metrics:
Maturazione outcome:
Late data policy:
Multiple-testing family:
Quali metriche possono bloccare ship?
Quali metriche sono solo esplorative?
```

> **Una metrica sperimentale non è soltanto una formula. È una regola concordata su quale evidenza può cambiare la decisione e quale danno rende inaccettabile una vittoria locale.**

[^ms-metric-patterns]: Microsoft Research, *Patterns of Trustworthy Experimentation: During-Experiment Stage*: https://www.microsoft.com/en-us/research/?p=720145
[^ms-alerting]: Microsoft Research, *Alerting in Microsoft’s Experimentation Platform (ExP)*: https://www.microsoft.com/en-us/research/articles/alerting-in-microsofts-experimentation-platform-exp/
