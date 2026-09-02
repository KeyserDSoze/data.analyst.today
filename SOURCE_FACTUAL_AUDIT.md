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

## Primo esito

Il primo blocco di fonti ad alta priorità del Capitolo 19 è **verificato senza necessità di correzioni al manoscritto**. Non vengono introdotte modifiche cosmetiche quando il claim è già ben calibrato.

## Prossimo blocco prioritario

Continuare con le fonti che sostengono:

1. claim causali e quasi-causali nei Capitoli 8–9;
2. casi reali documentati con organizzazioni nominate;
3. statistiche, benchmark e numeri time-sensitive;
4. standard e framework normativi/tecnici;
5. infine documentazione di tool e riferimenti evergreen.

L'obiettivo è arrivare a una classificazione esplicita di tutti i riferimenti prima del proofread globale e del layout QA.