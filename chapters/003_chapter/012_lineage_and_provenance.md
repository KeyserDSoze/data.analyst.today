## 3.11 Lineage e provenance: da dove arriva davvero questo numero?

Un dato senza storia è difficile da fidare.

Per lineage intendiamo il percorso che il dato compie attraverso sistemi, trasformazioni e modelli.

Per provenance intendiamo l'origine del dato e il contesto in cui è stato generato.

Nel lavoro reale, sapere da dove arriva una metrica può essere importante quanto conoscere la formula con cui viene calcolata.

### Caso studio simulato — Due dashboard, due margini diversi

**Orion Foods** utilizza due dashboard per monitorare il margine lordo.

La dashboard commerciale mostra un margine del 34,8%.

La dashboard finance mostra il 31,6%.

Entrambe sembrano corrette.

Il problema non è una formula sbagliata.

Il problema è il lineage.

La dashboard commerciale legge una tabella del data warehouse aggiornata ogni notte e utilizza il costo standard del prodotto.

La dashboard finance legge un dataset mensile riconciliato con il sistema ERP e utilizza il costo effettivo, includendo rettifiche di trasporto e variazioni di acquisto.

Le due metriche hanno lo stesso nome: `gross_margin_pct`.

Ma non rappresentano la stessa cosa.

Il conflitto non può essere risolto guardando solo il grafico.

Bisogna ricostruire il percorso:

```text
ERP vendite ─┐
             ├─> ETL ─> fact_sales ─> modello BI commerciale
Catalogo costi ┘

ERP finance ─> chiusura mensile ─> rettifiche ─> dataset finance
```

A quel punto il team decide di mantenere entrambe le misure, ma con nomi e utilizzi diversi:

- `gross_margin_standard_pct`
- `gross_margin_actual_pct`

### Domande di lineage

Quando una metrica è importante, dovremmo poter rispondere a domande come:

- Qual è il sistema sorgente?
- Chi produce il dato originale?
- Con quale frequenza viene aggiornato?
- Quali trasformazioni subisce?
- Quali join vengono applicate?
- Esistono filtri impliciti?
- Il dato viene corretto retroattivamente?
- Quale versione della logica stiamo usando?
- Chi è il data owner?

### Perché è fondamentale nell'era dell'AI

Quando un assistente AI interroga un semantic model o un data warehouse, può generare una risposta tecnicamente corretta sul dataset sbagliato.

Se esistono cinque campi chiamati `revenue`, il problema principale non è scrivere SQL.

È capire quale rappresenta il concetto richiesto.

L'AI accelera l'interrogazione.

Il lineage riduce l'ambiguità.

### Documentare senza burocrazia inutile

Non serve trasformare ogni analisi in un progetto di governance enorme.

Per le metriche critiche può bastare una scheda minimale:

```text
Metrica: net_revenue
Owner: Finance
Sorgente: ERP / invoices
Aggiornamento: giornaliero, ore 05:00 CET
Grain: una riga per invoice line
Esclusioni: fatture annullate
Resi: sottratti alla data di emissione della nota di credito
Valuta: EUR dopo conversione al cambio contabile giornaliero
```

Questa piccola documentazione può evitare settimane di discussione.