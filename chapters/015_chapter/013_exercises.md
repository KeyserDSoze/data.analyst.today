## 15.12 Esercizi: costruire decisioni, non soltanto analisi

Gli esercizi chiudono il capitolo facendo lavorare sull'intera catena:

```text
objective
→ alternatives
→ evidence
→ uncertainty
→ value / downside
→ reversibility
→ switching logic
→ recommendation
→ decision
→ learning
```

Quando un caso non fornisce abbastanza informazione, non inventarla. Dichiara l'assunzione mancante, indica se vale la pena comprarla e assegna uno stato del Decision Quality Gate. Il punto non è arrivare sempre a `DECIDE`: saper concludere `PILOT / STAGE`, `WAIT FOR X` o `NO ACTION` fa parte della competenza.

---

## Esercizio 1 — Un'associazione forte, una decisione ancora aperta

Un'app subscription osserva:

```text
churn D90
utenti con ≥3 sessioni nella prima settimana: 12%
altri utenti: 31%
```

Costruisci la prima metà del Decision Record. Deve includere finding, materialità, claim level, possibili confondenti, almeno quattro alternative compreso business as usual, una possibile azione reversibile prima di avere evidenza causale forte, l'informazione che potrebbe cambiare scelta e il deliverable dei Capitoli 8–9 che useresti per sostenere un causal claim.

Non concludere automaticamente che “tre sessioni riducono il churn”.

---

## Esercizio 2 — Supplier risk: trovare la soglia, non fissarsi sul 68%

Un modello stima:

```text
P(delivery delay) = 68%
```

Un ordine alternativo preventivo costa €18.000. Uno stock-out potrebbe costare circa €120.000, con range plausibile €60k–€200k. L'ordine alternativo è annullabile con penale di €4.000 fino a 48 ore prima della consegna.

Definisci le alternative, ragiona sul break-even probability / switching threshold, mostra come la reversibilità modifichi la scelta, aggiungi almeno due impatti non monetari e separa qualità del risk score da qualità della decision policy. Concludi con `DECIDE / PILOT-STAGE / WAIT FOR X / NO ACTION`.

---

## Esercizio 3 — Expected value senza decimali decorativi

Tre iniziative competono per lo stesso team.

**A — Payment reliability**

- upside plausibile: €1,4M–€2,0M annui;
- evidenza forte;
- costo: €250k;
- time to value: 2 mesi;
- downside limitato.

**B — Referral redesign**

- upside: €0–€3M;
- evidenza debole;
- costo: €450k;
- time to value: 5 mesi.

**C — Pricing redesign**

- upside: €1M–€4M;
- evidenza media;
- costo: €900k;
- downside plausibile: churn e sales friction;
- difficile rollback sui contratti annuali.

Non assegnare probabilità puntuali che non puoi difendere. Costruisci una Decision Scorecard con range value, evidence strength, downside, reversibilità, time to value, capacity fit, opportunity cost e switching assumption. Raccomanda una priorità e completa:

> **Cambierei scelta se...**

---

## Esercizio 4 — Switching value

Un progetto di automazione ha:

- investimento iniziale: €350.000;
- risparmio annuo centrale: €240.000;
- manutenzione annua: €60.000;
- orizzonte previsto: 3 anni;
- adoption completa prevista dopo 4 mesi.

Costruisci almeno gli switching values per risparmio annuo minimo, costo implementazione massimo, ritardo massimo di adozione e manutenzione massima. Poi identifica la variabile più vicina al decision boundary, quella su cui compreresti informazione aggiuntiva, la precisione necessaria perché la scelta sia robusta e una possibile versione staged/pilot con maggiore option value.

---

## Esercizio 5 — Scenari coerenti, non ±20%

Aster Logistics deve scegliere tra BAU, nuovo hub completo, hub modulare e outsourcing per 24 mesi.

Costruisci tre scenari coerenti — domanda debole, crescita centrale, crescita forte + fuel inflation — e per ciascuno valuta qualitativamente volume, saving logistico, capacità, capex, reversibilità e time to value. Indica poi opzioni dominate, opzione con massimo upside, opzione più robusta e informazione che potrebbe cambiare il ranking.

---

## Esercizio 6 — Caso reale documentato: leggere una decisione come NASA

NASA descrive la Decision Analysis come un processo che identifica criteri e alternative, valuta performance e incertezza, analizza la robustezza del ranking e documenta recommendation e decisione finale.[^nasa-exercise]

Scegli una decisione analitica aziendale — build vs buy, nuovo data warehouse, nuovo mercato, pricing rollout, migrazione BI o altro — e ristrutturala così:

