## 8.2 Correlazione e causalità: quando un pattern non basta

La correlazione misura associazione. Non spiega, da sola, perché due variabili si muovono insieme.

Tre meccanismi diversi possono generare una correlazione osservata:

1. `X` influenza `Y`;
2. `Y` influenza `X`;
3. una terza variabile influenza entrambe.

In pratica possono coesistere più meccanismi.

### Caso - Più chiamate al customer care, più churn

Una società telco osserva che i clienti che contattano il customer care almeno tre volte in un mese hanno un churn del 22%, contro il 6% degli altri.

Il direttore operations propone di ridurre il numero di contatti consentiti:

> "Ogni chiamata aumenta il rischio che il cliente se ne vada."

Ma questa interpretazione scambia un segnale per una causa.

I clienti chiamano perché hanno problemi: fatture errate, copertura, disservizi o modem difettosi. È plausibile che il problema iniziale aumenti sia il numero di contatti sia il churn.

Uno schema causale più credibile è:

`problema di servizio -> chiamate al supporto`

`problema di servizio -> churn`

Le chiamate sono associate al churn senza esserne necessariamente la causa principale.

Anzi, un supporto efficace potrebbe ridurre il churn rispetto a ciò che sarebbe accaduto senza assistenza.

### Predittivo e causale possono essere entrambi utili

Se l'obiettivo è costruire un sistema di early warning, il numero di chiamate può essere un ottimo predittore anche senza essere una causa.

Se invece vogliamo decidere se ridurre, aumentare o modificare il supporto, serve una domanda causale.

Questa distinzione è fondamentale:

> **Una variabile può essere molto utile per prevedere un outcome e completamente sbagliata come leva di intervento.**

### Caso - Sconto e valore cliente

Un retailer scopre che i clienti che usano molti coupon hanno LTV superiore del 31%.

Una conclusione possibile è: aumentare i coupon aumenta il lifetime value.

Ma l'EDA mostra che i coupon vengono inviati soprattutto ai membri loyalty, che acquistavano già più frequentemente prima dell'iscrizione al programma.

Inoltre i clienti ad alto valore ricevono più comunicazioni e quindi hanno più occasioni di usare coupon.

La correlazione osservata incorpora almeno:

- selezione nel programma loyalty;
- frequenza di acquisto preesistente;
- intensità di marketing;
- possibile effetto causale del coupon.

Separare queste componenti è il problema causale.

### Domande da fare prima di usare il verbo "causare"

Quando vediamo una relazione forte, chiediamoci:

- quale meccanismo potrebbe collegare le due variabili?
- la direzione causale potrebbe essere inversa?
- esistono variabili comuni che spiegano entrambe?
- come sono stati selezionati i soggetti osservati?
- la relazione esisteva già prima dell'intervento?
- che cosa accadrebbe a `Y` se modificassimo deliberatamente `X`?

L'ultima domanda è quella decisiva. La causalità riguarda interventi, non soltanto osservazioni.
