## 15.9 Pre-mortem e post-mortem: proteggere la scelta prima e l'apprendimento dopo

Le decisioni soffrono di due bias opposti. Prima della scelta tendiamo a difendere il piano preferito e a sottopesare ciò che potrebbe farlo fallire. Dopo l'esito tendiamo a riscrivere la storia come se ciò che è successo fosse stato più prevedibile di quanto fosse davvero.

Pre-mortem e post-mortem proteggono due momenti diversi dello stesso Decision Record.

### Prima dell'azione: rendere legittimo il dissenso

Nel pre-mortem il team assume che la decisione sia già fallita e chiede:

> **È passato un anno. Questa scelta è stata un fallimento evidente. Che cosa è successo?**

Gary Klein ha descritto il *project premortem* proprio come un modo per rendere più facile esprimere riserve e debolezze che durante la pianificazione possono restare silenziose.[^klein-premortem] Il suo valore non è il pessimismo. È ridurre il costo sociale del dire “questa parte del piano non mi convince” prima che il commitment renda più difficile cambiare rotta.

Consideriamo un SaaS che vuole aumentare il prezzo del piano Pro del 15%. Il business case centrale è positivo. Nel pre-mortem emergono però failure mode diversi: churn enterprise molto più alto del previsto, Sales che compensa con discounting, ticket Support in crescita, competitor che sfrutta il price change, minore new-logo conversion, NRR peggiore anche con ARPA iniziale più alto ed eterogeneità forte per tenure e mercato.

Queste non restano paure generiche. Diventano osservabilità:

| Failure mode | Leading indicator | Guardrail / mitigation |
|---|---|---|
| churn enterprise | renewal intent / churn cohort | rollout graduale + stop threshold |
| discount leakage | realized vs list price | track discount rate |
| support burden | ticket/account | capacity guardrail |
| new-logo conversion | funnel by segment | separate new/existing policy |
| competitive reaction | win/loss reasons | weekly sales feedback |

Il pre-mortem ha quindi modificato il learning contract **prima** del rollout.

Non tutti i failure mode meritano lo stesso spazio. Dopo la generazione li ordiniamo per plausibilità, impatto, velocità di rilevazione, detectability e mitigability. Ci interessano soprattutto quelli che possono cambiare la scelta, richiedere un guardrail, giustificare uno staged rollout o suggerire un dato che oggi non stiamo raccogliendo.

### Attaccare anche il measurement plan

Un progetto può fallire perché non sappiamo misurarlo, non soltanto perché l'esecuzione è sbagliata. Il pre-mortem dovrebbe chiedere se il KPI principale può migliorare mentre un outcome importante peggiora, se distinguiamo adoption da impact, se abbiamo exposure logging, se la baseline è credibile e se i dati maturano abbastanza presto.

Per decisioni ad alto commitment può essere utile anche un red team con un compito esplicito: costruire il caso migliore contro l'opzione preferita, cercando evidenza contraria, alternative sottovalutate, costi esclusi, lock-in, effetti di secondo ordine e downside correlato. Il suo obiettivo non è vincere il dibattito, ma verificare se la recommendation sopravvive a un attacco serio.

### Dopo l'azione: separare decision process, execution e outcome

Nel post-mortem la prima domanda non dovrebbe essere “la decisione era giusta o sbagliata?”. È più utile separare:

1. **Decision process** — con l'informazione disponibile allora, il ragionamento era buono?
2. **Execution** — abbiamo implementato ciò che avevamo deciso?
3. **Outcome** — che cosa è successo nel mondo?

Questa separazione impedisce di attribuire automaticamente un risultato negativo a una scelta ex ante debole oppure un risultato positivo a un processo eccellente.

Una decision review può usare:

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

Il post-mortem non deve produrre una nuova causa comoda. Se un nuovo mercato underperformer, le componenti possono includere scelta strategica, execution Sales lenta, hiring ritardato, competitor shock, recessione locale o ipotesi iniziali troppo ottimistiche. Dobbiamo distinguere ciò che era ragionevolmente conoscibile e controllabile da ciò che è emerso soltanto dopo.

### Blameless non significa accountability-free

Possiamo dire contemporaneamente che un owner era responsabile di un gate, che quel gate non è stato applicato, che il sistema rendeva facile bypassarlo e che il processo deve essere modificato. La domanda utile è:

> **Quale combinazione di decisione, processo ed execution ha reso possibile l'outcome, e quale controllo avrebbe avuto il miglior rapporto tra prevenzione e costo?**

L'apprendimento deve poi cambiare qualcosa di riusabile:

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

Nel Decision Record aggiungiamo quindi, prima della scelta:

```text
premortem top failures:
leading indicators:
mitigations:
guardrails added:
red-team challenge:
```

E dopo:

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

[^klein-premortem]: Gary Klein, *Performing a Project Premortem*, Harvard Business Review, September 2007, https://hbr.org/2007/09/performing-a-project-premortem
