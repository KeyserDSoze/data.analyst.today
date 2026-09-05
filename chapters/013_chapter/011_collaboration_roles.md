## 13.10 Il team è parte dello stack: scegliere strumenti che qualcuno possa possedere

Una soluzione tecnicamente elegante può essere una pessima scelta se nessuno nel team reale può revisionarla, operarla o modificarla. La mantenibilità non è una proprietà del tool da solo: è una proprietà della combinazione **tool + persone + processo**.

Immaginiamo due opzioni. La prima è tecnicamente ottimale, ma la conosce una sola persona e richiede deployment complesso. La seconda è leggermente meno sofisticata, ma è standard aziendale, ha logging e accessi già integrati e può essere revisionata da sei persone. Se la differenza di performance non cambia la decisione, la seconda può avere un costo totale molto inferiore.

Questo non significa scegliere sempre ciò che il team conosce già. La familiarità non deve diventare inerzia. Significa riconoscere che **la capacità collettiva è un requisito reale**, esattamente come runtime, freshness o costo.

### Quando un artefatto attraversa un confine organizzativo

Un analyst può collegare un dashboard a tre sorgenti operative e intervenire manualmente ogni lunedì quando il refresh fallisce. Finché è un prototipo personale, il costo può essere tollerabile. Quando **80 manager** iniziano a dipendere da quell'output, lo stesso failure mode cambia natura: non abbiamo più soltanto un'analisi, ma un servizio dati ricorrente.

Non serve che l'analista diventi improvvisamente data engineer. Serve riconoscere che ownership e tooling devono essere rivalutati insieme.

I segnali di handoff sono spesso concreti: più team dipendono dall'output, serve uno SLA, compaiono secret e credenziali gestiti, una trasformazione viene riusata ampiamente, il failure blocca un processo business, serve recovery o on-call, oppure il dataset deve avere access control più sofisticato. A quel punto alcune responsabilità possono restare in Analytics e altre passare ad Analytics Engineering o Data Engineering. Il titolo del ruolo conta meno della **responsabilità esplicita**.

### Il tool deve adattarsi anche alla capacità operativa

Un data scientist può produrre un churn score con **AUC 0,89** e una lista di **62.000 account** ad alto rischio. Se Customer Success può contattarne **450 a settimana**, il problema non si risolve con una libreria ML migliore. Serve un sistema di lavoro che colleghi rischio, valore, capacità di intervento, policy e misurazione dell'effetto.

La lezione del Capitolo 10 rimane: una previsione deve entrare in una decision policy. Qui aggiungiamo che **la scelta di tooling deve adattarsi al sistema di persone che trasforma l'output in azione**.

### Bus factor come segnale di rischio

Una domanda semplice è: quante persone potrebbero mantenere questo processo se il suo autore fosse indisponibile per un mese? Per un prodotto critico, `bus factor = 1` è un rischio concreto. Possiamo mitigarlo standardizzando il tool, facendo pairing e review, riducendo custom code, spostando il workload su una piattaforma supportata o creando runbook e documentazione.

Il Tooling Decision Record dovrebbe quindi distinguere builder e long-term owner, indicare reviewer disponibili, skill coverage, platform support, recovery need e soglia di handoff. Una soluzione non è completa finché non sappiamo **chi la possiede dopo che l'entusiasmo iniziale è finito**.

> **Non scegliere soltanto uno strumento che tu sappia usare. Scegli una soluzione che l'organizzazione possa continuare a capire e possedere quando il lavoro smette di essere personale.**
