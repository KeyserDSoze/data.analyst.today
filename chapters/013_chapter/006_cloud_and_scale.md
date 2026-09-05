## 13.5 Locale, shared compute e cloud: scegliere dove deve vivere l'esecuzione

Il Capitolo 12 ha già discusso architettura e piattaforme. Qui non dobbiamo decidere se un'azienda “deve andare in cloud”. La domanda per l'analista è molto più concreta: **questo calcolo può vivere responsabilmente sul mio computer oppure ha acquisito obblighi che richiedono un ambiente condiviso e gestito?**

La risposta non dipende solo dai gigabyte. Scala significa anche frequenza, numero di utenti, concorrenza, sorgenti, sensibilità del dato, durata, dipendenze downstream e bisogno di recovery. Un dataset da 5 GB può essere perfettamente gestibile localmente per una EDA una tantum e inadatto allo stesso laptop se deve essere elaborato ogni notte, con credenziali centralizzate, output per 200 utenti e un orario di disponibilità promesso.

Un retailer costruisce un'analisi settimanale su **40 milioni di righe**. Sul laptop dell'analista senior gira in 55 minuti. Poi il volume arriva a **250 milioni di righe**, tre persone devono eseguirla, Finance usa automaticamente l'output, il job diventa notturno e Security vieta copie locali dei dati cliente. Il problema non è diventato improvvisamente “big data”: è diventato un problema di **shared execution, sicurezza, scheduling, ownership e affidabilità**.

A quel punto spostare il workload su infrastruttura gestita può ridurre il rischio complessivo anche se una macchina personale più potente sarebbe ancora tecnicamente capace di eseguire il calcolo.

### Non confondere cloud con complessità distribuita

La migrazione non deve saltare dal laptop a un cluster distribuito. Una progressione plausibile può essere:

```text
laptop
→ query nel warehouse
→ job schedulato gestito
→ compute elastico
→ distributed processing solo se necessario
```

Ogni gradino deve rispondere a un vincolo reale.

Lo stesso criterio vale sui costi. Una dashboard che interroga una fact da miliardi di righe, ha 34 visualizzazioni e genera scansioni a ogni interazione può arrivare a circa **€27.000 al mese** nel nostro caso simulato. La prima risposta non dovrebbe essere “cambiamo cloud provider”, ma chiedere perché la superficie di consumo continua a ricostruire la stessa informazione dal livello più costoso. Pre-aggregazioni, pruning, caching o serving model dedicati possono cambiare il problema molto più del logo del provider.

### Local-first finché resta responsabile

Lavorare localmente è sensato se il dataset è gestibile, il lavoro è esplorativo, non esistono vincoli che vietano copie locali, l'esecuzione non è un servizio e il costo di setup centrale non crea valore. La semplicità locale è un vantaggio reale.

I segnali che spingono verso shared/managed execution sono invece di natura organizzativa oltre che tecnica: scheduling, più utenti, segreti gestiti centralmente, dati sensibili, consumer downstream, workload concorrenti, recovery, grandi scansioni ripetute e bisogno di compute elastico.

Il Tooling Decision Record dovrebbe quindi descrivere dove gira oggi il workload, quali vincoli di residency e sicurezza esistono, frequenza, utenti, dipendenze downstream, costo di esecuzione e **perché centralizzare riduce rischio o perché restare locale è ancora sufficiente**.

> **Non spostare un workload nel cloud perché “scala”. Spostalo quando un ambiente condiviso o elastico riduce concretamente rischio, tempo, costo o dipendenza da una macchina o da una persona.**
