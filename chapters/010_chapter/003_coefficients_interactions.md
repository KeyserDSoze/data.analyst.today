## 10.3 Coefficienti, categorie e interazioni: leggere il modello senza raccontarsi favole

La regressione sembra semplice perché produce coefficienti leggibili. Proprio per questo è facile attribuire loro più significato di quanto abbiano davvero.

Un coefficiente risponde a una domanda del tipo:

> a parità delle altre variabili incluse nel modello, come cambia il target quando questa feature aumenta di un'unità?

Questa frase contiene tre avvertenze:

- “a parità” vale solo per le variabili incluse;
- l'unità di misura conta;
- la relazione può non essere davvero lineare.

### Caso realistico: BluePeak SaaS e l'espansione dei contratti

BluePeak vende software B2B. Il team Revenue Operations costruisce un modello per stimare l'espansione annuale del contratto.

Feature:

- utenti attivi mensili;
- numero di integrazioni configurate;
- ticket di supporto;
- numero di business unit;
- piano Enterprise sì/no;
- utilizzo della funzione di automazione.

Il primo modello mostra un coefficiente positivo molto forte per `ticket_support`.

Interpretazione ingenua:

> più ticket generano più espansione.

L'indagine mostra invece che i clienti grandi generano più ticket **e** hanno maggiore probabilità di espandere. La dimensione organizzativa non era rappresentata bene nel modello iniziale.

Dopo aver aggiunto dimensione account, numero di business unit e complessità di implementazione, il coefficiente dei ticket si riduce drasticamente.

La lezione non è che la regressione sia “inaffidabile”. La lezione è che un modello riflette la struttura informativa che gli forniamo.

### Variabili categoriche

Una categoria come `piano = Enterprise / Pro / Basic` non può essere interpretata come un numero arbitrario 1, 2, 3.

Di solito si usano indicatori binari e una categoria di riferimento.

Esempio:

- Basic = riferimento;
- Pro = 1 se Pro, 0 altrimenti;
- Enterprise = 1 se Enterprise, 0 altrimenti.

Il coefficiente di `Enterprise` rappresenta quindi la differenza attesa rispetto a Basic, a parità delle altre feature incluse.

### Interazioni: quando l'effetto dipende da un'altra variabile

Supponiamo che un aumento di utilizzo del prodotto sia associato a maggiore espansione, ma solo per clienti con almeno tre integrazioni attive.

Un modello puramente additivo può perdere questo pattern.

Possiamo introdurre un termine di interazione:

\[
y = \beta_0 + \beta_1 usage + \beta_2 integrations + \beta_3(usage \times integrations)
\]

Nel caso BluePeak, l'analisi mostra che l'uso della funzione di automazione è molto più informativo per account con processi complessi.

Questa scoperta non serve solo alla previsione. Suggerisce anche un segmento su cui il team Customer Success può concentrare onboarding e training.

### Non linearità

Molti fenomeni business non sono lineari.

Il primo ticket di supporto può essere normale. Il ventesimo in una settimana può essere un segnale completamente diverso.

Il primo sconto può aumentare conversione. Ulteriori sconti possono erodere margine senza migliorare molto la probabilità di acquisto.

Una relazione può richiedere:

- trasformazioni logaritmiche;
- termini quadratici;
- spline;
- segmentazione;
- modelli non lineari.

Ma prima di aumentare la complessità bisogna capire se il pattern è reale o nasce da problemi di dati.

### Errore tipico

> “Il coefficiente è positivo, quindi questa variabile è buona.”

Un coefficiente non è un giudizio di valore. È una relazione stimata sotto un insieme di condizioni.

### Regola pratica

Quando presenti coefficienti a stakeholder, evita frasi causali se il disegno dello studio non le giustifica.

Preferisci:

> “Nel dataset osservato, a parità delle variabili incluse, gli account con questa caratteristica mostrano in media…”

anziché:

> “Questa caratteristica causa…”
