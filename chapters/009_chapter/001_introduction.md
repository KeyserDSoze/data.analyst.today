# Capitolo 9 — Experimentation e A/B testing nel mondo reale

> **Un esperimento non è affidabile perché è randomizzato. È affidabile quando assignment, exposure, telemetria, metriche, analisi e decisione restano coerenti dall'inizio alla fine.**

Il Capitolo 8 ha spiegato perché la randomizzazione può costruire un controfattuale credibile. Qui il problema diventa operativo: **come evitare di distruggere quella credibilità mentre il trattamento entra in produzione, gli utenti vengono esposti, gli eventi vengono raccolti e il team decide se fare ship**.

Un esperimento causalmente valido sulla lavagna può rompersi in molti punti. L'identità usata per il bucket può non essere stabile; un utente può vedere entrambe le varianti; assignment ed exposure possono divergere; una variante può generare crash o redirect che fanno sparire proprio parte degli utenti trattati; una primary metric può cambiare definizione a test iniziato; il sample size può essere raggiunto prima che maturino refund o chargeback; il team può fermarsi alla prima oscillazione favorevole; un marketplace può essere randomizzato a livello individuale anche se seller, inventory e prezzi reagiscono globalmente. Nessuno di questi è un dettaglio separato dalla statistica. Ognuno modifica il confronto che crediamo di stare osservando.

Per questo un A/B test reale va letto come una **catena di affidabilità**:

```text
DECISIONE
    ↓
IPOTESI / TREATMENT
    ↓
ELIGIBILITY
    ↓
RANDOMIZATION UNIT + ASSIGNMENT
    ↓
EXPOSURE
    ↓
TELEMETRIA
    ↓
METRIC CONTRACT
    ↓
HEALTH GATE
    ↓
INFERENCE PLAN
    ↓
SHIP / NO-SHIP / ITERATE
    ↓
ROLLOUT + MONITORING
```

Una rottura a monte può rendere irrilevante la sofisticazione a valle. Un confidence interval calcolato perfettamente non salva un test in cui la variante B ha perso selettivamente gli utenti più coinvolti durante il logging.

## 9.0 Dalla randomizzazione alla decisione

Nel Capitolo 5 abbiamo già costruito il linguaggio per effect size, confidence interval, Type I e Type II error, power, sample size e multiple testing. Qui non li ripeteremo come teoria statistica generale: li useremo come **vincoli di una decisione sperimentale**. La domanda non sarà soltanto “il p-value è piccolo?”, ma “quale effetto sarebbe abbastanza grande da cambiare la policy, con quale traffico possiamo distinguerlo, quando il risultato è maturo e quali peggioramenti renderebbero comunque inaccettabile lo ship?”.

Il Capitolo 8 ha invece chiarito perché la randomizzazione può identificare causalmente un effetto. Il punto di questo capitolo è verificare se la produzione ha preservato quel design. Per farlo dovremo distinguere unità di randomizzazione, unità di exposure e unità di analisi; assignment da treatment ricevuto; popolazione prevista da popolazione realmente osservata; metriche di business da metriche di experiment health.

### Caso simulato/composito — QuickPay

Una grande piattaforma e-commerce europea vuole testare **QuickPay**, un pulsante che salta alcuni passaggi del checkout. La conversione utente → ordine è 3,92%, il traffico mensile eleggibile è circa 3,1 milioni di utenti, il contribution margin medio per ordine è 17,40 €, il chargeback rate è 0,42% e il cancellation rate entro 24 ore è 2,8%.

La proposta iniziale del Product Manager è semplice: “Facciamo 50/50 per una settimana. Se la conversione sale, ship.” Il problema è che quella frase contiene già decisioni non dichiarate. Se randomizziamo per sessione, lo stesso utente può vedere A su web e B su app. Se “assegnato a B” non significa “QuickPay realmente renderizzato”, l'analisi per exposed users può selezionare una popolazione diversa. Se la primary è conversione ma la feature aumenta chargeback o cancellazioni, possiamo vincere localmente e perdere economicamente. Se il traffico è enorme, il sample size può arrivare in pochi giorni mentre gli outcome downstream non sono ancora maturi. E se il risultato è positivo al 20% di exposure, non sappiamo ancora se sistemi di pagamento, supporto e fraud review reggeranno il 100%.

Queste domande **sono il disegno sperimentale**. Non arrivano dopo il test.

Microsoft Experimentation Platform tratta proprio la qualità sperimentale come un prerequisito della lettura dell'effetto: l'SRM, la completezza dei dati e gli altri controlli di trustworthiness vengono usati per stabilire se il confronto è interpretabile prima di usarlo per una decisione.[^ms-data-quality]

L'ordine professionale diventa quindi:

```text
experiment health
    ↓
data validity
    ↓
effect estimate + uncertainty
    ↓
decision
    ↓
rollout governed by guardrails
```

## Il deliverable del capitolo: Experiment Contract

Il capitolo convergerà su un **Experiment Contract** scritto prima di vedere il risultato. Non serve a trasformare l'esperimento in burocrazia; serve a rendere verificabile ciò che avevamo deciso quando non sapevamo ancora quale variante avrebbe vinto.

```text
DECISIONE
Quale scelta deve informare il test?

HYPOTHESIS / TREATMENT
Che cosa cambia realmente tra controllo e trattamento?

POPOLAZIONE / ELIGIBILITY
Chi può entrare nel confronto e quando?

RANDOMIZATION / EXPOSURE / ANALYSIS
Qual è l'unità? Come resta stabile l'assegnazione? Che cosa significa essere trattati?

METRIC CONTRACT
Primary/OEC, guardrail, diagnostics e data-quality metrics.

MATERIALITY / FEASIBILITY
Quale effetto cambia la decisione e il traffico può distinguerlo?

DURATION / MATURITY
Quali cicli, learning effect e outcome ritardati devono maturare?

HEALTH GATE
SRM, identity, exposure, telemetry, population e metric integrity.

INTERFERENCE
Il trattamento di un'unità può cambiare il mondo del controllo?

INFERENCE PLAN
Fixed horizon o sequential? Quali confronti sono confermativi?

DECISION RULE
SHIP / NO-SHIP / REDESIGN / INCONCLUSIVE.

ROLLOUT
Ramp, holdout, rollback trigger e monitoring post-ship.
```

Seguiremo tre movimenti. Prima costruiremo il confronto e verificheremo che assignment, exposure e metriche rappresentino la decisione. Poi stabiliremo **quando e come** il test può essere letto, con quale sensibilità e quale disciplina inferenziale. Infine vedremo come un risultato valido diventa una ship candidate e perché il rollout rimane una fase di misurazione e risk management.

> **La trustworthy experimentation non consiste nel calcolare correttamente una differenza. Consiste nel preservare la credibilità del confronto dal primo bucket fino alla decisione e oltre.**

[^ms-data-quality]: Microsoft Research, *Data Quality: Fundamental Building Blocks for Trustworthy A/B testing Analysis*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis
