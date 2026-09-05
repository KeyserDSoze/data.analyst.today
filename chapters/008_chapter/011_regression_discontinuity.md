## 8.10 Regression Discontinuity: quando una soglia modifica il trattamento

Molte policy aziendali non assegnano il trattamento casualmente, ma lo fanno cambiare bruscamente a una soglia: supporto premium sopra un ARR minimo, chiamata retention sotto un health score, credito oltre un cutoff, incentivo sopra una performance threshold o spedizione gratuita oltre un valore d'ordine. Quando la regola è abbastanza rigida, le unità appena sopra e appena sotto la soglia possono creare un confronto quasi-sperimentale.

Questa è l'intuizione della **Regression Discontinuity Design (RDD)**: non chiediamo che trattati e non trattati siano comparabili ovunque, ma che lo siano **localmente attorno al cutoff**, salvo il trattamento che cambia proprio lì.

### Caso simulato/composito — Health score 60

Un SaaS assegna automaticamente una chiamata proattiva agli account con `health_score < 60`. Confrontare tutti i trattati con tutti i non trattati sarebbe poco informativo, perché i trattati sono per definizione più fragili. Vicino alla soglia osserviamo invece:

| Health score | Chiamata | Churn 30 gg |
|---|---|---:|
| 58–59 | sì | 13,2% |
| 60–61 | no | 16,7% |

Il salto locale è circa `-3,5 pp`. La causal claim è credibile solo se, senza chiamata, l'outcome atteso avrebbe attraversato la soglia in modo **continuo**. In altre parole, score 59 e 60 non devono essere identici; devono differire abbastanza poco da rendere plausibile che proprio al cutoff cambi soprattutto l'accesso al trattamento.

La World Bank presenta RDD come un confronto tra unità vicine a una soglia di eleggibilità e lega la credibilità del design alla regola di assegnazione e alla comparabilità locale.[^worldbank-rdd]

### Quello che cambia alla soglia definisce l'effetto

In una **sharp RDD** il cutoff determina perfettamente il trattamento:

```text
score < 60  -> trattamento certo
score >= 60 -> controllo certo
```

In una **fuzzy RDD** la soglia modifica fortemente la probabilità di trattamento ma non la determina perfettamente. Alcuni account sotto 60 possono non ricevere la chiamata e alcuni sopra 60 possono riceverla comunque. In questo caso la discontinuità nella regola di assignment viene usata come fonte di variazione e l'interpretazione si avvicina alla logica IV: l'effetto riguarda soprattutto le unità la cui probabilità di trattamento cambia per effetto del cutoff.

La località è quindi parte dell'estimand. Un effetto identificato intorno a 60 non può essere trasferito automaticamente agli account con score 20 o 95, ad altri segmenti o a periodi in cui la policy operativa è diversa.

### Quando il cutoff smette di assomigliare a un piccolo esperimento

Se le unità possono manipolare con precisione la running variable, la comparabilità locale si indebolisce. Se i commerciali sanno che sopra **100.000 € di ARR** scattano servizi premium e possono riclassificare contratti per superare la soglia, le unità appena sopra e sotto potrebbero essere state selezionate in modo strategico. La distribuzione della running variable, la possibilità pratica di gaming e anomalie di massa vicino al cutoff diventano quindi diagnostics sostanziali.

Va inoltre verificato che alla stessa soglia non cambino più cose. Se `score < 60` attiva contemporaneamente chiamata, voucher e account manager senior, la discontinuità identifica l'effetto del **pacchetto**, non quello della sola chiamata.

Le covariate pre-treatment — ARR, tenure, industry, usage precedente — non dovrebbero mostrare salti sistematici proprio al cutoff. Una discontinuità netta in queste variabili suggerisce che la soglia coincida con altra selezione o con altre regole operative.

Infine c'è il compromesso della **bandwidth**: una finestra ampia offre più dati ma confronta unità meno simili; una finestra stretta aumenta la comparabilità locale ma riduce precisione. Il risultato deve essere stressato su bandwidth ragionevoli e, quando utile, placebo cutoff, invece di scegliere la specifica che produce il coefficiente preferito.

### Caso simulato/composito — Spedizione gratuita sopra 500 €

Un retailer B2B concede free shipping per ordini `>= 500 €`. Gli ordini sopra soglia hanno repeat rate maggiore, ma un confronto globale è confuso dal fatto che ordini grandi appartengono a clienti diversi. La RDD può invece chiedere se esiste un salto nel repeat purchase appena attraversati i **500 €**, dove il valore d'ordine cambia poco mentre l'eleggibilità alla spedizione gratuita cambia bruscamente. Prima di interpretare il salto dobbiamo verificare che a 500 € non scattino altri benefit e che i clienti non manipolino sistematicamente il basket per superare la soglia.

La RDD card conserva i controlli che definiscono lo scope della causal claim:

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

> **RDD è forte proprio perché restringe la domanda: usa il piccolo salto nella regola di trattamento come un piccolo esperimento locale.**

[^worldbank-rdd]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*, capitolo sulla Regression Discontinuity Design: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
