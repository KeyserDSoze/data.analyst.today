## 6.13 Lifecycle Diagnostic Map: il deliverable operativo del capitolo

Questa sezione resta volutamente strutturata. Non è un riepilogo espositivo del capitolo, ma un **artefatto operativo** da usare quando retention, churn o valore cambiano e serve ricostruire dove nasce il problema.

La Lifecycle Diagnostic Map collega il KPI iniziale al punto del percorso in cui la traiettoria cambia e obbliga a separare osservazione, interpretazione e causalità non ancora dimostrata.

### 1. KPI iniziale

Scrivi il problema come variazione osservata, non come spiegazione.

> La retention M6 delle nuove coorti è scesa dal 67% al 59%.

Non:

> Il nuovo onboarding sta causando churn.

### 2. Chi

Identifica le popolazioni che spiegano materialmente il cambiamento. Usa solo dimensioni con significato operativo — prodotto/piano, canale, paese, device, segmento cliente, dimensione account, comportamento iniziale — e mostra sempre il denominatore. Se una segmentazione non cambia diagnosi o azione, probabilmente non serve nella mappa.

### 3. Quando

Definisci il momento zero e confronta coorti alla stessa maturità. Registra evento di ingresso nel lifecycle, granularità della coorte, età raggiunta e cambi di prodotto, processo o tracking avvenuti nella timeline.

### 4. Dove

Ricostruisci il funnel o il percorso essenziale. Per ogni step conserva evento, unità di analisi, denominatore, ordine richiesto, finestra temporale ed eventuali percorsi alternativi.

La domanda è: **in quale passaggio si concentra il cambiamento?**

### 5. Primo valore

Definisci il candidato di activation e verifica che rappresenti valore per il cliente, sia osservabile abbastanza presto, misurabile senza ambiguità e costruito sull'unità corretta — utente o account. Distingui sempre correlazione con retention da evidenza che l'evento sia una leva causale.

Aggiungi distribuzione e percentili del time-to-value, non soltanto la media.

### 6. Persistenza

Non fermarti a un solo punto di retention. Guarda curva completa, punti in cui cambia pendenza, hazard o momenti di rischio, maturità delle coorti, censoring e passaggio da first value a repeat value.

### 7. Churn

Dichiara quale perdita stai misurando: logo/customer churn, revenue churn, GRR, NRR, downgrade/contraction, churn volontario o involontario. Se il contratto ha scadenze discrete, costruisci il denominatore sulla popolazione realmente eleggibile al rinnovo.

### 8. Reactivation

Se il prodotto consente ritorni dopo inattività, separa primo evento di ritorno, durable reactivation, valore successivo, costo dell'incentivo e baseline di ritorno spontaneo.

### 9. Valore economico

Per le coorti rilevanti mostra revenue cumulata, margine o contribution profit quando disponibile, CAC, payback period, valore osservato rispetto a LTV previsto e maturità della coorte.

### 10. Rischio e actionability

Se esiste un churn model, non usare il risk score come unica priorità. Mantieni visibili rischio, valore a rischio, tempo al rinnovo, problema ipotizzato, actionability e capacità operativa del team.

### 11. Evidence status

Questa è la parte che impedisce alla mappa di diventare una nuova dashboard.

**Osservato** — ciò che i dati mostrano direttamente.

**Interpretazione plausibile** — spiegazioni compatibili con il pattern ma non ancora dimostrate causalmente.

**Non dimostrato** — affermazioni che richiedono un metodo ulteriore.

### 12. Prossimo metodo

La lifecycle analysis deve anche sapere quando fermarsi. Il passo successivo può essere altra EDA, correzione del tracking, analisi causale, A/B test, survival model, churn prediction, studio qualitativo o intervento operativo misurato.

### Template compatto

| Campo | Risposta |
| --- | --- |
| KPI iniziale |  |
| Chi |  |
| Quando/coorte |  |
| Dove/funnel |  |
| Activation |  |
| Time-to-value |  |
| Momento fragile |  |
| Churn/retention definition |  |
| Reactivation |  |
| Valore economico |  |
| Rischio |  |
| Actionability |  |
| Osservato |  |
| Plausibile |  |
| Non dimostrato |  |
| Prossimo metodo |  |

La mappa è completa quando un decision maker può capire **dove si sta creando o perdendo valore nel lifecycle, per chi, da quando, con quale forza dell'evidenza e quale domanda deve essere risolta dopo**.

Se contiene soltanto retention, churn e LTV, è ancora una dashboard. Se collega quelle metriche a una traiettoria e a una decisione, è diventata analisi.