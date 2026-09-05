# Capitolo 8 — Causalità, confondenti e ragionamento controfattuale

> **Una differenza osservata è un fatto sui dati. Un effetto causale è una conclusione su ciò che sarebbe cambiato sotto un'alternativa credibile.**

Nei capitoli precedenti abbiamo imparato a formulare domande, verificare i dati, descrivere pattern, quantificare l'incertezza, seguire clienti nel lifecycle e modellare il tempo. Tutto questo può dirci molto su **che cosa è successo** e, in alcuni casi, su **che cosa probabilmente succederà**. La causalità introduce una domanda più esigente: **che cosa cambierebbe se intervenissimo?**

Aumentare il budget advertising genererebbe vendite incrementali oppure comprerebbe soprattutto conversioni che sarebbero avvenute comunque? Un onboarding guidato ridurrebbe il churn oppure viene semplicemente completato più spesso dai clienti già motivati? Uno sconto salva un rinnovo oppure viene concesso proprio quando il cliente ha già deciso di andarsene? Queste domande non chiedono una correlazione più precisa. Chiedono di rappresentare un mondo che non osserviamo direttamente.

## 8.0 Dal pattern al causal claim

Consideriamo tre frasi che, in una dashboard, possono sembrare molto vicine. “I clienti che usano la nuova feature hanno retention più alta” descrive un'associazione. “Rendere disponibile la feature aumenta la retention” formula un effetto causale. “Rendere disponibile la feature a questo segmento aumenterebbe la retention a 90 giorni di circa 3 punti percentuali rispetto all'esperienza attuale” aggiunge anche popolazione, alternativa, orizzonte e dimensione dell'effetto. La distanza tra la prima e la terza frase non viene colmata da una regressione più sofisticata: richiede un **disegno di identificazione**.

La World Bank definisce il controfattuale come il nucleo dell'impact evaluation e presenta randomizzazione, instrumental variables, Regression Discontinuity, Difference-in-Differences e matching come strategie diverse per costruire un gruppo di confronto valido.[^worldbank-impact] Il metodo, quindi, viene dopo una domanda più fondamentale: **perché questo confronto dovrebbe rappresentare ciò che sarebbe successo senza l'intervento?**

Prima di scegliere il design dobbiamo sapere quale effetto vogliamo stimare. Una causal question utile specifica l'unità, il trattamento, l'alternativa, l'outcome, l'orizzonte e la popolazione. Per esempio:

> **Qual è l'effetto medio di una sessione tecnica aggiuntiva, rispetto al processo standard, sul rinnovo a 90 giorni degli account SMB che non hanno completato l'integrazione ERP entro il giorno 30?**

Questa frase è molto più vincolante di “il training funziona?”. Impedisce di cambiare trattamento, outcome o popolazione dopo aver visto il risultato e rende esplicito l'**estimand** che la decisione richiede.

Identificazione e stima sono due lavori diversi. L'identificazione chiede perché il confronto osservato possa rappresentare il controfattuale; la stima chiede quale effetto numerico emerge da quel confronto e con quale incertezza. Possiamo avere una stima matematicamente impeccabile di un confronto causalmente sbagliato. In analytics è uno degli errori più pericolosi proprio perché il numero finale può apparire estremamente professionale.

### Caso simulato/composito — Il programma VIP

Una piattaforma e-commerce osserva:

| Gruppo | Spesa media annua | Ordini medi | Retention 12 mesi |
|---|---:|---:|---:|
| VIP | 1.420 € | 9,8 | 88% |
| Non VIP | 510 € | 3,4 | 61% |

La differenza di **27 punti percentuali** nella retention è reale come differenza osservata. Ma l'accesso al programma è riservato ai clienti che hanno già superato **800 € di spesa nell'anno precedente**. I gruppi sono quindi diversi prima ancora che il programma inizi: il criterio di eleggibilità seleziona clienti già più fedeli e di maggior valore.

La domanda utile non è più “quanto sono migliori i VIP?”, ma “quale retention avrebbero avuto clienti eleggibili e comparabili se non avessero ricevuto il programma VIP?”. Quel risultato non osservato è il controfattuale. Finché non abbiamo un argomento credibile per rappresentarlo, il 27 pp non può essere chiamato effetto del programma.

Il Premio Sveriges Riksbank 2021 ha riconosciuto David Card per i contributi empirici all'economia del lavoro e Joshua Angrist e Guido Imbens per i contributi metodologici all'analisi delle relazioni causali. I materiali del Nobel sottolineano proprio il ruolo dei **natural experiments**: situazioni in cui eventi o policy generano gruppi trattati in modo differente e consentono, sotto specifiche condizioni, di formulare conclusioni su causa ed effetto senza una randomizzazione deliberata.[^nobel-2021]

La lezione per un Data Analyst è più generale del contesto accademico: **la forza della conclusione dipende da come si è generato il confronto, non dal prestigio del modello applicato dopo**.

## Il percorso del capitolo

Il capitolo seguirà un ordine intenzionale. Prima definiremo il controfattuale e distingueremo descrizione, previsione e intervento. Poi ricostruiremo il processo che genera il trattamento: confounding, interventi reattivi, selection bias, collider, mediatori e interference. Solo a quel punto entreranno i design — randomizzazione, DiD, matching, RDD e IV — letti non come un catalogo di tecniche, ma come risposte diverse a strutture diverse dell'assignment mechanism. Infine vedremo eterogeneità, causal targeting e un caso end-to-end in cui più interventi richiedono livelli di evidenza differenti.

Il deliverable sarà un **Causal Identification Brief**:

```text
DECISIONE
Quale scelta dipende dalla causal claim?

ESTIMAND
Unità, trattamento, alternativa, outcome, orizzonte, popolazione.

ASSIGNMENT MECHANISM
Perché alcuni ricevono il trattamento e altri no?

CAUSAL MODEL
Confondenti, reverse causality, selection, mediatori, interference.

COUNTERFACTUAL
Chi o che cosa rappresenta il mondo senza trattamento?

IDENTIFICATION STRATEGY
Randomizzazione, natural experiment, DiD, matching, RDD, IV o altro.

ASSUNZIONI
Quali devono essere vere perché la stima sia causale?

DIAGNOSTICS / FALSIFICATION
Che cosa possiamo controllare nei dati?

EFFECT + UNCERTAINTY
Dimensione, precisione, eterogeneità.

SCOPE
A chi e a quale contesto si applica?

CLAIM CONSENTITO
Qual è la frase più forte che l'evidenza permette?

PROSSIMO TEST
Che cosa ridurrebbe maggiormente l'incertezza residua?
```

Il brief serve a impedire una scorciatoia comune: **dati osservazionali → modello → coefficiente → verbo “causare”**. Il percorso corretto è invece **domanda → estimand → assignment mechanism → controfattuale → assunzioni → design → diagnostics → stima → claim**.

> **La causalità non è una proprietà del coefficiente. È una proprietà dell'argomento che collega il confronto al controfattuale.**

[^worldbank-impact]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
[^nobel-2021]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
