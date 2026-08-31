# Capitolo 12 — Data architecture per Data Analyst

Un Data Analyst non deve necessariamente progettare da solo l'intera piattaforma dati di un'azienda. Ma deve capire abbastanza bene l'architettura da sapere **dove vive il dato, come ci è arrivato, quanto è fresco, quali trasformazioni ha subito e quale livello è quello corretto da interrogare**.

Questa competenza diventa sempre più importante quando l'ecosistema cresce. Un file CSV locale è semplice. Un sistema composto da applicazioni transazionali, CRM, eventi digitali, API, pipeline, data warehouse, lakehouse, semantic layer e dashboard non lo è.

La domanda non è quindi:

> Qual è la tecnologia migliore?

La domanda utile è:

> Quale architettura rende possibile rispondere alle domande di business in modo affidabile, sostenibile, governato e sufficientemente veloce?

## Dalla query al sistema

Nel capitolo precedente abbiamo ragionato sulla qualità di una query. Qui allarghiamo la prospettiva.

Una query corretta può comunque produrre una risposta sbagliata se:

- legge una tabella operativa invece della versione analitica;
- ignora dati arrivati in ritardo;
- usa una dimensione non storicizzata;
- interroga un layer raw non ancora validato;
- legge una replica aggiornata ogni 24 ore per una decisione che richiede dati quasi real time;
- usa metriche costruite localmente invece di definizioni condivise;
- combina dati provenienti da pipeline con SLA differenti.

L'architettura non è quindi un tema distante dall'analisi. È parte della qualità dell'evidenza.

## Caso realistico: il dashboard che era sempre in ritardo

Una società di delivery, **SwiftDrop**, misura gli ordini consegnati in ritardo. Il management vede alle 9:00 del mattino un late delivery rate del 7,8% e conclude che la situazione è sotto controllo.

Alle 14:00 Operations comunica però che la mattina è stata disastrosa.

L'analista scopre che:

- gli ordini sono registrati nel sistema operativo in tempo reale;
- il data warehouse riceve un batch completo solo alle 6:00 e alle 18:00;
- il dashboard BI usa il warehouse;
- quindi alle 9:00 mostra quasi esclusivamente il giorno precedente.

Il calcolo del KPI era corretto. La **latenza architetturale** non era coerente con la decisione.

Il problema non si risolve cambiando formula. Si risolve chiarendo la relazione tra:

**domanda → freschezza necessaria → sorgente → pipeline → layer analitico → SLA**.

## La mappa del capitolo

Costruiremo una mappa mentale dei componenti più comuni:

**sistemi operativi → ingestion → trasformazione → storage analitico → modellazione → semantic layer → consumo**

Vedremo:

- OLTP vs OLAP;
- ETL vs ELT;
- warehouse e data mart;
- data lake e lakehouse;
- batch vs streaming;
- architetture a livelli come Bronze, Silver e Gold;
- semantic layer;
- lineage, catalogo e governance;
- affidabilità, costi e trade-off;
- come scegliere un'architettura proporzionata al problema.

Il principio guida sarà sempre lo stesso:

> L'architettura migliore non è quella con più componenti. È quella che riduce l'ambiguità e il costo operativo mantenendo il livello di affidabilità richiesto dalle decisioni.
