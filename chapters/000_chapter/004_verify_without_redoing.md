## 0.3 Verificare senza rifare tutto a mano
Se per usare l'AI dobbiamo rifare manualmente ogni passaggio, abbiamo perso gran parte del vantaggio.

Ma se non verifichiamo nulla, abbiamo perso il controllo.

La domanda corretta non è quindi:

> “Devo ricontrollare tutto?”

La domanda è:

> **“Quale sistema di controlli mi permette di ottenere sufficiente fiducia senza replicare l'intero lavoro?”**

È una differenza fondamentale.

## Verifica non significa duplicazione

Un buon processo di verifica utilizza controlli indipendenti e mirati.

Se un agente calcola il revenue mensile, non serve necessariamente riscrivere la stessa query da zero.

Possiamo controllare:

- il totale contro Finance;
- il numero di ordini contro la sorgente operativa;
- alcuni record campione;
- la cardinalità dei join;
- la coerenza con il mese precedente;
- la somma dei segmenti rispetto al totale;
- la presenza di valori impossibili.

Se un agente costruisce un modello predittivo, possiamo verificare:

- split temporale o casuale corretto;
- leakage;
- baseline semplice;
- metriche su holdout;
- calibrazione;
- stabilità su segmenti;
- performance dopo il deployment.

Se un agente propone una spiegazione causale, possiamo controllare:

- temporalità;
- confondenti plausibili;
- gruppi comparabili;
- design sperimentale o quasi-sperimentale;
- alternative explanation.

La verifica deve cercare **punti di rottura**, non replicare ogni operazione.

## Il principio dei controlli ortogonali

Un controllo è particolarmente utile quando misura il risultato da un'angolazione diversa.

Se una query dice che il fatturato è €12,4M e un secondo agente riscrive la stessa query con la stessa logica, abbiamo due implementazioni della stessa assunzione.

Non necessariamente due evidenze indipendenti.

Meglio confrontare il dato con:

- ledger Finance;
- incassi;
- ordini spediti;
- reconciliation esistente;
- trend storico.

Questo principio può essere espresso così:

> **Più il controllo è indipendente dall'errore che stiamo cercando, più è informativo.**

## Caso realistico: una query giusta per la tabella sbagliata

Un agente riceve il compito:

> “Calcola il churn mensile degli abbonati.”

Genera una query formalmente corretta usando `subscriptions_current`.

Il risultato mostra churn al 4,1%.

Il dato sembra plausibile.

Ma `subscriptions_current` contiene solo lo stato corrente degli abbonamenti.

Le sottoscrizioni cancellate vengono rimosse dalla tabella dopo 90 giorni.

La query è corretta.

La fonte non è adatta a una misura storica.

Un secondo agente che legge la stessa tabella potrebbe confermare il 4,1%.

Un controllo ortogonale usa invece:

- eventi di cancellazione;
- snapshot mensili;
- fatturazione;
- confronto con il report Finance.

Il churn ricostruito risulta 6,8%.

Il problema non era il codice.

Era il modello mentale del dato.

## Verification stack

Per analisi importanti possiamo pensare a quattro livelli.

### 1. Controlli deterministici

- unique;
- not null;
- range;
- referential integrity;
- row count;
- reconciliation;
- freshness.

### 2. Controlli statistici

- distribuzioni;
- drift;
- anomalie;
- intervalli attesi;
- benchmark storico.

### 3. Controlli semantici

- grain;
- definizione metrica;
- denominatore;
- popolazione;
- finestra temporale;
- inclusioni/esclusioni.

### 4. Controlli decisionali

- l'effetto è materialmente rilevante?
- l'incertezza è compatibile con la decisione?
- il risultato è causale o descrittivo?
- esiste una spiegazione alternativa credibile?

I primi controlli possono essere fortemente automatizzati.

Gli ultimi richiedono molto più giudizio.

## Campionare invece di leggere tutto

Quando gli agenti producono molti output, la review può usare campionamento intelligente.

Non leggiamo 500 query.

Possiamo selezionare:

- output ad alto impatto;
- casi con bassa confidence;
- risultati molto diversi dalla baseline;
- segmenti rari;
- query con molti join;
- casi che modificano dati o sistemi;
- output scelti casualmente per audit.

Questa logica assomiglia al quality control in produzione.

## Red team interno

Un pattern molto utile è assegnare a un agente il compito di contestare il risultato.

Non:

> “Verifica questa analisi.”

ma:

> “Assumi che questa conclusione sia sbagliata. Trova tre modi plausibili in cui potremmo esserci ingannati e proponi test per distinguerli.”

Il risultato non diventa automaticamente vero perché nessun controesempio emerge.

Ma il processo riduce il rischio di confirmation bias.

## Quando serve ancora la review manuale

La review umana approfondita resta particolarmente importante quando:

- l'azione è irreversibile;
- l'impatto finanziario è elevato;
- sono coinvolte persone;
- ci sono implicazioni normative;
- il sistema opera fuori distribuzione;
- gli agenti sono in disaccordo;
- l'evidenza è nuova o sorprendente;
- la spiegazione dipende da molte assunzioni.

La documentazione Microsoft sugli agenti raccomanda di mantenere human-in-the-loop per azioni consequenziali e di definire escalation chiare; la profondità della governance dovrebbe crescere con il rischio dell'agente.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

## La regola pratica

> **Non verificare tutto allo stesso modo. Verifica in proporzione a rischio, novità, impatto e incertezza.**

Il professionista AI-native non sostituisce il lavoro manuale con la fiducia cieca.

Sostituisce il controllo riga-per-riga con un sistema di evidenze, test, campionamento, audit ed escalation.