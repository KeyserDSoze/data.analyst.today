## 18.1 Ownership: il numero deve avere più di un proprietario

Quando un'organizzazione cresce, il problema raramente è la mancanza di metriche. È la presenza di numeri molto usati senza una catena di responsabilità abbastanza precisa da sopravvivere a conflitti, cambiamenti e incidenti.

Dire che una metrica è “owned by Finance” o “del data team” è troppo vago. Finance può possedere il significato economico senza mantenere la pipeline; Analytics Engineering può garantire test e SLO senza avere l'autorità di decidere quando una fattura entra nella recognized revenue; il CFO può consumare il numero senza gestire le eccezioni quotidiane. **Significato, decisione ed esercizio sono responsabilità diverse.** Se le comprimiamo nella parola `owner`, scopriamo l'ambiguità proprio quando il sistema smette di riconciliare.

Per un prodotto critico conviene distinguere almeno quattro ruoli. Il **decision owner** risponde della decisione ricorrente e chiarisce quali errori siano materialmente pericolosi. Il **semantic o metric owner** possiede definizione, popolazione, esclusioni, timing ed eventuali breaking change di significato. Il **product/technical owner** mantiene implementazione, test, SLO, monitoring, release, runbook e cost-to-serve. Lo **steward/governance owner** protegge accesso, privacy, classificazione, lineage e standard trasversali. I nomi possono cambiare; non deve cambiare la separazione delle responsabilità.

Questa distinzione è coerente con la Fabric Adoption Roadmap di Microsoft, che tratta content ownership, stewardship, supporto e trasferimento della proprietà come temi separati e collega il livello di controllo allo scope e alla criticità del contenuto.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-content-ownership-and-management

## Tre NRR corretti e una sola metrica da board

Una società SaaS prepara il board meeting. Nella stessa presentazione compaiono tre valori di NRR: `108%` in Finance, `104%` in Customer Success, `111%` in Product. Nessuna query è necessariamente sbagliata. Finance esclude contratti non ancora riconosciuti; Customer Success considera soltanto gli account assegnati alle regioni gestite; Product include expansion maturata entro trenta giorni dal rinnovo.

Il failure mode non è quindi “tre formule diverse”. Sono **tre oggetti diversi con lo stesso namespace**. Vietare le varianti e imporre un'unica dashboard risolverebbe il sintomo ma potrebbe distruggere use case legittimi. La soluzione più robusta è separare purpose e autorità: `Board NRR` come metrica executive certificata, `CS-managed NRR` per la gestione del portafoglio assegnato, `Product cohort NRR` per lifecycle analysis.

La metrica executive può essere descritta da una **Metric Operating Card**, un artefatto che merita di restare strutturato perché deve essere scansionabile durante change e incident response.

| Campo | Esempio |
|---|---|
| Nome autorevole | Board Net Revenue Retention |
| Decision owner | CFO |
| Semantic owner | Finance RevOps |
| Technical owner | Analytics Engineering |
| Steward | Data Governance |
| Grain | customer × month |
| Population | recurring-revenue customers at period opening |
| Formula | opening ARR + expansion − contraction − churn, diviso opening ARR |
| Source of truth | billing_curated + approved account mapping |
| Cut-off | 06:30 CET business day +1 |
| Freshness SLO | certified entro 07:00 nel 99% dei business day |
| Reconciliation | Finance ledger entro tolerance concordata |
| Version | v3 |
| Status | certified |
| Review | quarterly + on material business change |

La formula occupa una riga. Il resto spiega **perché quel numero ha il diritto organizzativo di essere usato**.

## Le promesse sono concatenate

Ownership della sorgente e ownership della metrica non coincidono. Il CRM owner può promettere stabilità di `account_id` e `contract_status`, ma non decide come calcolare NRR. Finance può possedere la definizione di NRR senza controllare ritardi del CRM, duplicate contract o mapping account. Un prodotto analitico è quindi un sistema di promesse concatenate: source contract → metric contract → serving contract → decision deadline.

Questo è il motivo per cui un problema di ownership non si risolve nominando genericamente “il data team”. Dobbiamo sapere chi può dichiarare una sorgente non fit, chi approva un backfill, chi decide una nuova definizione e chi informa i consumer se il prodotto deve passare da `READY` a `BLOCKED`.

## Ownership drift: la criticità cresce più velocemente del contratto

Un asset può cambiare ruolo senza cambiare una riga di SQL. Un analyst crea una tabella per una domanda ad hoc; il team la usa ogni settimana; una dashboard la incorpora; Finance comincia a citarla; un agente AI la include nel briefing executive. Tecnicamente è la stessa tabella. Operativamente è diventata infrastruttura.

Chiamiamo **ownership drift** questo scarto tra uso reale e responsabilità formale. I segnali sono consumer downstream in crescita, query e ticket che aumentano, uso in processi più critici, citazioni executive, dipendenze non dichiarate. Quando cambia il tier, devono cambiare anche owner, test, SLO, change policy e supporto.

La Fabric Adoption Roadmap esplicita un'idea simile: contenuti personali, di team, dipartimentali ed enterprise richiedono strategie di ownership e governance differenti; a livelli più maturi l'organizzazione identifica chiaramente ownership e conseguenze downstream dei cambiamenti.

Fonti:
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-content-ownership-and-management
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-content-delivery-scope

## Transfer test: il prodotto sopravvive al suo autore?

Una prova semplice di maturità è immaginare che l'owner tecnico cambi team domani. Se il successore deve ricostruire il prodotto interrogando colleghi e leggendo query a caso, il sistema è ancora dipendente dalla memoria personale.

Un handover serio dovrebbe consentire di ricostruire purpose, consumer, dependency map, SLO, test, runbook, known failure mode, accesso, costo, release process, debito aperto e retirement condition. Microsoft include esplicitamente il trasferimento di ownership tra le considerazioni di gestione dei contenuti: la proprietà non è un'etichetta statica, ma parte del lifecycle.

## Governance senza approval theater

Separare responsabilità non significa creare nove approvazioni per qualsiasi modifica. La stessa documentazione Microsoft raccomanda il modello di governance più leggero capace di raggiungere gli obiettivi, integrato nel normale workflow e bilanciato con empowerment e produttività.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-governance

La conseguenza operativa è risk-tiered: T0/T1 possono vivere con autonomia locale e standard minimi; T2 richiede ownership, supporto e change control espliciti; T3 può richiedere reconciliation indipendente, audit e approvazioni più forti. Governance uniforme su tutti gli asset è quasi sempre una cattiva allocazione di capacità.

Alla fine, il test dell'ownership è molto concreto. Per ogni metrica o prodotto business-critical dobbiamo sapere chi decide che cosa significa, chi può modificarlo, chi mantiene il servizio, chi riceve l'alert, chi può dichiararlo `not fit for decision`, chi approva un backfill, chi informa i consumer, chi paga il costo operativo e chi ne decide il retirement. Se la risposta ricorrente è soltanto “il data team”, non abbiamo ancora un ownership model: abbiamo un'etichetta.

> **Una metrica diventa infrastruttura quando la sua responsabilità resta comprensibile anche dopo che le persone che l'hanno costruita sono cambiate.**

Questa chiarezza ci permette di definire il passo successivo: quale livello di affidabilità promette davvero il servizio e come dichiara che quella promessa, oggi, non è rispettata.