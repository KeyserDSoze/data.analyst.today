## 0.7 Caso end-to-end: dodici agenti, un analista, una decisione

**Caso simulato/composito.** Consideriamo una società SaaS B2B, **NovaSuite**, con circa €95 milioni di ARR.

Un lunedì mattina il CEO riceve un alert:

> “Il Net Revenue Retention enterprise è sceso dal 112% al 104%.”

Otto punti percentuali sono abbastanza per richiedere attenzione immediata. Ma non abbastanza per dire, da soli, che cosa sia successo.

Il responsabile analytics dispone di una squadra di agenti specializzati. Il vantaggio non sta nel chiedere a dodici agenti la stessa domanda. Sta nel dare a ciascuno un ruolo diverso nella costruzione dell'evidenza.

### Fase 1 — Decomporre il problema

L'analista assegna compiti distinti.

| Agente | Mandato | Risultato iniziale |
|---|---|---|
| Metric definition | recuperare la definizione certificata di NRR | stessa base clienti, nuovi loghi esclusi |
| Data health | controllare freshness, completeness e schema | nessuna anomalia evidente |
| Reconciliation | confrontare ARR con Finance | differenza 0,4%, entro tolleranza |
| Segmentation | localizzare il delta | calo concentrato nell'enterprise europeo |
| Product usage | cercare cambiamenti di comportamento | uso di una feature premium in diminuzione |
| Support | analizzare ticket e temi | ticket performance in aumento |
| Pricing | ricostruire variazioni di listino | alcuni rinnovi europei hanno prezzi più alti |
| Release history | ricostruire i cambiamenti tecnici | release backend sei settimane prima |
| NRR decomposition | separare churn, contraction ed expansion | contraction è il contributo maggiore |
| Causal critic | contestare le prime spiegazioni | pricing e feature exposure sono confusi |
| Counterfactual search | cercare gruppi meno esposti | cluster e account con esposizione diversa |
| Executive draft | preparare una prima sintesi | propone di sospendere il nuovo listino |

La decomposizione del NRR è particolarmente utile:

- churn: -2,1 punti percentuali;
- contraction: -4,7 punti;
- minore expansion: -1,2 punti.

Il problema dominante non è quindi “più clienti che se ne vanno”. È che clienti esistenti stanno riducendo il valore del contratto.

Già questo cambia la domanda investigativa.

### Fase 2 — Non confondere una sintesi elegante con una conclusione

L'agent incaricato dell'executive draft produce:

> “La riduzione NRR è probabilmente causata dall'aumento di prezzo europeo. Raccomandiamo di sospendere il nuovo listino.”

La frase è plausibile. È anche prematura.

Il responsabile analytics non la inoltra. Fa tre domande.

**1. Il prezzo precede davvero il contraction?**

Per diversi account, la riduzione di seat o moduli compare prima del rinnovo con il nuovo listino. Il pricing non può quindi spiegare l'intero fenomeno.

**2. Il calo di utilizzo è una causa o un sintomo?**

Una feature usata meno potrebbe essere diventata meno utile. Oppure potrebbe essere diventata più lenta o instabile.

**3. Quale evento cambia per primo?**

La timeline ricostruita mostra:

1. release backend;
2. aumento della latenza sui workload più pesanti;
3. riduzione nell'uso della feature premium;
4. aumento dei ticket performance;
5. riduzione di seat e moduli al rinnovo;
6. contraction ARR.

La catena non dimostra ancora causalità, ma rende la spiegazione tecnica più coerente temporalmente dell'ipotesi pricing.

### Fase 3 — Cercare controlli che non dipendano dalla stessa storia

L'analista chiede verifiche ortogonali.

**Telemetria infrastrutturale.** La latenza p95 sui workload enterprise europei è aumentata del 38% dopo la release.

**Gruppo meno esposto.** I clienti enterprise statunitensi, serviti prevalentemente da un cluster diverso, non mostrano lo stesso aumento.

**Feature exposure.** Gli account che usano intensamente la feature colpita mostrano contraction molto più elevato.

**Account senza nuovo listino.** Anche clienti che non hanno ancora ricevuto l'aumento di prezzo mostrano calo di usage.

L'ultima evidenza è particolarmente importante: indebolisce una spiegazione che sembrava convincente perché separa il fenomeno operativo dalla variazione di prezzo.

### Fase 4 — Calibrare il linguaggio alla forza dell'evidenza

A questo punto l'analista non dice:

> “Abbiamo dimostrato che la release ha causato il calo di NRR.”

L'evidenza osservazionale non giustifica una certezza così forte.

Formula invece la conclusione così:

> “La principale ipotesi supportata dai dati è che la release backend abbia degradato le performance per workload enterprise europei, riducendo l'adozione della feature premium e contribuendo alla contraction al rinnovo. Il pricing può avere amplificato il fenomeno in alcuni account, ma non ne spiega la sequenza temporale principale.”

È meno spettacolare della prima risposta automatica.

È molto più utile per decidere.

### Fase 5 — Scegliere un'azione proporzionata all'incertezza

Il team non effettua immediatamente un rollback globale e non annulla il listino.

Decide di:

- mitigare la configurazione sui cluster europei;
- sospendere rollout aggiuntivi;
- monitorare latenza e usage per 72 ore;
- contattare gli account più colpiti;
- mantenere invariato il pricing finché il suo contributo non viene isolato meglio.

La decisione è mirata, osservabile e in buona parte reversibile. Produce inoltre nuove evidenze: se la mitigazione migliora latenza e usage nei segmenti esposti, l'ipotesi tecnica guadagna forza.

### Che cosa ha fatto davvero l'analista?

Non ha scritto personalmente tutte le query.

Non ha costruito ogni grafico.

Non ha letto manualmente migliaia di ticket.

Non ha preparato la prima bozza del memo.

Ha però:

- definito il fenomeno da misurare;
- scomposto il problema in mandati diversi;
- separato produzione, critica e decisione;
- individuato un conflitto tra spiegazioni;
- chiesto evidenze indipendenti;
- ragionato sulla sequenza temporale;
- distinto correlazione, plausibilità e causalità;
- calibrato il linguaggio all'incertezza;
- scelto un'azione proporzionata al rischio.

Gli agenti hanno svolto gran parte dell'esecuzione.

L'analista ha governato il **sistema di evidenze**.

### Il contrasto che conta

Immaginiamo due risposte al CEO.

Prima:

> “L'AI dice che è il pricing.”

Seconda:

> “Il pricing è emerso come prima ipotesi, ma non regge completamente alla verifica temporale. Abbiamo evidenza più forte su una degradazione backend che precede il calo di utilizzo e la contraction. Il pattern compare nella telemetria e nei segmenti più esposti, mentre account senza nuovo listino mostrano comunque il calo di usage. Propongo una mitigazione mirata e 72 ore di monitoraggio prima di modificare il pricing.”

Entrambe le risposte possono essere state prodotte con la stessa tecnologia.

Solo una dimostra leadership analitica.

> **Il valore dell'analista non sta nel numero di task che esegue personalmente. Sta nella qualità del sistema di decisione che riesce a dirigere.**
