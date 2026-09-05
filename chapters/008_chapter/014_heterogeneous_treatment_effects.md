## 8.13 Effetti eterogenei: non basta sapere che “in media funziona”

Il Capitolo 6 ha usato segmenti e coorti per localizzare dove il comportamento differisce. Qui la domanda è più forte: **lo stesso trattamento produce effetti causali diversi in popolazioni differenti?** Non basta osservare che due segmenti hanno outcome diversi; dobbiamo confrontare il contrasto trattamento-controllo all'interno di ciascun segmento.

### Caso simulato/composito — Campagna retention

Un esperimento produce churn **18,4%** nel controllo e **15,9%** nel trattamento, per un effetto medio di `-2,5 pp`. La media è utile, ma può nascondere differenze operative.

Per tenure:

| Segmento | Effetto stimato sul churn |
|---|---:|
| < 3 mesi | -0,3 pp |
| 3–12 mesi | -3,8 pp |
| > 12 mesi | -5,1 pp |

Per valore cliente:

| Segmento | Effetto stimato |
|---|---:|
| basso | -0,7 pp |
| medio | -2,9 pp |
| alto | -6,4 pp |

A questo punto la decisione non è più soltanto “la campagna funziona?”, ma “per chi l'effetto è abbastanza grande da giustificare costo e capacità?”. È qui che ATE, ATT e **CATE** smettono di essere sigle teoriche e diventano estimand differenti.

### Outcome level non è treatment effect

Un errore frequente consiste nel confrontare livelli di retention tra segmenti e chiamarli eterogeneità dell'effetto. Se otteniamo:

| Segmento | Controllo | Trattamento | Effetto |
|---|---:|---:|---:|
| SMB | 70% | 73% | +3 pp |
| Enterprise | 90% | 93% | +3 pp |

gli enterprise hanno retention molto più alta, ma l'effetto stimato è identico. L'eterogeneità causale riguarda **la differenza delle differenze tra trattamento e controllo**, non il livello dell'outcome.

Il prezzo della granularità è l'incertezza. Un CATE può essere più vicino alla decisione, ma dividere il campione riduce informazione. Un effetto di `-12 pp` su **38 clienti** non è automaticamente più interessante di `-4 pp` su **8.000**. Denominatori, intervalli, stabilità temporale, plausibilità del meccanismo e replica diventano ancora più importanti.

### Pre-specificare dove possibile

Se esploriamo cinquanta segmenti dopo aver visto i risultati, qualche effetto sembrerà eccezionale per puro caso. Il Capitolo 5 ci ha già fornito il linguaggio di multiple testing e uncertainty; qui va applicato ai treatment effects. Dobbiamo distinguere heterogeneity ipotizzata prima del test, analisi esplorativa post hoc, risultati replicati e pattern basati su piccoli campioni. Quando appropriato, tecniche di shrinkage o partial pooling possono aiutare a evitare che il rumore dei segmenti piccoli venga scambiato per policy.

Causal forests, meta-learners e uplift models possono esplorare strutture complesse di heterogeneity, ma non sostituiscono l'identificazione. Se il trattamento è confuso in modo non risolto, l'algoritmo non trasforma l'associazione in treatment effect. L'ordine rimane:

**design credibile → effetto identificabile → eterogeneità**.

### Dall'effetto alla convenienza

Anche un CATE credibile non decide da solo la policy. Supponiamo che una chiamata costi **40 €**. Nel segmento A riduce il churn di **2 pp** su clienti con margine **80 €**; nel segmento B lo riduce di **5 pp** su clienti con margine **2.000 €**. La priorità deve mettere insieme effetto, valore dell'outcome evitato e costo dell'intervento:

`effect × valore dell'outcome - costo intervento`

Questo ponte verrà sviluppato nel Capitolo 15, ma la causal analysis deve già evitare di confondere “effetto maggiore” con “decisione migliore”.

Lo stesso principio emerge in un marketplace che aumenta la commissione. Se l'effetto medio sui seller attivi è `-1,2%`, ma le stime sono `-0,1%` enterprise, `-0,8%` mid-market e `-6,7%` per piccoli seller a basso margine, una policy differenziata può essere più sensata di un rollback totale — purché gli effetti siano sufficientemente precisi, non frutto di esplorazione opportunistica e materialmente rilevanti.

La **Heterogeneity card** conserva il controllo decisionale:

```text
Estimand medio:
Dimensioni di heterogeneity definite prima?
Effetto per segmento, non solo outcome level:
Denominatori:
Intervalli / uncertainty:
Multiple comparisons gestite?
Pattern replicato?
Meccanismo plausibile?
Valore economico per segmento:
Policy che cambierebbe:
```

> **La media dice che cosa succede complessivamente. L'eterogeneità serve a capire se la stessa policy debba davvero essere applicata a tutti.**

Questa distinzione prepara un ultimo errore molto comune: usare il **rischio previsto** come se misurasse la **persuadibilità** all'intervento.
