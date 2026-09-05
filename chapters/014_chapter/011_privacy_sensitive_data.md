## 14.10 Privacy e dati sensibili: progettare il data boundary prima del prompt

L'AI-assisted analytics rende facilissimo prendere un estratto, incollarlo in un sistema generativo e chiedere di trovare pattern. Questa facilità può invertire l'ordine professionale corretto. La prima domanda non è "il modello sa analizzare questo dataset?", ma:

> **Per quale scopo stiamo trattando questi dati, quali informazioni sono davvero necessarie e quale sistema è autorizzato a riceverle?**

Questa sezione non è una guida legale. È una disciplina operativa per evitare che l'AI allarghi silenziosamente la superficie dei dati usati dall'analisi.

### Purpose limitation e minimizzazione

La Commissione europea riassume tra i principi del GDPR purpose limitation, data minimisation, storage limitation, integrity/confidentiality e accountability. La conseguenza pratica è importante: **"potrebbe essere utile al modello" non è una giustificazione sufficiente per includere una colonna**. Prima definiamo lo scopo; poi costruiamo il dataset minimo compatibile con quello scopo.

Fonti:

- https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en

### Data Exposure Review

Prima di inviare dati a un sistema AI, classifichiamo almeno identificatori diretti, quasi-identificatori, testo libero, categorie sensibili, dati commerciali riservati, secret/credential e campi non necessari. Il risultato non è "privacy sì/no". È un **data boundary esplicito**.

Prendiamo 180.000 ticket Customer Experience. L'export iniziale contiene nome, email, numero d'ordine, testo completo, note interne, categoria prodotto, paese ed esito. Per clustering tematico nome ed email non servono quasi mai; spesso non serve nemmeno il numero d'ordine. Le note interne possono contenere informazioni fuori scopo. Una vista dedicata può quindi esporre:

```text
ticket_id pseudonimizzato
clean_text
macro_categoria_prodotto
paese
mese
outcome
```

con redaction o trattamento separato per pattern sensibili nel testo. La qualità analitica può restare quasi invariata mentre la superficie di esposizione diminuisce drasticamente.

### Pseudonimizzato non significa anonimo

Sostituire `customer_id` con un token riduce il rischio, ma non rende automaticamente anonimo il dataset. Se altre informazioni permettono ragionevolmente di ricondurre il record a una persona, il dato resta identificabile nel contesto rilevante. L'EDPB, nell'Opinion 28/2024 sui modelli AI, sottolinea proprio che l'anonimato richiede una valutazione caso per caso.

Fonte: https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en

Per il Data Analyst la regola è semplice: **pseudonimizzazione è una misura di riduzione del rischio, non un lasciapassare universale**.

### Minimizzare prima di trasferire

Quando possibile spostiamo il calcolo verso il dato e portiamo al modello soltanto ciò che serve. Invece di trasferire due milioni di transazioni con identificatori individuali, potremmo usare aggregati per segmento, profili statistici, campioni autorizzati o query result già minimizzati. Questa scelta può migliorare contemporaneamente privacy, costo, velocità, leggibilità del contesto e verificabilità.

### Least privilege per gli agenti

Un agente collegato al warehouse non dovrebbe ereditare automaticamente i privilegi del suo sviluppatore. Il pattern professionale è:

```text
identity separata
→ dataset / tool allowlist
→ colonne o viste necessarie
→ read-only di default
→ write esplicitamente autorizzato
→ credenziali revocabili
→ audit log
```

Microsoft, nel proprio AI agent shared responsibility model, mantiene in capo al deployer dati, identity/least privilege, authorization e human oversight.

Fonte: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

### Il testo libero nasconde altri dati

Una tabella strutturata espone almeno le colonne che contiene. Un ticket, una nota CRM o una trascrizione può invece includere email, indirizzi, dati sanitari, informazioni finanziarie, password copiate per errore, segreti aziendali o informazioni su terzi. Autorizzare la colonna `ticket_text` non basta: dobbiamo chiederci **che cosa può contenere dentro i valori**.

### Quando serve escalation di governance

Prima di usare un servizio esterno vanno chiariti prodotto/tenant, data-handling terms, retention/logging, eventuali usi ulteriori, controlli amministrativi e processo di approvazione secondo le policy dell'organizzazione. Il Data Analyst non deve improvvisare una valutazione legale del fornitore; deve riconoscere quando il workflow richiede Security, Privacy, Legal o DPO.

La stessa disciplina vale per richieste ad alto impatto. Se qualcuno chiede di caricare tutte le exit interview e identificare chi potrebbe lasciare l'azienda, il lavoro non comincia dal prompt. Comincia da finalità, categorie di dati, autorizzazione, necessità/proporzionalità, ruolo umano nella decisione e obblighi applicabili.

La AI Analysis Control Sheet registra quindi processing purpose, data owner, ambiente approvato, categorie di dati, minimum fields, redaction/pseudonymisation, agent identity, read/write scope, eventuale third-party transfer, retention/logging e approvazioni richieste.

> **La potenza dell'AI non è una ragione per ampliare il dataset. Un workflow maturo dimostra prima quale minima evidenza serve e costruisce il confine dei dati intorno a quello scopo.**