```text
objectives
→ criteria
→ alternatives
→ uncertainty
→ robustness of ranking
→ recommendation
→ final decision
```

Spiega che cosa aggiunge questa struttura rispetto a un normale business case “progetto proposto + ROI”.

---

## Esercizio 7 — Pre-mortem prima del go-live

Un'azienda vuole lanciare un sistema AI che assegna priorità ai lead commerciali. Assumi:

> **Tra sei mesi il progetto è considerato un fallimento.**

Genera almeno dieci failure mode distribuiti tra data, model, sales process, incentives, adoption, governance, measurement e feedback loop. Per i cinque più importanti definisci:

```text
leading indicator:
guardrail:
mitigation:
stop condition:
owner:
```

Concludi indicando quali failure mode dovrebbero cambiare il design **prima** del rollout.[^premortem-exercise]

---

## Esercizio 8 — Decision quality vs outcome quality

Un team approva una campagna sulla base di un A/B test ben progettato.

```text
uplift centrale: +4%
plausible interval: +1% to +7%
```

Nel mese successivo le vendite totali dell'azienda diminuiscono del 3%.

Non giudicare subito la decisione. Costruisci una review separando:

**Decision quality** — design dell'esperimento, alternative, economics, guardrail, evidence threshold.

**Execution quality** — rollout, exposure, targeting, implementazione.

**Outcome quality** — performance della campagna, traffico totale, stagionalità, competitor/macroeconomia, altri shock.

Concludi spiegando quale evidenza sarebbe necessaria per affermare che la scelta di rollout era ex ante debole.

---

## Esercizio 9 — Aurora Home: secondo round

Dopo quattro settimane il pilot di Aurora Home mostra:

- contribution margin per visitor: +1,8%;
- conversion sul segmento esposto: -3,2%;
- AOV: +4,1%;
- complaints: +6%;
- competitor price gap invariato;
- confidence interval sul contribution margin ancora ampio.

Il guardrail originario era:

```text
conversion delta non oltre -3%
```

Valuta se il superamento è materialmente interpretabile oppure troppo vicino alla soglia, identifica lo switching value più importante, scegli quale nuova informazione comprare e decidi se continuare, fermare o restringere il pilot. Aggiorna il Decision Record **senza riscrivere retroattivamente quello originale**.

---

## Esercizio 10 — Decision Record completo

Scegli un problema reale o simulato e compila:

```text
Decision
Owner + deadline
Objective + constraints
Alternatives incl. BAU
Evidence + claim levels
Key assumptions
Dominant uncertainty
Value + downside
Non-monetizable impacts
Reversibility
Switching values
Scenarios
Pre-mortem
Recommendation
What would change our mind
Chosen decision
Guardrails / rollback
Learning plan
Review date
```

Il vincolo fondamentale è che **recommendation e final decision devono restare distinguibili**.

---

## Esercizio 11 — Decision memo da una pagina

Dopo aver compilato l'esercizio precedente, comprimi il Decision Record in una pagina per il decision owner. Il memo deve contenere soltanto decisione richiesta, alternative, evidenza che discrimina le alternative, recommendation, upside/downside, incertezza decisiva, switching condition, guardrail e scelta richiesta oggi.

Non raccontare cronologicamente tutta l'analisi. Questa è la preparazione diretta al Capitolo 16: la comunicazione dovrà **ridurre il costo cognitivo senza cambiare il significato, il claim level o il trade-off registrati nel Decision Record**.

## Chiusura del capitolo

L'analisi non termina quando abbiamo prodotto un numero corretto e nemmeno quando abbiamo trovato una spiegazione interessante. Termina quando objective, alternatives, evidence, uncertainty, value/downside, reversibility, switching logic, recommendation, decision e learning sono abbastanza espliciti da poter essere discussi, approvati e poi rivisti senza lasciare che l'esito riscriva ciò che sapevamo prima.

Il lavoro dell'analista non consiste nell'eliminare l'incertezza. Consiste nel ridurla dove vale la pena, accettarla dove non è eliminabile e impedire che venga nascosta proprio nel momento in cui scegliamo.

> **Dati migliori non garantiscono decisioni migliori. Una decisione migliora quando evidenza, alternative, rischio e condizioni per cambiare idea sono visibili prima che l'esito ci racconti una storia troppo semplice.**

[^nasa-exercise]: NASA, *6.8 Decision Analysis*, https://www.nasa.gov/reference/6-8-decision-analysis/
[^premortem-exercise]: Gary Klein, *Performing a Project Premortem*, Harvard Business Review, September 2007, https://hbr.org/2007/09/performing-a-project-premortem
