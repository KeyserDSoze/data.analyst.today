## 14.10 Privacy e dati sensibili: progettare il data boundary prima del prompt

L'AI-assisted analytics rende estremamente facile prendere un estratto di dati, incollarlo in un sistema generativo e chiedere:

> “Trova i pattern più importanti.”

Questa facilità può invertire l'ordine professionale corretto.

La prima domanda non è:

> “Il modello sa analizzare questo dataset?”

È:

> **“Per quale scopo stiamo trattando questi dati, quali dati sono davvero necessari e quale sistema è autorizzato a riceverli?”**

Questa sezione non è una guida legale. È una disciplina operativa per evitare che l'AI allarghi silenziosamente la superficie dei dati usati dall'analisi.

### Purpose limitation prima della curiosità analitica

La Commissione europea riassume tra i principi del GDPR:

- **purpose limitation** — il trattamento deve avere uno scopo specifico;
- **data minimisation** — vanno trattati solo i dati adeguati, pertinenti e necessari a quello scopo;
- **storage limitation**;
- **integrity and confidentiality**;
- **accountability**.

Fonti:

- European Commission, *Principles of the GDPR*: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- European Commission, *Obligations — Data protection by design and by default*: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en

La conseguenza pratica per l'analista è importante:

> **“potrebbe essere utile al modello” non è una giustificazione sufficiente per includere una colonna.**

### Il Data Exposure Review

Prima di inviare dati a un sistema AI, classifichiamo ciò che il workflow vorrebbe usare.

| Categoria | Domanda operativa |
|---|---|
| Identificatori diretti | servono davvero nome, email, telefono, account number? |
| Quasi-identificatori | combinazioni di età, località, ruolo o timestamp possono re-identificare? |
| Testo libero | contiene dati personali, segreti, note interne o informazioni non strutturate inattese? |
| Dati sensibili / speciali | esiste una ragione e un processo autorizzato per trattarli? |
| Dati commerciali riservati | il sistema e il canale sono approvati per riceverli? |
| Credenziali / token / secret | devono essere esclusi dal contesto e gestiti fuori dal prompt? |
| Dati non necessari | possiamo eliminarli prima dell'elaborazione? |

Il risultato non è “privacy sì/no”.

È un **data boundary esplicito**.

### Caso simulato/composito — classificare 180.000 ticket senza esporre tutto

Un team Customer Experience vuole classificare 180.000 ticket per capire le principali cause di insoddisfazione.

Il primo export contiene:

- nome cliente;
- email;
- numero d'ordine;
- testo completo del ticket;
- note interne dell'operatore;
- categoria prodotto;
- paese;
- esito della richiesta.

Per il clustering tematico, nome ed email non servono.

Spesso non serve nemmeno il numero d'ordine.

Le note interne possono inoltre contenere informazioni non necessarie al task.

Una vista dedicata espone invece:

```text
ticket_id pseudonimizzato
clean_text
macro_categoria_prodotto
paese
mese
outcome
```

con un processo separato per redigere pattern sensibili dal testo libero quando necessario.

La qualità dell'analisi tematica può restare quasi invariata mentre la superficie di esposizione diminuisce drasticamente.

### Pseudonimizzato non significa anonimo

Sostituire `customer_id` con un token non trasforma automaticamente il dataset in dato anonimo.

Se altri attributi consentono di ricondurre ragionevolmente il record a una persona, il rischio resta.

L'EDPB, nel Parere 28/2024 sui modelli AI, sottolinea che la valutazione dell'anonimato richiede un'analisi caso per caso e considera, tra le altre cose, la probabilità di identificazione diretta o indiretta e di estrazione di dati personali dal modello.

Fonti:

- EDPB, *Opinion 28/2024*: https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en
- sintesi EDPB: https://www.edpb.europa.eu/news/edpb-opinion-on-ai-models-gdpr-principles-support-responsible-ai_en

Per il Data Analyst la regola è semplice: **pseudonimizzazione è una misura di riduzione del rischio, non un lasciapassare universale**.

