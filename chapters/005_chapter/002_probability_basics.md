## 5.1 Eventi e probabilità: prima del numero viene il processo

La probabilità parte da una domanda apparentemente semplice:

> **Quale evento stiamo cercando di modellare?**

Un evento può essere:

- un cliente che rinnova entro la data prevista;
- una transazione che diventa chargeback entro 60 giorni;
- un ordine che supera lo SLA di consegna;
- un lead che acquista entro 30 giorni dalla demo;
- una macchina che si guasta entro il prossimo ciclo manutentivo.

Il primo errore non è matematico. È **semantico**.

“Cliente perso” può significare mancato rinnovo, cancellazione formale, nessun utilizzo per 90 giorni o contrazione del contratto. Quattro definizioni producono quattro eventi diversi e quindi quattro probabilità diverse.

Il Capitolo 2 ci ha insegnato a specificare la metrica. Qui aggiungiamo una proprietà:

> **la probabilità deve sempre riferirsi a un evento, una popolazione e un orizzonte temporale espliciti.**

### Caso simulato/composito — Quanti ticket verranno escalati domani?

Una piattaforma SaaS riceve mediamente circa 2.500 ticket al giorno. Negli ultimi tre mesi, tra i ticket comparabili, il 3,2% è stato escalato al team specialistico.

Il responsabile support chiede:

> “Quanti escalation dobbiamo aspettarci domani?”

Una prima stima è:

`2.500 × 3,2% = 80 escalation attese`.

Ma **80 non è una previsione deterministica**.

Domani potrebbero essercene 68, 83 o 97. Il 3,2% descrive un processo incerto e l'80 è un valore atteso sotto alcune assunzioni.

Prima di usarlo per il capacity planning l'analista verifica:

- i ticket di domani appartengono alla stessa popolazione storica?
- sono cambiate release, canali o categorie di problema?
- il volume di 2.500 è realistico per quel giorno della settimana?
- l'escalation rate è stabile o dipende fortemente dal tipo di ticket?

La probabilità non sostituisce il contesto. Lo rende esplicito.

### Frequenza osservata e probabilità futura

Se osserviamo 200.000 ordini e 14.000 resi, la frequenza empirica è 7%.

Possiamo usare quel 7% come stima della probabilità di reso di nuovi ordini soltanto nella misura in cui il futuro resta comparabile al processo che ha prodotto lo storico.

Se domani cambia il mix di prodotto, la politica di reso o il paese servito, il dato storico può rimanere perfettamente corretto e diventare una stima poco utile.

Per questo una probabilità storica contiene sempre una clausola implicita:

> **“se le condizioni rilevanti restano sufficientemente simili”.**

### Probabilità marginale e probabilità congiunta

Supponiamo che in una customer base:

- il 46% utilizzi il prodotto almeno quattro volte a settimana;
- il 78% rinnovi;
- il 42% utilizzi il prodotto almeno quattro volte a settimana **e** rinnovi.

Sono tre quantità diverse:

- `P(Uso alto) = 46%`;
- `P(Rinnovo) = 78%`;
- `P(Uso alto ∩ Rinnovo) = 42%`.

Le prime due descrivono eventi considerati singolarmente. La terza descrive la loro intersezione.

Questa distinzione diventa essenziale quando passiamo dalla domanda:

> “Quanto spesso succede A?”

alla domanda:

> “Quanto spesso succede A **insieme a** B?”

### Il complemento può rendere più visibile il rischio

Se il renewal rate è 82%, il non-renewal rate è 18%.

Matematicamente sono la stessa informazione:

`P(non rinnovo) = 1 - P(rinnovo)`.

Ma il framing cambia la lettura operativa.

“82% rinnova” può sembrare una performance rassicurante. “18% non rinnova” rende immediatamente visibile che quasi un cliente su cinque è a rischio a ogni ciclo.

L'analista dovrebbe conoscere entrambe le formulazioni e scegliere quella più adatta alla decisione, senza usarle per manipolare la percezione.

### Probabilità individuale e frequenza di gruppo

Se un modello assegna a un cliente `70%` di probabilità di churn, quel cliente non “churnerà al 70%”. Avrà un solo esito osservato.

Il significato diventa verificabile su gruppi di casi comparabili: se prendiamo molti clienti ai quali il modello assegna circa il 70% e il modello è ben calibrato, ci aspettiamo che una quota vicina al 70% faccia churn.

Questa distinzione tornerà nel Capitolo 10 sui modelli predittivi.

### La scheda minima di una probabilità

Ogni volta che usiamo una probabilità in un'analisi, dovremmo poter compilare:

```text
Evento:
Popolazione eleggibile:
Orizzonte temporale:
Fonte della stima:
Condizioni assunte stabili:
Decisione che usa la probabilità:
```

Se uno di questi campi è ambiguo, il problema non si risolve aggiungendo decimali.

> **Una probabilità precisa applicata all'evento sbagliato resta una risposta sbagliata.**
