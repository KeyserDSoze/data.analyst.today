# Capitolo 6 — Segmentazione, coorti e lifecycle analysis

> **Un KPI aggregato ci dice come sta il portafoglio. Il lifecycle ci dice dove si sta costruendo o distruggendo il futuro del portafoglio.**

Nei capitoli precedenti abbiamo imparato a formulare la domanda, verificare il dato, esplorare la struttura osservata e quantificare l'incertezza. Ora aggiungiamo una dimensione che cambia il modo in cui leggiamo clienti e utenti: **la posizione nel percorso**.

Un cliente appena acquisito, uno che ha appena scoperto il primo valore del prodotto, uno che lo usa da tre anni, uno che sta riducendo l'attività e uno che torna dopo sei mesi non sono cinque righe equivalenti della stessa tabella. Sono cinque stati differenti della relazione con il prodotto, con aspettative, rischi e decisioni differenti.

## 6.0 Da una fotografia a una traiettoria

Supponiamo che una società subscription presenti tre numeri rassicuranti: customer base **+18%**, revenue **+22%**, churn mensile stabile al **3,4%**. La fotografia è positiva. Ma la stessa azienda può avere, contemporaneamente, retention M6 delle nuove coorti in discesa dal **74% al 58%**, un time-to-value raddoppiato, crescita di revenue sostenuta soprattutto da espansioni dei clienti storici e una nuova campagna che porta molti clienti destinati ad abbandonare nei primi novanta giorni.

I KPI aggregati non sono falsi. Stanno semplicemente mescolando generazioni di clienti che si trovano in punti diversi del percorso. La base storica, ancora forte, può mantenere sano il presente mentre le nuove coorti stanno costruendo un futuro peggiore. Il lifecycle serve proprio a separare queste due cose.

Segmentazione, coorti, funnel, activation, retention, churn, reactivation e LTV non sono quindi analisi indipendenti. Sono coordinate dello stesso sistema:

| Lente | Domanda |
|---|---|
| **Segmento** | *Chi* si comporta diversamente? |
| **Coorte** | *Quando* è entrato e come evolve a parità di età? |
| **Funnel** | *Dove* nel percorso si interrompe il movimento verso il valore? |
| **Retention / churn** | *Quanto a lungo* continua la relazione e come termina? |
| **Reactivation / LTV** | *Può tornare* e quanto valore produce lungo il ciclo? |

Nel Capitolo 4 usavamo la segmentazione per capire se un pattern aggregato cambiasse dentro sottogruppi rilevanti. Qui il criterio diventa più esigente: un segmento interessa quando rivela una traiettoria abbastanza diversa da cambiare diagnosi, priorità o intervento. Non divideremo quindi la popolazione perché esistono colonne come `country`, `device` o `plan`; la divideremo quando quella distinzione modifica il modo in cui il lifecycle va interpretato.

Il Capitolo 5 aggiunge un secondo vincolo. Più incrociamo segmenti, coorti e finestre temporali, più i denominatori si assottigliano. Una retention del 42% su quaranta utenti non ha la stessa precisione dello stesso 42% su quarantamila. Per questo ogni heatmap o curva deve portarsi dietro definizione, denominatore e un livello di incertezza coerente con la decisione. Una cella rossa non diventa evidenza forte perché il colore è intenso.

## Un caso reale: Duolingo guarda la relazione, non soltanto la base utenti

Nel materiale per gli investitori relativo al 2024, **Duolingo** descrive engagement e user retention come leve centrali della propria strategia di prodotto. Nel Q4 2024 il rapporto DAU/MAU è salito di oltre quattro punti anno su anno fino al **34,7%**, mentre oltre **10 milioni di utenti** mantenevano streak di almeno un anno. Lo stesso documento attribuisce l'aumento di engagement e retention a un insieme di nuove funzionalità e iniziative di prodotto, non a una singola feature.[^duolingo-2024]

Il valore del caso non è dimostrare una specifica causalità. È mostrare come un prodotto digitale di grande scala non osservi soltanto quanti utenti possiede, ma **quanto spesso tornano, quanto a lungo persistono e quanto profondamente il prodotto entra nel loro comportamento**. Sono le stesse dimensioni che useremo nel capitolo.

## La Lifecycle Diagnostic Map

Il deliverable finale sarà una **Lifecycle Diagnostic Map**. La sua funzione è trasformare un KPI iniziale in una diagnosi che separi ciò che vediamo, ciò che riteniamo plausibile e ciò che richiede un metodo più forte.

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

La mappa è utile quando ci porta da una frase generica come “dobbiamo migliorare la retention” a una diagnosi del tipo:

> **Il deterioramento è concentrato nelle coorti SMB acquisite da paid search dopo il nuovo onboarding; il gap nasce prima della prima azione di valore e si amplifica nei primi sessanta giorni.**

Questa frase non dimostra ancora una causa. Ma restringe il problema, collega il comportamento a un punto del percorso e rende esplicito quale evidenza manca.

> **Lifecycle analysis significa trasformare una base clienti in una sequenza di stati, transizioni e valore nel tempo.**

[^duolingo-2024]: Duolingo, *Q4/FY 2024 Shareholder Letter / Form 8-K*, 27 febbraio 2025: https://www.sec.gov/Archives/edgar/data/1562088/000156208825000039/q4fy24duolingo12-31x24shar.htm
