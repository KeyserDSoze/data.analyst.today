## 14.7 Caso simulato/composito — Aurelia Travel: un'indagine revenue con AI sotto controllo

> **Nota editoriale:** Aurelia Travel è un caso simulato/composito costruito a fini didattici. Organizzazione, numeri e sequenza degli eventi non descrivono una singola azienda reale.

Il caso serve a mostrare un workflow completo in cui l'AI accelera realmente l'analisi, ma ogni passaggio importante produce un artefatto verificabile.

### Il contesto decisionale

Aurelia Travel gestisce una piattaforma di prenotazione in 11 mercati europei.

Lunedì, ore 08:05, il CFO riceve un alert automatico:

- net revenue settimana corrente: €18,7M;
- settimana precedente: €20,4M;
- variazione: -8,3%.

Il CEO chiede:

> “È un problema reale? Qual è il driver? Dobbiamo intervenire oggi?”

Questa non è una sola domanda. Sono tre gate distinti:

1. **measurement gate** — il -8,3% è un numero affidabile?
2. **diagnostic gate** — sappiamo dove si concentra il fenomeno?
3. **action gate** — l'evidenza è sufficiente per una decisione operativa?

### AI Analysis Control Sheet — apertura

L'analista apre la scheda di controllo.

```text
decision:
capire se bloccare/rollbackare un cambiamento operativo entro la giornata

risk level:
alto — possibile impatto su revenue e rollout prodotto

allowed data:
semantic model certificato + data-health metadata + release log

allowed actions:
read-only analytics; nessun rollback automatico

required gates:
certified metric
freshness/completeness
reconciliation
alternative hypotheses
human approval before action
```

Questa scheda cambia il comportamento del copilota: non è autorizzato a trasformare direttamente una correlazione in una raccomandazione eseguibile.

### Step 1 — La prima risposta è veloce e sbagliata

L'analista chiede:

> “Scomponi il calo di net revenue rispetto alla settimana precedente. Mostra i tre contributi maggiori.”

L'AI restituisce:

1. Francia: -€720k;
2. hotel urban: -€510k;
3. mobile app: -€430k.

E propone:

> “Il calo è principalmente dovuto a una riduzione della domanda mobile in Francia.”

Il risultato è plausibile. Non supera però il **measurement gate**.

### Step 2 — Verificare la metrica prima dei driver

L'analista richiede il Verification Bundle:

```text
metric id:
date field:
population filters:
source objects:
query / semantic expression:
data timestamp:
reconciliation reference:
```

Emerge che il copilota ha usato una misura `Revenue` presente nel modello ma non certificata.

Quella misura rappresenta gross booking value al netto delle sole cancellazioni immediate.

La misura ufficiale Finance è `Net_Revenue_Final`, che include commissioni, refund e adjustment tardivi.

Con la metrica certificata:

- settimana corrente: €19,35M;
- precedente: €20,10M;
- delta: -3,7%.

Prima lezione:

> **non diagnostichiamo un delta finché non abbiamo dimostrato che il delta significa ciò che crediamo.**

### Step 3 — Job verde non significa numero finale

Il data-health layer mostra:

| Dataset | Ultimo dato | Completezza stimata | Stato |
|---|---:|---:|---|
| bookings | 07:15 | 99,99% | READY |
| payments | 07:20 | 99,97% | READY |
| refunds | 07:10 | 99,98% | READY |
| advertising | 06:55 | 100% | READY |
| partner adjustments | 07:05 | 82% | PROVISIONAL |

`partner_adjustments` viene normalmente finalizzato verso le 11:00.

Il -3,7% diventa quindi:

```text
status: PROVISIONAL
claim allowed: “revenue attualmente sotto baseline”
claim not allowed: “revenue finale -3,7%”
```

L'agente non deve inventare certezza dove il sistema di dati dichiara esplicitamente incompletezza.

### Step 4 — Chiedere un piano, non una storia

L'analista non chiede più “perché?”.

Chiede:

> “Costruisci un decomposition plan. Separa traffico, conversion, booking value, cancellation/refund, commission rate e mix. Per ogni blocco indica metriche certificate, sanity check e possibili spiegazioni alternative. Non formulare causal claim.”

L'AI produce un piano che viene approvato prima di eseguire decine di query.

Questo evita un failure mode comune:

```text
prima narrativa plausibile
→ poi ricerca selettiva di evidenze che la confermano
```

### Step 5 — Decomposition

Dopo i controlli:

- traffico: -0,6%;
- conversion: -2,8%;
- average booking value: +1,1%;
- cancellation/refund: leggermente peggiore;
- commission rate: stabile.

Il fenomeno principale è dunque compatibile con un deterioramento di conversion, non con una grande contrazione della domanda.

Questo è ancora un finding descrittivo.

### Step 6 — Segmentazione e composition check

L'AI genera query per:

