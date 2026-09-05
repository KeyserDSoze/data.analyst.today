## 8.14 Prediction vs causal targeting: chi è a rischio non è necessariamente chi possiamo aiutare

Il lifecycle analysis ha già separato tre domande: chi probabilmente farà churn, quali condizioni sono associate al churn e quale intervento modifica davvero il churn. La causal inference aggiunge una conseguenza operativa: **il cliente con il rischio più alto non è necessariamente quello su cui la nostra azione produce l'effetto maggiore**.

Un modello predittivo stima qualcosa come:

`P(churn | informazioni disponibili)`

Una policy causale vuole invece conoscere un contrasto del tipo:

`P(churn | intervento) - P(churn | nessun intervento)`

Il primo ordina il **rischio**. Il secondo ordina la **sensibilità a una specifica azione**.

### Caso simulato/composito — Tre segmenti

| Segmento | Churn senza azione | Churn con chiamata | Effetto causale stimato |
|---|---:|---:|---:|
| A | 55% | 52% | -3 pp |
| B | 30% | 18% | -12 pp |
| C | 12% | 9% | -3 pp |

Un risk model mette A al primo posto perché ha il churn naturale più alto. Se la decisione è **chi chiamare**, B produce però un effetto incrementale molto più grande. Il cliente più facile da prevedere può essere il più difficile da salvare.

Questo spiega anche un apparente paradosso frequente. Un SaaS costruisce un churn model con **AUC 0,89** usando login recenti, ticket, riduzione feature usage, failed payment e utenti attivi. Customer Success contatta gli account con score più alto e, dopo due mesi, i contattati churnano molto più degli altri. Il dato non dimostra che la chiamata sia inefficace: il trattamento è stato assegnato **in base al rischio**. Confrontare trattati e non trattati incorpora il processo di targeting che ha creato i gruppi.

Per misurare l'effetto della chiamata serve quindi un design causale compatibile con quella policy, non un confronto successivo tra chi è stato contattato e chi no.

### Predittore, leva e trattamento sono tre cose diverse

Una feature può prevedere bene un outcome e non essere modificabile: tenure, country, industry, storico acquisti o dimensione aziendale. Altre variabili sono più vicine a una leva — tempo di risposta, frizione al pagamento, errori di onboarding, disponibilità di un'integrazione, time-to-value — ma nemmeno una variabile modificabile diventa automaticamente una causa. Dobbiamo ancora definire **quale intervento** la modifica e stimarne l'effetto.

Uplift modeling, causal forests e metodi per heterogeneous treatment effects cercano proprio di stimare dove cambia l'effetto di un'azione. Sono utili quando esiste un design che permette causal identification credibile, spesso dati sperimentali o quasi-sperimentali ben costruiti. Non riparano automaticamente confounding non osservato, treatment leakage, overlap scarso, interference o cambi di policy.

La regola da conservare è quindi:

> **Non usare una probabilità di evento come se fosse una probabilità di successo dell'intervento.**

### Dall'uplift alla policy

Anche il treatment effect non è la decisione completa. Se la capacità è limitata dobbiamo combinare effetto incrementale, valore economico dell'outcome evitato, costo dell'intervento e opportunity cost della capacità:

```text
effetto incrementale
× valore economico dell'outcome evitato
- costo del trattamento
- costo/opportunity cost della capacità
```

Un intervento con effetto causale alto può non valere il costo; un effetto più piccolo su account di grande valore può essere prioritario. Il Capitolo 15 svilupperà questa parte economica, ma già qui è importante non far coincidere “miglior modello causale” con “migliore policy”.

La **Policy targeting card** mantiene separati i pezzi:

```text
Risk model: quale evento predice?
Intervento disponibile:
Estimand causale dell'intervento:
Evidenza usata per stimarlo:
Heterogeneity affidabile?
Capacità operativa:
Costo per trattamento:
Valore outcome evitato:
Targeting basato su rischio o incremental effect?
Come misureremo la policy dopo il rollout?
```

> **Prediction localizza dove l'evento è probabile. Causal targeting localizza dove la nostra azione può cambiare il risultato.**

Ora possiamo mettere insieme tutto il capitolo in un caso realistico: più interventi, assignment mechanism diversi e livelli di causal claim che non devono essere trattati come equivalenti.
