## 6.14 Esercizi: ragionare su funnel, retention e churn

Gli esercizi di questo capitolo non richiedono soltanto calcoli. L'obiettivo è allenare la capacità di definire correttamente il problema prima di misurarlo.

### Esercizio 1 — Activation ambigua

Una piattaforma di videoconferenza considera “attivato” qualsiasi utente che abbia creato un account e avviato almeno una call.

I dati mostrano:

- signup mensili: 80.000;
- utenti con almeno una call: 62.000;
- utenti con almeno una call con un partecipante esterno: 41.000;
- utenti con almeno tre call in sette giorni: 19.000;
- retention a 60 giorni tra chi ha fatto una sola call: 18%;
- retention a 60 giorni tra chi ha fatto almeno tre call: 57%.

Domande:

1. Quale evento useresti come activation?
2. Quali ulteriori segmentazioni controlleresti?
3. Quale rischio c'è nel scegliere l'evento che massimizza semplicemente la correlazione con la retention?

### Esercizio 2 — Funnel che migliora, revenue che peggiora

Un e-commerce modifica il checkout. Dopo il redesign:

- add-to-cart → checkout: dal 54% al 61%;
- checkout → pagamento: dal 71% al 76%;
- conversion rate complessivo: +9%;
- average order value: -13%;
- return rate: dal 8% al 12%.

Scrivi una breve nota al Product Manager spiegando perché il funnel non può essere considerato vinto sulla base del solo conversion rate.

### Esercizio 3 — Due coorti, stessa retention D30

Due coorti hanno entrambe retention D30 del 52%.

Coorte A:

- D1: 86%;
- D7: 68%;
- D14: 58%;
- D30: 52%.

Coorte B:

- D1: 63%;
- D7: 56%;
- D14: 54%;
- D30: 52%.

Quali storie di prodotto potrebbero produrre due curve così diverse? Dove concentreresti l'analisi?

### Esercizio 4 — Churn o downgrade?

Una società SaaS perde 40 clienti su 1.000 in un trimestre. Nello stesso periodo 85 clienti riducono il proprio contratto e 30 espandono l'ARR.

Calcola e discuti perché il logo churn da solo può essere insufficiente per descrivere la salute della base clienti.

### Esercizio 5 — Il modello di churn

Un modello assegna un rischio elevato a clienti che:

- hanno meno login;
- aprono più ticket;
- utilizzano meno feature;
- hanno meno utenti attivi.

Per ciascuna variabile, proponi almeno due spiegazioni alternative. Poi indica quali interventi potresti testare senza assumere che la variabile sia causale.

### Esercizio finale — Il board vuole una risposta domani

Sei Data Analyst di una subscription company. Il board chiede perché la retention a sei mesi è scesa dal 67% al 59%.

Hai queste informazioni:

- la maggior parte del calo viene da due coorti recenti;
- entrambe provengono in gran parte da un nuovo canale di acquisition;
- il time-to-value è aumentato da 2,8 a 6,4 giorni;
- il pricing è aumentato nello stesso periodo;
- una parte del tracking dell'onboarding è cambiata;
- non esiste ancora un esperimento causale.

Prepara una risposta in tre sezioni:

1. cosa sappiamo;
2. cosa è plausibile ma non ancora dimostrato;
3. cosa faresti nelle prossime due settimane per ridurre l'incertezza.

Questo è il tipo di risposta che distingue una dashboard da un'analisi.
