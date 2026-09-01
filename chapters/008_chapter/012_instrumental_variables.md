## 8.11 Instrumental Variables: usare una fonte esterna di variazione nel trattamento

A volte trattamento e outcome condividono confondenti difficili da osservare.

Matching e regressione possono allora lasciare un problema sostanziale.

Le **Instrumental Variables (IV)** cercano una fonte di variazione che spinga alcune unità verso il trattamento senza influenzare l'outcome attraverso altri percorsi rilevanti.

È una strategia potente e difficile da difendere.

### Caso simulato/composito — Disponibilità del consulente

Una fintech vuole stimare se una chiamata tecnica entro 24 ore riduce il default tra clienti in difficoltà.

I consulenti, però, scelgono più spesso clienti percepiti come recuperabili.

Motivazione e qualità della relazione sono poco misurate e possono influenzare sia trattamento sia default.

L'azienda nota che alcune richieste arrivano casualmente in turni con forte capacità residua e altre in turni saturi.

La **capacità disponibile al momento dell'assegnazione** potrebbe essere candidata a strumento se:

1. modifica davvero la probabilità di ricevere la chiamata;
2. è plausibilmente indipendente dai fattori non osservati che influenzano il default;
3. influenza il default soltanto attraverso il trattamento definito.

Queste condizioni non sono dettagli tecnici. Sono l'identification argument.

### Relevance: lo strumento deve muovere il trattamento

Uno strumento che cambia la probabilità di trattamento dal 62% al 64% offre poca variazione utile.

Uno che la cambia dal 40% all'82% ha un first stage molto più forte.

Strumenti deboli possono produrre stime instabili e inference problematica.

Per questo non basta verificare che `Z` sia “statisticamente correlato” con `T`: bisogna guardare dimensione e stabilità del first stage.

### Independence / exogeneity

Lo strumento deve essere plausibilmente scollegato dalle cause non osservate dell'outcome.

Nel caso fintech, il turno disponibile sarebbe problematico se:

- clienti più complessi vengono instradati intenzionalmente verso certi turni;
- alcuni orari corrispondono a segmenti geografici con rischio diverso;
- la capacità residua dipende da picchi operativi collegati al default.

La fonte di variazione deve essere capita operativamente, non soltanto inserita nel modello.

### Exclusion restriction

Lo strumento dovrebbe influenzare l'outcome **attraverso il trattamento definito**, non tramite canali alternativi rilevanti.

Supponiamo che i turni meno saturi permettano non solo una chiamata entro 24 ore, ma anche:

- revisione del piano di rimborso;
- priorità nelle escalation;
- tempi di risposta migliori in seguito.

Allora “capacità residua” modifica un pacchetto più ampio della sola chiamata.

La causal claim deve essere ripensata oppure l'exclusion restriction diventa poco credibile.

### Monotonicity e LATE

Con molti design IV l'effetto identificato riguarda i **compliers**: unità la cui probabilità di trattamento cambia nella direzione indotta dallo strumento.

Questo porta al **Local Average Treatment Effect (LATE)**.

L'interpretazione richiede anche una forma di monotonicity: non dovrebbero esistere gruppi che reagiscono sistematicamente allo strumento nella direzione opposta.

Il Premio Nobel 2021 sottolinea proprio il contributo di Angrist e Imbens nel chiarire quali effetti causali possano essere identificati in natural experiment con compliance non perfetta.[^nobel-iv]

### Locale significa locale

Se la disponibilità dei consulenti modifica la chiamata soprattutto per clienti “al margine” tra essere contattati o no, l'effetto IV riguarda soprattutto quel gruppo.

Non possiamo automaticamente concludere che la chiamata abbia lo stesso effetto:

- sui clienti che verrebbero sempre chiamati;
- su quelli che non verrebbero mai chiamati;
- sull'intera customer base.

L'estimand deve dirlo esplicitamente.

### Caso simulato/composito — Demo personalizzate

Un SaaS osserva:

- conversione con demo: 46%;
- conversione senza demo: 19%.

Il gap grezzo è enorme, ma i lead migliori ricevono più demo.

Per alcuni trimestri l'assegnazione ai sales engineer dipende da rotazioni operative che cambiano fortemente la probabilità di demo.

Se il meccanismo è difendibile, una stima IV potrebbe produrre:

- effetto osservazionale grezzo: `+27 pp`;
- effetto IV locale: `+7 pp`.

Il secondo numero non è “più vero” perché usa IV.

È credibile solo nella misura in cui relevance, independence, exclusion e interpretazione locale reggono.

### Una IV non si trova con feature engineering

Cercare tra centinaia di colonne quella più correlata con il trattamento e chiamarla “instrument” è un errore concettuale.

La validità nasce da una storia istituzionale, operativa o naturale sul perché quella variabile modifica il trattamento senza aprire altri percorsi verso l'outcome.

### IV card

```text
Treatment:
Outcome:
Instrument candidate:
Meccanismo che collega Z -> T:
First-stage effect:
Perché Z è plausibilmente esogena?
Quali percorsi alternativi Z -> Y sono plausibili?
Exclusion restriction difendibile?
Monotonicity plausibile?
Quali unità sono i compliers?
Estimand: LATE per chi?
Sensitivity / alternative explanations:
```

> **Uno strumento non è valido perché è predittivo del trattamento. È valido solo se la variazione che genera nel trattamento può essere interpretata causalmente.**

[^nobel-iv]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
