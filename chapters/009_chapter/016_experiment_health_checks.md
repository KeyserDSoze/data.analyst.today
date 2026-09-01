## 9.15 Experiment Health Gate: prima di stimare l'effetto, certifica che il test sia interpretabile

A questo punto del capitolo abbiamo già incontrato quasi tutti i modi in cui un esperimento può rompersi: unità di randomizzazione sbagliata, identity instabile, Sample Ratio Mismatch, exposure incompleta, logging asimmetrico, contaminazione, peeking, metriche fragili e interferenza.

Serve quindi un passaggio esplicito tra **raccolta dei dati** e **interpretazione dell'effetto**.

Lo chiameremo **Experiment Health Gate**.

La domanda del gate non è:

> la variante B sta vincendo?

È:

> **questo esperimento ha prodotto un confronto abbastanza affidabile da meritare un'interpretazione causale?**

Finché la risposta non è sì, effect size, confidence interval e p-value sono secondari.

### Caso simulato/composito — RideFlow

RideFlow, piattaforma di mobilità urbana, testa un nuovo algoritmo per suggerire punti di pickup più efficienti.

La dashboard mostra:

- tempo medio di attesa: -6,4%;
- cancellazioni: -2,1%;
- intervallo sulla metrica primaria interamente favorevole al trattamento.

Il risultato sembra pronto per il rollout.

L'analista esegue però l'Experiment Health Gate e trova:

| Controllo | Esito |
|---|---|
| allocazione attesa 50/50 | fallisce: 53,8/46,2 |
| assignment stabile | ok |
| exposure per versione app | fallisce su una versione Android |
| logging dei pickup | ok |
| distribuzione OS pre-treatment | sbilanciata tra gruppi osservati |
| concurrent experiments | nessun conflitto noto |

La versione Android che riceve meno spesso il trattamento ha storicamente tempi di attesa peggiori. La variante B contiene quindi una composizione diversa proprio su una variabile legata all'outcome.

Il risultato business non viene classificato come "positivo" o "negativo".

Viene classificato come:

**INVALIDO PER DECISIONE — correggere exposure/telemetria e ripetere.**

Questa è una conclusione migliore di un numero preciso ottenuto da un confronto compromesso.

### I controlli del gate

L'Experiment Health Gate dovrebbe coprire almeno otto famiglie.

**1. Assignment integrity**  
L'unità prevista è stata assegnata una sola volta, con rapporto coerente con il design e senza meccanismi di auto-selezione?

**2. Identity stability**  
La stessa unità rimane nella stessa variante attraverso sessioni, device e periodi rilevanti?

**3. Exposure integrity**  
Assignment e trattamento ricevuto coincidono abbastanza da sostenere l'estimand dichiarato? Esistono versioni, mercati o superfici in cui l'utente è assegnato ma non può ricevere davvero la feature?

**4. Telemetry completeness**  
Gli eventi necessari alla metrica vengono prodotti e filtrati simmetricamente nei gruppi? Crash, redirect o bot filtering possono far sparire osservazioni in modo treatment-dependent?

**5. Population integrity**  
Eligibility, triggering e filtri analitici definiscono ancora la popolazione prevista dall'Experiment Contract, oppure stiamo condizionando su comportamenti avvenuti dopo il trattamento?

**6. Metric integrity**  
Numeratore, denominatore, timestamp, currency, join e finestre di maturazione sono quelli congelati prima del test?

**7. Interference e concurrent changes**  
Altri esperimenti, campagne, release o shared resources possono aver cambiato il trattamento o contaminato il controllo?

**8. Operational incidents**  
Ci sono stati outage, migrazioni, errori di pagamento, capacity constraints o anomalie di sistema abbastanza grandi da rendere il periodo non rappresentativo?

### Pre-treatment balance: diagnostica, non rituale

Con randomizzazione corretta alcune differenze pre-treatment emergeranno comunque per caso, soprattutto se osserviamo molte covariate.

Perciò il balance check non dovrebbe diventare:

> troviamo una covariata con `p < 0,05`, quindi il test è rotto.

È più utile cercare:

- pattern sistematici;
- differenze materialmente grandi;
- squilibri coerenti con un problema di assignment/exposure;
- concentrazione su device, geografie, versioni o canali specifici.

La diagnostica deve aiutare a capire il processo che ha generato i dati, non creare un nuovo torneo di p-value.

### Tre possibili verdetti

Per rendere il gate operativo conviene non usare una semplice checkbox "pass/fail".

#### VALIDO

Non emergono problemi materialmente rilevanti. L'effetto può essere interpretato secondo il piano previsto.

#### VALIDO CON CAVEAT

Esiste una deviazione compresa e circoscritta che non distrugge il confronto ma restringe lo scope della conclusione.

Esempio: una versione legacy dell'app, pari all'1,5% della popolazione, non riceve il trattamento ed è esclusa in modo simmetrico dall'estimand dichiarato.

#### INVALIDO PER DECISIONE

Esiste un problema che può produrre differenze tra gruppi o alterare selettivamente outcome/telemetria e non possiamo quantificarne in modo credibile l'impatto.

In questo caso il test non deve essere "aggiustato finché torna il risultato che piace". Va riparato e, quando necessario, ripetuto.

### Caso reale documentato — Microsoft Experimentation Platform

Microsoft ha documentato più volte che la validità di un esperimento dipende dall'intera catena assignment → execution → telemetry → metric computation. Nei test su modifiche infrastrutturali, il team ha trovato regressioni e problemi che metriche tecniche locali non avrebbero necessariamente mostrato, usando quindi metriche di prodotto e controlli di qualità più ampi prima di approvare il cambiamento.

Questo è coerente con la lezione SRM vista nella sezione 9.3: **prima di fidarsi dell'effetto bisogna fidarsi del processo che ha prodotto il confronto**.

### Il gate precede la statistica finale

L'ordine operativo è:

**Experiment Contract → test in esecuzione → Experiment Health Gate → stima dell'effetto → decisione → rollout.**

Invertire gli ultimi passaggi crea un bias organizzativo potente: se il team vede prima un risultato molto favorevole, diventa psicologicamente più difficile invalidare il test quando emerge un problema di qualità.

> **Un esperimento non è affidabile perché produce un intervallo stretto. È affidabile quando possiamo spiegare perché treatment e control rappresentano ancora il confronto che avevamo deciso di costruire.**

### Fonte pubblica

- Microsoft Experimentation Platform, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
