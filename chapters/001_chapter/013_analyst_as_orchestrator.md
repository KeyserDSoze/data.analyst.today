## 1.12 Il Data Analyst come orchestratore del sistema analitico

Il Capitolo 0 ha parlato dell'analista come manager di agenti AI.

Qui allarghiamo il concetto.

Anche senza AI, un Data Analyst opera al centro di un sistema composto da persone, processi, fonti dati, definizioni, trasformazioni, strumenti e decisioni.

Il suo lavoro non consiste nel padroneggiare personalmente ogni componente. Consiste nel capire **come i componenti si collegano e dove può rompersi il significato**.

### Un numero executive ha una storia

Immaginiamo una dashboard che mostra il `Monthly Recurring Revenue`.

Dietro quel singolo numero possono esserci:

1. un cliente che sottoscrive o modifica un piano;
2. un'applicazione che registra eventi e stati;
3. un database transazionale;
4. una pipeline di ingestione;
5. trasformazioni su contratti, upgrade, downgrade e cancellazioni;
6. un warehouse;
7. regole per valute, crediti e rimborsi;
8. un modello semantico;
9. una metrica condivisa;
10. una dashboard;
11. un processo di business che usa il numero per decidere.

L'analista non deve necessariamente costruire tutti questi elementi.

Deve però sapere che il numero finale eredita le assunzioni introdotte lungo l'intera catena.

Se una regola di downgrade cambia nella pipeline, il dashboard può cambiare senza che il business sia cambiato.

Se la definizione di MRR nel semantic layer diverge da Finance, due team possono discutere dello stesso concetto usando numeri incompatibili.

Se il dato è stale, un report perfettamente calcolato può descrivere il passato come se fosse il presente.

Questa è la **visione end-to-end del dato** che distingue progressivamente un analista maturo.

### Orchestrare significa sapere quando il problema non è “analytics”

Un problema che appare analitico può richiedere competenze diverse.

Se manca una sorgente affidabile, serve forse data engineering.

Se la stessa metrica viene implementata in dieci modi, serve forse un semantic layer o analytics engineering.

Se dobbiamo stimare un effetto causale complesso, può servire uno specialista di experimentation o data science.

Se una dashboard è corretta ma nessuno la usa, il problema può essere di processo decisionale, adozione o comunicazione.

Il valore dell'analista sta anche nel riconoscere **che tipo di problema ha davanti** invece di tentare di risolvere tutto con il proprio strumento preferito.

### Dal tool-first al problem-first

Un approccio fragile parte dalla tecnologia:

> “Ho Power BI: come risolvo questo problema in Power BI?”

oppure:

> “Sto studiando Python: devo usare Python per questa analisi.”

L'approccio maturo parte dal bisogno:

> **“Qual è il modo più semplice, affidabile e sostenibile per ottenere l'evidenza necessaria?”**

Una tabella di 2.000 righe analizzata una sola volta può essere perfetta in un foglio elettronico.

Miliardi di righe già presenti in un warehouse probabilmente devono essere aggregate vicino alla sorgente invece di essere scaricate su un laptop.

Metriche consultate ogni giorno da molti manager richiedono più governance di un notebook esplorativo usato da una persona per due ore.

Una trasformazione che alimenta molti processi ogni mattina non è più soltanto una query personale: sta diventando un prodotto operativo.

Il Capitolo 13 svilupperà un framework completo per la scelta degli strumenti. Qui ci interessa il principio:

> **la maturità tecnica non consiste nell'usare sempre lo strumento più potente, ma nel riconoscere il livello di tecnologia necessario al problema.**

### Cinque domande prima di scegliere lo strumento

Come anticipo del framework futuro, possiamo chiederci:

1. **Volume** — quanti dati dobbiamo elaborare?
2. **Frequenza** — è un'analisi una tantum o un processo ricorrente?
3. **Complessità** — basta un'aggregazione o servono trasformazioni e modelli più articolati?
4. **Audience** — il risultato serve a una persona o a un'intera organizzazione?
5. **Governance** — quanto contano accessi, lineage, riproducibilità e definizioni condivise?

A queste si aggiungeranno costo, latenza, sicurezza, mantenibilità e competenze del team.

### L'analista come ponte

Il Data Analyst moderno collega mondi che parlano linguaggi diversi.

Il business ragiona in clienti, ricavi, costi, rischi e decisioni.

I sistemi dati ragionano in eventi, tabelle, chiavi e timestamp.

La statistica ragiona in popolazioni, distribuzioni, assunzioni e incertezza.

L'architettura ragiona in pipeline, storage, latenza e affidabilità.

L'AI aggiunge un ulteriore strato di esecuzione e interazione, con le regole di supervisione discusse nel Capitolo 0.

Il valore dell'analista sta nella capacità di attraversare questi mondi senza confonderli.

### Una definizione operativa del Data Analyst moderno

Possiamo allora estendere la definizione introdotta nella sezione 1.3:

> **Un Data Analyst riduce l'incertezza attorno a decisioni reali trasformando problemi in domande, dati in evidenza ed evidenza in azioni verificabili, orchestrando persone e strumenti nella misura necessaria al problema.**

Nessun singolo software definisce il mestiere.

A definirlo è la capacità di mantenere coerente la catena tra realtà, dato, metodo e decisione.
