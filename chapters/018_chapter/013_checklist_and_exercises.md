## 18.12 Analytics Operating Contract, Promotion Gate ed esercizi

Il capitolo non termina chiedendo quale piattaforma usare. Termina con una domanda precedente all'architettura:

> **Questa analisi ricorrente ha davvero il diritto di diventare un servizio operativo?**

Industrializzare troppo presto crea infrastruttura per una domanda ancora instabile. Industrializzare troppo tardi lascia decisioni critiche dipendenti da memoria, file locali e controlli manuali. Il gate serve a distinguere le due situazioni.

## Promotion Gate: da analisi a prodotto operativo

Un workflow merita promozione quando la combinazione di ricorrenza, failure cost e stabilità semantica rende utile trasferire la promessa dalla persona al sistema.

Prima della promozione devono essere leggibili almeno quattro dimensioni.

**Decisione e failure cost.** Quale scelta ricorrente supporta il prodotto? Chi la prende, con quale frequenza e deadline? Che cosa costa un dato sbagliato, in ritardo o non disponibile? Che cosa succede se il prodotto scompare per una settimana?

**Stabilità del significato.** Grain, popolazione, metriche e tempo sono abbastanza stabili da poter essere contrattualizzati? Esiste un semantic owner? Le varianti legittime hanno nomi diversi? I consumer principali condividono il significato?

**Ripetizione e scala.** Il processo viene ricostruito spesso? È usato da più persone o sistemi? Il lavoro manuale ripetuto ha costo significativo o ha già prodotto errore, ritardo o ownership drift?

**Governabilità.** Possiamo testare e monitorare i failure mode rilevanti? Possiamo definire serving state, fallback e recovery? Possiamo identificare consumer downstream e gestire structural/semantic change?

Se queste condizioni non sono mature, l'output del gate può essere semplicemente:

`KEEP EXPLORATORY`.

Automazione non equivale a promozione.

## Analytics Operating Contract

Quando il workflow supera il Promotion Gate, il contratto operativo riunisce le promesse costruite nel capitolo. Questa struttura resta intenzionalmente schematica: è un artefatto da usare durante design, incident, handover e review.

### 1. Purpose e decision boundary

- recurring decision / use case;
- consumer;
- decision owner;
- cadence e decision deadline;
- do-nothing / fallback process.

### 2. Criticality

- `T0 — Exploratory`;
- `T1 — Team`;
- `T2 — Business-critical`;
- `T3 — High-consequence`.

Il tier non certifica qualità. Determina quanto controllo è economicamente proporzionato al failure cost.

### 3. Ownership

- semantic / metric owner;
- product / technical owner;
- source owner;
- stewardship / governance;
- incident escalation owner;
- backup e ownership-transfer path.

### 4. Product e compatibility boundary

- input authoritative;
- output e grain;
- metriche/semantic interface;
- consumer supportati e use case fuori scope;
- schema/semantic compatibility promise;
- version e history policy.

### 5. Reliability contract

- SLI e SLO;
- freshness, completeness, correctness/reconciliation;
- availability/latency se decision-critical;
- error-budget policy quando utile;
- decision deadline.

### 6. Serving states

| Stato | Uso consentito |
|---|---|
| `READY` | tutti i blocking gate passano |
| `READY WITH CAVEATS` | uso consentito entro caveat visibili |
| `STALE BUT SERVABLE` | last-known-good ancora valido entro limiti definiti |
| `PARTIAL / DEGRADED` | ambito escluso dichiarato; solo decisioni compatibili con la copertura |
| `BLOCKED` | non fit for decision |

Per ogni stato devono essere noti fallback, comunicazione e chi può accettare il rischio residuo.

### 7. Failure-mode coverage

La testing strategy deve indicare quali rischi proteggono source contract, structural test, transformation invariant, reconciliation, distribution check, semantic test, consumer/decision test e recovery test.

Ogni controllo ha disposition:

- `BLOCKING`;
- `WARNING`;
- `INFORMATIONAL`.

### 8. Observability e incident response

- monitor e alert actionability;
- severity;
- on-call/escalation proporzionata al tier;
- runbook;
- fallback/degraded mode;
- repair/replay/re-certification;
- incident communication;
- postmortem e reliability review.

### 9. Change e lifecycle

- technical + semantic diff;
- consumer impact analysis;
- notice;
- shadow/dual run;
- backfill vs forward-only;
- rollback/replay;
- asset states `EXPERIMENTAL → SUPPORTED → CERTIFIED → DEPRECATED → RETIRED`;
- successor e archival requirement.

### 10. Adoption e decision value

Misurare la ladder:

**availability → discoverability → usage → effective use → decision embedding → outcome**.

Usage non è automaticamente success. Anche la riduzione di dashboard, alert o query può indicare un sistema migliore.

### 11. Economics

- allocation strategy;
- cost-to-serve;
- service-level/freshness premium;
- cost anomaly;
- unit metrics coerenti con il valore;
- `optimize / resize / redesign / retire` review.

### 12. Agent Operating Profile, se presente

- purpose e criticality;
- model/tool/context configuration;
- data e permission boundary;
- autonomy/action budget;
- eval e monitor;
- stop/escalation;
- audit;
- authority-reduction/revoke path;
- re-eval trigger;
- retirement.

## Operating Readiness Gate

Un prodotto non esce dal gate soltanto come “approvato” o “rifiutato”. Gli stati devono riflettere il rischio operativo reale.

| Stato | Significato |
|---|---|
| `READY TO OPERATE` | ownership, reliability, change, recovery e cost model coerenti con il tier |
| `READY WITH EXPLICIT DEBT` | gap accettati da owner nominato, con scadenza e failure boundary chiari |
| `SHADOW / LIMITED MODE` | parallel run, audience o autorità limitati prima della promozione |
| `NOT READY` | failure cost troppo alto rispetto ai controlli disponibili |
| `KEEP EXPLORATORY` | domanda o semantica non abbastanza stabili da meritare industrializzazione |

> **Non tutto ciò che può essere automatizzato merita di diventare infrastruttura.**

## Esercizio 1 — Il report fragile

Ogni mattina alle 08:00 un report commerciale viene inviato a 200 manager. Negli ultimi tre mesi è arrivato in ritardo **7 volte**, due volte ha mostrato dati incompleti, nessuno sa quale versione di `pipeline_coverage` sia ufficiale, costa circa **€9.000/mese** e il **60%** dei destinatari non lo apre mai.

Costruisci l'Operating Contract minimo: recurring decision, tier, ownership, SLI/SLO, serving states, failure-mode coverage, adoption ladder, cost-to-serve e retirement trigger. Concludi scegliendo tra `IMPROVE`, `RESIZE`, `REDESIGN` o `RETIRE`; non assumere che un report inviato a 200 persone sia automaticamente T2.

## Esercizio 2 — Tutto verde, ma il numero è sbagliato

La pipeline `customer_health` ha job success 100%, freshness entro SLO, schema invariato, null rate stabile e row count nel range. Customer Success scopre però che il CRM ha ridefinito `renewal_date` da data contrattuale a data prevista.

Classifica il failure, progetta il semantic test che avrebbe potuto intercettarlo, ricostruisci blast radius e consumer, scegli il serving state durante l'incidente e definisci recovery/backfill e change notice.

## Esercizio 3 — Error budget quasi esaurito

Una dashboard executive T2 ha readiness SLO **99%** dei business day. Nel trimestre l'error budget è quasi esaurito, ma il team propone tre nuove feature che aggiungono dipendenze.

Decidi se continuare feature work, quali SLI/root-cause analizzare, chi può accettare un cambio di SLO e quale evidenza dimostrerebbe che il 99% è troppo aggressivo o troppo permissivo. Evita di trattare lo SLO come un numero rituale.

## Esercizio 4 — Self-service con usage alto e effective use basso

