## 18.2 Reliability: SLI, SLO, osservabilità, degraded mode e incident management

Un prodotto analitico può essere tecnicamente disponibile e decisionally unusable.

Se il report arriva alle 10:15 ma il capacity meeting è alle 09:00, il servizio ha fallito anche se la pipeline è `SUCCESS`.

Se arriva puntuale con il 92% delle transazioni, ma nessuno sa quali sorgenti mancano, il servizio ha fallito in un altro modo.

Se è fresco e completo ma una definizione è cambiata senza preavviso, il rischio può essere ancora maggiore.

Per questo il reliability model dell'analytics deve partire dall'esperienza del **consumer della decisione**, non dalla salute del job.

## Dal “job verde” al “dato fit for decision”

Possiamo distinguere almeno tre livelli.

### Infrastructure health

- processo in esecuzione;
- CPU/memoria;
- scheduler;
- storage disponibile;
- query terminata.

### Pipeline health

- task completati;
- dependency rispettate;
- runtime;
- retry;
- schema leggibile.

### Decision-data health

- sorgenti attese presenti;
- completezza sufficiente;
- metrica riconciliata;
- definizione comparabile;
- dato disponibile entro la decision deadline;
- eventuali caveat visibili.

Un sistema può essere verde nei primi due livelli e rosso nel terzo.

## Il linguaggio SRE: SLI, SLO, SLA

Google SRE distingue:

- **SLI — Service Level Indicator:** misura osservata del comportamento che conta;
- **SLO — Service Level Objective:** target dell'indicatore;
- **SLA — Service Level Agreement:** accordo che associa conseguenze esplicite al mancato rispetto di un livello di servizio.

Fonte: https://sre.google/sre-book/service-level-objectives/

Per l'analytics questa distinzione è utile perché ci obbliga a passare da:

> “Il dashboard deve essere affidabile.”

a qualcosa di verificabile.

Esempio:

### SLI freshness

Percentuale di business day in cui il dataset `executive_revenue` è certificato entro le 07:00 CET.

### SLO freshness

`≥ 99%` nel trimestre.

### SLI completeness

Percentuale di ordini del giorno precedente presenti rispetto alla fonte operativa riconciliata.

### SLO completeness

`≥ 99,8%` prima della pubblicazione del daily pack.

### SLI semantic correctness

Percentuale dei controlli di riconciliazione e business invariant critici che passano.

### SLO semantic correctness

`100%` per i gate classificati `blocking`.

Il target non deve essere identico per ogni prodotto.

## Non copiare gli SLO software alla lettera

Una API può misurare availability e latency richiesta per richiesta.

Un prodotto analitico spesso ha eventi meno frequenti e dimensioni differenti.

SLI utili possono includere:

- **freshness** — dato disponibile entro la deadline;
- **completeness** — quota attesa di sorgenti/record coperta;
- **correctness** — reconciliation e invariant;
- **semantic stability** — nessuna breaking change non comunicata;
- **availability** — superficie interrogabile quando serve;
- **latency** — tempo evento → dato consumabile;
- **recoverability** — capacità di ricostruire il dato entro una finestra;
- **traceability** — possibilità di risalire a versione, sorgente e trasformazione.

Google SRE osserva che i big-data system tendono a interessarsi a throughput ed end-to-end latency, ma sottolinea anche che **correctness** è una proprietà essenziale della salute del sistema.

Fonte: https://sre.google/sre-book/service-level-objectives/

## Criticality tier → SLO diverso

Non dobbiamo promettere 99,99% a tutto.

Esempio:

| Prodotto | Tier | SLO principale |
|---|---|---|
| notebook personale | T0 | best effort |
| team dashboard | T1 | refresh entro 09:00 nel 95% dei business day |
| executive revenue pack | T2 | certified entro 07:00 nel 99% dei business day + blocking reconciliation |
| payout/regulatory feed | T3 | controllo rigoroso, auditability e recovery concordati con il processo critico |

Google SRE evidenzia che pretendere 100% di reliability può essere indesiderabile: aumenta costo e conservatorismo, mentre un SLO ben scelto deve riflettere ciò che gli utenti realmente richiedono.

Fonte: https://sre.google/sre-book/service-level-objectives/

## Error budget: affidabilità come trade-off esplicito

Se lo SLO è 99%, stiamo implicitamente accettando che una quota limitata del servizio possa non rispettare il target.

Quella quota è l'**error budget**.

In analytics, l'idea non deve diventare un gioco matematico.

Serve a decidere **quando il debito di reliability deve prendere priorità rispetto a nuove feature**.

Esempio:

Un executive pack ha SLO di readiness 99% su 100 business day.

Se accumula più failure di quanto il budget consenta, la policy può imporre:

- freeze di nuove feature;
- priorità a root-cause e test;
- riduzione di dipendenze fragili;
- revisione dello SLO se era irrealistico.

Google SRE usa proprio l'error budget come meccanismo di bilanciamento tra reliability e velocità del cambiamento.

Fonte: https://sre.google/workbook/error-budget-policy/

## Caso simulato/composito: dashboard verde, decisione rossa

Una catena retail utilizza una dashboard giornaliera per allocare stock.

Alle 08:00:

- pipeline: `SUCCESS`;
- report: disponibile;
- KPI: apparentemente normali.

Alle 10:30 Operations scopre che **63 store** non hanno inviato i dati POS.

Il sistema monitorava:

- job success;
- runtime;
- presenza della tabella.

Non monitorava:

- numero di store attesi;
- store mancanti;
- volume per fonte;
- scostamento dalla baseline;
- reconciliation con il sistema POS.

La pipeline aveva processato correttamente ciò che aveva ricevuto.

