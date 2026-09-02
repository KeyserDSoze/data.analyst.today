## 14.15 Sintesi ed esercizi: dall'assistente al sistema sotto responsabilità

Il punto del capitolo non è imparare a “usare l'AI per analytics”.

È costruire un'abitudine più difficile:

> **ogni delega deve avere un boundary, ogni output importante un controllo, ogni claim un livello di evidenza e ogni azione un owner.**

La sequenza finale è:

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

L'AI può entrare in quasi ogni blocco.

Non elimina nessuno dei passaggi logici che rendono l'analisi difendibile.

### Dieci idee da portare fuori dal capitolo

1. Un prompt è una specifica, non una formula magica.
2. Il Context Pack vale spesso più di un prompt più sofisticato.
3. Codice eseguibile non significa analisi corretta.
4. Un agente con tool è un sistema operativo, non un chatbot più lungo.
5. `STOP / DEGRADE / ESCALATE` sono output validi.
6. L'AI può generare causal stories; l'identification design autorizza causal claims.
7. Model search economico richiede evidenza finale più protetta, non meno.
8. Privacy e least privilege si progettano prima del prompt.
9. Un eval deve sostenere un claim specifico e va a sua volta validato.
10. Il deliverable finale è la **AI Analysis Control Sheet**, non la chat history.

---

## Esercizio 1 — SQL plausibile, Verification Bundle insufficiente

Un agente riceve:

> “Calcola la net revenue per cliente nel 2026.”

Genera una query che unisce `orders`, `order_items`, `payments` e `refunds`, somma `payment_amount - refund_amount` e raggruppa per `customer_id`.

La query gira.

### Compito

Costruisci il Verification Bundle prima di accettare il risultato.

Deve includere almeno:

- grain di ogni tabella;
- expected cardinality dei join;
- definizione certificata di net revenue;
- data economica;
- guest customer handling;
- refund timing;
- reconciliation con Finance;
- edge case;
- query o calcolo indipendente di controllo.

Assegna poi uno stato:

`APPROVED / APPROVED WITH CAVEATS / PROVISIONAL / BLOCKED`.

---

## Esercizio 2 — Caso reale documentato: Copilot usa la data sbagliata

Microsoft documenta un esempio in cui Copilot per Power BI, interrogato su profitto per anno, applica il filtro alla colonna `Birthday` del cliente invece della date table corretta.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

### Compito

Rispondi come se dovessi prevenire lo stesso failure mode nella tua organizzazione.

1. Qual è la classe di errore: sintattico, fattuale, strutturale, semantico o causale?
2. Quali campi devono entrare nel Context Pack?
3. Quale test deterministico o semantic check potrebbe intercettarlo?
4. Quale claim level consentiresti prima della verifica?
5. Come modificheresti semantic model e verified answers per ridurre il rischio?
6. Scrivi la relativa sezione della AI Analysis Control Sheet.

---

## Esercizio 3 — Cinque agenti, una raccomandazione troppo sicura

Un team usa:

1. data-quality agent;
2. SQL agent;
3. anomaly agent;
4. causal-reasoning agent;
5. executive-summary agent.

Il data-quality agent restituisce `PROVISIONAL`.

Il SQL agent trova revenue -6%.

L'anomaly agent segnala un evento raro.

Il causal agent scrive “pattern compatibile con un problema di pricing”.

L'executive-summary agent conclude:

> “Il pricing ha causato un calo del 6% della revenue.”

### Compito

Progetta:

- trust boundary tra agenti;
- metadata che devono accompagnare ogni artefatto;
- regola che impedisca la promozione del claim;
- stop condition;
- human checkpoint;
- audit trace.

Spiega perché cinque output non equivalgono a cinque evidenze indipendenti.

---

## Esercizio 4 — Privacy prima del clustering

Un team HR vuole inviare a un LLM esterno il testo completo delle exit interview per trovare temi ricorrenti.

I record contengono:

- nome;
- ruolo;
- manager;
- sede;
- età;
- testo libero;
- note HR;
- informazioni talvolta relative a salute o situazioni familiari.

### Compito

Non iniziare dal prompt.

Costruisci il **Data Exposure Review**:

- finalità;
- campi necessari;
- campi da escludere;
- trasformazioni/redaction;
- pseudonimizzazione;
- ambiente approvato;
- accesso dell'agente;
- review Privacy/Legal/DPO da richiedere secondo policy;
- retention;
- output restrictions.

Spiega perché pseudonimizzato non significa automaticamente anonimo.

Riferimenti:

- European Commission, GDPR principles: https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en
- EDPB, Opinion 28/2024: https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en

---

## Esercizio 5 — Caso reale documentato: quando l'eval è rotto

Nel 2026 OpenAI ha auditato SWE-Bench Pro e stimato che circa il 30% dei task presentasse problemi di costruzione o scoring.

Fonte: https://openai.com/index/separating-signal-from-noise-coding-evaluations/

### Compito

Trasferisci la lezione a un agente SQL aziendale.

Hai un eval set da 200 domande con accuracy dichiarata del 96%.

Progetta un audit dell'eval che controlli:

- qualità del ground truth;
- prompt sottospecificati;
- test troppo rigidi;
- test troppo permissivi;
- distribuzione dei casi;
- errori rari ma severi;
- shortcut/leakage;
- manual review di pass/fail;
- validità del claim “pronto per Finance”.

Concludi scrivendo una Eval Card.

---

## Esercizio 6 — LLM-as-a-judge

Un'organizzazione usa un secondo modello per giudicare automaticamente la qualità degli executive summary generati dal primo.

Il judge assegna score 1–5 su:

- correttezza;
- concisione;
- chiarezza;
- rispetto dei caveat.

### Compito

Progetta una procedura di calibrazione con:

- campione human-rated;
- rubric;
- disagreement analysis;
- false positive/false negative importanti;
- periodic audit;
- regression dopo cambio del judge;
- casi in cui il judge non deve essere l'unico gate.

Riferimento: Google Cloud documenta l'uso di human ratings come ground truth per valutare la qualità di judge model.

Fonte: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluate-judge-model

---

## Esercizio 7 — Caso reale documentato: un agente oltre il boundary di test

OpenAI ha documentato nel 2026 incidenti durante valutazioni cyber condotte da partner esterni, in cui la combinazione tra configurazioni di test, controlli e capacità del modello ha consentito attività oltre i confini previsti della valutazione.

Fonte: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

### Compito

Non analizzare il caso come incidente cyber. Usalo come problema di **agent control design**.

Per un agente analytics con accesso a warehouse, Slack e sistema di ticketing, definisci:

- agent identity;
- tool allowlist;
- read/write scope;
- network/data boundary;
- max steps;
- cost limit;
- forbidden actions;
- approval points;
- sandbox;
- action logging;
- kill switch;
- rollback.

Quali controlli testeresti in staging prima di dare accesso produttivo?

---

## Esercizio 8 — Model search con holdout contaminato dalle decisioni

Un agente prova 350 pipeline di churn prediction.

Ogni pipeline viene confrontata sullo stesso test set e i risultati vengono usati per decidere nuove feature e nuovi modelli.

La pipeline finale ottiene AUC 0,91.

### Compito

1. Perché il test set non è più realmente indipendente?
2. Come separeresti generator, selector ed evaluator?
3. Quale evidence set manterresti intatto?
4. Come controlleresti feature availability `as-of`?
5. Quale baseline useresti?
6. Quali metriche operative aggiungeresti oltre AUC?
7. Quando fermeresti la model search?

Compila il blocco Modeling Delegation Contract della Control Sheet.

---

## Esercizio 9 — Caso simulato/composito: DeltaHome e il rollback troppo veloce

> **Nota:** DeltaHome è un caso didattico simulato/composito.

DeltaHome è un retailer europeo. Lunedì mattina un sistema agentico segnala:

- revenue settimanale: -7,6%;
- conversion: -9,2%;
- mobile checkout: principale concentrazione del delta;
- ipotesi proposta: nuova UI introdotta venerdì.

Il sistema ha autonomamente:

- interrogato il warehouse;
- segmentato per paese e device;
- letto anomaly history;
- consultato release note;
- preparato una raccomandazione di rollback.

Prima dell'approvazione emerge che:

- il feed pagamenti di un provider è in ritardo di 11 ore;
- la nuova UI è attiva solo sul 25% degli utenti;
- un altro provider mostra conversion stabile;
- il calo apparente è concentrato proprio nel provider con feed incompleto.

### Compito

Compila l'intera **AI Analysis Control Sheet**.

Il deliverable deve includere:

- risk tier;
- autonomy level;
- data-readiness gate;
- fatti osservati;
- evidenze non mature;
- alternative hypotheses;
- claim consentito;
- claim bloccato;
- decisione da non prendere;
- condizione che renderebbe il rollback giustificato;
- human approver;
- prossimo check temporale;
- audit trace.

### Risposta professionale attesa

La direzione corretta non è:

> “La UI non è responsabile.”

Non abbiamo ancora evidenza sufficiente neppure per questo.

La conclusione corretta è più simile a:

> “Il calo osservato non è ancora interpretabile come effetto della nuova UI perché coincide con incompletezza del feed pagamenti. Il rollback resta un'ipotesi operativa, non una decisione supportata dall'evidenza corrente. Prima servono riconciliazione del provider, confronto esposti/non esposti e verifica del funnel su dati maturi.”

Status:

```text
PROVISIONAL
```

### Conclusione del capitolo

L'AI sposta il baricentro del lavoro analitico.

La sintassi, la generazione di query e molte attività di esplorazione diventano più economiche.

La scarsità si sposta verso:

```text
framing
→ semantica
→ confini
→ evidenza indipendente
→ verifica
→ claim discipline
→ governance
→ decisione
→ responsabilità
```

Questo chiude il cerchio con il Capitolo 0.

Essere **al timone** non significa eseguire ogni passaggio personalmente.

Significa sapere:

- cosa è stato delegato;
- quali assunzioni reggono il risultato;
- quali controlli sono passati;
- dove il sistema potrebbe ancora sbagliare;
- perché l'evidenza disponibile autorizza proprio quel livello di decisione e non uno più forte.

> **Il nuovo standard professionale non è dimostrare che l'AI non ha partecipato. È poter difendere il sistema di lavoro che ha trasformato la sua capacità in evidenza affidabile.**
