## 14.2 AI-generated SQL e Python: il codice è una proposta eseguibile, non una prova

La generazione di codice è uno dei vantaggi più immediati dell'AI per un Data Analyst.

Possiamo ottenere rapidamente:

- SQL;
- Python/R;
- formule;
- test;
- trasformazioni;
- boilerplate;
- documentazione tecnica.

Il guadagno è reale.

Ma proprio perché il costo di scrittura si avvicina a zero, una vecchia euristica smette di funzionare:

> “Se il codice è complesso e ci ha richiesto molto lavoro, probabilmente qualcuno lo ha pensato con attenzione.”

Con AI possiamo produrre **molto codice prima di aver stabilito che il codice rappresenta il problema giusto**.

Per questo il codice generato va trattato come:

> **una proposta eseguibile che deve attraversare evidence gates.**

## 14.2.1 Le quattro correttezze

Prima di usare un artefatto generato distinguiamo quattro livelli.

### Correttezza sintattica

Il codice compila o gira?

### Correttezza computazionale

Implementa correttamente l'algoritmo o la formula dichiarata?

### Correttezza semantica

Popolazione, grain, date, metriche e business rules sono quelle corrette?

### Correttezza decisionale

L'output è adatto alla decisione e al livello di claim richiesto?

Un sistema generativo è spesso molto forte sul primo livello.

Il lavoro professionale consiste nel non confondere il primo gate con l'ultimo.

## 14.2.2 Caso simulato/composito — retention D30 perfettamente sbagliata

Un'app consumer chiede:

> Calcola retention D30 per signup cohort.

L'AI genera una query elegante che identifica utenti attivi esattamente 30 giorni dopo signup.

La query è sintatticamente e computazionalmente corretta.

Ma la definizione aziendale è:

```text
D30 retained = almeno un evento qualificante tra D27 e D33
```

perché il prodotto ha uso prevalentemente settimanale.

In più:

- gli utenti test devono essere esclusi;
- activation deve essere completata entro D2 per entrare nella cohort;
- le date di prodotto sono locali, non UTC.

Il codice non contiene un bug tradizionale.

Ha implementato **una specifica che nessuno aveva realmente definito**.

Questo è precisamente il motivo per cui il Context Pack viene prima della generazione.

## 14.2.3 Il Verification Bundle

Non chiediamo soltanto codice.

Chiediamo un **Verification Bundle**.

Per una query può includere:

```text
1. expected output grain
2. row-count invariants
3. key uniqueness checks
4. join cardinality checks
5. reconciliation query
6. edge cases
7. small hand-computable fixture
8. performance / scan estimate se rilevante
```

Esempio:

```sql
-- deve esistere una riga per user nella cohort finale
SELECT user_id, COUNT(*) AS n
FROM cohort_final
GROUP BY user_id
HAVING COUNT(*) > 1;
```

Oppure:

```sql
-- quale percentuale della popolazione viene persa dopo il join?
SELECT
    COUNT(DISTINCT b.user_id) AS before_join,
    COUNT(DISTINCT j.user_id) AS after_join
FROM base_population b
LEFT JOIN joined_population j USING (user_id);
```

La query generata e i test non devono necessariamente provenire dallo stesso sistema.

Quando il rischio è alto, **indipendenza del percorso di verifica** aumenta il valore del controllo.

## 14.2.4 Test fixture: prima milioni di righe, cinque casi che possiamo capire

Un metodo molto efficace è creare una piccola fixture con casi noti.

Esempio retention:

| user | signup | activity | expected D30 |
|---|---|---|---:|
| A | 1 gen | 31 gen | 1 |
| B | 1 gen | 28 gen | 1 |
| C | 1 gen | 10 feb | 0 |
| D | 1 gen | nessuna | 0 |
| E | test account | 31 gen | excluded |

Prima di lanciare la query su centinaia di milioni di eventi possiamo verificare se produce il risultato atteso su cinque righe comprensibili.

Questa pratica è particolarmente utile con codice AI-generated perché riduce il rischio di **plausibility bias**: fidarsi del risultato perché “sembra giusto” su una tabella enorme.

## 14.2.5 Python: pipeline leakage e hidden preprocessing

Consideriamo:

```python
X_filled = imputer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_filled, y)
```

Il codice gira.

Ma il preprocessing è fit prima dello split e quindi impara anche dalla distribuzione del test set.

La lezione non è “l'AI sbaglia sklearn”.

Il Capitolo 10 ha già trattato leakage.

Qui la lezione è:

> **il reviewer deve applicare gli invarianti del dominio tecnico al codice generato, non limitarsi a chiedere al modello se il codice è corretto.**

Per modeling, gli invarianti possono includere:

- fit solo sul training;
- feature disponibili `as-of` prediction time;
- split coerente con deployment;
- baseline;
- calibration/threshold separati;
- metriche per segmento e tempo.

## 14.2.6 Read-only by default

Se l'AI può usare tool, la generazione di codice si fonde con l'esecuzione.

Questo cambia il rischio.

Una proposta SQL che dobbiamo copiare manualmente è diversa da un agente con permesso di eseguire:

```sql
DELETE
UPDATE
MERGE
CREATE OR REPLACE
```

Per analisi ordinarie una policy ragionevole è:

```text
read-only by default
write only when the task requires it
approval before destructive/irreversible action
```

Il principio vale anche fuori dal database:

- creare file è diverso da sovrascriverli;
- preparare una bozza email è diverso da inviarla;
- proporre un dashboard change è diverso da pubblicarlo.

La **permission boundary** è parte della correttezza del workflow.

## 14.2.7 AI come reviewer: utile, ma non indipendente per definizione

Chiedere:

> Trova cinque failure mode in questa query.

può essere molto utile.

Ma “AI genera” + “stessa AI approva” non equivale automaticamente a review indipendente.

Possiamo migliorare la separazione usando:

- test deterministici;
- query di reconciliation;
- fixture note;
- regole statiche;
- peer review umana;
- secondo modello/configurazione quando appropriato;
- confronto con asset certificati.

L'obiettivo non è moltiplicare revisori.

È evitare che **lo stesso errore di contesto** venga ripetuto in generation e critique.

## 14.2.8 Acceptance gate per codice generato

Per un artefatto importante definiamo prima:

```text
must compile/run
must pass tests
must preserve expected grain
must reconcile within tolerance
must respect permission policy
must satisfy cost/runtime limit
must produce no unresolved critical warning
```

Solo dopo può diventare input dell'interpretazione.

### Campo della AI Analysis Control Sheet

```text
Generated artifact:
Execution environment:
Permission mode:
Expected invariants:
Fixture / golden cases:
Tests generated:
Independent checks:
Reconciliation target:
Performance/cost limit:
Reviewer:
Acceptance result:
```

### Regola operativa

> **L'AI abbassa il costo di scrivere codice. Il processo analitico deve abbassare anche il costo di falsificarlo: piccoli test, invarianti e reconciliation devono diventare parte standard dell'artefatto.**
