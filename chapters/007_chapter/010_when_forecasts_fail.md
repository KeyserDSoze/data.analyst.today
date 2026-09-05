## 7.9 Quando il forecast smette di meritare fiducia: regime change, drift e model failure

Ogni forecast quantitativo trasferisce qualcosa dal passato al futuro. Hyndman e Athanasopoulos rendono esplicita la condizione: i metodi quantitativi hanno senso quando esistono dati storici rilevanti e quando possiamo ragionevolmente assumere che **alcuni aspetti dei pattern passati continuino nel futuro**.[^fpp-data]

Questa continuità può rompersi in modi diversi. Può cambiare la distribuzione degli input (**data drift**), può cambiare la relazione tra segnali e target (**relationship/concept drift**), oppure può cambiare direttamente il processo economico — prezzo, prodotto, contratto, capacità, regolamentazione, canale o comportamento — cioè il **business regime**. Nel lavoro dell'analista quest'ultimo punto è cruciale perché spesso il business sa che il mondo è cambiato prima che un test automatico riesca a mostrarlo.

### Caso reale documentato — Google Flu Trends e l'errore che aveva struttura

**Google Flu Trends (GFT)** rimane uno dei casi più istruttivi sul rischio di trattare una relazione storica come stabile per definizione. Il sistema utilizzava query di ricerca per stimare l'andamento dell'influenza in anticipo rispetto alle statistiche tradizionali di sorveglianza sanitaria.

Nel 2014 David Lazer, Ryan Kennedy, Gary King e Alessandro Vespignani pubblicarono su *Science* “The Parable of Google Flu: Traps in Big Data Analysis”.[^gft-science] Nella finestra dal **21 agosto 2011 al 1 settembre 2013**, GFT sovrastimò le stime CDC in **100 settimane su 108**. Nella stagione 2011–2012 arrivò a sovrastimare il livello reale di oltre il 50%, e il problema divenne particolarmente evidente nella stagione 2012–2013.[^gft-paper]

Il punto più interessante non è che un modello abbia sbagliato. È che **gli errori stessi mostravano autocorrelazione e stagionalità**.[^gft-followup] Non stavamo osservando soltanto rumore imprevedibile: il sistema sbagliava secondo una struttura.

Questo avrebbe dovuto far riaprire l'argomento molto prima. Se l'errore conserva memoria, stagionalità o bias persistente, il modello sta lasciando informazione sistematica fuori dalla previsione oppure sta lavorando in condizioni che non corrispondono più a quelle del training.

### Una baseline più semplice può contenere informazione che il modello ignora

Lazer e colleghi confrontarono GFT con modelli che incorporavano dati CDC ritardati e stagionalità annuale. Un modello basato su CDC laggato ottenne errore medio assoluto fuori campione inferiore a GFT; una combinazione di GFT e CDC fece ancora meglio.[^gft-paper]

La lezione non è che i segnali digitali siano inutili. È che un nuovo segnale non ottiene automaticamente il diritto di sostituire una baseline storica solida. Deve dimostrare, fuori campione, di aggiungere informazione.

Il caso mostra anche un secondo rischio: la piattaforma che genera le feature può cambiare. Lazer e colleghi discussero il ruolo delle modifiche all'algoritmo di ricerca di Google.[^gft-followup] Query, click, impression, ranking, recommendation ed engagement social non sono “sensori naturali”: sono prodotti di sistemi che vengono continuamente modificati. Può quindi degradare la relazione con il target anche se il fenomeno esterno non è cambiato nello stesso modo.

### Quando il business sa qualcosa che la serie non può sapere

Consideriamo una società industriale che prevede la domanda mensile di componenti per tre grandi clienti automotive. Storicamente il forecast ha MAE sotto il **6%**. A gennaio uno dei clienti firma un accordo che sposterà il **35%** degli ordini futuri verso un concorrente. Il commerciale lo sa subito; la serie storica no.

Il modello continua a prevedere **48.000 pezzi** per marzo. Gli ordini reali sono **34.500**. Non è un bug matematico: il processo economico è cambiato attraverso un'informazione esterna che il modello non possedeva.

Aspettare mesi affinché l'algoritmo “impari” il nuovo regime significa scegliere consapevolmente di pagare errori evitabili. In casi del genere serve un override o uno scenario informato, documentato e valutato ex post.

Pricing radicalmente diverso, redesign, acquisizioni, ingresso o uscita da mercati, nuova regolamentazione, grandi contratti, cambi di capacità, migrazioni di tracking o promozioni senza precedenti non implicano automaticamente che il modello debba essere scartato. Implicano però che dobbiamo riaprire la domanda: **la storia di training rappresenta ancora lo stesso problema?**

### Monitoring: osservare l'errore come una serie

Un forecast in produzione non va monitorato soltanto con un KPI medio. Dobbiamo seguire errore, bias, coverage degli intervalli, performance per horizon e segmento, confronto con la baseline, distribuzione degli input e struttura temporale degli errori. Il caso GFT mostra perché quest'ultimo punto è potente: se il modello sbaglia sempre dalla stessa parte o secondo un calendario, non stiamo più guardando casualità pura.

La baseline deve rimanere un challenger permanente. Se per più finestre il seasonal naïve torna a battere il modello complesso in un segmento materiale, qualcosa è cambiato oppure la complessità non aggiunge più valore.

Ogni forecast importante dovrebbe anche dichiarare le proprie **conditions of validity**, per esempio: “listino stabile, capacità invariata, nessuna campagna eccezionale fuori calendario e continuità della relazione storica tra meteo e domanda”. Non è una clausola difensiva; è parte dell'argomento che rende credibile il forecast.

### Override umano: informazione nuova, non intuizione incontrollata

Un override è rigoroso quando porta un'informazione che il modello non poteva conoscere, il meccanismo è comprensibile, l'impatto atteso viene documentato e la modifica viene valutata dopo il fatto. Non lo è quando un manager cambia il numero perché “sembra troppo basso”.

Per questo conviene conservare separatamente forecast statistico e forecast finale dopo override, insieme alla motivazione. Nel tempo possiamo verificare se gli interventi umani riducono davvero accuracy error o business loss.

Nel Temporal Decision Brief questa parte rimane operativa:

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

Il caso finale del capitolo mostrerà questa idea nella forma più concreta: un modello che migliora l'accuracy media e peggiora contemporaneamente la decisione di inventory.

[^fpp-data]: Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd ed., “Forecasting data and methods”, https://otexts.com/fpp3/data-methods.html
[^gft-science]: Lazer, D., Kennedy, R., King, G. & Vespignani, A., “The Parable of Google Flu: Traps in Big Data Analysis”, *Science*, 343(6176), 2014, DOI 10.1126/science.1248506, PubMed: https://pubmed.ncbi.nlm.nih.gov/24626916/
[^gft-paper]: Lazer et al., manuscript copy of the *Science* article, Harvard DASH, https://dash.harvard.edu/bitstreams/7312037d-0e0d-6bd4-e053-0100007fdf3b/download
[^gft-followup]: Lazer, Kennedy, King & Vespignani, “Google Flu Trends Still Appears Sick: An Evaluation of the 2013–2014 Flu Season”, Harvard University, https://gking.harvard.edu/publication/google-flu-trends-still-appears-sick-an-evaluation-of-the-20132014-flu-season/
