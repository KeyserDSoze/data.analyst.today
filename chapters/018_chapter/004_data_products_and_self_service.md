## 18.3 Data product e self-service: autonomia senza trasferire ambiguità al consumer

Il self-service analytics viene spesso riassunto così:

> “Gli utenti business possono accedere ai dati senza chiedere al data team.”

È una definizione insufficiente.

Se l'utente non deve aprire un ticket, ma deve comunque indovinare:

- quale tabella usare;
- quale metrica è autorevole;
- quale data rappresenta l'evento corretto;
- quali righe sono complete;
- chi contattare quando qualcosa non torna;

abbiamo eliminato una coda di supporto e trasferito il costo cognitivo al consumer.

Il self-service maturo non significa **assenza del team centrale**.

Significa che una parte rilevante del contesto necessario per usare bene il dato è incorporata nel prodotto, nei guardrail e nel sistema di supporto.

## Data product: output tecnico o promessa operativa?

Una tabella ben modellata non è automaticamente un data product.

Una dashboard molto usata non è automaticamente un data product.

Un data product esiste quando c'è una promessa mantenibile verso consumer riconoscibili.

Possiamo descriverlo con sei elementi.

### 1. Purpose

Quale problema o famiglia di decisioni supporta?

### 2. Consumer

Chi lo usa e con quale livello di competenza?

### 3. Contract

Che cosa può assumere stabile il consumer?

### 4. Reliability

Quali SLO e quality gate valgono?

### 5. Ownership

Chi risponde di significato, esercizio e cambiamento?

### 6. Lifecycle

Come viene evoluto, deprecato e ritirato?

Questa struttura entra nell'**Analytics Operating Contract**.

## Caso simulato/composito: il Customer 360 che nessuno vuole usare

Un team data costruisce `customer_360`.

Il progetto dura nove mesi.

La tabella contiene oltre 400 colonne:

- identity;
- campagne;
- revenue;
- piani;
- utilizzo;
- support;
- churn;
- score;
- decine di flag.

Tecnicamente è ricca.

Dopo il rilascio:

- Marketing continua a usare il proprio export;
- Customer Success usa un mart locale;
- Finance non utilizza `lifetime_revenue`;
- Product costruisce una nuova tabella.

### Perché?

Marketing non sa se `campaign_source` rappresenti first touch o latest touch.

Customer Success non sa se `customer_id` sia account, workspace o legal entity.

Finance non riesce a riconciliare revenue con billing.

Product trova campi che cambiano senza change notice.

Il problema non è la discoverability.

Tutti conoscono la tabella.

Il problema è la **trust usability**.

## Ridisegnare dal consumer verso la sorgente

Il team smette di chiedere:

> “Quali campi possiamo mettere nel Customer 360?”

E parte da tre use case:

1. campaign segmentation;
2. retention analysis;
3. account health review.

Per ogni use case definisce:

- grain;
- decisione;
- metriche authoritative;
- freshness;
- access boundary;
- known limitations;
- owner;
- query examples;
- escalation path.

Il core model scende a 72 campi.

Le feature sperimentali vengono separate.

I campi critici hanno definizioni e owner.

L'uso cresce perché il prodotto contiene **meno ambiguità**, non più colonne.

## Caso reale documentato: AWS e il concetto di data product

AWS descrive il data mesh come un modello che combina:

- domain-oriented ownership;
- data as a product;
- self-service platform;
- federated governance.

Nella stessa documentazione un data product viene descritto come una componente strutturata e riutilizzabile che serve un purpose business e può essere usata autonomamente da altri team, con standard comuni che favoriscono interoperabilità e qualità.

Fonte: https://aws.amazon.com/what-is/data-mesh/

La AWS Prescriptive Guidance separa inoltre responsabilità di:

- domain team, che possiedono i data product;
- self-service platform team, che mantiene capacità condivise;
- governance team, che garantisce standard e requisiti.

Fonte: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html

Questa struttura è utile come esempio organizzativo, non come dogma architetturale.

Non ogni azienda ha bisogno di “fare data mesh”.

Il principio trasferibile è:

> **la responsabilità del dominio e la piattaforma condivisa risolvono problemi differenti.**

## Product boundary: dove finisce la promessa?

Un prodotto chiamato `customer_360` può diventare pericolosamente ampio.

La product boundary deve dire che cosa il prodotto **non** promette.

Esempio:

`Customer Lifecycle Core` promette:

- customer identity certificata per analytics;
- acquisition source authoritative;
- lifecycle dates;
- recurring revenue;
- activity aggregates giornalieri;
- support summary.

Non promette:

- real-time personalization;
- credit scoring;
- raw clickstream completo;
- marketing attribution causale;
- legal master-data authority.

Un boundary chiaro riduce il rischio che lo stesso asset venga usato oltre il proprio design.

## Self-service contract

