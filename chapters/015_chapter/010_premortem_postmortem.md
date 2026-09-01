## 15.9 Pre-mortem e post-mortem: cercare il fallimento prima, capire l'apprendimento dopo

Le decisioni soffrono di due bias opposti.

**Prima della scelta**

Tendiamo a difendere il piano preferito e a sottopesare ciò che potrebbe farlo fallire.

**Dopo l'esito**

Tendiamo a riscrivere la storia come se ciò che è successo fosse stato più prevedibile di quanto fosse davvero.

Pre-mortem e post-mortem servono a proteggere due momenti diversi del Decision Record.

### Il pre-mortem: assumere che abbiamo già fallito

La tecnica è semplice.

Prima di impegnarsi, il team assume:

> “È passato un anno. Questa decisione è stata un fallimento evidente. Che cosa è successo?”

Poi ogni partecipante genera spiegazioni plausibili.

Gary Klein ha descritto il **project premortem** come tecnica per rendere più facile esprimere dubbi e debolezze che durante la pianificazione possono restare silenziosi.

Fonte: Harvard Business Review, *Performing a Project Premortem*: https://hbr.org/2007/09/performing-a-project-premortem

Il valore non è il pessimismo.

È creare una struttura in cui il dissenso diventa un input legittimo prima che il piano accumuli commitment.

### Caso simulato/composito — aumento prezzo SaaS

Una SaaS vuole aumentare il prezzo del piano Pro del 15%.

Il business case centrale è positivo.

Prima del rollout il team fa un pre-mortem.

> “Tra sei mesi diciamo che il pricing change è stato un errore. Perché?”

Emergono:

- churn enterprise molto più alto del previsto;
- Sales compensa con discounting e il list-price increase non diventa realized price;
- ticket Support crescono e aumentano cost-to-serve;
- competitor usa il nuovo prezzo per displacement campaigns;
- nuovi clienti convertono meno;
- vecchi clienti percepiscono un cambio di valore non accompagnato dal prodotto;
- NRR peggiora anche se ARPA iniziale sale;
- metriche aggregate nascondono forte eterogeneità per tenure e mercato.

Ora ogni failure mode viene trasformato in una parte del Decision Record.

| Failure mode | Leading indicator | Guardrail / mitigation |
|---|---|---|
| churn enterprise | renewal intent / churn cohort | rollout graduale + stop threshold |
| discount leakage | realized vs list price | track discount rate |
| support burden | ticket/account | capacity guardrail |
| new-logo conversion | funnel by segment | separate new/existing policy |
| competitive reaction | win/loss reasons | weekly sales feedback |

Il pre-mortem ha creato **osservabilità della decisione**.

### Pre-mortem ≠ lista infinita di paure

Non tutti i failure mode meritano lo stesso spazio.

Dopo la generazione, classifichiamo:

```text
plausibility
impact
speed of detection
detectability
mitigability
```

Poi selezioniamo quelli che:

- possono cambiare la scelta;
- richiedono guardrail;
- devono essere monitorati;
- suggeriscono un pilot o rollout più reversibile.

### Il pre-mortem deve attaccare anche la measurement plan

Un progetto può “fallire” perché non sappiamo misurarlo.

Domande:

- il KPI principale può migliorare mentre un outcome importante peggiora?
- distinguiamo adoption da impact?
- abbiamo exposure logging?
- il dato matura abbastanza presto?
- possiamo separare policy effect da trend esterno?
- esiste una baseline credibile?

Un pre-mortem utile può quindi scoprire che **la decisione non è ancora valutabile**, non soltanto che l'esecuzione è rischiosa.

### Red team: chi deve cercare di farci cambiare idea?

Per decisioni ad alto commitment può essere utile assegnare esplicitamente un ruolo:

> “Costruisci il caso migliore contro la preferred option.”

Il red team dovrebbe cercare:

- evidenza contraria;
- alternative sottovalutate;
- assunzioni troppo ottimistiche;
- costi esclusi;
- effetti di secondo ordine;
- lock-in;
- correlated downside.

L'obiettivo non è vincere il dibattito.

È ridurre la probabilità che una scelta sopravviva soltanto perché nessuno l'ha attaccata seriamente.

### Il post-mortem: non partire dall'esito

Dopo l'azione, il team non dovrebbe chiedere subito:

> “La decisione era giusta o sbagliata?”

Meglio separare tre domande:

1. **Decision process** — con l'informazione disponibile allora, il processo era buono?
2. **Execution** — abbiamo implementato ciò che avevamo deciso?
3. **Outcome** — che cosa è successo nel mondo?

Questa separazione evita di confondere fortuna, esecuzione e qualità del ragionamento.

### Un template di decision review

```text
What we expected:
central scenario:
plausible range:
key assumptions:
switching thresholds:

What happened:
outcome:
execution deviations:
external changes:

What surprised us:
assumptions wrong:
signals missed:
unknown unknowns:

What worked:
controls:
guardrails:
rollback:

What changes now:
model/forecast:
process:
data collection:
future decision rule:
```

### Non usare il post-mortem per produrre una causa comoda

Un outcome negativo può avere più cause.

Esempio:

```text
new market underperforms
```

Possibili componenti:

- scelta strategica sbagliata;
- execution Sales lenta;
- hiring ritardato;
- competitor shock;
- recessione locale;
- metriche iniziali troppo ottimistiche.

Il post-mortem deve distinguere ciò che il team **avrebbe potuto ragionevolmente conoscere e controllare** da ciò che è emerso dopo.

### Blameless non significa accountability-free

Evitare il blame game non significa evitare responsabilità.

Possiamo dire contemporaneamente:

- l'owner era responsabile del gate;
- il gate non è stato applicato;
- il sistema rendeva facile bypassarlo;
- il processo va corretto.

La domanda utile è:

> **“Quale combinazione di decisione, processo ed execution ha reso questo outcome possibile, e quale controllo avrebbe avuto il miglior rapporto tra prevenzione e costo?”**

### Feed learning nel prossimo Decision Record

L'apprendimento deve cambiare qualcosa di riusabile.

Esempi:

```text
historical project overruns
→ nuovo optimism-bias adjustment

pricing churn più sensibile del previsto
→ nuova prior per future price changes

pilot insufficiente su enterprise
→ nuova minimum exposure rule

supplier switching lento
→ nuovo lead-time assumption
```

Se il post-mortem produce soltanto una presentazione, l'organizzazione non ha realmente imparato.

### Campo del Decision Record

Prima della scelta:

```text
premortem top failures:
leading indicators:
mitigations:
guardrails added:
red-team challenge:
```

Dopo:

```text
review date:
expected vs observed:
decision-process assessment:
execution assessment:
external shocks:
assumptions updated:
reusable learning:
```

> **Il pre-mortem protegge la decisione dall'eccesso di fiducia prima dell'azione. Il post-mortem protegge l'apprendimento dalla storia che costruiamo dopo aver visto l'esito.**
