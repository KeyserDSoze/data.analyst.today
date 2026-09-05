## 8.8 Difference-in-Differences: usare un'altra traiettoria come controfattuale

La **Difference-in-Differences (DiD)** non rende causale un confronto soltanto perché usa il tempo. La sua forza nasce da una domanda molto più precisa: **la traiettoria di un altro gruppo può rappresentare il cambiamento che i trattati avrebbero avuto senza intervento?**

La formula a due gruppi e due periodi rende visibile l'idea:

```text
DiD = (Trattati_dopo - Trattati_prima)
    - (Confronto_dopo - Confronto_prima)
```

Il secondo cambiamento non è una correzione cosmetica. È la stima del controfattuale.

### Caso simulato/composito — Nuovo layout in 25 negozi

Revenue medio settimanale:

| Gruppo | Prima | Dopo | Variazione |
|---|---:|---:|---:|
| Nuovo layout | 118.000 € | 129.000 € | +11.000 € |
| Confronto | 121.000 € | 126.000 € | +5.000 € |

Il prima/dopo dei negozi trattati suggerisce **+11.000 €**, ma anche i negozi di confronto crescono di **+5.000 €**. Se quella crescita rappresenta bene ciò che sarebbe accaduto ai trattati senza nuovo layout, la differenza differenziale è circa **+6.000 € a settimana**.

La causal claim non deriva dalla sottrazione. Deriva dall'assunzione che la traiettoria controfattuale dei trattati avrebbe seguito un andamento comparabile a quella del gruppo di confronto. La World Bank descrive la DiD esattamente in questi termini: il cambiamento del gruppo di confronto viene usato per stimare il cambiamento controfattuale del gruppo trattato.[^worldbank-did]

### Parallel trends: l'assunzione che regge tutto

I gruppi non devono partire dallo stesso livello. Devono però avere una dinamica pre-intervento compatibile con l'idea che, senza trattamento, avrebbero continuato a muoversi in modo comparabile. Avere più periodi pre-treatment aiuta molto: possiamo vedere se i trend storici sono simili, cercare anticipazione e individuare rotture precedenti alla policy.

I pre-trend sono però **diagnostica, non prova**. Il fatto che due serie si siano mosse parallelamente in passato non garantisce che lo avrebbero fatto anche dopo. Serve ancora un argomento sul processo reale.

Consideriamo il pricing UK contro Francia:

| Mese | UK | Francia |
|---|---:|---:|
| Gen | 186 € | 181 € |
| Feb | 191 € | 182 € |
| Mar | 198 € | 183 € |
| Apr — pricing | 211 € | 184 € |
| Mag | 222 € | 185 € |

L'UK cresceva già molto più rapidamente prima del pricing. La Francia è quindi un controfattuale debole per la dinamica UK, anche se un coefficiente DiD può essere calcolato senza problemi.

### Il tempo non protegge dagli shock differenziali

Una DiD resta vulnerabile a eventi che cambiano nello stesso periodo **solo** per il gruppo trattato: una campagna locale, un nuovo concorrente, differenze di stock, un cambio di sales team, una seconda policy o una modifica di tracking. Se un'altra causa si muove insieme al trattamento, la stima può attribuire al trattamento anche quell'effetto.

Anche la composizione del gruppo conta. Se dopo un aumento prezzi escono molti clienti piccoli dal mercato UK, l'MRR medio può crescere perché rimangono account più grandi, non soltanto per un vero aumento dell'outcome sulle stesse unità. Per questo vanno controllati ingressi, uscite, attrition differenziale e cambi di mix.

Il momento del trattamento merita la stessa cura. Se una policy viene annunciata tre mesi prima, clienti e manager possono reagire già all'annuncio. Un **event study** aiuta a visualizzare pre-trend, anticipazione, effetto immediato o graduale, persistenza e decadimento; non sostituisce però l'identification argument.

### Rollout staggered: quando la formula semplice non basta

Nel mondo reale il trattamento viene spesso introdotto regione per regione o cliente per cliente in momenti diversi. Con **staggered adoption**, una regressione con unit fixed effects e time fixed effects non deve essere interpretata automaticamente come la semplice DiD a due gruppi e due periodi, soprattutto se gli effetti cambiano nel tempo o tra coorti di trattamento. Il design deve essere coerente con il timing del rollout e con l'estimand desiderato.

La checklist operativa resta utile perché riassume proprio le condizioni che la prosa ha motivato:

```text
Trattamento e data effettiva:
Gruppo di confronto:
Perché è un controfattuale plausibile?
Periodi pre disponibili:
Pre-trend compatibili?
Anticipazione possibile?
Shock differenziali?
Composizione stabile?
Treatment timing uguale o staggered?
Outcome definito allo stesso modo nel tempo?
Qual è l'estimand?
```

Una conclusione calibrata non dice “dopo il rollout le vendite sono salite, quindi il rollout ha funzionato”. Dice:

> **Rispetto a un gruppo con traiettoria pre-intervento comparabile, il gruppo trattato mostra un incremento differenziale di circa 6.000 € a settimana; l'interpretazione causale dipende dalla plausibilità dei parallel trends e dall'assenza di shock differenziali materialmente rilevanti.**

> **Difference-in-Differences usa una traiettoria osservata per rappresentare una traiettoria controfattuale. Il tempo aggiunge informazione solo se il confronto nel tempo è credibile.**

[^worldbank-did]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*, capitolo su Difference-in-Differences: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
