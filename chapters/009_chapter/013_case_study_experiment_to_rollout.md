## 9.12 Caso simulato/composito — Dal test al rollout: quando la conversione vince e lo ship perde

**Northstar Retail** è una piattaforma e-commerce immaginaria con circa 28 milioni di sessioni mensili in Europa.

Il team Checkout propone una modifica semplice:

> preselezionare la consegna più veloce quando disponibile.

L'ipotesi è che meno scelta visibile riduca frizione e aumenti gli ordini completati.

La richiesta iniziale è:

> “Mettiamola al 20%, guardiamo conversion per una settimana e, se sale, ship.”

L'analista trasforma invece la richiesta in un **Experiment Contract**.

### 1. Decisione

La decisione non è:

> “La conversione sale?”

È:

> **“Possiamo rendere default la consegna veloce aumentando il valore netto per utente senza creare un livello inaccettabile di cancellazioni, reclami o costi di supporto?”**

### 2. Popolazione e randomizzazione

- unità: `stable_user_id`;
- eligibility: utenti con almeno due delivery option disponibili;
- allocation: 50/50 dentro il 20% di traffico attivato al test;
- persistent bucketing tra sessioni;
- analisi primaria intent-to-treat sulla popolazione eleggibile randomizzata.

Questo evita che utenti che non arrivano al checkout vengano esclusi in modo differenziale dopo l'assignment.

### 3. Metric Contract

**Primary/OEC**

- contribution margin per eligible user a D2.

**Diagnostic**

- checkout conversion;
- AOV;
- premium-delivery selection;
- checkout duration.

**Guardrail**

- cancellation D1;
- refund;
- delivery complaints;
- support contacts/order;
- payment errors.

**Data-quality**

- SRM;
- eligibility rate;
- exposure/render rate;
- event completeness.

Il team decide prima che un peggioramento superiore a `+0,30 pp` sulle cancellazioni D1 blocchi lo ship anche con primary positiva.

### 4. MDE e durata

Il team stabilisce che un beneficio inferiore alla soglia economica concordata non compensa:

- sviluppo;
- support load;
- rischio reputazionale;
- complessità del rollout.

Il traffic plan richiede circa due cicli settimanali e il team impone comunque:

- minimum duration: 14 giorni;
- outcome maturity: 48 ore dopo l'ultimo enrollment;
- final read dopo maturazione completa.

### 5. Giorni 1–7: il risultato che invita al peeking

| Metrica | Control | Treatment | Delta |
|---|---:|---:|---:|
| Checkout conversion | 4,91% | 5,18% | +0,27 pp |
| AOV | 73,40 € | 74,10 € | +0,95% |
| Margin/order | 18,60 € | 18,94 € | +1,8% |

Il PM chiede rollout immediato.

Il test continua perché:

- il fixed-horizon contract non è completo;
- cancellation/refund non sono maturi;
- il test non ha coperto due settimane;
- la decision metric è margin **per eligible user**, non margin/order isolato.

### 6. Experiment health

Prima dell'analisi finale:

```text
SRM: PASS
assignment stability: PASS
exposure rate A/B: compatibile
payment telemetry: PASS
late-event maturity: PASS
```

Questa sezione è breve ma decisiva.

Se SRM avesse fallito, il meeting sul lift sarebbe stato sospeso.

### 7. Giorni 8–14: i costi downstream maturano

Dopo due settimane e maturity:

- checkout conversion: `+0,23 pp`;
- cancellation D1: `+0,34 pp`;
- support contacts/order: `+7,6%`;
- delivery complaint: `+11,8%`;
- primary contribution margin/eligible user: positivo, ma sotto la soglia di ship stabilita.

Il guardrail cancellation supera inoltre il limite predefinito.

**Decisione: NO-SHIP della variante originale.**

Non perché “il test è negativo”.

Il test ha imparato qualcosa di più preciso:

> la preselezione riduce frizione, ma parte degli utenti non percepisce abbastanza chiaramente il sovrapprezzo.

### 8. Segmento pre-specificato: new vs returning

Il team aveva dichiarato prima del test che nuovi e returning users potevano capire diversamente il default.

Il pattern diagnostico è:

- returning: beneficio di conversione con guardrail quasi stabili;
- nuovi: lift maggiore, ma più cancellazioni e reclami.

Poiché il segmento era pre-specificato per una ragione di meccanismo, può guidare **l'iterazione successiva**.

Non autorizza automaticamente un rollout selettivo senza un nuovo test coerente con la policy modificata.

### 9. Iterazione 2

Nuovo trattamento:

- returning users: delivery veloce preselezionata;
- new users: testo prezzo più esplicito e nessun default aggressivo;
- surcharge reso visivamente prominente.

Nuovo Experiment Contract, nuova randomizzazione.

Risultato dopo maturity:

- contribution margin/eligible user: sopra la soglia di materialità;
- cancellation guardrail: dentro il margin;
- support contacts: nessuna regressione materialmente rilevante;
- SRM e health checks: PASS.

Ora la variante diventa **ship candidate**.

### 10. Ship non significa 100%

Il rollout viene pianificato:

```text
20% -> 50% -> 80% -> 100%
```

A ogni fase:

- system health;
- cancellation/refund;
- support;
- latency;
- segment coverage;
- payment/delivery partner failures.

Esistono rollback threshold scritti prima del ramp.

### 11. Caso reale documentato — Microsoft testa anche modifiche infrastrutturali

Microsoft Experimentation Platform ha documentato l'uso di A/B test per rollout di cambi infrastrutturali. In una fase, metriche frontend mostrarono degradazioni severe dovute a piccoli aumenti di latenza backend amplificati da richieste sequenziali e CORS preflight; il team iterò sul design e ritestò prima di procedere. In altre iterazioni, feature flag e scorecard permisero rollback rapidi e scoperta di problemi di telemetria e chiamate ridondanti.[^ms-infra]

La lezione è direttamente trasferibile:

> **un test serve non soltanto a dare un voto a una variante, ma a scoprire come il cambiamento interagisce con il sistema prima di esporlo completamente.**

### 12. Experiment Contract finale

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

### La lezione

Un team inesperto avrebbe detto:

> “V1 converte di più, ship.”

Un team sperimentale maturo dice:

> **“Il confronto è sano, la variante aumenta il comportamento locale ma fallisce una condizione di qualità; iteriamo il trattamento, rieseguiamo il test e solo allora passiamo a un rollout governato.”**

Questa è la differenza tra A/B testing come statistica e experimentation come sistema decisionale.

[^ms-infra]: Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp
