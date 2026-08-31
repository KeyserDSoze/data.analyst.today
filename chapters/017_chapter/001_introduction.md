# Capitolo 17 — Casi end-to-end di Data Analysis

## 17.0 Dalla domanda ambigua alla decisione

Finora abbiamo studiato separatamente problemi, dati, statistica, causalità, esperimenti, forecasting, regressione, SQL, architettura, strumenti, AI, decisioni e comunicazione.

Nel lavoro reale, però, nessuno ci consegna un problema già diviso in capitoli.

Arriva una domanda come:

> “Perché le vendite stanno scendendo?”

oppure:

> “Quali clienti rischiamo di perdere?”

oppure:

> “Stiamo spendendo troppo in marketing?”

La difficoltà vera sta nel trasformare una domanda ambigua in un percorso analitico affidabile.

Questo capitolo è quindi un laboratorio. Ogni caso segue una struttura ricorrente:

**problema → framing → dati → controlli → analisi → alternative → evidenza → decisione → misurazione**

L'obiettivo non è mostrare la query perfetta o il modello più sofisticato. È mostrare il comportamento professionale dell'analista quando:

- i dati sono incompleti;
- le metriche sono ambigue;
- più spiegazioni competono;
- una correlazione sembra una causa;
- il management vuole una risposta rapida;
- l'AI può accelerare il lavoro ma non eliminare la responsabilità;
- la decisione ha costi e conseguenze reali.

In alcuni casi useremo esempi realistici compositi. In altri richiameremo casi pubblici documentati, chiarendo sempre la differenza.

La domanda che ci accompagnerà in tutto il capitolo è semplice:

> **Che cosa farebbe davvero un buon analista, passo dopo passo?**
