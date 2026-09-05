## 17.12 Capstone Gate, rubric ed esercizi

Questo capitolo non va memorizzato come una tabella `problema → tecnica`. Se dopo i casi pensassimo “churn = modello”, “tempo = forecasting”, “release = A/B test”, avremmo costruito una nuova scorciatoia proprio dove volevamo imparare a ragionare.

Il capstone deve invece rispondere a una domanda:

> **Quale sequenza minima di evidenze ha il diritto di cambiare questa decisione, e quando altra analisi smette di valere il suo costo?**

Per renderla operativa conserviamo tre artefatti strutturati: il **Capstone Gate**, un **Method Budget** e la **Capstone Rubric**.

## Capstone Gate

Prima di consegnare un'analisi end-to-end, il team deve poter rispondere a questi nove blocchi.

### 1. Decisione

- Quale scelta concreta è aperta?
- Chi può prenderla ed entro quando?
- Qual è `business as usual / do nothing`?

### 2. Failure cost

- Quanto costa agire erroneamente?
- Quanto costa non agire?
- Quanto costa aspettare?
- Quale downside è irreversibile o ha grande blast radius?

### 3. Claim necessario

- Serve descrivere, diagnosticare, prevedere, identificare un effetto causale/treatment effect o confrontare economics?
- La decisione richiede davvero quel livello di claim?

### 4. Readiness

- Grain, identità e denominatore sono corretti?
- Definizione e time semantics sono stabili?
- Freshness/maturity sono sufficienti?
- Esistono measurement change, selection, leakage, exposure o comparability failure?
- Il dato riconcilia con una fonte indipendente quando il rischio lo richiede?

### 5. Ipotesi e alternative

- Esiste almeno una spiegazione concorrente seria?
- Abbiamo cercato evidence against?
- Esiste un'azione più piccola, reversibile o economica?
- `Do nothing`, `pilot` e `wait for information` sono stati considerati quando sensati?

### 6. Method Gate

Per ogni tecnica proposta completiamo:

> **“Se non facessimo questa analisi, quale rischio decisionale rimarrebbe aperto?”**

Se non sappiamo rispondere, la tecnica è candidata a essere eliminata.

### 7. Stop rule e switching condition

- Quando l'evidenza è sufficiente per la decisione corrente?
- Quale informazione potrebbe cambiare il ranking?
- Qual è la soglia operativa che cambia stato?

Gli stati ammessi sono deliberatamente più ricchi di `GO / NO-GO`:

```text
DECIDE
PILOT / STAGE
WAIT FOR X
BUY INFORMATION
NO ACTION / ABANDON
BLOCKED
NOT IDENTIFIED
```

`NOT IDENTIFIED` significa che il claim richiesto non è sostenibile con il disegno disponibile. Non è un invito a inventare una stima più sofisticata.

### 8. Decision quality

- Value e downside sono incrementali rispetto alla baseline?
- Reversibilità e option value sono esplicite?
- La recommendation è robusta a scenari plausibili?
- Quale owner accetta il trade-off?

### 9. Communication integrity

- Observed, inferred e unknown restano distinti?
- La headline ha la stessa forza del claim analitico?
- L'incertezza che attraversa la decision boundary è visibile?
- La visualizzazione può far sembrare più forte l'evidenza?
- La decisione richiesta oggi è esplicita?

## Method Budget

Un capstone può fallire anche per eccesso di rigore apparente. Prima della prima decisione assegniamo quindi un **method budget**:

```text
Decision deadline:
Maximum methods/deliverables before first decision:
Current evidence already sufficient for:
Unclosed decision risks:
Next method candidate:
Risk closed by that method:
Cost/time to obtain it:
Stop state if not obtained:
```

Il budget non vieta di approfondire. Costringe a dimostrare il valore marginale del prossimo metodo.

## Capstone Rubric

Un caso non viene valutato dal numero di pagine o tecniche. Una rubrica da 0 a 3 rende esplicito che anche la **complessità minima sufficiente** è una competenza.

