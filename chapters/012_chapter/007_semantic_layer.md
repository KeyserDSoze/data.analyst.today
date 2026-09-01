## 12.6 Semantic layer come serving boundary: pubblicare significato, non solo tabelle

Nel Capitolo 11 abbiamo già costruito la semantica delle metriche e l'Analytical Data Contract.

Qui ci interessa una domanda architetturale diversa:

> **Dove viene pubblicata quella semantica affinché dashboard, notebook, applicazioni e agenti non debbano ricostruirla separatamente?**

Il semantic layer è uno dei possibili **serving boundary** tra modelli analitici e consumer.

### Il percorso

Una struttura concettuale può essere:

```text
curated tables
      ↓
analytical models
      ↓
semantic layer
      ↓
BI / notebooks / natural-language analytics / applications
```

Il semantic layer non sostituisce i modelli sottostanti.

Espone in modo più consumabile:

- metriche;
- dimensioni;
- relazioni;
- gerarchie;
- calendario;
- nomi business;
- policy di accesso dove supportate.

### Il valore architetturale: ridurre accoppiamento

Senza un serving boundary condiviso, ogni consumer può diventare direttamente dipendente da:

- nomi fisici delle tabelle;
- dettagli dei join;
- colonne tecniche;
- cambiamenti di storage;
- business logic ripetuta.

Con un'interfaccia semantica stabile, parte di questa complessità viene nascosta dietro un contratto più vicino al linguaggio del business.

### Caso simulato/composito — SkyShop e tre conversion rate

SkyShop ha tre metriche legittime:

```text
session_to_order_conversion
user_to_purchase_conversion
checkout_to_paid_conversion
```

Il problema non è scegliere una sola conversion universale.

Il problema è evitare che tre dashboard espongano tutte la label `conversion_rate` senza spiegare quale fenomeno rappresentano.

Il lavoro semantico appartiene al Capitolo 11.

Il lavoro architetturale di questa sezione è:

> **rendere quelle tre definizioni disponibili attraverso un punto di consumo riconoscibile e governabile.**

### Caso reale documentato — metric views come semantic object

Databricks documenta le metric views come oggetti che centralizzano misure riusabili e dimensioni, così gli utenti possono interrogare le stesse definizioni senza duplicarne la logica nei singoli consumer.

Fonte: https://docs.databricks.com/aws/en/uc-semantics/metric-views

La tecnologia specifica può cambiare. Il pattern rimane:

```text
shared semantic definition
→ many consumers
```

### Il serving layer non corregge upstream data

Se `net_revenue` è costruita su refund mancanti, centralizzarla non la rende corretta.

Anzi, un errore centralizzato può propagarsi più velocemente.

Per questo il serving boundary deve dipendere da:

- modelli testati;
- lineage;
- owner;
- versioning;
- quality state.

Centralizzazione senza qualità crea **incoerenza coerente**: tutti sbagliano nello stesso modo.

### Il vantaggio durante un cambiamento

Supponiamo che una definizione certificata debba cambiare.

Con logica duplicata in 27 dashboard dobbiamo:

- trovare ogni copia;
- capire le differenze locali;
- modificare separatamente;
- verificare che nessuna sia rimasta indietro.

Con un serving boundary condiviso possiamo almeno sapere:

- quale definizione cambia;
- quali consumer dipendono da essa;
- quale versione stanno usando.

La lineage della sezione successiva diventa quindi essenziale.

### Semantic serving e AI

Quando un agente traduce linguaggio naturale in query, deve poter distinguere:

```text
raw amount
vs
recognized revenue
vs
net sales
```

Il semantic layer può ridurre lo spazio di ambiguità esponendo:

- metriche certificate;
- descrizioni;
- dimensioni supportate;
- relazioni valide.

Ma l'AI non deve interpretare “certificato” come “infallibile”.

Valgono ancora test, caveat e ownership.

### Campo della Data Flow Architecture Map

Nel nodo `SERVE` annotiamo:

```text
serving interface:
certified assets:
semantic model/version:
refresh/freshness:
access policy:
downstream consumers:
fallback if serving fails:
owner:
```

### Confine editoriale

Ricordiamo:

- Ch11: **che cosa significa la metrica e come viene costruita**;
- Ch12: **dove quella definizione viene servita e come si collega ai consumer**;
- Ch18: **come l'organizzazione governa ownership, adozione e lifecycle su scala**.

> **Un semantic layer è utile architetturalmente quando riduce la dipendenza dei consumer dai dettagli fisici senza nascondere provenienza, stato di qualità e ownership della definizione.**
