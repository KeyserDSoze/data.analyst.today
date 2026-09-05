## 18.11 Caso end-to-end: quando il weekly review diventa infrastruttura

### Caso simulato/composito: Helios Mobility

**Helios Mobility** è un'azienda europea di micromobilità con circa **4,8 milioni di corse al mese**. Ogni lunedì il management decide come riallocare la flotta, dove aumentare manutenzione e charging capacity, quali promozioni modificare, quali anomalie richiedono escalation e se il forecast trimestrale resta compatibile con il piano.

Il weekly business review contiene rides, revenue, contribution margin, fleet availability, incident rate, retention, CAC e forecast. Esistono molte dashboard. A prima vista il sistema sembra già industrializzato.

In realtà il pacchetto richiede quasi **due giorni-persona** di preparazione distribuiti tra più analyst. Tre team usano definizioni diverse di `active_rider`; Finance riconcilia revenue con uno scarto medio dell'**1,7%**; il forecast vive in notebook separati per città; una modifica all'app può cambiare tracking senza consumer impact notice; una sorgente incompleta alle 05:00 viene spesso scoperta nel meeting; alcune dashboard si aggiornano ogni dieci minuti anche se servono una volta al giorno. Soprattutto, nessuno possiede il weekly review end-to-end.

Helios non ha un problema di scarsità di dati. Ha una **promessa operativa implicita**.

## La prima decisione non è “rifacciamo le dashboard”

Il team potrebbe iniziare migrando tutto su una nuova piattaforma. Invece applica il Promotion Gate del capitolo: quale capacità ricorrente è diventata abbastanza importante da meritare ownership, SLO e failure boundary?

Il `Weekly Mobility Review` viene classificato **T2 — business-critical** perché informa decisioni che muovono flotta, capacità e spesa ogni settimana. Da questa classificazione nasce un Analytics Operating Contract, non il contrario.

| Campo | Promessa operativa |
|---|---|
| Consumer | COO, CFO, City Operations |
| Decision owner | COO |
| Semantic owner | Finance per revenue/margin; Operations per fleet availability |
| Product owner | Analytics Platform |
| Criticality | T2 |
| Freshness | previous-day data certified entro 07:00 CET |
| Completeness | ≥99,5% delle ride attese oppure stato degradato esplicito |
| Finance reconciliation | scarto ≤0,25% prima del board-use |
| Degraded mode | last-known-good + affected-city exclusion + warning |
| Escalation | Analytics on-call → source owner → decision owner |
| Change review | semantic diff + consumer impact analysis |
| Retirement review | semestrale |

Il cambiamento più importante non è tecnico. Per la prima volta esiste una promessa che può essere verificata e, soprattutto, violata in modo visibile.

## Separare il significato dall'esercizio

Prima del redesign tutti erano “responsabili dei dati”; quindi nessuno era accountable quando il problema attraversava più team. Il nuovo modello separa decision owner, semantic owner, product owner, source owner e stewardship. Analytics non decide più unilateralmente la semantica di revenue o fleet availability; Finance e Operations non mantengono pipeline e incident response; il COO può accettare o rifiutare il rischio residuo quando il serving state non è `READY`.

La stessa distinzione consente di certificare una sola versione executive di `active_rider`, `completed_ride`, `recognized_revenue`, `contribution_margin`, `vehicle_availability` e `30-day retention`. Le varianti locali non vengono proibite: vengono nominate in modo differente e non possono presentarsi come `certified executive metric`.

Per ogni metrica executive grain, popolazione, timezone, event/accounting date, filtri, owner, versione e validità temporale diventano parte della promessa. La standardizzazione non cancella l'analisi locale; impedisce che oggetti diversi si presentino con lo stesso nome nel processo critico.

## Il primo incidente dimostra perché `job_success` non era abbastanza

Helios aggiunge source coverage, city coverage, ride/payment reconciliation, uniqueness di `ride_id`, telemetry lateness e distribution check. Il weekly review espone un piccolo **data health header** prima dei KPI:

```text
Freshness: OK
Ride completeness: 99.82%
Payment reconciliation: 99.93%
Known incidents: 1
Affected scope: Valencia telemetry only
Serving state: READY WITH CAVEATS
```

Poche settimane dopo, un lunedì alle **05:40**, un provider telemetria smette di consegnare parte degli eventi di Milano. La pipeline termina senza errore. Il vecchio sistema avrebbe pubblicato numeri parziali.

Il nuovo sistema vede city volume `-19%` rispetto alla baseline, active provider count sotto atteso, payment count incompatibile con ride count e completeness stimata all'**82%**. Lo stato diventa:

`PARTIAL — DO NOT USE MILAN RIDE KPI FOR ALLOCATION`.

Alle 07:00 il review viene comunque pubblicato. Le altre città sono `READY`; Milano è esclusa dai confronti operativi; il last-known-good è mostrato come riferimento e chiaramente etichettato; incident e owner sono visibili; il forecast non viene ricalibrato sul dato incompleto.

La sorgente è fallita. **La decisione non è fallita silenziosamente.** Questo è il valore reale di SLO, observability e degraded mode.

## Il secondo incidente è semantico, non tecnico

Tre mesi dopo Product modifica l'evento `ride_started`. Prima viene emesso quando il veicolo si sblocca; dopo quando il mezzo supera una soglia di movimento. Nome e schema rimangono identici.

