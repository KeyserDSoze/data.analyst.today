# Come usare questo libro

Questo libro non è un catalogo di strumenti e non richiede di applicare ogni tecnica a ogni problema. È costruito attorno a una domanda più stabile:

> **Quale evidenza serve per prendere una decisione migliore, con un livello di affidabilità proporzionato al costo dell'errore?**

Il percorso segue il lavoro reale del Data Analyst: parte da domande ambigue, attraversa dati imperfetti, statistica, comportamento, tempo, causalità, modelli, sistemi e comunicazione, e arriva alla responsabilità di decidere che cosa possiamo sostenere, che cosa resta incerto e quali capacità meritano di diventare ricorrenti.

## Lettura sequenziale

La lettura dall'inizio alla fine è consigliata a chi vuole costruire un modello mentale completo. La progressione è:

```text
mentalità
→ domanda
→ dati
→ statistica
→ comportamento
→ tempo
→ causalità
→ esperimenti
→ modelli
→ semantica/SQL
→ architettura
→ strumenti
→ AI
→ decisione
→ comunicazione
→ casi end-to-end
→ sistema operativo dell'analytics
→ futuro professionale
```

Ogni passaggio introduce un nuovo failure mode da governare. La tecnica arriva dopo la decisione che deve supportare, non prima.

## Lettura per problema

Chi usa il libro come riferimento può entrare direttamente dal problema che deve risolvere.

- domanda business ancora vaga → Capitolo 2;
- dubbio sulla qualità o utilizzabilità del dato → Capitolo 3;
- esplorazione e struttura osservata → Capitolo 4;
- incertezza e inferenza → Capitolo 5;
- funnel, retention e lifecycle → Capitolo 6;
- serie temporali e forecast → Capitolo 7;
- claim causali → Capitolo 8;
- esperimenti → Capitolo 9;
- modelli predittivi → Capitolo 10;
- SQL, grain e semantica → Capitolo 11;
- architettura e affidabilità del flusso → Capitolo 12;
- scelta degli strumenti → Capitolo 13;
- workflow AI-assisted → Capitolo 14;
- decisione e trade-off → Capitolo 15;
- comunicazione e dashboard → Capitolo 16;
- casi end-to-end → Capitolo 17;
- analytics come servizio operativo → Capitolo 18;
- skill, seniority e carriera nell'era dell'AI → Capitolo 19.

## Gli artefatti operativi

Il libro introduce un vocabolario di deliverable riutilizzabili:

```text
Analytical Brief
Data Readiness Review
EDA Evidence Map
Uncertainty Brief
Lifecycle Diagnostic Map
Temporal Decision Brief
Causal Identification Brief
Experiment Contract
Predictive Decision Card
Analytical Data Contract
Data Flow Architecture Map
Tooling Decision Record
AI Analysis Control Sheet
Decision Record
Decision Communication Pack
Capstone Routing Canvas
Analytics Operating Contract
Personal Career Operating Plan
```

Non sono una pipeline obbligatoria. Sono controlli da attivare quando il rischio corrispondente è materialmente rilevante. Un problema semplice può richiederne pochi; un problema ad alto impatto può richiederne diversi. Il **Capstone Routing Canvas** del Capitolo 17 rende esplicita proprio questa selezione; il Capitolo 18 decide quando un workflow merita di essere promosso a servizio operativo; il Capitolo 19 applica lo stesso principio alla crescita professionale.

## Come leggere gli esempi

Gli esempi non seguono una ricetta unica. Alcuni si fermano dopo una reconciliation o una decomposition perché l'evidenza è già sufficiente; altri devono arrivare a causalità, experimentation, rollout o operating model perché il failure cost richiede un claim più forte. Nei casi end-to-end, quindi, è importante osservare non soltanto **che cosa viene fatto**, ma anche **che cosa viene deliberatamente saltato e perché**.

Quando un'organizzazione o un evento reale viene nominato, il testo lo tratta come **caso reale documentato** e limita il claim a ciò che una fonte pubblica consente di sostenere. Quando numeri, organizzazioni o circostanze sono costruiti per la didattica, il caso è dichiarato **simulato/composito**.

## Come usare l'AI durante la lettura

L'AI può essere utile per spiegare un passaggio con un esempio diverso, generare esercizi, produrre query candidate, attaccare un'ipotesi con spiegazioni concorrenti o simulare una review critica. Il modo più utile di usarla non è ottenere una risposta più velocemente, ma aumentare la quantità di ipotesi e verifiche che riusciamo a esplorare senza perdere il controllo del metodo.

La regola del libro resta la stessa:

> **possiamo delegare esecuzione, esplorazione, prime bozze e parte della verifica; non possiamo delegare la responsabilità di capire ciò che consegniamo.**

L'obiettivo non è ricordare ogni formula o ogni sintassi. È costruire abbastanza competenza da sapere quale decisione stiamo realmente supportando, che cosa il dato significa, quale evidenza abbiamo, quali assunzioni stiamo facendo e quando fermarci prima di rafforzare troppo una conclusione.