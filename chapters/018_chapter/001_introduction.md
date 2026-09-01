# Capitolo 18 — Costruire un sistema analitico che scala

## 18.0 Quando un'analisi smette di essere un progetto e diventa un servizio

Una buona analisi risolve una decisione.

Un buon sistema analitico evita che la stessa decisione debba essere ricostruita da zero ogni settimana.

Questo capitolo comincia esattamente dove termina il capstone.

Nel Capitolo 17 abbiamo imparato a selezionare il minimo percorso di evidenza necessario per una decisione complessa.

Ora la domanda cambia:

> **Che cosa succede quando quella decisione torna ogni giorno, ogni lunedì o a ogni chiusura mensile?**

Se continuiamo a risolverla come un progetto ad hoc, il costo cresce con l'organizzazione.

L'analista diventa un collo di bottiglia.

La conoscenza resta nella memoria di poche persone.

Le eccezioni si accumulano in query locali e fogli di calcolo.

Le metriche divergono.

E quando il sistema fallisce, spesso lo scopre per primo il business.

Scalare significa trasferire una capacità analitica ricorrente dalla **memoria personale** a un **contratto operativo esplicito**.

Non significa soltanto automatizzarla.

## Il salto di natura

Consideriamo due situazioni.

### Situazione A — analisi occasionale

Un'azienda valuta se entrare in un nuovo mercato.

L'analista costruisce:

- dataset;
- scenari;
- Decision Record;
- presentazione.

La decisione viene presa.

Il lavoro può essere archiviato.

Non è necessario trasformare ogni query in infrastruttura permanente.

### Situazione B — processo ricorrente

Ogni lunedì alle 08:30 il leadership team decide:

- forecast commerciale;
- capacità operativa;
- rischi di churn;
- azioni su margin e cash.

Se il report non arriva, arriva tardi o cambia definizione senza preavviso, il processo decisionale viene compromesso.

Non stiamo più parlando di un documento.

Stiamo parlando di un **servizio analitico interno**.

E un servizio ha proprietà che un'analisi ad hoc può non avere:

- utenti riconoscibili;
- criticality;
- owner;
- livello di affidabilità atteso;
- dipendenze;
- change policy;
- supporto;
- incident management;
- costo di esercizio;
- lifecycle.

## Il deliverable del capitolo: Analytics Operating Contract

Il centro del capitolo sarà l'**Analytics Operating Contract**.

Non è un contratto legale.

È la scheda con cui rendiamo esplicito che cosa significa **operare** un prodotto analitico.

Una versione completa può contenere:

```text
recurring decision / use case
→ criticality tier
→ product boundary
→ consumers
→ decision / business owner
→ metric / semantic owner
→ technical / product owner
→ source-of-truth contract
→ reliability SLO
→ freshness / completeness / correctness indicators
→ test gates
→ observability
→ incident severity + escalation
→ fallback / degraded mode
→ version / change policy
→ backfill / replay policy
→ self-service interface
→ access / governance
→ cost-to-serve
→ adoption / decision-value metrics
→ AI-agent ownership if applicable
→ review cadence
→ deprecation / retirement criteria
```

Il contratto risponde a una domanda molto concreta:

> **“Se questa capacità deve continuare a funzionare senza il suo autore originale, che cosa dobbiamo rendere esplicito?”**

## Non tutto merita lo stesso livello operativo

Il primo errore del capitolo sarebbe trattare ogni dashboard come se fosse un sistema bancario critico.

L'affidabilità costa.

Servono:

- test;
- monitoring;
- supporto;
- ridondanza;
- recovery;
- change control;
- capacità umana.

Per questo introduciamo i **criticality tier**.

Un esempio semplice:

| Tier | Uso | Esempio | Aspettativa |
|---|---|---|---|
| T0 — Exploratory | analisi personale/ad hoc | notebook EDA | best effort |
| T1 — Team | decisioni locali ricorrenti | dashboard settimanale di team | owner + test base + freshness visibile |
| T2 — Business-critical | processo decisionale rilevante | revenue review, capacity plan | SLO, incident process, controlled change |
| T3 — High-consequence | regolatorio/finanziario/operativo ad alto impatto | closing, payout, risk decision feed | controlli rigorosi, reconciliation, fallback, audit trace |

Questi livelli non sono uno standard universale.

Servono a rendere visibile un principio:

> **la disciplina operativa deve essere proporzionata al costo del fallimento.**

Microsoft, nella roadmap di adozione di Fabric, distingue esplicitamente livelli differenti di ownership e governance in base a scope e criticità: self-service personale/team, managed self-service ed enterprise non richiedono gli stessi controlli. La stessa documentazione sottolinea che una soluzione considerata essenziale per il decision making richiede separazione tra sviluppo e produzione, change management controllato, aspettative di supporto chiare e governance più rigorosa.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

## Il confine con il Capitolo 12

Il Capitolo 12 chiedeva:

> “Da dove passa il dato e con quali garanzie?”

Il Capitolo 18 chiede:

> **“Chi risponde del servizio analitico nel tempo, quale affidabilità promette, come cambia e che cosa accade quando fallisce?”**

Possiamo avere un'architettura tecnicamente elegante e un operating model pessimo.

Oppure una pipeline semplice, ma ben posseduta, osservabile e proporzionata alla decisione.

Qui ci interessa soprattutto il secondo livello.

## Il confine con il Capitolo 13

Il Capitolo 13 decideva quale strumento o ambiente fosse proporzionato al workflow.

Qui il tool è secondario.

Un Analytics Operating Contract può governare:

- un modello SQL;
- un foglio controllato;
- una semantic layer;
- una dashboard;
- un API data product;
- un modello ML;
- una pipeline con agenti AI.

La domanda non è “qual è lo stack moderno?”.

È:

> **“Qual è il costo totale di mantenere questa promessa analitica?”**

## Il confine con il Capitolo 14

Il Capitolo 14 governa l'esecuzione AI-assisted:

- context boundary;
- permission boundary;
- verification;
- eval;
- human control.

Il Capitolo 18 aggiunge un'altra prospettiva:

> **chi mantiene l'agente dopo il go-live?**

Un agente ricorrente può avere:

- owner che lascia l'azienda;
- prompt o policy non aggiornati;
- credenziali troppo ampie;
- dipendenze che cambiano;
- output che nessuno controlla più;
- costi che crescono;
- consumer che continuano a fidarsi.

Questo è un problema di **operational lifecycle**, non di prompting.

## Caso simulato/composito: il weekly report che diventa infrastruttura

Una società B2B SaaS, **MercuryOne**, produce ogni lunedì un executive revenue pack.

All'inizio un senior analyst impiega quattro ore:

1. esporta opportunità dal CRM;
2. legge billing;
3. riconcilia ARR;
4. applica eccezioni enterprise;
5. aggiorna forecast e file del CFO.

Il processo funziona bene per due anni.

Poi il senior analyst cambia azienda.

Il team scopre che:

- la definizione di expansion ARR non è documentata;
- tre eccezioni enterprise vivono in formule Excel;
- il mapping dei territori è in un file personale;
- il cut-off settimanale non è scritto;
- la pipeline automatizzata non ha reconciliation con Finance;
- Sales e Finance usano due snapshot diversi;
- nessuno sa chi deve essere avvisato se il dato non arriva entro le 08:00.

Il problema non è che il vecchio processo fosse manuale.

Il problema è che una capacità diventata **business-critical** era ancora operata come conoscenza personale.

## Industrializzare non significa riscrivere tutto

MercuryOne potrebbe reagire così:

> “Portiamo tutto sul nuovo lakehouse.”

Ma non è ancora la domanda giusta.

Prima serve sapere:

- quale decisione supporta il prodotto;
- quali metriche sono authoritative;
- quale precisione/freshness serve davvero;
- chi decide una modifica semantica;
- come degradare se una sorgente manca;
- quali errori devono bloccare il report;
- quali possono essere segnalati come caveat;
- quanto vale mantenere il sistema.

Solo dopo queste risposte l'architettura può essere progettata in modo proporzionato.

## Il lifecycle del prodotto analitico

Un prodotto analitico attraversa fasi:

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

Molte organizzazioni progettano bene soltanto le prime quattro.

È così che si riempiono di:

- dashboard zombie;
- tabelle obsolete;
- metriche duplicate;
- pipeline senza owner;
- modelli che nessuno osa eliminare;
- costi infrastrutturali che nessuno collega più a un valore.

Il retirement non è pulizia cosmetica.

È parte della capacità di scalare.

## La tesi del capitolo

Il sistema operativo dell'analytics può essere riassunto con due catene.

### Catena del prodotto

**Sources → Contracts → Transformations → Tests → Metrics → Analytical Product → Decision → Feedback**

### Catena operativa

**Criticality → Ownership → SLO → Observability → Change → Incident → Cost → Adoption → Review → Retirement**

La prima produce informazione.

La seconda mantiene il diritto di fidarsi di quell'informazione nel tempo.

> **Scalare l'analytics non significa automatizzare una risposta. Significa rendere mantenibile la promessa che quella risposta continuerà ad avere lo stesso significato, la qualità necessaria e un owner quando qualcosa cambierà.**
