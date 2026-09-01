## 3.16 Data Readiness Review: pronto, pronto con caveat o non pronto?

Una checklist è utile solo se conduce a una decisione.

Prima di iniziare l'analisi vera e propria, raccogliamo quindi le verifiche del capitolo in una **Data Readiness Review**.

L'obiettivo non è certificare che il dataset sia perfetto. È stabilire se le proprietà che contano per l'Analytical Brief sono comprese e sufficientemente affidabili.

### 1. Rappresentazione

- Una riga rappresenta esattamente che cosa?
- Qual è il grain dichiarato?
- Il grain osservato coincide con quello dichiarato?
- Quali misure sono additive a questo livello?
- Esistono record che rappresentano versioni, eventi o rettifiche invece di entità distinte?

### 2. Identità

- Qual è la chiave attesa?
- È realmente unica nel perimetro corretto?
- L'identificatore rappresenta persona, account, contratto o altro?
- Può cambiare nel tempo?
- Esistono false split o false merge plausibili?
- Le relazioni principali producono record orfani?

### 3. Tempo

- Il dataset descrive eventi, stati o snapshot?
- Quale timestamp risponde alla domanda di business?
- Quale timezone viene usata?
- Esistono late-arriving data o backfill?
- Quando un periodo può considerarsi sufficientemente completo?
- Le definizioni temporali sono rimaste stabili?

### 4. Completezza e popolazione

- Sono presenti tutti i periodi attesi?
- Mancano interi segmenti, canali, regioni o sorgenti?
- I null sono concentrati in popolazioni specifiche?
- Esistono codici sentinella che nascondono missing?
- Una trasformazione potrebbe aver escluso record legittimi?

### 5. Validità e plausibilità

- Minimi e massimi hanno senso?
- Tipi, unità e domini sono espliciti?
- Esistono valori impossibili?
- Gli outlier più influenti sono stati investigati?
- Le categorie sono coerenti tra sistemi e periodi?

### 6. Provenienza

- Qual è la sorgente primaria?
- Quali trasformazioni critiche separano la sorgente dal dataset?
- Esistono filtri o deduplicazioni implicite?
- La logica può essere corretta retroattivamente?
- Chi conosce o possiede la definizione?

### 7. Riconciliazione

- Totali e cardinalità tornano con almeno una fonte indipendente?
- Le differenze residue sono spiegate?
- È definita una tolleranza accettabile?
- Sappiamo quale fonte è autorevole per ciascun uso?

### 8. Impatto sulla decisione

Questa è la parte che distingue il controllo del dato dalla semplice pulizia.

Per ogni issue importante chiedi:

> **Se questo problema fosse peggiore di quanto pensiamo, quale conclusione potrebbe cambiare?**

E poi:

> **Quanto deve essere affidabile questa proprietà per il rischio della decisione che stiamo supportando?**

Una mancanza del 5% può essere irrilevante per una metrica aggregata e inaccettabile se riguarda proprio il segmento su cui dobbiamo intervenire.

### Il verdetto

Alla fine della review assegna uno stato esplicito.

**PRONTO**

Le proprietà critiche sono comprese, i controlli sono coerenti e le limitazioni residue non compromettono la domanda.

**PRONTO CON CAVEAT**

Il dato può essere usato, ma soltanto entro limiti documentati.

Esempi:

- escludere le ultime 24 ore per latenza;
- non confrontare periodi precedenti a una migrazione;
- evitare una segmentazione con missing non casuali;
- riportare una sensibilità rispetto a una regola di deduplica.

**NON PRONTO**

Esiste un'incertezza sul dato abbastanza grande da rendere non difendibile la conclusione.

In questo caso il deliverable dell'analista può essere proprio la diagnosi del problema e il piano necessario per rendere il dato utilizzabile.

### Caso simulato — il Black Friday confrontato con il giorno sbagliato

Un analyst prepara un report sul Black Friday. Query, importi e conteggi sono corretti.

Durante la review emerge però che il confronto anno su anno usa gli stessi numeri di giorno del mese invece di allineare l'effettivo evento promozionale, che cadeva in date differenti.

Il dataset è tecnicamente sano.

Il confronto non è fit for purpose.

Questo ricorda un punto decisivo:

> **Data readiness non significa soltanto "il dato non è corrotto". Significa "il dato, così definito e confrontato, è adatto alla domanda".**

La review chiude il ponte tra Capitolo 2 e Capitolo 3:

**Analytical Brief → Data Readiness Review → Analisi**

Quando questi primi due artefatti sono solidi, tutto ciò che viene dopo diventa più veloce e soprattutto più difendibile.