## 13.13 Tooling Decision Record: scegliere, motivare e sapere quando cambiare

Una checklist aiuta a non dimenticare domande.

Un **Tooling Decision Record (TDR)** fa un passo in più: registra la scelta in modo che tra sei mesi possiamo capire **perché era sensata e se lo è ancora**.

Non deve diventare burocrazia.

Per un'analisi semplice può stare in mezza pagina.

Per un prodotto critico può essere più dettagliato.

Il valore nasce da quattro obblighi:

1. partire dal problema;
2. confrontare alternative reali;
3. dichiarare i limiti della scelta;
4. definire un'**exit condition**.

### Prima regola: “non costruire” è un'alternativa

Tra le opzioni candidate dovrebbero poter comparire anche:

- risposta manuale una tantum;
- query ad hoc;
- usare un asset esistente;
- migliorare un processo già disponibile;
- non automatizzare ancora;
- non fare nulla perché il valore atteso è troppo basso.

Se confrontiamo soltanto strumenti nuovi, abbiamo già incorporato la conclusione nella domanda.

### TDR — sezione 1: decision context

```text
Decision / use case:
Business owner:
Who consumes the result:
Action enabled by the output:
Current stage:
  explore | prototype | recurring | production
Decision deadline:
Expected lifetime of the solution:
```

La distinzione tra **decision deadline** e **solution lifetime** è importante.

Possiamo aver bisogno di una risposta domani e di un processo stabile per i prossimi tre anni. Non necessariamente la stessa implementazione deve soddisfare entrambe le esigenze fin dal primo giorno.

### TDR — sezione 2: problem shape

```text
Data location:
Input scale:
Expected growth:
Number of sources:
Processing frequency:
Freshness required:
Method required:
  aggregation | EDA | statistics | simulation | ML | optimization | other
Human interaction required:
Downstream systems:
```

Questa parte impedisce di usare parole vaghe come:

> grandi dati

oppure:

> serve real time.

Servono numeri o almeno ordini di grandezza.

### TDR — sezione 3: risk and control

```text
Impact if wrong:
Impact if late:
Impact if unavailable:
Sensitive / regulated data:
Required reproducibility level: R0-R4
Audit requirement:
Recovery requirement:
Required review / approval:
```

Due problemi con lo stesso volume possono richiedere tool diversi se uno produce un report esplorativo e l'altro blocca transazioni.

### TDR — sezione 4: people and ownership

```text
Builder:
Long-term owner:
Available reviewers:
Team skills:
Bus factor:
Platform support available:
Who handles failures:
Who approves semantic changes:
```

Questa sezione impedisce di scegliere un sistema che esiste soltanto finché esiste la persona che lo ha costruito.

### TDR — sezione 5: candidates

Per ogni alternativa scriviamo almeno:

| Candidate | Vantaggi | Limiti | TCO / effort | Rischio | Reversibilità |
|---|---|---|---|---|---|
| Manual / one-off | | | | | |
| Existing tool/process | | | | | |
| Spreadsheet | | | | | |
| SQL/shared model | | | | | |
| Python/R/notebook | | | | | |
| BI | | | | | |
| Low-code | | | | | |
| Managed/shared platform | | | | | |

Non dobbiamo compilare righe irrilevanti.

L'importante è non confrontare una soluzione reale con un'alternativa caricaturale.

### TDR — sezione 6: chosen design

```text
Chosen tool / combination:
Where each responsibility lives:
Why it is sufficient now:
Why a simpler option is insufficient:
Why a more complex option is not justified yet:
Known limitations:
Controls required:
```

La domanda:

> **perché una soluzione più semplice non basta?**

è uno dei migliori antidoti all'overengineering.

La domanda opposta:

> **perché non serve ancora quella più sofisticata?**

impedisce di comprare future capability senza un requisito reale.

### TDR — sezione 7: exit condition

Questa è la parte più importante del record.

```text
Review / migrate if ANY of these becomes true:
- volume > ...
- frequency becomes ...
- consumers > ...
- manual effort > ... hours/month
- failure rate > ...
- output becomes input to ...
- sensitive data requirement changes
- reproducibility requirement moves from R... to R...
- business logic stabilizes enough to centralize
- latency requirement becomes ...
- bus factor drops below ...
- annual TCO exceeds ...
```

L'exit condition trasforma:

> Excel vs SQL

in una domanda molto più utile:

> **in quali condizioni Excel smette di essere sufficiente?**

### Caso simulato/composito — stessa domanda, tre TDR diversi

Domanda business:

> Quali account enterprise hanno ridotto l'uso del prodotto di oltre il 30% negli ultimi 60 giorni?

#### Scenario A — 2.000 account, review una tantum

```text
Choice: SQL export + spreadsheet
Reason: dataset piccolo, decisione domani, forte review manuale
Exit condition: processo diventa settimanale o condiviso da CS
```

#### Scenario B — 300 milioni di eventi, review settimanale

```text
Choice: SQL model nel warehouse + tabella account-level
Reason: compute vicino al dato, logica ripetibile
Serving: export o BI leggero
Exit condition: CS richiede monitoraggio continuo e self-service
```

#### Scenario C — 800 CS manager, workflow operativo

```text
Choice: certified SQL model + BI/CRM serving
Reason: consumo ricorrente, access control, refresh e ownership
Optional Python: risk model se aggiunge valore validato
Exit condition: score diventa automatic decision input → nuova production/risk review
```

La domanda business è identica.

Il sistema di responsabilità no.

### Decision gate in dieci domande

Prima di approvare la scelta, un reviewer dovrebbe riuscire a rispondere:

1. Quale decisione abilita?
2. Qual è il minimo requisito reale?
3. Dove vive il dato?
4. Quale parte del calcolo deve stare vicino al dato?
5. Quanto deve essere riproducibile?
6. Chi possiede il processo dopo il builder?
7. Quanto costa davvero possederlo?
8. Qual è il failure mode più costoso?
9. Esiste un'opzione più semplice e reversibile?
10. **Quale evento ci obbligherà a rivalutare questa scelta?**

Se la decima risposta è:

> vedremo

il TDR non è ancora finito.

### Il TDR non deve diventare un vincolo permanente

Una decisione tecnica non è una promessa identitaria.

Cambiare idea quando cambiano i requisiti è un segnale di maturità.

Il record serve proprio a distinguere:

- cambiamento ragionato;
- tool hopping guidato dalla moda.

### Template compatto

Per lavori piccoli è sufficiente:

```text
TOOLING DECISION RECORD

Decision:
Stage:
Data / scale:
Frequency / freshness:
Consumers:
Risk:
Reproducibility:
Choice:
Alternatives considered:
Why sufficient:
Known limitation:
Owner:
TCO / effort estimate:
Exit condition:
Review date:
```

### Regola operativa

> **Una buona tool choice non dice soltanto cosa useremo. Dice perché è sufficiente, quale complessità stiamo evitando e quali cambiamenti renderebbero la decisione obsoleta.**
