# Capitolo 17 — Casi end-to-end di Data Analysis

## 17.0 Il problema reale non arriva con il nome della tecnica

Finora abbiamo costruito un vocabolario operativo molto ampio:

- Analytical Brief;
- Data Readiness Review;
- EDA Evidence Map;
- Uncertainty Brief;
- Lifecycle Diagnostic Map;
- Temporal Decision Brief;
- Causal Identification Brief;
- Experiment Contract;
- Predictive Decision Card;
- Analytical Data Contract;
- Data Flow Architecture Map;
- Tooling Decision Record;
- AI Analysis Control Sheet;
- Decision Record;
- Decision Communication Pack.

Nel lavoro reale nessuno ci consegna però una richiesta come:

> “Per favore applica una Difference-in-Differences e poi costruisci un Decision Record.”

Arriva qualcosa di molto più ambiguo:

> “Perché le vendite stanno scendendo?”

> “Dobbiamo cambiare prezzo?”

> “Quali clienti dobbiamo contattare?”

> “Possiamo fidarci di questo forecast?”

> “La campagna sta davvero creando valore?”

La parte più difficile del mestiere è quindi **selezionare il percorso analitico prima ancora di eseguirlo**.

## Questo capitolo è il capstone del libro

I casi che seguono non devono essere letti come:

> “esempio di forecasting”, “esempio di causalità”, “esempio di churn”.

Devono essere letti come decisioni con dati incompleti, pressioni reali e più percorsi possibili.

La domanda guida sarà:

> **Qual è il minimo insieme di evidenze sufficientemente affidabili per cambiare questa decisione?**

Questo significa che in alcuni casi serviranno molti deliverable.

In altri sarà professionale fermarsi prima.

Un'analisi semplice con una buona reconciliation può essere migliore di un modello sofisticato costruito per una domanda che non lo richiede.

## Il Capstone Routing Canvas

Prima di entrare nei dati, per ogni caso compiliamo mentalmente sei campi.

### 1. Decisione

Quale scelta concreta è aperta?

Se non sappiamo quale comportamento potrebbe cambiare, rischiamo di produrre un report invece di un'analisi decisionale.

### 2. Failure cost

Che cosa costa di più?

- agire quando non dovremmo;
- non agire quando dovremmo;
- aspettare troppo;
- usare un dato sbagliato;
- sostenere una causalità che non possiamo identificare.

### 3. Claim necessario

Per decidere ci basta sapere:

- **cosa è successo**?
- **dove si concentra**?
- **cosa succederà probabilmente**?
- **cosa ha causato il fenomeno**?
- **quale intervento funzionerebbe**?

Non chiediamo causalità se una decomposition descrittiva è già sufficiente. Non usiamo una correlazione se la decisione richiede davvero causalità.

### 4. Readiness

Quale parte della catena può essere rotta?

- definizione;
- identità;
- grain;
- freshness;
- comparabilità temporale;
- measurement change;
- selection;
- leakage;
- incomplete exposure.

### 5. Deliverable necessari

Scegliamo soltanto quelli che riducono un rischio reale.

Esempio:

```text
Analytical Brief
→ Data Readiness Review
→ EDA Evidence Map
→ Decision Record
→ Decision Communication Pack
```

può essere sufficiente.

In un altro problema servirà:

```text
Analytical Brief
→ Data Readiness Review
→ Causal Identification Brief
→ Experiment Contract
→ Decision Record
```

Il valore non è completare tutta la catena. È **selezionare quella corretta**.

### 6. Stop rule

Quando avremo abbastanza evidenza?

Un capstone maturo deve poter terminare con:

- `DECIDE`;
- `PILOT`;
- `WAIT FOR X`;
- `BUY INFORMATION`;
- `NO ACTION`;
- oppure **“non identificabile con i dati disponibili”**.

Produrre sempre una recommendation netta sarebbe un fallimento del capitolo.

## La struttura dei casi

Ogni caso verrà rivisto secondo una sequenza comune:

**messy question → decision → risk → data contract/readiness → investigation → competing explanations → method gate → evidence → alternatives → decision → communication → measurement**

Ma non tutti useranno ogni passaggio con la stessa profondità.

## Evidence ledger

Durante ogni caso terremo idealmente tre colonne.

### Observed

Fatti direttamente supportati dai dati.

### Inferred

Interpretazioni che richiedono assunzioni.

### Still unknown

Informazioni che possono ancora cambiare la scelta.

Questa separazione impedisce alla narrazione end-to-end di trasformare retroattivamente ogni indizio in una certezza.

## Casi reali e casi compositi

Il capitolo usa entrambi.

### Caso reale documentato

Serve quando una fonte pubblica affidabile permette di osservare una pratica, un problema o un risultato realmente documentato.

Non estenderemo i claim oltre ciò che la fonte sostiene.

### Caso simulato/composito

Serve quando vogliamo seguire un'indagine completa con dati, alternative e decisioni costruiti appositamente per la didattica.

Verrà sempre dichiarato esplicitamente.

## Il ruolo dell'AI nel capstone

L'AI può comparire come:

- generatore di query;
- hypothesis partner;
- debugger;
- reviewer;
- agente di ricerca;
- generatore di comunicazione.

Ma il lettore dovrà sempre chiedere:

> **Quale parte della catena sto delegando e quale controllo impedisce a un errore di propagarsi fino alla decisione?**

Questa è la continuità con **Al timone**.

## La misura del successo

Alla fine di un caso non chiederemo:

> “Abbiamo usato abbastanza tecniche?”

Chiederemo:

- la decisione è diventata più chiara?
- abbiamo eliminato i failure mode più pericolosi?
- il claim è proporzionato all'evidenza?
- sappiamo che cosa non sappiamo?
- il costo di altra analisi è giustificato dal suo possibile valore informativo?
- la comunicazione preserva il significato?
- esiste un piano per misurare ciò che accade dopo?

> **La maturità analitica appare quando sappiamo non soltanto usare una tecnica, ma scegliere quale evidenza produrre, quale evitare e quando è il momento di decidere.**
