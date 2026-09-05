## 1.5 Dalla richiesta di business alla domanda analitica

Le richieste che arrivano a un analista raramente sono formulate nel linguaggio dell'analisi. Arrivano nel linguaggio dell'organizzazione:

> “Perché stiamo perdendo clienti?”

> “Quali prodotti dobbiamo spingere?”

> “La campagna marketing ha funzionato?”

> “Dobbiamo aumentare i prezzi?”

Sono domande legittime, ma non ancora specifiche abbastanza da determinare un'analisi. Dentro ciascuna ci sono concetti vaghi, popolazioni implicite, periodi non dichiarati e soprattutto più obiettivi possibili.

Il lavoro dell'analista consiste nel trasformare la richiesta in qualcosa che possa essere **misurato, confrontato e smentito dai dati**. Il Capitolo 2 costruirà un vero analytical brief; qui ci interessa il passaggio mentale che deve avvenire prima di qualsiasi documento.

### “Stiamo perdendo clienti” non è ancora un fenomeno definito

Supponiamo che un manager dica che stiamo perdendo clienti. La prima tentazione è aprire il dashboard del churn. Ma anche “perdere un cliente” può significare cose molto diverse: mancato rinnovo di un abbonamento, assenza di acquisti per un certo periodo, riduzione della frequenza, cancellazione formale del contratto o progressiva scomparsa dell'utilizzo del prodotto.

Queste definizioni non sono intercambiabili. Un e-commerce con acquisti stagionali e un SaaS con rinnovo mensile non possono usare lo stesso segnale per definire l'abbandono senza modificare il fenomeno che stanno osservando.

Dopo la definizione viene la popolazione. Il problema riguarda tutti i clienti o soltanto quelli acquisiti recentemente? B2B e B2C si comportano nello stesso modo? La dinamica è comune a tutti i prodotti? Poi viene il tempo: il fenomeno è cambiato rispetto al mese precedente, all'anno precedente o a una baseline costruita sulla stagionalità?

Solo a quel punto possiamo chiederci quale tipo di risposta serva davvero.

### Cinque domande diverse possono nascondersi nella stessa richiesta

La distinzione seguente non è una tassonomia universale della professione. È un modo pratico per evitare di usare lo stesso metodo per problemi che chiedono forme di evidenza diverse.

| Tipo | Domanda | Esempio sul churn | Che cosa deve produrre l'analisi |
|---|---|---|---|
| **Descrittiva** | Che cosa è successo? | Quanto è aumentato il churn nell'ultimo trimestre? | una misura definita e confrontabile |
| **Diagnostica** | Dove e in quali condizioni è successo? | In quali coorti, canali e segmenti è aumentato? | una localizzazione del fenomeno e ipotesi più ristrette |
| **Predittiva** | Che cosa è probabile che succeda? | Quali clienti rischiano di abbandonare nei prossimi 30 giorni? | una stima dell'esito futuro |
| **Causale** | Che cosa cambierebbe se intervenissimo? | Un onboarding guidato ridurrebbe il churn? | un confronto controfattuale credibile |
| **Decisionale** | Quale azione conviene intraprendere? | Tra onboarding, sconto e contatto del customer success, quale intervento crea più valore? | una scelta che combina evidenza, costi, vincoli e rischio |

Il passaggio da una categoria all'altra non rende automaticamente l'analisi più sofisticata o più utile. Spesso una buona decomposizione descrittiva o diagnostica risolve il problema prima che serva un modello. In altri casi una previsione accurata non risponde affatto alla domanda causale che interessa al business: sapere chi è a rischio non equivale a sapere quale intervento ridurrà quel rischio.

La forma della domanda determina quindi il tipo di evidenza che dobbiamo cercare.

### Rendere visibili le scelte rende la domanda verificabile

Consideriamo la frase:

> “Gli utenti sono insoddisfatti.”

È difficile da analizzare non soltanto perché “insoddisfatti” è vago, ma perché non specifica quale osservazione potrebbe contraddire la nostra intuizione.

Una formulazione più utile potrebbe essere:

> “Il tasso di rinnovo dei clienti che hanno aperto almeno due ticket ad alta severità nei 90 giorni precedenti è inferiore a quello di clienti comparabili senza ticket ad alta severità?”

Ora sono visibili una popolazione, un'esposizione, un outcome, una finestra temporale e un confronto. La nuova formulazione non rende automaticamente valida l'analisi: “clienti comparabili” è ancora un problema da risolvere e i ticket possono essere un proxy imperfetto della soddisfazione. Ma proprio questo è il vantaggio. Le assunzioni non sono più nascoste dentro una frase generica; possiamo discuterle e testarle.

Una buona domanda analitica non elimina l'incertezza in partenza. **La rende localizzabile.**

### La decisione chiarisce quanto deve essere buona la risposta

Prima di costruire un report è utile completare una frase:

> **“Se l'analisi mostra X, allora prenderemo in considerazione Y.”**

Questo semplice esercizio costringe a collegare la domanda a un uso. Se stiamo valutando un piccolo test reversibile, possiamo accettare evidenza più preliminare. Se il risultato deve sostenere una modifica di prezzo globale o un investimento difficile da invertire, la soglia cambia.

Non tutte le analisi devono produrre immediatamente una decisione operativa. Possono servire a comprendere un fenomeno o a stabilire che cosa non sappiamo ancora. Ma dovrebbero poter spiegare quale incertezza riducono e perché quella riduzione conta.

Se nessun risultato plausibile cambierebbe la nostra comprensione, la priorità o una scelta futura, potremmo trovarci davanti a una richiesta informativa a basso valore o a una dashboard priva di un vero processo decisionale collegato.

> **Trasformare una richiesta in una buona domanda non è preparazione all'analisi. È già analisi.**
