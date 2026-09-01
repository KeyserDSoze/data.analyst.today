## 15.12 Esercizi: costruire decisioni, non soltanto analisi

Gli esercizi di questo capitolo non chiedono principalmente di calcolare numeri.

Chiedono di produrre **Decision Record difendibili**.

Per ogni caso, quando mancano dati, non inventarli silenziosamente. Indica:

- assunzione;
- informazione mancante;
- se vale la pena ottenerla;
- quale stato del Decision Quality Gate assegneresti.

---

## Esercizio 1 — Un'associazione forte, una decisione ancora aperta

Un'app subscription osserva:

```text
churn D90
utenti con ≥3 sessioni nella prima settimana: 12%
altri utenti: 31%
```

### Compito

Costruisci la prima metà del Decision Record.

Deve contenere:

- finding;
- materialità;
- claim level;
- possibili confondenti;
- almeno quattro alternative, incluso business as usual;
- una possibile azione reversibile prima di avere evidenza causale forte;
- quale informazione potrebbe cambiare la scelta;
- quale deliverable dei Capitoli 8–9 useresti se volessi sostenere un causal claim.

Non concludere automaticamente che “tre sessioni riducono il churn”.

---

## Esercizio 2 — Supplier risk: trovare la soglia, non fissarsi sul 68%

Un modello stima:

```text
P(delivery delay) = 68%
```

Un ordine alternativo preventivo costa €18.000.

Uno stock-out potrebbe costare circa €120.000, ma il range plausibile è €60k–€200k.

L'ordine alternativo è annullabile con una penale di €4.000 fino a 48 ore prima della consegna.

### Compito

1. Definisci le alternative.
2. Calcola o ragiona sul break-even probability / switching threshold rilevante.
3. Mostra come la reversibilità dell'ordine alternativo modifica la decisione.
4. Aggiungi almeno due impatti non monetari.
5. Distingui la qualità del risk score dalla qualità della decision policy.
6. Assegna uno stato: `DECIDE / PILOT-STAGE / WAIT FOR X / NO ACTION`.

---

## Esercizio 3 — Expected value senza decimali decorativi

Tre iniziative competono per lo stesso team.

### A — Payment reliability

- upside plausibile: €1,4M–€2,0M annui;
- evidenza forte;
- costo: €250k;
- time to value: 2 mesi;
- downside limitato.

### B — Referral redesign

- upside: €0–€3M;
- evidenza debole;
- costo: €450k;
- time to value: 5 mesi.

### C — Pricing redesign

- upside: €1M–€4M;
- evidenza media;
- costo: €900k;
- downside plausibile: churn e sales friction;
- difficile rollback sui contratti annuali.

### Compito

Non assegnare probabilità puntuali se non puoi difenderle.

Costruisci una Decision Scorecard con:

- expected/range value;
- evidence strength;
- downside;
- reversibilità;
- time to value;
- capacity fit;
- opportunity cost;
- switching assumption.

Raccomanda una priorità e completa:

> “Cambierei scelta se…”

---

## Esercizio 4 — Switching value

Un progetto di automazione ha:

- investimento iniziale: €350.000;
- risparmio annuo centrale: €240.000;
- manutenzione annua: €60.000;
- orizzonte previsto: 3 anni;
- adoption completa prevista dopo 4 mesi.

### Compito

Costruisci almeno questi switching values:

- risparmio annuo minimo;
- costo implementazione massimo;
- ritardo massimo di adozione;
- manutenzione massima.

Poi rispondi:

1. Quale variabile è più vicina alla decision boundary?
2. Su quale variabile compreresti informazione aggiuntiva?
3. Quanto deve essere precisa la stima perché la decisione sia robusta?
4. Esiste una versione staged/pilot con maggiore option value?

---

## Esercizio 5 — Scenari coerenti, non ±20%

Aster Logistics deve scegliere tra:

- BAU;
- nuovo hub completo;
- hub modulare;
- outsourcing per 24 mesi.

### Compito

Costruisci tre scenari **coerenti**:

1. domanda debole;
2. crescita centrale;
3. crescita forte + fuel inflation.

Per ogni scenario valuta qualitativamente:

- volume;
- saving logistico;
- capacità;
- capex;
- reversibilità;
- time to value.

Poi indica:

- opzioni dominate;
- opzione con massimo upside;
- opzione più robusta;
- informazione che potrebbe cambiare il ranking.

---

