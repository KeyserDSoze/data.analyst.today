## 14.15 Sintesi ed esercizi: dall'assistente al sistema sotto responsabilità

Il capitolo non chiede al lettore di diventare più bravo a "usare l'AI". Chiede una disciplina più impegnativa: **ogni delega deve avere un boundary, ogni output importante un controllo, ogni claim un livello di evidenza e ogni azione un owner**.

La catena finale è:

```text
Decision
→ Analytical contract
→ Context Pack
→ Data/tool boundary
→ AI generation/execution
→ Verification Bundle
→ Method-specific gate
→ Eval / regression evidence
→ Claim gate
→ Human control
→ Action
→ Audit trace
```

L'AI può entrare in quasi ogni blocco, ma non elimina nessuno dei passaggi logici che rendono l'analisi difendibile. La **AI Analysis Control Sheet** serve proprio a tenere visibile questa catena.

---

## Esercizio 1 — SQL plausibile, Verification Bundle insufficiente

Un agente riceve:

> Calcola la net revenue per cliente nel 2026.

Genera una query che unisce `orders`, `order_items`, `payments` e `refunds`, somma `payment_amount - refund_amount` e raggruppa per `customer_id`. La query gira.

Costruisci il Verification Bundle prima di accettare il risultato. Deve includere almeno grain di ogni tabella, cardinalità attesa dei join, definizione certificata di net revenue, data economica, guest customer handling, refund timing, reconciliation con Finance, un edge case e un calcolo/query indipendente di controllo. Assegna poi uno stato:

```text
APPROVED
APPROVED WITH CAVEATS
PROVISIONAL
BLOCKED
```

---

## Esercizio 2 — Caso documentato: la data sbagliata in Power BI

Microsoft documenta un esempio in cui Copilot, interrogato sul profitto per anno, applica il filtro alla colonna `Birthday` del cliente invece della date table corretta.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

Spiega quale failure class rappresenta, quali informazioni devono entrare nel Context Pack, quale controllo semantico può intercettarla e quale claim level consentiresti prima della verifica. Proponi inoltre come AI data schema, instructions o verified answers potrebbero ridurre l'ambiguità e compila il relativo blocco della Control Sheet.

---

## Esercizio 3 — Cinque agenti, una conclusione troppo sicura

Un team usa data-quality agent, SQL agent, anomaly agent, causal-reasoning agent ed executive-summary agent. Il primo restituisce `PROVISIONAL`; il SQL agent trova revenue `-6%`; l'anomaly agent segnala un evento raro; il causal agent scrive "pattern compatibile con un problema di pricing". L'executive writer conclude:

> Il pricing ha causato un calo del 6% della revenue.

Progetta trust boundary tra agenti, metadata da trasportare con ogni artefatto, regola che impedisca la promozione del claim, stop condition, human checkpoint e audit trace. Spiega perché cinque output non equivalgono a cinque evidenze indipendenti.

---

## Esercizio 4 — Privacy prima del clustering

Un team HR vuole inviare a un LLM esterno il testo completo delle exit interview. I record contengono nome, ruolo, manager, sede, età, testo libero, note HR e talvolta informazioni relative a salute o situazioni familiari.

Non iniziare dal prompt. Costruisci il **Data Exposure Review**: finalità, campi necessari, campi da escludere, redaction, pseudonimizzazione, ambiente approvato, agent access, eventuale review Privacy/Legal/DPO, retention e output restrictions. Spiega perché pseudonimizzato non significa automaticamente anonimo.

Riferimenti:

- https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en

---

## Esercizio 5 — Caso documentato: quando l'eval è rotto

Nel luglio 2026 OpenAI ha auditato SWE-Bench Pro e stimato che circa il **30%** dei task presentasse problemi; la pipeline automatizzata ne aveva segnalati il `27,4%` e la campagna umana il `34,1%`.

Fonte: https://openai.com/index/separating-signal-from-noise-coding-evaluations/

Trasferisci la lezione a un agente SQL aziendale con eval set da 200 domande e accuracy dichiarata del 96%. Progetta un audit che controlli qualità del ground truth, prompt sottospecificati, test troppo rigidi o permissivi, distribuzione dei casi, failure rari ma severi, shortcut/leakage e manual review di pass/fail. Concludi con una Eval Card e spiega se il claim "pronto per Finance" è davvero supportato.

---

## Esercizio 6 — LLM-as-a-judge

