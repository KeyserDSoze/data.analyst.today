## 10.15 Caso studio: il modello eccellente offline che perde valore in produzione

### Contesto

**OrbitCom** è un operatore telecom con circa 3,8 milioni di clienti consumer.

L'azienda vuole ridurre il churn volontario nei 60 giorni successivi.

Il team costruisce un modello che assegna ogni settimana una probabilità di churn a ciascun cliente.

L'obiettivo operativo è semplice:

- selezionare i clienti più a rischio;
- inviarli al team retention;
- offrire un intervento mirato;
- ridurre le disdette.

### La fase offline

Il modello viene sviluppato su 18 mesi di storico.

Feature principali:

- variazione dell'utilizzo dati;
- numero di reclami;
- ritardi di pagamento;
- qualità rete percepita;
- chiamate al supporto;
- variazione della spesa;
- anzianità cliente;
- upgrade/downgrade recenti;
- utilizzo dell'app;
- presenza di offerte concorrenti rilevate da survey.

Performance sul test temporale:

| Metrica | Valore |
|---|---:|
| ROC-AUC | 0,87 |
| PR-AUC | 0,39 |
| precision top 5% | 44% |
| recall top 5% | 31% |

Il risultato viene considerato eccellente.

Il business stima che, se il modello identifica correttamente clienti che stanno per abbandonare, una chiamata proattiva può salvare una quota significativa del valore.

### Il primo mese di produzione

Dopo quattro settimane, il team retention contatta circa 38.000 clienti.

La precision osservata sembra coerente con le attese.

Il progetto viene dichiarato un successo.

### Tre mesi dopo

Le metriche iniziano però a peggiorare:

| Metrica | Offline | Mese 1 | Mese 3 |
|---|---:|---:|---:|
| ROC-AUC | 0,87 | 0,85 | 0,77 |
| precision top 5% | 44% | 41% | 28% |
| churn rate nel top 5% | 46% | 43% | 30% |

Il team sospetta un problema del modello.

Ma l'analisi mostra almeno quattro cause diverse.

### Problema 1 — è cambiata la popolazione

Una nuova campagna aggressiva ha portato molti clienti più giovani, con contratti mensili e forte utilizzo digitale.

Questi utenti erano poco rappresentati nel training set.

Le distribuzioni di:

- età;
- tenure;
- device;
- canale di acquisizione;
- frequenza di login;

sono cambiate sensibilmente.

È **data drift**.

### Problema 2 — è cambiata la relazione tra segnali e churn

Nel periodo storico, un forte calo di utilizzo era un segnale potente di abbandono.

Dopo l'introduzione di un nuovo piano con roaming incluso, molti clienti riducono temporaneamente il traffico domestico senza voler disdire.

Il vecchio pattern “calo utilizzo → churn” si indebolisce.

È **concept drift**.

### Problema 3 — il modello modifica il processo che sta osservando

I clienti ad alto rischio vengono contattati.

Quindi il loro churn osservato non rappresenta più il churn che avrebbero avuto senza intervento.

Il deployment genera un feedback loop.

Se il trattamento funziona, alcuni clienti ad alto score non churnano proprio perché il modello li ha identificati.

Valutare ingenuamente il modello sulla popolazione trattata può quindi sottostimare il rischio reale che aveva previsto.

### Problema 4 — capacità operativa

Il team retention può gestire circa 25.000 contatti alla settimana.

Il modello ne produce 42.000 sopra la soglia scelta.

Ne consegue che:

- alcuni clienti vengono contattati tardi;
- altri non vengono contattati;
- gli operatori accelerano le chiamate;
- la qualità dell'intervento scende.

La performance del **sistema decisionale** peggiora anche se una parte del problema non è nel modello.

### La diagnosi corretta

Il team separa finalmente quattro livelli:

```text
data quality
↓
model performance
↓
operational execution
↓
business outcome
```

Viene creato un monitoraggio distinto per ciascun livello.

### La soluzione

OrbitCom modifica il processo:

1. retraining mensile con rolling window;
2. validation temporale su periodi recenti;
3. calibration separata per nuovi clienti e clienti storici;
4. soglia scelta in funzione della capacità reale del team;
5. gruppo di controllo randomizzato tra clienti eleggibili;
6. monitoraggio del trattamento, non solo dello score;
7. dashboard di drift per canale, tenure e piano tariffario;
8. rollback automatico se precision e calibration superano soglie di deterioramento concordate.

### Il punto più importante

Il modello non aveva semplicemente “perso accuracy”.

Era cambiato il sistema in cui operava.

Il problema iniziale era stato formulato come:

> prevedere il churn.

Ma la vera decisione era:

> quali clienti dobbiamo contattare, con quale intervento, con quale priorità e con quale capacità operativa per massimizzare churn evitato e valore economico?

Questa seconda domanda richiede molto più di un buon classifier.

Richiede dati, modello, causalità, operations e misurazione.

Ed è esattamente qui che il Data Analyst smette di essere un produttore di score e diventa progettista del processo decisionale.