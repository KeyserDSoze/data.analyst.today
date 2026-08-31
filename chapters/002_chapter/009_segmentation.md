## 2.8 Segmentazioni previste: dove ci aspettiamo eterogeneità utile

Le medie aggregate possono nascondere fenomeni decisivi.

Ma il Capitolo 6 sarà il luogo in cui studieremo davvero segmentazione, coorti, funnel, retention e churn. Nel brief ci interessa una domanda precedente:

> **Quali dimensioni vale la pena preparare prima dell'analisi perché potrebbero cambiare la spiegazione o l'azione?**

### Segmentare con una ragione

Dimensioni frequenti includono:

- area geografica;
- canale di acquisizione;
- prodotto o categoria;
- piano commerciale;
- anzianità del cliente;
- fascia di valore;
- dimensione aziendale;
- dispositivo;
- coorte temporale.

Non devono entrare tutte nel brief.

Una segmentazione merita priorità quando esiste una ragione per credere che:

1. il fenomeno possa comportarsi diversamente nel gruppo;
2. il dato sia sufficientemente affidabile;
3. una differenza porterebbe a una spiegazione o a un'azione diversa.

Segmentare per una variabile disponibile ma irrilevante aggiunge rumore, non informazione.

### Pre-specificata ed esplorativa

È utile distinguere due momenti.

**Segmentazioni pre-specificate**

Sono motivate prima di vedere il risultato.

Esempio: se un nuovo checkout è stato rilasciato soltanto su mobile, `device` è una segmentazione ovvia da prevedere nel brief.

**Segmentazioni esplorative**

Emergono durante l'EDA perché osserviamo pattern inattesi.

Sono preziose, ma vanno trattate come scoperte da confermare, soprattutto se abbiamo esplorato moltissime combinazioni.

Questa distinzione aiuta a evitare una forma di *data fishing*: cercare tra centinaia di tagli finché ne appare uno spettacolare e poi raccontarlo come se fosse stato atteso dall'inizio.

### Caso simulato/composito: retention stabile, mix cambiato

La retention complessiva scende dall'82% al 77%.

Segmentando per canale scopriamo che la retention dentro ogni canale è quasi stabile. È invece aumentato molto il peso di un canale paid-social che storicamente ha retention inferiore.

La diagnosi cambia:

- non abbiamo necessariamente un peggioramento dell'esperienza dentro i segmenti;
- abbiamo un **mix di acquisizione diverso**.

La decisione potrebbe quindi spostarsi dal prodotto al marketing mix.

È un esempio del motivo per cui il livello di aggregazione conta e anticipa temi come il paradosso di Simpson, che approfondiremo nel Capitolo 4.

### Una segmentazione deve poter cambiare qualcosa

Una buona domanda è:

> **“Se questo segmento risultasse molto diverso, prenderemmo una decisione diversa?”**

Se la risposta è no, il taglio può essere interessante ma probabilmente non è prioritario nel brief iniziale.

### Campo del brief

| Segmentazione | Perché potrebbe contare | Decisione che potrebbe cambiare | Priorità |
|---|---|---|---|
| device | rollout differente mobile/desktop | rollback mirato | alta |
| acquisition channel | mix clienti differente | riallocazione budget | alta |
| paese | policy e pricing diversi | intervento locale | media |

Le segmentazioni esplorative potranno aggiungersi dopo, ma annotare quelle motivate prima dell'analisi rende il piano più disciplinato.

> **Segmenta non perché puoi dividere il dataset, ma perché una differenza tra gruppi potrebbe cambiare ciò che credi o ciò che fai.**
