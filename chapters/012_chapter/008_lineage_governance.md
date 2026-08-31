## 12.7 Lineage e governance: sapere da dove viene il numero

Quando un numero finisce in una decisione importante, dovremmo essere in grado di rispondere a una domanda semplice:

> Da dove viene?

Questa domanda apre il tema della **data lineage**.

La lineage descrive il percorso del dato attraverso il sistema:

```text
source
  ↓
ingestion
  ↓
raw table
  ↓
transformation
  ↓
curated model
  ↓
semantic metric
  ↓
dashboard / notebook / API
```

Una buona lineage permette di capire non solo il percorso, ma anche quali oggetti dipendono da quali trasformazioni.

## Caso realistico: il KPI cambiato senza saperlo

**NordRail**, azienda di trasporto, modifica la logica con cui classifica un viaggio come "cancellato".

Prima:

```text
status = CANCELLED
```

Dopo:

```text
status IN (CANCELLED, ABORTED_AFTER_DEPARTURE)
```

La modifica viene applicata in una tabella intermedia.

Due settimane dopo il tasso di cancellazione sembra peggiorare del 14%.

Il management interpreta il dato come deterioramento operativo.

Con lineage e versioning, l'analista vede immediatamente che il salto coincide con una modifica nella trasformazione. Senza lineage, il team passa tre giorni a cercare guasti operativi inesistenti.

## Governance non significa burocrazia infinita

Data governance viene spesso percepita come un insieme di approvazioni e divieti.

Una governance utile, invece, risponde a domande concrete:

- chi è owner del dato?
- chi può accedervi?
- quali campi sono sensibili?
- quali dataset sono certificati?
- quale qualità ci aspettiamo?
- quali SLA esistono?
- chi approva una modifica semantica?
- quanto a lungo conserviamo il dato?
- come tracciamo l'impatto di una modifica?

## Catalogo, glossary e certificazione

Tre oggetti concettualmente diversi aiutano molto.

### Data catalog

Aiuta a trovare asset tecnici:

- tabelle;
- viste;
- file;
- pipeline;
- dashboard;
- modelli.

### Business glossary

Definisce termini come:

- customer;
- active account;
- net revenue;
- churn;
- order;
- fiscal month.

### Certified datasets

Indicano quali asset sono raccomandati per determinati usi.

Un analyst dovrebbe poter distinguere tra:

```text
raw_orders_v2_backup
```

e
```text
gold.fact_orders_certified
```

senza dover chiedere ogni volta a tre colleghi.

## Governance e velocità

Una governance ben progettata può **aumentare** la velocità analitica.

Se un analyst sa già:

- dove trovare il dato;
- quale tabella è affidabile;
- chi è l'owner;
- cosa significa ogni campo;
- quali limiti esistono;

passa meno tempo a investigare infrastruttura e più tempo ad analizzare il problema.

## Caso realistico: il dato sensibile copiato per comodità

In una società assicurativa alcuni analyst esportano tabelle con dati personali in file locali perché l'ambiente centrale è lento e poco documentato.

La risposta superficiale sarebbe:

> vietiamo gli export.

La risposta architetturale è più completa:

- creare viste pseudonimizzate per analytics;
- applicare access control per ruolo;
- migliorare performance e discoverability;
- definire policy di retention;
- tracciare gli accessi;
- educare gli utenti sul perché delle restrizioni.

La governance efficace deve considerare il comportamento reale degli utenti. Se l'ambiente governato è inutilizzabile, le persone cercheranno scorciatoie.

### Principio operativo

Per ogni dataset critico dovremmo poter rispondere almeno a:

```text
owner?
source?
refresh?
quality checks?
sensitivity?
certified for what?
downstream dependencies?
```

Se nessuno sa rispondere, quel dataset non è davvero governato.
