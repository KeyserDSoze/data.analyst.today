## 4.4 Istogrammi e forma: vedere ciò che le statistiche comprimono

Media, mediana e percentili sono sintesi utili. Ma nessuna di queste statistiche, da sola, ci mostra **come** le osservazioni occupano lo spazio dei valori.

L'istogramma serve proprio a questo: divide la scala in intervalli e mostra quante osservazioni cadono in ciascuno.

NIST include gli istogrammi tra le tecniche fondamentali dell'EDA e mostra come forme differenti — simmetriche, asimmetriche, bimodali, a coda lunga — richiedano interpretazioni differenti.[^nist-hist]

### Caso simulato/composito — Lo scontrino medio che non descrive quasi nessuno

Una catena retail osserva un average basket value di **47,80 euro**.

Il management immagina un cliente tipico che spende circa 50 euro.

L'istogramma mostra invece due concentrazioni:

- molti acquisti tra 15 e 30 euro;
- un secondo gruppo tra 75 e 110 euro.

La distribuzione è **bimodale**.

Approfondendo, emerge che il primo gruppo acquista soprattutto prodotti di consumo ricorrente, mentre il secondo compra bundle e linee premium.

La media è corretta come rapporto tra ricavi e numero di ordini. Ma descrive male entrambi i comportamenti.

La forma della distribuzione suggerisce quindi una nuova domanda:

> stiamo osservando una popolazione unica o due processi di acquisto differenti mescolati insieme?

### Forme che vale la pena riconoscere

**Simmetrica**

Media e mediana tendono a essere vicine e le code sono relativamente bilanciate.

**Asimmetrica a destra**

Molte osservazioni piccole o moderate e pochi valori molto grandi. Ricavi per cliente, importi di ordine e durata di ticket spesso hanno questa forma.

**Asimmetrica a sinistra**

La coda più lunga si trova verso i valori bassi.

**Bimodale o multimodale**

Più picchi possono indicare segmenti, regimi o processi differenti.

**Troncata**

La distribuzione sembra interrompersi artificialmente. Potrebbe esistere una soglia di processo, una regola di censura o un limite di misurazione.

**Heaping**

Le osservazioni si accumulano su valori tondi o preferiti.

### Heaping: quando la distribuzione racconta come è stato raccolto il dato

In una survey interna molti dipendenti dichiarano di lavorare esattamente 40, 45 o 50 ore settimanali.

Non dobbiamo concludere automaticamente che gli orari reali siano così discretizzati.

Potrebbe esserci arrotondamento mentale.

La distribuzione sta quindi descrivendo contemporaneamente:

- il fenomeno;
- il modo in cui il fenomeno è stato misurato o ricordato.

La Data Readiness Review del Capitolo 3 ci aiuta a distinguere i problemi noti di misurazione; l'EDA può far emergere strutture che non avevamo anticipato.

### I bin sono una scelta analitica

Lo stesso dataset può apparire molto diverso con intervalli differenti.

Bin troppo larghi possono cancellare bimodalità e code. Bin troppo stretti possono trasformare il rumore campionario in una sequenza di picchi apparentemente significativi.

Per questo non dovremmo interpretare una forma senza verificare che sia ragionevolmente stabile rispetto a scelte sensate dei bin.

### Non usare l'istogramma come test di normalità

L'istogramma aiuta a vedere asimmetria, code e modalità, ma non deve diventare un rituale del tipo:

> "se non sembra una campana, il dato è sbagliato".

Molti fenomeni di business non sono affatto normali e non hanno alcun motivo per esserlo.

Il compito dell'EDA è descrivere la struttura osservata, non forzarla verso una forma desiderata.

### Dalla forma alla prossima domanda

Una distribuzione interessante dovrebbe generare domande come:

- quali segmenti producono i diversi picchi?
- la coda dipende da pochi clienti o da un'intera categoria?
- il limite osservato deriva da una regola del processo?
- la forma è stabile nel tempo?
- media e mediana stanno raccontando esperienze diverse?

> **La distribuzione è il fenomeno. Le statistiche descrittive sono viste parziali della distribuzione.**

[^nist-hist]: NIST/SEMATECH, *Histogram*. https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm