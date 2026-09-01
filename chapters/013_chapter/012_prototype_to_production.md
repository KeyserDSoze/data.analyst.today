## 13.11 Dal prototipo alla produzione: cambiare tool quando cambia la responsabilità

Un prototipo e un sistema di produzione possono usare lo stesso linguaggio e avere requisiti completamente diversi.

Il prototipo deve rispondere:

> **questa idea merita di essere usata?**

La produzione deve rispondere anche:

> **possiamo continuare a fidarci del processo che la esegue quando volume, utenti, errori e tempo reale entrano in gioco?**

Per questo il passaggio a produzione non è un semplice deploy.

È una **nuova decisione di design**.

### Caso simulato/composito — notebook di pricing che cambia categoria

Un analyst costruisce un notebook per suggerire condizioni commerciali a 120 clienti enterprise.

Il processo:

- legge tre estratti;
- applica regole;
- calcola scenari;
- produce un workbook per Sales.

Per due trimestri funziona bene.

Poi il business decide di usarlo per:

- 18.000 clienti;
- 14 paesi;
- esecuzione notturna;
- caricamento automatico nel CRM;
- audit delle raccomandazioni.

Il metodo può essere lo stesso.

Ma sono cambiati:

- scala;
- frequenza;
- consumer;
- rischio;
- data access;
- recovery requirement;
- ownership.

Il notebook non è diventato improvvisamente “cattivo”.

Ha semplicemente **superato l'exit condition del prototipo**.

### Promotion gate

Un Tooling Decision Record dovrebbe stabilire in anticipo i segnali che richiedono una nuova review.

Cinque categorie sono particolarmente utili.

#### 1. Ricorrenza

```text
ad hoc → settimanale → giornaliero → continuo
```

Ogni aumento di frequenza aumenta il valore di automazione e osservabilità.

#### 2. Dipendenza

```text
solo analyst → team → processo operativo → sistema downstream
```

Più persone dipendono dall'output, meno è accettabile uno stato locale non controllato.

#### 3. Scala

- righe;
- utenti;
- paesi;
- sorgenti;
- chiamate;
- runtime.

#### 4. Rischio

- economico;
- privacy;
- compliance;
- customer impact;
- decisioni automatizzate.

#### 5. Riutilizzo

Se la stessa logica viene consumata da più processi, il valore di centralizzazione e test aumenta.

### Prototype maturity ladder

Possiamo rappresentare una progressione tipica.

**P0 — scratch**

- file/notebook personale;
- input temporanei;
- nessun consumer.

**P1 — validated prototype**

- metodo verificato;
- input identificati;
- output confrontato con baseline;
- decisione di continuare presa.

**P2 — recurring analytical process**

- esecuzione ripetibile;
- version control;
- test principali;
- owner e documentazione.

**P3 — production analytical product**

- scheduling;
- monitoring;
- access control;
- recovery;
- SLA/SLO quando serve;
- change management.

Non tutti i progetti devono arrivare a P3.

Molti non dovrebbero farlo.

### Il costo della premature productionization

Un team vuole testare un recommendation system.

Prima di verificare valore costruisce:

- streaming;
- feature store;
- microservizi;
- orchestration;
- CI/CD sofisticata;
- monitoring completo.

Dopo quattro mesi scopre che una semplice regola recency-frequency produce quasi lo stesso valore economico.

La tecnologia costruita può essere impeccabile.

Ma il processo di apprendimento è stato inefficiente.

Una sequenza più sana è spesso:

```text
problema
→ soluzione minima verificabile
→ evidenza di valore
→ failure modes reali
→ industrializzazione proporzionata
```

### Continuità semantica durante la migrazione

Quando engineering riscrive un prototipo, non basta confrontare runtime o output shape.

Bisogna verificare che restino invariati, quando devono restarlo:

- popolazione;
- grain;
- date;
- identity logic;
- filtri;
- metriche;
- fallback;
- handling dei missing.

Esempio:

```text
prototype revenue = incasso netto dopo refund
production revenue = gross_amount
```

La pipeline nuova può essere più robusta e al tempo stesso implementare un prodotto diverso.

L'**Analytical Data Contract** del Capitolo 11 diventa quindi uno strumento di migrazione.

### Shadow run e parity test

Prima di sostituire un processo importante può essere utile eseguire vecchio e nuovo sistema in parallelo.

```text
old output
vs
new output
```

Le differenze devono essere:

- attese;
- spiegate;
- approvate.

Non bisogna pretendere sempre equivalenza perfetta: una migrazione può correggere bug o cambiare definizioni.

Ma le differenze non devono essere sorprese.

### Campo del Tooling Decision Record

```text
current maturity: P0-P3
current tool:
current consumers:
frequency:
risk:
known manual steps:
promotion trigger:
production requirements missing:
parity / migration plan:
new owner:
rollback:
```

### Regola operativa

> **Non chiedere “possiamo mettere in produzione questo notebook?”. Chiedi “quali nuovi obblighi sono comparsi perché questo lavoro è diventato importante, ricorrente o operativo?”. Lo strumento deve cambiare solo quanto serve per soddisfarli.**
