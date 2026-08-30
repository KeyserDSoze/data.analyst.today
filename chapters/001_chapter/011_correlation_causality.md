## 1.10 Correlazione, causalità e spiegazioni plausibili

Uno dei compiti più delicati dell'analista è distinguere tra tre livelli diversi di affermazione:

1. **descrizione** — due fenomeni si muovono insieme;
2. **associazione** — esiste una relazione statistica tra i fenomeni;
3. **causalità** — modificare un fenomeno produce un cambiamento nell'altro.

Confondere questi livelli è una delle fonti più comuni di conclusioni sbagliate.

### Correlazione non significa causalità

Supponiamo di osservare che i clienti che usano frequentemente una funzione dell'app hanno una retention più alta.

Una conclusione superficiale potrebbe essere:

> Se costringiamo più utenti a usare quella funzione, aumenteremo la retention.

Ma altre spiegazioni sono possibili.

Forse gli utenti già più interessati al prodotto usano maggiormente la funzione e rimangono più a lungo per ragioni indipendenti.

Forse la funzione è disponibile soltanto agli utenti premium, che hanno già caratteristiche differenti.

Forse entrambi i fenomeni dipendono da una terza variabile, come l'anzianità del cliente.

La correlazione osservata è reale. La spiegazione causale potrebbe essere sbagliata.

### Il ruolo delle variabili confondenti

Una variabile confondente influenza sia la presunta causa sia il risultato osservato.

Consideriamo un esempio semplice.

Scopriamo che i clienti che ricevono più chiamate dal team commerciale acquistano di più.

Possiamo concludere che aumentare il numero di chiamate farà aumentare le vendite?

Non necessariamente.

Il team commerciale potrebbe chiamare più frequentemente proprio i clienti che considera più promettenti. Il potenziale del cliente influenza quindi sia il numero di chiamate sia la probabilità di acquisto.

Se non teniamo conto di questo meccanismo, attribuiamo alla chiamata un effetto che potrebbe derivare almeno in parte dalla selezione dei clienti.

### Selezione e survivorship bias

Molte analisi osservano soltanto gli elementi che sono sopravvissuti a un processo.

Se analizziamo esclusivamente gli utenti ancora attivi per capire quali funzionalità usano di più, perdiamo informazioni fondamentali sugli utenti che hanno abbandonato il prodotto.

Se studiamo soltanto campagne marketing di successo, potremmo identificare caratteristiche presenti anche in numerose campagne fallite.

Il dataset osservabile non coincide sempre con la popolazione che ci interessa.

### Temporalità

Per sostenere una spiegazione causale, la causa deve precedere l'effetto.

Sembra ovvio, ma nelle analisi aggregate può essere facile perdere l'ordine temporale.

Supponiamo di trovare una relazione tra numero di ticket di assistenza e churn.

Le richieste di assistenza causano l'abbandono?

Oppure i clienti che stanno già vivendo problemi che li porteranno ad abbandonare aprono più ticket?

Oppure entrambe le cose?

La sequenza temporale degli eventi è parte dell'analisi.

### Reverse causality

Un altro problema frequente è la causalità inversa.

Osserviamo che le aziende con più Data Analyst utilizzano più dati nelle decisioni.

È possibile che assumere analisti renda l'azienda più data-driven.

Ma è anche possibile che aziende già più orientate ai dati decidano di assumere più analisti.

Una semplice correlazione cross-sectional non permette di distinguere facilmente le due direzioni.

### Esperimenti e A/B test

Quando possibile, gli esperimenti controllati sono uno degli strumenti più potenti per stimare effetti causali.

In un A/B test gli individui vengono assegnati casualmente a condizioni differenti. La randomizzazione, se implementata correttamente e con un campione adeguato, tende a rendere comparabili i gruppi sulle caratteristiche osservate e non osservate.

Questo non significa che ogni A/B test sia automaticamente valido.

Dobbiamo comunque verificare:

- qualità della randomizzazione;
- dimensione campionaria;
- durata dell'esperimento;
- interferenze tra gruppi;
- metriche primarie e secondarie;
- multiple testing;
- utenti esposti realmente al trattamento;
- effetti di novità;
- stagionalità;
- significatività pratica oltre a quella statistica.

Approfondiremo questi aspetti nei capitoli dedicati alla sperimentazione.

### Quando non possiamo sperimentare

Molti problemi reali non permettono un esperimento.

Non possiamo assegnare casualmente una recessione economica a metà dei nostri clienti. Non possiamo sempre modificare prezzi, territori, politiche commerciali o caratteristiche sensibili in modo sperimentale.

In questi casi esistono metodi osservazionali e quasi-sperimentali, come:

- regression adjustment;
- matching;
- propensity score;
- difference-in-differences;
- regression discontinuity;
- instrumental variables;
- synthetic control;
- interrupted time series.

Questi strumenti richiedono assunzioni specifiche. Il punto importante, per ora, è che **la causalità non emerge semplicemente perché un modello statistico è sofisticato**.

### La disciplina delle spiegazioni alternative

Un'abitudine potente consiste nel chiedersi, davanti a ogni risultato interessante:

> Quali altre spiegazioni potrebbero produrre lo stesso pattern nei dati?

Se il fatturato cresce dopo una campagna marketing:

- la campagna ha causato la crescita?
- nello stesso periodo è iniziata una promozione?
- è cambiata la stagionalità?
- sono aumentati i prezzi?
- è cambiato il tracciamento?
- sono entrati nuovi mercati?
- il confronto utilizza un periodo anomalo?

L'obiettivo non è diventare paralizzati dal dubbio. È capire quanto forte sia realmente l'evidenza.

### Un linguaggio proporzionato all'evidenza

La comunicazione dovrebbe riflettere il metodo utilizzato.

Se abbiamo un'analisi osservazionale, possiamo scrivere:

> Gli utenti che utilizzano la funzione X mostrano una retention maggiore, anche dopo aver controllato alcune caratteristiche osservabili.

È diverso da:

> L'utilizzo della funzione X aumenta la retention.

La seconda frase implica una conclusione causale molto più forte.

Un Data Analyst competente non cerca di rendere le conclusioni più certe di quanto siano. Cerca di renderle **proporzionate all'evidenza disponibile**.

### Una regola pratica

Quando osserviamo una relazione, dovremmo chiederci almeno:

1. la relazione è reale o può essere rumore?
2. è stabile tra segmenti e periodi?
3. esiste una variabile confondente plausibile?
4. l'ordine temporale è coerente?
5. potrebbe esserci causalità inversa?
6. il modo in cui i dati sono stati selezionati introduce bias?
7. quale esperimento o analisi aggiuntiva distinguerebbe tra le spiegazioni concorrenti?

Questa disciplina diventa ancora più importante con sistemi AI capaci di generare rapidamente spiegazioni plausibili.

Un modello linguistico è molto bravo a inventare una storia coerente attorno a un pattern. Il lavoro dell'analista consiste nel chiedere se quella storia sia supportata dai dati e dal disegno dell'analisi.
