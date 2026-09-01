## 4.19 Caso end-to-end — Una crescita vera, ma molto meno semplice di quanto sembra

> **Caso simulato/composito.** Azienda, numeri e circostanze sono costruiti a fini didattici.

Il management di **MercatoHub**, marketplace europeo di elettronica ricondizionata, riceve il report del secondo trimestre:

- GMV: **+18,7% YoY**;
- ordini: **+12,1%**;
- average order value: **+5,9%**;
- clienti attivi: **+9,4%**.

La prima slide preparata per il management titola:

> **La crescita sta accelerando.**

I numeri sono corretti. La conclusione, però, contiene molta più informazione di quanta ne abbiano dimostrata i quattro KPI.

La domanda analitica diventa quindi:

> **La crescita è ampia, sostenibile e accompagnata da segnali operativi coerenti, oppure è concentrata in pochi driver?**

### Handoff dal Capitolo 3: il dataset è utilizzabile

La Data Readiness Review è già stata completata. Grain, chiavi, ordini duplicati, resi e copertura temporale sono stati verificati.

Resta un caveat noto: la definizione storica di `active_customer` è stata alterata dal lancio della nuova app. Per questo nell'EDA useremo anche `unique_buyers`, definito in modo coerente su entrambi gli anni.

Questo confine è importante. Non stiamo rifacendo la data-quality review. Stiamo esplorando un dataset che sappiamo **come** usare e con quali caveat.

### Passo 1 — Guardare la distribuzione, non solo l'AOV

L'AOV passa da 286 € a 303 €.

La mediana racconta però un movimento molto più piccolo:

- P50: 231 € → 234 €;
- P90: 612 € → 735 €.

Il cliente al centro della distribuzione spende quasi quanto l'anno precedente. L'aumento medio è trainato soprattutto dalla parte alta della distribuzione.

L'osservazione cambia da:

> “Gli ordini valgono mediamente di più.”

A:

> **“È cresciuto soprattutto il peso degli ordini ad alto valore.”**

La seconda frase è più precisa e suggerisce subito la domanda successiva: *quali ordini?*

### Passo 2 — Scomporre la crescita per categoria

| Categoria | GMV YoY |
|---|---:|
| Smartphone | +6% |
| Laptop | +11% |
| Tablet | +4% |
| Fotografia | +9% |
| Gaming GPU | +71% |

La categoria Gaming GPU genera il **46% dell'incremento assoluto di GMV**, pur rappresentando meno del 15% del business nel periodo precedente.

La crescita complessiva è quindi reale, ma non è uniformemente distribuita nel catalogo.

Questo non rende il risultato peggiore. Lo rende **più concentrato**.

### Passo 3 — Controllare il denominatore della crescita clienti

`active_customer` cresce del 9,4%, ma la definizione include chiunque abbia effettuato almeno una visita autenticata negli ultimi 90 giorni.

Con la nuova app è diventato necessario fare login per salvare un prodotto nei preferiti. L'attività autenticata è quindi aumentata anche per una modifica del comportamento richiesto dall'interfaccia.

Gli **acquirenti unici**, definiti in modo stabile, crescono invece del **4,1%**.

Entrambi i numeri sono veri:

- utenti autenticati attivi: +9,4%;
- persone/account che hanno acquistato: +4,1%.

Ma supportano interpretazioni diverse.

Dire “la base clienti cresce del 9,4%” sarebbe troppo ambiguo per una decisione di investimento.

### Passo 4 — Guardare la concentrazione tra seller

Il marketplace ha 1.840 seller attivi.

La mediana del GMV per seller è quasi invariata. Il top 5% cresce invece del 38%.

Il box plot e la distribuzione per decile mostrano che una quota crescente del GMV è prodotta dai seller più grandi, molti dei quali vendono proprio GPU e hardware premium.

Ora abbiamo due concentrazioni che si sovrappongono:

- concentrazione per categoria;
- concentrazione per seller.

Un KPI aggregato di crescita non rendeva visibile nessuna delle due.

### Passo 5 — Trattare i tassi come definizioni complete

Il vecchio report indica un return rate del 7,8%; il nuovo dashboard mostra 7,1%.

Il confronto sembra positivo, ma le due versioni usano denominatori differenti:

