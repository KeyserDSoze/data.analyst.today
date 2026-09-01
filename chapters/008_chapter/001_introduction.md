# Capitolo 8 — Causalità, confondenti e ragionamento controfattuale

> **Una differenza osservata è un fatto sui dati. Un effetto causale è una conclusione su ciò che sarebbe cambiato sotto un'alternativa credibile.**

Nei capitoli precedenti abbiamo imparato a descrivere pattern, quantificare incertezza, seguire clienti nel lifecycle e modellare il tempo.

Ora la domanda cambia.

Non chiediamo più soltanto:

> “Che cosa è successo?”

oppure:

> “Che cosa probabilmente succederà?”

Chiediamo:

> **“Che cosa cambierebbe se intervenissimo?”**

Aumentare il budget advertising aumenterebbe davvero le vendite incrementali? Un onboarding guidato ridurrebbe il churn? Uno sconto genererebbe ordini aggiuntivi oppure verrebbe usato soprattutto da clienti che avrebbero comprato comunque? Una chiamata del Customer Success salva clienti oppure viene semplicemente assegnata a quelli già più a rischio?

Queste sono domande causali.

## 8.0 Dal pattern alla causal claim

Consideriamo tre frasi.

1. **Associazione:** i clienti che usano la nuova feature hanno retention più alta.
2. **Effetto causale:** rendere disponibile la feature aumenta la retention.
3. **Effetto decisionale:** rendere disponibile la feature a questo segmento aumenterebbe la retention a 90 giorni di circa 3 punti percentuali rispetto all'esperienza attuale.

La distanza tra la prima e la terza frase non viene colmata da una regressione più sofisticata.

Richiede un **disegno di identificazione**.

La World Bank descrive il controfattuale come il nucleo dell'impact evaluation: tutti i principali metodi — randomizzazione, instrumental variables, regression discontinuity, Difference-in-Differences e matching — cercano, con assunzioni diverse, di costruire un gruppo di confronto capace di rappresentare ciò che sarebbe accaduto senza il programma.[^worldbank-impact]

### Prima del metodo: definire l'estimand

Una domanda causale deve specificare almeno:

- **unità:** cliente, account, negozio, ordine, territorio;
- **trattamento/esposizione:** che cosa cambia concretamente;
- **alternativa:** rispetto a quale condizione confrontiamo il trattamento;
- **outcome:** quale risultato misuriamo;
- **orizzonte:** entro quale finestra;
- **popolazione:** per chi vogliamo l'effetto;
- **estimand:** quale effetto medio vogliamo stimare.

Per esempio:

> “Qual è l'effetto medio di una sessione tecnica aggiuntiva, rispetto al processo standard, sul rinnovo a 90 giorni degli account SMB che non hanno completato l'integrazione ERP entro il giorno 30?”

È molto più preciso di:

> “Il training funziona?”

Quella precisione evita di cambiare domanda a metà analisi.

### Identificazione e stima sono due lavori diversi

È utile distinguere:

**Identificazione**

> Perché il confronto che stiamo usando può rappresentare il controfattuale?

**Stima**

> Dato quel confronto, quale effetto numerico otteniamo e con quale incertezza?

Possiamo avere una stima matematicamente impeccabile di un confronto causalmente sbagliato.

È uno degli errori più pericolosi nell'analytics.

### Caso simulato/composito — Il programma VIP

Una piattaforma e-commerce presenta:

| Gruppo | Spesa media annua | Ordini medi | Retention 12 mesi |
|---|---:|---:|---:|
| VIP | 1.420 € | 9,8 | 88% |
| Non VIP | 510 € | 3,4 | 61% |

Il CEO conclude:

> “Il VIP aumenta enormemente la fedeltà. Estendiamolo.”

Ma l'accesso al programma è riservato a clienti che hanno già superato 800 € di spesa nell'anno precedente.

I gruppi sono stati costruiti usando una caratteristica legata proprio alla fedeltà e al valore che vogliamo spiegare.

Il 27 punti percentuali di differenza nella retention è reale come **differenza osservata**.

Non è automaticamente l'effetto causale del programma.

La domanda corretta è:

> “Quale retention avrebbero avuto clienti eleggibili e comparabili se non avessero ricevuto il programma VIP?”

Quel risultato non osservato è il controfattuale.

### Un caso reale documentato — Perché i natural experiment hanno cambiato l'empirical work

Nel 2021 il Premio Sveriges Riksbank per le scienze economiche ha riconosciuto David Card per contributi empirici all'economia del lavoro e Joshua Angrist e Guido Imbens per contributi metodologici all'analisi delle relazioni causali. Il comitato sottolinea il ruolo dei **natural experiments** nel permettere conclusioni su causa ed effetto quando una randomizzazione deliberata non è disponibile.[^nobel-2021]

Il punto per un Data Analyst non è imitare un paper accademico.

È capire la logica:

> **la forza della conclusione dipende da come si è generato il confronto, non dal prestigio del modello usato dopo.**

## Le quattro domande che guideranno il capitolo

Per ogni causal claim chiederemo:

1. **Che effetto stiamo cercando?** — estimand.
2. **Perché alcune unità ricevono il trattamento e altre no?** — assignment mechanism.
3. **Perché il gruppo di confronto rappresenta un controfattuale credibile?** — identification strategy e assunzioni.
4. **Quale frase siamo autorizzati a pronunciare dopo i diagnostics?** — claim consentito.

## Il Causal Identification Brief

Il deliverable finale del capitolo sarà un **Causal Identification Brief**.

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

Questo schema impedisce una scorciatoia molto comune:

**dati osservazionali → modello → coefficiente → verbo “causare”**.

Il percorso corretto è:

**domanda → estimand → processo di assegnazione → controfattuale → assunzioni → design → diagnostics → stima → claim**.

> **La causalità non è una proprietà del coefficiente. È una proprietà dell'argomento che collega il confronto al controfattuale.**

[^worldbank-impact]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
[^nobel-2021]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
