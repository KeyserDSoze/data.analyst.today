## 9.12 Caso simulato/composito — Northstar Retail: quando la conversione vince e lo ship perde

**Northstar Retail** è una piattaforma e-commerce immaginaria con circa 28 milioni di sessioni mensili in Europa. Il team Checkout vuole preselezionare la consegna più veloce quando sono disponibili più opzioni, convinto che meno scelta visibile riduca frizione e aumenti gli ordini completati.

La richiesta iniziale è familiare: “Mettiamola al 20%, guardiamo conversion per una settimana e, se sale, ship.” L'analista la trasforma in una decisione verificabile: **possiamo rendere default la consegna veloce aumentando il valore netto per utente senza creare un livello inaccettabile di cancellazioni, reclami o costi di supporto?**

Da questa frase discende il design. L'unità di randomizzazione è `stable_user_id`; sono eleggibili gli utenti con almeno due delivery option; dentro il 20% di traffico attivato al test l'allocation è 50/50; il bucketing resta persistente tra sessioni e l'analisi primaria è intent-to-treat sulla popolazione eleggibile randomizzata. In questo modo non escludiamo a posteriori utenti che non arrivano al checkout in modo differenziale.

Anche la scorecard cambia. La primary/OEC non è checkout conversion ma **contribution margin per eligible user a D2**. Conversion, AOV, premium-delivery selection e checkout duration diventano diagnostics. Cancellation D1, refund, delivery complaints, support contacts/order e payment errors sono guardrail. SRM, eligibility rate, exposure/render rate ed event completeness appartengono al piano di health.

Il team decide inoltre prima del test che un peggioramento superiore a `+0,30 pp` sulle cancellazioni D1 blocca lo ship anche con primary positiva. Il traffic plan richiede circa due cicli settimanali; il contract impone comunque 14 giorni di minimum duration e 48 ore di maturity dopo l'ultimo enrollment.

### La prima settimana produce esattamente la tentazione che il contract deve contenere

Dopo sette giorni:

| Metrica | Control | Treatment | Delta |
|---|---:|---:|---:|
| Checkout conversion | 4,91% | 5,18% | +0,27 pp |
| AOV | 73,40 € | 74,10 € | +0,95% |
| Margin/order | 18,60 € | 18,94 € | +1,8% |

Il PM chiede rollout immediato. Il test continua non per formalismo, ma perché la decisione non è ancora leggibile: il fixed horizon non è completo, cancellation e refund non sono maturi, manca il secondo ciclo settimanale e `margin/order` non è la primary definita nel contract.

Prima del final read il team esegue il gate:

```text
SRM: PASS
assignment stability: PASS
exposure rate A/B: compatibile
payment telemetry: PASS
late-event maturity: PASS
```

Se l'SRM avesse fallito, la discussione sul lift sarebbe stata sospesa.

### Quando maturano i costi downstream, la storia cambia

Dopo due settimane e maturity completa la checkout conversion resta positiva, `+0,23 pp`, ma cancellation D1 arriva a `+0,34 pp`, support contacts/order a `+7,6%` e delivery complaints a `+11,8%`. La primary contribution margin/eligible user è positiva, ma **sotto la soglia di ship** stabilita. Inoltre cancellation supera il guardrail di `+0,30 pp`.

La decisione è quindi **NO-SHIP della variante originale**.

Non è corretto dire che “il test è negativo”. Il test ha prodotto informazione più utile: la preselezione riduce frizione, ma una parte degli utenti non percepisce abbastanza chiaramente il sovrapprezzo della delivery veloce.

Un segmento pre-specificato aiuta a localizzare il meccanismo. I returning users mostrano beneficio di conversione con guardrail quasi stabili; i nuovi utenti mostrano lift maggiore ma anche più cancellazioni e reclami. Poiché new vs returning era stato dichiarato prima per una ragione sostantiva, il pattern può guidare **l'iterazione**, non autorizzare automaticamente un rollout selettivo della V1.

### La seconda variante cambia il trattamento, quindi richiede un nuovo test

Northstar ridisegna l'esperienza: delivery veloce preselezionata per returning users, testo prezzo più esplicito per i nuovi, surcharge visivamente prominente e nessun default aggressivo dove il meccanismo appare più fragile.

È un trattamento diverso. Il team apre un nuovo Experiment Contract e una nuova randomizzazione. Dopo maturity, contribution margin/eligible user supera la soglia di materialità, cancellation resta nel margin, support contacts non mostrano regressioni materialmente rilevanti e SRM/health checks passano. La V2 diventa **SHIP CANDIDATE**.

### Ship candidate non significa 100%

Il rollout segue un ramp:

```text
20% -> 50% -> 80% -> 100%
```

A ogni fase il team monitora system health, cancellation/refund, support, latency, segment coverage e payment/delivery partner failures. Le soglie di rollback sono scritte prima dell'espansione.

Microsoft ExP ha documentato lo stesso principio in rollout infrastrutturali: piccoli aumenti di latency backend possono essere amplificati da richieste sequenziali o CORS preflight e diventare regressioni visibili soltanto su metriche più vicine all'esperienza reale; feature flag e scorecard permettono iterazione e rollback prima dell'esposizione completa.[^ms-infra]

### Experiment Contract — Northstar

```text
DECISION
Ship solo se valore netto/eligible user supera la soglia
senza violare cancellation/support guardrails.

RANDOMIZATION
stable user, persistent, ITT.

METRICS
OEC + guardrail + diagnostics + health.

MATERIALITY
Threshold deciso prima del test.

DURATION
2 weekly cycles + 48h maturity.

HEALTH
SRM/exposure/logging pass before effect analysis.

ANALYSIS
Fixed horizon; segment new/returning pre-specified.

RESULT V1
Conversion positiva, guardrail fallisce -> NO-SHIP / redesign.

RESULT V2
Primary sopra threshold, guardrail pass -> SHIP CANDIDATE.

ROLLOUT
Progressive ramp + rollback triggers.
```

Il caso mostra la differenza tra A/B testing come classifica di varianti ed experimentation come sistema decisionale. La V1 non viene “bocciata” perché il lift scompare: viene fermata perché l'effetto locale non soddisfa la funzione di valore e rischio decisa in anticipo. La V2 non viene “promossa” direttamente al 100%: guadagna il diritto di aumentare l'esposizione.

> **Il risultato di un esperimento non è un voto alla feature. È evidenza che autorizza, limita o impedisce il passo successivo.**

[^ms-infra]: Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp
