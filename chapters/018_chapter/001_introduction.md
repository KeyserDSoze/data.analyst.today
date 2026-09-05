# Capitolo 18 — Costruire un sistema analitico che scala

## 18.0 Quando un'analisi smette di essere un progetto e diventa un servizio

Il Capitolo 17 terminava con una domanda: qual è il minimo percorso di evidenza sufficiente per rendere difendibile **questa** decisione? Il Capitolo 18 comincia quando quella decisione non è più eccezionale. Torna ogni giorno, ogni lunedì alle 08:30 o a ogni chiusura mensile, e l'organizzazione non può permettersi di ricostruire ogni volta significato, controlli e responsabilità da zero.

A quel punto cambia la natura del problema. Una buona analisi può dipendere molto dalla competenza di chi la conduce. Un servizio analitico ricorrente, invece, deve continuare a funzionare quando cambiano persone, sorgenti, software, mapping, soglie e perfino il modo in cui il business definisce il fenomeno. **Scalare significa quindi trasferire una promessa analitica dalla memoria personale a un contratto operativo esplicito.** Non significa semplicemente schedulare la query che ieri abbiamo eseguito a mano.

Pensiamo a due lavori apparentemente simili. Nel primo, un'azienda valuta una sola volta l'ingresso in un nuovo mercato: costruiamo dataset, scenari, Decision Record e comunicazione; la decisione viene presa e non c'è alcun obbligo di trasformare ogni passaggio in infrastruttura permanente. Nel secondo, ogni lunedì il leadership team decide forecast commerciale, capacità, rischio di churn, margin e cash. Se il dato arriva dopo il meeting, se manca una sorgente senza che nessuno lo veda o se una metrica cambia significato senza preavviso, il processo decisionale è compromesso anche quando la pipeline risulta tecnicamente `SUCCESS`.

È in questa seconda situazione che un asset diventa un **servizio analitico interno**. Da quel momento non basta più chiedere se il numero sia corretto oggi. Dobbiamo sapere chi lo usa, quale decisione supporta, quanto è critico, chi ne possiede il significato, chi mantiene l'implementazione, quale affidabilità promettiamo, come segnaliamo uno stato degradato, come gestiamo una breaking change, quanto costa mantenerlo e quando deve essere ritirato.

## Il deliverable: Analytics Operating Contract

Il centro del capitolo è l'**Analytics Operating Contract**. Non è un contratto legale e non è una checklist da compilare per qualsiasi notebook. È la rappresentazione della promessa operativa che un prodotto analitico assume verso consumer riconoscibili.

Una versione completa può rendere esplicita questa catena:

```text
recurring decision / use case
→ criticality tier
→ product boundary + consumers
→ decision / semantic / technical ownership
→ source-of-truth contract
→ SLI / SLO + quality gates
→ serving states + degraded mode
→ observability + incident response
→ change / compatibility / backfill policy
→ self-service interface + governance
→ cost-to-serve + adoption
→ AI-agent profile if applicable
→ review / deprecation / retirement
```

La domanda sottostante è semplice e severa:

> **Se questa capacità deve continuare a funzionare senza il suo autore originale, che cosa dobbiamo rendere esplicito?**

Questa domanda impedisce anche l'errore opposto: industrializzare tutto. Reliability, monitoring, recovery e change control costano tecnologia e capacità umana. Un notebook esplorativo non merita lo stesso operating model di un feed che alimenta payout o closing finanziario. Per questo useremo **criticality tier** intenzionalmente semplici, non come standard universale ma come modo per collegare il rigore al costo del fallimento.

| Tier | Uso | Esempio | Aspettativa operativa |
|---|---|---|---|
| T0 — Exploratory | analisi personale/ad hoc | notebook EDA | best effort |
| T1 — Team | decisione locale ricorrente | dashboard settimanale | owner, test base, freshness visibile |
| T2 — Business-critical | processo decisionale rilevante | revenue review, capacity plan | SLO, incident process, controlled change, fallback |
| T3 — High-consequence | finanziario/regolatorio/operativo ad alto impatto | closing, payout, risk decision feed | reconciliation rigorosa, recovery, audit trace, change control forte |

Microsoft, nella Fabric Adoption Roadmap, distingue esplicitamente scope e strategie di ownership differenti per self-service, managed self-service ed enterprise, e lega la maturità a ownership, supporto, governance e change management proporzionati all'importanza del contenuto. Il punto trasferibile non è adottare Fabric: è che un asset personale e un prodotto essenziale al decision making non possono vivere con la stessa promessa operativa.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

