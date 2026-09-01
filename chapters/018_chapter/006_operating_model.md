## 18.5 Operating model: decentralizzare il lavoro senza decentralizzare la fiducia

Quando analytics cresce, la domanda organizzativa non è semplicemente:

> “Quanti analyst ci servono?”

È:

> **“Quali responsabilità devono stare vicino al dominio e quali capacità devono essere condivise?”**

Questa distinzione determina:

- velocità;
- qualità;
- ownership;
- duplicazione;
- supporto;
- governance;
- costi.

Un operating model fragile può rendere inefficace anche un'architettura eccellente.

## Tre failure mode opposti

### Centralizzazione totale

Tutto passa dal team data centrale.

Vantaggi:

- standard coerenti;
- competenza concentrata;
- governance più semplice.

Rischi:

- coda infinita;
- scarsa conoscenza del dominio;
- team centrale che diventa owner semantico di concetti che non può conoscere abbastanza bene;
- priorità lontane dal business.

### Federazione totale

Ogni dominio costruisce tutto.

Vantaggi:

- velocità locale;
- ownership vicina alla decisione;
- profonda conoscenza del business.

Rischi:

- metriche duplicate;
- infrastrutture replicate;
- policy incoerenti;
- costi più alti;
- scarsa interoperabilità.

### Centralized approval theater

Formalmente i domini sono autonomi, ma ogni decisione richiede numerosi approval centrali.

Il risultato può essere il peggio dei due mondi:

- responsabilità locale;
- autorità centrale;
- tempi lunghi;
- accountability confusa.

## Il principio: centralizzare capability, federare accountability dove serve

Un modello pratico può separare quattro funzioni.

### Domain analytics / data product team

Possiede vicino al business:

- use case;
- semantica locale;
- data product;
- decision feedback;
- parte del supporto.

### Shared analytics platform

Fornisce:

- orchestration;
- storage/query capability;
- CI/CD pattern;
- observability;
- catalog;
- access primitive;
- cost metadata;
- standard template.

La piattaforma dovrebbe ridurre lavoro ripetitivo, non diventare owner di ogni prodotto.

### Governance / risk / security

Definisce policy comuni dove la libertà locale produce rischio sistemico:

- privacy;
- identity;
- access;
- retention;
- data classification;
- audit;
- standard di interoperabilità.

### Analytics enablement / COE

Aiuta l'organizzazione a:

- diffondere pattern efficaci;
- formare creator e consumer;
- supportare community;
- misurare adoption;
- trasformare pratiche locali efficaci in standard riusabili.

Il COE non deve essere per forza una fabbrica di report né un comitato di veto.

## Caso reale documentato: AWS e i ruoli nel data mesh

AWS Prescriptive Guidance descrive un operating model in cui:

- i **domain team** possiedono i data product e allineano le priorità ai business use case;
- il **self-service data platform team** possiede e mantiene la piattaforma condivisa;
- il **governance team** garantisce standard e requisiti.

Fonte: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html

Non serve adottare formalmente un data mesh per usare questa distinzione.

È utile perché evita di confondere:

> **chi conosce il significato**

con

> **chi costruisce le capability comuni**.

## Caso reale documentato: Microsoft e Center of Excellence

La Microsoft Fabric Adoption Roadmap descrive un Center of Excellence come un team interno con competenze tecniche e business che aiuta attivamente la community analytics e promuove obiettivi di adozione coerenti con la data culture.

Fonte: https://learn.microsoft.com/it-it/power-bi/guidance/fabric-adoption-roadmap-center-of-excellence

La documentazione non impone che il COE sia l'owner di tutto.

Questa è una distinzione importante.

Un COE efficace può aumentare la capacità distribuita dell'organizzazione invece di accentrare ogni delivery.

## Caso simulato/composito: approval rate senza owner end-to-end

Una fintech monitora l'approval rate dei pagamenti.

Payments Engineering gestisce gateway e provider.

Risk modifica regole antifrode.

Finance misura il costo di false decline.

Analytics mantiene la dashboard.

Quando approval rate scende di 4 punti:

- Engineering controlla latency;
- Risk controlla fraud rule;
- Finance aspetta un numero riconciliato;
- Analytics produce breakdown.

Tutti sono responsabili di qualcosa.

Nessuno è accountable per la **health del decision process end-to-end**.

L'azienda introduce:

- decision owner: VP Payments;
- semantic owner: Payments Analytics + Finance per economics;
- product owner: analytics engineering;
- incident commander assegnato per SEV-1/2;
- common runbook;
- SLO e severity condivisi.

Non viene creato un nuovo team.

Viene creata una struttura di responsabilità.

## RACI è utile soltanto se cambia il comportamento

Una matrice RACI può chiarire:

- Responsible;
- Accountable;
- Consulted;
- Informed.

Ma fallisce quando:

- l'Accountable non ha autorità;
- il Responsible non ha capacity;
- tutti sono Consulted;
- nessuno possiede incidenti fuori orario;
- la matrice non viene aggiornata dopo riorganizzazioni.

Per ogni responsabilità dobbiamo chiedere:

- ha accesso ai sistemi?
- può approvare la modifica?
- riceve l'alert?
- ha tempo allocato alla manutenzione?
- ha un backup?
- è incentivato a investire nella reliability?

Ownership senza capacità operativa è documentazione, non operating model.

## Team boundary e product boundary devono allinearsi abbastanza

Un problema comune nasce quando un data product attraversa cinque team e nessuno può correggerlo end-to-end.

Più handoff esistono, più servono:

- contract;
- SLO;
- escalation;
- dependency ownership.

Non dobbiamo eliminare ogni dipendenza.

Dobbiamo evitare dipendenze senza promessa osservabile.

Esempio:

```text
CRM domain
  ↓ source contract
Revenue product
  ↓ certified metric contract
Executive pack
  ↓ decision deadline
CFO review
```

Ogni boundary deve indicare:

- cosa viene promesso;
- chi risponde;
- come il failure viene propagato.

## Escalation path

Un sistema critico dovrebbe avere un percorso più chiaro di:

> “scrivi nel canale #data-help”.

Esempio:

### T1

Owner di team durante business hours.

### T2

Primary owner + backup + escalation al decision owner se la deadline è a rischio.

### T3

Incident process formalizzato con authority per:

- bloccare pubblicazione;
- attivare fallback;
- sospendere change;
- informare stakeholder critici.

Il livello di reperibilità deve essere proporzionato al rischio.

Non ogni dashboard merita on-call.

## Support model

L'Analytics Operating Contract può distinguere:

### Consumer support

“Come uso il prodotto?”

### Data quality support

“Il dato non sembra corretto.”

### Access support

“Non posso accedere.”

### Incident

“Il prodotto critico è fuori SLO.”

### Change request

“Serve una nuova definizione o capability.”

Se tutto entra nello stesso backlog, le urgenze e il product development competono senza priorità leggibile.

## Operating model e prioritization

Un team che possiede prodotti in esercizio non può pianificare il 100% della capacità su nuove feature.

Serve budget per:

- reliability;
- incident;
- tech debt;
- semantic debt;
- cost optimization;
- deprecation;
- user support.

Altrimenti il portafoglio cresce e la capacità di mantenerlo non cresce con lui.

Questo è uno dei modi più comuni in cui un'organizzazione “scala” il numero di asset ma non la qualità del sistema.

## Toil analitico

Google SRE definisce **toil** come lavoro operativo manuale, ripetitivo e con scarso valore duraturo che tende a crescere linearmente con il servizio.

Fonte: https://sre.google/sre-book/part-II-principles/

In analytics il toil include:

- refresh manuale;
- correzioni ripetitive;
- mapping aggiornati a mano;
- ticket “quale tabella?”;
- reconciliation identica ogni settimana;
- recovery non automatizzata;
- access provisioning ripetitivo.

Non tutto il lavoro manuale è toil.

Un'indagine complessa può essere manuale e ad altissimo valore.

Il segnale di toil è:

> **il lavoro si ripete perché il sistema non ha ancora incorporato l'apprendimento.**

## Automazione come conseguenza del redesign

DORA avverte che continuous delivery non consiste nel ripetere più spesso il vecchio processo; senza miglioramenti a processo, architettura e capability, più deployment possono aumentare failure e burnout.

Fonte: https://dora.dev/capabilities/continuous-delivery/

Lo stesso vale per analytics operations.

Prima di automatizzare:

1. chiarire responsibility;
2. eliminare passaggi inutili;
3. definire contract;
4. standardizzare il caso ricorrente;
5. poi automatizzare.

Automatizzare un processo ambiguo produce ambiguità più veloce.

## Operating-model review

Ogni trimestre, un portfolio analitico può essere rivisto chiedendo:

- quali prodotti hanno owner chiari?
- quali hanno più consumer del tier previsto?
- dove il team centrale è collo di bottiglia?
- quali domain team dipendono da capability duplicate?
- quale toil cresce linearmente?
- quali incidenti attraversano troppi handoff?
- quali prodotti non hanno backup owner?
- quali asset dovrebbero essere ritirati?

## Una regola organizzativa

> **Federare significa spostare responsabilità vicino al contesto, non spostare il problema della qualità sul consumer. Centralizzare significa creare capability comuni, non assumere che un team centrale possa possedere il significato di tutta l'organizzazione.**

Un operating model scala quando autonomia e responsabilità crescono insieme.
