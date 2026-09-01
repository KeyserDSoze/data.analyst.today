## 18.1 Ownership: chi decide il significato, chi mantiene il servizio, chi usa il numero

Quando un'organizzazione cresce, il problema raramente è la mancanza di metriche.

È la presenza di numeri senza una catena di responsabilità chiara.

Una metrica può essere:

- calcolata correttamente;
- documentata;
- disponibile in una semantic layer;
- usata da centinaia di persone;

ma diventare comunque fragile se nessuno sa chi abbia l'autorità di:

- cambiarne la definizione;
- approvare una breaking change;
- dichiararla non affidabile;
- decidere cosa fare quando due sistemi non riconciliano.

Per questo il primo blocco dell'Analytics Operating Contract non è il tool.

È l'**ownership model**.

## “Owner” è una parola troppo generica

Dire:

> “Finance è owner della revenue.”

non basta.

Finance potrebbe possedere la definizione economica, ma non la pipeline.

Analytics Engineering potrebbe mantenere il modello, ma non avere autorità per decidere quando una fattura debba entrare nella recognized revenue.

Il CFO potrebbe consumare il numero, ma non essere la persona che gestisce le eccezioni quotidiane.

È utile distinguere almeno quattro responsabilità.

### 1. Decision owner

È responsabile della decisione ricorrente supportata dal prodotto.

Esempio:

- CFO per il weekly revenue review;
- VP Operations per il capacity plan;
- Chief Risk Officer per una policy di credito.

Il decision owner risponde a:

> **“A quale decisione serve questa capacità e quali errori sono materialmente pericolosi?”**

### 2. Semantic / metric owner

È responsabile del significato business.

Decide o approva:

- definizione;
- popolazione;
- esclusioni;
- timing;
- trattamento delle eccezioni;
- breaking semantic change.

Il data team può proporre una formula più coerente.

Non dovrebbe però inventare unilateralmente che cosa significhi `recognized_revenue` o `active_customer`.

### 3. Product / technical owner

È responsabile del prodotto analitico in esercizio:

- implementazione;
- test;
- SLO;
- monitoring;
- incident response;
- release;
- documentation;
- cost-to-serve.

Può essere un analytics engineer, data engineer, BI team o team di dominio.

### 4. Steward / governance owner

Protegge aspetti trasversali:

- accesso;
- privacy;
- classificazione;
- retention;
- lineage;
- standard organizzativi;
- certification/deprecation.

Non tutte le organizzazioni useranno questi nomi.

La distinzione importante è evitare che **significato, esercizio e decisione** vengano trattati come un'unica responsabilità vaga.

## Caso simulato/composito: tre NRR nello stesso board pack

Una società SaaS prepara il board meeting.

Nella stessa presentazione compaiono:

- `NRR = 108%` nella slide Finance;
- `NRR = 104%` nella slide Customer Success;
- `NRR = 111%` nella slide Product.

Tutti i numeri sono matematicamente corretti.

Finance esclude contratti non ancora riconosciuti.

Customer Success usa soltanto account assegnati alle regioni gestite.

Product include expansion maturata entro 30 giorni dal rinnovo.

Il problema non è una query sbagliata.

Sono tre oggetti diversi chiamati con lo stesso nome.

### Prima reazione sbagliata

> “Costruiamo un unico dashboard certificato e vietiamo gli altri.”

La standardizzazione può essere necessaria per il board KPI, ma non implica che tutte le varianti siano inutili.

Customer Success può avere bisogno di una metrica operativa propria.

Product può aver bisogno di una cohort metric.

Il problema è **namespace + purpose + ownership**.

Il redesign definisce:

- **Board NRR** — authoritative per performance aziendale;
- **CS-managed NRR** — per gestione del portafoglio assegnato;
- **Product cohort NRR** — per analisi lifecycle.

Ogni metrica ha owner, scope e consumer differenti.

## La Metric Operating Card

Per una metrica critica, l'Analytics Operating Contract può includere una scheda minima:

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
| Freshness SLO | ready by 07:00 in 99% dei business day |
| Reconciliation | Finance ledger within agreed tolerance |
| Version | v3 |
| Status | certified |
| Review | quarterly + on material business change |

