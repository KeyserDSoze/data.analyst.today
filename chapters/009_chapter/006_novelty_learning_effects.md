## 9.5 Durata, novelty e learning: abbastanza utenti non significa abbastanza comportamento

Un test può raggiungere la numerosità pianificata molto prima di aver osservato il fenomeno che deve informare la decisione. Nei prodotti ad alto traffico è normale arrivare al sample requirement in poche ore; questo non rende mature metriche che richiedono giorni, returning exposure o cicli settimanali.

Il sample size risponde soprattutto a **quanta informazione** raccogliamo. La durata risponde anche a **quale fase del comportamento** abbiamo osservato.

### Caso simulato/composito — La homepage che vince perché è nuova

Una media company testa una homepage più dinamica:

| Exposure age | Delta pagine/sessione B vs A |
|---|---:|
| giorni 1–3 | +6,7% |
| giorni 4–7 | +2,2% |
| giorni 8–14 | +0,4% |

Leggendo soltanto il calendario del test diremmo che “l'effetto decade”. Ma un utente arrivato al giorno 12 può essere alla prima exposure, mentre un returning user può avere già visto B dieci volte. Per capire se stiamo osservando novelty o adattamento dobbiamo distinguere **experiment age** da **exposure age**.

Una novità può generare temporaneamente curiosità, esplorazione o attenzione. Un nuovo flusso complesso può invece partire peggio e migliorare con l'apprendimento. In un software B2B, per esempio, una nuova interfaccia di reporting può mostrare nella prima settimana task completion -5,8%, tempo task +13% ed errori +19%, per poi arrivare alla quarta settimana a task completion +4,1%, tempo task -11% ed errori -7%.

Il test breve e quello lungo non stanno necessariamente contraddicendosi: possono misurare due fasi diverse della stessa transizione. La decisione deve stabilire se interessa l'effetto immediato del rollout, lo steady state o entrambi.

### Duration floor: il tempo minimo nasce dal processo

Supponiamo che QuickPay raggiunga il sample size in 36 ore. Possiamo comunque definire:

```text
sample requirement: raggiunto
minimum calendar duration: 14 giorni
reason: due cicli weekday/weekend + returning exposure
```

Non perché “ogni A/B test deve durare due settimane”, ma perché quel prodotto ha un mix weekday/weekend, utenti che tornano e outcome che devono maturare. In altri sistemi il floor può dipendere da payday, rinnovi, frequenza di acquisto, business cycle o learning atteso.

La data di fine enrollment e quella di fine observation possono inoltre essere differenti. Per QuickPay un ordine nasce a `t0`, una cancellazione può arrivare entro 24 ore, un chargeback molto più tardi e un reso dopo giorni o settimane. Se la primary o un guardrail richiedono una finestra di maturazione, l'ultimo cohort di utenti deve completarla prima del final read.

### Il calendario limita anche la generalizzazione

La randomizzazione protegge A e B da molti shock contemporanei comuni, perché entrambi attraversano la stessa settimana. Ma un test interamente eseguito durante Black Friday può stimare bene l'effetto **in quel contesto** e generalizzare male a un mese normale.

Per questo duration e calendar coverage devono chiedere se il traffico osservato rappresenta il regime a cui vogliamo applicare la policy. Separare first exposure, repeated exposure, nuovi e returning users può aiutare a distinguere valore strutturale, surprise e migration cost, purché queste slice vengano trattate come diagnostics o segmenti pre-specificati e non come una ricerca post-hoc di vittorie.

### Duration card

```text
Sample size requirement:
Expected time to reach it:
Minimum calendar duration:
Cycles that must be covered:
Outcome maturation lag:
Expected novelty:
Expected learning:
Exposure-age diagnostics:
New vs returning user plan:
Exceptional calendar events:
Analysis date after maturity:
```

> **Un test è completo quando ha raccolto abbastanza unità e abbastanza storia comportamentale per la decisione che deve supportare. Le due condizioni non coincidono necessariamente.**
