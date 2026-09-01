## 6.9 Reactivation: distinguere il ritorno momentaneo dal recupero duraturo

Retention e churn vengono spesso rappresentati come due stati definitivi: presente oppure perso.

Molti prodotti reali sono più intermittenti. Un cliente può diventare inattivo, tornare dopo settimane, usare intensamente il prodotto per poco tempo e poi sparire di nuovo.

Per questo conviene modellare almeno tre stati distinti:

- **attivo**;
- **inattivo/churned secondo una soglia operativa**;
- **riattivato**.

Il problema è che “riattivato” può significare quasi qualunque cosa.

### Caso simulato/composito: FitNow e la campagna che recuperava il 18%

**FitNow** è un'app fitness in abbonamento. Considera inattivo un utente che non apre l'app e non completa workout per almeno trenta giorni.

Il CRM team contatta 180.000 utenti inattivi con email, push notification e un mese premium gratuito.

Dopo due settimane:

- 32.400 utenti riaprono l'app;
- reactivation rate dichiarata: 18%.

La campagna sembra un successo.

L'analista osserva però ciò che succede dopo il ritorno:

| Comportamento dopo il ritorno | Quota dei riattivati | Attivi anche dopo 60 giorni |
| --- | ---: | ---: |
| Una sola apertura | 37% | 4% |
| Almeno un workout | 34% | 21% |
| Almeno 3 workout in 14 giorni | 21% | 49% |
| Nuovo piano settimanale completato | 8% | 68% |

Il 18% misurava **ritorno**, non necessariamente **recupero della relazione**.

### Reactivation event e durable reactivation

È utile distinguere:

**Reactivation event** — il primo comportamento che riporta l'utente nello stato attivo.

**Durable reactivation** — il ritorno persiste abbastanza da indicare un recupero reale del comportamento.

FitNow sostituisce quindi la metrica principale con una definizione più severa:

> utente inattivo da almeno trenta giorni che completa almeno due workout nei quattordici giorni successivi al ritorno e rimane attivo nella finestra seguente.

La reactivation scende dal 18% al 6,3%.

È un numero meno spettacolare, ma molto più vicino al fenomeno economico che interessa.

### Il denominatore deve descrivere chi era realmente recuperabile

Anche il denominatore può essere ingannevole.

Tra i 180.000 utenti inattivi potrebbero esserci:

- persone che hanno già chiesto la cancellazione definitiva;
- account duplicati;
- utenti che non possono più essere contattati;
- clienti che hanno smesso perché il bisogno è terminato;
- utenti stagionali che sarebbero tornati comunque.

La popolazione eleggibile a una campagna di reactivation dovrebbe essere definita prima di calcolare il tasso.

### Il problema controfattuale: quanti sarebbero tornati comunque?

Se 32.400 persone tornano dopo una campagna, non possiamo attribuire automaticamente tutti i ritorni alla campagna.

Una parte degli utenti inattivi sarebbe potuta tornare spontaneamente.

Supponiamo che, nello stesso periodo e su una popolazione comparabile non contattata, il 7% torni comunque.

Il 18% osservato nella popolazione contattata resta interessante, ma la domanda causale diventa:

> quanto ritorno **incrementale** ha prodotto davvero l'intervento rispetto a ciò che sarebbe successo senza campagna?

Questa distinzione prepara il terreno per sperimentazione e causalità. Qui ci basta non confondere un evento post-campagna con un effetto della campagna.

### Il costo della reactivation

Il mese premium gratuito ha un costo.

Se consideriamo tutti i 32.400 utenti tornati, il costo per reactivation sembra basso. Se consideriamo soltanto i recuperi duraturi, il costo per cliente realmente recuperato aumenta molto.

Una valutazione completa dovrebbe includere:

- costo del contatto;
- costo dell'incentivo;
- quota di ritorni duraturi;
- revenue/margine dopo il ritorno;
- eventuale cannibalizzazione;
- ritorno spontaneo di baseline.

### Reactivation non è acquisition

Un utente riattivato porta con sé una storia che un nuovo utente non ha.

Conviene quindi costruire coorti specifiche per:

- durata dell'inattività;
- comportamento prima dell'uscita;
- motivo di churn, quando disponibile;
- canale di reactivation;
- incentivo ricevuto;
- comportamento dopo il ritorno.

Un utente inattivo da 35 giorni e uno assente da 18 mesi non sono necessariamente lo stesso problema.

### La domanda operativa

Una buona analisi di reactivation non si ferma a:

> quanti sono tornati?

Chiede:

> quanti sono tornati, quanti sono rimasti, quanto valore hanno ricominciato a generare e quanta parte del ritorno è plausibilmente incrementale?

Il lifecycle non termina sempre con il churn. Ma nemmeno ogni ritorno rappresenta una relazione recuperata.
