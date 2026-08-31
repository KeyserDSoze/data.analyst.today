## 1.10 Correlazione, causalità e spiegazioni plausibili

Uno dei compiti più delicati dell'analista è distinguere tra livelli diversi di affermazione.

Possiamo osservare che due fenomeni si muovono insieme. Possiamo stimare un'associazione statistica. Possiamo, in condizioni più forti, sostenere che intervenire su uno dei due modificherebbe l'altro.

Queste affermazioni non sono equivalenti.

### Un pattern non è ancora un intervento

Supponiamo di osservare che i clienti che utilizzano frequentemente una funzione dell'app hanno retention più alta.

Una conclusione superficiale sarebbe:

> “Se spingiamo più utenti a usare quella funzione, aumenteremo la retention.”

Ma il pattern è compatibile anche con altre spiegazioni:

- gli utenti già più coinvolti usano di più la funzione e rimangono più a lungo;
- la funzione è disponibile soprattutto a clienti premium;
- l'anzianità del cliente influenza sia uso sia retention;
- utenti prossimi all'abbandono riducono l'uso di molte funzioni contemporaneamente.

La relazione osservata può essere reale mentre la spiegazione causale è sbagliata.

### Confondenti e selezione

Un **confondente** è una variabile che influenza sia l'esposizione che ci interessa sia l'outcome.

Scopriamo, per esempio, che i clienti chiamati più spesso dal team commerciale acquistano di più.

Aumentare il numero di chiamate farà aumentare le vendite?

Forse. Ma il team potrebbe chiamare più spesso proprio i clienti che considera più promettenti. Il potenziale del cliente influenza allora sia il trattamento sia l'esito.

La selezione può comparire anche in modi meno visibili.

Se analizziamo soltanto utenti ancora attivi per capire quali funzionalità “creano retention”, abbiamo escluso proprio chi ha abbandonato. Se studiamo soltanto campagne di successo, non sappiamo se le stesse caratteristiche fossero presenti nelle campagne fallite.

Il dataset osservato non coincide automaticamente con la popolazione necessaria per rispondere alla domanda.

### Temporalità e causalità inversa

Una causa deve precedere il proprio effetto.

Sembra banale, ma le aggregazioni possono nascondere la sequenza.

Se i clienti che aprono molti ticket hanno churn elevato, il supporto provoca l'abbandono? Oppure problemi già presenti generano sia ticket sia churn?

Analogamente, aziende con più Data Analyst possono usare più dati perché gli analisti migliorano i processi decisionali. Oppure aziende già data-driven assumono più analisti.

La direzione della relazione è parte del problema.

### Come otteniamo evidenza più forte?

Quando possibile, la randomizzazione è uno strumento molto potente perché costruisce gruppi comparabili prima del trattamento.

Ma un A/B test non è automaticamente valido: randomizzazione, exposure, campione, durata, interferenze, metriche e modalità di analisi possono fallire. Il **Capitolo 9** sarà dedicato proprio alla sperimentazione nel mondo reale.

Quando non possiamo randomizzare, possiamo usare disegni osservazionali o quasi-sperimentali. Il **Capitolo 8** entrerà in matching, regression discontinuity, variabili strumentali e altri approcci, insieme alle assunzioni che li rendono credibili o fragili.

Per ora basta un principio:

> **un modello più sofisticato non trasforma automaticamente un'associazione in causalità.**

### La disciplina delle spiegazioni alternative

Davanti a un pattern interessante è utile chiedersi:

> **“Quale altra storia potrebbe produrre questi stessi dati?”**

Se il fatturato cresce dopo una campagna marketing, dovremmo chiederci almeno se nello stesso periodo:

- è iniziata una promozione;
- è cambiata la stagionalità;
- sono aumentati i prezzi;
- è cambiato il tracking;
- sono entrati nuovi mercati;
- il periodo di confronto era anomalo.

L'obiettivo non è diventare paralizzati dal dubbio. È capire quali spiegazioni l'evidenza ha davvero eliminato.

### Il linguaggio deve seguire il metodo

Un'analisi osservazionale può sostenere:

> “Gli utenti che utilizzano la funzione X mostrano retention maggiore, anche dopo aver controllato alcune caratteristiche osservabili.”

È molto diverso da:

> “La funzione X aumenta la retention.”

La seconda frase contiene una promessa controfattuale: se cambiassimo X, cambierebbe Y.

Questa promessa richiede un disegno adeguato.

### Checklist minima davanti a una relazione

1. Il pattern è stabile o può essere rumore?
2. È coerente tra segmenti e periodi?
3. Esistono confondenti plausibili?
4. L'ordine temporale è coerente?
5. Potrebbe esserci causalità inversa?
6. La selezione del campione introduce bias?
7. Quale osservazione o esperimento distinguerebbe le spiegazioni concorrenti?

I sistemi generativi sono molto bravi a proporre storie plausibili attorno a un pattern.

Il compito dell'analista non è scegliere la storia più fluida.

È capire quale storia merita più fiducia.
