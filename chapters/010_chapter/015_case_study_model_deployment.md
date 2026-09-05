## 10.15 Caso simulato/composito — OrbitCom: dal buon modello offline al sistema che cambia il proprio futuro

OrbitCom è un operatore telecom con **3,8 milioni di clienti consumer**. Il management parte con una richiesta apparentemente semplice:

> **“Costruiamo un modello che preveda il churn.”**

Il team non sceglie subito un algoritmo. Trasforma la richiesta in una prediction task: ogni lunedì alle 05:00 vuole ordinare i clienti consumer attivi per probabilità di cancellazione volontaria nei successivi 60 giorni, senza superare i **25.000 contatti/settimana** che il team retention può gestire con qualità. La baseline è la regola esistente basata su reclami recenti, payment issues e calo utilizzo.

Questa specifica cambia il progetto. Non serve il miglior classifier in astratto: serve un ranking utile nei primi 25.000 casi e una pipeline che possa riprodurre ogni lunedì la stessa frontiera informativa.

### Prima del modello: che cosa esiste davvero alle 05:00?

Le feature candidate includono tenure, variazione di utilizzo dati, reclami aperti e chiusi prima del prediction time, payment failures storici, outage, variazione spesa, downgrade già avvenuti, app usage, device e piano tariffario.

`last_retention_offer_result` viene esclusa perché l'offerta viene spesso fatta dopo che il rischio è già stato identificato e troppo vicino al churn. `competitor_offer_declared` proviene da survey disponibili soltanto per una parte dei clienti e viene mantenuta come feature sperimentale con coverage monitorata.

Già qui il progetto ha guadagnato più credibilità di quanta ne avrebbe ottenuta aggiungendo un algoritmo più complesso: ha stabilito che cosa il modello può sapere.

### La validation prova a ricostruire il futuro operativo

Pricing e acquisition mix sono cambiati nell'ultimo anno, quindi OrbitCom evita di affidarsi soltanto a random split. Usa periodi più vecchi per il training, un periodo successivo per validation, gli ultimi mesi maturi come test out-of-time e controlla separatamente nuovi clienti e tenure >12 mesi.

Il confronto è:

| Modello | ROC-AUC test | PR-AUC | Precision@25k | Note |
|---|---:|---:|---:|---|
| regola esistente | 0,69 | 0,17 | 24% | baseline operativa |
| logistic regression | 0,82 | 0,31 | 38% | interpretabile |
| gradient boosting | 0,87 | 0,39 | 44% | modello candidato |

Il boosting guadagna il diritto alla complessità perché migliora proprio il punto operativo: nei 25.000 slot disponibili concentra più churn futuri della baseline e della logistica.

### Il leakage review riduce lo score e aumenta la fiducia

Una review `as-of` trova due problemi: uno snapshot CRM storico ricostruiva il passato usando `current account status`; una feature di ticket severity poteva essere aggiornata retroattivamente dopo la chiusura del ticket.

Dopo la correzione la ROC-AUC scende da **0,90 a 0,87**. Il team non chiama questa variazione “regressione del modello”. La classifica precedente misurava un sistema impossibile da replicare in produzione. Il nuovo numero è il primo che può sostenere una decisione reale.

### Ranking, calibration e capacità diventano policy

Il modello ordina bene ma sovrastima il rischio dei clienti più nuovi. OrbitCom mantiene il ranking globale, applica una calibration validata separatamente e controlla reliability per tenure.

La policy non usa `threshold = 0,5`. Seleziona i **top 25.000 account eleggibili per expected risk/value**, con guardrail business. La capacità non è quindi un'aggiunta operativa dopo il modeling: è parte della funzione decisionale che il modello deve servire.

### Predire il churn non significa sapere chi salvare

A questo punto emerge il confine con i Capitoli 8 e 9. Un cliente può essere ad alto rischio ma irrecuperabile, a rischio medio e molto persuadibile, oppure destinato a non churnare anche senza intervento.

Per questo OrbitCom crea, nella popolazione eleggibile alla retention policy e compatibilmente con i vincoli commerciali, un **holdout sperimentale**. Prediction misura chi è a rischio; experimentation misura l'incremental effect della policy.

Senza questa separazione un modello accurato potrebbe essere confuso con un programma retention efficace.

### Il primo mese sembra confermare la promessa

Nel primo mese la scoring pipeline è stabile, `precision@25k` è vicina al test, il contact rate è **91%**, la capacità è quasi pienamente utilizzata e la calibration resta nei range previsti. Il sistema è production-ready, non “finito”.

Tre mesi dopo le metriche cambiano:

| Metrica | Test offline | Mese 1 | Mese 3 |
|---|---:|---:|---:|
| ROC-AUC | 0,87 | 0,85 | 0,77 |
| precision@25k | 44% | 41% | 29% |
| contact rate | — | 91% | 63% |
| quota nuovi clienti nel top-K | 18% | 21% | 37% |

Dire semplicemente “il modello è peggiorato” sarebbe troppo poco. L'indagine separa quattro fenomeni.

Una campagna ha portato molti clienti giovani, mensili e mobile-first poco rappresentati nel training: **population drift**. Un nuovo piano con roaming incluso ha cambiato il significato predittivo di `domestic_data_usage_drop`: ranking e calibration peggiorano, quindi c'è anche **concept/calibration drift**. Nel frattempo una riorganizzazione riduce il contact rate al 63%: **operational degradation**. Infine i clienti ad alto score vengono trattati e alcune label future incorporano l'effetto della retention policy: **feedback loop**.

### La dashboard viene separata in quattro layer

```text
DATA
feature freshness · missing · training-serving skew · population mix

MODEL
ranking · precision@25k · calibration · score distribution

OPERATIONS
selected · contacted · time-to-contact · capacity · treatment delivered

OUTCOME
churn · incremental effect vs holdout · value saved · cost · customer guardrails
```

Questa separazione rende impossibile nascondere un problema del call center dentro “model performance” e, allo stesso tempo, evita di usare i problemi operativi per giustificare un ranking che si sta realmente deteriorando.

### Retraining è una promozione, non un refresh automatico

OrbitCom genera mensilmente un retraining candidate, ma lo promuove soltanto dopo champion/challenger evaluation su dati recenti out-of-time, gate su calibration e `precision@25k`, verifica di training-serving parity e confronto con la baseline concordata. Feature, modello e policy vengono versionati separatamente. L'holdout continua a misurare l'efficacia della retention policy indipendentemente dal risk model.

La richiesta iniziale “chi farà churn?” è così diventata un sistema di domande coordinate: chi è a rischio, quanto è affidabile lo score oggi, chi entra nei 25.000 slot, chi viene realmente contattato, quale intervento salva churn incrementale, quanto valore netto produce e quando modello o policy devono essere fermati o ridisegnati.

Un failure può quindi essere di prediction, di dati/serving, di policy o di treatment. Chiamare tutto “model performance” rende la diagnosi peggiore.

> **Il prodotto predittivo non è il file del modello. È la catena che trasforma informazione disponibile oggi in una priorità, una decisione, un'azione e una misura del risultato futuro — sapendo che l'azione stessa cambierà i dati che vedremo domani.**