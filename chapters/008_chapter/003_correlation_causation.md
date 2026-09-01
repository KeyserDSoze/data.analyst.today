## 8.2 Correlazione, previsione e causalità: tre domande diverse

Una relazione osservata può essere utile senza essere causale.

Questo è importante perché nel lavoro dell'analista convivono almeno tre obiettivi differenti:

- **descrivere:** quali variabili si muovono insieme?
- **prevedere:** quali segnali anticipano l'outcome?
- **intervenire:** che cosa cambierebbe l'outcome se modificassimo una specifica esposizione?

Confondere questi obiettivi produce decisioni sbagliate anche quando i numeri sono corretti.

### Caso simulato/composito — Più chiamate al supporto, più churn

Una telco osserva:

| Clienti | Churn 60 giorni |
|---|---:|
| almeno 3 chiamate al supporto | 22% |
| meno di 3 chiamate | 6% |

Il numero di chiamate è un ottimo **segnale di rischio**.

Ma sarebbe pericoloso concludere:

> “Riduciamo le chiamate consentite, così ridurremo il churn.”

Un meccanismo plausibile è:

```text
problema di servizio -> più chiamate
problema di servizio -> churn
```

Il supporto potrebbe persino attenuare il churn rispetto al controfattuale senza assistenza.

La stessa variabile può quindi essere:

- forte predittore;
- debole spiegazione causale;
- pessima leva di intervento.

### Quattro modi in cui nasce un'associazione

Quando `X` e `Y` sono associati, tra le spiegazioni plausibili ci sono:

1. `X -> Y`;
2. `Y -> X`;
3. `Z -> X` e `Z -> Y` — confounding;
4. selezione o condizionamento che crea l'associazione nel campione osservato.

Possono inoltre coesistere più percorsi contemporaneamente.

Per questo il coefficiente di correlazione non contiene, da solo, la direzione delle frecce.

### “X viene prima di Y” è necessario, ma non sufficiente

Perché `X` causi `Y`, l'esposizione deve precedere l'outcome rilevante.

Ma la precedenza temporale non basta.

Se il deterioramento del cliente inizia a gennaio, la chiamata di retention avviene a febbraio e il churn a marzo, la chiamata precede il churn ma è stata provocata da un rischio già presente.

Il tempo aiuta a escludere storie impossibili. Non identifica da solo il controfattuale.

### Caso simulato/composito — Coupon e LTV

Un retailer scopre che chi utilizza almeno quattro coupon l'anno ha LTV superiore del 31%.

Possibili spiegazioni:

- i coupon aumentano davvero frequenza e retention;
- i clienti loyalty, già più attivi, ricevono più coupon;
- chi compra più spesso ha semplicemente più occasioni di utilizzare coupon;
- il marketing invia più offerte agli utenti ad alto valore;
- una combinazione delle precedenti.

L'EDA ha trovato un pattern utile.

Il predictive model potrebbe usare `coupon_usage` con successo.

Ma per decidere se **inviare più coupon** serve una domanda causale separata.

### Una prova mentale: sostituire “associato” con “intervenire”

Quando una dashboard mostra una relazione, prova a trasformare la frase.

Da:

> “Gli utenti con tre workflow hanno retention più alta.”

A:

> “Se inducissimo utenti comparabili a creare tre workflow, la loro retention aumenterebbe.”

La seconda frase richiede evidenza molto più forte.

Questa prova mentale è semplice ma potente: rivela immediatamente quando stiamo passando da descrizione a intervento senza un identification argument.

### Claim ladder

Durante il capitolo useremo una scala di linguaggio:

**Livello 1 — Descrittivo**

> “X e Y sono associati.”

**Livello 2 — Predittivo**

> “X migliora la previsione di Y fuori campione.”

**Livello 3 — Causale condizionato**

> “Sotto queste assunzioni e con questo design, la stima è compatibile con un effetto causale di X su Y.”

**Livello 4 — Decisionale**

> “Per questa popolazione e questo trattamento, l'effetto stimato è abbastanza grande e preciso da giustificare questa azione.”

Non ogni analisi deve arrivare al livello 4.

La maturità consiste anche nel fermarsi al livello che l'evidenza sostiene.

> **Un'associazione può essere preziosa. Diventa pericolosa quando le chiediamo di rispondere a una domanda di intervento che il disegno non può sostenere.**
