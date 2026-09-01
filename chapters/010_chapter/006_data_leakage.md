## 10.6 Data leakage e training-serving skew: il modello non può usare informazione che la decisione non possiede

Il leakage è uno dei modi più efficaci per costruire un modello eccellente che non esiste davvero.

Succede quando il processo di training riceve informazione che non sarebbe disponibile **nella stessa forma e nello stesso momento** quando la previsione deve essere prodotta.

La documentazione ufficiale di scikit-learn definisce il data leakage proprio in questi termini: informazione non disponibile al prediction time entra nella costruzione del modello e rende le metriche di validazione troppo ottimistiche.

Fonte: https://scikit-learn.org/stable/common_pitfalls.html

### La regola `as-of`

Per ogni prediction row dovrebbe essere possibile immaginare una query storica del tipo:

> **Mostrami solo ciò che il sistema conosceva alle 06:00 del 3 marzo 2025.**

Se una feature non può essere ricostruita `as-of` quel momento senza usare aggiornamenti successivi, non appartiene alla feature set di quella previsione.

Questa regola è più forte di:

> "la colonna esiste nel database."

Molte colonne esistono oggi proprio perché il futuro è già accaduto.

### Quattro forme comuni di leakage

**1. Future leakage**  
Eventi successivi al prediction time entrano direttamente nella feature.

Esempio: predire churn il 1° marzo usando ticket aperti tra il 1° e il 31 marzo.

**2. Target/label leakage**  
Una variabile è una conseguenza quasi diretta dell'outcome.

Esempio: prevedere default usando `sent_to_collections`, valorizzato solo dopo la mora.

**3. Preprocessing leakage**  
Imputazione, scaling, feature selection o altre trasformazioni imparano proprietà anche dal validation/test set.

**4. Entity/group leakage**  
Informazione quasi duplicata della stessa entità appare nei due lati dello split e rende la valutazione più semplice del deployment reale.

### Caso reale documentato — 10.000 feature casuali, accuracy 0,76

Scikit-learn mostra un esempio volutamente estremo.

Il dataset contiene:

- 200 osservazioni;
- target binario casuale;
- **10.000 feature generate casualmente**.

Non esiste alcun segnale reale.

Se però la feature selection viene fatta sull'intero dataset prima dello split, il modello può ottenere accuracy intorno a **0,76**.

La feature selection ha avuto accesso anche al target del futuro test set e ha selezionato coincidenze casuali favorevoli.

Quando il processo corretto diventa:

**split → fit feature selection sul train → transform train/test → fit model → evaluate**, 

la performance torna vicino al caso.

È uno dei migliori esempi di una regola generale:

> **anche una trasformazione perfettamente legittima può diventare leakage se impara dal futuro set di valutazione.**

Fonte: https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

### Pipeline: proteggere il confine, non solo organizzare codice

Scikit-learn raccomanda le `Pipeline` anche perché aiutano a garantire che trasformazioni come scaler, imputer e feature selector vengano fit solo sui dati di training durante validation e cross-validation.

Il principio è tool-agnostic.

Vale anche per:

- SQL transformations;
- notebook;
- feature store;
- dbt/modeling layer;
- cloud pipelines;
- AI-generated code.

La domanda è sempre:

> **quale dataset ha potuto influenzare la trasformazione che sto applicando?**

### Caso simulato/composito — HealthFlow e il campo che cambia retroattivamente

HealthFlow vuole prevedere no-show 48 ore prima di un appuntamento per decidere chi riceve reminder intensivi.

Un modello iniziale raggiunge AUC 0,94.

Tra le feature c'è:

`days_since_last_contact`

Il campo sembra storico, ma il CRM lo ricalcola ogni notte rispetto allo stato corrente.

Quando l'analista ricostruisce appuntamenti di sei mesi fa, il valore incorpora anche contatti avvenuti **dopo** l'appuntamento.

Ricostruendo la feature tramite log storici `as-of`, l'AUC scende a 0,72.

Il secondo risultato è molto meno impressionante. È anche il primo risultato reale.

### Training-serving skew: stessa feature, significato diverso

Il leakage riguarda spesso il training storico. In produzione compare un problema affine: **training-serving skew**.

Google documenta sistemi di produzione in cui differenze tra pipeline di training e serving hanno degradato la performance. Le cause includono:

- preprocessing implementato diversamente;
- feature aggiornate con latenze diverse;
- cambi di distribuzione;
- feedback loop del sistema.

Google raccomanda di misurare esplicitamente lo skew e, dove possibile, di riutilizzare o loggare le stesse feature viste al serving.

Fonte: https://developers.google.com/machine-learning/guides/rules-of-ml/

Questa distinzione è utile:

- **leakage:** il modello in sviluppo ha visto troppo;
- **training-serving skew:** il modello in produzione vede qualcosa di diverso da ciò su cui è stato addestrato.

Entrambi rompono la promessa della validation.

### Feature availability matrix

Per modelli importanti conviene creare una tabella come:

| Feature | Source | Available at prediction time? | Historical as-of available? | Serving latency |
|---|---|---|---|---|
| invoice_balance | billing snapshot | sì | sì | 1h |
| latest_ticket_status | CRM current state | sì oggi | **no storico affidabile** | realtime |
| cancellation_reason | cancellation event | no | sì | post-outcome |
| app_sessions_30d | event log | sì | sì | 15m |

Una riga "no storico affidabile" non significa necessariamente che la feature non sarà mai usabile. Significa che non possiamo validare onestamente oggi il modello storico che la usa senza ricostruire quella storia.

### AI e leakage

Un LLM può generare in pochi secondi:

- split;
- preprocessing;
- feature selection;
- modello;
- metriche.

Non può dedurre automaticamente dalla colonna `retention_offer_status` se il valore viene scritto prima o dopo il churn intent, se non gli forniamo lineage e semantica temporale.

È un esempio perfetto della tesi del Capitolo 0: la sintassi può essere delegata; la responsabilità sulla frontiera informativa no.

### Anti-leakage review

Prima di fidarti di un modello molto performante, verifica:

- prediction time esplicito;
- timestamp di nascita di ogni feature;
- storico `as-of` reale, non ricostruito con current state;
- label window e feature window non sovrapposte impropriamente;
- preprocessing fit solo sul train/fold corretto;
- entity/group split coerente;
- training-serving parity;
- plausibilità della performance rispetto al problema.

> **Quando un modello sembra conoscere troppo bene il futuro, la prima ipotesi non dovrebbe essere “abbiamo trovato un algoritmo straordinario”. Dovrebbe essere “da dove è entrato il futuro?”**
