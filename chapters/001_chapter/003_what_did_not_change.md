## 1.2 Cosa non è cambiato

Se il modo di eseguire l'analisi cambia rapidamente, che cosa rimane stabile?

Prendiamo una frase comune:

> “Le vendite stanno diminuendo.”

Non è ancora una domanda analitica completa.

Prima di aprire un foglio, scrivere SQL o interrogare un assistente AI dobbiamo chiarire almeno:

- che cosa significa “vendite”;
- rispetto a quale baseline stiamo osservando il calo;
- quale popolazione e quale periodo contano;
- quale decisione deve essere presa;
- quali spiegazioni sarebbero compatibili con l'evidenza.

La tecnologia può accelerare il lavoro che segue. Non può rendere irrilevanti queste scelte.

### L'analisi comincia dal problema

Questa è una delle tesi fondamentali del libro:

> **L'analisi dei dati non comincia dai dati. Comincia dal problema.**

Un dataset può avere milioni di righe, ma senza una domanda non sappiamo ancora quale informazione sia rilevante, quale livello di qualità sia necessario o quale metodo abbia senso applicare.

Framework sviluppati molto prima dell'AI generativa formalizzano lo stesso principio. In CRISP-DM la prima fase è la **Business Understanding**: chiarire obiettivi, vincoli e criteri di successo prima di investire nelle fasi tecniche.[^ibm-business]

### Le definizioni vengono prima dei calcoli

Concetti come revenue, cliente attivo, churn, conversione o margine non sono semplici nomi di colonne.

Sono definizioni.

Un calcolo può essere sintatticamente corretto e semanticamente sbagliato. Possiamo sommare la colonna giusta nel periodo sbagliato, usare un denominatore non comparabile o trattare come “cliente” un'entità diversa da quella rilevante per la decisione.

Per questo la semantica non è un'aggiunta alla tecnica. Viene prima.

### Il dato è una rappresentazione, non la realtà

I dati sono prodotti da sistemi e processi.

Qualcuno decide che cosa registrare. Un'applicazione decide quando creare un evento. Una pipeline filtra, deduplica o trasforma. Alcune osservazioni mancano. Alcune definizioni cambiano nel tempo.

La fase di **Data Understanding** di CRISP-DM include proprio l'esame del contenuto e della qualità dei dati prima della modellazione.[^ibm-data-understanding]

La domanda non è soltanto:

> “Che cosa dice il dataset?”

ma anche:

> **“Come è stato prodotto, e quale parte del fenomeno non riesce a rappresentare?”**

### Il confronto determina il significato

Dire che una metrica è alta, bassa, cresciuta o diminuita implica sempre una baseline.

Mese precedente, anno precedente, forecast, budget, gruppo di controllo e trend storico possono raccontare storie diverse.

Scegliere il confronto non è un dettaglio di visualizzazione. È parte della domanda.

### Un pattern non è ancora una causa

Due fenomeni possono muoversi insieme senza che uno produca l'altro.

Confondenti, selezione, causalità inversa e cambiamenti simultanei possono generare pattern molto convincenti.

Strumenti più potenti possono trovare più associazioni. Non eliminano il bisogno di chiedere quale meccanismo potrebbe averle prodotte.

La causalità avrà un capitolo dedicato. Qui fissiamo soltanto la disciplina di base: **non trasformare una relazione osservata in una spiegazione più forte di quanto il disegno dell'analisi consenta.**

### L'incertezza rimane

Dati incompleti, campioni, errori di misurazione, modelli e futuro introducono incertezza.

Una risposta professionale non deve sempre essere certa. Deve essere chiara su ciò che sappiamo, ciò che non sappiamo e su quanto questa differenza conta per la decisione.

### La decisione rimane il punto di arrivo

Un'analisi può essere descrittiva, esplorativa o conoscitiva e non generare immediatamente un'azione. Ma dovrebbe comunque ridurre un'incertezza rilevante.

Il lavoro analitico produce valore quando collega il fenomeno osservato a una scelta migliore e, quando possibile, misura ciò che accade dopo la scelta.

Le sezioni successive entreranno in dettaglio su questi elementi. Per ora possiamo riassumere ciò che non è cambiato con una frase:

> **Un analista non viene pagato per produrre numeri. Viene pagato per ridurre l'incertezza in modo sufficientemente affidabile da migliorare una decisione.**

Gli strumenti cambiano radicalmente.

Questa responsabilità molto meno.

---

### Fonti

[^ibm-business]: IBM, *Business Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/it/spss-modeler/19.0.0?topic=understanding-business-overview
[^ibm-data-understanding]: IBM, *Data Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview
