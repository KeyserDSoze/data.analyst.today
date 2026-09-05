## 14.7 Caso simulato/composito — Aurelia Travel: un'indagine revenue con AI sotto controllo

> **Nota editoriale:** Aurelia Travel è un caso simulato/composito costruito a fini didattici. Organizzazione, numeri e sequenza degli eventi non descrivono una singola azienda reale.

Aurelia Travel gestisce una piattaforma di prenotazione in 11 mercati europei. Lunedì alle 08:05 il CFO riceve un alert: net revenue settimana corrente €18,7M, settimana precedente €20,4M, variazione `-8,3%`. Il CEO chiede: "È un problema reale? Qual è il driver? Dobbiamo intervenire oggi?"

La domanda sembra unica, ma contiene tre gate distinti: **measurement**, **diagnostic** e **action**. Il workflow AI-assisted è utile proprio se impedisce di saltarli.

### Aprire la Control Sheet prima dell'indagine

L'analista registra subito:

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

Questa specifica non rallenta l'analisi: impedisce che la velocità dell'AI trasformi una correlazione in un'azione prima della verifica.

### La prima risposta è veloce e sbagliata

Alla richiesta di scomporre il calo, l'AI restituisce Francia `-€720k`, hotel urban `-€510k`, mobile app `-€430k` e propone che la domanda mobile in Francia sia il driver principale. La risposta è plausibile, ma non ha ancora superato il **measurement gate**.

L'analista richiede metric id, date field, population filters, source objects, semantic expression, timestamp del dato e reconciliation reference. Emerge che il copilota ha usato una misura `Revenue` presente nel modello ma non certificata. Quella misura rappresenta gross booking value al netto delle sole cancellazioni immediate. La misura Finance è `Net_Revenue_Final`, che include commissioni, refund e adjustment tardivi.

Con la metrica certificata il confronto diventa:

```text
settimana corrente: €19,35M
settimana precedente: €20,10M
delta: -3,7%
```

La prima lezione del caso è semplice: **non diagnostichiamo un delta finché non abbiamo dimostrato che il delta significa ciò che crediamo**.

### Job verde non significa numero finale

Il data-health layer mostra:

| Dataset | Ultimo dato | Completezza stimata | Stato |
|---|---:|---:|---|
| bookings | 07:15 | 99,99% | READY |
| payments | 07:20 | 99,97% | READY |
| refunds | 07:10 | 99,98% | READY |
| advertising | 06:55 | 100% | READY |
| partner adjustments | 07:05 | 82% | PROVISIONAL |

`partner_adjustments` viene normalmente finalizzato verso le 11:00. Il `-3,7%` può quindi orientare l'attenzione, ma non essere comunicato come revenue finale. La Control Sheet registra:

```text
status: PROVISIONAL
claim allowed: revenue attualmente sotto baseline
claim not allowed: revenue finale -3,7%
```

### Chiedere un piano prima della storia

A questo punto l'analista non chiede "perché?". Chiede un decomposition plan che separi traffico, conversion, booking value, cancellation/refund, commission rate e mix; per ogni blocco richiede metriche certificate, sanity check e spiegazioni alternative. Nessun causal claim è autorizzato.

Dopo l'approvazione del piano, l'AI esegue la decomposizione. I risultati sono:

- traffico `-0,6%`;
- conversion `-2,8%`;
- average booking value `+1,1%`;
- cancellation/refund leggermente peggiore;
- commission rate stabile.

Il fenomeno principale è compatibile con un deterioramento di conversion, non con una grande contrazione della domanda. È ancora un finding descrittivo.

### Segmentare senza confondere proxy e meccanismo

L'AI genera query per market, device, app/web, payment method, destination type, acquisition channel e app version. La prima vista continua a far sembrare la Francia il problema. L'analista però chiede se il peggioramento resta **dentro** ciascuna app version o dipende dal mix.

| App version | Share precedente | Share corrente | Conversion precedente | Conversion corrente |
|---|---:|---:|---:|---:|
| 8.41 | 62% | 18% | 4,9% | 4,8% |
| 8.42 | 21% | 67% | 4,8% | 3,7% |
| altro | 17% | 15% | 4,5% | 4,4% |

Il calo è concentrato sulla 8.42. La working hypothesis diventa che la release abbia degradato il pagamento, ma il workflow obbliga ora a cercare alternative: mix geografico, tracking mobile rotto, PSP outage, acquisition quality, stored cards correlate con mercati diversi, rollout non casuale.

### Falsificazione e triangolazione

L'analisi del funnel localizza la caduta tra `payment_started` e `payment_authorized`. Il payment error rate sale dal `2,1%` al `6,8%` sulla versione 8.42, quasi soltanto per stored cards. Un release note indica che la 8.42 ha modificato il token refresh delle carte salvate. Engineering riproduce poi il bug in ambiente controllato.

Ora abbiamo tre evidenze convergenti: pattern quantitativo, localizzazione nel funnel e riproduzione tecnica indipendente. La Francia si rivela un proxy: aveva rollout 8.42 più avanzato e utilizzo più elevato delle stored cards. Il claim "la domanda mobile in Francia è crollata" viene rifiutato.

Il claim consentito è:

> Il deterioramento di conversion è concentrato sugli utenti della versione 8.42 che usano stored cards. La Francia appare maggiormente colpita perché presenta una quota più alta di quella combinazione. Engineering ha riprodotto un difetto nel token refresh compatibile con il pattern osservato.

### Quantificare senza falsa precisione

L'impatto viene espresso come range:

```text
booking persi: circa 8.900–10.600
net revenue associata: circa €510k–€620k
```

La stima resta soggetta a refund e partner adjustment non finalizzati. La Control Sheet registra `impact status: estimated / provisional` e identifica come fonti di incertezza late adjustments e assunzione sulla conversion controfattuale.

### Action gate

La decisione proposta è bloccare ulteriore rollout della 8.42 sulle stored cards, preparare rollback mirato, mantenere monitoraggio su conversion/payment errors, aggiornare il CFO dopo la finalizzazione dei dati e fare una post-incident review su metric selection e readiness gate. L'AI può preparare il piano, ma non approvare il rollback: l'Agent Execution Contract è **A2 — Prepare action**. L'approvazione resta a Product/Engineering owner.

Alla fine della run la Control Sheet conserva domanda, metrica/versione, readiness, piano AI, query, controlli, alternative testate, claim level, impact range, raccomandazione, approvatore e decisione finale. Questo trace è più importante della cronologia completa della chat: rende ricostruibile **quale evidenza ha autorizzato quale passaggio**.

L'AI ha creato valore riducendo il costo di scrivere query, generare decomposition, enumerare alternative e preparare controlli. Senza il sistema di controllo avrebbe invece accelerato una diagnosi basata su metrica non certificata, dato immaturo e proxy geografico scambiato per driver.

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
