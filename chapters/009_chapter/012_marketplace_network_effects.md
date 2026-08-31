## 9.11 Esperimenti su marketplace e network effects: quando gli utenti interferiscono tra loro

L'A/B test classico funziona meglio quando l'esperienza di un'unità non modifica il risultato delle altre. Nei marketplace questa assunzione spesso è fragile.

Se cambiamo il ranking per una parte dei buyer, influenziamo la domanda ricevuta dai seller. Se riduciamo le commissioni solo per alcuni driver, possiamo cambiare la disponibilità di corse anche per gli utenti del controllo. Se mostriamo più spesso certi ristoranti a un gruppo, riduciamo implicitamente la visibilità disponibile per altri.

Il trattamento "trabocca" tra gruppi.

### Caso simulato/composito - Il ranking che sembrava aumentare il GMV del 5,9%

Un marketplace di servizi locali testa un nuovo ranking che privilegia fornitori con maggiore probabilità di accettazione.

Randomizzazione iniziale: buyer-level.

Dopo tre settimane:

- conversion controllo: 12,4%;
- conversion trattamento: 13,1%;
- GMV per buyer: +5,9%;
- tempo medio alla conferma: -11%.

Sembra una vittoria netta.

Poi il team seller nota qualcosa: alcuni fornitori molto popolari stanno ricevendo quasi tutta la domanda del trattamento. Questi fornitori hanno capacità limitata. Quando saturano, diventano meno disponibili anche per i buyer assegnati al controllo.

Il controllo non è più un vero controfattuale: il trattamento ha modificato il mercato in cui anche il controllo opera.

Analizzando aree geografiche con bassa sovrapposizione e costruendo un successivo test clusterizzato per zona, l'effetto stimato sul GMV scende a circa +2,1%. Rimane positivo, ma molto inferiore al +5,9% iniziale.

### Perché succede

Nei sistemi con interazione tra utenti possono comparire:

- spillover;
- congestione;
- cannibalizzazione;
- capacity constraints;
- equilibrium effects;
- network effects;
- competizione per la stessa offerta.

L'effetto osservato su una piccola percentuale di traffico può anche non coincidere con quello a rollout completo.

### Strategie sperimentali

A seconda del problema si possono considerare:

- randomizzazione per area geografica;
- randomizzazione per marketplace locale;
- cluster randomization;
- switchback experiments, alternando trattamento e controllo nel tempo;
- analisi esplicita di spillover e saturazione.

Nessuna soluzione è universale. L'unità di randomizzazione deve riflettere il livello a cui l'interferenza diventa rilevante.

> **Quando il prodotto è un mercato, l'utente non è sempre l'unità indipendente giusta.**

### Un collegamento pubblico

Microsoft ha documentato problemi analoghi nei tenant-randomized experiments: quando gli utenti devono condividere un'esperienza coerente a livello di organizzazione, la randomizzazione per singolo utente non è appropriata. La piattaforma usa quindi tenant/cluster come unità e combina tecniche specifiche per correggere varianza e sensibilità.

### Fonte

- Microsoft Experimentation Platform, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work*.
