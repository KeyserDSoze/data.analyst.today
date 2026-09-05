## 10.6 Data leakage e training-serving skew: proteggere la frontiera `as-of`

Un modello può sembrare straordinario semplicemente perché gli abbiamo lasciato leggere informazione che, nel momento reale della decisione, non esiste ancora.

Questo è il senso professionale del **data leakage**: il processo di training o validation riceve informazione che non sarebbe disponibile **nella stessa forma e nello stesso momento** al prediction time. Il risultato non è soltanto una metrica ottimistica. È la valutazione di un sistema che in produzione non potremo riprodurre.

La regola più utile è immaginare, per ogni prediction row, una query storica:

> **“Mostrami soltanto ciò che il sistema conosceva alle 06:00 del 3 marzo 2025.”**

Se una feature non può essere ricostruita `as-of` quel momento senza utilizzare aggiornamenti successivi, non appartiene alla feature set validata per quella previsione.

### Il futuro può entrare in modi diversi

A volte il leakage è evidente: predire churn il 1° marzo usando ticket aperti durante marzo, oppure predire default usando `sent_to_collections`, valorizzato soltanto dopo la mora. Più spesso è nascosto nel processo.

Può entrare quando preprocessing, scaling, imputazione o feature selection imparano anche dal validation/test set; quando lo stesso soggetto compare quasi duplicato nei due lati dello split; oppure quando una tabella “storica” è in realtà una current-state table ricalcolata oggi.

Per questo split e feature lineage devono essere verificati insieme.

### Caso reale documentato — 10.000 feature casuali e accuracy 0,76

La documentazione scikit-learn mostra un esempio volutamente estremo con **200 osservazioni**, target binario casuale e **10.000 feature generate casualmente**. Non esiste segnale reale.

Se però la feature selection viene eseguita sull'intero dataset prima dello split, un modello può raggiungere accuracy circa **0,76**. La selezione ha usato anche il target del futuro test set e ha premiato coincidenze casuali favorevoli.

Quando l'ordine diventa correttamente:

```text
split
→ fit feature selection sul train
→ transform train/test
→ fit model
→ evaluate
```

la performance torna vicino al caso.

Riferimento: https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

La lezione è più ampia della feature selection: una trasformazione legittima diventa leakage se impara dal set che dovrebbe valutare la generalizzazione.

### Pipeline significa anche proteggere il confine

Scikit-learn raccomanda le `Pipeline` perché aiutano a fit-tare scaler, imputer e selector soltanto sui dati consentiti all'interno dei fold. Ma il principio è tool-agnostic: vale per SQL, notebook, dbt, feature store, cloud pipeline e codice generato da AI.

Una pipeline ben costruita non può però decidere da sola se `retention_offer_status` nasce prima o dopo il churn intent. Per questo il controllo sintattico deve essere accompagnato da lineage e semantica temporale.

### Caso simulato/composito — HealthFlow

HealthFlow vuole prevedere no-show 48 ore prima dell'appuntamento. Un primo modello raggiunge **AUC 0,94**. Tra le feature compare `days_since_last_contact`, apparentemente storica.

Il CRM però ricalcola quel campo ogni notte rispetto allo stato corrente. Quando ricostruiamo appuntamenti di sei mesi fa, il valore incorpora contatti avvenuti **dopo** l'appuntamento. Ricostruendo la feature da log storici realmente `as-of`, l'AUC scende a **0,72**.

Il secondo numero è meno spettacolare ed è il primo credibile. Una diminuzione di performance può essere un miglioramento della qualità dell'evidenza.

### Leakage e training-serving skew sono parenti, non sinonimi

Il leakage descrive un processo di sviluppo che ha visto troppo. Il **training-serving skew** compare quando il modello in produzione vede qualcosa di diverso da ciò su cui è stato addestrato o validato: preprocessing differente, latenze diverse, definizioni non allineate, dati che cambiano o feedback loop.

Google documenta casi di produzione in cui questo skew ha degradato la performance e raccomanda di misurarlo esplicitamente, riutilizzando quando possibile la stessa logica tra training e serving e loggando le feature realmente viste online.

Riferimento: https://developers.google.com/machine-learning/guides/rules-of-ml/

### Feature availability matrix

Per modelli importanti la frontiera informativa merita un artefatto esplicito:

| Feature | Source | Available at prediction time? | Historical `as-of` available? | Serving latency |
|---|---|---|---|---|
| invoice_balance | billing snapshot | sì | sì | 1h |
| latest_ticket_status | CRM current state | sì oggi | **no storico affidabile** | realtime |
| cancellation_reason | cancellation event | no | sì | post-outcome |
| app_sessions_30d | event log | sì | sì | 15m |

Una feature con “no storico affidabile” potrebbe essere tecnicamente disponibile in futuro, ma non può essere usata oggi per una validation storica onesta finché non ricostruiamo quella history.

### Anti-leakage review

Prima di fidarci di una performance sorprendente dobbiamo riuscire a difendere prediction time, timestamp di nascita delle feature, storico `as-of`, separazione tra feature window e label window, preprocessing fit sul solo train/fold, split delle entità, training-serving parity e plausibilità del risultato.

> **Quando un modello sembra conoscere troppo bene il futuro, la prima domanda non è quale algoritmo abbiamo inventato. È da quale passaggio della pipeline è entrato il futuro.**