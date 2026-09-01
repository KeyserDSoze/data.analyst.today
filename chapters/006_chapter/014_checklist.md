## 6.13 Lifecycle Diagnostic Map: il deliverable operativo del capitolo

Il rischio di un capitolo su retention e churn è terminare con una collezione di metriche.

Il deliverable operativo dovrebbe invece essere una **Lifecycle Diagnostic Map**: una sintesi che collega il KPI iniziale al punto del lifecycle in cui il comportamento cambia, separando ciò che è osservato da ciò che deve ancora essere dimostrato.

### 1. KPI iniziale

Scrivi il problema come variazione osservata, non come spiegazione.

Esempio:

> La retention M6 delle nuove coorti è scesa dal 67% al 59%.

Non:

> Il nuovo onboarding sta causando churn.

La seconda frase contiene già una causa non ancora verificata.

### 2. Chi

Quali popolazioni spiegano materialmente il cambiamento?

Controlla almeno le dimensioni che hanno significato operativo:

- prodotto/piano;
- canale;
- paese;
- device;
- segmento cliente;
- dimensione account;
- comportamento iniziale.

Evita segmentazioni infinite: il segmento deve cambiare la diagnosi o l'azione.

### 3. Quando

Definisci il momento zero e confronta le coorti alla stessa maturità.

Dichiara:

- evento di ingresso nel lifecycle;
- granularità della coorte;
- età raggiunta;
- cambi di prodotto/processo avvenuti nella timeline.

### 4. Dove

Costruisci il funnel o il percorso essenziale.

Per ogni step specifica:

- evento;
- unità di analisi;
- denominatore;
- ordine richiesto;
- finestra temporale;
- eventuali percorsi alternativi.

La domanda è: **in quale passaggio si concentra il cambiamento?**

### 5. Primo valore

Definisci il candidato di activation.

Chiedi:

- rappresenta davvero valore per il cliente?
- è disponibile abbastanza presto?
- è misurabile senza ambiguità?
- l'unità corretta è utente o account?
- il comportamento è solo correlato alla retention o abbiamo evidenza che sia una leva?

Aggiungi distribuzione e percentili del time-to-value, non soltanto la media.

### 6. Persistenza

Non limitarti a un singolo punto di retention.

Controlla:

- curva completa;
- punti in cui cambia pendenza;
- hazard/momenti di rischio;
- coorti con diversa maturità;
- censoring;
- first value vs repeat value.

### 7. Churn

Dichiara quale perdita stai misurando:

- logo/customer churn;
- revenue churn;
- GRR;
- NRR;
- downgrade/contraction;
- churn volontario;
- churn involontario.

Se il contratto ha scadenze discrete, usa una popolazione eleggibile coerente con il rinnovo.

### 8. Reactivation

Se il prodotto consente ritorni dopo inattività, separa:

- primo evento di ritorno;
- ritorno duraturo;
- valore dopo la riattivazione;
- costo dell'incentivo;
- ritorno spontaneo di baseline.

### 9. Valore economico

Per le coorti più rilevanti mostra almeno:

- revenue cumulata;
- margine/contribution profit quando disponibile;
- CAC;
- payback period;
- valore osservato vs LTV previsto;
- maturità della coorte.

### 10. Rischio e actionability

Se esiste un modello di churn, non usare il risk score come unica priorità.

Mantieni visibili:

- rischio;
- valore a rischio;
- tempo prima del rinnovo;
- causa/problema ipotizzato;
- actionability;
- capacità operativa del team.

### 11. Evidence status

Questa è la parte più importante della mappa.

Dividi le conclusioni in tre blocchi:

**Osservato** — ciò che i dati mostrano direttamente.

**Interpretazione plausibile** — spiegazioni compatibili con l'evidenza, ma non ancora causalmente dimostrate.

**Non dimostrato** — affermazioni che richiedono un metodo ulteriore.

### 12. Prossimo metodo

Una buona lifecycle analysis deve sapere quando fermarsi.

Il prossimo passo può essere:

- altra EDA;
- correzione del tracking;
- analisi causale;
- A/B test;
- survival model;
- churn prediction;
- studio qualitativo/interviste;
- intervento operativo misurato.

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

### La regola finale

La Lifecycle Diagnostic Map è completa quando permette a un decision maker di capire:

> **dove si sta perdendo o creando valore nel lifecycle, per chi, da quando, con quale evidenza e quale domanda deve essere risolta dopo.**

Se contiene soltanto retention, churn e LTV, è ancora una dashboard di metriche. Se collega quelle metriche a un punto del processo e a una decisione, è diventata analisi.
