# Source & factual audit — data.analyst.today

Ultimo aggiornamento: 2 settembre 2026.

Questo file traccia il **source/factual audit globale** della release editoriale. Markdown resta la source of truth; le correzioni ai capitoli vanno effettuate solo quando una fonte non è raggiungibile, è meno autorevole di un'alternativa disponibile, non supporta il claim, oppure il wording eccede il livello di evidenza.

## Criteri

Per ogni riferimento verificare:

1. **Raggiungibilità** — URL attivo e destinazione corretta.
2. **Autorità** — preferenza per fonte primaria, standard, governo, documentazione ufficiale o letteratura accademica riconosciuta.
3. **Claim support** — la fonte sostiene davvero la proposizione presente nel manoscritto.
4. **Claim level** — associazione, previsione, esposizione, causalità e outcome non devono essere confusi.
5. **Caso reale/composito** — un caso pubblico deve essere documentato; un caso simulato/composito deve essere dichiarato come tale.
6. **Freshness** — data/versione adeguata quando il claim è time-sensitive.
7. **Canonical URL** — niente tracking parameter o redirect evitabili.

## Stati

- `VERIFIED` — fonte raggiungibile, autorevole e claim proporzionato.
- `WORDING` — fonte valida ma wording da correggere o restringere.
- `REPLACE` — preferibile una fonte primaria/canonica diversa.
- `BROKEN` — URL non raggiungibile o destinazione errata.
- `REVIEW` — verifica incompleta.

## Audit log