Se Helios controllasse soltanto structural compatibility, nessuna pipeline si romperebbe. Ma `ride_started` non rappresenterebbe più lo stesso istante del processo. È un semantic breaking change.

Il Source Contract richiede notice. Il team esegue dual emission su un campione, confronta vecchio e nuovo evento per città e device, aggiorna le metriche colpite, richiede semantic-owner approval, dichiara la data di efficacia e sceglie esplicitamente tra backfill e forward-only. Il grafico storico non viene lasciato cambiare di significato in silenzio.

Da questo failure mode nasce la delivery chain T2: version control, structural test, invariant, reconciliation, distribution check, semantic diff, shadow run e rollback/replay plan. Il rigore non aumenta perché Helios “vuole fare CI/CD bene”; aumenta perché ora sappiamo quale tipo di change potrebbe attraversare i test tecnici senza farsi vedere.

## Meno dashboard, più self-service

Helios ha oltre **140 dashboard** sulle performance città. Il redesign non prova ad aumentarne l'uso. Costruisce tre prodotti principali — `City Operations`, `Finance Performance`, `Weekly Mobility Review` — e rende esplicite boundary, owner, serving state e source of truth.

Alcune dashboard duplicate vengono ritirate. Il numero di asset diminuisce, ma una quota maggiore dei meeting usa metriche certificate; le reconciliation request calano; gli utenti trovano più rapidamente il prodotto authoritative; i meeting cominciano da uno stato comune di data health.

È un buon esempio di adoption non misurabile con “più dashboard” o “più sessioni”: **meno superficie, maggiore decision embedding**.

## Il costo rivela un'altra forma di mismatch

L'allocazione dei costi mostra che molto compute viene consumato da refresh frequenti su report giornalieri, semantic model duplicati per città, query esplorative che scansionano raw history e pipeline near-real-time per consumer che non prendono decisioni real-time.

Helios ridefinisce quindi i service level: fleet incident operations near-real-time, city performance hourly, Finance/weekly review daily, exploration on demand. Non è un progetto di cost cutting. È il riallineamento tra **valore della latency e costo della promessa**.

Il sistema smette di pagare il livello di servizio più urgente su ogni use case.

## L'agente entra soltanto dentro il contratto esistente

Dopo aver reso più stabile il prodotto, Helios introduce un agente per il triage dei data incident. Può eseguire query read-only, leggere il semantic layer certificato e lineage, aprire ticket, proporre decomposition e sintetizzare evidence e alternative hypothesis. Non può modificare metriche, scrivere nel warehouse, chiudere autonomamente incident T2, pubblicare causal claim o agire sui sistemi operativi.

Questa boundary impedisce all'AI di creare un secondo shadow operating model.

Poi accade l'incidente che giustifica la governance. Dopo un update del lineage tool, l'agente comincia a selezionare una vista deprecated con una vecchia definizione di revenue. Gli eval pre-deploy non avevano coperto quella combinazione. Il monitoring osserva un aumento dei reconciliation failure nel Verification Bundle.

Il runbook non aspetta di capire perfettamente la root-cause. Revoca temporaneamente il lineage tool, porta l'agente in `suggestion-only`, blocca gli output finance-related, identifica i run già prodotti e richiede re-eval prima del restore.

La lezione non è che “l'agente può sbagliare”. È più operativa: **il sistema sapeva ridurre l'autorità quando la fiducia in una dipendenza era scesa**.

## Sei mesi dopo: misurare capacità, non attività

Essendo un caso composito, non trasformiamo il finale in una storia di successo inevitabile. La scorecard che Helios dovrebbe leggere è più importante dei numeri specifici.

Sul piano **reliability**, conta che una quota crescente di incidenti venga scoperta dal monitoring prima dei consumer, che Finance reconciliation rispetti più spesso lo SLO e che MTTR T2 diminuisca. Sul piano **semantic consistency**, conta avere una sola `active_rider` executive certificata, breaking change con notice e asset legacy in retirement. Sul piano **adoption**, conta che più processi decisionali usino prodotti certificati e che il tempo speso a chiedere “quale numero è corretto?” scenda. Sul piano **economics**, il compute near-real-time dovrebbe concentrarsi nei workload che ne ricavano valore. Sul piano **AI operations**, audit completo, escalation e abstention devono essere osservati come comportamenti governati; per unsupported claim high-severity il target può essere zero tolerance.

Il successo non è quindi “abbiamo automatizzato il report”. Helios ha trasformato una routine in una capacità con questa catena:

**decisione → tier → ownership → contract → SLO → test → serving state → change control → self-service → cost-to-serve → agent governance → learning**.

Ogni elemento è entrato perché proteggeva un failure mode emerso o plausibile. Questa è la differenza tra checklist di maturità e operating model.

Microsoft, nella Fabric Adoption Roadmap, tratta adoption organizzativa come combinazione di ownership, governance, COE, supporto, system oversight e change management, non come distribuzione di una piattaforma. È un riferimento utile proprio perché la lezione di Helios non è tecnologica: persone, processi e tecnologia devono evolvere insieme.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap

> **Scalare analytics significa rendere esplicito cosa promettiamo, chi ne risponde, come degradiamo quando la promessa non può essere mantenuta e quando abbiamo il diritto di cambiare o ritirare il sistema.**

L'ultima sezione trasforma questa storia in un gate operativo riutilizzabile, mantenendo però una regola essenziale: non tutto ciò che può essere automatizzato merita di diventare infrastruttura.