## Esercizio 6 — Caso reale documentato: leggere una decisione come NASA

NASA descrive la Decision Analysis come un processo che identifica criteri e alternative, valuta performance e incertezza, analizza la robustezza del ranking e documenta recommendation e decisione finale.

Fonte: https://www.nasa.gov/reference/6-8-decision-analysis/

### Compito

Scegli una decisione analitica aziendale, per esempio:

- build vs buy;
- nuovo data warehouse;
- nuovo mercato;
- rollout di un pricing;
- migrazione BI.

Ristrutturala usando:

```text
objectives
→ criteria
→ alternatives
→ uncertainty
→ robustness of ranking
→ recommendation
→ final decision
```

Quali elementi aggiunge questa struttura rispetto a un normale business case “progetto proposto + ROI”? 

---

## Esercizio 7 — Pre-mortem prima del go-live

Un'azienda vuole lanciare un sistema AI che assegna priorità ai lead commerciali.

Assumi:

> “Tra sei mesi il progetto è considerato un fallimento.”

### Compito

Genera almeno dieci failure mode divisi tra:

- data;
- model;
- sales process;
- incentives;
- adoption;
- governance;
- measurement;
- feedback loop.

Per i cinque più importanti definisci:

```text
leading indicator:
guardrail:
mitigation:
stop condition:
owner:
```

Poi spiega quali failure mode dovrebbero cambiare il design **prima** del rollout.

Riferimento sulla tecnica pre-mortem:

https://hbr.org/2007/09/performing-a-project-premortem

---

## Esercizio 8 — Decision quality vs outcome quality

Un team approva una campagna sulla base di un A/B test ben progettato.

Stima pre-rollout:

```text
uplift centrale: +4%
plausible interval: +1% to +7%
```

La campagna viene lanciata.

Nel mese successivo le vendite totali dell'azienda diminuiscono del 3%.

### Compito

Non giudicare subito la decisione.

Costruisci una review separando:

**Decision quality**

- design dell'esperimento;
- alternative;
- economics;
- guardrail;
- evidence threshold.

**Execution quality**

- rollout;
- exposure;
- targeting;
- implementazione.

**Outcome quality**

- performance della campagna;
- traffico totale;
- stagionalità;
- competitor/macroeconomia;
- altri shock.

Concludi spiegando che cosa sarebbe necessario osservare per affermare che la scelta di rollout era ex ante debole.

---

## Esercizio 9 — Aurora Home: secondo round

Riprendi il caso Aurora Home.

Dopo quattro settimane il pilot mostra:

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

### Compito

1. Il guardrail è stato superato materialmente o siamo troppo vicini alla soglia per dirlo?
2. Quale switching value conta di più?
3. Quale nuova informazione compreresti?
4. Continueresti, fermeresti o restringeresti il pilot?
5. Aggiorna il Decision Record senza riscrivere retroattivamente quello originale.

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

Il vincolo è che **recommendation e final decision devono essere distinguibili**.

---

## Esercizio 11 — Decision memo da una pagina

Dopo aver compilato l'esercizio precedente, crea una sintesi da una pagina per il decision owner.

Deve contenere soltanto:

1. decisione richiesta;
2. alternative;
3. evidenza che discrimina le alternative;
4. raccomandazione;
5. upside/downside;
6. incertezza decisiva;
7. switching condition;
8. guardrail;
9. decisione richiesta oggi.

Non raccontare cronologicamente tutta l'analisi.

Il Capitolo 16 mostrerà come trasformare questo contenuto in una comunicazione executive ancora più efficace.

---

## Chiusura del capitolo

L'analisi non termina quando abbiamo prodotto un numero corretto.

E non termina nemmeno quando abbiamo trovato una spiegazione interessante.

Termina quando abbiamo costruito un processo in cui:

```text
objective
→ alternatives
→ evidence
→ uncertainty
→ value/downside
→ reversibility
→ switching logic
→ recommendation
→ decision
→ learning
```

sono espliciti abbastanza da poter essere discussi, approvati e rivisti.

Il lavoro dell'analista non consiste nell'eliminare l'incertezza.

Consiste nel ridurla dove vale la pena, accettarla dove non è eliminabile e impedire che venga nascosta proprio nel momento in cui scegliamo.

> **Dati migliori non garantiscono decisioni migliori. Una decisione migliora quando evidenza, alternative, rischio e condizioni per cambiare idea sono visibili prima che l'esito ci racconti una storia troppo semplice.**