| Dimensione | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Decision framing | nessuna decisione | vaga | esplicita | decisione + alternative + timing |
| Data semantics | assunte | controlli minimi | metriche/grain verificati | reconciliation + failure mode espliciti |
| Hypothesis discipline | una storia | alternative deboli | ipotesi concorrenti | evidence for/against + falsification |
| Method selection | tool-first | plausibile | coerente col claim | **minimo sufficiente + method gate** |
| Uncertainty | ignorata | caveat generici | quantificata/descritta | collegata a switching threshold |
| Decision economics | assente | beneficio isolato | costi/benefici | downside + reversibilità + option value |
| Stop rule | assente | implicita | esplicita | stato + trigger + next evidence |
| Communication | cronologia | summary | decision-first | claim calibrato + evidence hierarchy + provenance |
| Outcome review | assente | KPI generico | metriche coerenti | decision/execution/outcome separati |

Una soluzione sovra-ingegnerizzata può quindi perdere punti in method selection anche se usa correttamente molte tecniche.

---

## Esercizio 1 — “La crescita non si vede nella cassa”

Un B2B SaaS riporta ARR **+18%**, new logo **+27%**, cash collection **-9%**, DSO **47 → 66 giorni**, churn stabile. Il CFO chiede perché la crescita non si veda nella cassa.

Costruisci Capstone Routing Canvas ed Evidence Ledger. Definisci decisione, failure cost, almeno tre spiegazioni concorrenti, il primo reconciliation check, i deliverable realmente necessari e quelli che non useresti ancora. La stop rule deve specificare quale evidenza è sufficiente per una prima azione su billing/collection o per concludere che serve altra informazione.

Possibili aree da investigare sono billing terms, annual vs monthly, invoice timing, collection, customer mix, discount e differenza tra revenue recognition e cash. L'ordine, però, deve derivare dalla decisione.

---

## Esercizio 2 — “Dopo la release la conversione è scesa”

Dopo una release mobile:

```text
checkout conversion -4,2%
crash rate +0,3 pp
Android stabile
iOS -7,1%
payment failures +5%
traffic mix apparentemente stabile
```

Il VP Product chiede “Rollback?”. Definisci i controlli dei primi 30 minuti e ciò che deve essere vero per autorizzare rollback immediato. Distingui release, payment provider, tracking e mix; indica quando lo stato deve essere `ROLLBACK`, `HOLD`, `CONTINUE` o `NOT IDENTIFIED`.

Non è obbligatorio arrivare a una causa unica.

---

## Esercizio 3 — “Questa campagna è eccezionale?”

Una campagna mostra ROAS **6,4x**, ma il 72% dei convertiti era già cliente, branded search cresce nello stesso periodo, non esiste holdout e gli utenti più attivi ricevono più exposure.

Costruisci il Routing Canvas. Quale claim sostiene il ROAS osservato? Quale claim serve per triplicare il budget? Quale evidenza manca? Quando un esperimento ha abbastanza Value of Information da giustificare l'attesa? Che cosa comunicheresti oggi, prima del test?

---

## Esercizio 4 — “Quale forecast è migliore?”

Due forecast di domanda:

```text
A: MAE 920 unità, sottostima i picchi
B: MAE 1.040 unità, sovrastima leggermente i picchi
stock-out cost = 4 × overstock cost per unità
```

Definisci decisione operativa, orizzonte, loss function di business, informazioni mancanti, ruolo di intervalli/quantili e switching condition tra le policy. Il deliverable non è obbligato a scegliere il modello con MAE minore.

---

## Esercizio 5 — “Abbiamo 20.000 clienti a rischio”

Un modello identifica 20.000 clienti high-risk; Retention può contattarne soltanto 4.000.

