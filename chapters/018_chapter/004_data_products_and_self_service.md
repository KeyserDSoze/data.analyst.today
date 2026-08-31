## 18.3 Data products e self-service
Il self-service analytics viene spesso descritto come la possibilità per gli utenti business di interrogare autonomamente i dati.

Ma questa definizione è incompleta.

Se ogni team costruisce le proprie metriche, duplica trasformazioni e interpreta i campi in modo diverso, abbiamo self-service tecnico ma non self-service affidabile.

Il vero obiettivo è ridurre la dipendenza dal team centrale **senza moltiplicare incoerenza e rischio**.

## Data as a product

La documentazione Databricks aggiornata nel 2026 descrive esplicitamente il principio di trattare i dati come prodotti con definizione chiara, schema, lifecycle, qualità crescente e responsabilità definite. L'idea è che i consumer possano scoprire e utilizzare dati affidabili senza dover aprire ogni volta una richiesta a un team centrale.

Questo cambia il modo di pensare.

Un dataset non è più soltanto l'output di una pipeline.

È qualcosa con:

- utenti;
- bisogni;
- interfaccia;
- documentazione;
- qualità attesa;
- owner;
- lifecycle;
- feedback.

## Dal dataset al prodotto

Consideriamo una tabella `customer_360`.

Tecnicamente contiene:

- customer_id;
- acquisition_channel;
- first_order_date;
- lifetime_revenue;
- current_plan;
- churn_flag;
- support_tickets;
- last_login.

Questo non la rende automaticamente un buon data product.

Dobbiamo sapere:

- chi la usa;
- per quali decisioni;
- quanto è fresca;
- quali campi sono certificati;
- quali sono derivati;
- come vengono gestiti merge e identity resolution;
- quali dati sensibili contiene;
- quale grain rappresenta;
- chi risponde delle anomalie.

## Caso realistico: il dataset che nessuno vuole usare

Un team data costruisce una customer master table con oltre 400 colonne.

Il progetto dura nove mesi.

Tecnicamente è impressionante.

Dopo il rilascio, i team Marketing e Customer Success continuano però a usare i propri export.

Perché?

Marketing non trova una definizione affidabile di campaign source.

Customer Success non sa se il customer_id rappresenti account o legal entity.

Finance non si fida del lifetime revenue perché non riconcilia con billing.

Il problema non era la quantità di dati.

Era che il prodotto era stato progettato intorno alle sorgenti, non ai consumer.

Il redesign parte da tre use case:

1. segmentazione campagne;
2. retention analysis;
3. account health review.

Il team riduce il core model a 72 campi, certifica le metriche principali, separa campi sperimentali, aggiunge lineage e owner.

L'utilizzo cresce non perché il dataset contiene più informazioni, ma perché contiene **meno ambiguità**.

## Self-service ha bisogno di guardrail

Un ambiente self-service maturo offre libertà entro confini chiari.

Per esempio:

- accesso a metriche certificate;
- sandbox per esplorazioni;
- dati sensibili con policy esplicite;
- naming standard;
- template di test;
- catalogo;
- semantic layer;
- percorsi di escalation.

L'alternativa è creare una falsa scelta tra centralizzazione totale e anarchia.

## Federazione con standard comuni

Una struttura utile è:

- domini business responsabili dei propri data product;
- piattaforma centrale responsabile degli standard e dell'infrastruttura;
- governance trasversale per sicurezza, lineage e qualità;
- metriche condivise per i concetti inter-domain.

Microsoft, nelle linee guida 2026 per i data processing standards, raccomanda standard organizzativi per ingestion, transformation e publishing dei data product, con publishing governato e scoperta centralizzata. Il punto non è il prodotto specifico: è il principio di separare autonomia locale e standard globali.

## Il test del self-service

Un buon prodotto dovrebbe permettere a un analyst competente di rispondere a una domanda ricorrente senza dover chiedere ogni volta:

- quale tabella devo usare?
- quale colonna è corretta?
- perché i numeri non tornano?
- questo campo è ancora mantenuto?
- chi devo contattare?

Se queste domande restano inevitabili, il prodotto non è ancora davvero self-service.

## Product thinking per i dati

Possiamo applicare concetti tipici del product management:

### User

Chi consuma il prodotto?

### Problem

Quale decisione deve prendere?

### Promise

Che livello di qualità e freshness garantiamo?

### Interface

Come viene consumato: SQL, API, semantic layer, dashboard?

### Feedback

Come scopriamo se il prodotto è utile o confonde?

### Deprecation

Come ritiriamo una versione senza rompere i consumer?

## Una frase chiave

> **Un data product non è una tabella ben costruita. È una promessa mantenibile tra chi produce dati e chi prende decisioni.**

La scala non nasce quindi dal duplicare più velocemente dataset e dashboard.

Nasce dal creare componenti affidabili che possano essere riutilizzati senza ricostruire ogni volta significato, qualità e fiducia.

## Fonti

- Databricks, *Guiding principles*: https://docs.databricks.com/gcp/en/lakehouse-architecture/guiding-principles
- Microsoft, *Data Processing Standards for AI and Analytics*: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/data/operational-standards-data-processing-standards-unify-data-platform
