## 5.16 Errori di tipo I e II: quando sbagliare ha costi diversi

Ogni test di ipotesi può sbagliare. La statistica non elimina questo rischio: lo rende esplicito.

Un errore di tipo I avviene quando rifiutiamo \(H_0\) pur essendo vera. In termini di business, concludiamo che esiste un effetto quando in realtà non c'è.

Un errore di tipo II avviene quando non rifiutiamo \(H_0\) pur essendo falsa. In pratica, non rileviamo un effetto che esiste davvero.

Queste due possibilità non sono simmetriche dal punto di vista economico.

### Caso realistico: antifrode

Una fintech sta valutando una nuova regola per bloccare transazioni sospette.

Se la regola produce troppi falsi positivi, vengono bloccati clienti legittimi. Il costo è composto da chiamate al supporto, abbandono, perdita di fiducia e minore conversione.

Se la regola produce troppi falsi negativi, vengono autorizzate frodi reali. Il costo è finanziario e reputazionale.

La scelta della soglia non è quindi puramente statistica. È una decisione economica sul costo relativo dei due errori.

### Alpha non è un numero sacro

Il livello di significatività α controlla la probabilità di errore di tipo I nel quadro del test. Impostare α = 0,05 significa accettare, sotto le assunzioni del test, un certo rischio di falso positivo.

Ma perché il 5% dovrebbe essere appropriato per ogni decisione?

Per una modifica cosmetica a una landing page, un falso positivo può costare poco. Per lanciare un farmaco, disattivare un impianto industriale o bloccare milioni di pagamenti, il costo può essere molto diverso.

Il livello di evidenza richiesto dovrebbe riflettere il contesto decisionale.

### Potenza statistica

La potenza di un test è la probabilità di rilevare un effetto quando quell'effetto esiste realmente, per una specifica dimensione dell'effetto.

La potenza dipende da diversi fattori:

- dimensione del campione;
- variabilità dei dati;
- grandezza dell'effetto;
- livello di significatività;
- struttura del disegno sperimentale.

Un test sottodimensionato può fallire non perché il trattamento non funzioni, ma perché non ha sufficiente informazione per distinguere l'effetto dal rumore.

### Caso realistico: il test che "non funzionò"

Un e-commerce prova una nuova pagina di pagamento. Il team si aspetta un miglioramento realistico della conversione dal 3,0% al 3,15%, cioè +0,15 punti percentuali.

Dopo quattro giorni il test ha raccolto 8.000 utenti per gruppo. Le conversioni risultano:

- controllo: 3,01%;
- variante: 3,19%.

Il p-value non supera la soglia stabilita dal team.

Il product manager conclude: "La variante non funziona".

L'analyst calcola però che il test era stato pianificato senza una power analysis. Con quella baseline e con quell'effetto minimo rilevante, il campione necessario era molto più grande.

Il test non aveva dimostrato che l'effetto fosse assente. Aveva dimostrato che l'esperimento era troppo piccolo per prendere una decisione affidabile.

### Potenza e decisione

Fare power analysis prima di un test significa chiedere:

> Qual è il più piccolo effetto che ci interessa davvero rilevare, e quanti dati servono per avere una probabilità ragionevole di rilevarlo?

Questa domanda lega statistica e business in modo diretto.

Il NIST evidenzia il trade-off tra errori di tipo I e tipo II: ridurre completamente uno dei due può aumentare drasticamente l'altro, fino a ottenere test inutili.[^nist-errors]

Un test che non rifiuta mai \(H_0\) non produce falsi positivi, ma non scopre mai nulla.

[^nist-errors]: NIST, *Comparing Instruments*, Technical Note 2106, https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2106.pdf