## MercuryOne: quando il problema non è la manualità

Una società B2B SaaS, **MercuryOne**, produce ogni lunedì un executive revenue pack. Per due anni un senior analyst impiega circa quattro ore: esporta opportunità dal CRM, legge billing, riconcilia ARR, applica eccezioni enterprise, aggiorna forecast e file del CFO. Il processo funziona. Poi l'analyst cambia azienda.

Solo allora il team scopre che la definizione di expansion ARR non è documentata, tre eccezioni enterprise vivono in formule Excel, il mapping dei territori è in un file personale, il cut-off settimanale non è scritto, Sales e Finance usano snapshot diversi e nessuno sa chi debba essere avvisato se il dato non è pronto entro le 08:00.

La tentazione è concludere che il problema fosse la manualità e proporre subito un lakehouse, una nuova pipeline o una dashboard più moderna. Sarebbe una diagnosi incompleta. Il vero failure mode è che una capacità diventata **business-critical** era ancora operata come conoscenza personale. Automatizzare quel processo senza chiarire semantica, source of truth, owner, blocking gate e fallback avrebbe soltanto reso più veloce un sistema ambiguo.

MercuryOne deve prima esplicitare quale decisione supporta il pack, quali metriche sono authoritative, quale freshness serve davvero, chi può approvare un semantic change, quali errori devono bloccare la pubblicazione, quali possono produrre `READY WITH CAVEATS`, come riconciliare Finance e quale costo operativo è giustificato. L'architettura viene dopo, perché deve implementare quella promessa anziché inventarla.

## Due catene che devono restare collegate

Nei capitoli precedenti abbiamo costruito la catena che produce informazione:

**Sources → Contracts → Transformations → Tests → Metrics → Analytical Product → Decision → Feedback**.

Da qui in avanti le affianchiamo una seconda catena:

**Criticality → Ownership → SLO → Observability → Change → Incident → Cost → Adoption → Review → Retirement**.

La prima dice come nasce l'evidenza. La seconda mantiene nel tempo il diritto di fidarsi di quell'evidenza. Un sistema può essere tecnicamente elegante e fallire nella seconda catena: nessun owner, nessun degraded mode, costi senza accountability, metriche duplicate, asset certificati che nessuno usa più. Oppure può essere relativamente semplice e operativamente maturo perché la promessa è chiara, osservabile e trasferibile.

Questo chiarisce anche il rapporto con i capitoli 12–14. L'architettura del Capitolo 12 chiedeva da dove passa il dato e con quali garanzie; il tooling del 13 quale ambiente sia proporzionato al workflow; il 14 come controllare una singola esecuzione AI-assisted. Qui la domanda è differente: **chi mantiene la promessa nel tempo, come cambia e cosa succede quando non può essere mantenuta?** Lo stesso Operating Contract può governare una view SQL, un semantic model, una dashboard, un API data product, un modello ML o un agente AI ricorrente.

## Il lifecycle include anche la fine

Un prodotto analitico attraversa un lifecycle:

```text
explore
→ prove value
→ operationalize
→ scale
→ maintain
→ evolve
→ deprecate
→ retire
```

Molte organizzazioni progettano con cura le prime quattro fasi e lasciano le ultime alla buona volontà. È così che si accumulano dashboard zombie, metriche duplicate, tabelle senza owner, agenti orfani e costi che nessuno sa più collegare a una decisione. **Retirement non è pulizia cosmetica: è una parte della scalabilità.** Un portfolio che sa soltanto aggiungere asset aumenta la superficie operativa più velocemente della capacità di governarla.

La tesi del capitolo può quindi essere formulata in modo netto:

> **Scalare l'analytics non significa automatizzare una risposta. Significa rendere mantenibile la promessa che quella risposta continuerà ad avere lo stesso significato, la qualità necessaria, un costo giustificabile e un owner quando qualcosa cambierà.**

Nei prossimi passaggi costruiremo quella promessa partendo dall'ownership, poi dalla reliability e dagli stati di servizio; soltanto dopo arriveremo a self-service, change, delivery, testing, economics, adoption e agenti. L'ordine conta: senza responsabilità e failure boundary, le capability successive rischiano di industrializzare soltanto l'ambiguità.