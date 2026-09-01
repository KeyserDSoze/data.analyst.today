## 4.5 Confrontare gruppi: composizione, denominatori e Simpson's paradox

Molte analisi iniziano con un confronto:

- clienti nuovi contro clienti esistenti;
- regione A contro regione B;
- prima contro dopo;
- campagna X contro campagna Y;
- piano mensile contro annuale.

Il confronto è potente perché crea un riferimento.

È anche pericoloso perché due gruppi possono differire in molti modi oltre alla caratteristica che stiamo osservando.

### Caso reale documentato — Le ammissioni graduate a Berkeley nel 1973

Uno degli esempi più noti del problema di composizione nasce dai dati di ammissione graduate della University of California, Berkeley.

Nei dati aggregati del 1973 risultavano:

| Gruppo | Applicant | Tasso di ammissione |
|---|---:|---:|
| Uomini | 8.442 | 44% |
| Donne | 4.321 | 35% |

Guardando soltanto il totale, il gap era netto e sembrava fornire forte evidenza di un processo sfavorevole alle donne.[^berkeley-simpson]

Bickel, Hammel e O'Connell analizzarono però il processo a livello di dipartimento. Le ammissioni graduate venivano decise dai singoli dipartimenti, che avevano tassi di selettività molto differenti. Inoltre uomini e donne non presentavano domanda con la stessa composizione tra i diversi campi di studio.

Nel materiale Berkeley che ricostruisce il lavoro originale, su 101 dipartimenti:

- 75 non mostravano bias statisticamente rilevato;
- 4 mostravano un risultato sfavorevole alle donne;
- 6 un risultato sfavorevole agli uomini;
- in 16 non era possibile il confronto perché non avevano candidate donne o non rifiutavano nessuno.[^berkeley-simpson]

Nei sei dipartimenti più grandi si vede bene il meccanismo: le donne presentavano domanda molto più frequentemente in dipartimenti con tassi di ammissione bassi, mentre gli uomini erano maggiormente rappresentati in alcuni dipartimenti meno selettivi.

Gli autori conclusero che il test applicato all'aggregato non rispettava una propria assunzione fondamentale e che, tenendo conto della diversa composizione per campo, non emergeva evidenza di bias contro le donne **nel processo di ammissione dipartimentale studiato**. Allo stesso tempo sottolinearono che la diversa distribuzione delle candidature tra discipline sollevava un problema sociale più ampio, che non poteva essere liquidato dalla sola analisi delle decisioni di ammissione.[^berkeley-simpson]

Questo è importante perché evita una lettura caricaturale del caso.

La lezione non è:

> "segmentare elimina sempre il problema".

È:

> **un tasso aggregato è una media pesata di gruppi con dimensioni e baseline differenti; se cambia la composizione, il totale può cambiare anche quando il comportamento all'interno dei gruppi racconta un'altra storia.**

### Il meccanismo in termini di business

Supponiamo di confrontare due team commerciali:

```text
Nord:   win rate 31%
Centro: win rate 24%
```

Prima di concludere che Nord sia migliore, dobbiamo chiedere come sono distribuite le opportunità tra:

- SMB;
- mid-market;
- enterprise;
- inbound;
- outbound;
- territori più o meno maturi.

Se Nord riceve soprattutto opportunità facili e Centro soprattutto account enterprise, il confronto totale mescola **performance** e **portfolio mix**.

### Simpson's paradox

Il termine **Simpson's paradox**, o Yule-Simpson effect, descrive situazioni in cui una relazione aggregata si indebolisce, scompare o può perfino invertirsi quando osserviamo gruppi rilevanti separatamente.

Matematicamente non c'è nulla di paradossale: cambiano i pesi con cui i sottogruppi contribuiscono al totale.

Analiticamente, però, l'effetto è potente perché il dato aggregato può suggerire una decisione opposta a quella suggerita dai confronti condizionati.

### Ma segmentare non è automaticamente corretto

Qui serve una cautela fondamentale che ci prepara ai Capitoli 8 e 9.

Non ogni variabile deve essere "controllata".

Se segmentiamo per una variabile che è conseguenza dell'azione che stiamo studiando, possiamo eliminare proprio parte dell'effetto che ci interessa. Se segmentiamo arbitrariamente decine di dimensioni, possiamo produrre pattern casuali.

Nell'EDA la domanda è quindi:

> **Questa dimensione descrive una differenza di composizione plausibilmente rilevante per interpretare il confronto?**

La risposta causale richiederà un ragionamento più forte.

### Differenza assoluta e relativa

Un conversion rate che passa dal 2% al 3% cambia di:

- **+1 punto percentuale**;
- **+50% in termini relativi**.

Entrambe le espressioni sono corrette e comunicano aspetti diversi.

Una buona pratica è riportarle insieme quando entrambe aiutano:

> Conversion rate +1 pp, da 2% a 3%, equivalente a +50% rispetto alla baseline.

### Checklist del confronto

Prima di confrontare gruppi chiediti:

- la popolazione è comparabile?
- il periodo è comparabile?
- metriche e denominatori sono definiti nello stesso modo?
- la composizione per segmenti rilevanti è differente?
- un gruppo ha diversa esposizione al rischio o all'opportunità?
- pochi sottogruppi dominano il totale?
- il risultato aggregato sopravvive a segmentazioni motivate dal processo?

> **Confrontare due numeri è facile. Capire che cosa rende i gruppi confrontabili è il vero lavoro analitico.**

[^berkeley-simpson]: Lisa Goldberg, Berkeley Math Circle, *Gender Bias, Simpson's Paradox and Causal Inference*, basato su Bickel, Hammel & O'Connell (1975), *Sex Bias in Graduate Admissions: Data from Berkeley*. https://mathcircle.berkeley.edu/sites/default/files/handouts/2019/Simpson%20Paradox%20-%20Lisa%20Goldberg%20BMC%20Dec%2015%202019_0.pdf