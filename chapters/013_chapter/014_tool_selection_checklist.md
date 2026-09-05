## 13.13 Tooling Decision Record: scegliere, motivare e sapere quando cambiare

Una checklist aiuta a non dimenticare domande. Un **Tooling Decision Record (TDR)** registra invece la scelta in modo che, tra sei mesi, possiamo capire **perché era sensata e se le condizioni che la giustificavano esistono ancora**.

Non deve diventare burocrazia. Per un'analisi semplice può stare in mezza pagina; per un prodotto critico può essere più dettagliato. Il valore nasce da quattro obblighi: partire dal problema, confrontare alternative reali, dichiarare i limiti della scelta e definire un'**exit condition**.

La prima alternativa da ammettere è spesso “non costruire”: risposta manuale una tantum, query ad hoc, asset già esistente, miglioramento del processo corrente o nessuna automazione finché il valore atteso non è sufficiente. Se confrontiamo soltanto strumenti nuovi, la conclusione è già incorporata nella domanda.

### 1. Decision context

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

`Decision deadline` e `solution lifetime` non sono la stessa cosa. Potremmo aver bisogno di una risposta domani e di un processo stabile per tre anni; non è obbligatorio che la prima implementazione soddisfi già tutti gli obblighi del terzo anno.

### 2. Problem shape

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

Questa sezione impedisce termini vaghi come “big data” o “real time” senza ordini di grandezza e senza una decisione che li richieda.

### 3. Risk and control

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

Due problemi con la stessa scala possono richiedere soluzioni radicalmente diverse se uno produce una EDA esplorativa e l'altro alimenta un processo operativo.

### 4. People and ownership

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

Questa parte evita che il sistema esista soltanto finché esiste la persona che lo ha costruito.

### 5. Candidate comparison

Compiliamo soltanto le alternative realmente plausibili, includendo sempre una soluzione più semplice quando esiste.

| Candidate | Vantaggi | Limiti | TCO / effort | Rischio | Reversibilità |
|---|---|---|---|---|---|
| Manual / one-off | | | | | |
| Existing process | | | | | |
| Spreadsheet | | | | | |
| SQL/shared model | | | | | |
| Python/R/notebook | | | | | |
| BI | | | | | |
| Low-code | | | | | |
| Managed/shared platform | | | | | |

Non serve riempire righe irrilevanti. Serve evitare il confronto tra una proposta reale e alternative caricaturali.

### 6. Chosen design

```text
Chosen tool / combination:
Where each responsibility lives:
Why it is sufficient now:
Why a simpler option is insufficient:
Why a more complex option is not justified yet:
Known limitations:
Controls required:
```

Le due domande centrali sono speculari: **perché non basta una soluzione più semplice?** e **perché non serve ancora quella più sofisticata?**. Insieme proteggono sia dall'underengineering sia dall'acquisto prematuro di complessità.

### 7. Exit condition

Questa è la parte più importante del TDR.

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

L'exit condition trasforma “Excel o SQL?” in una domanda più utile: **in quali condizioni Excel smette di essere sufficiente per questa responsabilità?**

La stessa domanda business può quindi generare TDR differenti. Per una review una tantum su 2.000 account, `SQL export + spreadsheet` può essere proporzionato. Con **300 milioni di eventi** e review settimanale, un modello SQL nel warehouse riduce lavoro ripetuto. Con **800 Customer Success manager** e workflow operativo, la stessa logica può richiedere un modello certificato e serving BI/CRM. La domanda è la stessa; il sistema di responsabilità è cambiato.

### Decision gate

Prima di approvare una scelta un reviewer dovrebbe poter rispondere a queste domande:

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

Se la decima risposta è “vedremo”, il record non è ancora completo.

### Template compatto

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

Una decisione tecnica non è una promessa identitaria. Cambiare idea quando cambiano i requisiti è maturità; cambiare tool perché è cambiata la moda è un'altra cosa. Il TDR serve a distinguere i due casi.

> **Una buona tool choice non dice soltanto cosa useremo. Dice perché è sufficiente, quale complessità stiamo evitando e quali cambiamenti renderebbero la decisione obsoleta.**