### Minimizzare prima di trasferire

Quando possibile, spostiamo il calcolo verso il dato e portiamo al modello solo ciò che serve.

Invece di inviare:

```text
2 milioni di transazioni con identificatori individuali
```

potremmo inviare:

```text
aggregati per segmento
metriche diagnostiche
campione autorizzato
schema + profilo statistico
query result già minimizzato
```

Questa scelta può migliorare contemporaneamente:

- privacy;
- costo;
- velocità;
- leggibilità del contesto;
- verificabilità.

### Least privilege per gli agenti

Un agente collegato al warehouse non dovrebbe ereditare automaticamente i privilegi del suo sviluppatore.

Il principio operativo è:

```text
identity separata
→ dataset allowlist
→ colonne/viste necessarie
→ read-only di default
→ azioni write esplicitamente autorizzate
→ credenziali revocabili
→ audit log
```

Microsoft, nel modello di responsabilità condivisa per agenti AI, indica esplicitamente tra le responsabilità del deployer identità, least privilege, autorizzazione delle azioni, supervisione umana e governance dei dati.

Fonte: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

Microsoft documenta inoltre pattern di least privilege per agent identity, allowlist delle azioni, audit log e revoca.

Fonte: https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents

### Testo libero: il dato che nasconde altri dati

Una tabella strutturata mostra almeno le colonne che contiene.

Il testo libero è più insidioso.

Un ticket, una nota CRM o una trascrizione può contenere:

- email;
- indirizzi;
- dettagli sanitari;
- informazioni finanziarie;
- password copiate per errore;
- segreti aziendali;
- dati su terze persone.

Per questo “la colonna `ticket_text` è autorizzata” non basta.

Serve chiedersi cosa può contenere **dentro i valori**.

### Terze parti e sistema approvato

Prima di usare un servizio esterno vanno chiariti, secondo i processi dell'organizzazione:

- quale prodotto/tenant stiamo usando;
- quali data-handling terms si applicano;
- dove e come vengono elaborati i dati;
- quali retention/logging sono previsti;
- se i dati possono essere usati per scopi ulteriori;
- quali controlli amministrativi esistono;
- chi ha approvato il caso d'uso.

Il Data Analyst non deve improvvisare una valutazione legale del fornitore.

Deve sapere **quando il workflow supera il proprio perimetro e richiede Security, Privacy, Legal o DPO**.

### Data protection by design, non filtro finale

La Commissione europea descrive la protezione dei dati by design/by default come misure integrate fin dalle prime fasi, incluso trattare per default solo i dati necessari e limitarne l'accessibilità.

Questo si traduce bene in AI analytics:

```text
purpose
→ minimum dataset
→ approved environment
→ least-privilege access
→ transformation/redaction
→ model interaction
→ output review
→ retention/deletion policy
```

Aggiungere una nota “non condividere dati sensibili” alla fine del progetto è troppo tardi.

### Caso ad alto rischio: quando fermarsi prima dell'analisi

Se un analyst riceve una richiesta come:

> “Carica tutte le exit interview e identifica quali dipendenti potrebbero lasciare l'azienda.”

non dovrebbe iniziare ottimizzando il prompt.

Prima deve chiarire:

- finalità del trattamento;
- categorie di dati presenti;
- autorizzazione;
- necessità e proporzionalità;
- ruolo umano nella decisione;
- eventuali obblighi specifici dell'organizzazione e della giurisdizione.

La competenza professionale include anche riconoscere che **alcuni problemi richiedono governance prima dell'analytics**.

### Campo della AI Analysis Control Sheet

```text
processing purpose:
data owner:
approved AI environment:
data categories:
minimum fields required:
redaction/pseudonymisation:
agent identity:
read/write scope:
third-party transfer?:
retention/logging:
privacy/security approval required?:
output restrictions:
```

> **La potenza dell'AI non è una ragione per ampliare il dataset. Un workflow maturo dimostra prima quale minima evidenza serve e costruisce il confine dei dati intorno a quello scopo.**
