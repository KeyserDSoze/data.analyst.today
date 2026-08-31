## 2.4 Metriche e KPI nel brief: outcome, driver, guardrail e soglia

Il Capitolo 1 ha già fissato il principio semantico: una metrica viene definita, non semplicemente trovata.

Nel brief ci serve un passaggio ulteriore: **assegnare a ogni metrica un ruolo nell'analisi**.

Se raccogliamo venti KPI senza sapere che funzione abbiano, stiamo compilando un catalogo. Un piano analitico efficace distingue invece almeno quattro categorie.

### Outcome metric

È il risultato principale che vogliamo comprendere, prevedere o modificare.

Esempi:

- retention a 90 giorni;
- margine per ordine;
- tempo di consegna;
- conversion rate;
- forecast error.

Nel brief dovrebbe esserci, quando possibile, una metrica primaria chiaramente identificata.

### Driver metrics

Sono variabili o componenti che aiutano a decomporre l'outcome.

Se il margine per ordine è sceso, possibili driver possono essere:

- prezzo medio;
- sconto;
- costo prodotto;
- costo di fulfillment;
- mix categorie;
- tasso di reso.

Un driver non è automaticamente una causa. È una componente o un segnale utile alla diagnosi.

### Guardrail metrics

Servono a impedire che un miglioramento della metrica primaria nasconda un danno altrove.

Se vogliamo aumentare conversione con una promozione, potremmo monitorare:

- margine per ordine;
- tasso di reso;
- cancellazioni;
- customer satisfaction.

Ottimizzare una sola metrica è pericoloso soprattutto quando diventa un obiettivo operativo.

### Target e soglie decisionali

Un KPI acquista maggiore valore decisionale quando è collegato a un riferimento: target, budget, SLA, range atteso o soglia di intervento.

La documentazione Microsoft sui KPI nei modelli tabulari, per esempio, descrive KPI costruiti attorno a una misura di base, un valore target e uno stato. È una convenzione implementativa specifica, ma rende bene una distinzione generale: **una metrica descrive; un KPI viene usato per giudicare una performance rispetto a un riferimento**.

Fonti:
- Microsoft Learn, *Key Performance Indicators in tabular models*: https://learn.microsoft.com/en-us/analysis-services/tabular-models/kpis-ssas-tabular
- Microsoft Learn, *Create key performance indicator (KPI) visualizations*: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi

### Una metric contract minima

Nel brief non serve replicare tutta la documentazione del semantic layer. Serve però una definizione sufficiente a impedire ambiguità durante l'analisi.

Per la metrica primaria annotiamo almeno:

```text
Nome:
Ruolo: outcome / driver / guardrail
Definizione business:
Formula:
Unità/grain:
Popolazione eleggibile:
Numeratore/denominatore, se applicabili:
Finestra temporale:
Esclusioni principali:
Fonte/metric owner:
Baseline o target:
Soglia decisionale, se nota:
```

### Esempio: conversion rate

> Percentuale di sessioni e-commerce valide che generano almeno un ordine confermato nella stessa sessione, escludendo traffico interno, bot e ordini di test.

Formula:

`sessioni con almeno un ordine confermato / sessioni valide`

Questa sola riga apre domande importanti:

- una sessione con due ordini conta una o due volte?
- “confermato” significa creato, pagato o non cancellato?
- come riconosciamo bot e traffico interno?
- la sessione può attraversare la mezzanotte?

Definire la metrica nel brief non risolve automaticamente questi dettagli. Li rende visibili **prima** che due analisti li implementino in modi incompatibili.

### KPI utili soltanto se collegati a una risposta

Una domanda pratica è:

> **“Se questa metrica supera o scende sotto una certa condizione, chi dovrebbe fare che cosa?”**

Se nessuno sa rispondere, può essere comunque una metrica diagnostica o informativa. Ma forse non è un KPI operativo.

Il Capitolo 15 approfondirà le soglie decisionali. Qui ci basta collegare ogni metrica critica al ruolo che svolge nel brief.

> **Non scegliere le metriche perché sono disponibili. Sceglile perché ciascuna riduce un'incertezza specifica o protegge la decisione da un effetto collaterale.**
