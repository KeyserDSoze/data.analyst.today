## 4.19 Caso studio: il marketplace che sembrava crescere troppo bene

Il management di **MercatoHub**, marketplace europeo di elettronica ricondizionata, riceve un report molto positivo.

Nel secondo trimestre:

- GMV: +18,7% anno su anno;
- ordini: +12,1%;
- average order value: +5,9%;
- clienti attivi: +9,4%.

La presentazione del lunedì mattina apre con una frase: “La crescita sta accelerando”.

Prima di accettarla, l'analista costruisce un'EDA completa.

### Primo passo: distribuzioni, non soltanto medie

L'AOV è passato da 286 € a 303 €.

Ma l'istogramma mostra che la crescita non è uniforme. La fascia sotto 200 € è quasi stabile, mentre aumenta molto il peso degli ordini sopra 800 €.

Il P50 passa da 231 € a 234 €. Il P90 passa da 612 € a 735 €.

La crescita dell'AOV è quindi trainata soprattutto dalla coda alta.

### Secondo passo: segmentare

Per categoria:

| Categoria | GMV YoY |
|---|---:|
| Smartphone | +6% |
| Laptop | +11% |
| Tablet | +4% |
| Fotografia | +9% |
| Gaming GPU | +71% |

Il 46% dell'incremento assoluto di GMV proviene da Gaming GPU, che rappresentava meno del 15% del business l'anno precedente.

### Terzo passo: guardare il denominatore

Il numero di clienti attivi cresce del 9,4%. Ma la definizione di “attivo” comprende chiunque abbia visitato il sito da autenticato almeno una volta negli ultimi 90 giorni.

Il team marketing ha lanciato una nuova app e introdotto il login obbligatorio per salvare un prodotto nei preferiti.

I clienti “attivi” sono quindi cresciuti anche per un cambiamento di tracking e UX.

Gli acquirenti unici crescono soltanto del 4,1%.

### Quarto passo: osservare la dispersione per seller

Il marketplace ha 1.840 seller attivi.

La mediana del GMV per seller è quasi invariata. Il top 5% dei seller cresce invece del 38%.

Un box plot per seller mostra una distribuzione ancora più asimmetrica rispetto all'anno precedente.

La crescita si sta concentrando.

### Quinto passo: controllare tassi e qualità

Il return rate complessivo sembra migliorare dal 7,8% al 7,1%.

Separando per categoria:

- Smartphone: 6,4% → 6,5%;
- Laptop: 7,0% → 7,2%;
- GPU: 11,2% → 12,8%.

L'apparente miglioramento aggregato nasce dal mix e da una modifica nel denominatore: il nuovo report conta i resi sulle unità spedite, mentre quello storico usava gli ordini consegnati.

La serie non è perfettamente comparabile.

### Sesto passo: identificare gli outlier

Tre giornate mostrano GMV superiore di oltre quattro deviazioni standard rispetto alla media giornaliera.

Non sono errori. Corrispondono al lancio di una nuova GPU ad alta domanda, venduta da pochi seller con prezzi medi oltre 1.200 €.

Rimuoverle come outlier cancellerebbe un evento reale che spiega una parte importante della crescita.

### La conclusione cambia

La frase iniziale “la crescita sta accelerando” diventa:

> Il GMV cresce del 18,7%, ma la crescita è fortemente concentrata nella categoria Gaming GPU e nei seller di fascia alta. Gli acquirenti unici crescono molto meno dei clienti attivi dichiarati, perché una modifica nella UX ha alterato la metrica di attività. La crescita core del marketplace è positiva ma più moderata di quanto suggeriscano i KPI aggregati. Inoltre la concentrazione e il return rate della nuova categoria richiedono monitoraggio.

Questa seconda conclusione è meno spettacolare. È anche molto più utile.

### Le decisioni che ne derivano

Il management decide di non aumentare indiscriminatamente il budget marketing del 25%.

Vengono invece approvate tre azioni:

1. separare nei report la crescita core dalla crescita della categoria GPU;
2. creare guardrail su seller concentration e return rate;
3. ridefinire formalmente active customer e rendere retrocompatibile la serie storica.

Il valore dell'EDA non è stato produrre più grafici.

È stato impedire che un aggregato vero producesse una storia sbagliata.
