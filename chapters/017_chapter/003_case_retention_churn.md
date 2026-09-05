## 17.2 NorthPeak — “Quali clienti dobbiamo salvare?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

NorthPeak, piattaforma SaaS B2B, vede il logo churn trimestrale salire dal **2,8% al 4,1%**. Il Chief Customer Officer chiede quali clienti salvare subito e la richiesta sembra indicare una soluzione ovvia: costruire un churn model e ordinare gli account per score.

Il routing corretto mostra invece che una sola frase contiene tre problemi. Dobbiamo capire **dove nasce il deterioramento**, chi ha alta probabilità di non rinnovare e, soprattutto, chi può essere persuaso da un intervento che abbia valore economico positivo. Il team può gestire soltanto **500 interventi ad alta intensità per trimestre**; sprecare quella capacità su account già persi è il failure cost dominante.

La stop rule iniziale è quindi più importante dell'algoritmo: **nessuna campagna automatica sui top-risk finché rischio e treatment opportunity non vengono separati**.

### Il problema nasce prima del renewal

L'Analytical Brief definisce l'unità come account, il churn come mancato rinnovo alla renewal date, una prediction window di 90 giorni e l'esclusione di trial, account con meno di 60 giorni di vita e contratti già in dismissione. L'outcome economico è NRR/contribution margin, non il solo logo retention.

Prima di addestrare alcun modello, le coorti cambiano il problema. Il peggioramento è concentrato nei clienti acquisiti negli ultimi dodici mesi tramite un nuovo **partner channel**; il direct-sales è quasi stabile. Il Lifecycle Diagnostic Map mostra inoltre activation entro 14 giorni **71% → 54%**, uso della feature core nel primo mese **-19%**, ticket di onboarding **+32%** e time-to-first-value **+4,6 giorni**.

Il finding più importante non è ancora “questi account hanno churn risk alto”. È che **il deterioramento comincia durante l'attivazione, molto prima del rinnovo, e ha una forte concentrazione per acquisition source**. Aspettare gli ultimi 30 giorni per intervenire diventa così una policy poco coerente con l'evidenza.

### Prediction risponde soltanto a una parte della domanda

Il team costruisce poi un modello perché esiste un problema operativo reale di priorità. Il candidato validato temporalmente ottiene **AUC 0,84**, viene controllato per calibration sui decili e per leakage rispetto a informazioni disponibili soltanto dopo il momento decisionale. Tra le feature più informative compaiono diminuzione di utilizzo, mancata attivazione della feature core, ticket, distanza dal renewal, NPS e seat utilization.

La Predictive Decision Card, però, registra il limite che impedisce al modello di diventare una policy da solo: **feature importance non equivale a causalità**. Molti ticket possono predire churn perché sono conseguenza di un problema sottostante; eliminare o ridurre il ticket count non implica ridurre churn.

Microsoft Customer Insights offre un buon esempio documentato del ruolo corretto della prediction: la documentazione corrente richiede una definizione esplicita di churn e finestra predittiva, costruisce score di rischio e permette di creare segmenti di clienti ad alto rischio. Questo supporta la fase “chi ha maggior probabilità di churn”, non la domanda “quale trattamento cambierà il suo outcome?”.[^ms-churn]

### I clienti più a rischio non sono necessariamente i migliori da trattare

Tra i 500 score più alti NorthPeak trova account con azienda chiusa, merger, budget eliminato, migrazione strategica già deliberata o incompatibilità strutturale con il prodotto. Sono clienti che possono avere churn probability elevatissima e treatment effect vicino a zero per l'intervento disponibile.

La priorità operativa deve quindi combinare almeno quattro oggetti diversi:

```text
risk of churn
× economic value
× incremental treatment opportunity
− intervention cost
```

La capacità limitata del Customer Success team rende questa distinzione materiale. Un account a rischio medio ma ad alto valore e persuadibilità può essere un uso migliore di una delle 500 slot rispetto a un account quasi certamente perso.

Anche lo storico delle chiamate CSM dimostra perché prediction e causalità non possono essere confuse. I CSM chiamavano soprattutto account già fragili e, nei dati osservazionali, chi riceveva una chiamata churnava di più. Concludere che la chiamata “causa churn” invertirebbe il meccanismo di assegnazione: il rischio ha causato il trattamento.

Questa è la ragione concreta per cui entra il **Causal Identification Brief**. Non per completare il catalogo del libro, ma perché senza di esso la policy rischia di ottimizzare un'associazione selezionata.

### Qui l'esperimento guadagna davvero il diritto di esistere

Il team decide di testare un programma di onboarding intensivo sui nuovi account partner-channel. L'unità di randomizzazione è l'account; il primary outcome è activation entro 30 giorni, con renewal e NRR come outcome downstream; i guardrail includono costo CSM, ticket e time-to-resolution. L'eterogeneità da esplorare viene pre-specificata prima di guardare i risultati.

L'esperimento non deve “validare il churn model”. Deve stimare se **un intervento specifico cambia un outcome specifico** nella popolazione in cui il deterioramento è iniziato.

A questo punto le alternative sono diventate più mature. Ordinare semplicemente i 500 score più alti è facile ma confonde rischio e persuadibilità. Correggere soltanto onboarding partner-channel affronta il driver principale ma lascia scoperti gli account legacy già in deterioramento. La policy preferita combina invece correzione dell'onboarding, intervento anticipato, risk score per prioritizzazione, esclusione dei casi non persuadibili/economicamente non convenienti e sperimentazione per stimare l'incremental effect delle azioni.

La policy non è permanente. Cambia se l'uplift dell'onboarding intensivo è vicino a zero, il costo per renewal salvato supera il contribution margin atteso, il partner channel migliora spontaneamente dopo correzioni di processo, il modello perde calibration o la capacità Customer Success cambia materialmente.

### Evidence Ledger al decision point

| Observed | Inferred | Still unknown |
|---|---|---|
| churn 2,8%→4,1% | problema principale nasce nel nuovo onboarding partner | treatment effect dell'onboarding intensivo |
| activation 71%→54% | alcuni top-risk sono poco persuadibili | costo per renewal realmente salvato |
| feature-core use -19%, ticket +32%, TTFV +4,6 giorni | risk score utile per capacity allocation | eterogeneità stabile del treatment effect |
| model AUC 0,84, temporal validation/calibration | | |

La headline executive può quindi dire:

> **Il deterioramento di churn è concentrato nelle nuove coorti partner-channel e comincia durante l'attivazione. Il risk model aiuta a prioritizzare, ma non identifica chi possiamo salvare. Proponiamo di correggere onboarding e allocare la capacità retention usando rischio, valore e incremental treatment effect.**

L'outcome review segue activation a 30 giorni, time-to-first-value, feature adoption, renewal, incremental retention uplift, costo per renewal salvato, NRR per coorte e calibration drift.

**Percorso minimo effettivo:** Analytical Brief → Lifecycle Diagnostic Map → Predictive Decision Card → Causal Identification Brief → Experiment Contract → Decision Record → Decision Communication Pack.

Qui la catena è più lunga di Orion Living per una ragione precisa: la decisione non chiede soltanto **chi rischia**, ma anche **su chi l'azione produce valore**.

> **Predire chi perderemo non equivale a sapere chi possiamo salvare. Sapere chi possiamo salvare non equivale ancora a sapere se conviene usare su di lui una delle 500 opportunità di intervento.**

[^ms-churn]: Microsoft Learn, *Predict transaction churn*, https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/predict-transactional-churn ; Microsoft Learn, *Subscription churn prediction sample guide*, https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/sample-guide-predict-subscription-churn
