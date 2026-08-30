## 8.3 Confondenti: la terza variabile che cambia la storia

Un confondente è una variabile associata sia all'esposizione o trattamento sia all'outcome e può creare o distorcere una relazione osservata.

### Caso - La campagna display che sembrava generare vendite

Un e-commerce investe 1,2 milioni di euro in campagne display. L'analista confronta gli utenti esposti con quelli non esposti:

| Gruppo | Conversion rate |
|---|---:|
| Esposti alla campagna | 5,8% |
| Non esposti | 2,1% |

La differenza sembra enorme.

Ma la piattaforma pubblicitaria mostra più annunci proprio agli utenti che visitano spesso siti della categoria e che hanno già mostrato interesse per quei prodotti.

La **propensione all'acquisto preesistente** influenza sia la probabilità di essere esposti sia la probabilità di convertire.

Uno schema plausibile è:

`intento d'acquisto -> esposizione advertising`

`intento d'acquisto -> conversione`

L'esposizione può comunque avere un effetto causale. Il confronto grezzo, però, non lo identifica.

### "Controllare per tutto" non è una strategia

Una reazione comune è inserire tutte le colonne disponibili in una regressione e considerare il problema risolto.

Non funziona così.

Aggiustare per una variabile è corretto solo se comprendiamo il suo ruolo causale. Alcune variabili vanno controllate, altre no; alcune sono conseguenze del trattamento e aggiustarle può eliminare una parte dell'effetto che vogliamo misurare.

### Caso - Prezzo, domanda e meteo

Una catena di gelaterie trova una correlazione positiva tra prezzo medio e numero di gelati venduti.

Sembra assurdo: prezzi più alti generano più domanda?

L'analista segmenta per temperatura.

Nei giorni molto caldi:

- aumenta la domanda;
- alcuni punti vendita applicano prezzi dinamici leggermente superiori.

La temperatura influenza sia prezzo sia vendite e crea una correlazione aggregata positiva.

Una volta confrontati giorni con condizioni meteo simili, la relazione tra prezzo e quantità torna negativa.

### Confondenti osservabili e non osservabili

Alcuni confondenti sono facili da misurare:

- età;
- area geografica;
- storico acquisti;
- dimensione aziendale;
- giorno della settimana.

Altri sono difficili o impossibili da osservare direttamente:

- motivazione;
- qualità del management;
- reale intenzione di acquisto;
- propensione al rischio;
- urgenza del bisogno.

Questo è uno dei motivi per cui la randomizzazione è così importante: non richiede di conoscere e misurare ogni possibile confondente per ottenere gruppi comparabili in media.

### Checklist operativa sul confounding

Prima di interpretare causalmente un confronto osservazionale chiediamo:

- perché alcune unità ricevono il trattamento e altre no?
- quali caratteristiche influenzano questa selezione?
- quelle caratteristiche influenzano anche l'outcome?
- erano presenti prima del trattamento?
- sono misurate in modo affidabile?
- esistono confondenti non osservati plausibili?

> **Il confounding nasce dal processo che ha generato i gruppi, non dalla formula usata per analizzarli.**
