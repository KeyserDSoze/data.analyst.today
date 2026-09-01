## 8.14 Prediction vs causal targeting: chi è a rischio non è necessariamente chi possiamo aiutare

Il Capitolo 6 ha già separato tre domande:

1. chi probabilmente farà churn?
2. perché il churn è più frequente in certi gruppi?
3. quale intervento modifica realmente il churn?

Qui aggiungiamo il passaggio causale che serve alla decisione di targeting.

### Risk score e treatment effect hanno target diversi

Un modello predittivo stima qualcosa come:

`P(churn | informazioni disponibili)`

Una policy causale vuole invece conoscere qualcosa come:

`P(churn | intervento) - P(churn | nessun intervento)`

Il primo ordina il **rischio**.

Il secondo ordina la **sensibilità all'intervento**.

Sono quantità diverse.

### Caso simulato/composito — Tre segmenti

| Segmento | Churn senza azione | Churn con chiamata | Effetto causale stimato |
|---|---:|---:|---:|
| A | 55% | 52% | -3 pp |
| B | 30% | 18% | -12 pp |
| C | 12% | 9% | -3 pp |

Un modello di rischio mette A al primo posto.

Se la decisione è **chi chiamare**, B può creare molto più valore incrementale.

Il cliente più facile da prevedere può essere il più difficile da salvare.

### Caso simulato/composito — Il modello con AUC alta

Un SaaS costruisce un churn model con AUC 0,89.

Tra le feature più importanti:

- login recenti;
- ticket;
- riduzione feature usage;
- failed payment;
- utenti attivi.

Il Customer Success contatta gli account con rischio più alto. Dopo due mesi i contattati churnano molto più degli altri.

Non possiamo concludere che la chiamata sia inefficace: il trattamento è stato assegnato **in base al risk score**.

Il confronto trattati/non trattati incorpora quindi il processo di targeting.

Per valutare l'effetto della chiamata serve un design causale compatibile con quella policy.

### Feature predittiva ≠ leva

Una feature può essere fortemente predittiva ma impossibile o insensata da modificare:

- tenure;
- country;
- industry;
- storico acquisti;
- dimensione aziendale.

Altre variabili possono essere meno predittive ma più vicine a una leva:

- tempo di risposta;
- errore onboarding;
- frizione al pagamento;
- disponibilità di una integrazione;
- time-to-value.

Anche una variabile modificabile, però, non diventa automaticamente una leva causale. Deve ancora essere identificato l'effetto dell'intervento che la modifica.

### Uplift e causal ML

Uplift modeling e metodi per heterogeneous treatment effects cercano di stimare **dove l'effetto di una specifica azione cambia**.

Sono utili quando abbiamo un design che consente identificazione causale credibile, spesso dati sperimentali o quasi-sperimentali ben costruiti.

Non riparano automaticamente:

- confounding non osservato;
- treatment leakage;
- overlap scarso;
- interference;
- cambi di policy.

Il Capitolo 10 approfondirà predictive modeling. Qui ci interessa una sola regola:

> **non usare una probabilità di evento come se fosse una probabilità di successo dell'intervento.**

### Targeting economico

Anche treatment effect e uplift non sono ancora la decisione completa.

Per prioritizzare potremmo voler combinare:

```text
effetto incrementale
× valore economico dell'outcome evitato
- costo del trattamento
- costo/opportunity cost della capacità
```

Un intervento con effetto causale alto può non valere il costo. Un effetto più piccolo su account ad alto valore può essere prioritario.

Questo ponte verso decision economics sarà sviluppato nel Capitolo 15.

### Policy targeting card

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
