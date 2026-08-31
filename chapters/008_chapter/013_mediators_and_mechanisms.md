## 8.12 Mediatori e meccanismi: non basta sapere se funziona, vogliamo capire come

Una volta stimato un effetto causale, spesso il business pone una seconda domanda:

> **perché funziona?**

Questa domanda introduce il concetto di **mediatore**.

Un mediatore è una variabile che si trova sul percorso causale tra trattamento e outcome.

Esempio:

**nuovo onboarding → activation più rapida → maggiore retention**

Qui `activation_speed` potrebbe essere un mediatore.

### Caso realistico: onboarding SaaS

Una società SaaS testa un onboarding guidato con checklist, template e chiamata iniziale.

Risultati a 90 giorni:

| Metrica | Controllo | Nuovo onboarding |
|---|---:|---:|
| activation entro 7 giorni | 44% | 63% |
| retention a 90 giorni | 71% | 79% |

L'intervento sembra migliorare la retention di 8 punti percentuali.

Ma il team prodotto vuole capire se il beneficio deriva davvero dall'activation più rapida.

La tentazione è inserire `activation_within_7_days` come variabile di controllo in una regressione del churn.

Questo può però essere concettualmente sbagliato: l'activation è successiva al trattamento ed è probabilmente parte del meccanismo causale.

Controllarla significa bloccare una porzione dell'effetto che stiamo cercando di spiegare.

### Effetto totale, diretto e indiretto

In modo intuitivo possiamo distinguere:

- **effetto totale**: quanto cambia l'outcome grazie al trattamento;
- **effetto diretto**: parte dell'effetto che non passa attraverso il mediatore considerato;
- **effetto indiretto**: parte che passa attraverso il mediatore.

Questa scomposizione richiede assunzioni causali più forti rispetto alla semplice stima dell'effetto totale.

### Perché è utile al business

Capire il meccanismo cambia la decisione.

Se il nuovo onboarding funziona soprattutto perché riduce il time-to-value, l'azienda può investire direttamente in:

- importazione dati automatica;
- template preconfigurati;
- integrazioni più rapide;
- assistenza nei primi sette giorni.

Se invece l'effetto deriva soprattutto dalla relazione personale con il Customer Success, la soluzione operativa è diversa.

### Caso marketing: sconto e conversione

Un e-commerce testa un coupon del 10%.

La conversione cresce dal 3,8% al 4,7%.

Il team vuole sapere se l'effetto passa da:

1. percezione di convenienza;
2. aumento dell'urgenza;
3. modifica del mix prodotti;
4. riduzione dell'abbandono al checkout.

Queste variabili non sono semplicemente "controlli". Possono essere componenti del percorso causale.

### Attenzione al post-treatment bias

Una regola molto importante:

> **Non controllare automaticamente variabili misurate dopo il trattamento.**

Possono essere mediatori, conseguenze del trattamento o collider creati dal trattamento stesso.

### Il DAG aiuta

Un DAG semplice può rappresentare:

```text
Onboarding -> Activation -> Retention
     \---------------------> Retention
```

Questo schema obbliga a chiedere quale effetto vogliamo stimare.

Se vogliamo l'effetto totale dell'onboarding, controllare per activation può essere controproducente.

Se vogliamo studiare il meccanismo, dobbiamo formulare una domanda di mediazione esplicita.

### Regola pratica

> **Prima di aggiungere una variabile al modello chiedi se è una causa preesistente, una conseguenza del trattamento o una parte del meccanismo che vuoi capire.**
