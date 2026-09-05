## 5.9 Distribuzione campionaria: la stima osservata è una sola possibilità

Una volta stabilito che il campione ha una relazione difendibile con la popolazione, compare un secondo problema. Anche con un disegno corretto, **un campione diverso avrebbe quasi certamente prodotto una stima leggermente diversa**.

Questa è l'idea che rende possibile tutta la parte inferenziale del capitolo.

Immaginiamo un marketplace che voglia stimare il tempo medio di consegna internazionale. Ogni settimana seleziona casualmente 400 spedizioni da una popolazione molto più ampia e ottiene:

| Campione | Media stimata |
|---|---:|
| 1 | 3,84 giorni |
| 2 | 3,67 giorni |
| 3 | 3,91 giorni |
| 4 | 3,72 giorni |
| 5 | 3,80 giorni |

Non c'è bisogno di supporre che il sistema logistico sia cambiato cinque volte. Campioni diversi contengono combinazioni diverse di spedizioni. Se potessimo ripetere l'estrazione migliaia di volte, otterremmo migliaia di medie leggermente differenti. La distribuzione di quelle medie è la **sampling distribution della media**.

## Dati e stime hanno distribuzioni diverse

La distinzione più importante è tra la distribuzione delle osservazioni e quella della statistica che calcoliamo su di esse.

Le singole consegne possono durare da 1 a 12 giorni e avere una distribuzione molto dispersa. La media di 400 consegne varia molto meno da campione a campione. La prima distribuzione racconta **come varia il fenomeno**; la seconda racconta **come varia la nostra stima del suo centro**.

Prima di raccogliere il campione, la media campionaria non ha ancora un valore: è una quantità casuale. Lo stesso vale per una proporzione, un churn rate, una differenza tra due gruppi o un coefficiente. Dopo il campionamento ne osserviamo una sola realizzazione.

L'inferenza nasce da questa domanda:

> **Quanto avrebbe potuto essere diversa la statistica che abbiamo osservato se il processo di raccolta avesse prodotto un altro campione comparabile?**

## Lo stesso numero di decimali non implica la stessa precisione

Una dashboard può mostrare:

- Regione A: conversion rate 6,1% su 80.000 sessioni eleggibili;
- Regione B: conversion rate 6,5% su 180 sessioni eleggibili.

Entrambe le stime hanno una cifra decimale. Visivamente sembrano possedere la stessa precisione. In realtà pochi acquisti in più o in meno spostano enormemente il 6,5% della Regione B, mentre il 6,1% della Regione A è molto più stabile rispetto al solo rumore campionario.

Questo ci costringe a leggere ogni stima su due assi:

> **livello:** quale valore abbiamo osservato?
>
> **precisione:** quanto quella stima oscillerebbe tra campioni ottenuti con lo stesso disegno?

Il prossimo concetto, lo standard error, quantifica proprio il secondo asse.

> **Una stima puntuale è un risultato osservato. La sampling distribution ci ricorda tutti i risultati plausibili che il campionamento avrebbe potuto produrre al suo posto.**
