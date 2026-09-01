## 10.9 Overfitting e underfitting: la complessità deve guadagnarsi il diritto di esistere

Un modello non viene premiato perché descrive bene il training set.

Viene premiato se il pattern che ha imparato sopravvive a:

- nuove osservazioni;
- nuovi periodi;
- segmenti importanti;
- piccole variazioni del campione;
- deployment reale.

Questa è la generalizzazione.

Due fallimenti opposti sono:

- **underfitting:** il modello non cattura abbastanza struttura nemmeno nel training;
- **overfitting:** cattura anche dettagli, rumore e coincidenze che non si ripetono fuori campione.

### Caso simulato/composito — FalconCredit

FalconCredit stima il rischio di insolvenza a 90 giorni.

Confronta:

| Modello | Feature | AUC train | AUC validation |
|---|---:|---:|---:|
| logistic baseline | 18 | 0,71 | 0,70 |
| boosting esteso | 240 | 0,94 | 0,73 |

La slide iniziale mette in grande `0,94`.

È il numero meno importante della tabella.

Il miglioramento che deve giustificare complessità, serving e monitoring è `0,70 → 0,73` fuori campione.

Potrebbe essere molto prezioso. Potrebbe essere troppo piccolo. Dipende da ciò che cambia alla soglia operativa.

### Il gap train-validation è una diagnosi, non una formula automatica

Un pattern classico:

```text
train molto alto
validation molto più basso
```

è compatibile con alta variance / overfitting.

Due score bassi possono indicare underfitting o segnale predittivo debole.

Ma il gap va interpretato insieme al design della validation.

Se validation appartiene a un periodo nuovo e difficile, parte del calo può essere **distribution shift**, non soltanto overfitting tradizionale.

Per questo la domanda più utile è:

> **dove e perché il modello smette di generalizzare?**

### Learning curve: più dati o modello diverso?

Una learning curve confronta performance train/validation al crescere della quantità di dati.

Può aiutare a distinguere situazioni come:

- validation continua a migliorare con più dati → raccogliere dati può avere valore;
- train e validation convergono entrambi a performance mediocre → più dati dello stesso tipo potrebbero non bastare;
- gap train-validation rimane elevato → serve più regolarizzazione, meno complessità o feature più robuste.

Scikit-learn usa learning e validation curves proprio per diagnosticare bias/variance e comportamento della generalizzazione.

Fonte: https://scikit-learn.org/stable/modules/learning_curve.html

### Caso reale documentato — underfitting e overfitting nell'esempio scikit-learn

Scikit-learn mostra un esempio didattico con regressioni polinomiali di complessità crescente:

- un modello troppo semplice non cattura la funzione;
- un modello intermedio generalizza bene;
- un modello molto flessibile segue quasi perfettamente le osservazioni ma performa peggio in cross-validation.

La lezione non è "usa grado X". È che **training fit e predictive value sono oggetti differenti**.

Fonte: https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html

### Complexity budget

Ogni aumento di complessità ha almeno quattro costi potenziali:

**1. Statistical cost**  
Più libertà di adattarsi a rumore o sottogruppi fragili.

**2. Data cost**  
Più feature da produrre con lineage, qualità e history corretti.

**3. Operational cost**  
Più dipendenze, latency, serving e failure mode.

**4. Governance cost**  
Più difficile spiegare, monitorare, validare e revisionare il comportamento.

Perciò una nuova complessità dovrebbe poter rispondere:

> **quale miglioramento fuori campione otteniamo e quale decisione migliora abbastanza da giustificare questi costi?**

### Slice overfitting

Un modello può avere performance globale buona e adattarsi male a segmenti specifici.

Controlliamo quindi non solo la media, ma almeno:

- train/validation gap globale;
- performance per periodo;
- performance per popolazioni business rilevanti;
- code dell'errore;
- stabilità tra fold.

Questo è particolarmente importante se la decisione ha costo diverso tra segmenti.

### Hyperparameter search e multiple tries

Anche il processo di modeling può overfittare la validation.

Se testiamo centinaia di configurazioni e scegliamo quella con score massimo sullo stesso set, parte della "vittoria" può essere fortuna di selezione.

Per progetti intensivi servono quindi:

- cross-validation adeguata;
- test finale isolato;
- confronti con baseline;
- preferenza per miglioramenti replicabili, non per il massimo decimale ottenuto.

### Regola editoriale e operativa

Non presentare:

> "il modello complesso ha AUC 0,94."

Presenta:

> **"Rispetto alla baseline, il modello migliora la metrica fuori campione da 0,70 a 0,73; al top 5% aumenta precision da X a Y; il costo aggiuntivo è Z; il miglioramento è stabile in questi periodi e non in questi altri."**

> **La complessità non è progresso. È un investimento che deve produrre generalizzazione e valore decisionale misurabili.**
