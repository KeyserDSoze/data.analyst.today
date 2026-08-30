## 4.3 Percentili, code e livelli di servizio

Le medie sono spesso insufficienti quando il problema riguarda l'esperienza peggiore di una parte degli utenti.

È il caso di tempi di risposta, latenza, consegne, attese, ticket di assistenza e processi industriali.

### Caso: il customer care sembra veloce

Un'azienda SaaS dichiara un tempo medio di prima risposta ai ticket di 2 ore e 14 minuti.

Il dato sembra buono.

L'analista calcola però i percentili:

- P50: 47 minuti;
- P75: 2 ore e 5 minuti;
- P90: 7 ore e 42 minuti;
- P95: 15 ore e 18 minuti;
- P99: 41 ore.

La maggioranza dei clienti riceve una risposta rapidamente, ma una minoranza rilevante attende quasi un giorno.

Quando i ticket vengono segmentati per piano commerciale emerge che il problema è concentrato nel piano Basic durante il weekend.

Il dato medio non era falso. Era troppo aggregato per mostrare il problema operativo.

### Perché le code contano

In molti sistemi la qualità percepita non è determinata dal comportamento medio, ma dai casi peggiori.

Un sito può avere una latenza media di 350 millisecondi, ma se il P99 supera 8 secondi una parte degli utenti vivrà un'esperienza fortemente negativa.

Un corriere può consegnare mediamente in 2,4 giorni, ma se il 10% delle consegne arriva oltre una settimana il problema commerciale resta serio.

### Percentili e SLA

Gli SLA, Service Level Agreement, vengono spesso definiti in termini percentili o percentuali di casi entro una soglia.

Esempi:

- 95% dei ticket risposto entro 4 ore;
- 99% delle API call sotto 1 secondo;
- 97% delle consegne entro 48 ore.

L'analista deve quindi saper passare dal linguaggio statistico al linguaggio operativo.

### Errore frequente

Un errore comune è scegliere il percentile dopo aver visto i dati, soltanto perché produce una storia più favorevole.

La metrica deve essere legata alla decisione o al livello di servizio, non scelta opportunisticamente.
