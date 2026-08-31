## 2.1 Dal problema di business al problema analitico

Il Capitolo 1 ha già mostrato che una richiesta di business non è ancora una domanda analitica. Qui ci interessa il passaggio successivo: **come documentare la traduzione senza perdere il problema originale**.

Un problema di business riguarda un risultato, un rischio o un'opportunità.

> “Stiamo perdendo clienti.”

Un problema analitico specifica invece che cosa dobbiamo misurare e confrontare per ridurre l'incertezza su quel risultato.

> “La retention a 90 giorni delle coorti acquisite negli ultimi sei mesi è diminuita rispetto alle coorti comparabili dell'anno precedente? In quali segmenti si concentra il delta e quali cambiamenti osservabili lo precedono?”

La seconda formulazione introduce:

- un outcome definito;
- una popolazione;
- un orizzonte temporale;
- una baseline;
- una segmentazione;
- una direzione investigativa.

Ma non deve sostituire il problema di business. Deve rimanergli collegata.

### Traduzione non significa parafrasi

Scrivere:

> “Vogliamo analizzare il churn perché stiamo perdendo clienti.”

non è una vera traduzione. Ha soltanto sostituito una parola con una metrica.

Una traduzione utile rende possibile decidere:

- che cosa osserveremo;
- quale evidenza sarebbe sorprendente;
- quali dati servono;
- quale metodo potrebbe essere necessario;
- quale decisione potrebbe cambiare.

### Il rischio della falsa precisione

Precisione non significa inventare definizioni che il business non ha ancora concordato.

Se “cliente perso” può significare cancellazione formale, 90 giorni senza acquisto, riduzione d'uso o perdita di marginalità, l'analista non dovrebbe scegliere in silenzio la versione più facile da calcolare.

Il brief deve trasformare l'ambiguità in una **decisione esplicita sulla definizione**.

Una buona frase può essere:

> “Per questa analisi useremo churn contrattuale, definito come cancellazione dell'abbonamento. Il calo di utilizzo verrà trattato come possibile leading indicator, non come churn.”

Ora sappiamo che cosa misura la metrica e che cosa non misura.

### Un formato di riscrittura

Una struttura utile è:

> **Dobbiamo capire [fenomeno] per supportare [decisione], osservando [popolazione] nel periodo [tempo], misurando [outcome] e confrontando [baseline/alternative].**

Per esempio:

> “Dobbiamo capire che cosa sta comprimendo il margine e-commerce per decidere se intervenire su pricing, promozioni o logistica, osservando gli ordini completati degli ultimi dodici mesi e confrontando margine e driver con lo stesso periodo dell'anno precedente.”

Non è ancora il brief completo, ma è già abbastanza precisa da impedire che l'analisi parta da “facciamo qualche grafico sul margine”.

### Le ambiguità che vanno risolte subito

Davanti a una richiesta vaga, le domande iniziali dovrebbero chiarire almeno:

1. Che cosa è cambiato o potrebbe cambiare?
2. Perché conta per il business?
3. Quale decisione potrebbe essere influenzata?
4. Quale fenomeno dobbiamo definire operativamente?
5. Qual è la popolazione rilevante?
6. Quale confronto rende il fenomeno interpretabile?
7. Entro quando serve la decisione?
8. Quale errore sarebbe più costoso?

Le domande più dettagliate verranno distribuite nelle sezioni successive del brief.

> **La richiesta descrive il sintomo. Il problema analitico definisce quale evidenza può renderlo comprensibile e azionabile.**
