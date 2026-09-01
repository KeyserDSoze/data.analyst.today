# Capitolo 6 — Segmentazione, coorti e lifecycle analysis

> **Un KPI aggregato ci dice come sta il portafoglio. Il lifecycle ci dice dove si sta costruendo o distruggendo il futuro del portafoglio.**

Nei capitoli precedenti abbiamo imparato a formulare la domanda, verificare il dato, esplorare la struttura osservata e quantificare l'incertezza.

Ora introduciamo una dimensione che cambia profondamente l'analisi di clienti e utenti: **la posizione nel percorso**.

Un cliente appena acquisito, uno che ha appena scoperto il primo valore del prodotto, uno che lo usa da tre anni, uno che sta riducendo l'attività e uno che è tornato dopo sei mesi non sono semplicemente cinque righe della stessa tabella.

Sono cinque **stati diversi della relazione con il prodotto**.

Questo capitolo serve a capire quella relazione.

## 6.0 Da una fotografia a una traiettoria

Supponiamo che una società subscription mostri:

- customer base: +18%;
- revenue: +22%;
- churn mensile: stabile al 3,4%.

La fotografia appare positiva.

Ma immaginiamo che, contemporaneamente:

- le nuove coorti abbiano retention M6 in discesa da 74% a 58%;
- il tempo per arrivare alla prima azione di valore sia raddoppiato;
- la crescita revenue provenga soprattutto da espansioni di clienti storici;
- una nuova campagna stia acquisendo molti clienti che abbandonano nei primi 90 giorni.

Il business oggi può ancora apparire sano perché porta con sé una grande base di clienti forti acquisiti nel passato.

Il lifecycle mostra invece che **la qualità del futuro sta peggiorando**.

È per questo che segmentazione, coorti, funnel, activation, retention e churn devono essere letti insieme.

### Cinque domande, cinque lenti

| Lente | Domanda |
|---|---|
| **Segmento** | *Chi* si comporta diversamente? |
| **Coorte** | *Quando* è entrato e come evolve a parità di età? |
| **Funnel** | *Dove* nel percorso si interrompe il movimento verso il valore? |
| **Retention / churn** | *Quanto a lungo* continua la relazione e come termina? |
| **Reactivation / LTV** | *Può tornare* e quanto valore produce lungo il ciclo? |

Non sono cinque analisi indipendenti.

Sono coordinate dello stesso sistema.

### Il confine con l'EDA

Nel Capitolo 4 abbiamo usato la segmentazione per chiedere:

> “Il pattern aggregato cambia se guardiamo sottogruppi rilevanti?”

Qui facciamo un passo ulteriore:

> **“Questi gruppi hanno traiettorie di acquisizione, activation, retention e valore abbastanza diverse da richiedere una strategia diversa?”**

Quindi non creeremo segmenti soltanto perché esiste una colonna `country`, `device` o `plan`.

Cercheremo segmenti che cambiano il modo in cui interpretiamo il **lifecycle**.

### Il confine con l'inferenza

Il Capitolo 5 ci ha ricordato che una percentuale su 40 utenti non ha la stessa precisione di una percentuale su 40.000.

Le cohort table sono particolarmente vulnerabili a questo problema: andando verso coorti, mesi e segmenti più piccoli, il denominatore si assottiglia rapidamente.

Per questo ogni heatmap o curva di retention deve conservare almeno tre cose:

- definizione;
- denominatore;
- incertezza proporzionata alla decisione.

Una cella rossa non diventa evidenza forte perché il colore è intenso.

## Caso reale documentato — Duolingo misura la salute attraverso engagement e retention

Nei materiali per gli investitori relativi al 2024, **Duolingo** descrive engagement e user retention come leve centrali della propria strategia di prodotto. L'azienda riporta che il rapporto DAU/MAU è salito di oltre quattro punti anno su anno fino al **34,7% nel Q4 2024** e che oltre **10 milioni di utenti** mantenevano streak di almeno un anno. Nello stesso documento Duolingo afferma di aver introdotto numerose funzionalità che hanno aumentato engagement e retention.[^duolingo-2024]

Questo non dimostra che una singola feature abbia causato la crescita complessiva: il documento stesso descrive molte iniziative di prodotto e marketing.

Il caso è utile per un'altra ragione.

Un'azienda digitale molto grande non osserva soltanto “quanti utenti abbiamo?”. Osserva **frequenza, persistenza e profondità della relazione nel tempo**.

Sono esattamente le dimensioni che costruiremo in questo capitolo.

## La Lifecycle Diagnostic Map

Il deliverable finale del capitolo sarà una **Lifecycle Diagnostic Map**.

La sua logica è:

```text
KPI AGGREGATO
Che cosa sembra stare cambiando?

SEGMENTO
Per chi cambia?

COORTE
Da quando e a quale età del cliente emerge la differenza?

FUNNEL / ACTIVATION
In quale passaggio verso il valore si apre il gap?

RETENTION / CHURN
Come si propaga il gap nel tempo?

REACTIVATION / ECONOMICS
Il cliente torna? Quanto valore perdiamo o recuperiamo?

INCERTEZZA
Quali celle o segmenti sono realmente informativi?

IPOTESI
Quale meccanismo potrebbe spiegare il pattern?

PROSSIMO METODO
Descrizione ulteriore, esperimento, causalità o modello predittivo?
```

È una catena diagnostica, non una formula.

L'obiettivo non è dire genericamente:

> “dobbiamo migliorare la retention”.

È arrivare a frasi del tipo:

> **“Il deterioramento è concentrato nelle coorti SMB acquisite da paid search dopo il nuovo onboarding; il gap nasce prima della prima azione di valore e si amplifica nei primi 60 giorni.”**

Quella frase non dimostra ancora una causa.

Ma restringe enormemente il problema e indica dove deve lavorare il team.

> **Lifecycle analysis significa trasformare una base clienti in una sequenza di stati, transizioni e valore nel tempo.**

[^duolingo-2024]: Duolingo, *Q4/FY 2024 Shareholder Letter / Form 8-K*, 27 febbraio 2025: https://investors.duolingo.com/static-files/d0adccff-bfe0-4d10-a5bc-f116d746afd2
