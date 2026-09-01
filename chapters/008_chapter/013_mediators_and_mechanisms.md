## 8.12 Mediatori e meccanismi: capire come funziona senza cambiare domanda per errore

Dopo aver stimato un effetto totale, il business spesso chiede:

> **“Perché funziona?”**

È una domanda diversa.

Un **mediatore** è una variabile sul percorso causale tra trattamento e outcome.

```text
Trattamento -> Mediatore -> Outcome
```

Esempio:

```text
onboarding guidato -> time-to-value più breve -> retention più alta
```

### Caso simulato/composito — Onboarding SaaS

Un esperimento mostra:

| Metrica | Standard | Guidato |
|---|---:|---:|
| Activation D7 | 44% | 63% |
| Retention D90 | 71% | 79% |

L'effetto totale sulla retention è `+8 pp`.

Il team vuole sapere se il beneficio passa attraverso activation più rapida.

La tentazione è aggiungere `activation_D7` come controllo in una regressione sulla retention.

Ma activation è **post-trattamento**.

Controllarla non “rende più precisa” la stima dell'effetto totale. Cambia il problema che stiamo tentando di stimare.

### Effetto totale, diretto e indiretto

In modo intuitivo:

- **effetto totale:** tutto ciò che cambia nell'outcome per effetto del trattamento;
- **effetto indiretto:** parte che opera attraverso il mediatore considerato;
- **effetto diretto:** parte che non passa attraverso quel mediatore, secondo la definizione scelta.

Queste quantità sembrano una semplice scomposizione.

In realtà richiedono assunzioni causali aggiuntive.

### Il mediatore non è randomizzato solo perché il trattamento lo era

Anche se l'onboarding è stato randomizzato, `activation_D7` non lo è.

Utenti che si attivano presto possono differire per:

- motivazione;
- competenza tecnica;
- urgenza;
- qualità dei dati importati;
- supporto interno.

Queste caratteristiche possono influenzare anche retention.

Quindi una relazione `activation -> retention` all'interno dell'esperimento non diventa automaticamente una prova del meccanismo.

### Post-treatment confounding

Il trattamento può generare variabili che influenzano sia mediatore sia outcome.

Per esempio:

```text
onboarding -> supporto ricevuto -> activation
                         \-----> retention
```

Studiare mediazione ignorando questo percorso può produrre interpretazioni fragili.

La domanda “quanto passa da M?” è spesso più difficile della domanda “T funziona?”

### Un meccanismo è utile se cambia la decisione

Supponiamo di avere evidenza credibile che il nuovo onboarding migliori retention.

Possibili meccanismi:

- time-to-value più breve;
- importazione dati più completa;
- relazione personale con Customer Success;
- maggiore numero di collaboratori invitati;
- riduzione degli errori iniziali.

Se il beneficio deriva soprattutto dal TTV, potremmo investire in automazione e template.

Se deriva dalla relazione umana, una soluzione completamente self-service potrebbe distruggere il valore.

Capire il meccanismo può quindi cambiare **come scalare** l'intervento.

### Mechanism evidence ladder

È utile distinguere livelli di evidenza.

**Livello 1 — Pattern coerente**

> Il trattamento modifica il mediatore e il mediatore è associato all'outcome.

Interessante, non sufficiente per una mediazione causale.

**Livello 2 — Timing e DAG coerenti**

> Il mediatore segue il trattamento, precede l'outcome e il causal model è plausibile.

Più forte, ma restano confondenti del mediatore.

**Livello 3 — Design specifico sul meccanismo**

> Variazioni sperimentali o quasi-sperimentali permettono di isolare parti del percorso.

Molto più informativo.

### Caso simulato/composito — Coupon e checkout

Un coupon aumenta conversione dal 3,8% al 4,7%.

Il team osserva anche minore abbandono checkout.

Non basta concludere:

> “Il coupon funziona perché riduce checkout abandonment.”

Potrebbero coesistere:

- maggiore intenzione d'acquisto;
- cambi di mix prodotto;
- aumento urgenza;
- riduzione della sensibilità al prezzo;
- modifica del basket.

Per attribuire una quota dell'effetto al checkout serve una domanda di mediazione esplicita.

### Mechanism card

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
