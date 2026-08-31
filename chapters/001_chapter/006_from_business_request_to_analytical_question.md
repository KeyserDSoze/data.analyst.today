## 1.5 Dalla richiesta di business alla domanda analitica

Le richieste che arrivano a un analista sono formulate nel linguaggio del business, non in quello dell'analisi.

> “Perché stiamo perdendo clienti?”

> “Quali prodotti dobbiamo spingere?”

> “La campagna marketing ha funzionato?”

> “Dobbiamo aumentare i prezzi?”

> “Quali clienti rischiano di abbandonarci?”

Sono domande importanti, ma contengono ancora concetti vaghi, popolazioni implicite, periodi non dichiarati e diversi possibili obiettivi analitici.

Il lavoro dell'analista consiste nel trasformarle in domande che possano essere **misurate, confrontate e smentite dai dati**.

Il Capitolo 2 costruirà un vero analytical brief. Qui introduciamo la trasformazione mentale che viene prima del documento.

### Esempio: “stiamo perdendo clienti”

La prima operazione è definire il fenomeno.

Che cosa significa perdere un cliente?

- non compra da 30 giorni?
- non rinnova l'abbonamento?
- cancella formalmente il contratto?
- riduce la frequenza d'acquisto?
- smette di utilizzare il prodotto?

Poi serve la popolazione.

Tutti i clienti? Soltanto quelli acquisiti negli ultimi dodici mesi? B2B o B2C? Una linea di prodotto specifica?

Poi serve il tempo.

Il fenomeno è aumentato rispetto al mese precedente, all'anno precedente o a una baseline storica?

Infine serve capire che cosa vogliamo ottenere.

Descrivere il churn, localizzarlo, prevederlo, stimare l'effetto di un intervento e scegliere quale intervento convenga sono problemi diversi.

### Cinque tipi di domanda da non confondere

La tassonomia non è universale, ma questa distinzione è molto utile nel lavoro quotidiano.

**Descrittiva — Che cosa è successo?**

> “Quanto è aumentato il churn nell'ultimo trimestre?”

Richiede soprattutto definizioni e misurazione corrette.

**Diagnostica — Dove e in quali condizioni è successo?**

> “In quali coorti, canali e segmenti è aumentato maggiormente?”

Serve a localizzare il fenomeno e restringere le ipotesi.

**Predittiva — Che cosa è probabile che succeda?**

> “Quali clienti hanno maggiore probabilità di abbandonare nei prossimi 30 giorni?”

Qui il problema è stimare un esito futuro, non necessariamente spiegarne la causa.

**Causale — Che cosa cambierebbe se intervenissimo?**

> “Un onboarding guidato ridurrebbe il churn rispetto all'esperienza attuale?”

Questa domanda richiede un disegno capace di sostenere un confronto controfattuale.

**Decisionale — Quale azione conviene intraprendere?**

> “Tra onboarding guidato, sconto e contatto del customer success, quale intervento genera il miglior valore netto per i segmenti su cui possiamo intervenire?”

Qui entrano anche costi, capacità operative, rischio e valore economico.

Una domanda non è “migliore” perché appartiene a una categoria più sofisticata. Spesso una buona decomposizione descrittiva risolve il problema senza bisogno di un modello.

### Rendere la domanda falsificabile

“Gli utenti sono insoddisfatti” è difficile da analizzare perché non specifica quale osservazione potrebbe smentire l'affermazione.

Una domanda migliore potrebbe essere:

> “Il tasso di rinnovo dei clienti che hanno aperto almeno due ticket ad alta severità nei 90 giorni precedenti è inferiore a quello di clienti comparabili senza ticket ad alta severità?”

Ora sono espliciti:

- una popolazione;
- un'esposizione;
- un outcome;
- una finestra temporale;
- un confronto.

La formulazione non garantisce che l'analisi sarà valida, ma rende visibili le scelte che dovremo discutere.

### La decisione viene prima della dashboard

Prima di costruire un report è utile provare a completare una frase:

> **“Se l'analisi mostra X, allora prenderemo in considerazione Y.”**

Non tutte le analisi devono produrre subito una decisione operativa, ma dovrebbero almeno poter spiegare quale incertezza riducono e perché quella riduzione conta.

Se nessun risultato plausibile cambierebbe alcuna scelta, potremmo trovarci davanti a una richiesta informativa a bassa priorità o a una dashboard senza un vero processo decisionale collegato.

> **Trasformare una richiesta in una buona domanda è già analisi.**
