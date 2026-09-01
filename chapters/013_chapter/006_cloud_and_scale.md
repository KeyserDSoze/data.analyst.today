## 13.5 Locale, shared compute e cloud: scegliere dove deve vivere l'esecuzione

Il Capitolo 12 ha già spiegato l'architettura dati.

Qui non dobbiamo decidere se l'azienda “deve andare in cloud”.

Dobbiamo rispondere a una domanda più vicina al lavoro dell'analista:

> **Questo calcolo può vivere responsabilmente sul mio computer oppure ha bisogno di un ambiente condiviso e gestito?**

La differenza non dipende soltanto dai gigabyte.

### La scala ha più dimensioni

Quando diciamo “scala” possiamo intendere:

- volume di dati;
- frequenza di esecuzione;
- numero di utenti;
- concorrenza;
- numero di sorgenti;
- sensibilità del dato;
- durata del processo;
- dipendenze downstream;
- necessità di compute elastico.

Un dataset da 5 GB può essere perfettamente gestibile localmente per una EDA una tantum.

Lo stesso dataset può richiedere un ambiente condiviso se deve essere elaborato ogni notte, con credenziali centralizzate, output per 200 utenti e SLA mattutino.

### Caso simulato/composito — il processo che funziona finché lo esegue una persona

Un retailer costruisce un'analisi settimanale su 40 milioni di righe.

Sul laptop dell'analista senior gira in 55 minuti.

Dopo alcuni mesi:

- tre persone devono eseguirla;
- il volume cresce a 250 milioni di righe;
- il job diventa notturno;
- Finance usa automaticamente l'output;
- Security vieta copie locali dei dati cliente.

Il problema non è diventato improvvisamente “big data”.

È diventato un problema di:

- **shared execution**;
- sicurezza;
- scheduling;
- ownership;
- affidabilità.

Qui spostare il workload su infrastruttura gestita può ridurre il rischio complessivo anche se un laptop più potente sarebbe ancora tecnicamente capace di eseguire il calcolo.

### Non usare “cloud” come sinonimo di distribuito

Molte analisi possono girare in cloud su una singola istanza o direttamente nel warehouse senza usare framework distribuiti.

La sequenza di maturità non è necessariamente:

```text
laptop → cluster distribuito
```

Può essere:

```text
laptop
→ query nel warehouse
→ job schedulato gestito
→ compute elastico
→ distributed processing solo se necessario
```

Ogni gradino dovrebbe essere giustificato da un vincolo reale.

### Caso simulato/composito — dashboard da €27.000 al mese

Una dashboard interroga direttamente una fact event da miliardi di righe.

Ha 34 visualizzazioni e ogni interazione genera nuove scansioni.

Il costo mensile cresce fino a circa €27.000.

La risposta sbagliata è:

> cambiamo cloud provider.

La prima domanda dovrebbe essere:

> perché una superficie di consumo sta chiedendo ripetutamente al motore di ricostruire la stessa informazione da miliardi di eventi?

Possibili interventi:

- pre-aggregazione;
- partition pruning;
- caching;
- modelli serving dedicati;
- refresh proporzionato;
- riduzione delle visualizzazioni/query duplicate.

Questo collega il tool selection all'architettura: **il posto dell'esecuzione e il design del dato contano insieme**.

### Local-first quando è sufficiente

Lavorare localmente resta ragionevole quando:

- il dataset è gestibile;
- il lavoro è esplorativo;
- non ci sono dati che non devono essere copiati;
- l'esecuzione non è un servizio;
- una singola persona possiede il processo;
- il costo di setup centrale non crea valore.

La semplicità locale può essere un vantaggio reale.

### Shared/managed execution quando il lavoro diventa sistema

Segnali di migrazione:

- scheduling;
- più utenti;
- credenziali condivise in modo sicuro;
- dati sensibili;
- output downstream;
- workload concorrenti;
- necessità di recovery;
- grandi scansioni ripetute;
- compute che deve crescere/ridursi dinamicamente.

### Campo del Tooling Decision Record

```text
current execution location:
data residency constraints:
input/output size:
frequency:
concurrent users/jobs:
sensitive data:
downstream dependency:
local runtime:
managed/shared alternative:
estimated run cost:
reason to centralize or remain local:
exit condition:
```

### Regola operativa

> **Non spostare un workload nel cloud perché “scala”. Spostalo quando un ambiente condiviso o elastico riduce concretamente rischio, tempo, costo o dipendenza da una macchina/persona.**
