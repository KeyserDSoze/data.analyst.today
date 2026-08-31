## 9.7 Sample size e Minimum Detectable Effect: quanto traffico serve davvero?

Un esperimento non diventa affidabile solo perché coinvolge "molti utenti". La domanda corretta è: **quanti utenti servono per rilevare un effetto abbastanza piccolo da essere ancora rilevante per il business?**

Il concetto operativo è il Minimum Detectable Effect, o MDE: la più piccola variazione che vogliamo essere in grado di distinguere dal rumore con una probabilità ragionevole.

Se la conversione di checkout è del 4,0%, un miglioramento di 0,05 punti percentuali può essere statisticamente interessante ma economicamente irrilevante. Un aumento di 0,4 punti percentuali, invece, potrebbe valere milioni. Il sample size deve quindi partire dalla decisione, non da una formula scollegata dal contesto.

### Caso simulato/composito - Il bottone che valeva troppo poco

Una grande piattaforma travel vuole testare un nuovo bottone di conferma prenotazione. La baseline è:

- conversion rate: 3,80%;
- sessioni eleggibili al mese: 4,2 milioni;
- margine medio per booking: 17,40 euro.

Il product manager propone un MDE relativo del 2%, cioè circa +0,076 punti percentuali. Il test richiederebbe una quantità di traffico rilevante e diverse settimane.

L'analista fa però una domanda diversa: quanto vale quell'effetto?

Un incremento di 0,076 punti percentuali su 4,2 milioni di sessioni equivale a circa 3.192 booking aggiuntivi al mese. A 17,40 euro di margine, parliamo di circa 55.500 euro mensili prima dei costi operativi e degli effetti collaterali.

Il team scopre che il redesign richiede manutenzione su quattro codebase e introduce dipendenze con due sistemi di pagamento. Il costo annuale stimato supera il beneficio atteso dell'MDE originario.

La soglia viene quindi ridefinita: il team vuole rilevare almeno +0,15 punti percentuali. Il test diventa più breve e soprattutto allineato a una decisione economicamente sensata.

> **Il MDE non è solo una scelta statistica. È una dichiarazione su quale effetto sarebbe abbastanza importante da cambiare una decisione.**

### Cosa determina il sample size

A parità di tutto il resto, servono più osservazioni quando:

- l'effetto che vogliamo rilevare è più piccolo;
- la metrica è più rumorosa;
- chiediamo maggiore potenza statistica;
- imponiamo una soglia di errore di tipo I più severa;
- la randomizzazione avviene a livello di cluster, tenant, negozio o area geografica anziché utente;
- la metrica primaria è rara, come frodi, cancellazioni o incidenti.

Per proporzioni, la dimensione campionaria dipende fortemente dal tasso di base. Per metriche continue, conta molto la varianza storica.

### Errore frequente: scegliere il test in base al tempo disponibile

"Abbiamo dieci giorni" non è un criterio statistico. Se in dieci giorni il test non può distinguere un effetto economicamente utile dal rumore, le opzioni corrette sono:

1. aumentare il traffico;
2. allungare il test;
3. usare una metrica più sensibile e coerente;
4. applicare tecniche di variance reduction se appropriate;
5. accettare esplicitamente che il risultato sarà inconclusivo.

La scelta sbagliata è fingere che dieci giorni siano sufficienti solo perché la roadmap lo richiede.

### Fonti

- Microsoft Experimentation Platform, *Beyond Power Analysis: Metric Sensitivity Analysis in A/B Tests*.
