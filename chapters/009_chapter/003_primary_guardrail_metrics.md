## 9.2 Metric Contract: decidere prima che cosa significa vincere

Un esperimento raramente muove una sola cosa.

QuickPay può aumentare conversione e contemporaneamente:

- aumentare chargeback;
- ridurre il tempo al checkout;
- aumentare cancellazioni impulsive;
- modificare il basket;
- creare più ticket;
- peggiorare latency.

Per questo le metriche devono avere **ruoli differenti**, definiti prima di vedere il risultato.

### Quattro famiglie di metriche

Una struttura utile è:

1. **Primary / Overall Evaluation Criterion (OEC)** — la metrica che sintetizza il successo principale rispetto alla decisione;
2. **Guardrail** — ciò che non deve peggiorare oltre una soglia accettabile;
3. **Diagnostic / local feature metrics** — aiutano a capire dove e come cambia il comportamento;
4. **Data-quality / experiment-health metrics** — dicono se il test è tecnicamente interpretabile.

Microsoft Experimentation Platform usa una tassonomia molto simile, distinguendo data-quality metrics, OEC metrics, local/feature metrics e guardrail metrics nel monitoraggio degli esperimenti.[^ms-metric-patterns]

### Caso simulato/composito — QuickPay “vince” sulla conversione

Dopo il periodo pianificato:

| Metrica | Controllo | QuickPay | Delta |
|---|---:|---:|---:|
| Conversion user → order | 3,93% | 4,12% | +0,19 pp |
| Chargeback | 0,42% | 0,61% | +0,19 pp |
| Cancellazioni entro 24h | 2,8% | 3,6% | +0,8 pp |
| Support contacts / 1.000 ordini | 14,1 | 18,7 | +32,6% |

Dire soltanto:

> “B è statisticamente significativa sulla conversione.”

ignora la domanda decisionale.

### Primary metric: proxy o valore?

La conversione è vicina al comportamento che la feature modifica.

Ma il business potrebbe realmente voler massimizzare:

- contribution margin per utente;
- net revenue per eligible user;
- completed-and-not-cancelled orders per user.

Una primary metric troppo distante dal valore può premiare comportamenti che non vogliamo.

Una metrica troppo lenta, però, può rendere impossibile un test pratico.

Quindi la scelta è un compromesso tra:

- vicinanza al valore business;
- sensibilità;
- latenza dell'outcome;
- affidabilità del tracking;
- interpretabilità.

### Guardrail con soglia, non decorativi

Scrivere “monitoriamo frodi” non è sufficiente.

Un guardrail deve specificare **quando blocca la decisione**.

Esempio:

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

A quel punto un test può avere una primary positiva e restare **NO-SHIP**.

### Non-inferiority come logica di guardrail

Per molti guardrail la domanda non è:

> “La variante è significativamente diversa?”

ma:

> **“Possiamo escludere con sufficiente confidenza un peggioramento più grande della soglia che consideriamo materialmente dannosa?”**

Questo è più vicino a una logica di non-inferiority.

La soglia deve essere scelta prima e giustificata dal rischio business, non dopo aver osservato il delta.

### Diagnostic metrics non devono diventare primary retroattive

Immaginiamo che la primary sia piatta, ma una delle 35 diagnostic metric cresca molto.

Possiamo usare il risultato per generare una nuova ipotesi.

Non dovremmo riscrivere la storia come:

> “Il test è riuscito perché quella era in realtà la metrica importante.”

La distinzione tra confermativo ed esplorativo del Capitolo 5 vale anche qui.

### Data-quality metric prima del business outcome

Un dashboard sperimentale maturo dovrebbe visualizzare prima:

- SRM;
- exposure rate;
- event completeness;
- missing identifiers;
- metric invariants;
- logging differences.

Solo dopo ha senso discutere lift e intervalli.

### Denominatore e unità devono entrare nel metric contract

`conversion_rate` non è una definizione sufficiente.

Scriviamo:

```text
Nome: eligible-user conversion D7
Numeratore: utenti con >=1 ordine valido entro 7 giorni dalla prima eligibility
Denominatore: utenti randomizzati eleggibili
Deduplicazione: 1 per stable_user_id
Cancellazioni: ordine considerato valido solo se non cancellato entro 24h
Late events: finestra di maturazione 48h
Timezone: UTC per event time
```

Il Capitolo 11 formalizzerà ulteriormente le metriche nel semantic layer. Nell'esperimento questa precisione serve a impedire che A e B vengano calcolati con una semantica mobile.

### Caso reale documentato — Alerting sugli esperimenti Microsoft

Microsoft ExP documenta alert su SRM e su metriche che si muovono fuori da range prestabiliti. L'obiettivo è individuare rapidamente test che degradano seriamente prodotto o user experience, fino ad arrivare in alcuni casi all'auto-shutdown di esperimenti egregi.[^ms-alerting]

Questo trasforma i guardrail da tabella osservata ex post a **controllo operativo durante l'esecuzione**.

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

> **Una metrica sperimentale non è soltanto una formula. È una regola concordata su quale evidenza può cambiare la decisione.**

[^ms-metric-patterns]: Microsoft Research, *Patterns of Trustworthy Experimentation: During-Experiment Stage*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/
[^ms-alerting]: Microsoft Research, *Alerting in Microsoft’s Experimentation Platform (ExP)*: https://www.microsoft.com/en-us/research/articles/alerting-in-microsofts-experimentation-platform-exp/
