## 17.9 “L'alert è rosso: cosa è cambiato davvero?”

### Caso simulato/composito: Atlas Streaming

Atlas gestisce una piattaforma video in abbonamento.

Alle 09:12 il monitoring segnala:

**trial-to-paid conversion -17% rispetto al baseline atteso.**

L'alert è classificato `high severity` perché la metrica impatta ricavi futuri.

La reazione naturale è aprire un incident channel e cercare il bug.

Ma un sistema di anomaly detection identifica **deviazione rispetto a un'attesa**. Non identifica automaticamente la natura del fenomeno.

La domanda corretta è:

> **“Abbiamo un problema di dato, definizione, mix, comportamento, sistema o contesto esterno?”**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | intervenire sul sistema, correggere la metrica o non fare nulla |
| Failure cost | outage non rilevato oppure rollback inutile di una feature sana |
| Claim necessario | diagnostico rapido, con escalation causale solo se serve |
| Tempo disponibile | minuti/ore, non settimane |
| Reversibilità | alta per pause/rollback; diversa per partnership e campagne |
| Stop rule | nessuna azione irreversibile finché il fenomeno non è riconciliato con una fonte indipendente |

## 1. Prima domanda: l'anomalia è nel dato o nel mondo?

Il team controlla immediatamente:

- freshness;
- completeness;
- duplicati;
- errori di pipeline;
- cambi schema;
- volume degli eventi;
- sorgente indipendente di billing.

Il numero di eventi `subscription_started` è diminuito.

Anche la fatturazione mostra però un calo coerente.

Quindi non è soltanto telemetry.

Questo supera il primo gate: **il cambiamento del KPI esiste davvero nei sistemi economici**.

## 2. Playbook di diagnosi

Atlas usa una tassonomia operativa:

1. **data anomaly** — pipeline, tracking, duplicate, lateness;
2. **definition anomaly** — la metrica non rappresenta più lo stesso processo;
3. **mix anomaly** — cambia la popolazione;
4. **behavior anomaly** — cambia il comportamento reale;
5. **system anomaly** — bug, performance, payment, release;
6. **external shock** — mercato, festività, competitor, regolazione.

La tassonomia impedisce che “anomalia” diventi sinonimo di “bug”.

## 3. Ipotesi 1: payment failure

Il team verifica:

- authorization rate;
- provider error;
- latency;
- decline code;
- country/provider split.

Nessun segnale anomalo.

L'ipotesi payment perde priorità.

Questo è un esempio di **evidence against**, che deve essere registrato quanto l'evidenza favorevole.

## 4. Ipotesi 2: release

Il team controlla rollout e versioni.

Nessun breakpoint netto coincide con una release.

La conversione cala anche su client non esposti.

L'ipotesi release non è impossibile, ma diventa meno plausibile.

## 5. Ipotesi 3: il mix geografico è cambiato

Il calo è concentrato in tre paesi.

Una nuova partnership ha generato un forte aumento dei trial proprio in quei mercati.

Gli utenti della partnership entrano però con una prova di **30 giorni**, mentre il trial standard dura 7 giorni.

La metrica aziendale è:

> `trial-to-paid entro 14 giorni`.

Quegli utenti vengono quindi classificati come non convertiti quando, per design, non hanno ancora raggiunto il momento di conversione.

## 6. Semantic drift: il KPI è cambiato senza cambiare formula

Questa è una forma particolarmente pericolosa di **semantic drift**.

La query non è cambiata.

La formula non è cambiata.

Il processo business sì.

Quindi il significato decisionale della metrica si è spostato.

L'anomaly detector ha fatto correttamente il proprio lavoro:

> “questa serie non si comporta come prima”.

Ma sarebbe sbagliato tradurre automaticamente il segnale in:

> “la capacità del prodotto di convertire trial in clienti è peggiorata del 17%”.

## 7. Data Readiness Review sotto pressione temporale

In un incidente non possiamo fare un audit di tre settimane.

Serve una versione compatta:

- dato fresco?
- fonte indipendente coerente?
- definizione stabile?
- denominatore stabile?
- popolazione stabile?
- release/evento business recente?
- impatto economico reale già osservabile?

Questa mini-review è sufficiente per evitare molte escalation sbagliate.

## 8. La decisione

Le alternative sono:

### A — Rollback prodotto

Non supportato dall'evidenza.

### B — Bloccare la partnership

Prematuro: la partnership ha cambiato il timing del funnel, non necessariamente il valore economico.

### C — Correggere la metrica e aprire un monitor separato

- activation per cohort e trial type;
- conversione misurata dopo eleggibilità alla conversione;
- expected revenue per trial cohort;
- alert distinti per standard e 30-day trial;
- monitoraggio delle coorti partnership quando maturano.

La scelta è C.

## 9. Decision Record e severity

L'incidente cambia classificazione:

- da `high-severity product incident`;
- a `metric semantics incident` con monitoraggio economico aperto.

Questo non significa che “non è successo niente”.

È successo qualcosa di importante: **il sistema di osservabilità non era più allineato al processo business**.

Anche questo può produrre decisioni sbagliate se non viene corretto.

## 10. Decision Communication Pack

La headline non è:

> “Conversion -17%.”

È:

> **“L'alert non indica al momento un deterioramento del checkout: il nuovo trial da 30 giorni ha cambiato la popolazione e rende non comparabile la metrica `paid entro 14 giorni`. Correggiamo il KPI e manteniamo monitoraggio sulle coorti partnership fino alla maturazione.”**

Il pack operativo contiene:

- cosa è osservato;
- cosa è stato escluso;
- spiegazione semantica;
- impatto noto/non noto;
- decisione;
- next check time;
- owner.

## 11. Outcome review

Dopo 30–45 giorni il team verifica:

- conversione dopo eligibility;
- revenue per trial cohort;
- churn iniziale;
- CAC/payback partnership;
- differenza tra trial standard e partnership.

Solo allora può giudicare se la nuova offerta porta clienti economicamente migliori o peggiori.

## Cosa abbiamo scelto di non fare

Non serve addestrare un nuovo anomaly model per risolvere il primo incidente.

Non serve causal inference per riconoscere una incompatibilità di definizione.

La catena effettiva è:

**alert → Data Readiness Review compatta → EDA Evidence Map → Decision Record operativo → Decision Communication Pack → outcome review**

> **Anomaly detection riduce il tempo necessario per accorgersi che qualcosa è cambiato. L'analisi riduce il rischio di agire prima di capire che cosa sia cambiato davvero.**
