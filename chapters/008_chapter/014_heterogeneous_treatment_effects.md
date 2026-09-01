## 8.13 Effetti eterogenei: non basta sapere che “in media funziona”

Il Capitolo 6 ha usato segmenti e coorti per localizzare **dove il comportamento differisce**.

Qui la domanda è più forte:

> **L'effetto causale dello stesso trattamento cambia tra popolazioni differenti?**

Questa è causal heterogeneity, non semplice segmentazione descrittiva.

### Caso simulato/composito — Campagna retention

Un esperimento produce:

- churn controllo: 18,4%;
- churn trattamento: 15,9%;
- effetto medio: `-2,5 pp`.

La media è utile, ma può nascondere differenze operative.

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

La domanda diventa:

> “Per chi l'effetto è abbastanza grande da giustificare costo e capacità operativa?”

### ATE, ATT e CATE non sono sinonimi

- **ATE:** effetto medio nella popolazione target;
- **ATT:** effetto medio sulle unità trattate;
- **CATE:** effetto medio condizionato a caratteristiche `X`.

Un CATE può essere più vicino alla decisione, ma è anche più difficile da stimare in modo stabile.

Dividere il campione riduce informazione e aumenta il rischio di trovare pattern casuali.

### Heterogeneity richiede un effect contrast, non due retention rate separate

Errore comune:

> “Il gruppo enterprise ha retention più alta, quindi il trattamento funziona meglio sugli enterprise.”

Per dire che l'effetto è diverso dobbiamo confrontare **l'effetto trattamento-controllo dentro i segmenti**, non i livelli assoluti dell'outcome.

Esempio:

| Segmento | Controllo | Trattamento | Effetto |
|---|---:|---:|---:|
| SMB | 70% | 73% | +3 pp |
| Enterprise | 90% | 93% | +3 pp |

Gli enterprise hanno retention maggiore, ma l'effetto stimato è identico.

### Pre-specificato vs esplorativo

Se analizziamo 50 segmenti dopo aver visto i risultati, qualcosa sembrerà eccezionale per caso.

Distingui sempre:

- heterogeneity ipotizzata prima del test;
- analisi esplorativa post hoc;
- risultati replicati;
- pattern basati su piccoli denominatori.

Il Capitolo 5 ci ha già dato il linguaggio per multiple testing e incertezza. Qui lo applichiamo agli effetti causali.

### Segmenti troppo granulari

Un effetto di `-12 pp` su 38 clienti non va trattato come automaticamente più interessante di `-4 pp` su 8.000 clienti.

Servono:

- intervalli;
- denominatori;
- stabilità temporale;
- plausibilità del meccanismo;
- eventuale shrinkage/partial pooling quando appropriato;
- replica.

### Causal ML non elimina l'identificazione

Causal forests, meta-learners e uplift models possono aiutare a trovare eterogeneità complessa.

Ma se il trattamento è confuso in modo non identificato, l'algoritmo non trasforma magicamente l'associazione in causal effect.

L'ordine resta:

**design credibile → effetto identificabile → eterogeneità**.

Non:

**algoritmo sofisticato → causalità**.

### Dall'effetto al valore decisionale

Supponiamo che una chiamata costi 40 €.

Segmento A:

- riduzione churn: 2 pp;
- margine cliente: 80 €.

Segmento B:

- riduzione churn: 5 pp;
- margine cliente: 2.000 €.

Anche se il CATE è la metrica causale, la priorità finale richiede economia:

`effect × valore dell'outcome - costo intervento`

Questo ponte verrà sviluppato nel Capitolo 15.

### Caso simulato/composito — Pricing seller

Un marketplace aumenta la commissione.

Effetto medio sui seller attivi: `-1,2%`.

Per segmento:

- enterprise: -0,1%;
- mid-market: -0,8%;
- piccoli seller a basso margine: -6,7%.

La decisione può diventare pricing differenziato invece di rollback totale.

Ma prima di farlo dobbiamo sapere se questi effetti sono:

- sufficientemente precisi;
- pre-specificati o scoperti post hoc;
- replicabili;
- economicamente rilevanti.

### Heterogeneity card

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

> **La media dice se un intervento funziona nel complesso. L'eterogeneità serve a capire se la stessa policy debba davvero essere applicata a tutti.**
