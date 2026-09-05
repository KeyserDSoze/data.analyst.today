## 8.7 Randomizzazione e natural experiment: quando l'assegnazione rende credibile il confronto

Dopo aver ricostruito confondenti, timing e selection mechanism possiamo finalmente chiedere quale proprietà dell'assegnazione renda plausibile il controfattuale. La randomizzazione offre una risposta particolarmente forte: l'assegnazione viene generata da un meccanismo noto che, in media, non dipende dalle caratteristiche preesistenti delle unità. Non elimina ogni problema possibile, ma cambia radicalmente il motivo per cui possiamo credere al confronto.

### Caso simulato/composito — Nuovo onboarding B2B

Una piattaforma assegna casualmente nuovi account a onboarding standard o onboarding guidato:

| Gruppo | Account | Activation D14 | Retention D60 |
|---|---:|---:|---:|
| Standard | 4.812 | 42,6% | 31,8% |
| Guidato | 4.776 | 47,9% | 35,1% |

La differenza non diventa causale perché esiste una colonna `variant`. Diventa interpretabile causalmente perché **l'assegnazione è stata randomizzata prima dell'outcome** e perché l'analisi preserva quel meccanismo. Il Capitolo 9 entrerà nei failure mode operativi degli A/B test; qui il principio è che il controfattuale nasce dall'assignment, non dalla sofisticazione del modello.

Questa logica obbliga a scegliere l'unità giusta. Se una promozione viene applicata a un intero punto vendita, la randomization unit può essere il negozio, non la singola transazione. Randomizzare **40 store** non produce automaticamente centinaia di migliaia di osservazioni indipendenti solo perché esistono molte ricevute. Il livello di assignment determina l'estimand, la dipendenza tra osservazioni e i possibili spillover.

Va inoltre distinta l'**assegnazione** dall'**exposure effettiva**. Alcune unità assegnate al trattamento possono non riceverlo o non aderire. Confrontare i gruppi secondo l'assegnazione conserva il vantaggio della randomizzazione e stima spesso un effetto **intent-to-treat**. Se invece selezioniamo soltanto chi ha effettivamente aderito, compliance, motivazione o capacità possono reintrodurre selezione.

### Quando la randomizzazione non è deliberata

Molte esposizioni reali dipendono da norme, soglie amministrative, rollout geografici, vincoli di capacità, timing esterno o shock istituzionali. A volte queste strutture creano variazione utilizzabile causalmente. Ma “è successo fuori dal nostro controllo” non basta per chiamare un evento **natural experiment**: dobbiamo capire come l'evento assegna il trattamento e perché quell'assegnazione interrompe, almeno nel confronto rilevante, il normale processo di selezione.

Il Premio Sveriges Riksbank 2021 ha riconosciuto proprio il contributo di David Card, Joshua Angrist e Guido Imbens allo studio dei natural experiment e all'interpretazione degli effetti causali che essi consentono di identificare.[^nobel] Il punto metodologico è che policy o eventi reali possono generare gruppi trattati differentemente in modo abbastanza simile a un esperimento da sostenere un causal argument — ma solo dopo averne difeso il meccanismo.

Un natural experiment rimane quindi pieno di assunzioni. Una policy può coincidere con un'altra riforma, una regione può subire uno shock specifico, i soggetti possono anticipare il cambiamento, il measurement può cambiare o la popolazione può migrare tra gruppi. La scheda iniziale dovrebbe poter rispondere:

```text
Qual è la fonte di variazione?
Chi viene esposto e perché?
Chi rappresenta il confronto?
Quali altre cose cambiano nello stesso momento?
Quanto è locale l'effetto identificato?
```

La World Bank organizza i principali metodi di impact evaluation proprio attorno alle caratteristiche operative del programma e alla capacità di costruire un gruppo di confronto valido.[^worldbank-methods] Questo aiuta a leggere i design successivi con una logica comune. La **Difference-in-Differences** sfrutta una traiettoria di confronto nel tempo; la **RDD** una discontinuità nella regola di assegnazione; le **IV** una fonte esterna che modifica la probabilità di trattamento. Il **matching** segue invece una logica più debole: cerca comparabilità sulle covariate osservate quando non esiste una quasi-randomizzazione forte.

> **Il nome del metodo viene dopo. Prima dobbiamo capire quale caratteristica del processo di assegnazione rende possibile il confronto.**

[^nobel]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
[^worldbank-methods]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*, parte II: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
