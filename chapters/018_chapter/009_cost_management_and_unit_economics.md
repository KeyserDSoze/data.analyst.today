## 18.8 Cost management: scalare senza perdere il controllo economico
Una piattaforma analitica può diventare tecnicamente più sofisticata e contemporaneamente economicamente peggiore.

Query più frequenti, refresh più aggressivi, copie ridondanti, modelli sovradimensionati, notebook sempre accesi e pipeline streaming dove sarebbe sufficiente il batch possono far crescere i costi senza creare valore proporzionale.

Il problema non è “spendere meno”.

È capire se il costo cresce insieme al valore prodotto.

## Dal costo totale al costo per unità di valore

La logica FinOps suggerisce di collegare costo e utilizzo a una unità di business: una transazione, un cliente, un ordine, una previsione, una raccomandazione, un milione di righe elaborate.

Microsoft definisce la unit economics come il processo di calcolare il costo di una singola unità di business e collegarlo al valore generato dal cloud.

Per un sistema analitico potremmo misurare:

- costo per dashboard refresh;
- costo per mille query;
- costo per pipeline eseguita;
- costo per cliente servito da un modello;
- costo per decisione automatizzata;
- costo per forecast prodotto.

## Caso realistico: dashboard “gratuita” da €31.000 al mese

Un marketplace costruisce una dashboard executive molto usata.

Nel tempo vengono aggiunti:

- refresh ogni 10 minuti;
- 34 visualizzazioni;
- query non aggregate su due anni di eventi;
- copie separate per cinque regioni;
- calcoli ripetuti in ogni report.

Il costo mensile della piattaforma cresce fino a circa €31.000.

La reazione iniziale è comprare più capacità.

Una revisione mostra invece che:

- il CEO consulta il report una volta al giorno;
- solo due metriche richiedono freshness inferiore all'ora;
- l'80% delle query ripete aggregazioni identiche;
- cinque semantic model regionali potrebbero essere uno solo con policy di accesso.

La soluzione non è “ottimizzare il cloud”.

È riallineare architettura, frequenza e dettaglio al bisogno decisionale.

Il costo scende, ma soprattutto aumenta la chiarezza del sistema.

## Cost visibility e accountability

Per gestire i costi servono almeno:

- allocazione per team/prodotto;
- tagging coerente;
- reporting sui principali driver;
- anomaly detection sui costi;
- budget e alert;
- owner identificabile.

La documentazione FinOps di Microsoft insiste proprio su ingestion, allocation, reporting, anomaly management e unit economics come capacità collegate.

## Non ottimizzare ciò che crea valore

Un errore opposto è tagliare costi indiscriminatamente.

Se un forecast da €2.000 al mese evita stock-out da €400.000, ridurre la frequenza per risparmiare €700 può essere una falsa economia.

Per questo una metrica utile è:

**Cost per unit of analytical value**

Non sarà sempre perfettamente misurabile, ma costringe a porre la domanda corretta.

> **Un sistema analitico sostenibile non è quello che costa poco. È quello in cui sappiamo spiegare perché costa ciò che costa e quale valore quel costo rende possibile.**

## Fonti

- Microsoft FinOps documentation: https://learn.microsoft.com/en-us/cloud-computing/finops/
- Microsoft Unit economics: https://learn.microsoft.com/en-us/cloud-computing/finops/framework/quantify/unit-economics
