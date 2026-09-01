# Capitolo 10 — Regressione e modelli predittivi per Data Analyst

## 10.1 Prima del modello: definire prediction time, target e azione

Quando un'organizzazione dice di voler "fare machine learning", spesso sta saltando una domanda più importante:

> **quale informazione futura ci serve prima che accada qualcosa, e quale decisione cambierà quando la avremo?**

Prevedere non è un obiettivo autonomo. È un modo per anticipare una decisione.

Possiamo voler stimare:

- un valore numerico, come tempo di consegna o spesa attesa;
- una probabilità, come churn, default o frode;
- un ranking, come la lista dei casi da revisionare per primi;
- un rischio futuro da tradurre in una policy operativa.

Il modello è solo una componente di questa catena:

**decisione → prediction moment → dati disponibili → modello → score/probabilità → soglia o ranking → azione → outcome → monitoring**.

Se non sappiamo descrivere la catena, ottimizzare l'algoritmo è prematuro.

### Caso simulato/composito — Northstar Logistics

Northstar Logistics gestisce consegne B2B per clienti industriali. Il management chiede:

> "Possiamo prevedere quali spedizioni arriveranno in ritardo?"

La richiesta sembra chiara, ma contiene almeno quattro possibili problemi differenti:

1. prevedere le **ore di ritardo**;
2. prevedere la probabilità di superare **2 ore di ritardo**;
3. ordinare le spedizioni per rischio affinché il control tower analizzi le prime 200;
4. decidere quali spedizioni meritano un intervento costoso, come cambio corriere o capacità aggiuntiva.

Sono target e decisioni diverse.

Il dataset contiene:

- distanza;
- corriere;
- giorno della settimana;
- numero di colli;
- saturazione del deposito;
- meteo;
- ora prevista di partenza;
- eventi di tracking;
- ora effettiva di consegna.

Un primo modello usa anche `actual_delivery_time` e ottiene performance quasi perfetta.

Il problema è evidente: quell'informazione nasce **dopo** l'evento che vogliamo prevedere.

Il modello non sta anticipando il futuro. Lo sta leggendo.

### Le quattro definizioni obbligatorie

Prima di costruire un modello, fissiamo quattro elementi.

#### 1. Prediction unit

Che cosa riceve una previsione?

- cliente;
- ordine;
- spedizione;
- transazione;
- account;
- macchina;
- ticket.

La prediction unit non coincide necessariamente con una riga del dataset storico.

#### 2. Prediction time

In quale istante dobbiamo produrre lo score?

Esempio:

> ogni lunedì alle 06:00 per tutti i clienti attivi.

Questa definizione crea una frontiera informativa: una feature è utilizzabile solo se sarebbe stata conoscibile entro quell'istante.

#### 3. Prediction horizon e target

Che cosa deve accadere, e entro quando?

Non "churn", ma:

> **probabilità che un account attivo al prediction time cancelli volontariamente entro i successivi 60 giorni.**

Non "ritardo", ma:

> **minuti di ritardo rispetto alla promessa di consegna, misurati al completamento dell'ordine.**

Target e horizon devono essere abbastanza precisi da ricostruire la label storica senza ambiguità.

#### 4. Decision/action

Che cosa faremo con il risultato?

- prioritizzare 2.000 clienti per Customer Success;
- inviare 500 transazioni a review manuale;
- aumentare safety stock;
- cambiare routing;
- non fare nulla sotto una certa soglia economica.

Un risk score senza una policy è un output tecnico, non ancora un prodotto analitico.

### Prediction e causalità rimangono problemi diversi

Un modello di churn può scoprire che molti ticket, pagamenti falliti e riduzione dei login sono ottimi segnali di rischio.

Questo può essere perfetto per il ranking.

Non significa che:

- impedire di aprire ticket;
- nascondere i pagamenti falliti;
- forzare login artificiali

ridurrebbe il churn.

Il Capitolo 8 ha affrontato la domanda causale:

> quale intervento cambia l'outcome rispetto al controfattuale?

Qui la domanda è:

> **quali casi futuri possiamo anticipare abbastanza bene da supportare una decisione?**

Un modello predittivo e un modello causale possono lavorare insieme, ma non sono intercambiabili.

### La baseline viene prima della complessità

Prima di cercare il modello migliore serve un riferimento semplice.

Per un target continuo può essere:

- media;
- mediana;
- regola operativa esistente;
- regressione lineare semplice.

Per una classificazione può essere:

- prevalenza/base rate;
- regola euristica già usata;
- regressione logistica.

Google raccomanda esplicitamente, nelle proprie linee guida di ML engineering, di partire da sistemi e modelli semplici e costruire prima una pipeline end-to-end solida. La complessità deve guadagnarsi il proprio costo attraverso un miglioramento misurabile fuori dal training set.

Fonte: https://developers.google.com/machine-learning/guides/rules-of-ml/

### Il deliverable del capitolo

Alla fine costruiremo una **Predictive Decision Card** che documenta:

- decisione;
- prediction unit;
- prediction time;
- horizon e label;
- feature availability;
- baseline;
- validation design;
- metriche di ranking/calibration;
- operating threshold e capacità;
- principali failure mode;
- monitoring e retraining;
- scope e owner.

> **Un modello utile non è quello con lo score più impressionante nel notebook. È quello la cui performance fuori campione rimane abbastanza affidabile da migliorare una decisione reale.**
