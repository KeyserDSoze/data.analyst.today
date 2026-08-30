## 8.7 Randomizzazione e natural experiment: costruire confronti credibili

Quando possiamo randomizzare, assegniamo il trattamento in modo indipendente dalle caratteristiche dei soggetti. In media, questo rende i gruppi comparabili anche rispetto a molte variabili che non osserviamo direttamente.

### Caso - Nuovo onboarding per una piattaforma B2B

Una piattaforma B2B vuole capire se un nuovo onboarding guidato aumenta l'activation entro 14 giorni.

Invece di distribuirlo subito a tutti, assegna casualmente il 50% dei nuovi account alla nuova esperienza e il 50% alla precedente.

Dopo sei settimane:

| Gruppo | Account | Activation 14 gg | Retention 60 gg |
|---|---:|---:|---:|
| Controllo | 4.812 | 42,6% | 31,8% |
| Nuovo onboarding | 4.776 | 47,9% | 35,1% |

La randomizzazione non garantisce che ogni metrica sia identica nei gruppi, ma rende plausibile attribuire le differenze sistematiche all'intervento, entro l'incertezza statistica e se l'esperimento è stato eseguito correttamente.

### Randomizzare non basta se l'esperimento è progettato male

Problemi frequenti:

- utenti che passano da un gruppo all'altro;
- esposizione incompleta;
- metriche cambiate durante il test;
- peeking continuo e stop opportunistico;
- interferenza tra unità;
- trattamento diverso da quello dichiarato;
- sample ratio mismatch;
- esclusioni post-randomizzazione.

La causalità non viene "attivata" da una colonna `experiment_group`. Serve coerenza tra assegnazione, esposizione, misura e analisi.

### Caso - Promozione nei punti vendita

Una catena retail non può randomizzare a livello cliente perché la promozione è visibile in negozio. Randomizza allora 40 punti vendita su 80, bilanciando macro-area e dimensione.

Questo cambia l'unità di randomizzazione: il negozio, non il singolo cliente.

Se analizziamo ogni transazione come osservazione indipendente, sottostimiamo l'incertezza perché clienti dello stesso negozio condividono lo stesso trattamento e molte condizioni locali.

Il design dell'esperimento determina anche il modo corretto di analizzare i dati.

### Quando non possiamo randomizzare

Molte decisioni business non possono essere assegnate casualmente:

- un nuovo prezzo viene introdotto per legge in una sola regione;
- una policy entra in vigore in una certa data;
- un fornitore cambia condizioni soltanto per alcuni magazzini;
- una funzionalità è rilasciata gradualmente per vincoli tecnici;
- un'interruzione di servizio colpisce alcuni utenti e non altri.

A volte questi eventi generano variazioni esterne che assomigliano a un esperimento. Parliamo in senso ampio di **natural experiment** quando il meccanismo di assegnazione crea gruppi comparabili in modo plausibilmente indipendente dalle loro scelte rispetto all'outcome studiato.

### Caso - Commissione di consegna introdotta per vincolo normativo

Un marketplace opera in due regioni simili. In una delle due una nuova normativa obbliga ad aggiungere una commissione minima sulle consegne; nell'altra no.

La commissione non è stata assegnata casualmente dal marketplace. Tuttavia l'evento normativo può offrire un'opportunità quasi-sperimentale per studiare l'effetto su frequenza d'ordine, basket e churn, se le regioni avevano dinamiche comparabili e se non si verificano altri shock differenziali importanti nello stesso periodo.

Il punto non è chiamare "esperimento naturale" qualsiasi cambiamento esterno. Il punto è capire **perché l'assegnazione del trattamento potrebbe essere considerata credibilmente esogena rispetto all'outcome**.

> **Il valore di un design causale sta nel meccanismo che rende il confronto credibile, non nel nome della tecnica.**

## Riferimenti

- World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitoli su causal inference e randomized assignment.
- Stanford University, *Potential Outcomes Model*.
