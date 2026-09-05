## 10.11 Cross-validation: misurare quanto la performance dipende dal futuro simulato

Un singolo split può essere corretto e comunque fortunato o sfortunato. La cross-validation aiuta a capire quanto la performance dipenda dalla particolare divisione dei dati e permette di fare model selection senza consumare subito il test finale.

Ma il numero di fold viene dopo la domanda centrale:

> **quale futuro stiamo cercando di simulare?**

Se i fold non rappresentano il modo in cui il modello dovrà generalizzare, una media molto precisa può essere precisamente irrilevante.

### Caso simulato/composito — MedSupply

MedSupply prevede ritardi superiori a 48 ore per ordini ospedalieri. Un singolo split produce AUC 0,82. Cinque fold mostrano:

| Fold | AUC |
|---|---:|
| 1 | 0,83 |
| 2 | 0,81 |
| 3 | 0,74 |
| 4 | 0,79 |
| 5 | 0,72 |

La media è circa 0,78. Ma la parte interessante non è il nuovo decimale: i fold peggiori contengono molte più spedizioni internazionali.

La dispersione apre quindi una domanda diagnostica: domestic e international sono due processi predittivi differenti? Mancano feature? Il volume internazionale è insufficiente? Nascondere tutto dietro `mean AUC = 0,78` eliminerebbe proprio l'informazione che serve per migliorare il sistema.

### Random K-fold non è un default universale

K-fold casuale è sensato quando le osservazioni sono abbastanza exchangeable rispetto al deployment. È fragile con tempo, gruppi, entità ripetute, geografie o dipendenze tra righe.

In questi casi possiamo usare group split, stratificazione quando serve a preservare il base rate, forward validation temporale oppure holdout geografici. Il nome dell'oggetto software conta meno della domanda che il fold rappresenta.

Per target futuri, il training non dovrebbe includere informazione cronologicamente successiva alla previsione che il fold sta simulando. Una sequenza possibile è:

```text
train fino a giugno  → validate luglio
train fino a luglio  → validate agosto
train fino ad agosto → validate settembre
```

Il Capitolo 7 ha già approfondito il backtesting temporale; qui usiamo lo stesso principio per qualunque prediction system.

### Caso simulato/composito — Finora

Finora costruisce un modello di default. La random CV produce AUC media **0,86**. La forward validation restituisce **0,81**, **0,78**, **0,75** nei trimestri successivi. Acquisition mix e underwriting sono cambiati nel tempo.

La random CV non è “sbagliata” in astratto: risponde a una domanda più facile. Il forward design assomiglia maggiormente alla produzione che il business vuole affrontare.

### Tuning e validation fanno parte dello stesso processo di ricerca

Se usiamo la cross-validation per scegliere feature, regularization, hyperparameter, modello, calibration method o threshold, tutte queste decisioni stanno imparando da quei fold. Per progetti con tuning intenso può quindi servire un final holdout, nested CV oppure un successivo periodo out-of-time davvero untouched.

Non serve applicare la procedura più complessa a ogni progetto. Serve sapere quando la ricerca stessa rischia di overfittare la valutazione.

### La dispersione tra fold è un risultato

Un report migliore di `mean = 0,81` mostra media, range tra fold, composizione dei fold, worst business slice e confronto con la stessa baseline in ciascun fold. Un modello che supera la baseline in tutti i periodi con margine modesto può essere preferibile a uno con media maggiore ma failure severi in periodi cruciali.

Nella Predictive Decision Card useremo quindi una frase come:

> **“La validation lascia fuori interi account e rispetta l'ordine temporale perché il modello deve generalizzare sia a clienti nuovi sia a mesi futuri.”**

> **La cross-validation non rende robusta una valutazione per il solo fatto di ripeterla. La rende informativa quando ogni fold rappresenta un modo plausibile in cui il deployment potrà metterci alla prova.**