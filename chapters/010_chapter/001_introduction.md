# Capitolo 10 — Regressione e modelli predittivi per Data Analyst

## 10.1 Prima del modello: definire che cosa dobbiamo sapere prima che accada

Quando un'organizzazione dice di voler “fare machine learning”, spesso sta nominando una tecnologia prima di avere definito il problema. La domanda professionale viene prima:

> **quale informazione futura ci serve, in quale momento deve essere disponibile e quale decisione cambierà quando l'avremo?**

Prevedere non è un obiettivo autonomo. È un modo per anticipare una decisione. Per questo, prima dell'algoritmo, dobbiamo fissare quattro elementi che descrivono il prodotto predittivo: quale entità riceve una previsione, quando la previsione viene prodotta, che cosa deve accadere e entro quale orizzonte, quale azione userà lo score.

Questa sequenza crea il filo dell'intero capitolo:

```text
decisione
→ prediction unit / prediction time
→ dati realmente disponibili
→ target / horizon
→ baseline
→ validation
→ score / probabilità
→ soglia o ranking
→ azione
→ outcome
→ monitoring
```

Il modello è soltanto uno degli anelli. Se gli altri non sono coerenti, un algoritmo molto accurato può comunque essere inutile.

### Caso simulato/composito — Northstar Logistics

Northstar Logistics gestisce consegne B2B per clienti industriali. Il management chiede:

> “Possiamo prevedere quali spedizioni arriveranno in ritardo?”

La frase sembra precisa, ma può nascondere almeno quattro prodotti differenti: stimare le **ore di ritardo**, stimare la probabilità di superare **2 ore**, ordinare le spedizioni per rischio affinché il control tower analizzi le prime 200, oppure decidere quali spedizioni meritano un intervento costoso come cambio corriere o capacità aggiuntiva.

I dati disponibili contengono distanza, corriere, giorno della settimana, numero di colli, saturazione del deposito, meteo, ora prevista di partenza, eventi di tracking e ora effettiva di consegna. Un primo modello usa anche `actual_delivery_time` e ottiene performance quasi perfetta. Il problema non è statistico: quell'informazione nasce **dopo** l'evento che vorremmo anticipare. Il modello non sta prevedendo il futuro, lo sta leggendo.

Il caso introduce il concetto che governerà tutto il capitolo: il **prediction time** crea una frontiera informativa. Una feature è valida soltanto se sarebbe stata disponibile, nella stessa forma e con la stessa semantica, nel momento in cui la decisione doveva essere presa.

### Prediction unit, time, horizon e action sono una sola specifica

Supponiamo di voler prevedere churn. Dire semplicemente “cliente che churna” non basta. Una specifica utile potrebbe essere:

```text
Prediction unit: account attivo
Prediction time: ogni lunedì alle 06:00
Target: cancellazione volontaria
Horizon: successivi 60 giorni
Decisione: prioritizzare al massimo 2.000 account per Customer Success
```

La prediction unit può essere cliente, ordine, transazione, ticket, macchina o spedizione; non coincide necessariamente con una riga del dataset storico. Il prediction time stabilisce che cosa era conoscibile. Horizon e target devono permettere di ricostruire la label senza ambiguità. L'azione chiarisce perché stiamo costruendo il modello.

Un risk score senza una policy resta un output tecnico. Una policy senza capacità, costi e ownership resta una proposta astratta.

### Prediction e causalità restano problemi diversi

Un modello di churn può usare con grande successo ticket, pagamenti falliti e riduzione dei login. Questo rende quelle feature **segnali di rischio**; non le trasforma automaticamente in leve. Impedire ai clienti di aprire ticket o forzare login artificiali non segue dalla predictive importance.

Il Capitolo 8 ha chiesto: *quale intervento cambia l'outcome rispetto al controfattuale?* Qui chiediamo: *quali casi futuri possiamo anticipare abbastanza bene da supportare una decisione?* Le due capacità possono lavorare insieme, ma non sono intercambiabili.

### La baseline viene prima della complessità

Per capire se un modello crea davvero valore serve un avversario semplice. Per target continui può essere media, mediana, regola operativa o regressione lineare; per classificazione può essere base rate, euristica esistente o regressione logistica.

Google, nelle *Rules of Machine Learning*, raccomanda di costruire prima una pipeline end-to-end solida e modelli semplici, facendo guadagnare alla complessità il proprio costo attraverso miglioramenti misurabili fuori campione. Lo stesso documento raccomanda di testare su dati successivi nel tempo quando il deployment riguarda il futuro e di misurare esplicitamente il training-serving skew.

Riferimento: https://developers.google.com/machine-learning/guides/rules-of-ml/

### Il deliverable: Predictive Decision Card

Alla fine del capitolo costruiremo una **Predictive Decision Card**. Documenterà decisione, prediction unit e time, horizon e label, disponibilità `as-of` delle feature, baseline, validation design, ranking/calibration, operating threshold o top-K, capacità, monitoring, retraining, scope e owner.

La card servirà a rendere verificabile questa promessa:

> **Questo sistema produce questa previsione, in questo momento, per questa popolazione, usando soltanto informazione che esiste davvero allora; la performance è stata validata in questo modo e lo score attiva questa decisione.**

Il resto del capitolo non sarà quindi una rassegna di algoritmi. Sarà il percorso necessario per capire se quella promessa regge davvero fuori dal notebook.