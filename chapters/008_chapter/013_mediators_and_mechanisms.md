## 8.12 Mediatori e meccanismi: capire come funziona senza cambiare domanda per errore

Dopo aver identificato un effetto, il business chiede spesso: **“Perché funziona?”**. È una domanda legittima, ma non è la stessa domanda che ha prodotto l'effetto totale.

Un **mediatore** si trova sul percorso causale tra trattamento e outcome:

```text
Trattamento -> Mediatore -> Outcome
```

Per esempio:

```text
onboarding guidato -> time-to-value più breve -> retention più alta
```

Se vogliamo sapere l'effetto totale dell'onboarding, controllare automaticamente per il time-to-value può rimuovere proprio una parte dell'effetto che vogliamo misurare. Se vogliamo invece capire quanto dell'effetto passi da quel meccanismo, abbiamo cambiato estimand e introdotto assunzioni ulteriori.

### Caso simulato/composito — Onboarding SaaS

Un esperimento mostra:

| Metrica | Standard | Guidato |
|---|---:|---:|
| Activation D7 | 44% | 63% |
| Retention D90 | 71% | 79% |

L'effetto totale osservato sulla retention è **+8 pp**. Il team nota che l'activation D7 cresce molto e propone di “controllarla” in una regressione. Ma `activation_D7` è post-treatment: non rende la stima totale più pulita, cambia la domanda.

La distinzione intuitiva è tra **effetto totale**, che include tutti i percorsi attraverso cui il trattamento modifica l'outcome, **effetto indiretto**, che passa attraverso un mediatore definito, ed **effetto diretto**, che non passa attraverso quel mediatore secondo la definizione scelta. Questa scomposizione non è una contabilità automatica: richiede un causal model più ricco.

Il punto cruciale è che il mediatore non diventa randomizzato solo perché il trattamento lo era. Gli utenti che si attivano presto possono differire per motivazione, competenza tecnica, urgenza, qualità dei dati importati o supporto interno. Queste caratteristiche possono influenzare anche la retention. La relazione `activation -> retention` dentro un esperimento randomizzato sul training non è, da sola, un esperimento randomizzato sull'activation.

Il trattamento può inoltre generare altre variabili post-treatment che influenzano sia mediatore sia outcome:

```text
onboarding -> supporto ricevuto -> activation
                         \-----> retention
```

Questo **post-treatment confounding** rende spesso la domanda “come funziona?” più difficile della domanda “funziona?”.

### Perché il meccanismo conta per la decisione

Capire il percorso può cambiare il modo in cui un intervento viene scalato. Se il beneficio dell'onboarding guidato dipende soprattutto da un time-to-value più breve, il team può investire in template, automazione e riduzione delle frizioni. Se dipende dalla relazione umana creata con Customer Success, trasformare tutto in self-service potrebbe eliminare proprio la componente di valore.

Per non sovrainterpretare, conviene trattare l'evidenza sul meccanismo come una scala. Un pattern in cui il trattamento modifica `M` e `M` è associato a `Y` è una prima pista. Timing coerente e DAG plausibile rafforzano l'argomento. Una variazione sperimentale o quasi-sperimentale che isola il percorso fornisce evidenza molto più forte.

Consideriamo un coupon che aumenta la conversione dal **3,8% al 4,7%** e coincide con minore checkout abandonment. Non basta concludere che “il coupon funziona perché riduce l'abbandono”: potrebbero cambiare intenzione d'acquisto, mix prodotto, urgenza, sensibilità al prezzo e composizione del basket. Per attribuire una quota dell'effetto al checkout serve una domanda di mediazione esplicita.

La **Mechanism card** resta intenzionalmente strutturata:

```text
Effetto totale già identificato?
Mediatore candidato:
Timing T -> M -> Y:
Perché M è plausibilmente sul percorso?
Quali cause pre-treatment influenzano M e Y?
Quali variabili post-treatment possono confondere M -> Y?
Quale effetto vogliamo: totale, diretto, indiretto?
Quale decisione cambia conoscendo il meccanismo?
Quanto è forte la causal claim consentita?
```

> **Non controllare automaticamente ciò che succede dopo il trattamento. Una variabile post-treatment può essere proprio il meccanismo che stai cercando di capire.**

Anche quando l'effetto totale è credibile, resta un'altra domanda: **è lo stesso per tutti?**
