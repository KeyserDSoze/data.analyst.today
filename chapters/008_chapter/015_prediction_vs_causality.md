## 8.14 Prevedere il churn non significa sapere come ridurlo

Una delle confusioni più frequenti nell'analytics moderno nasce dall'equivalenza implicita tra previsione e causalità.

Un modello può prevedere molto bene chi farà churn e dirci molto poco su quale intervento possa evitarlo.

### Caso realistico: il modello con AUC 0,89

Una società SaaS costruisce un modello di churn con AUC 0,89.

Le feature più importanti sono:

- numero di login negli ultimi 30 giorni;
- ticket aperti;
- calo nell'utilizzo delle feature core;
- pagamento fallito;
- numero di utenti attivi;
- contatti con il supporto.

Il team Customer Success decide di chiamare i clienti con rischio più alto.

Dopo due mesi nota che i clienti chiamati hanno un churn del 31%, contro il 7% degli altri.

Qualcuno conclude che le chiamate non funzionano.

Ma il confronto è privo di senso: i clienti chiamati erano scelti proprio perché ad altissimo rischio.

### Predictive target e causal target sono diversi

Il modello predittivo risponde a:

> **chi è più probabile che faccia churn?**

La domanda causale è:

> **per quali clienti una specifica azione ridurrà il churn rispetto a ciò che sarebbe successo senza l'azione?**

Sono problemi diversi.

Un cliente con rischio altissimo potrebbe essere ormai irrecuperabile.

Un cliente con rischio medio potrebbe invece rispondere molto bene a una chiamata.

Se spendiamo tutte le risorse sui clienti con rischio più alto, potremmo ottenere un ROI inferiore rispetto a un targeting basato sull'**incremental effect** dell'intervento.

### Risk score vs uplift

Immaginiamo 10.000 clienti:

| Segmento | Churn previsto senza azione | Churn con chiamata | Riduzione causale stimata |
|---|---:|---:|---:|
| A | 55% | 52% | 3 pp |
| B | 30% | 18% | 12 pp |
| C | 12% | 9% | 3 pp |

Un modello di rischio puro metterebbe A in cima alla lista.

Un modello di uplift o una stima dell'effetto eterogeneo suggerirebbe invece che B è il segmento con maggiore valore dell'intervento.

### Feature predittive che non sono leve

Molte feature fortemente predittive non sono modificabili:

- anzianità del cliente;
- settore;
- paese;
- storico di acquisto;
- dimensione aziendale.

Possono aiutare a prevedere, ma non indicano necessariamente cosa fare.

Al contrario, variabili meno predittive possono rappresentare leve operative importanti:

- tempo di risposta del supporto;
- numero di errori nell'onboarding;
- frizione al pagamento;
- tempo al primo valore.

### Causal ML

Metodi di causal machine learning e uplift modeling cercano di stimare l'eterogeneità dell'effetto del trattamento.

Ma anche qui vale la stessa regola: servono dati e disegni che consentano identificazione causale credibile.

Un algoritmo sofisticato non ripara automaticamente un trattamento assegnato in modo fortemente selettivo.

### Caso operativo: retention budget

Una subscription company dispone di 25.000 euro al mese per campagne di retention.

Approccio 1: contatta i 2.000 clienti con rischio di churn più alto.

Approccio 2: usa evidenza sperimentale per identificare i clienti su cui il voucher da 15 euro produce maggiore riduzione incrementale del churn.

Dopo tre mesi:

- targeting per rischio: 240 churn evitati stimati;
- targeting per uplift: 410 churn evitati stimati;
- stesso budget.

Il punto non è che l'uplift sia sempre migliore. Il punto è che **ottimizzare la probabilità dell'evento e ottimizzare l'effetto di un intervento sono obiettivi differenti**.

### Regola pratica

> **Prediction dice dove probabilmente accadrà qualcosa. Causal inference prova a dire cosa cambierà se interveniamo.**
