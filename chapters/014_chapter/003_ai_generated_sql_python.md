## 14.2 AI-generated SQL e Python: il codice è una proposta eseguibile, non una prova

Generare SQL, Python, R, formule o test è uno dei vantaggi più immediati dell'AI. Il guadagno di velocità è reale, ma cambia anche una vecchia euristica: oggi possiamo produrre molto codice **prima** di aver stabilito che quel codice rappresenta il problema giusto. Per questo l'artefatto generato non entra direttamente nell'interpretazione. Entra in un percorso di verifica.

Un modo utile per ragionare è distinguere quattro correttezze. La prima è **sintattica**: il codice compila o gira? La seconda è **computazionale**: implementa correttamente l'algoritmo o la formula dichiarata? La terza è **semantica**: popolazione, grain, date, metriche e business rule sono quelle corrette? La quarta è **decisionale**: l'output è adatto alla scelta e al livello di claim richiesto? Un sistema generativo può essere molto forte sul primo livello. Il lavoro professionale consiste nel non confonderlo con l'ultimo.

### Retention D30: codice elegante, specifica sbagliata

Un'app consumer chiede di calcolare retention D30 per signup cohort. L'AI genera una query che cerca utenti attivi esattamente 30 giorni dopo il signup. La query è sintatticamente e computazionalmente corretta, ma la definizione aziendale è diversa:

```text
D30 retained = almeno un evento qualificante tra D27 e D33
```

perché il prodotto ha uso prevalentemente settimanale. Inoltre gli utenti test devono essere esclusi, l'activation deve essere completata entro D2 per entrare nella cohort e le date di prodotto sono locali, non UTC. Non esiste un bug tradizionale. Il codice ha implementato una definizione plausibile che nessuno aveva autorizzato. Il **Context Pack** viene quindi prima della generazione.

### Verification Bundle

Per un artefatto importante non chiediamo soltanto il codice; chiediamo un **Verification Bundle**. Per una query può contenere:

```text
expected output grain
row-count invariants
key uniqueness checks
join cardinality checks
reconciliation query
edge cases
small hand-computable fixture
performance / scan estimate se rilevante
```

Una query di controllo può verificare, per esempio, che esista una sola riga per utente nella cohort finale o che un join non elimini una quota inattesa della popolazione. La verifica è più forte quando almeno una parte del percorso è indipendente dalla generazione: test deterministici, reconciliation verso metriche certificate, fixture note o peer review riducono il rischio che lo stesso errore di contesto venga ripetuto sia nella proposta sia nella critique.

### Prima milioni di righe, poi cinque casi che possiamo capire

Una piccola fixture rende l'errore falsificabile prima della scala:

| user | signup | activity | expected D30 |
|---|---|---|---:|
| A | 1 gen | 31 gen | 1 |
| B | 1 gen | 28 gen | 1 |
| C | 1 gen | 10 feb | 0 |
| D | 1 gen | nessuna | 0 |
| E | test account | 31 gen | excluded |

Se il codice non produce il risultato atteso su cinque casi comprensibili, non ha senso fidarsi perché "sembra giusto" su centinaia di milioni di eventi. Questo è particolarmente importante con codice AI-generated, che può amplificare il **plausibility bias**: l'output è ordinato, il runtime termina, i numeri hanno la scala attesa e quindi il reviewer abbassa la guardia.

### Gli invarianti del metodo restano validi

La stessa disciplina vale per Python e modeling. Consideriamo:

```python
X_filled = imputer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_filled, y)
```

Il codice gira, ma l'imputer è stato fit prima dello split e quindi apprende anche dalla distribuzione del test set. Il Capitolo 10 ha già trattato leakage: qui la lezione è che il reviewer deve applicare gli invarianti del metodo al codice generato. Per un modello predittivo possono essere: fit solo sul training, feature disponibili `as-of` prediction time, split coerente con deployment, baseline, calibration/threshold separati e metriche per segmento e tempo.

### Quando generazione ed esecuzione si fondono

Se un agente può eseguire ciò che genera, il rischio cambia. Una query proposta che dobbiamo copiare manualmente è diversa da un agente autorizzato a fare `DELETE`, `UPDATE`, `MERGE` o `CREATE OR REPLACE`. Per l'analisi ordinaria una policy sensata è:

```text
read-only by default
write only when required by the task
approval before destructive or irreversible action
```

Lo stesso principio vale fuori dal database: preparare una bozza email non equivale a inviarla; creare un file non equivale a sovrascriverlo; proporre una modifica a un dashboard non equivale a pubblicarla. La **permission boundary** è parte della correttezza del sistema.

### Acceptance gate

Un artefatto AI-generated entra nella catena analitica soltanto quando supera un gate dichiarato, per esempio:

```text
must compile/run
must pass tests
must preserve expected grain
must reconcile within tolerance
must respect permission policy
must satisfy cost/runtime limit
must have no unresolved critical warning
```

La AI Analysis Control Sheet registra artefatto, ambiente di esecuzione, permission mode, invarianti, fixture, controlli indipendenti, target di reconciliation, limiti di costo/runtime, reviewer e risultato dell'acceptance gate.

> **L'AI abbassa il costo di scrivere codice. Il processo analitico deve abbassare anche il costo di falsificarlo: piccoli test, invarianti e reconciliation devono diventare parte standard dell'artefatto.**
