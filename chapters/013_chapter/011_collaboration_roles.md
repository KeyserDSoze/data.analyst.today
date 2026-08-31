## 13.10 Collaborare tra analyst, analytics engineer, data engineer e data scientist

Molti problemi attribuiti agli strumenti sono in realtà problemi di confini organizzativi poco chiari.

Un Data Analyst non lavora in isolamento. Nei team maturi, il valore nasce spesso dall'interazione tra competenze diverse.

### Un modello mentale dei ruoli

| Ruolo | Domanda tipica |
|---|---|
| Data Analyst | Cosa sta succedendo e cosa significa per il business? |
| Analytics Engineer | Come rendiamo questa logica analitica affidabile e riusabile? |
| Data Engineer | Come facciamo arrivare il dato in modo stabile, scalabile e osservabile? |
| Data Scientist | Possiamo stimare, prevedere o ottimizzare un fenomeno con modelli più avanzati? |
| Business stakeholder | Quale decisione dobbiamo prendere? |

Queste categorie non sono rigide. In aziende piccole una persona può coprirne tre. In aziende grandi possono esistere specializzazioni ancora più fini.

Il punto non è il titolo. È sapere **quale problema appartiene a quale livello**.

### Caso realistico: il dashboard che si rompe ogni lunedì

Un analyst costruisce una dashboard vendite collegata direttamente a tre database operativi.

Ogni lunedì:

- una sorgente risponde lentamente;
- una tabella cambia schema;
- il refresh fallisce;
- l'analyst perde due ore a sistemare il problema.

La soluzione non è diventare più bravo a fare refresh manuali.

Il problema è passato da analisi a **affidabilità della pipeline**.

A quel punto serve collaborazione con engineering.

### Quando l'analyst dovrebbe chiedere supporto

Segnali tipici:

- la stessa trasformazione viene riscritta da molti analyst;
- un dataset alimenta processi business critici;
- il volume cresce oltre ciò che uno script locale gestisce bene;
- servono SLA o alert;
- la logica deve essere usata da più team;
- l'accesso ai dati richiede governance o sicurezza avanzata;
- un prototipo sta diventando servizio operativo.

### Quando invece non serve escalation tecnica

Non ogni analisi esplorativa ha bisogno di una pipeline industriale.

Se una domanda è una tantum, il dataset è piccolo e la decisione deve essere presa oggi, costruire tre livelli di orchestrazione e CI/CD può essere puro overhead.

La maturità consiste anche nel **non industrializzare troppo presto**.

### Caso realistico: churn prediction che nessuno può usare

Il data scientist produce un modello con AUC 0,89.

Il Customer Success Manager chiede:

> "Chi devo chiamare domani mattina?"

Il modello restituisce 62.000 account ad alto rischio.

Il team CS può contattarne 450 a settimana.

Qui la parte statistica è buona ma il prodotto analitico è incompleto.

L'analyst può fare da ponte tra modello e decisione:

- definire segmenti prioritari;
- stimare valore economico per account;
- introdurre soglie coerenti con capacità operativa;
- misurare il trattamento;
- distinguere rischio da persuadibilità.

### La collaborazione migliore parte dal contratto decisionale

Prima di discutere di strumenti o modelli, il team dovrebbe chiarire:

1. quale decisione deve essere presa;
2. da chi;
3. con quale frequenza;
4. entro quale tempo;
5. con quale livello di rischio;
6. con quali risorse operative.

Questa semplice disciplina riduce moltissimi progetti tecnicamente impressionanti ma inutilizzati.

### Regola operativa

> **Il confine tra ruoli dovrebbe seguire la natura del problema, non il titolo scritto sull'organigramma.**
