## 4.13 L'output dell'EDA: una mappa dell'evidenza, non una cartella di grafici

Una buona EDA può produrre decine di tabelle e visualizzazioni durante il lavoro.

Il deliverable finale non dovrebbe conservarle tutte.

Dovrebbe conservare **la struttura dell'evidenza** emersa dall'esplorazione.

Un modo utile è costruire una **EDA Evidence Map** con cinque blocchi:

1. fenomeno osservato;
2. concentrazione e composizione;
3. robustezza;
4. ipotesi candidate;
5. prossimo metodo necessario.

### 1. Fenomeno osservato

Scrivi il cambiamento principale in modo quantitativo e con la baseline esplicita.

Esempio:

> Il churn mensile è passato dal 6,2% all'8,1% negli ultimi quattro mesi, +1,9 pp rispetto alla media dei sei mesi precedenti.

Non ancora:

> Il nuovo onboarding sta facendo aumentare il churn.

La seconda frase appartiene a un livello di evidenza diverso.

### 2. Concentrazione e composizione

Dove vive il fenomeno?

- quali segmenti contribuiscono di più al delta?
- il movimento è generalizzato o localizzato?
- cambia il mix della popolazione?
- numeratore e denominatore si muovono nello stesso modo?
- media e percentili raccontano la stessa storia?

Esempio:

> Circa il 72% dell'aumento assoluto di churn proviene da SMB con meno di sei mesi di tenure; Enterprise è stabile.

Questa frase restringe il problema senza pretendere di averne trovato la causa.

### 3. Robustezza

Ogni pattern importante dovrebbe essere accompagnato da almeno un controllo di sensibilità.

Domande utili:

- resta visibile usando mediana invece della media?
- cambia se escludiamo un periodo eccezionale, mantenendolo comunque documentato?
- sopravvive alla segmentazione per una dimensione plausibile?
- dipende da uno o due punti influenti?
- è stabile con una baseline temporale alternativa sensata?
- cambia quando mostriamo tasso e volume insieme?

Possiamo classificare informalmente il pattern come:

- **robusto**;
- **moderatamente sensibile**;
- **fragile**.

Non è un test statistico. È un modo per non dimenticare quanto la conclusione dipenda dalle scelte esplorative.

### 4. Ipotesi candidate e spiegazioni alternative

Una tabella semplice evita che le ipotesi diventino fatti per ripetizione:

| Pattern | Ipotesi candidata | Alternativa plausibile | Evidenza mancante |
|---|---|---|---|
| churn alto nei nuovi SMB | onboarding insufficiente | acquisition mix | completion e canale |
| P95 delivery alto nel weekend | capacity insufficiente | mix geografico | volume per zona |
| AOV alto nel social | effetto canale | product mix premium | confronto a mix costante |

L'EDA è molto utile proprio quando mantiene aperte spiegazioni concorrenti.

### 5. Prossimo metodo

Alla fine dobbiamo sapere che cosa non può più essere risolto con un altro grafico.

Possibili prossimi passi:

- statistica inferenziale;
- raccolta di nuovi dati;
- analisi di coorte;
- modello predittivo;
- esperimento;
- metodo causale;
- approfondimento temporale;
- nessun ulteriore lavoro, se l'evidenza è già sufficiente per la decisione descrittiva.

### Template operativo

```text
Domanda:

Fatto principale:

Baseline:

Distribuzione:

Segmenti che spiegano il delta:

Composizione / denominatori rilevanti:

Pattern principali:

Sensitivity checks:

Pattern robusti:

Pattern fragili:

Ipotesi candidate:

Spiegazioni alternative:

Cosa NON è dimostrato:

Prossimo metodo / decisione:
```

### Caso breve

Invece di consegnare:

> Correlazione ticket-churn = 0,54.

l'EDA può produrre:

> Il churn è aumentato dal 6,2% all'8,1%, quasi interamente nei nuovi SMB. In quel gruppo i clienti che aprono almeno tre ticket nei primi 30 giorni mostrano churn più elevato. La relazione resta visibile per canale ma si riduce molto controllando per product tier. Non sappiamo se i ticket siano causa del churn, sintomo di problemi di prodotto o entrambe le cose. Il prossimo passo è distinguere categorie ticket e sequenza temporale, poi valutare un disegno causale se vogliamo decidere un intervento.

Questa è già una rappresentazione analitica molto più utile.

### Una checklist finale, ma non quella del Capitolo 3

Prima di chiudere l'EDA chiediti:

- ho descritto centro, dispersione e forma dove servono?
- ho mostrato volumi e denominatori?
- ho controllato la composizione dei gruppi?
- ho guardato i grafici prima di fidarmi dei coefficienti?
- ho verificato pattern temporali plausibili?
- ho stressato gli insight principali?
- ho distinto fatti, ipotesi e causalità non dimostrata?
- so quale domanda viene dopo?

NIST descrive l'EDA come un approccio orientato alla scoperta della struttura e al controllo delle assunzioni, non come una procedura meccanica.[^nist-eda]

> **Una buona EDA riduce il numero di storie compatibili con i dati, ma non finge di aver identificato la storia causale definitiva.**

[^nist-eda]: NIST/SEMATECH, *Exploratory Data Analysis*. https://www.itl.nist.gov/div898/handbook/eda/eda_d.htm