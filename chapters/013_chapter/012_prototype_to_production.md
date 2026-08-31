## 13.11 Dal prototipo alla produzione: quando il successo cambia il problema

Un prototipo ha un obiettivo diverso da un sistema di produzione.

Il prototipo deve dimostrare rapidamente che un'idea può funzionare.

La produzione deve funzionare anche:

- domani;
- con più utenti;
- con dati incompleti;
- dopo una modifica di schema;
- quando l'autore è in ferie;
- quando il volume raddoppia;
- quando qualcuno deve capire perché un numero è cambiato.

Il passaggio da prototipo a produzione non è quindi un semplice "deploy". È un cambio di requisiti.

### Caso realistico: il notebook che diventa processo di pricing

Un analyst costruisce in Python un notebook per suggerire sconti a 120 clienti enterprise.

Il notebook:

- legge tre CSV;
- applica regole commerciali;
- stima probabilità di rinnovo;
- produce un file Excel per il sales team.

Per due trimestri funziona benissimo.

Poi il processo viene esteso a 18.000 clienti in 14 paesi e deve girare ogni notte.

Improvvisamente emergono problemi che nel prototipo erano irrilevanti:

- autenticazione alle sorgenti;
- refresh automatico;
- gestione degli errori;
- audit delle raccomandazioni;
- versionamento del modello;
- rollback;
- monitoraggio;
- permessi;
- localizzazione delle valute;
- tempi di esecuzione.

Il notebook non era "sbagliato". Era perfettamente adeguato al problema iniziale.

È cambiato il problema.

### Cinque segnali che un prototipo sta diventando prodotto

1. **Ricorrenza** — viene usato ogni giorno, settimana o mese.
2. **Dipendenza** — qualcuno non può lavorare se il processo fallisce.
3. **Scala** — crescono utenti, record, mercati o sorgenti.
4. **Rischio** — un errore produce impatto economico, legale o reputazionale.
5. **Riutilizzo** — la stessa logica viene consumata da più processi.

Più questi segnali sono presenti, più aumenta il valore dell'industrializzazione.

### Cosa cambia in produzione

Un processo produttivo dovrebbe normalmente introdurre, in misura proporzionata:

- configurazione separata dal codice;
- logging;
- gestione degli errori;
- test automatici;
- ambienti separati;
- version control;
- dependency management;
- monitoraggio della qualità dati;
- ownership;
- documentazione;
- procedure di recovery.

Non serve implementare ogni elemento al massimo livello dal primo giorno. Serve però sapere quali rischi si stanno accettando.

### Il pericolo opposto: production engineering prima della prova di valore

Un team decide di costruire un motore di raccomandazione.

Prima ancora di verificare che le raccomandazioni producano valore, crea:

- microservizi;
- feature store;
- streaming;
- Kubernetes;
- CI/CD;
- monitoring avanzato.

Dopo quattro mesi scopre che una semplice regola basata su recency e frequency produce quasi lo stesso risultato.

Il costo dell'errore non è solo tecnologico. Sono quattro mesi in cui il business non ha imparato quasi nulla.

Una sequenza più sana è spesso:

**domanda → prototipo → evidenza di valore → limiti → industrializzazione proporzionata**

### Analista come custode della continuità semantica

Quando un prototipo viene riscritto da engineering, c'è un rischio sottile: preservare il codice ma cambiare il significato.

Esempio:

nel prototipo `revenue` significa incasso netto dopo refund.

Nella nuova pipeline engineering usa il campo `gross_amount` perché è più semplice da reperire.

Il sistema è più robusto tecnicamente ma il KPI non è più lo stesso.

L'analyst deve verificare non solo che la nuova pipeline "giri", ma che mantenga:

- grain;
- filtri;
- finestre temporali;
- identity logic;
- definizioni metriche;
- regole di esclusione.

### Regola operativa

> **Un prototipo dimostra che un'idea può funzionare. La produzione dimostra che possiamo fidarci del processo che la rende ripetibile.**
