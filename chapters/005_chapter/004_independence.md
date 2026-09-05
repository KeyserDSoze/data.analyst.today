## 5.3 Indipendenza: l'assunzione nascosta dietro molte formule

Due eventi sono **indipendenti** quando sapere che uno si è verificato non modifica la probabilità dell'altro. In simboli, se `A` e `B` sono indipendenti:

`P(A|B) = P(A)`

ed equivalentemente:

`P(A ∩ B) = P(A)P(B)`.

Queste formule sembrano innocue perché permettono calcoli semplici. Il rischio nasce quando trattiamo l'indipendenza come una proprietà matematica da applicare per comodità invece che come un'affermazione sul processo reale.

Indipendenza, inoltre, non significa “assenza di causalità diretta”. Due eventi possono non causarsi reciprocamente e risultare comunque dipendenti perché condividono condizioni comuni.

## Due ritardi che condividono lo stesso mondo

Una piattaforma di food delivery vuole stimare la probabilità che un ordine subisca contemporaneamente un ritardo del rider e un ritardo del ristorante. Nello storico osserva:

`P(ritardo rider) = 8%`

`P(ritardo ristorante) = 6%`.

Se moltiplicassimo le due probabilità assumendo indipendenza otterremmo:

`8% × 6% = 0,48%`.

Nei dati, però, la frequenza congiunta è **1,9%**, quasi quattro volte più alta. La formula non è stata eseguita male: era sbagliata l'assunzione che la rendeva applicabile.

Quando il team segmenta gli ordini per condizioni meteo, il meccanismo diventa visibile:

| Condizione | Ritardo rider | Ritardo ristorante | Entrambi |
|---|---:|---:|---:|
| Normale | 5,1% | 4,3% | 0,5% |
| Pioggia forte | 18,4% | 12,7% | 5,9% |

Pioggia intensa, picchi serali, grandi eventi locali, traffico critico e sovraccarico dei ristoranti possono aumentare contemporaneamente entrambi i rischi. I due eventi condividono il contesto e quindi la probabilità dell'uno contiene informazione sull'altro.

Nel Capitolo 8 parleremo di queste strutture con un linguaggio causale più rigoroso. Qui serve fissare un principio precedente: **una probabilità congiunta eredita le dipendenze del processo che stiamo modellando**.

## Correlazione zero non ci salva

Il Capitolo 4 ha mostrato che una relazione non lineare può avere correlazione di Pearson vicina a zero. Per questo:

> **correlazione zero non implica indipendenza**.

L'indipendenza è una condizione più forte: se due variabili sono indipendenti e le quantità coinvolte sono ben definite, la covarianza è zero; l'inverso non vale in generale. “Non vedo correlazione lineare” non autorizza quindi a trattare due variabili come se non condividessero alcuna struttura.

## Quante osservazioni sono davvero indipendenti?

L'indipendenza non compare soltanto quando moltiplichiamo due probabilità. Entra silenziosamente anche in molte formule inferenziali. Diecimila righe possono essere diecimila unità indipendenti oppure cento utenti che hanno generato cento eventi ciascuno. Nel secondo caso la numerosità fisica del file sovrastima la quantità di informazione indipendente.

Lo stesso problema compare con ordini raggruppati nello stesso store, dipendenti dello stesso team, clienti della stessa azienda, misure ripetute di un sensore o osservazioni consecutive nel tempo. Trattare ogni riga come indipendente può produrre intervalli artificialmente stretti e test eccessivamente sicuri.

Prima di usare una formula che presume indipendenza vale quindi la pena ricostruire la struttura del dato: le unità possono influenzarsi tra loro? condividono tempo, geografia, campagna o capacità operativa? la stessa persona genera più record? esistono cluster naturali? un evento modifica direttamente o indirettamente la probabilità dell'altro?

Queste non sono domande accessorie da porre dopo il calcolo. Sono ciò che decide se il calcolo rappresenta il fenomeno.

> **Quando una formula richiede indipendenza, la domanda professionale non è soltanto “so applicarla?”, ma “quale struttura del processo rende plausibile l'assunzione che la formula sta usando?”.**
