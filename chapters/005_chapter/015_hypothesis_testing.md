## 5.14 Test di ipotesi: trasformare un dubbio in una regola decisionale

Un test di ipotesi non è un rituale statistico e non è una macchina che produce verità. È un modo formale per chiedere: *se una certa ipotesi di base fosse vera, quanto sarebbero compatibili con essa i dati che abbiamo osservato?*

La struttura minima contiene due ipotesi. L'ipotesi nulla, indicata con \(H_0\), rappresenta in genere uno scenario di riferimento: nessuna differenza, nessun effetto, nessun cambiamento rispetto a una baseline. L'ipotesi alternativa, \(H_1\), rappresenta invece lo scenario che vogliamo valutare come possibile spiegazione dei dati.

Immaginiamo una piattaforma di food delivery che modifichi il processo di checkout. Prima della modifica, il tasso di completamento degli ordini era del 72%. Dopo il rilascio, su 18.400 sessioni osservate, il completamento sale al 73,1%.

La domanda di business è immediata: il nuovo checkout funziona davvero oppure stiamo osservando una normale fluttuazione casuale?

Una formulazione semplice può essere:

- \(H_0\): il nuovo checkout non cambia il vero tasso di completamento;
- \(H_1\): il nuovo checkout modifica il vero tasso di completamento.

Il punto importante è che il test non dimostra \(H_0\) né \(H_1\). Confronta ciò che abbiamo osservato con ciò che sarebbe plausibile osservare se \(H_0\) fosse vera.

### Prima del test viene la domanda

Un errore frequente è aprire un software statistico, lanciare un test e solo dopo cercare di interpretare il risultato. La sequenza dovrebbe essere opposta.

Prima dobbiamo stabilire:

- qual è la metrica;
- qual è la popolazione;
- qual è il confronto;
- quale effetto sarebbe rilevante per il business;
- quali errori decisionali siamo disposti ad accettare;
- quali assunzioni rendono il test appropriato.

Nel caso del checkout, per esempio, un incremento da 72% a 72,1% potrebbe risultare statisticamente rilevabile con milioni di sessioni ma essere economicamente irrilevante. Viceversa, un aumento da 72% a 74% potrebbe essere molto importante ma non ancora statisticamente conclusivo se il campione fosse piccolo.

### Caso realistico: il test che arrivò troppo tardi

Una società SaaS B2B lanciò una nuova sequenza di onboarding e osservò che la percentuale di utenti che completavano la configurazione entro sette giorni passava dal 61,4% al 64,0%.

Il team prodotto festeggiò. Tre settimane dopo un analyst ricostruì l'esperimento e scoprì che la nuova sequenza era stata assegnata soprattutto ai clienti europei, mentre il controllo conteneva una quota maggiore di clienti nordamericani enterprise, che avevano storicamente onboarding più lunghi.

Il problema non era il test statistico. Era il disegno dell'analisi.

Un test formalmente corretto applicato a gruppi non comparabili può produrre una conclusione molto precisa su una domanda sbagliata.

### Un test è parte di un processo più ampio

Il NIST, nelle sue linee metodologiche sui confronti statistici, sottolinea che i test di ipotesi dovrebbero essere accompagnati da intervalli, grafici ed esplorazione dei dati, perché il solo esito "rifiuta/non rifiuta" non descrive la dimensione dell'effetto né la struttura dei dati.[^nist-hyp]

La regola operativa è quindi:

**definizione del problema → disegno del confronto → controllo dei dati → stima dell'effetto → quantificazione dell'incertezza → test → interpretazione → decisione.**

Il test è un passaggio della catena, non la catena intera.

[^nist-hyp]: NIST, *Comparing Instruments*, Technical Note 2106, https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2106.pdf
