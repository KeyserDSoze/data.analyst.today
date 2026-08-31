# 16.3 Dashboard operative, diagnostiche e decisionali

Non tutte le dashboard devono fare la stessa cosa.

Uno degli errori più comuni è costruire una sola dashboard che prova contemporaneamente a:

- monitorare;
- diagnosticare;
- spiegare;
- decidere;
- raccontare una storia;
- servire executive, analyst e operatori.

Il risultato è spesso una pagina sovraccarica che non soddisfa davvero nessuno.

## Dashboard operative

Servono a rispondere:

> “Cosa sta succedendo adesso?”

Caratteristiche tipiche:

- alta frequenza di aggiornamento;
- pochi KPI critici;
- soglie e alert;
- confronto con target o baseline;
- possibilità di drill-down rapido;
- ownership chiara delle anomalie.

Esempi:

- ordini nell'ultima ora;
- payment failure rate;
- call center queue;
- inventory stockout;
- pipeline ingestion freshness.

## Dashboard diagnostiche

Servono a rispondere:

> “Dove e perché sta succedendo?”

Qui possiamo avere:

- segmentazioni;
- decomposizioni;
- funnel;
- cohort;
- drill-down;
- filtri;
- distribuzioni;
- confronti tra periodi.

Sono spesso più ricche e interattive.

## Dashboard decisionali

Servono a rispondere:

> “Cosa dobbiamo decidere?”

Qui il design dovrebbe essere ancora più selettivo.

Spesso servono:

- stato corrente;
- delta vs baseline;
- driver principali;
- scenario o forecast;
- rischio/incertezza;
- opzioni disponibili;
- impatto economico;
- raccomandazione o decision threshold.

## Caso realistico: la dashboard da 54 visualizzazioni

Una catena retail costruisce una “Executive Sales Dashboard” con 54 visualizzazioni distribuite su sei pagine.

Contiene:

- revenue;
- units;
- margin;
- transactions;
- customers;
- store performance;
- category performance;
- weather;
- promotions;
- inventory;
- delivery;
- employee hours;
- NPS;
- returns;
- forecast;
- budget;
- e molto altro.

Il CEO la apre ogni lunedì.

Dopo due mesi emerge un dato interessante: utilizza quasi sempre soltanto quattro viste.

Vuole sapere:

1. siamo sopra o sotto piano?
2. dove si concentra il delta?
3. è un problema temporaneo o strutturale?
4. quali decisioni richiedono attenzione questa settimana?

La dashboard viene ridisegnata.

La prima pagina contiene:

- revenue vs plan;
- margin vs plan;
- contributo al delta per region/category;
- forecast di fine mese;
- tre exception che richiedono decisione.

Le analisi dettagliate restano disponibili in pagine diagnostiche separate.

Il numero di visualizzazioni diminuisce, ma il valore decisionale aumenta.

## Dashboard come interfaccia di un sistema decisionale

Una dashboard non dovrebbe essere giudicata soltanto per:

- estetica;
- numero di utenti;
- numero di visualizzazioni;
- velocità di refresh.

Domande migliori sono:

- quali decisioni supporta?
- quali segnali devono attirare attenzione?
- quale azione segue un alert?
- chi è l'owner?
- quanto tempo impiega un utente a capire se serve intervenire?

## “One screen” non è una legge, è una disciplina

Microsoft suggerisce, quando possibile, di far emergere la storia essenziale su una singola schermata e rimuovere elementi non essenziali.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips

Il principio non significa che ogni sistema debba avere una sola pagina.

Significa che **la prima vista dovrebbe rendere evidente ciò che conta prima di chiedere all'utente di esplorare**.

## Una struttura a livelli

Un pattern utile è:

### Livello 1 — Executive / decision

Pochi KPI, delta, rischi, decisioni.

### Livello 2 — Diagnostic

Segmenti, driver, funnel, breakdown.

### Livello 3 — Evidence

Dettaglio tabellare, controlli, definizioni, lineage.

Questo permette di ridurre il cognitive load senza perdere trasparenza.

**Una buona dashboard non cerca di mostrare tutto. Organizza l'accesso alla complessità.**