La formula è soltanto una riga.

Il resto descrive il diritto organizzativo del numero a essere usato.

## Ownership del dato sorgente e ownership della metrica non sono la stessa cosa

Il CRM owner può garantire che `account_id` e `contract_status` rispettino un contratto sorgente.

Non per questo decide come calcolare NRR.

Viceversa, Finance può definire la metrica ma non controllare direttamente:

- ritardi del CRM;
- schema change;
- duplicate contract;
- mapping account.

L'Operating Contract deve rendere visibili queste dipendenze.

Un prodotto analitico è spesso un **sistema di promesse concatenate**.

## Caso reale documentato: Microsoft e content ownership

La Microsoft Fabric Adoption Roadmap distingue tre strategie di ownership e gestione dei contenuti analitici:

- business-led self-service;
- managed self-service;
- enterprise.

La documentazione sottolinea che il livello di governance e supervisione deve dipendere da scope, sensibilità e importanza del contenuto per decisioni critiche, e che ownership e stewardship devono essere chiare.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-content-ownership-and-management

Questo è utile oltre Fabric.

Una dashboard personale e un board pack certificato non devono essere operati allo stesso modo.

Il problema nasce quando un asset nato come personale diventa de facto enterprise senza che l'ownership cambi con il suo impatto.

## Ownership drift

Un prodotto può cambiare criticità senza che nessuno se ne accorga.

Esempio:

1. un analyst crea una tabella per una domanda ad hoc;
2. il team la riusa ogni settimana;
3. una dashboard la incorpora;
4. Finance la usa per una decisione;
5. un agente AI la include in un executive brief.

Tecnicamente la tabella è la stessa.

Operativamente non lo è più.

Chiamiamo questo fenomeno **ownership drift**: l'uso del prodotto cresce più velocemente della sua responsabilità formale.

Un buon operating model cerca segnali di questo tipo:

- molti consumer downstream;
- uso in processi critici;
- aumento delle query;
- dipendenze non dichiarate;
- richieste di supporto;
- citazioni in report executive.

Quando il tier cambia, deve cambiare anche il contratto operativo.

## Ownership transfer: la prova che il sistema non dipende da una persona

Una delle migliori verifiche di maturità è chiedere:

> “Se l'owner tecnico cambia team domani, possiamo trasferire il prodotto senza ricostruirlo?”

Un handover dovrebbe includere:

- purpose;
- consumer;
- dependency map;
- SLO;
- test;
- runbook;
- known failure modes;
- cost;
- release process;
- access;
- open incident/debt;
- roadmap;
- retirement conditions.

Microsoft include esplicitamente gli **ownership transfer** tra i temi della gestione dei contenuti. Il punto è fondamentale: ownership non è un'etichetta statica; ha un lifecycle.

## La governance non deve trasformarsi in veto theater

Un errore opposto è costruire una matrice di approvazione enorme per qualsiasi modifica.

Microsoft raccomanda un modello di governance il più leggero possibile compatibilmente con gli obiettivi, bilanciando controllo ed empowerment e integrando le regole nel normale workflow degli utenti.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-governance

Questa idea può essere tradotta così:

- T0/T1: autonomia locale + standard minimi;
- T2: ownership e change control espliciti;
- T3: approvazioni, reconciliation e audit più rigorosi.

La governance è **risk-tiered**, non uniforme.

## Un test operativo dell'ownership

Per ogni metrica o data product business-critical chiediamo:

1. Chi decide che cosa significa?
2. Chi può modificarla?
3. Chi mantiene il sistema?
4. Chi riceve l'alert?
5. Chi può dichiarare il dato `not fit for decision`?
6. Chi approva un backfill?
7. Chi informa i consumer?
8. Chi paga il costo operativo?
9. Chi decide quando ritirarlo?

Se la risposta ricorrente è:

> “il data team”

probabilmente il modello è ancora troppo ambiguo.

> **Una metrica diventa infrastruttura quando non dipende più dalla memoria di chi l'ha scritta, ma da responsabilità che restano comprensibili anche quando le persone cambiano.**
