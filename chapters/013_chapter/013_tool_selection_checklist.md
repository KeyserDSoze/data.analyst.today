## 13.13 Tool-selection checklist: scegliere partendo dal problema

Quando un analyst deve scegliere uno strumento, la domanda peggiore è:

> "Qual è il tool più moderno?"

La domanda migliore è:

> "Qual è il modo più semplice, affidabile e mantenibile per risolvere questo problema nel contesto reale in cui verrà usato?"

### Checklist operativa

Prima di scegliere, rispondi a queste domande.

#### 1. Qual è la decisione?

- esplorazione una tantum;
- report ricorrente;
- dashboard operativa;
- modello predittivo;
- processo automatizzato;
- sistema quasi real-time.

#### 2. Quanto dato c'è davvero?

Non usare "big data" come concetto astratto.

Chiedi:

- quante righe?
- quante colonne?
- quanti GB/TB?
- quante sorgenti?
- quale crescita attesa?

#### 3. Dove vive il dato?

Portare 500 GB sul laptop per usarli in Python può essere molto peggio che eseguire una query vicino al dato.

#### 4. Quanto spesso cambia?

Una domanda trimestrale e un processo ogni 30 secondi richiedono architetture diverse.

#### 5. Chi userà il risultato?

- solo l'analyst;
- un team tecnico;
- 300 sales manager;
- il CEO;
- un sistema downstream.

La distribuzione influenza la scelta quasi quanto il calcolo.

#### 6. Deve essere riproducibile?

Più il risultato è importante e ricorrente, maggiore è il bisogno di versionamento, test e automazione.

#### 7. Quanto è stabile la logica?

Se il business sta ancora cercando di capire cosa significhi "cliente attivo", industrializzare troppo presto può cristallizzare una definizione sbagliata.

#### 8. Qual è il costo dell'errore?

Un'analisi esplorativa su una campagna pilota e un modello che blocca pagamenti sospetti hanno livelli di rischio diversi.

#### 9. Quali competenze possiede già il team?

Una soluzione teoricamente elegante ma impossibile da mantenere dal team reale ha un TCO elevato.

#### 10. Quanto velocemente dobbiamo imparare?

Il time-to-insight è parte del problema.

### Matrice di orientamento

| Scenario | Tool spesso sensato come punto di partenza |
|---|---|
| Analisi rapida su dataset piccolo | Excel / spreadsheet |
| Aggregazioni su warehouse | SQL |
| Analisi statistica avanzata | Python o R |
| Dashboard condivisa | BI + semantic layer |
| Esplorazione tecnica iterativa | Notebook |
| Pipeline ripetibile | SQL/Python + orchestrazione |
| Sorgenti SaaS semplici | low-code/no-code, se governabile |
| Scala molto elevata | compute vicino al dato / cloud |

Questa tabella non è una legge. È un punto di partenza.

### Caso realistico: quattro strumenti per la stessa domanda

Domanda:

> "Quali clienti enterprise hanno ridotto l'uso del prodotto di oltre il 30% negli ultimi 60 giorni?"

Possibili implementazioni:

**Excel** — appropriato se abbiamo 2.000 account e un export già pronto.

**SQL** — migliore se gli eventi sono centinaia di milioni nel warehouse.

**Python** — utile se vogliamo aggiungere smoothing, anomaly detection e modelli di rischio.

**BI** — utile se Customer Success deve monitorare continuamente il fenomeno.

La domanda business è la stessa. Cambia il contesto operativo.

### La sequenza migliore spesso usa più strumenti

Una buona analisi può iniziare con SQL, passare a Python e terminare in BI.

Per esempio:

```text
warehouse
   ↓ SQL
coorte analitica
   ↓ Python
modello / simulazione
   ↓ tabella risultati
semantic layer
   ↓ BI
decisione operativa
```

Non c'è alcun premio per fare tutto nello stesso ambiente.

### Quando cambiare tool

Cambiare strumento è giustificato quando il problema supera chiaramente i limiti dell'approccio corrente.

Segnali:

- processi manuali ricorrenti;
- tempi di calcolo eccessivi;
- errori frequenti;
- collaborazione difficile;
- mancanza di auditabilità;
- volume oltre la capacità dello strumento;
- necessità di servizio continuo.

### Regola operativa

> **Parti dal tool più semplice che soddisfa i requisiti reali. Aggiungi complessità solo quando un requisito concreto la rende necessaria.**
