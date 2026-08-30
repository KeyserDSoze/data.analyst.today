## 8.11 Instrumental variables: quando serve una fonte esterna di variazione

A volte il trattamento è fortemente confuso con caratteristiche non osservate e il matching non basta.

Immaginiamo una fintech che vuole sapere se il contatto telefonico con un consulente riduce il default dei clienti in difficoltà.

Problema: i consulenti chiamano più spesso proprio i clienti che percepiscono come recuperabili. Motivazione, qualità della relazione, serietà del cliente e altre caratteristiche difficili da misurare influenzano sia la probabilità di ricevere la chiamata sia il default.

Il semplice confronto trattati/non trattati è quindi contaminato.

### L'idea dello strumento

Una **instrumental variable (IV)** è una variabile che modifica la probabilità di ricevere il trattamento, ma che non dovrebbe influenzare direttamente l'outcome attraverso altri canali rilevanti.

In termini intuitivi, cerchiamo una fonte di variazione quasi esterna che spinga alcune unità verso il trattamento senza essere essa stessa parte del meccanismo che determina l'outcome.

### Caso realistico: disponibilità casuale dei consulenti

La fintech scopre che, per ragioni di turnazione, alcune richieste vengono assegnate a consulenti con capacità residua elevata e altre a consulenti già quasi saturi.

La disponibilità del consulente influenza fortemente la probabilità che la chiamata avvenga entro 24 ore.

Potrebbe essere usata come strumento solo se è plausibile che:

1. influenzi effettivamente il trattamento;
2. non influenzi il default se non attraverso la chiamata;
3. non sia correlata con caratteristiche non osservate dei clienti che influenzano il default.

Queste condizioni sono forti.

### Relevance

Lo strumento deve essere rilevante: deve cambiare davvero la probabilità di trattamento.

Se la disponibilità del consulente aumenta la probabilità di contatto dal 62% al 64%, lo strumento è probabilmente troppo debole.

Se la aumenta dal 40% all'82%, il primo stadio è molto più credibile.

### Exclusion restriction

La condizione più difficile è l'**exclusion restriction**: lo strumento non deve influenzare direttamente l'outcome attraverso altri canali.

Supponiamo che i consulenti meno occupati non solo chiamino prima, ma dedichino anche più tempo alla revisione del piano di rimborso. In quel caso la variabile "disponibilità" agisce attraverso più meccanismi e l'interpretazione diventa più complessa.

### Un esempio B2B

Una società SaaS vuole stimare l'effetto causale delle demo personalizzate sul closing rate.

I lead migliori ricevono più spesso una demo, quindi il confronto grezzo è inutilizzabile.

Per alcuni trimestri l'assegnazione dei lead ai sales engineer dipende quasi casualmente dalla disponibilità giornaliera.

Se la disponibilità influenza la probabilità di fare una demo ma non il closing attraverso altri canali, può offrire una fonte di variazione utile.

Il risultato potrebbe essere:

- effetto osservazionale grezzo della demo: +22 punti di conversione;
- stima IV locale: +7 punti.

La differenza racconta quanto la selezione iniziale gonfiasse l'apparente efficacia delle demo.

### Local Average Treatment Effect

Con strumenti di questo tipo, l'effetto stimato spesso riguarda le unità il cui trattamento cambia a causa dello strumento: i cosiddetti **compliers**.

Non necessariamente rappresenta l'effetto medio per tutta la popolazione.

### Perché l'IV è potente ma pericolosa

Le instrumental variables possono risolvere problemi che altri metodi non riescono ad affrontare, ma richiedono assunzioni difficili da verificare direttamente.

Un'IV non diventa valida perché produce un coefficiente significativo.

Serve una storia causale convincente.

### Regola pratica

> **Uno strumento valido non è una variabile correlata con il trattamento. È una fonte di variazione nel trattamento che può essere difesa causalmente.**

### Riferimenti

- World Bank, *Impact Evaluation in Practice*, capitolo sulle instrumental variables.