- market;
- device;
- app/web;
- payment method;
- destination type;
- acquisition channel;
- app version.

La prima vista fa sembrare la Francia il problema principale.

L'analista chiede però:

> “Il peggioramento resta dentro ciascuna app version oppure dipende dal cambiamento del mix di versioni?”

Risultato:

| App version | Share precedente | Share corrente | Conversion precedente | Conversion corrente |
|---|---:|---:|---:|---:|
| 8.41 | 62% | 18% | 4,9% | 4,8% |
| 8.42 | 21% | 67% | 4,8% | 3,7% |
| altro | 17% | 15% | 4,5% | 4,4% |

Il calo è concentrato sulla 8.42.

### Step 7 — Falsificare l'ipotesi prima di innamorarsene

Ipotesi corrente:

> “La release 8.42 ha degradato il pagamento.”

L'AI viene usata come generatore di alternative.

Propone:

- mix geografico;
- tracking mobile rotto;
- PSP outage;
- acquisizione di traffico peggiore;
- stored cards correlate con mercati diversi;
- rollout non casuale.

Per ogni ipotesi viene associato un test discriminante.

Questa è una funzione molto più utile di “scrivi una spiegazione convincente”.

### Step 8 — Funnel, log e triangolazione

La caduta si concentra tra:

```text
payment_started
→ payment_authorized
```

Il payment error rate sale dal 2,1% al 6,8% sulla versione 8.42, ma quasi solo per carte salvate.

Un release note indica che la 8.42 ha modificato il token refresh delle stored cards.

Engineering riproduce il bug in ambiente controllato.

Ora abbiamo tre evidenze convergenti:

1. pattern quantitativo;
2. localizzazione coerente nel funnel;
3. riproduzione tecnica indipendente.

### Step 9 — La Francia era un proxy

Perché la prima risposta indicava la Francia?

Perché quel mercato aveva:

- rollout 8.42 più avanzato;
- utilizzo più elevato delle stored cards.

Il paese era quindi un **proxy di esposizione**, non il meccanismo del problema.

La frase:

> “la domanda mobile in Francia è crollata”

viene rifiutata.

Il claim consentito diventa:

> “Il deterioramento di conversion è concentrato sugli utenti della versione 8.42 che usano stored cards. La Francia appare maggiormente colpita perché presenta una quota più alta di quella combinazione. Engineering ha riprodotto un difetto nel token refresh compatibile con il pattern osservato.”

### Step 10 — Quantificare senza falsa precisione

L'analista stima un range di impatto, non un numero singolo:

- booking persi: circa 8.900–10.600;
- net revenue associata: circa €510k–€620k;
- stima ancora soggetta a refund e partner adjustment non finalizzati.

La scheda registra:

```text
impact status: estimated / provisional
uncertainty driver:
late adjustments + counterfactual conversion assumption
```

### Step 11 — Action gate

La decisione proposta è:

1. bloccare ulteriore rollout della 8.42 sulle stored cards;
2. rollback mirato della modifica;
3. mantenere monitoraggio su conversion e payment errors;
4. aggiornare il CFO dopo la finalizzazione dei dati;
5. fare post-incident review su metric selection e data-readiness gate.

L'AI può preparare il piano.

Non può approvare il rollback perché l'Agent Execution Contract prevede **A2 — Prepare action**.

L'approvazione finale resta a Product/Engineering owner.

### Il trace che deve restare

Alla fine dell'indagine la AI Analysis Control Sheet contiene:

```text
question:
certified metric:
metric version:
data readiness:
AI-generated plan:
queries executed:
checks passed/failed:
alternative hypotheses tested:
claim level allowed:
impact estimate + caveat:
recommended action:
human approver:
final decision:
```

Questo trace è più importante della cronologia completa della chat con l'AI.

Serve a ricostruire **quale evidenza ha autorizzato quale passaggio**.

### Dove l'AI ha creato valore

Ha ridotto il costo di:

- scrivere query;
- generare decomposition;
- enumerare alternative;
- costruire sanity check;
- confrontare segmenti;
- preparare la documentazione.

### Dove avrebbe creato danno senza controllo

La prima risposta combinava:

- metrica non certificata;
- dato non finalizzato;
- proxy geografico scambiato per driver;
- narrativa anticipata rispetto alla verifica.

La velocità avrebbe reso l'errore operativo prima, non migliore.

### Il workflow canonico del caso

```text
Decision
→ Context Pack
→ Certified metric
→ Data-readiness gate
→ AI diagnostic plan
→ Generated queries
→ Verification Bundle
→ Alternative hypotheses
→ Independent evidence
→ Claim gate
→ Impact range
→ Human approval
→ Action
→ Audit trace
```

> **Quando l'esecuzione diventa quasi istantanea, il collo di bottiglia professionale si sposta dalla produzione della risposta alla dimostrazione che ogni passaggio merita il livello di fiducia richiesto dal successivo.**
