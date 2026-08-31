## 0.7 Caso end-to-end: dodici agenti, un analista, una decisione
Consideriamo una società SaaS B2B, **NovaSuite**, con circa €95 milioni di ARR.

Un lunedì mattina il CEO riceve un alert:

> “Il net revenue retention enterprise è sceso dal 112% al 104%.”

È un segnale grave.

Il responsabile analytics dispone di una squadra di agenti specializzati.

## Fase 1 — Delega

L'analista assegna compiti distinti.

### Agent 1 — Metric definition

Recupera la definizione certificata di NRR e conferma:

- popolazione: clienti enterprise attivi all'inizio del periodo;
- numerator: ARR finale della stessa base clienti;
- include expansion e contraction;
- include churn;
- esclude nuovi loghi.

### Agent 2 — Data health

Controlla freshness, completeness e schema.

Tutto sembra regolare.

### Agent 3 — Reconciliation

Confronta ARR aggregato con Finance.

Trova una differenza dello 0,4%: entro la tolleranza abituale.

### Agent 4 — Segmentation

Mostra che quasi tutto il calo è concentrato nel segmento enterprise europeo.

### Agent 5 — Product usage

Trova una riduzione dell'utilizzo di una feature premium.

### Agent 6 — Support

Trova aumento dei ticket relativi a performance.

### Agent 7 — Pricing

Nota che alcuni rinnovi europei hanno ricevuto un aumento di listino.

### Agent 8 — Release history

Trova una release backend avvenuta sei settimane prima.

### Agent 9 — Churn decomposition

Scompone il delta NRR:

- churn: -2,1 pp;
- contraction: -4,7 pp;
- expansion: -1,2 pp.

Il problema principale è quindi contraction, non churn.

### Agent 10 — Causal critic

Contesta l'ipotesi pricing:

> “Gli account con aumento prezzo coincidono in gran parte con account grandi che hanno anche maggiore esposizione alla feature premium.”

### Agent 11 — Counterfactual search

Cerca gruppi comparabili con e senza esposizione alla release.

### Agent 12 — Executive writer

Produce una prima sintesi:

> “La riduzione NRR è probabilmente causata dall'aumento di prezzo europeo. Raccomandiamo di sospendere il nuovo listino.”

## Fase 2 — Il momento in cui serve il timoniere

L'output dell'Agent 12 è elegante e plausibile.

Ma il responsabile analytics non lo inoltra.

Fa tre domande.

### Domanda 1 — Il prezzo precede davvero il contraction?

Per molti account, il contraction avviene prima del rinnovo con nuovo listino.

Quindi il pricing non può spiegare l'intero fenomeno.

### Domanda 2 — L'utilizzo della feature è una causa o un sintomo?

Il calo di usage potrebbe essere conseguenza di problemi di performance.

### Domanda 3 — Quale evento cambia prima degli altri?

La timeline mostra:

1. release backend;
2. aumento della latenza per workload pesanti;
3. calo utilizzo feature premium;
4. aumento ticket;
5. riduzione seat e moduli al rinnovo;
6. contraction ARR.

Ora emerge una catena causale più plausibile.

## Fase 3 — Verifica indipendente

L'analista non accetta ancora la spiegazione.

Chiede controlli ortogonali.

### Controllo A — Telemetria infrastrutturale

Le metriche mostrano che la latenza p95 per il workload enterprise europeo è aumentata del 38% dopo la release.

### Controllo B — Gruppo meno esposto

I clienti enterprise americani, serviti da un cluster diverso, non mostrano lo stesso aumento.

### Controllo C — Feature exposure

Gli account con uso intensivo della feature colpita hanno contraction molto più elevato.

### Controllo D — Account non rinnovati

Anche clienti che non hanno ancora ricevuto il nuovo listino mostrano calo di usage.

Questo indebolisce ulteriormente l'ipotesi pricing come driver principale.

## Fase 4 — Gli agenti non decidono il livello di certezza

A questo punto l'evidenza è forte, ma non perfetta.

L'analista formula la conclusione così:

> “La principale ipotesi supportata dai dati è che la release backend abbia degradato le performance per workload enterprise europei, riducendo l'adozione della feature premium e aumentando contraction al rinnovo. Il pricing può avere contribuito in alcuni account, ma non spiega temporalmente il fenomeno principale.”

Questa formulazione è più lunga della raccomandazione automatica.

Ed è migliore.

## Fase 5 — Decisione proporzionata

Il team non effettua immediatamente un rollback globale.

Decide di:

- mitigare la configurazione sui cluster europei;
- monitorare latenza e usage per 72 ore;
- contattare gli account più colpiti;
- sospendere temporaneamente rollout aggiuntivi;
- mantenere il pricing invariato finché l'effetto non viene isolato meglio.

La decisione è reversibile e mirata.

## Cosa ha fatto davvero l'analista?

Non ha scritto personalmente tutte le query.

Non ha costruito ogni grafico.

Non ha letto manualmente migliaia di ticket.

Non ha preparato la prima bozza del memo.

Ha fatto qualcosa di più importante:

- ha definito la domanda;
- ha assegnato ruoli;
- ha separato esplorazione e decisione;
- ha individuato conflitti;
- ha chiesto controlli indipendenti;
- ha ragionato sulla temporalità;
- ha distinto correlazione e causalità;
- ha calibrato la conclusione;
- ha scelto un'azione proporzionata all'incertezza.

Gli agenti hanno svolto gran parte dell'esecuzione.

L'analista ha governato il sistema di evidenze.

## Il contrasto

Immaginiamo due risposte al CEO.

Prima risposta:

> “L'AI dice che è il pricing.”

Seconda risposta:

> “Il pricing è emerso come prima ipotesi, ma non regge completamente alla verifica temporale. Abbiamo evidenza più forte su una degradazione backend che precede il calo di utilizzo e la contraction. Abbiamo verificato su telemetria e gruppi meno esposti. Propongo una mitigazione mirata e un monitoraggio di 72 ore prima di modificare il listino.”

Entrambe possono essere state prodotte usando la stessa tecnologia.

Solo una dimostra leadership analitica.

> **Il valore dell'analista non sta nel numero di task che esegue personalmente. Sta nella qualità del sistema di decisione che riesce a dirigere.**