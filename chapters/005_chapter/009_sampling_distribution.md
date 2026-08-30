## 5.9 Distribuzione campionaria: il numero che ottieni avrebbe potuto essere diverso

Quando calcoliamo una media, una proporzione o un tasso su un campione, tendiamo a trattare il risultato come se fosse il numero vero.

Non lo è.

È uno dei possibili risultati che avremmo potuto ottenere estraendo un campione diverso dalla stessa popolazione.

Questa idea è il cuore della distribuzione campionaria.

### Caso realistico: il tempo medio di consegna che cambia ogni settimana

Un marketplace vuole stimare il tempo medio di consegna degli ordini internazionali. Per contenere i costi di analisi, ogni settimana seleziona casualmente 400 spedizioni tra circa 85.000 consegne.

Nelle prime cinque settimane ottiene queste medie:

| Settimana | Tempo medio stimato |
|---|---:|
| 1 | 3,84 giorni |
| 2 | 3,67 giorni |
| 3 | 3,91 giorni |
| 4 | 3,72 giorni |
| 5 | 3,80 giorni |

Il processo logistico non è necessariamente cambiato cinque volte.

Parte della variazione deriva semplicemente dal fatto che ogni settimana stiamo osservando un campione diverso.

Se potessimo ripetere l'estrazione migliaia di volte e calcolare ogni volta la media, otterremmo una distribuzione di medie campionarie.

Quella distribuzione ci dice quanto la nostra stima tende a fluttuare per puro campionamento.

### Una statistica è una variabile casuale

Questo passaggio concettuale è importante.

La media campionaria non è soltanto una formula applicata ai dati. Prima di osservare il campione, è una quantità che può assumere valori diversi.

Lo stesso vale per:

- una conversion rate;
- una retention rate;
- il churn;
- il ticket medio;
- il tempo medio di gestione;
- la percentuale di difetti;
- la differenza tra due gruppi.

Ogni statistica ha una propria distribuzione campionaria.

### Perché questa idea cambia il modo di leggere una dashboard

Immaginiamo due regioni.

La Regione A mostra una conversion rate del 6,1%.

La Regione B mostra una conversion rate del 6,5%.

Se A ha 80.000 sessioni e B ne ha 180, quei due numeri non hanno la stessa stabilità.

La differenza di 0,4 punti percentuali potrebbe essere molto informativa nel primo caso e quasi interamente rumore nel secondo.

La dashboard mostra due percentuali con lo stesso numero di decimali. La statistica ci ricorda che la loro incertezza può essere radicalmente diversa.

### Il concetto operativo

Una stima ha almeno due dimensioni:

**livello** — quale valore abbiamo osservato;

**precisione** — quanto quel valore avrebbe potuto cambiare con un campione diverso.

L'analista maturo non comunica mai la prima dimenticando la seconda.

Questa distinzione prepara il terreno per errore standard, intervalli di confidenza e test di ipotesi.

### Fonti

[^nist-clt]: NIST/SEMATECH e-Handbook of Statistical Methods, *Normal Distribution*, sezione sul Central Limit Theorem, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
