# 17.6 Product analytics e funnel: quando il problema non è dove gli utenti escono, ma perché

Un funnel è una delle rappresentazioni più semplici e utili dell'analisi prodotto.

Visita → registrazione → onboarding → prima azione di valore → utilizzo ricorrente → pagamento.

La semplicità è anche il suo rischio.

Quando un team vede che il passaggio tra due step peggiora, tende a trattare quello step come causa del problema.

Ma un funnel descrive **dove** osserviamo una perdita. Non dimostra automaticamente **perché** quella perdita avviene.

## Caso composito: PulseNote, SaaS di collaborazione

PulseNote ha 420.000 utenti attivi mensili e un modello freemium.

Nel giro di sei settimane il tasso di attivazione dei nuovi account scende dal 43% al 35%.

Il product manager chiede:

> “Cosa si è rotto nell'onboarding?”

È una domanda plausibile. Ma contiene già un'ipotesi: che il problema sia nell'onboarding.

L'analista costruisce il funnel per coorte di registrazione:

| Step | Prima | Dopo | Delta |
|---|---:|---:|---:|
| Signup completato | 100% | 100% | — |
| Workspace creato | 82% | 80% | -2 pp |
| Primo invito inviato | 61% | 52% | -9 pp |
| Primo documento condiviso | 49% | 41% | -8 pp |
| Activation entro 7 giorni | 43% | 35% | -8 pp |

Il punto di rottura sembra evidente: primo invito.

La prima spiegazione sarebbe:

> “Il nuovo flow di invito ha peggiorato la conversione.”

Ma prima di concludere, l'analista segmenta per:

- paese;
- device;
- sorgente di acquisizione;
- dimensione aziendale;
- template scelto;
- versione dell'app;
- tipo di email aziendale vs personale.

Il calo è quasi tutto concentrato negli account acquisiti tramite una nuova campagna paid destinata a freelance e studenti.

Nel segmento storico B2B il funnel è praticamente stabile.

## Il funnel non era rotto: era cambiato l'ingresso

Il mix dei nuovi utenti era cambiato.

Prima:

- 68% account aziendali;
- 32% individuali.

Dopo il lancio della campagna:

- 47% account aziendali;
- 53% individuali.

Gli utenti individuali hanno meno probabilità di invitare qualcuno perché spesso usano il prodotto da soli.

Il funnel aggregato peggiora, ma non perché l'esperienza sia necessariamente peggiorata.

È cambiata la popolazione che lo attraversa.

Questa è una forma classica di **mix shift**.

## La domanda cambia

La domanda iniziale era:

> “Cosa si è rotto nell'onboarding?”

Dopo l'analisi diventa:

> “La nuova acquisizione sta portando utenti con un modello di utilizzo diverso da quello per cui definiamo activation?”

Questa seconda domanda ha implicazioni molto diverse.

Potrebbero esserci almeno tre possibilità:

1. la campagna porta traffico di bassa qualità;
2. la definizione di activation è adatta al B2B ma non ai single-player users;
3. il prodotto potrebbe avere un'opportunità reale in un segmento nuovo che richiede un activation path diverso.

## L'errore possibile: ottimizzare il funnel sbagliato

Se il team ridisegnasse immediatamente la schermata degli inviti, potrebbe aumentare artificialmente il numero di inviti senza aumentare il valore reale ottenuto dagli utenti.

Potrebbe perfino introdurre spam o peggiorare l'esperienza.

Un funnel sano non deve massimizzare ogni passaggio.

Deve rappresentare una sequenza di comportamenti collegati alla creazione di valore.

## Da conversion funnel a behavioral model

L'analista ricostruisce l'activation distinguendo due percorsi:

### Collaborativo

Workspace → invito → documento condiviso → ritorno di almeno due membri.

### Individuale

Workspace → creazione di tre note → utilizzo in almeno tre giorni diversi → ritorno entro sette giorni.

Nel nuovo segmento individuale, il secondo percorso è molto più predittivo della retention a 30 giorni.

La decisione quindi non è “riparare il bottone invite”.

È:

- separare i due activation paths;
- misurare retention e monetizzazione per segmento;
- testare onboarding differenziato;
- rivalutare l'economia della nuova campagna.

## Metodo operativo

Quando un funnel peggiora:

1. verificare che tracking e definizioni siano stabili;
2. controllare mix e composizione delle coorti;
3. segmentare prima di attribuire la causa allo step;
4. collegare gli step a outcome di valore successivi;
5. distinguere perdita di conversione da cambio del comportamento desiderato;
6. testare la soluzione, non soltanto il sintomo.

> **Un funnel indica dove guardare. Non decide da solo cosa correggere.**
