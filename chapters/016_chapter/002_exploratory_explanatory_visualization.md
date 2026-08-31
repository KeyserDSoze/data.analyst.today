## 16.1 Visualizzazione esplorativa e visualizzazione esplicativa
Non tutti i grafici hanno lo stesso scopo.

Durante l'analisi usiamo visualizzazioni per **scoprire**.

Durante la comunicazione usiamo visualizzazioni per **spiegare**.

Confondere queste due fasi produce spesso slide piene di dettagli che riflettono il percorso mentale dell'analista, non il bisogno del pubblico.

## Esplorare significa lasciare spazio alle domande

In EDA possiamo voler vedere:

- distribuzioni;
- segmenti;
- outlier;
- correlazioni;
- serie temporali;
- breakdown multipli;
- versioni alternative dello stesso KPI.

In questa fase è normale produrre decine di grafici.

Molti saranno inutili alla fine.

Non è uno spreco: servono a capire.

## Spiegare significa selezionare

Quando dobbiamo presentare il risultato, la domanda cambia:

> “Qual è il minimo insieme di evidenze necessario perché il pubblico comprenda la conclusione e possa valutarla?”

Qui eliminare è spesso più importante che aggiungere.

## Caso realistico: 27 grafici per rispondere a una domanda

Un team e-commerce deve spiegare perché la conversione è diminuita dal 3,8% al 3,4%.

Durante l'analisi produce 27 visualizzazioni:

- conversione per device;
- browser;
- paese;
- canale;
- landing page;
- giorno della settimana;
- ora;
- new vs returning;
- pagamento;
- app version;
- basket size;
- categoria prodotto;
- e molte altre.

Alla fine emerge una spiegazione molto più semplice:

- il 78% del calo viene da iOS;
- quasi tutto è nella versione 6.12;
- il punto di rottura è il passaggio payment authentication;
- Android e versioni iOS precedenti sono stabili.

La presentazione efficace non mostra 27 grafici.

Ne mostra tre:

1. decomposizione del delta per platform;
2. conversione per app version;
3. funnel con drop sul payment step.

Gli altri grafici restano come materiale di supporto.

## Una regola utile: discovery artifacts vs decision artifacts

Possiamo distinguere:

### Discovery artifacts

Servono all'analista.

Possono essere complessi, numerosi, iterativi e tecnici.

### Decision artifacts

Servono a chi deve decidere.

Devono essere selettivi, contestuali e orientati alla domanda.

Un notebook esplorativo è spesso un buon discovery artifact e un pessimo decision artifact.

Una slide executive può essere un buon decision artifact e un pessimo strumento per fare EDA.

## Non raccontare il percorso in ordine cronologico

Un errore comune è presentare l'analisi nel modo in cui è stata eseguita:

> “Prima abbiamo guardato le vendite, poi i clienti, poi i canali, poi abbiamo fatto questo test...”

Il pubblico raramente ha bisogno della cronologia investigativa.

Ha bisogno della struttura logica:

**cosa è successo → dove → perché pensiamo sia successo → quanto siamo sicuri → cosa proponiamo di fare**.

## Il grafico esplicativo deve avere una frase

Una prova semplice:

Per ogni visualizzazione importante dovremmo essere in grado di completare:

> “Questo grafico serve a mostrare che...”

Se la risposta è vaga, probabilmente il grafico non ha ancora un ruolo chiaro.

Esempio debole:

> “Questo mostra le vendite per paese.”

Esempio forte:

> “Questo mostra che la Germania spiega circa due terzi del calo europeo, mentre gli altri mercati sono sostanzialmente stabili.”

La seconda formulazione contiene una tesi verificabile.

## Separare evidenza e interpretazione

Un grafico dovrebbe aiutare il pubblico a vedere l'evidenza.

L'annotazione o il testo dovrebbe aiutare a capire l'interpretazione.

Non dobbiamo nascondere il dato dietro la narrativa.

Ma nemmeno obbligare il pubblico a ricostruire da solo il messaggio.

**Una visualizzazione esplicativa non mostra tutto ciò che sappiamo. Mostra ciò che serve per capire la decisione.**