Un consumer dovrebbe poter sapere rapidamente:

### What

Che cosa rappresenta il prodotto?

### Who

Chi è owner?

### When

Quanto è fresco e quando viene aggiornato?

### How good

Quali SLO/test proteggono il dato?

### How to use

Quali interface e pattern sono supportati?

### What not to do

Quali interpretazioni sono fuori scope?

### What changed

Qual è la versione e quali breaking change recenti?

### Where to go

Dove segnalare problemi o chiedere supporto?

Se servono cinque meeting per rispondere a queste domande, il prodotto non è ancora davvero self-service.

## Self-service non è “puoi interrogare tutto”

Un ambiente maturo può separare superfici differenti.

### Certified zone

- metriche e data product authoritative;
- SLO;
- owner;
- documentazione;
- compatibilità controllata.

### Exploration zone

- sandbox;
- dati sperimentali;
- query ad hoc;
- expectation di reliability più bassa.

### Restricted zone

- dati sensibili;
- accesso motivato;
- purpose limitation;
- audit.

### Published product zone

- asset destinati al riuso organizzativo;
- contract esplicito;
- lifecycle e supporto.

Questo evita due estremi:

- centralizzazione in cui il team data deve rispondere a ogni domanda;
- anarchia in cui ogni utente deve ricostruire semantica e qualità.

## Governance come paved road

Una governance utile rende il comportamento corretto più semplice.

Microsoft, nella Fabric Adoption Roadmap, raccomanda una governance che bilanci controllo ed empowerment, usando il modello più leggero capace di soddisfare gli obiettivi e integrando le regole nel normale workflow degli utenti.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-governance

In pratica, una **paved road** self-service può offrire:

- template di data product;
- default di accesso sicuri;
- test standard;
- catalogazione automatica;
- lineage;
- naming;
- semantic definitions;
- CI/CD;
- cost tagging;
- support channel.

L'autonomia cresce perché non dobbiamo reinventare queste capacità ogni volta.

## Il central team non deve diventare un product factory universale

Un team centrale può essere molto bravo a costruire data mart.

Ma se deve conoscere in profondità:

- supply chain;
- risk;
- marketing;
- finance;
- product;
- customer support;

e diventare owner semantico di tutto, prima o poi diventa collo di bottiglia.

Un modello federato può separare:

### Domain ownership

Il dominio risponde del significato e del valore del proprio prodotto.

### Platform capability

La piattaforma fornisce strumenti e standard riutilizzabili.

### Federated governance

L'organizzazione definisce policy comuni per concetti che non possono essere locali:

- privacy;
- security;
- identity;
- naming;
- interoperability;
- certification;
- audit.

## Self-service support: una funzione del prodotto

Self-service non significa “nessun supporto”.

Significa spostare supporto da domande ripetitive a problemi ad alto valore.

Possiamo misurare:

- ticket per 100 consumer;
- percentuale di ticket già coperti da documentazione;
- time-to-first-success;
- query fallite per misunderstanding semantico;
- dipendenze create correttamente;
- tempo medio necessario per trovare l'owner.

Se l'uso aumenta ma i ticket crescono linearmente, il prodotto forse sta scalando i consumer, non il self-service.

## Interfaccia: non ogni consumer deve vedere il livello più basso

Lo stesso product boundary può essere servito tramite:

- SQL table/view;
- semantic layer;
- API;
- dashboard;
- notebook template;
- feature service.

L'interfaccia deve dipendere dal consumer.

Il self-service di un analyst SQL non è il self-service di un sales manager.

Un errore frequente è chiamare “democratizzazione” l'esposizione dello stesso livello tecnico a tutti.

## Feedback loop

Un prodotto senza feedback tende a seguire la propria roadmap invece del valore dei consumer.

Feedback utili:

- use case effettivi;
- query pattern;
- ticket;
- feature richieste;
- confusioni semantiche;
- decisioni supportate;
- consumer che hanno abbandonato il prodotto;
- asset duplicati costruiti altrove.

Una tabella molto interrogata può essere usata perché è l'unica disponibile.

Una tabella poco interrogata può essere essenziale a un closing trimestrale.

Usage da solo non misura product value.

## Data product scorecard

Un prodotto può essere valutato su quattro dimensioni.

### Trust

- SLO attainment;
- incident;
- reconciliation;
- semantic stability.

### Usability

- discoverability;
- documentation;
- time-to-first-answer;
- support burden.

### Reuse

- consumer indipendenti;
- duplicazioni ritirate;
- nuove analisi costruite senza re-implementare logica core.

### Decision value

- processi ricorrenti supportati;
- tempo risparmiato;
- qualità/velocità decisionale;
- valore economico dove misurabile.

> **Un data product non scala perché molti possono accedervi. Scala quando molti possono usarlo correttamente senza ricostruire da zero significato, fiducia e responsabilità.**
