## 8.10 Regression Discontinuity: quando una soglia modifica il trattamento

Molti processi assegnano interventi tramite cutoff:

- supporto premium sopra un ARR minimo;
- chiamata retention sotto un health score;
- credito sopra una soglia;
- incentivo oltre una performance threshold;
- spedizione gratuita sopra un valore d'ordine.

Quando il trattamento cambia bruscamente a una soglia, le unità appena sopra e appena sotto possono offrire un confronto quasi-sperimentale.

Questa è l'intuizione della **Regression Discontinuity Design (RDD)**.

### Caso simulato/composito — Health score 60

Un SaaS assegna automaticamente una chiamata proattiva agli account con `health_score < 60`.

Confrontare tutti i trattati con tutti i non trattati sarebbe sbagliato: i trattati sono, per definizione, più a rischio.

Ma vicino alla soglia:

| Health score | Chiamata | Churn 30 gg |
|---|---|---:|
| 58–59 | sì | 13,2% |
| 60–61 | no | 16,7% |

Il salto locale è circa `-3,5 pp`.

Se le unità appena sotto e sopra 60 sarebbero altrimenti comparabili, quel salto può identificare un effetto causale **locale**.

### L'assunzione chiave è la continuità del controfattuale

L'idea non è che score 59 e 60 siano identici.

È che, in assenza del trattamento, l'outcome atteso cambierebbe **in modo continuo** attraversando il cutoff.

Se proprio a 60 cambia soltanto l'accesso alla chiamata, una discontinuità nell'outcome è informativa sul trattamento.

La World Bank presenta RDD come confronto tra unità vicine a una soglia di eleggibilità, sottolineando che la credibilità deriva dalla regola di assegnazione e dalla comparabilità locale.[^worldbank-rdd]

### Sharp e fuzzy RDD

**Sharp RDD**

```text
score < 60  -> trattamento certo
score >= 60 -> controllo certo
```

**Fuzzy RDD**

Il cutoff modifica fortemente la probabilità di trattamento, ma non la determina perfettamente.

Per esempio:

- alcuni score 59 non ricevono la chiamata;
- alcuni score 61 vengono comunque contattati.

In una fuzzy RDD la discontinuità nell'assegnazione viene usata come fonte di variazione nel trattamento; l'interpretazione dell'effetto diventa più vicina alla logica IV e riguarda unità la cui probabilità di trattamento è modificata dal cutoff.

### L'effetto è locale

Se il design identifica un effetto vicino a 60, non possiamo automaticamente estenderlo a:

- score 20;
- score 95;
- clienti enterprise fuori dalla popolazione analizzata;
- altri periodi con processo operativo diverso.

La località non è un difetto.

È parte dell'estimand.

### Manipolazione della running variable

Supponiamo che i commerciali sappiano che sopra 100.000 € di ARR un account riceve servizi premium e possano riclassificare contratti per superare la soglia.

Se le unità possono manipolare con precisione il running variable, quelle appena sopra e sotto possono non essere comparabili.

Diagnostics utili:

- distribuzione della running variable vicino al cutoff;
- procedure operative che generano il punteggio;
- possibilità pratica di gaming;
- anomalie di massa subito sopra/sotto la soglia.

### Altri trattamenti allo stesso cutoff

Se a `score < 60` il cliente riceve contemporaneamente:

- chiamata;
- voucher;
- account manager senior;

la discontinuità identifica l'effetto del **pacchetto**, non della sola chiamata.

La domanda causale deve riflettere ciò che cambia davvero alla soglia.

### Covariate continuity

Variabili pre-treatment come:

- ARR;
- tenure;
- industry;
- utilizzo precedente;

non dovrebbero mostrare salti sistematici proprio al cutoff se il design è credibile.

Non è necessario che ogni differenza sia zero. Ma discontinuità nette nelle covariate fanno sospettare selezione o altre regole operative.

### Bandwidth: quanto vicino è “vicino”?

Una finestra molto ampia aumenta il campione ma confronta unità meno simili.

Una finestra molto stretta migliora la località ma riduce precisione.

Per questo il risultato dovrebbe essere controllato rispetto a bandwidth ragionevoli e specifiche alternative, non scelto soltanto quella che produce il coefficiente desiderato.

### Caso simulato/composito — Spedizione gratuita sopra 500 €

Un retailer B2B concede free shipping per ordini `>= 500 €`.

Gli ordini sopra soglia hanno repeat rate maggiore.

Un confronto globale è confuso dal fatto che ordini grandi appartengono a clienti diversi.

Una RDD può chiedere:

> “Esiste un salto nel repeat purchase appena attraversata la soglia dei 500 €, dove il valore d'ordine cambia poco ma l'eleggibilità alla spedizione gratuita cambia bruscamente?”

Prima di interpretarlo, bisogna però controllare che a 500 € non scattino anche altri benefit e che i clienti non aggiungano artificialmente prodotti solo per superare la soglia in modo da alterare il processo osservato.

### RDD card

```text
Running variable:
Cutoff:
Regola di assignment:
Sharp o fuzzy?
Treatment che cambia al cutoff:
Altre policy allo stesso cutoff:
Manipolazione possibile?
Covariate continuity:
Bandwidth principali:
Placebo cutoff / sensitivity:
Estimand locale:
Popolazione a cui NON generalizzare:
```

> **RDD è forte perché restringe la causal claim: non chiede se unità molto diverse sono comparabili, ma se un piccolo salto nella regola di trattamento crea un piccolo esperimento locale.**

[^worldbank-rdd]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitolo sulla Regression Discontinuity Design: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
