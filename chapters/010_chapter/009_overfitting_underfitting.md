## 10.9 Overfitting e underfitting: la complessità deve comprare generalizzazione

Un modello non viene premiato perché descrive bene il training set. Viene premiato quando il pattern che ha imparato sopravvive a nuove osservazioni, nuovi periodi, slice importanti e deployment reale.

Underfitting e overfitting sono due modi opposti di fallire questa promessa. Nel primo caso il modello non cattura abbastanza struttura nemmeno nel training; nel secondo cattura anche rumore e coincidenze che non si ripetono fuori campione. La distinzione importante, però, non è il nome del fallimento. È **dove e perché la performance smette di generalizzare**.

### Caso simulato/composito — FalconCredit

FalconCredit stima il rischio di insolvenza a 90 giorni:

| Modello | Feature | AUC train | AUC validation |
|---|---:|---:|---:|
| logistic baseline | 18 | 0,71 | 0,70 |
| boosting esteso | 240 | 0,94 | 0,73 |

La slide iniziale mette in grande `0,94`. È il numero meno utile per decidere. Il miglioramento che deve giustificare 240 feature, serving e monitoring è **0,70 → 0,73** fuori campione.

Tre punti di AUC possono valere moltissimo oppure quasi nulla. La domanda successiva è quindi: al top-K o alla soglia operativa, quanti casi aggiuntivi vengono identificati? Quanto costa produrre le feature? Quanto è stabile il guadagno nei periodi e segmenti che contano?

### Il train-validation gap è un indizio, non una diagnosi completa

Un train score molto alto e validation molto più bassa è compatibile con alta variance. Ma se la validation appartiene a un periodo nuovo o a una popolazione diversa, parte del calo può riflettere distribution shift. Per questo non basta dire “overfitting”: dobbiamo localizzare il deterioramento.

Learning e validation curves possono aiutare. Se la validation continua a migliorare con più dati, raccogliere altri esempi può avere valore. Se train e validation convergono entrambi a performance mediocre, più dati dello stesso tipo potrebbero non bastare. Se il gap resta elevato, regolarizzazione o riduzione di complessità diventano candidate naturali.

Riferimento: https://scikit-learn.org/stable/modules/learning_curve.html

La documentazione scikit-learn mostra anche il caso didattico di regressioni polinomiali: un modello troppo semplice non cattura la funzione, uno intermedio generalizza, uno molto flessibile segue quasi perfettamente i dati osservati ma peggiora in cross-validation.

Riferimento: https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html

### Ogni feature aggiunge più di un costo statistico

La complessità ha almeno quattro prezzi. Statisticamente aumenta la libertà di inseguire rumore; sul dato richiede più lineage, history e qualità; operativamente aggiunge dipendenze, latency e failure mode; nella governance rende più difficile spiegare e monitorare il sistema.

Per questo un modello più complesso deve poter rispondere:

> **quale miglioramento fuori campione produce, in quale parte della policy, e quanto vale rispetto ai costi che introduce?**

### Anche il processo di model search può overfittare

Se proviamo centinaia di configurazioni sullo stesso validation set e scegliamo il massimo decimale, stiamo adattando anche la ricerca al campione. Cross-validation coerente, un test finale isolato e confronto con baseline riducono questo rischio.

Inoltre la performance globale può nascondere **slice overfitting**. Conviene confrontare train/validation gap per periodo, popolazioni business critiche, code dell'errore e stabilità tra fold. Un modello che batte la baseline in tutti i periodi con margine modesto può essere più affidabile di uno con media più alta che crolla nei momenti operativamente importanti.

La comunicazione dovrebbe quindi suonare così:

> “Rispetto alla baseline, il modello migliora AUC fuori campione da 0,70 a 0,73; al punto operativo aumenta precision da X a Y; il miglioramento è stabile in questi periodi e debole in questi altri; il costo aggiuntivo è Z.”

> **La complessità non è progresso. È un investimento che deve produrre generalizzazione e valore decisionale misurabili.**