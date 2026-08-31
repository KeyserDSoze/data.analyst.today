## 5.17 Significatività statistica e rilevanza business non sono la stessa cosa

Una delle competenze più importanti per un analyst è saper tenere separate due domande:

1. l'effetto osservato è distinguibile dalla variabilità casuale?
2. l'effetto è abbastanza grande da cambiare una decisione?

La prima domanda è statistica. La seconda è economica, operativa o strategica.

Confonderle produce decisioni mediocri.

### Caso realistico: una campagna CRM "vincente"

Una catena retail invia una nuova sequenza CRM a 2,8 milioni di clienti. Il tasso di riacquisto a 30 giorni passa dal 18,42% al 18,55%.

La differenza è di 0,13 punti percentuali.

Con un campione così grande, il risultato può risultare statisticamente molto convincente.

Il team marketing propone quindi di adottare la nuova sequenza su tutta la customer base.

Ma il costo incrementale per cliente è 0,09 euro tra piattaforma, messaggistica e incentivo. Il margine medio generato dai riacquisti aggiuntivi non copre completamente il costo.

Il test ha trovato un effetto. Il business ha trovato un investimento mediocre.

### Minimum Detectable Effect e Minimum Business-Relevant Effect

Un concetto utile è distinguere tra:

- **Minimum Detectable Effect (MDE)**: l'effetto minimo che un esperimento, date dimensione campionaria e variabilità, è progettato per rilevare con una certa potenza;
- **Minimum Business-Relevant Effect (MBRE)**: l'effetto minimo che giustificherebbe una decisione dal punto di vista del business.

I due numeri dovrebbero essere collegati.

Se il business considera interessante solo un miglioramento di almeno +0,5 punti percentuali, progettare un test capace di rilevare variazioni di +0,05 può produrre grande precisione su effetti irrilevanti.

### Caso realistico: ridurre i tempi di consegna

Un'azienda logistica testa un nuovo algoritmo di routing.

Su 420.000 consegne:

- media controllo: 41,8 ore;
- media trattamento: 41,5 ore;
- differenza: -0,3 ore, cioè 18 minuti;
- p-value: molto piccolo.

Statisticamente, il cambiamento è credibile.

Ma l'algoritmo aumenta il costo operativo di 0,47 euro per spedizione. I clienti non percepiscono differenze inferiori a circa due ore, e l'NPS non cambia in modo sostanziale.

Dire "abbiamo migliorato significativamente i tempi di consegna" è statisticamente difendibile ma managerialmente fuorviante.

### Effect size prima della celebrazione

Per interpretare un risultato servono almeno tre elementi:

- grandezza dell'effetto;
- incertezza sull'effetto;
- costo o valore economico associato.

Per esempio:

> La variante aumenta la conversione di +0,24 punti percentuali, con intervallo di confidenza 95% tra +0,07 e +0,41. Il break-even economico è +0,18 punti percentuali.

Questa frase contiene molta più informazione di:

> p = 0,012, risultato significativo.

### Decisioni sotto incertezza

Un intervallo di confidenza può attraversare la soglia economica rilevante. In quel caso il problema non è soltanto "statisticamente significativo o no". La domanda diventa:

> Quanto è plausibile che il vero effetto sia abbastanza grande da giustificare il costo?

Anche in un'impostazione frequentista, guardare l'intervallo rispetto a soglie decisionali aiuta a capire se i dati consentono una scelta robusta.

La American Statistical Association sottolinea che il p-value non misura la dimensione dell'effetto né l'importanza del risultato, e che decisioni di business non dovrebbero dipendere esclusivamente dal superamento di una soglia convenzionale.[^asa-business]

### Regola operativa

Ogni volta che presenti un test, prova ad aggiungere una riga che risponda a questa domanda:

**Se questo effetto fosse esattamente della dimensione stimata, cambierebbe davvero ciò che facciamo?**

Se la risposta è no, la significatività statistica non basta.

[^asa-business]: American Statistical Association, *Statement on Statistical Significance and P-Values*, https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
