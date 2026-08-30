## 2.18 Sintesi ed esercizi del capitolo

Il Capitolo 2 ha introdotto il passaggio fondamentale che precede quasi ogni analisi di qualità: trasformare una richiesta di business in un problema analitico ben definito.

Il flusso completo può essere sintetizzato così:

> **Problema di business → Decisione → Stakeholder → Domanda analitica → Metriche → Baseline → Ipotesi → Dati → Metodo → Evidenza → Comunicazione → Azione**

Questa sequenza non deve essere interpretata in modo rigido. Nella pratica è iterativa: nuove informazioni possono costringerci a ridefinire metriche, scope o ipotesi.

### Idee chiave

- una richiesta non è automaticamente una domanda analitica;
- bisogna partire dalla decisione che si vuole migliorare;
- metriche e KPI devono essere definiti semanticamente prima di essere calcolati;
- baseline e denominatori determinano il significato di un confronto;
- segmentare non significa solo dividere i dati, ma cercare eterogeneità utile;
- domande descrittive, diagnostiche, predittive e causali richiedono metodi diversi;
- la qualità dell'analisi dipende anche dalla qualità del processo di misurazione;
- non tutte le analisi meritano la stessa profondità;
- un risultato inconcludente può essere professionalmente corretto;
- bisogna sapere quando fermarsi;
- l'AI può accelerare esecuzione e generazione di ipotesi, ma non sostituisce la definizione del problema e il controllo dell'evidenza.

---

### Esercizio 1 — Trasformare una richiesta vaga

Richiesta:

> "Vorrei capire meglio i nostri clienti."

Costruisci un Analytical Brief rispondendo almeno a:

1. Quali decisioni potrebbero nascondersi dietro questa richiesta?
2. Chi potrebbero essere i decision owner?
3. Quali metriche useresti in tre scenari diversi?
4. Quali baseline useresti?
5. Quali dati servirebbero?
6. Quali output sarebbero utili?

---

### Esercizio 2 — Vendite in calo

Il CFO afferma:

> "Il fatturato è sceso del 12%. Dobbiamo capire perché."

Prima di analizzare i dati, prepara:

- almeno 10 domande di chiarimento;
- una decomposizione del fatturato in driver;
- almeno 8 ipotesi plausibili;
- i segmenti che analizzeresti;
- la baseline corretta;
- i dati necessari.

Bonus: costruisci un hypothesis tree.

---

### Esercizio 3 — Metriche ambigue

Definisci in modo rigoroso le seguenti metriche:

- cliente attivo;
- churn rate;
- conversion rate;
- fatturato mensile;
- average order value;
- repeat purchase rate.

Per ognuna specifica:

- numeratore;
- denominatore;
- finestra temporale;
- popolazione;
- casi limite;
- possibili interpretazioni alternative.

---

### Esercizio 4 — Descrittivo o causale?

Classifica ciascuna domanda:

1. Quanto è aumentato il churn?
2. Quali clienti hanno maggiore probabilità di abbandonare?
3. Perché il churn è aumentato?
4. L'aumento del prezzo ha causato il churn?
5. Cosa succederebbe al margine se riducessimo il prezzo del 5%?

Spiega quale tipo di evidenza servirebbe per rispondere in modo credibile.

---

### Esercizio 5 — Quando fermarsi

Immagina di avere già scoperto che il calo delle vendite proviene al 85% da due categorie prodotto e che entrambe hanno avuto stock-out ripetuti nello stesso periodo.

Quali analisi aggiuntive faresti prima di concludere?

Quali invece non faresti?

Definisci una stop rule esplicita.

---

### Esercizio 6 — Analisi inconcludente

Hai confrontato la retention di due onboarding flow. Il flow B sembra migliore di 3 punti percentuali, ma il campione è piccolo e l'intervallo di confidenza è ampio.

Scrivi tre versioni della conclusione:

1. una versione scorretta e troppo sicura;
2. una versione tecnicamente corretta;
3. una versione executive che comunichi l'incertezza senza risultare evasiva.

---

### Esercizio 7 — AI come copilota

Usa un sistema AI per generare 15 possibili cause di una riduzione del conversion rate.

Poi valuta ogni ipotesi secondo:

- plausibilità;
- osservabilità;
- dato necessario;
- confondenti;
- test possibile;
- costo dell'analisi.

L'obiettivo non è accettare le ipotesi prodotte dall'AI, ma usarle come materiale grezzo da sottoporre a giudizio analitico.

---

## Domande di autovalutazione

Alla fine del capitolo dovresti essere in grado di rispondere con sicurezza a queste domande:

- So distinguere una richiesta da una domanda analitica?
- Riesco a identificare la decisione dietro una dashboard o un report?
- So definire una metrica in modo non ambiguo?
- So scegliere una baseline sensata?
- So costruire un hypothesis tree?
- So distinguere descrizione, previsione e causalità?
- So definire i requisiti dati prima di iniziare a interrogare il database?
- So dire quando un'analisi è sufficiente?
- So comunicare un risultato inconcludente?
- So usare l'AI come supporto senza delegarle il giudizio?

Se alcune risposte sono ancora incerte, non è un problema: questi concetti torneranno più volte nei capitoli successivi, applicati a dataset, SQL, statistica, visualizzazione e architettura.

Nel prossimo capitolo inizieremo a studiare **la materia prima dell'analista: il dato**. Vedremo come leggere tabelle e dataset, come ragionare sulla granularità, come riconoscere problemi di qualità e come capire se una struttura dati è davvero adatta alla domanda che vogliamo porre.