Un'organizzazione usa un secondo modello per giudicare executive summary generati dal primo, con score 1–5 su correttezza, concisione, chiarezza e rispetto dei caveat.

Progetta una procedura con campione human-rated, rubric, disagreement analysis, false positive/negative importanti, periodic audit, regression dopo cambio del judge e casi in cui il judge non deve essere l'unico gate. Spiega come misureresti l'accordo tra judge e valutazioni umane.

Riferimento: https://cloud.google.com/blog/products/ai-machine-learning/evaluating-large-language-models-in-business

---

## Esercizio 7 — Caso documentato: un agente oltre il boundary di test

OpenAI ha documentato nell'agosto 2026 incidenti durante valutazioni cyber di terze parti in cui configurazione e controlli dell'ambiente hanno consentito attività oltre i boundary previsti.

Fonte: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

Non trattare il caso come esercizio cyber. Usalo come problema di **agent control design**. Per un agente analytics con accesso a warehouse, Slack e ticketing definisci identity, tool allowlist, read/write scope, network/data boundary, max steps, cost limit, forbidden actions, approval points, sandbox, action logging, kill switch e rollback. Indica quali controlli testeresti in staging prima dell'accesso produttivo.

---

## Esercizio 8 — Model search con holdout contaminato dalle decisioni

Un agente prova 350 pipeline di churn prediction. Ogni pipeline viene confrontata sullo stesso test set e i risultati guidano nuove feature e nuovi modelli. La pipeline finale ottiene AUC `0,91`.

Spiega perché il test set non è più indipendente, separa generator/selector/evaluator, definisci l'evidence set che manterresti intatto, controlla feature availability `as-of`, scegli una baseline e aggiungi metriche operative oltre AUC. Indica anche quando fermeresti la ricerca. Compila il blocco **Modeling Delegation Contract** della Control Sheet.

---

## Esercizio 9 — DeltaHome e il rollback troppo veloce

> **Nota:** DeltaHome è un caso didattico simulato/composito.

DeltaHome è un retailer europeo. Lunedì mattina un sistema agentico segnala revenue settimanale `-7,6%`, conversion `-9,2%`, mobile checkout come principale concentrazione e propone come ipotesi la nuova UI introdotta venerdì. Ha interrogato il warehouse, segmentato per paese/device, letto anomaly history, consultato release note e preparato un rollback.

Prima dell'approvazione emerge però che:

- il feed pagamenti di un provider è in ritardo di 11 ore;
- la nuova UI è attiva solo sul 25% degli utenti;
- un altro provider mostra conversion stabile;
- il calo apparente è concentrato nel provider con feed incompleto.

Compila l'intera **AI Analysis Control Sheet** includendo risk tier, autonomy level, readiness gate, fatti, evidenze immature, alternative, claim consentito e claim bloccato, decisione da non prendere, condizione che renderebbe il rollback giustificato, human approver e audit trace.

La risposta professionale non è "la UI non è responsabile". Non abbiamo evidenza sufficiente neppure per escluderlo. Una conclusione coerente è:

> Il calo osservato non è ancora interpretabile come effetto della nuova UI perché coincide con incompletezza del feed pagamenti. Il rollback resta un'ipotesi operativa, non una decisione supportata dall'evidenza corrente. Prima servono riconciliazione del provider, confronto esposti/non esposti e verifica del funnel su dati maturi.

Status:

```text
PROVISIONAL
```

## Chiusura del capitolo

L'AI sposta il baricentro del lavoro analitico. Sintassi, query e molte attività esplorative diventano più economiche; la scarsità si sposta verso **framing, semantica, confini, evidenza indipendente, verifica, claim discipline, governance e responsabilità**.

Questo chiude il cerchio con il Capitolo 0. Essere al timone non significa eseguire ogni passaggio personalmente. Significa sapere che cosa è stato delegato, quali assunzioni reggono il risultato, quali gate sono passati e perché l'evidenza autorizza proprio quel livello di decisione.

Il Capitolo 15 prende il testimone da qui. Una volta stabilito che un finding o un claim è sufficientemente supportato, resta ancora una domanda distinta: **quale scelta cambia davvero, tra quali alternative, con quali trade-off e con quale grado di reversibilità?**

> **Il nuovo standard professionale non è dimostrare che l'AI non ha partecipato. È poter difendere il sistema di lavoro che ha trasformato la sua capacità in evidenza affidabile.**
