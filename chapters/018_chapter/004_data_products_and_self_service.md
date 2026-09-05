## 18.3 Data product e self-service: autonomia senza trasferire l'ambiguità

Il self-service analytics viene spesso descritto come la possibilità per gli utenti business di accedere ai dati senza aprire ticket al data team. È una definizione troppo debole. Se l'utente non deve più aspettare una coda, ma deve comunque indovinare quale tabella usare, quale metrica sia authoritative, quale data rappresenti l'evento giusto, quali righe siano complete e chi contattare quando i numeri non tornano, non abbiamo eliminato il costo: **lo abbiamo spostato sul consumer**.

Il self-service maturo nasce quindi dalla sezione precedente. Ownership, serving state e reliability non sono controlli esterni al prodotto; sono parte dell'esperienza che permette al consumer di usarlo senza ricostruire ogni volta il contesto. Il punto non è rendere tutto interrogabile. È incorporare abbastanza significato e guardrail da rendere economico il comportamento corretto.

## Un data product è una promessa, non una tabella

Una tabella ben modellata o una dashboard molto usata non diventano automaticamente un data product. Il salto avviene quando esistono consumer riconoscibili e una promessa mantenibile. L'Analytics Operating Contract deve rendere espliciti almeno purpose, consumer, contract, reliability, ownership e lifecycle. In altre parole: quale problema supportiamo, per chi, che cosa può essere assunto stabile, quali gate proteggono l'output, chi risponde del servizio e come verrà cambiato o ritirato.

AWS descrive il data mesh attraverso domain ownership, data as a product, self-service platform e federated governance; nella Prescriptive Guidance distingue inoltre domain team, platform team e governance team. Non serve adottare formalmente un data mesh per usare la lezione organizzativa: il dominio possiede significato e use case, la piattaforma fornisce capability comuni, la governance definisce guardrail che non possono essere locali.

Fonti:
- https://aws.amazon.com/what-is/data-mesh/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html

## Il Customer 360 da 400 colonne che nessuno vuole usare

Un team costruisce `customer_360` in nove mesi. La tabella contiene oltre 400 colonne: identity, campagne, revenue, piani, utilizzo, supporto, churn, score e decine di flag. Tecnicamente è ricca. Dopo il rilascio, però, Marketing continua a usare il proprio export, Customer Success un mart locale, Finance non si fida di `lifetime_revenue` e Product costruisce una nuova tabella.

La prima interpretazione potrebbe essere “manca adoption” o “serve un catalogo migliore”. Ma tutti conoscono già l'asset. Il problema è la **trust usability**. Marketing non sa se `campaign_source` sia first touch o latest touch; Customer Success non sa se `customer_id` rappresenti account, workspace o legal entity; Finance non riconcilia revenue con billing; Product vede campi cambiare senza notice.

Il redesign parte dai consumer, non dalle colonne disponibili. Il team seleziona tre use case — campaign segmentation, retention analysis, account health review — e per ciascuno definisce grain, decisione, metriche authoritative, freshness, access boundary, known limitations, owner, query pattern ed escalation. Il core model scende a 72 campi; feature sperimentali e use case non compatibili vengono separati. L'uso cresce perché diminuisce l'ambiguità, non perché aumenta il volume del prodotto.

## Product boundary: una buona promessa dice anche cosa non promette

Un oggetto chiamato `customer_360` invita al riuso oltre il proprio design. Un boundary più onesto può chiamarsi `Customer Lifecycle Core` e promettere identity certificata per analytics, acquisition source authoritative, lifecycle dates, recurring revenue, activity aggregates e support summary. Può contemporaneamente dichiarare fuori scope real-time personalization, credit scoring, raw clickstream completo, attribution causale e legal master-data authority.

Questa parte negativa del contratto è fondamentale. Un prodotto self-service è più sicuro quando il consumer sa rapidamente **what, who, when, how good, how to use, what not to do, what changed e where to go**. Se servono cinque meeting per rispondere, l'asset è discoverable ma non self-service.

## Certified, exploratory e restricted non sono la stessa superficie

L'autonomia cresce quando il sistema distingue chiaramente la promessa. Una **certified zone** può contenere metriche authoritative, owner, SLO e compatibilità controllata. Una **exploration zone** può consentire sandbox e dati sperimentali con reliability più bassa. Una **restricted zone** protegge dati sensibili con purpose limitation e audit. Una **published product zone** espone asset destinati al riuso, con contract e lifecycle espliciti.

Lo scopo non è creare quattro piattaforme. È evitare due estremi: centralizzazione in cui ogni domanda passa dal team data e anarchia in cui ogni consumer deve ricostruire semantica, qualità e policy da zero.

Microsoft formula un principio analogo nella Fabric Adoption Roadmap: la governance funziona meglio quando bilancia controllo ed empowerment, usa il modello più leggero capace di raggiungere gli obiettivi e rende semplice seguire le regole all'interno del normale workflow.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-governance

Questa è l'idea della **paved road**: template di data product, default sicuri, test standard, catalogazione, lineage, naming, CI/CD, cost metadata e support channel riducono il lavoro ripetitivo. L'autonomia cresce perché non dobbiamo reinventare i guardrail a ogni use case.

## Il team centrale non può possedere il significato di tutto

Un central team può costruire ottime capability e diventare comunque collo di bottiglia se deve essere semantic owner di supply chain, risk, finance, marketing, product e supporto. Un operating model federato separa meglio le responsabilità: domain ownership per significato e valore locale; platform capability per primitive riutilizzabili; federated governance per privacy, security, identity, interoperability, certification e audit.

AWS Prescriptive Guidance rende questa separazione concreta: i domain team creano e mantengono data product e use case; il self-service platform team possiede e mantiene la piattaforma; il governance team definisce principi e guardrail. La struttura non è un dogma architetturale, ma un buon antidoto all'idea che “self-service” significhi semplicemente dare accesso al warehouse.

Fonte: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html

## Supporto e interfaccia fanno parte del prodotto

Self-service non significa assenza di supporto. Significa spostare il supporto dalle domande ripetitive ai problemi che richiedono giudizio. Ticket per 100 consumer, time-to-first-success, misunderstanding semantici, dipendenze create correttamente e tempo per trovare l'owner sono metriche molto più informative del semplice numero di utenti abilitati. Se i consumer raddoppiano e i ticket raddoppiano allo stesso ritmo, abbiamo scalato il pubblico, non il self-service.

Anche l'interfaccia deve seguire il consumer. La stessa boundary può essere esposta via SQL view, semantic layer, API, dashboard, notebook template o feature service. Democratizzazione non significa mostrare a tutti lo stesso livello tecnico: il self-service di un analyst SQL e quello di un sales manager sono problemi differenti.

## Adoption come feedback, non come applausometro

Usage è un segnale, non una prova di valore. Un asset molto interrogato può esserlo perché non esistono alternative. Un asset poco usato può essere essenziale a un closing trimestrale. Per questo la scorecard di un data product dovrebbe leggere insieme **trust, usability, reuse e decision value**: SLO e incident; discoverability e support burden; consumer indipendenti e duplicazioni ritirate; processi decisionali supportati e valore creato dove misurabile.

> **Un data product non scala perché molte persone possono accedervi. Scala quando molte persone possono usarlo correttamente senza ricostruire ogni volta significato, fiducia e responsabilità.**

Ma una promessa self-service stabile deve anche poter cambiare. Il prossimo problema è quindi il più insidioso: come evolvere un prodotto senza lasciare che una breaking change venga scoperta retroattivamente nel meeting in cui il numero è già stato usato.