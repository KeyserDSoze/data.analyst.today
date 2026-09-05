## 2.1 Dal sintomo al problema analitico

Una richiesta di business nasce quasi sempre da qualcosa che preoccupa o interessa l'organizzazione: clienti che sembrano diminuire, margini che si comprimono, una campagna che non convince, un processo che rallenta. Il primo compito dell'analista non è sostituire quella frase con un termine tecnico. È preservarne il significato mentre la trasforma in qualcosa che possa essere osservato e discusso con precisione.

Consideriamo la richiesta:

> “Stiamo perdendo clienti.”

Questa frase descrive un problema di business, ma non dice ancora che cosa significhi “perdere”. Potrebbe indicare cancellazioni contrattuali, assenza di acquisti per novanta giorni, riduzione d'uso, downgrade o perdita di marginalità. Scegliere in silenzio la definizione più facile da calcolare introdurrebbe una precisione soltanto apparente: la query sarebbe specifica, ma la domanda resterebbe irrisolta.

Una formulazione analitica più utile potrebbe essere:

> “La retention a 90 giorni delle coorti acquisite negli ultimi sei mesi è diminuita rispetto alle coorti comparabili dell'anno precedente? In quali segmenti si concentra il delta e quali cambiamenti osservabili lo precedono?”

La nuova frase non è semplicemente una parafrasi. Ha introdotto un outcome, una popolazione, un orizzonte temporale, una baseline e una direzione investigativa. Soprattutto, ha reso possibile discutere se quelle scelte rappresentino davvero il problema che il business vuole capire.

## La traduzione deve conservare il legame con la decisione

Il passaggio da business problem ad analytical problem è riuscito soltanto se rende più chiaro che cosa dovremo osservare **senza perdere il motivo per cui lo osserviamo**. Scrivere “analizziamo il churn perché stiamo perdendo clienti” non basta: ha sostituito una parola con un'altra, ma non ci dice quale decisione cambierà né quale evidenza sarebbe importante.

Una formulazione più completa lega invece fenomeno e decisione:

> **Dobbiamo capire [fenomeno] per supportare [decisione], osservando [popolazione] nel periodo [tempo], misurando [outcome] e confrontando [baseline o alternative].**

Per esempio:

> “Dobbiamo capire che cosa sta comprimendo il margine e-commerce per decidere se intervenire su pricing, promozioni o logistica, osservando gli ordini completati degli ultimi dodici mesi e confrontando margine e driver con lo stesso periodo dell'anno precedente.”

Questa frase non contiene ancora tutto il brief, ma cambia già il modo in cui verrà eseguito il lavoro. Se la decisione riguarda pricing, promozioni o logistica, il margine deve essere definito in modo coerente con quelle leve; una semplice analisi della revenue sarebbe insufficiente. Se il confronto è year-over-year, dovremo verificare stagionalità e comparabilità del perimetro. La specifica comincia quindi a generare requisiti concreti.

## Ambiguità non risolta è un requisito, non un dettaglio

La professionalità non consiste nel far sparire l'ambiguità rapidamente. Consiste nel renderla discutibile prima che si trasformi in codice.

Se “cliente perso” ha più significati plausibili, il brief deve registrare la scelta. Potremmo scrivere:

> “Per questa analisi useremo churn contrattuale, definito come cancellazione dell'abbonamento. Il calo di utilizzo verrà trattato come possibile leading indicator, non come churn.”

Da quel momento sappiamo sia che cosa misura l'outcome sia che cosa **non** misura. Questa distinzione diventerà importante più avanti, quando useremo il calo di utilizzo come possibile spiegazione o segnale anticipatore senza confonderlo con l'evento finale.

Prima di procedere, il team dovrebbe quindi riuscire a chiarire almeno il nucleo del problema: che cosa sembra essere cambiato, perché conta, quale decisione potrebbe essere influenzata, quale fenomeno deve essere definito operativamente, quale popolazione e quale confronto sono rilevanti e quanto costa sbagliare. Non serve trasformare queste domande in un'intervista interminabile; serve evitare che le risposte vengano inventate implicitamente durante l'esecuzione.

> **La richiesta descrive il sintomo. Il problema analitico specifica quale evidenza può trasformare quel sintomo in qualcosa di comprensibile e azionabile.**
