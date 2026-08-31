# 19.1 Cosa diventa commodity e cosa aumenta di valore

L’AI tende a comprimere il valore economico delle attività che hanno tre caratteristiche:

1. input relativamente chiari;
2. output verificabile rapidamente;
3. procedura standardizzabile.

Molti task analitici rientrano almeno in parte in questa categoria.

## Attività che diventano più economiche

Tra le attività sempre più assistibili o automatizzabili troviamo:

- generazione di SQL standard;
- traduzione tra SQL dialect;
- formule di foglio elettronico;
- boilerplate Python;
- grafici di base;
- documentazione tecnica iniziale;
- profiling esplorativo;
- riassunti di dashboard;
- conversione di requisiti in query candidate;
- ricerca di errori sintattici;
- refactoring semplice;
- generazione di test iniziali;
- preparazione di una prima bozza di presentazione.

Questo non significa che tali attività non servano più.

Significa che diventano meno rare.

E quando una capacità diventa meno rara, da sola tende a differenziare meno.

## Caso realistico: la query che prima richiedeva due ore

Un analyst deve calcolare la repeat purchase rate a 90 giorni per paese e canale.

In passato potrebbe aver impiegato due ore per:

- capire le tabelle;
- ricordare la sintassi delle window function;
- scrivere la query;
- correggere errori;
- documentare il risultato.

Con un buon semantic context e un assistente AI, una prima versione può arrivare in pochi minuti.

Il lavoro difficile però resta.

L’analista deve ancora decidere:

- la coorte è definita sul primo ordine o sul primo ordine pagato?
- i resi annullano l’acquisto?
- i clienti guest vengono riconciliati?
- i 90 giorni sono rolling o calendario?
- il denominatore include clienti che non hanno ancora avuto 90 giorni di osservazione?
- il canale è quello di acquisizione o quello del repeat order?

La sintassi è diventata economica.

La semantica no.

## Le competenze che salgono di valore

Quando produrre output diventa più facile, aumenta il valore delle competenze che determinano se quell’output merita fiducia.

### Problem framing

Trasformare una domanda vaga in un problema analitico ben definito.

### Business understanding

Capire economia, processi, vincoli e incentivi dell’organizzazione.

### Semantica

Sapere cosa significa realmente una metrica, un evento, un’entità, una coorte.

### Data judgment

Capire quando il dato è incompleto, distorto, obsoleto o non comparabile.

### Causal reasoning

Distinguere associazione, previsione e intervento.

### Decision analysis

Collegare evidenza, costi, rischi, trade-off e azione.

### Verification

Sapere come mettere alla prova un risultato, anche quando è stato prodotto da un agente.

### Communication

Presentare il problema al livello di dettaglio corretto per chi deve decidere.

### System thinking

Capire dipendenze tra metriche, processi, incentivi, sistemi e comportamento umano.

## Una matrice utile

Possiamo pensare alle competenze lungo due dimensioni:

- facilità di automazione;
- valore della responsabilità associata.

| Attività | Automazione potenziale | Responsabilità decisionale |
|---|---:|---:|
| scrivere una query standard | alta | bassa-media |
| scegliere la definizione di churn | bassa | alta |
| produrre un grafico | alta | media |
| decidere cosa mostrare al CEO | media | alta |
| fare profiling di una tabella | alta | media |
| stabilire se manca un segmento critico | media | alta |
| generare un forecast | alta | media |
| decidere se il forecast è utilizzabile per inventory planning | bassa-media | alta |
| creare un modello churn | alta | media |
| decidere su chi intervenire e con quale trattamento | bassa | molto alta |

La carriera resiliente tende a spostarsi verso la parte destra della tabella.

## Il rischio opposto: pensare che la tecnica non serva più

Sarebbe però un errore concludere:

> “Se l’AI scrive SQL, non devo più capire SQL.”

Per poter verificare un sistema bisogna comprenderne abbastanza il funzionamento.

Un analyst che non capisce join, grain, leakage, baseline o confidence interval non diventa più strategico usando l’AI.

Diventa più dipendente dall’output che riceve.

La tecnica quindi non scompare.

Cambia funzione.

Da competenza puramente esecutiva diventa anche **competenza di controllo**.

> **Non serve essere il più veloce a scrivere ogni riga. Serve capire abbastanza bene il sistema da riconoscere quando quella riga porta nella direzione sbagliata.**
