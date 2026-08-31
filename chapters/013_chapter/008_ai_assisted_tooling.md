# 13.7 AI-assisted analytics: accelerare senza delegare il giudizio

L'AI generativa sta trasformando quasi tutti gli strumenti dell'analista.

Oggi può:

- generare formule Excel;
- scrivere SQL;
- produrre codice Python o R;
- suggerire visualizzazioni;
- spiegare errori;
- costruire trasformazioni;
- documentare query;
- proporre test;
- riassumere risultati.

Questo cambia radicalmente il costo dell'esecuzione.

Non cambia però la responsabilità dell'analista sul significato.

## 13.7.1 Caso realistico: una query perfetta per una domanda sbagliata

Un analyst chiede a un assistente AI:

> «Trova i clienti con churn più alto negli ultimi sei mesi e identifica le feature più importanti.»

L'assistente produce:

- query SQL;
- dataset di training;
- modello di classificazione;
- feature importance;
- grafici.

Il lavoro sembra completo.

Poi emerge che la variabile `cancel_reason` era stata popolata solo dopo la cancellazione ed era presente nel dataset utilizzato per predire il churn.

Il modello ha AUC 0,96.

È quasi inutile in produzione.

L'AI ha accelerato ogni fase tecnica e ha accelerato anche il leakage.

## 13.7.2 Il nuovo ruolo dell'analista

Con l'AI, il lavoro si sposta da:

**scrivere tutto manualmente**

verso:

**specificare → generare → ispezionare → testare → correggere → interpretare**.

Questo richiede competenze diverse:

- definire bene il contesto;
- fornire schema e grain;
- esplicitare assunzioni;
- costruire test;
- riconoscere output plausibili ma sbagliati;
- validare su esempi noti;
- confrontare con baseline semplici.

## 13.7.3 AI come junior analyst velocissimo

Una metafora utile è trattare l'AI come un collaboratore molto veloce che:

- conosce molta sintassi;
- non conosce automaticamente il contesto aziendale;
- può inventare colonne;
- può assumere definizioni non concordate;
- può produrre risposte convincenti senza verificarle.

Quindi non basta chiedere «scrivimi la query».

Meglio specificare:

- grain delle tabelle;
- chiavi;
- definizione del KPI;
- periodo;
- inclusioni/esclusioni;
- controlli attesi;
- esempi di output corretto.

## 13.7.4 Caso realistico: l'AI trova l'errore che l'analista non vede

L'AI non è solo una fonte di rischio.

Un analyst scrive una query lunga con sei CTE. Il risultato della revenue è superiore del 14% al sistema finance.

Chiede all'assistente di revisionare esclusivamente:

- cardinalità dei join;
- possibili duplicazioni;
- filtri post-join;
- gestione dei NULL.

L'assistente segnala che la join con `order_promotions` è one-to-many e moltiplica le righe ordine.

L'analista verifica con un controllo di conteggio e conferma il problema.

Qui l'AI agisce come secondo revisore e aumenta la qualità.

## 13.7.5 Il protocollo di verifica

Per output generati dall'AI, usiamo almeno cinque controlli:

1. **schema check** — tabelle, colonne e tipi esistono davvero?
2. **grain check** — l'output ha il livello di dettaglio corretto?
3. **reconciliation** — i totali tornano con fonti note?
4. **edge cases** — NULL, duplicati, date limite, zero denominator?
5. **reasonableness** — il risultato è coerente con ordini di grandezza plausibili?

Per modelli statistici aggiungiamo:

- leakage;
- split temporale;
- baseline;
- calibration;
- robustezza;
- causalità vs predizione.

## 13.7.6 AI e convergenza degli strumenti

La distinzione tra strumenti sta diventando meno netta.

Microsoft, per esempio, integra Python in Excel: il codice Python può essere scritto direttamente nelle celle, eseguito nel cloud e combinato con dati del workbook. Questo dimostra che l'interfaccia del foglio di calcolo può convivere con librerie come pandas, NumPy e statsmodels.

Il punto strategico è importante: un analista futuro potrebbe passare meno tempo a scegliere un linguaggio e più tempo a scegliere **il livello di controllo, scala e governance necessario**.

## 13.7.7 La regola più importante

> **Usa l'AI per ridurre il costo della costruzione. Non usarla per ridurre il livello di verifica.**

Più la generazione diventa facile, più la validazione diventa centrale.

### Fonti

- Microsoft Support, *Introduction to Python in Excel*: https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
- Microsoft Support, *Open-source libraries and Python in Excel*: https://support.microsoft.com/en-us/excel/python/open-source-libraries-and-python-in-excel