Progetta una policy migliore del ranking per churn probability considerando valore cliente, costo intervento, capacity, treatment opportunity, non-persuadable cases e constraint/fairness rilevanti. Specifica quale parte richiede prediction e quale richiede causal evidence. Indica anche quale esperimento **non** faresti se la capacità fosse già allocabile in modo robusto senza conoscere un treatment effect più preciso.

---

## Esercizio 6 — “Più inventory, più stock-out”

Un'azienda osserva inventory value **+16%**, fill rate **-3 pp**, expedite cost **+28%**; nove componenti spiegano il **61% del production downtime**. Il COO propone +10% su tutti i target di stock.

Costruisci una risposta che distingua aggregato/distribuzione, variabilità, criticità, lead time, downtime cost e working capital. Dichiara esplicitamente quale analisi **non aspetteresti** prima di intervenire sui nove componenti critici e perché l'attesa avrebbe scarso valore marginale.

---

## Esercizio 7 — “Il test è significativo”

Un esperimento mostra uplift **+1,1 pp**, `p = 0,012`, SRM significativo, guardrail revenue positivo e latency **+9%**.

Assegna uno stato tra `APPROVED`, `APPROVED WITH CAVEATS`, `PROVISIONAL` e `BLOCKED`. Poi indica quale evidence gate deve cambiare stato. La risposta deve distinguere la qualità del primary effect dalla validità del comparison.

---

## Esercizio 8 — Il caso senza etichetta

Un marketplace osserva contemporaneamente:

```text
ordini +9%
margin/order -14%
NPS -6 punti
nuovi seller +35%
refund rate +2,1 pp
delivery time +0,6 giorni
marketing spend +22%
customer support cost +19%
```

Il CEO chiede: **“La crescita è sana?”**

Prepara un **Capstone Case File** contenente decisione/owner, `do nothing`, failure cost, claim necessario, metric/data contract minimo, ipotesi concorrenti, Evidence Ledger, method gate, stop rule, alternative, switching condition, Decision Record sintetico, Decision Communication Pack da una pagina e outcome review.

### Vincolo — Method Budget

Prima della **prima decisione** non puoi usare più di **sei deliverable canonici**. Per ciascuno devi scrivere quale rischio chiude. I deliverable esclusi devono essere motivati con la stessa attenzione di quelli inclusi.

Dopo la prima decisione puoi attivare altri metodi soltanto se emerge una nuova decisione o un nuovo failure risk.

---

## Esercizio 9 — Dal capstone al sistema operativo

Riprendi uno degli esercizi precedenti e immagina che la stessa decisione debba essere presa **ogni lunedì alle 08:30**.

Non ridisegnare ancora l'architettura. Elenca invece ciò che non può più restare nella memoria dell'analista:

- metric/source-of-truth contract;
- owner;
- freshness/correctness expectation;
- readiness gate;
- fallback/degraded mode;
- alert/escalation;
- change policy;
- cost-to-serve;
- review/retirement condition.

Questo è il ponte al Capitolo 18: la stessa capacità che nel capstone era un progetto diventa un **servizio analitico ricorrente**.

## Chiusura del capitolo

I casi hanno attraversato vendite, churn, pricing, marketing, supply chain, product analytics, forecasting, experimentation, anomaly investigation e unit economics. Non convergono su una tecnica. Convergono su una responsabilità:

```text
messy question
→ decision + failure cost
→ claim needed
→ readiness
→ cheapest discriminating evidence
→ method escalation only if needed
→ alternatives
→ stop state
→ decision
→ communication
→ outcome review
```

Un analista maturo sa riconoscere quale evidenza manca, quanto costa ottenerla, se può davvero cambiare la scelta e quando il prossimo metodo sarebbe soltanto ritardo o complessità.

La domanda finale non è più “quale tecnica hai usato?”. È:

> **Perché questa sequenza di evidenze era sufficiente per questa decisione, che cosa avrebbe cambiato la scelta e che cosa dovremmo rendere operativo se dovessimo rifarla ogni settimana?**

È esattamente la domanda da cui parte il Capitolo 18.
