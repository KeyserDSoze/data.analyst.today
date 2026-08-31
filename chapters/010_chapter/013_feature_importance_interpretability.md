## 10.13 Feature importance e interpretabilità: capire cosa usa il modello senza inventare causalità

Quando un modello produce buone previsioni, la domanda successiva arriva quasi sempre:

> quali variabili contano di più?

È una domanda legittima, ma pericolosa se viene interpretata male.

### Feature importance non significa causa

Se una variabile è molto importante per il modello, significa che contribuisce alla sua capacità predittiva.

Non significa automaticamente che modificare quella variabile cambierà il risultato.

Un esempio semplice: nei modelli di churn, il numero di chiamate al supporto può essere altamente predittivo.

Ma ridurre artificialmente il numero di chiamate non elimina necessariamente il problema del cliente. Potrebbe soltanto nascondere il segnale.

### Caso simulato: NovaBank e la variabile “numero di contatti”

NovaBank costruisce un modello per prevedere quali clienti chiuderanno il conto nei prossimi 60 giorni.

Le feature più importanti risultano:

1. numero di contatti al call center;
2. riduzione del saldo medio;
3. numero di login nell'app;
4. reclami aperti;
5. anzianità cliente.

Il responsabile operations propone:

> “Se i contatti al call center aumentano il churn, riduciamo il numero di contatti.”

Il ragionamento confonde previsione e causalità.

I contatti potrebbero essere semplicemente un sintomo di problemi già esistenti.

### Permutation importance

Una tecnica utile consiste nel misurare quanto peggiora la performance del modello quando i valori di una feature vengono rimescolati.

Se permutare una variabile distrugge una parte importante della performance, il modello dipende molto da quella feature.

La documentazione ufficiale di scikit-learn sottolinea però due punti fondamentali:

- l'importanza è relativa a **quel modello** e a **quella metrica**;
- è preferibile calcolarla su dati held-out se vogliamo capire quali feature contribuiscono alla generalizzazione.

Fonte: https://scikit-learn.org/stable/modules/permutation_importance.html

### Caso pubblico documentato: feature casuali nel Titanic esteso

Nella documentazione scikit-learn sulla permutation importance viene mostrato un esempio con un dataset Titanic arricchito da feature casuali. L'esempio evidenzia anche un limite delle impurity-based importances degli alberi: feature ad alta cardinalità possono apparire artificialmente importanti, mentre la permutation importance su dati held-out è più utile per capire il contributo alla performance fuori dal training set.

Questo è un ottimo esempio di un principio generale:

> una feature può sembrare importante perché il modello l'ha usata per adattarsi al training set, non perché sia davvero informativa nel mondo reale.

### Feature correlate

Quando due variabili contengono informazione simile, l'importanza può distribuirsi in modo instabile.

Per esempio:

- spesa ultimi 30 giorni;
- spesa ultimi 28 giorni;
- numero ordini ultimi 30 giorni;
- valore medio ordine.

Se sono molto correlate, rimuovere o permutare una può lasciare alle altre abbastanza informazione da compensare.

Quindi una bassa importance individuale non implica necessariamente inutilità concettuale.

### Interpretabilità locale e globale

È utile distinguere:

- **interpretabilità globale**: quali pattern usa mediamente il modello;
- **interpretabilità locale**: perché un singolo caso ha ricevuto un certo punteggio.

In ambito credito, frodi o customer service, questa distinzione è importante perché la domanda può essere diversa:

- “Quali variabili guidano il modello in generale?”
- “Perché questo cliente specifico ha ricevuto score 0,87?”

### Metodo operativo

Quando presenti feature importance:

1. specifica quale tecnica hai usato;
2. indica su quale dataset è stata calcolata;
3. ricorda che è model-dependent;
4. controlla feature correlate;
5. non trasformare importanza predittiva in causalità;
6. collega sempre l'interpretazione a una domanda business concreta.

La frase corretta è:

> “Il modello usa molto questa informazione per prevedere.”

Non:

> “Questa variabile causa il risultato.”