## 18.6 Automazione e CI/CD: incorporare il controllo invece di automatizzare la speranza

Quando un'analisi diventa ricorrente, la domanda cambia da:

> “Funziona oggi?”

a:

> **“Come facciamo a cambiare questo prodotto cento volte senza perdere il diritto di fidarci del risultato?”**

È qui che analytics incontra pratiche di software engineering:

- version control;
- review;
- test automatici;
- ambienti separati;
- release;
- rollback;
- observability.

Il punto non è imitare DevOps per moda.

È riconoscere che una modifica SQL o semantica può produrre un impatto business altrettanto reale di un bug applicativo.

## Automatizzare un processo fragile lo rende soltanto più veloce

Consideriamo un processo manuale:

1. export;
2. mapping;
3. formula;
4. controllo con Finance;
5. pubblicazione.

Se automatizziamo i primi tre punti e rimuoviamo il quarto senza capire perché esistesse, abbiamo aumentato la velocità riducendo il controllo.

DORA sottolinea un principio simile per la continuous delivery: ripetere più spesso il vecchio processo senza redesign di processo, architettura e capability può aumentare failure rate e burnout.

Fonte: https://dora.dev/capabilities/continuous-delivery/

Per analytics la sequenza corretta è spesso:

```text
understand recurring work
→ remove unnecessary steps
→ make semantics explicit
→ define tests and owner
→ automate
→ observe
→ improve
```

Non:

```text
manual process
→ schedule script
→ hope
```

## Caso simulato/composito: il KPI che cambia senza rompersi

Una società SaaS usa `active_customer` nel denominatore di una executive retention metric.

Un analytics engineer modifica una condizione per escludere account in grace period.

La query:

- compila;
- gira;
- non produce null;
- mantiene schema e tipo.

Il KPI passa da `108,4%` a `104,9%`.

Il sistema tecnico è sano.

Il cambiamento è semanticamente materiale.

Una CI che verifica soltanto codice e schema non protegge la decisione.

## La pipeline di release analitica

Per un prodotto T2 possiamo immaginare:

```text
branch / proposed change
→ static checks
→ structural tests
→ unit / logic tests
→ data contract checks
→ reconciliation
→ semantic diff
→ impact analysis
→ owner approval if needed
→ pre-production / shadow run
→ deploy
→ post-deploy verification
→ certification
```

Non ogni asset necessita tutti questi gate.

Il criticality tier decide la profondità.

## Semantic diff: che cosa cambia nei numeri?

Uno dei controlli più potenti prima della release è confrontare vecchio e nuovo output.

Non basta chiedere:

> “I test passano?”

Chiediamo:

- quali righe cambiano?
- quali metriche cambiano?
- di quanto?
- in quali segmenti?
- la variazione è attesa?
- cambia una soglia decisionale?
- il passato viene riscritto?

Esempio di release summary:

| Metrica | Old | New | Delta | Atteso? |
|---|---:|---:|---:|---|
| Active customers | 184.320 | 176.940 | -4,0% | sì |
| NRR | 108,4% | 104,9% | -3,5 pp | sì, effetto denominatore |
| Churn rate | 2,8% | 2,9% | +0,1 pp | da investigare |

Il semantic diff non decide da solo se la modifica sia corretta.

Rende visibile dove serve giudizio.

## Dev, test e prod: separare esperimento da promessa

Un asset esplorativo deve poter cambiare rapidamente.

Un asset certificato non dovrebbe essere modificato direttamente in produzione.

La separazione può essere tecnica o logica, ma il principio è:

### Development

Libertà di costruire e rompere.

### Validation / test

Controllo su dati rappresentativi, contract e metric diff.

### Production

Solo versioni che hanno superato i gate richiesti dal tier.

Microsoft descrive una soluzione analytics considerata **essential** come distinta tra ambiente di produzione e sviluppo/test, con change e release management più controllati proprio per l'impatto dei cambiamenti.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

## Shadow run e parallel run

Per una breaking change, una strategia utile è eseguire vecchio e nuovo prodotto in parallelo.

Serve per:

- quantificare delta;
- osservare casi limite;
- aggiornare threshold;
- verificare consumer;
- preparare rollback.

Esempio:

`revenue_v1` e `revenue_v2` vengono calcolate per due closing cycle prima della migrazione.

Non è duplicazione permanente.

È una finestra di osservabilità del cambiamento.

## Deployment progressivo

Anche un prodotto dati può essere rilasciato progressivamente.

Possibili strategie:

- nuova semantic model a un gruppo pilota;
- new metric version visibile solo a Finance/Analytics;
- dual-read per un subset di consumer;
- API versioned;
- canary su una regione;
- feature flag per un report.

Più il blast radius è alto, più il rollout progressivo può avere valore.

## Rollback: che cosa significa davvero nei dati?

Nel software, rollback può significare ripristinare una versione.

Nel dato può essere più complesso.

Se una trasformazione errata ha già scritto output o propagato snapshot, servono decisioni su:

- code rollback;
- data rollback;
- backfill;
- cache invalidation;
- consumer notification;
- report già esportati;
- decisioni già prese.

Per questo l'Operating Contract deve distinguere:

### rollbackable code

Possiamo tornare alla logica precedente.

### replayable data

Possiamo ricostruire output corretti dalle sorgenti.

### non-reversible consumption

Una decisione o comunicazione può essere già avvenuta.

Il recovery tecnico non annulla automaticamente l'impatto decisionale.

## Release gate per criticality

### T0

- version control consigliato;
- nessun deployment formale.

### T1

- review;
- test base;
- scheduled automation;
- owner.

### T2

- CI automatica;
- semantic diff;
- reconciliation;
- change classification;
- rollback/fallback;
- post-deploy verification.

### T3

- segregation più forte;
- approval/audit appropriati;
- UAT o independent verification quando necessario;
- release window;
- rollback/recovery testato;
- change record.

La disciplina cresce con il failure cost.

## Configuration is code — quando la configurazione cambia il significato

Molti incidenti non nascono dal SQL.

Nascono da:

- mapping territoriale;
- lista di account esclusi;
- threshold;
- currency rate source;
- feature flag;
- calendar;
- business-day definition.

Se una configurazione può cambiare un KPI, deve avere:

- owner;
- versioning;
- review proporzionata;
- traceability.

Un file CSV manuale non è “solo configurazione” se decide milioni di euro di reporting.

## CI non è sufficiente senza CD operativa

Possiamo avere una pipeline di test eccellente e un deployment manuale fragile.

Oppure deployment automatico perfetto che pubblica output senza controllare il consumer impact.

Una delivery chain affidabile unisce:

- test prima;
- controllo durante;
- osservazione dopo.

Il post-deploy check deve confermare:

- dati freschi;
- metriche plausibili;
- reconciliation;
- consumer surface disponibile;
- nessun SLO in degradazione.

## Release telemetry

Un team può monitorare:

- deployment frequency;
- lead time change → production;
- percentuale change con rollback/hotfix;
- incident causati da release;
- semantic breaking change;
- tempo di certification post-release;
- percentuale deployment progressivi;
- manual step/toil residuo.

La velocità non è un obiettivo isolato.

È utile se la reliability non viene sacrificata.

## La regola

> **Automazione non significa eliminare il controllo umano o tecnico. Significa spostare i controlli ripetibili dal ricordo delle persone alla pipeline, lasciando al giudizio umano i cambiamenti di significato e rischio che non possono essere ridotti a una regola.**
