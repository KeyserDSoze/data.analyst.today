# Capitolo 2 — Dal problema di business al problema analitico

> **Una buona analisi non comincia dalla prima query. Comincia da un accordo esplicito su quale decisione stiamo cercando di migliorare e su quale evidenza potrebbe farci cambiare idea.**

Il Capitolo 1 ha costruito il modello mentale generale del lavoro analitico. Abbiamo distinto problemi, domande, dati, metodi, evidenza e decisioni.

Questo capitolo fa un passo più operativo: trasforma quei concetti in una **specifica di lavoro**.

Un Data Analyst riceve raramente domande già pronte per essere analizzate. Più spesso riceve richieste come:

- “Le vendite stanno andando male, capiamo perché.”
- “Ci serve una dashboard clienti.”
- “Vorremmo capire se il marketing funziona.”
- “Perché gli utenti abbandonano?”
- “Quali prodotti dovremmo spingere?”
- “Possiamo prevedere il prossimo trimestre?”

Sono segnali di un bisogno. Non sono ancora istruzioni analitiche sufficienti.

Tra la richiesta e l'esecuzione manca un passaggio di progettazione.

Lo chiameremo **Analytical Brief**.

## Il brief come contratto di lavoro

Un buon brief non deve essere lungo. Deve rendere esplicite le scelte che, se lasciate implicite, rischiano di emergere soltanto dopo giorni di lavoro:

- quale problema di business stiamo affrontando;
- quale decisione deve essere presa;
- chi possiede quella decisione;
- qual è la domanda analitica primaria;
- quale tipo di evidenza richiede;
- come definiamo la metrica principale;
- quale popolazione e quale periodo osserviamo;
- qual è la baseline;
- quali ipotesi meritano priorità;
- quali dati sono necessari;
- quali limiti conosciamo già;
- quanto approfondimento vale la pena fare;
- quando l'analisi sarà sufficientemente completa.

In altre parole, questo capitolo non aggiunge una seconda catena analitica a quella del Capitolo 1. Prende la catena già fissata e la trasforma in un **piano prima dell'esecuzione**.

## Business Understanding prima della tecnica

La logica è precedente all'AI. CRISP-DM colloca il *Business Understanding* prima del *Data Understanding*: prima si chiariscono obiettivi, requisiti e criteri di successo, poi si entra nei dati.

Fonte:
- IBM, *Business Understanding Overview*: https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview

L'AI rende questo ordine ancora più importante. Se generare una query o una prima analisi richiede pochi secondi, diventa molto facile iniziare a eseguire prima di avere concordato che cosa significhi una risposta utile.

Il problema non è la velocità.

È **accelerare prima di avere scelto la direzione**.

## Obiettivo del capitolo

Alla fine dovresti essere in grado di prendere una richiesta vaga e produrre un brief di una pagina che un business stakeholder, un analyst e un data engineer possano leggere senza interpretazioni incompatibili.

Le sezioni successive costruiranno quel documento un pezzo alla volta:

**problema → decisione → stakeholder → metriche → ipotesi → scope → baseline → segmentazioni → requisiti dati → piano → priorità → stop rule**.

Alla fine riuniremo tutto in un caso completo.

Il deliverable più importante del capitolo non è una dashboard.

È una domanda abbastanza ben progettata da meritare una dashboard, una query, un esperimento o qualunque altro metodo risulti necessario.
