## 8.11 Instrumental Variables: usare una fonte esterna di variazione nel trattamento

Quando trattamento e outcome condividono confondenti difficili da osservare, matching e regressione possono lasciare un problema che nessun balance plot risolve. Le **Instrumental Variables (IV)** cercano allora una fonte di variazione `Z` che modifichi il trattamento senza influenzare l'outcome attraverso altri percorsi materialmente rilevanti.

È una strategia potente proprio perché l'identification argument è esigente. Uno strumento non diventa valido perché predice bene il trattamento: deve muoverlo **nel modo giusto**.

### Caso simulato/composito — Disponibilità del consulente

Una fintech vuole stimare se una chiamata tecnica entro 24 ore riduce il default tra clienti in difficoltà. I consulenti, però, scelgono più spesso clienti percepiti come recuperabili; motivazione e qualità della relazione sono poco misurate e possono influenzare sia chiamata sia default.

L'azienda nota che alcune richieste arrivano in turni con forte capacità residua e altre in turni saturi. La **capacità disponibile al momento dell'assegnazione** può essere candidata a strumento se soddisfa tre condizioni sostanziali: modifica davvero la probabilità di ricevere la chiamata; è plausibilmente indipendente dalle cause non osservate del default; influenza il default soprattutto attraverso il trattamento definito.

La prima condizione è la **relevance**. Uno strumento che sposta la probabilità di trattamento dal 62% al 64% offre poca variazione utile; uno che la sposta dal 40% all'82% produce un first stage molto più forte. Strumenti deboli possono generare stime instabili e inference problematica, quindi non basta una correlazione statisticamente diversa da zero.

La seconda riguarda **independence / exogeneity**. Nel caso fintech la capacità residua sarebbe un cattivo strumento se clienti più complessi vengono instradati verso certi turni, se alcuni orari corrispondono a geografie con rischio diverso o se la saturazione stessa dipende da picchi operativi collegati al default. La fonte di variazione va capita nel processo reale.

La terza è la **exclusion restriction**. Se i turni meno saturi consentono non soltanto una chiamata entro 24 ore, ma anche revisione del piano di rimborso, priorità nelle escalation e tempi di risposta migliori, `Z` modifica un pacchetto di trattamento più ampio. La causal question deve riflettere quel pacchetto oppure l'exclusion restriction diventa poco credibile.

### L'effetto identificato può essere locale

Nei design IV con compliance non perfetta l'effetto riguarda spesso i **compliers**: unità la cui probabilità di trattamento cambia nella direzione indotta dallo strumento. È il **Local Average Treatment Effect (LATE)**. La sua interpretazione richiede anche una forma di monotonicity: non dovrebbero esistere gruppi che reagiscono sistematicamente allo strumento nella direzione opposta.

Il Nobel 2021 sottolinea proprio il contributo di Angrist e Imbens nel chiarire quali effetti causali siano identificabili in natural experiment con trattamento non perfettamente controllato.[^nobel-iv] “Locale” non significa debole: significa che dobbiamo sapere **per chi** il confronto identifica l'effetto.

### Caso simulato/composito — Demo personalizzate

Un SaaS osserva conversione **46%** con demo e **19%** senza demo. Il gap grezzo è `+27 pp`, ma i lead migliori ricevono più spesso una demo. Per alcuni trimestri l'assegnazione ai sales engineer dipende da rotazioni operative che modificano fortemente la probabilità di ricevere la demo.

Se quel meccanismo è difendibile come strumento, una stima IV locale potrebbe produrre un effetto di circa `+7 pp`. Il secondo numero non è “più vero” perché nasce da una tecnica più sofisticata. È credibile solo se relevance, independence, exclusion e interpretazione locale reggono insieme.

Questo è il motivo per cui una IV non si trova facendo feature engineering su centinaia di colonne. La validità nasce da una storia istituzionale, operativa o naturale sul perché `Z` modifica `T` e sul perché non dovrebbe modificare `Y` attraverso altri percorsi.

La **IV card** mantiene esplicito l'argomento:

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

Con RDD e IV abbiamo incontrato due design che spesso identificano effetti locali. Il passo successivo è diverso: anche quando conosciamo l'effetto totale, il business può voler capire **attraverso quale meccanismo** quell'effetto si produce.

[^nobel-iv]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
