## 5.3 Indipendenza: quando conoscere B non cambia la probabilità di A

Due eventi sono **indipendenti** quando conoscere il verificarsi di uno non cambia la probabilità dell'altro.

Formalmente, se `A` e `B` sono indipendenti:

`P(A|B) = P(A)`

ed equivalentemente:

`P(A ∩ B) = P(A)P(B)`

È importante usare parole precise: indipendenza statistica non significa semplicemente che due eventi “non si causano”. È una proprietà della loro distribuzione congiunta.

Due eventi possono non avere un rapporto causale diretto e risultare comunque dipendenti perché condividono condizioni comuni.

### Caso simulato/composito — Il rischio di consegna sottostimato

Una piattaforma di food delivery vuole stimare la probabilità che un ordine subisca contemporaneamente:

- un ritardo del rider;
- un ritardo del ristorante.

Dai dati storici:

- `P(ritardo rider) = 8%`;
- `P(ritardo ristorante) = 6%`.

Assumendo indipendenza otterremmo:

`8% × 6% = 0,48%`.

Ma nei dati la frequenza congiunta osservata è **1,9%**.

È quasi quattro volte più alta.

Perché?

Entrambi gli eventi sono più probabili quando si verificano condizioni come:

- pioggia intensa;
- picchi serali;
- grandi eventi locali;
- traffico critico;
- ristoranti sovraccarichi;
- zone con offerta di rider insufficiente.

Le due probabilità condividono driver comuni. Non possiamo quindi moltiplicarle come se fossero indipendenti.

### Un modo utile per diagnosticare la dipendenza

L'analista segmenta gli ordini per condizioni meteo.

| Condizione | Ritardo rider | Ritardo ristorante | Entrambi |
|---|---:|---:|---:|
| Normale | 5,1% | 4,3% | 0,5% |
| Pioggia forte | 18,4% | 12,7% | 5,9% |

Il tempo atmosferico cambia entrambe le probabilità.

Questo è un esempio semplice di **dipendenza indotta da un fattore comune**.

Nel Capitolo 8 useremo un linguaggio causale più rigoroso per parlare di confondenti. Qui ci interessa una lezione precedente:

> **le assunzioni sulle relazioni tra eventi devono riflettere il processo reale, non la comodità della formula.**

### Correlazione zero non implica indipendenza

Nel Capitolo 4 abbiamo visto che la correlazione lineare può essere vicina a zero anche quando esiste una relazione non lineare forte.

Di conseguenza:

> **correlazione zero ≠ indipendenza**.

L'indipendenza è una condizione più forte. Se due variabili sono indipendenti, in condizioni regolari la loro covarianza è zero; l'inverso non vale in generale.

Questo è uno dei motivi per cui “non vedo correlazione” non dovrebbe diventare automaticamente “le variabili non hanno nulla a che fare l'una con l'altra”.

### Quando l'assunzione di indipendenza entra nei modelli

L'indipendenza compare continuamente, spesso senza essere dichiarata.

Per esempio quando stimiamo:

- probabilità congiunte di più guasti;
- sequenze di conversione;
- failure rate di componenti;
- errori standard;
- probabilità binomiali;
- risultati di osservazioni campionarie.

In alcuni casi l'assunzione è ragionevole. In altri è un'approssimazione. In altri ancora è chiaramente falsa.

Per questo, prima di moltiplicare probabilità o applicare una formula che presume osservazioni indipendenti, chiediamo:

1. le unità possono influenzarsi tra loro?
2. condividono tempo, geografia, campagna o capacità operativa?
3. una stessa persona può generare più osservazioni?
4. esistono cluster naturali, come store, aziende, famiglie o team?
5. un evento rende più o meno probabile l'altro?

Queste domande torneranno nei capitoli su inferenza, A/B test e modelli.

### La domanda dell'analista

Quando una probabilità combina più eventi, non chiediamo soltanto:

> “La formula è corretta?”

Chiediamo:

> **“Quale assunzione di dipendenza o indipendenza rende corretta questa formula, e il processo reale la rende plausibile?”**

La matematica viene dopo la struttura del fenomeno.
