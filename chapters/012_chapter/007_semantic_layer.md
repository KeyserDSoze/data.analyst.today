## 12.6 Semantic layer come serving boundary: pubblicare significato, non solo tabelle

Nel Capitolo 11 abbiamo definito che cosa significano metriche, dimensioni e relazioni. Qui la domanda è architetturale:

> **Dove viene pubblicata quella semantica affinché dashboard, notebook, applicazioni e agenti non debbano ricostruirla separatamente?**

Il semantic layer è uno dei possibili **serving boundary** tra modelli analitici e consumer. Una struttura concettuale può essere:

```text
curated tables
      ↓
analytical models
      ↓
semantic layer
      ↓
BI / notebooks / natural-language analytics / applications
```

Il valore non sta nel nascondere le tabelle, ma nel ridurre l'accoppiamento dei consumer ai dettagli fisici: join, nomi tecnici, colonne, storage e business logic ripetuta. Un'interfaccia semantica può esporre metriche, dimensioni, relazioni, gerarchie, calendario e nomi business attraverso un contratto più stabile.

### Caso simulato/composito — SkyShop e tre conversion rate

SkyShop usa tre metriche legittime:

```text
session_to_order_conversion
user_to_purchase_conversion
checkout_to_paid_conversion
```

Il problema non è sceglierne una come “conversione universale”. È evitare che tre dashboard mostrino tutte `conversion_rate` facendo credere che il concetto sia unico.

Il Capitolo 11 risolve la definizione. Il Capitolo 12 deve assicurarsi che quelle definizioni vengano **servite da un punto riconoscibile e governabile**, così i consumer non reinventano la semantica ogni volta.

Databricks documenta le metric views proprio come oggetti semantici che centralizzano misure e dimensioni riusabili per consumer differenti.

Fonte: https://docs.databricks.com/aws/en/uc-semantics/metric-views

### Centralizzare non corregge gli errori

Se `net_revenue` è costruita su refund mancanti, pubblicarla in un semantic layer non la rende corretta. Anzi, un errore centralizzato può propagarsi più rapidamente. Per questo il serving boundary deve dipendere da modelli testati, lineage, owner, versioning e stato di qualità.

Il vantaggio emerge soprattutto durante un cambiamento. Con la logica duplicata in 27 dashboard dobbiamo trovare e modificare ogni copia. Con un serving boundary condiviso possiamo almeno sapere quale definizione cambia, quali consumer dipendono da essa e quale versione stanno usando.

Questo diventa ancora più importante con l'AI. Un agente può tradurre linguaggio naturale in query, ma deve poter distinguere `raw amount`, `recognized revenue` e `net sales`. Un semantic layer riduce l'ambiguità esponendo definizioni certificate e relazioni valide, senza trasformare “certificato” in “infallibile”.

Nel nodo `SERVE` della Data Flow Architecture Map annotiamo:

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

> **Un semantic layer è utile architetturalmente quando riduce la dipendenza dei consumer dai dettagli fisici mantenendo visibili provenienza, stato di qualità e ownership della definizione.**