Una piattaforma ha **2.400 utenti registrati**, **61% MAU**, **490 dashboard**, **38 metriche certificate**, **74 duplicate non certificate**, **11 data incident/mese** e quattro ore medie di reconciliation prima del monthly business review.

Costruisci una scorecard che distingua reach, usage, effective use, decision embedding, reliability, semantic consistency, outcome e cost efficiency. Indica almeno due metriche che potrebbero **diminuire** mentre il sistema migliora.

## Esercizio 5 — Un agente cambia natura

Un agente può interrogare il warehouse, generare SQL, leggere lineage, produrre grafici, inviare sintesi e aprire data-incident ticket. La prima versione è `suggestion-only`. La seconda può anche sospendere automaticamente una campagna marketing fino a **€500.000/mese**.

Costruisci per entrambe le versioni l'Agent Operating Profile: tier, data/tool boundary, authority, eval, runtime/action budget, monitoring, stop condition, escalation, revoke/rollback, re-eval e retirement. Spiega perché il secondo agente non è “lo stesso sistema con un tool in più”: è cambiata l'autorità e quindi il failure cost.

## Esercizio 6 — CI verde, change management rosso

Una nuova semantic layer è tecnicamente migliore ma cambia nomi di metriche, navigation path, workflow Finance, export e ownership di due data product. La CI passa.

Disegna consumer impact analysis, dual run, migration deadline, training/support, deprecation, feedback e rollback. La Fabric Adoption Roadmap ricorda che change management riguarda l'impatto sulle persone e sui processi, non soltanto il deploy tecnico.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-change-management

## Esercizio 7 — Il prodotto che nessuno vuole spegnere

`customer_360_v1` ha un successore da **14 mesi**, costa **€18.000/mese**, riceve ancora il **7% delle query**, non ha owner attivo, contiene due definizioni legacy e alimenta tre job notturni senza business owner noto.

Progetta: lineage/discovery → consumer classification → replacement validation → notice → migration → access restriction progressiva → archival/audit → shutdown → post-retirement monitoring. Decidi anche chi deve possedere il retirement fino alla chiusura effettiva.

## Esercizio finale — Cinque workflow, cinque promesse diverse

Un marketplace ha:

**A.** executive revenue review giornaliero;  
**B.** forecast trimestrale aggiornato mensilmente;  
**C.** fraud decision in pochi secondi;  
**D.** notebook una tantum per valutare una nuova categoria;  
**E.** agente che triagea anomalie e può aprire incident.

Per ciascuno scegli se merita un Analytics Operating Contract, tier, ownership, SLO/failure boundary, testing depth, degraded mode, change process, cost model, adoption/outcome metric, agent governance se rilevante e review/retirement cadence.

Il vincolo è lo stesso che attraversa tutto il libro: **assegnare il minimo controllo sufficiente al costo del failure**, non il massimo controllo tecnicamente possibile.

## Dal sistema operativo dell'analytics al sistema operativo della carriera

Il percorso del capitolo è:

**analisi → asset → prodotto → servizio operativo → capacità organizzativa**.

A ogni passaggio cresce la necessità di rendere espliciti **promessa → owner → failure boundary → controllo → recovery → costo → lifecycle**. Un'organizzazione matura non dipende dall'analyst eroico che ricorda tutte le eccezioni, ma non cerca neppure di eliminare ogni giudizio umano tramite automazione. Posiziona il giudizio nei punti in cui cambia significato, rischio o decisione e incorpora il resto nella capacità operativa.

> **La vera scalabilità non è fare più analisi con le stesse persone. È fare in modo che una decisione continui a ricevere evidenza affidabile anche quando cambiano dati, persone, software, agenti e organizzazione.**

Il Capitolo 19 porta la stessa idea sul professionista. Se query, dashboard, orchestrazione e una parte dell'analisi diventano più automatizzabili, il problema non sarà difendere ogni task manuale. Sarà capire **quali responsabilità vogliamo essere capaci di possedere quando l'esecuzione diventa più economica**.