- storico: **ordini con almeno un reso / ordini consegnati**;
- nuovo: **unità restituite / unità spedite**.

Non sono la stessa metrica.

L'analista ricostruisce la serie usando una definizione coerente, `ordini con almeno un reso / ordini consegnati`, per entrambi i periodi.

Il risultato è:

- anno precedente: **7,8%**;
- anno corrente: **8,3%**.

Per la categoria GPU il tasso passa dall'11,2% al 12,8%.

La storia non è più “crescita con qualità in miglioramento”, ma:

> **crescita concentrata in una categoria che mostra anche un'esperienza post-vendita più problematica.**

Questa è ancora descrizione, non spiegazione causale.

### Passo 6 — Misurare quanto il risultato dipende da pochi giorni

Tre giornate hanno GMV eccezionalmente alto. Corrispondono al lancio di una GPU molto richiesta e sono eventi commerciali reali.

Non vanno cancellate come errori.

Ma possiamo chiedere quanto influenzino la conclusione.

Sensitivity analysis:

- GMV YoY con tutti i giorni: **+18,7%**;
- GMV YoY escludendo i tre giorni di lancio: **+12,6%**.

La crescita resta forte. Quindi il risultato non dipende interamente da tre osservazioni.

Tuttavia circa un terzo dell'accelerazione apparente rispetto alla crescita “core” è associata a un evento molto concentrato.

Questa è informazione decisionale importante.

### Passo 7 — Costruire l'EDA Evidence Map

A questo punto l'analista non scrive ancora una spiegazione unica. Organizza ciò che l'EDA ha realmente stabilito.

| Livello | Evidenza |
|---|---|
| **Osservato** | GMV +18,7%; ordini +12,1%; unique buyers +4,1%. |
| **Struttura** | Crescita fortemente concentrata su GPU, ordini high-value e top seller. |
| **Robustezza** | Senza tre launch days il GMV resta +12,6% YoY. |
| **Segnale operativo** | Return rate coerentemente definito peggiora 7,8% → 8,3%; GPU 11,2% → 12,8%. |
| **Ipotesi** | Nuova domanda GPU, mix premium e concentrazione seller possono spiegare gran parte dell'accelerazione. |
| **Non dimostrato** | Che il marketing abbia causato la crescita; che il boom GPU sia persistente; che la maggiore concentrazione sia economicamente negativa. |
| **Prossimo passo** | Analizzare contribution margin, repeat buyers, acquisizione per canale e persistenza delle coorti GPU. |

Questa tabella è il vero output dell'EDA.

### Dalla headline alla conclusione difendibile

La headline iniziale era:

> **La crescita sta accelerando.**

Dopo l'EDA diventa:

> **Il GMV cresce del 18,7% YoY e la crescita resta solida (+12,6%) anche escludendo i tre principali giorni di lancio. L'accelerazione è però concentrata nella categoria Gaming GPU, negli ordini di fascia alta e nei seller maggiori. Gli acquirenti unici crescono del 4,1%, molto meno della precedente metrica di “active customer”. Inoltre, usando una definizione comparabile, il return rate peggiora dal 7,8% all'8,3%. La crescita è quindi reale, ma meno diffusa e accompagnata da rischi di concentrazione e post-vendita che richiedono analisi ulteriori prima di aumentare indiscriminatamente gli investimenti.**

È una conclusione più lunga, ma soprattutto è **calibrata sull'evidenza**.

### Decisione

Il management non approva automaticamente un aumento generalizzato del budget marketing del 25%.

Decide invece di:

1. separare nei report crescita core e contributo delle categorie ad alta volatilità;
2. monitorare concentrazione seller, contribution margin e return rate della GPU;
3. utilizzare `unique_buyers` come metrica stabile della crescita della base acquirenti;
4. verificare nei mesi successivi se la domanda GPU produce repeat purchase e margine sostenibile;
5. progettare test mirati prima di attribuire l'accelerazione a uno specifico canale marketing.

Il valore dell'EDA non è stato trovare una frase più pessimista.

È stato trasformare:

> **un aggregato corretto**

in:

> **una descrizione della struttura abbastanza precisa da sapere quali spiegazioni meritano di essere testate.**
