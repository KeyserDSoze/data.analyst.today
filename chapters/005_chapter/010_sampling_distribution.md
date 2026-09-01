## 5.9 Distribuzione campionaria: la stima è uno dei risultati possibili

Quando calcoliamo una media, una proporzione o una differenza su un campione, il valore ottenuto sembra spesso definitivo.

Ma se avessimo estratto un campione diverso dalla stessa popolazione, avremmo quasi certamente ottenuto un numero leggermente diverso.

Questa idea è il cuore della **distribuzione campionaria**.

### Distribuzione dei dati e distribuzione della statistica

È utile distinguere due oggetti:

1. **distribuzione dei dati** — come variano le singole osservazioni;
2. **distribuzione campionaria** — come varierebbe una statistica se ripetessimo il campionamento molte volte.

Esempio:

- i tempi delle singole consegne possono andare da 1 a 12 giorni;
- la **media di 400 consegne** varia molto meno da campione a campione.

Sono due distribuzioni diverse e rispondono a due domande diverse.

### Caso simulato/composito — Cinque campioni, cinque medie

Un marketplace vuole stimare il tempo medio di consegna internazionale. Ogni settimana seleziona casualmente 400 spedizioni da una popolazione molto più ampia.

| Campione | Media stimata |
|---|---:|
| 1 | 3,84 giorni |
| 2 | 3,67 giorni |
| 3 | 3,91 giorni |
| 4 | 3,72 giorni |
| 5 | 3,80 giorni |

Non dobbiamo concludere che il sistema logistico sia cambiato cinque volte.

Anche con una popolazione stabile, campioni diversi contengono combinazioni diverse di spedizioni.

Se potessimo ripetere l'estrazione migliaia di volte, avremmo migliaia di medie. La distribuzione di quelle medie è la **sampling distribution della media**.

Questa distribuzione descrive la variabilità dovuta al processo di campionamento.

### Una statistica è una variabile casuale prima di essere osservata

Prima di raccogliere i dati, non sappiamo quale valore assumerà:

- la media campionaria;
- una proporzione;
- un churn rate;
- una differenza tra due gruppi;
- un coefficiente stimato.

La statistica è quindi una quantità casuale indotta dal campionamento.

Dopo aver osservato il campione ne vediamo una sola realizzazione.

L'inferenza nasce dal tentativo di capire **quanto quella realizzazione avrebbe potuto essere diversa**.

### Due percentuali con gli stessi decimali possono avere precisione opposta

Supponiamo:

- Regione A: conversion rate 6,1% su 80.000 sessioni eleggibili;
- Regione B: conversion rate 6,5% su 180 sessioni eleggibili.

La dashboard visualizza entrambi con una cifra decimale.

Ma la seconda stima è molto più sensibile a pochi eventi in più o in meno.

Questo è il motivo per cui una percentuale dovrebbe essere letta insieme almeno a:

- numerosità;
- disegno con cui sono state ottenute le osservazioni;
- misura della precisione quando stiamo facendo inferenza.

### Livello e precisione

Ogni stima ha quindi almeno due dimensioni:

- **livello:** quale valore abbiamo osservato;
- **precisione:** quanto quella stima tende a variare tra campioni comparabili.

Il prossimo concetto, lo **standard error**, quantifica proprio la seconda.

> **L'errore standard non ci dice quanto sono dispersi i clienti, gli ordini o i ticket. Ci dice quanto è dispersa la nostra stima tra possibili campioni.**
