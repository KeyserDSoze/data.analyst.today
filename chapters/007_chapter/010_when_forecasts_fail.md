## 7.9 Quando il forecast smette di meritare fiducia: regime change, drift e model failure

Ogni forecast quantitativo trasferisce qualcosa dal passato al futuro.

Hyndman e Athanasopoulos formulano la condizione in modo molto chiaro: i metodi quantitativi hanno senso quando abbiamo dati storici e quando è ragionevole supporre che **alcuni aspetti dei pattern passati continuino nel futuro**.[^fpp-data]

Quando questa continuità si rompe, il modello può continuare a produrre numeri estremamente precisi dal punto di vista formale e diventare, nello stesso momento, meno credibile dal punto di vista operativo.

### Tre cose possono cambiare

È utile distinguere:

**Data drift** — cambia la distribuzione degli input.

**Relationship / concept drift** — cambia la relazione tra segnali e target.

**Business regime change** — cambia il processo reale: prezzo, prodotto, contratto, capacità, comportamento, regolazione, canale.

Nel lavoro dell'analista il terzo tipo è cruciale, perché spesso viene conosciuto prima attraverso il business che attraverso un test automatico.

### Caso reale documentato — Google Flu Trends e l'errore che aveva struttura

**Google Flu Trends (GFT)** è uno dei casi più istruttivi sul rischio di trattare una relazione storica come se fosse stabile per definizione.

Il sistema utilizzava query di ricerca per stimare l'andamento dell'influenza in anticipo rispetto alle tradizionali statistiche di sorveglianza sanitaria.

Nel 2014 David Lazer, Ryan Kennedy, Gary King e Alessandro Vespignani pubblicarono su *Science* “The Parable of Google Flu: Traps in Big Data Analysis”.[^gft-science]

L'analisi documentò un problema molto concreto: tra il **21 agosto 2011 e il 1 settembre 2013**, GFT sovrastimò la prevalenza dell'influenza in **100 settimane su 108**. Nel 2011–2012 arrivò a sovrastimare il livello reale di oltre il 50%, e nella stagione 2012–2013 il problema divenne particolarmente evidente.[^gft-paper]

Il punto più interessante per questo capitolo non è il singolo errore.

Gli autori trovarono **autocorrelazione e stagionalità negli errori di GFT**. L'errore stesso conteneva struttura temporale.[^gft-followup]

In altre parole, il modello non stava semplicemente incontrando rumore imprevedibile. Stava sbagliando in modo sistematico.

### Una baseline più semplice conteneva informazione che il modello ignorava

Nel paper gli autori confrontarono GFT con modelli che incorporavano dati CDC ritardati e stagionalità annuale. Il modello basato su CDC laggato ebbe un errore medio assoluto fuori campione inferiore a GFT; una combinazione tra GFT e dati CDC fece ancora meglio.[^gft-paper]

La lezione non è:

> i dati digitali sono inutili.

È quasi l'opposto:

> **un nuovo segnale può avere molto valore, ma non ottiene automaticamente il diritto di sostituire una baseline storica solida.**

Il caso mostra perché dobbiamo sempre chiedere:

- il modello batte davvero il benchmark tradizionale?
- gli errori sono casuali o mostrano struttura?
- il processo che genera le feature è stabile?
- il sistema viene continuamente rivalutato fuori campione?

### Il dato stesso può cambiare perché cambia la piattaforma

Lazer e colleghi discussero anche il ruolo delle modifiche all'algoritmo di ricerca di Google: una piattaforma digitale non è un sensore passivo della realtà; modifica continuamente l'esperienza che genera i dati.[^gft-followup]

Questo principio è estremamente moderno.

Pensiamo a feature basate su:

- query di ricerca;
- click;
- impression;
- ranking;
- recommendation;
- engagement social;
- attribution advertising.

Se cambia la piattaforma che produce quei segnali, può cambiare la relazione con il fenomeno target anche se il mondo esterno è rimasto simile.

Un modello può degradare perché è cambiato il **misuratore**, non soltanto perché è cambiato il fenomeno.

### Caso simulato/composito — Il contratto che il modello non poteva conoscere

Una società industriale prevede la domanda mensile di componenti per tre grandi clienti automotive.

Storicamente il forecast ha MAE sotto il 6%.

