## 13.6 No-code e low-code: comprare automazione senza nascondere il software

Gli strumenti no-code e low-code riducono il costo iniziale dell'automazione.

Possono essere eccellenti per collegare sorgenti, trasformare dati, schedulare flussi, inviare notifiche e costruire piccoli processi senza sviluppare un'applicazione custom.

Il loro vantaggio non è “non essere codice”.

È rendere economico automatizzare **workflow relativamente semplici, visibili e stabili**.

### Caso simulato/composito — il report del lunedì

Ogni lunedì un analyst:

1. scarica dati dal CRM;
2. aggiorna un estratto billing;
3. applica una tabella di mapping;
4. produce un report;
5. lo distribuisce a 18 manager.

Il processo richiede circa 90 minuti.

Se le sorgenti sono supportate, le regole sono stabili e gli errori sono facili da osservare, un workflow visuale può eliminare gran parte del lavoro manuale con un investimento molto inferiore rispetto a una soluzione custom.

Il valore non è soltanto il tempo risparmiato.

Riduce anche:

- copy-paste;
- dimenticanze;
- variazioni nell'ordine dei passaggi;
- dipendenza dalla presenza dell'analista.

### Automazione semplice vs software visuale

Il problema nasce quando il workflow cresce.

Una sequenza come:

```text
trigger
→ read file
→ transform
→ publish
→ notify
```

è facile da comprendere.

Ma con:

- decine di branch;
- loop;
- retry custom;
- chiamate API;
- mapping dinamici;
- gestione di stato;
- eccezioni accumulate negli anni;

stiamo costruendo software, anche se lo rappresentiamo con blocchi.

### Caso simulato/composito — 146 blocchi e nessun owner reale

Un team Operations usa un workflow visuale per riconciliare ordini, pagamenti e refund.

Nel tempo arriva a 146 blocchi, 11 branch, 8 retry e 4 API.

Quando cambia il payment provider, il team non riesce più a prevedere quali percorsi verranno impattati.

Il processo era nato per evitare software engineering.

È diventato **software engineering senza gli strumenti che normalmente rendono il software revisionabile**.

### Complexity budget

Un Tooling Decision Record per no-code dovrebbe includere un vero **complexity budget**.

Per esempio:

```text
max critical integrations: 4
max manual exception classes: 3
workflow owner: 2 persone
required execution log: sì
required alert on failure: sì
version / change history: obbligatoria
```

Non perché questi numeri siano universali, ma perché obbligano il team a dichiarare quando il processo deve essere riesaminato.

### Quando no-code è particolarmente adatto

- workflow lineare;
- regole deterministicamente semplici;
- volumi moderati;
- connettori standard;
- errore facilmente osservabile;
- utenti che devono poter comprendere/modificare il flusso;
- basso costo di failure;
- nessuna necessità di algoritmi custom complessi.

### Segnali di uscita

Il processo dovrebbe essere riesaminato quando crescono:

- branching;
- stato persistente;
- dipendenze;
- volume;
- criticità;
- test necessari;
- recovery;
- gestione di segreti;
- riuso di logica comune;
- numero di persone che modificano il workflow.

L'uscita non richiede necessariamente una “big rewrite”.

Può essere progressiva:

```text
workflow visuale
→ estrazione della logica più critica in SQL/code
→ centralizzazione dei dataset condivisi
→ workflow resta come orchestrazione leggera
```

### Automazione non significa validazione

Automatizzare un processo sbagliato non lo rende maturo.

Prima bisogna sapere:

- qual è la metrica;
- quale input è authoritative;
- quali eccezioni sono reali;
- cosa succede se manca una sorgente;
- come verifichiamo l'output;
- chi riceve un alert.

È la stessa lezione del Capitolo 0 sull'AI: **delegare esecuzione non significa delegare responsabilità**.

### Campo del Tooling Decision Record

```text
workflow purpose:
frequency:
number of steps / branches:
integrations:
stateful logic:
failure impact:
observability:
version/change history:
owners:
manual exception rate:
maintenance hours/month:
exit condition:
```

### Regola operativa

> **No-code riduce il costo dell'automazione semplice. Quando la complessità cresce, non fingere che il processo non sia software soltanto perché il software è disegnato invece che scritto.**