| Area | Fonte | Occorrenze principali | Esito | Note |
|---|---|---|---|---|
| Cap. 19 — task exposure / lavoro | ILO, *Generative AI and jobs: A 2025 update* | `019/001`, `019/002`, `019/011`, `019/013` | `VERIFIED` | La fonte ILO del 20 maggio 2025 afferma che circa un lavoratore su quattro è in un'occupazione con qualche grado di esposizione alla GenAI e che, per la necessità persistente di input umano, la trasformazione dei lavori è più probabile della completa ridondanza. Il wording del libro distingue correttamente esposizione da perdita effettiva del posto di lavoro. URL canonico: `https://www.ilo.org/publications/generative-ai-and-jobs-2025-update`. |
| Cap. 19 — skill trend | World Economic Forum, *Future of Jobs Report 2025* | `019/001`, `019/006`, `019/008`, `019/011`, `019/013` | `VERIFIED` | Il digest WEF indica analytical thinking come core skill più richiesta dagli employer nel 2025 e AI/big data come skill a crescita più rapida. I claim nel capitolo restano descrittivi e non vengono trasformati in previsione deterministica sui job title futuri. URL canonico: `https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/`. |
| Cap. 19 — agentic work | Microsoft, *2026 Work Trend Index* | `019/001`, `019/003`, `019/011`, `019/013` | `VERIFIED` | Fonte Microsoft pubblicata il 5 maggio 2026. Supporta il framing secondo cui AI/agenti possono assorbire più execution mentre il lavoro umano si sposta verso direzione, decisione e ownership degli outcome. Il manoscritto include correttamente la cautela che si tratta di ricerca Microsoft sul proprio ecosistema e non di una legge generale del mercato del lavoro. URL canonico: `https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization`. |
| Cap. 19 — critical thinking / deskilling | Microsoft Research, CHI 2025, *The Impact of Generative AI on Critical Thinking...* | `019/010` | `VERIFIED` | Studio su 319 knowledge worker e 936 esempi auto-riferiti. Supporta l'associazione tra maggiore fiducia nella GenAI e minore critical-thinking enactment/effort e lo spostamento verso verification, response integration e task stewardship. Il testo dichiara esplicitamente che è una survey/self-report e non prova causalmente il deskilling: claim level corretto. URL canonico: `https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/`. |
| Cap. 8 — DiD / matching / RDD | World Bank + Inter-American Development Bank, *Impact Evaluation in Practice* | `008/009`, `008/010`, `008/011` | `VERIFIED` | La fonte primaria istituzionale contiene capitoli dedicati a Difference-in-Differences, Matching e Regression Discontinuity Design. Supporta il ruolo del controfattuale, le assunzioni forti dei metodi quasi-sperimentali e la comparabilità locale per RDD. Il manoscritto calibra correttamente i claim e non presenta pre-trend, matching o cutoff come garanzia automatica di causalità. URL canonico mantenuto: `https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice`. |
| Cap. 8 — Instrumental Variables / LATE | Nobel Prize 2021, press release + scientific background | `008/012` | `VERIFIED` | La fonte Nobel attribuisce ad Angrist e Imbens i contributi metodologici all'analisi delle relazioni causali con natural experiments; il background scientifico esplicita LATE, compliers e monotonicity. Il claim del libro è coerente e limita l'interpretazione alla popolazione influenzata dallo strumento. URL canonico: `https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/`. |
| Cap. 9 — experiment health / SRM | Microsoft Research, *Data Quality: Fundamental Building Blocks for Trustworthy A/B testing Analysis* | `009/001`, `009/004` | `VERIFIED` | La fonte definisce SRM come mismatch tra allocation osservata e configurata e afferma che analisi con SRM sono generalmente considerate non affidabili e non dovrebbero guidare decisioni. Il vecchio path Microsoft `.../research/group/experimentation-platform-exp/articles/...` redirigeva al nuovo percorso canonico; i riferimenti nel manoscritto sono stati aggiornati. URL canonico: `https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/`. |
| Cap. 9 — caso MSN / SRM | Microsoft Research, *Diagnosing Sample Ratio Mismatch in A/B Testing* | `009/004` | `VERIFIED` | La fonte documenta il caso MSN del carousel: la variante con più contenuto appariva inizialmente negativa, falliva SRM, e l'indagine mostrò che il maggiore engagement confondeva il bot detector facendo filtrare utenti della variante B; risolto il problema, il risultato si ribaltò. Il caso reale nel libro è fedele alla fonte. URL canonico: `https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/`. |
| Cap. 9 — metriche / monitoring / stop operativo | Microsoft Research, *Patterns of Trustworthy Experimentation: During-Experiment Stage* | `009/003`, `009/007` | `VERIFIED` | La fonte supporta il monitoraggio durante l'esperimento, una tassonomia di metriche che include OEC/local/guardrail e l'intervento su regressioni importanti. I vecchi URL con path `group/.../articles` sono stati sostituiti con il percorso canonico corrente. URL canonico: `https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/`. |
| Cap. 9 — interference / concurrent experiments | Microsoft Research, *A/B Interactions: A Call to Relax* | `009/005` | `VERIFIED` | La fonte documenta la pratica Microsoft di eseguire molti test concorrenti e mostra che le interazioni osservate nel campione studiato erano rare, senza affermare che siano impossibili. Il manoscritto mantiene correttamente il claim prudente: non isolare automaticamente ogni test, ma investigare le interazioni materialmente plausibili. URL canonicalizzato a `https://www.microsoft.com/en-us/research/articles/a-b-interactions-a-call-to-relax/`. |
| Cap. 9 — CUPED / variance reduction | Microsoft Research, *Deep Dive Into Variance Reduction* + *A/B Testing Infrastructure Changes at Microsoft ExP* | `009/010` | `VERIFIED` | Le fonti supportano CUPED come variance-reduction technique, l'aumento di power senza aumentare la probabilità di decisione errata quando lo stimatore è corretto, l'`effective traffic multiplier` e l'utilità su test con traffico modesto. Il vecchio URL CUPED è stato sostituito con quello canonico corrente: `https://www.microsoft.com/en-us/research/articles/deep-dive-into-variance-reduction/`. |
| Cap. 9 — multiple metrics / correlated metrics | Microsoft Research, *Treatment Effect Assessment at Scale*, 15 luglio 2026 | `009/011` | `VERIFIED` | Fonte recente e time-sensitive verificata. Microsoft ExP dichiara che un esperimento può generare centinaia o migliaia di metriche; discute false discovery, correlazione tra metriche e rilevanza del metric set, con implicazioni esplicite per sistemi agentici. Il manoscritto non generalizza oltre il contesto documentato. URL canonico: `https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/`. |
| Cap. 9 — tenant randomization | Microsoft Research, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work* | `009/012` | `VERIFIED` | La fonte documenta la necessità di randomizzare a livello tenant quando utenti della stessa organizzazione richiedono esperienza coerente e descrive perdita di power, eterogeneità dei tenant e problemi di variance/balance. L'uso nel libro come analogia per scegliere il livello di randomizzazione è proporzionato. URL canonico: `https://www.microsoft.com/en-us/research/articles/why-tenant-randomized-a-b-test-is-challenging-and-tenant-pairing-may-not-work/`. |

## Esiti completati

### Blocco 1 — Capitolo 19

Le fonti ad alta priorità su lavoro, skill, agentic work e critical thinking sono **verificate senza necessità di correzioni al manoscritto**. Non vengono introdotte modifiche cosmetiche quando il claim è già ben calibrato.

### Blocco 2 — Capitoli 8–9, causalità ed experimentation

Il primo pass sui riferimenti più sensibili di causalità e sperimentazione è **verificato**. Non sono emersi claim causali da restringere nei file controllati. È emerso invece un problema di canonical URL: sei riferimenti Microsoft del Capitolo 9 usavano un percorso legacy che redirige al nuovo URL. I sei file sono stati aggiornati su `main` senza modificare il contenuto sostantivo dei claim.

## Prossimo blocco prioritario

Continuare con le fonti che sostengono:

1. casi reali documentati con organizzazioni nominate;
2. statistiche, benchmark e numeri time-sensitive;
3. standard e framework normativi/tecnici;
4. documentazione di tool e riferimenti evergreen.

L'obiettivo è arrivare a una classificazione esplicita di tutti i riferimenti prima del proofread globale e del layout QA.