A gennaio uno dei clienti firma un accordo che sposterà il 35% dei futuri ordini verso un concorrente. Il commerciale lo sa subito. La serie storica non può saperlo.

Il modello continua a prevedere 48.000 pezzi per marzo. Gli ordini reali sono 34.500.

Non è un “bug” matematico. Il processo economico è cambiato con informazione esterna che non era rappresentata nel modello.

La risposta corretta non è aspettare che il modello impari il nuovo regime dopo molti errori. È introdurre un **override o scenario informato**.

### Quali eventi devono farci riaprire il modello

Segnali di regime change:

- pricing radicalmente diverso;
- nuovo prodotto o redesign;
- fusione/acquisizione;
- ingresso o uscita da un mercato;
- nuova regolamentazione;
- cambi importanti di capacità;
- grandi contratti persi o acquisiti;
- competitor strutturale;
- pandemia o shock macro;
- migrazione di tracking;
- cambio della piattaforma che genera una feature;
- promozione senza precedenti storici.

Non tutti richiedono di buttare il modello. Tutti richiedono di chiedersi se il training history rappresenti ancora lo stesso problema.

### Monitoring: non aspettare che il KPI medio esploda

Dopo il deployment monitoriamo almeno:

- forecast error;
- bias;
- coverage degli intervalli;
- errore per horizon;
- errore per segmento;
- rapporto rispetto alla baseline;
- distribuzione degli input;
- struttura/autocorrelazione dei residui o forecast error;
- eventi di business che modificano le condizioni.

Il caso Google Flu Trends mostra perché la **struttura degli errori** è particolarmente informativa. Se il modello sbaglia sempre dalla stessa parte o secondo un pattern stagionale, non stiamo più osservando soltanto casualità.

### Champion vs baseline, sempre

Un modello in produzione non dovrebbe essere monitorato soltanto contro sé stesso.

Manteniamo una baseline semplice come challenger permanente.

Se per molte settimane il seasonal naïve torna a battere il modello complesso, è un segnale forte che qualcosa è cambiato o che la complessità non sta più aggiungendo valore.

### Conditions of validity

Ogni forecast importante dovrebbe dichiarare le proprie condizioni operative, per esempio:

> La previsione assume listino stabile, capacità invariata, nessuna campagna eccezionale non presente nel calendario e continuità della relazione storica tra meteo e domanda.

Non è una clausola per difendersi dagli errori. È parte del modello.

### Override umano: quando è disciplinato e quando è wishful thinking

Il business può conoscere informazioni che il modello non possiede.

Un override è giustificato quando:

- l'informazione era indisponibile al modello;
- il meccanismo è chiaro;
- l'impatto atteso può essere documentato;
- la modifica viene registrata e valutata ex post.

Un override non è giustificato soltanto perché “il manager sente che il numero è troppo basso”.

È utile mantenere due colonne:

- forecast statistico;
- forecast finale dopo override.

E misurare nel tempo se gli override migliorano davvero l'accuracy o la loss decisionale.

### Il campo del Temporal Decision Brief

```text
Segnali di drift/regime:
Baseline ancora valida?
Errori mostrano struttura?
Evento business noto:
Input/processo di misura cambiato:
Condition of validity violata:
Override necessario:
Motivazione override:
Data di revisione/retraining:
```

> **Un forecast non fallisce soltanto quando sbaglia un numero. Fallisce quando continua a essere usato dopo che sono cambiate le condizioni che rendevano informativo il suo passato.**

[^fpp-data]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Forecasting data and methods”, https://otexts.com/fpp3/data-methods.html
[^gft-science]: Lazer, D., Kennedy, R., King, G. & Vespignani, A., “The Parable of Google Flu: Traps in Big Data Analysis”, *Science*, 343(6176), 2014, DOI 10.1126/science.1248506, PubMed: https://pubmed.ncbi.nlm.nih.gov/24626916/
[^gft-paper]: Lazer et al., manuscript copy of the *Science* article, Harvard DASH, https://dash.harvard.edu/bitstreams/7312037d-0e0d-6bd4-e053-0100007fdf3b/download
[^gft-followup]: Lazer, Kennedy, King & Vespignani, “Google Flu Trends Still Appears Sick: An Evaluation of the 2013–2014 Flu Season”, Harvard University, https://gking.harvard.edu/publication/google-flu-trends-still-appears-sick-an-evaluation-of-the-20132014-flu-season/