Il prodotto analitico aveva fallito la sua promessa.

## Observability: non monitorare tutto, monitorare ciò che cambia azione

Google SRE distingue il monitoring utile per trend, dashboard, debugging e alerting, e sottolinea che un alert dovrebbe richiedere un'azione umana significativa invece di produrre rumore continuo.

Fonte: https://sre.google/sre-book/monitoring-distributed-systems/

Per un data product possiamo osservare:

### Source signals

- arrival;
- record count;
- partition coverage;
- schema version;
- source-specific heartbeat.

### Transformation signals

- runtime;
- failure/retry;
- row expansion/contraction;
- duplicate rate;
- null rate;
- join match rate.

### Semantic signals

- business invariant;
- accounting reconciliation;
- metric continuity;
- denominator shift;
- unexpected definition/version.

### Consumer signals

- data age visibile;
- query failures;
- dashboard availability;
- number of users affected;
- missed decision deadline.

La domanda non è:

> “Quante metriche possiamo monitorare?”

È:

> **“Quale segnale ci permette di scoprire un fallimento prima che produca una decisione sbagliata?”**

## Alerting: page, ticket o dashboard?

Non ogni deviazione deve svegliare qualcuno.

Possiamo distinguere:

### Page / immediate escalation

Quando:

- il prodotto T2/T3 è fuori SLO;
- la decision deadline è imminente;
- il dato potrebbe causare impatto materiale;
- esiste un'azione immediata possibile.

### Ticket / business-hours action

Quando:

- il problema degrada qualità ma non blocca la decisione corrente;
- il budget di reliability si sta consumando;
- serve manutenzione ma non incidente.

### Monitoring only

Quando:

- il segnale serve a trend e capacity planning;
- non richiede un intervento puntuale.

Troppi alert producono **alert fatigue** e trasformano l'osservabilità in rumore.

## Degraded mode: non esistono solo “verde” e “rotto”

Uno dei concetti più utili per l'analytics è il **degraded mode**.

Supponiamo che manchi il feed di un piccolo mercato che rappresenta il 2% delle vendite.

Le opzioni non sono soltanto:

- pubblicare come se nulla fosse;
- bloccare tutto.

Possiamo avere stati operativi:

### READY

Tutti i blocking gate passano.

### READY WITH CAVEATS

Il dato è utilizzabile per alcune decisioni, con caveat visibile.

### STALE BUT SERVABLE

Nuovo refresh non disponibile; ultima versione certificata ancora utile entro un limite definito.

### PARTIAL / DEGRADED

Una parte della copertura manca; il prodotto espone chiaramente cosa è escluso.

### BLOCKED

Il rischio semantico o di correttezza rende il prodotto non fit for decision.

Il degraded mode deve essere progettato **prima** dell'incidente.

## Fallback: che cosa mostriamo quando il nuovo dato non è affidabile?

Un Operating Contract può specificare:

- ultima snapshot certificata;
- stima preliminare marcata `PROVISIONAL`;
- dataset parziale con coverage label;
- manual reconciliation;
- dashboard disabilitata con status page;
- processo alternativo per decisioni critiche.

Un fallback non deve massimizzare availability a costo di nascondere l'incertezza.

## Incident severity

Una severity taxonomy può combinare:

- decisione impattata;
- impatto economico;
- numero di consumer;
- deadline;
- rischio regolatorio/privacy;
- possibilità di rollback;
- durata;
- esposizione esterna.

Esempio:

### SEV-1

Dato T3 errato già usato per payout/regulatory decision o rischio imminente equivalente.

### SEV-2

Prodotto T2 critico bloccato o materialmente sbagliato prima di una decision deadline.

### SEV-3

Problema circoscritto con workaround.

### SEV-4

Difetto minore / cosmetic / non decision-critical.

I nomi possono cambiare. Conta avere escalation proporzionata.

## Runbook: il contrario della memoria eroica

Un runbook utile include:

```text
symptom
→ affected product / tier
→ decision deadline
→ current data status
→ likely failure domains
→ checks
→ fallback
→ communication path
→ recovery/backfill
→ verification before re-certification
```

Il runbook non deve contenere cento pagine.

Deve ridurre il tempo necessario per capire **che cosa fare nei primi minuti**.

## Postmortem: imparare senza cercare un colpevole

Google SRE promuove una cultura di postmortem blameless: l'obiettivo è capire le condizioni del sistema che hanno reso possibile il fallimento e trasformare l'incidente in miglioramento organizzativo.

Fonte: https://sre.google/workbook/postmortem-culture/

Un postmortem analytics dovrebbe chiedere:

- quando è iniziato il problema?
- quando lo abbiamo rilevato?
- chi lo ha rilevato: sistema o utente?
- perché i controlli esistenti non lo hanno fermato?
- quale decisione poteva essere compromessa?
- il degraded mode ha funzionato?
- quanto tempo è servito per recovery?
- quale test/monitor/runbook deve cambiare?

Non:

> “Chi ha scritto la query sbagliata?”

## Reliability review

A cadenza mensile o trimestrale, i prodotti critici possono essere valutati su:

- SLO attainment;
- error budget consumption;
- incident count e severity;
- time to detect;
- time to recover;
- percentuale incidenti trovati dagli utenti;
- repeat incidents;
- stale/degraded usage;
- reliability cost.

Questo chiude il ciclo:

**promessa → misura → deviazione → risposta → apprendimento**.

> **Un prodotto analitico affidabile non è quello che non fallisce mai. È quello che rende esplicito quale livello di fallimento è accettabile, scopre rapidamente quando lo supera e degrada senza fingere che il dato sia più affidabile di quanto sia.**
