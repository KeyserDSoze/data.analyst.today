## 17.12 Capstone gate, rubric ed esercizi

Questo capitolo non va memorizzato come una collezione di ricette.

Se dopo averlo letto pensassimo:

> “quando vedo churn uso il modello; quando vedo tempo uso forecasting; quando vedo una release uso A/B testing”

avremmo mancato il punto.

Il lavoro reale richiede prima di capire **quale decisione è aperta e quale tipo di evidenza ha il diritto di cambiarla**.

## Il Capstone Gate

Prima di consegnare un'analisi end-to-end, il team deve poter rispondere a nove domande.

### 1. Decisione

- Quale scelta concreta è aperta?
- Chi può prenderla?
- Entro quando?
- Qual è l'alternativa `do nothing`?

### 2. Failure cost

- Qual è il costo di un falso allarme?
- Qual è il costo di non intervenire?
- Qual è il costo dell'attesa?
- Il downside è reversibile?

### 3. Claim

Stiamo cercando di sostenere un claim:

- descrittivo;
- diagnostico;
- predittivo;
- causale;
- di treatment effect;
- economico/decisionale?

Il metodo scelto ha davvero il diritto di sostenere quel claim?

### 4. Readiness

- Grain corretto?
- Definizione stabile?
- Denominatore corretto?
- Freschezza sufficiente?
- Comparabilità temporale?
- Measurement change?
- Selection/leakage?
- Reconciliation con una fonte indipendente?

### 5. Alternative

- Abbiamo considerato almeno una spiegazione concorrente seria?
- Abbiamo cercato evidence against?
- Esiste una soluzione più semplice?
- Abbiamo incluso `do nothing`, pilot o wait-for-information quando sensati?

### 6. Method gate

Per ogni tecnica usata dobbiamo completare:

> **“Se non facessimo questa analisi, quale rischio decisionale rimarrebbe aperto?”**

Se non sappiamo rispondere, quella tecnica è candidata a essere eliminata.

### 7. Stop rule e switching condition

- Quando l'evidenza è sufficiente per decidere?
- Quale nuova informazione cambierebbe scelta?
- Quale soglia produce `PILOT`, `WAIT`, `NO ACTION` o `BLOCKED`?

### 8. Decision quality

- Valore e downside sono espliciti?
- Reversibilità e option value sono considerate?
- La raccomandazione è robusta a scenari plausibili?
- Esiste un owner dell'azione?

### 9. Communication integrity

- Fatti, inferenze e unknown sono separati?
- Il claim nella headline ha la stessa forza del claim nell'analisi?
- L'incertezza decision-critical è visibile?
- La visualizzazione può indurre un'interpretazione più forte dell'evidenza?
- La decisione richiesta è esplicita?

## La Capstone Rubric

Un caso non viene valutato dal numero di pagine o tecniche usate.

Possiamo usare una rubrica da 0 a 3 per dimensione.

| Dimensione | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Decision framing | nessuna decisione | decisione vaga | decisione esplicita | decisione + alternative + timing |
| Data semantics | assunte | controlli minimi | metriche/grain verificati | reconciliation + failure mode espliciti |
| Hypothesis discipline | una storia | alternative deboli | ipotesi concorrenti | evidence for/against + falsification |
| Method selection | tool-first | tecnica plausibile | tecnica coerente col claim | tecnica minima sufficiente + method gate |
| Uncertainty | ignorata | caveat generici | quantificata/descritta | collegata a switching threshold |
| Decision economics | assente | beneficio isolato | costi/benefici | downside + reversibilità + option value |
| Stop rule | assente | implicita | esplicita | stop/degrade/escalate condizionali |
| Communication | cronologia analisi | summary | decision-first | claim calibrato + evidence hierarchy + provenance |
| Outcome review | assente | KPI generico | metriche coerenti | review di decision quality separata dalla fortuna |

Un punteggio alto non richiede di usare tutti i deliverable.

Anzi, una soluzione sovra-ingegnerizzata può perdere punti in method selection.

## Esercizio 1 — “La crescita non si vede nella cassa”

Un'azienda B2B SaaS riporta:

- ARR `+18%`;
- new logo `+27%`;
- cash collection `-9%`;
- DSO `47 → 66 giorni`;
- churn stabile.

Il CFO chiede:

> “Perché la crescita non si vede nella cassa?”

### Compito

Non partire da una tecnica.

Compila:

1. decisione aperta;
2. failure cost;
3. tre spiegazioni concorrenti;
4. primo reconciliation check;
5. deliverable necessari;
6. deliverable che **non** useresti ancora;
7. stop rule;
8. headline che potresti sostenere solo dopo l'analisi.

Possibili aree da investigare includono billing terms, annual vs monthly, invoice timing, collection, customer mix, discount e differenza tra revenue recognition e cash.

Ma l'ordine dell'indagine deve derivare dalla decisione.

## Esercizio 2 — “Dopo la release la conversione è scesa”

Dopo una release mobile:

- checkout conversion `-4,2%`;
- crash rate `+0,3 pp`;
- traffic mix apparentemente stabile;
- Android stabile;
- iOS `-7,1%`;
- payment failures `+5%`.

Il VP Product chiede:

> “Rollback?”

### Compito

Definisci:

- cosa deve essere vero per autorizzare un rollback immediato;
- quali controlli faresti nei primi 30 minuti;
- quali evidenze distinguono release, payment provider e tracking;
- quale azione è reversibile;
- quando diresti `ROLLBACK`, `HOLD`, `CONTINUE` o `NOT IDENTIFIED`.

Non è obbligatorio arrivare a una causa unica.

## Esercizio 3 — “Questa campagna è eccezionale?”

Una campagna mostra ROAS `6,4x`.

Ma:

- 72% dei convertiti era già cliente;
- branded search cresce nello stesso periodo;
- non esiste holdout;
- la campagna viene mostrata più spesso agli utenti più attivi.

Il CMO propone di triplicare il budget.

### Compito

Costruisci un Capstone Routing Canvas.

In particolare:

- qual è il claim che il ROAS può sostenere?
- quale claim serve per triplicare il budget?
- quale evidenza manca?
- quando un esperimento avrebbe valore informativo sufficiente da giustificare l'attesa?
- cosa comunicheresti oggi, prima del test?

## Esercizio 4 — “Quale forecast è migliore?”

Due forecast di domanda:

- A: MAE 920 unità;
- B: MAE 1.040 unità.

A sottostima i picchi; B li sovrastima leggermente.

Il costo di stock-out è quattro volte il costo di overstock per unità.

### Compito

Non scegliere subito A o B.

Definisci:

1. decisione operativa;
2. orizzonte;
3. loss function di business;
4. informazioni mancanti;
5. eventuale ruolo di intervalli/quantili;
6. switching condition tra le due policy.

## Esercizio 5 — “Abbiamo 20.000 clienti a rischio”

Un modello identifica 20.000 clienti ad alto rischio.

Il team retention può contattarne soltanto 4.000.

### Compito

Progetta una policy migliore del ranking per churn probability.

Considera:

- valore cliente;
- costo intervento;
- capacità;
- probabilità di risposta;
- effetto incrementale;
- casi non persuadibili;
- fairness/constraint operative rilevanti.

Poi specifica quale parte è predizione e quale richiede evidenza causale.

## Esercizio 6 — “Più inventory, più stock-out”

Un'azienda vede:

- inventory value `+16%`;
- fill rate `-3 pp`;
- expedite cost `+28%`;
- 9 componenti spiegano il 61% del production downtime.

Il COO propone di aumentare del 10% tutti i target di stock.

### Compito

Costruisci una risposta che distingua:

- aggregato e distribuzione;
- variabilità;
- criticità;
- lead time;
- costo del fermo;
- working capital;
- scenario decisionale.

Dichiara anche quale analisi **non** aspetteresti prima di intervenire sui nove componenti più critici.

## Esercizio 7 — “Il test è significativo”

Un esperimento mostra:

- uplift `+1,1 pp`;
- p-value `0,012`;
- SRM significativo;
- guardrail revenue positivo;
- latency peggiorata del 9%.

Il team vuole fare rollout.

### Compito

Assegna uno stato:

- `APPROVED`;
- `APPROVED WITH CAVEATS`;
- `PROVISIONAL`;
- `BLOCKED`.

Spiega quali gate devono essere superati per cambiare stato.

## Esercizio finale — Il caso senza etichetta

Un marketplace osserva contemporaneamente:

- ordini `+9%`;
- margin/order `-14%`;
- NPS `-6 punti`;
- nuovi seller `+35%`;
- refund rate `+2,1 pp`;
- delivery time `+0,6 giorni`;
- marketing spend `+22%`;
- customer support cost `+19%`.

Il CEO chiede:

> **“La crescita è sana?”**

Non viene fornito alcun metodo suggerito.

### Deliverable richiesto

Prepara un **Capstone Case File** con:

1. decisione e owner;
2. `do nothing`;
3. failure cost;
4. claim necessario;
5. metric/data contract minimo;
6. ipotesi concorrenti ordinate;
7. evidence ledger `observed / inferred / unknown`;
8. deliverable che attiveresti;
9. deliverable che non attiveresti e perché;
10. method gate per ogni tecnica scelta;
11. stop rule;
12. alternative;
13. switching condition;
14. Decision Record sintetico;
15. Decision Communication Pack da una pagina;
16. outcome review.

### Vincolo

Non puoi usare più di **sei deliverable canonici** prima della prima decisione.

Il vincolo è intenzionale.

Costringe a prioritizzare il rischio invece di trasformare il capstone in una dimostrazione enciclopedica.

## Chiusura del capitolo

I casi del capitolo attraversano domini diversi, ma la struttura profonda converge:

```text
messy question
→ decision
→ failure cost
→ claim needed
→ readiness
→ competing explanations
→ method gate
→ evidence
→ alternatives
→ uncertainty
→ decision
→ communication
→ outcome review
```

Non esiste una tecnica obbligatoria in ogni passaggio.

Esiste invece una responsabilità costante: evitare che il livello di certezza cresca più velocemente dell'evidenza.

Un analista maturo non riconosce soltanto pattern nei dati.

Riconosce:

- quale tipo di evidenza manca;
- quanto costa ottenerla;
- se quella informazione può davvero cambiare la decisione;
- quando una risposta è sufficientemente affidabile per agire;
- quando è professionale dire `non ancora`;
- quando altra analisi sarebbe soltanto ritardo o complessità.

La domanda finale del capstone non è:

> “Quale tecnica hai usato?”

È:

> **“Perché questa sequenza di evidenze era sufficiente per questa decisione, e cosa ti avrebbe fatto scegliere diversamente?”**

Se sappiamo rispondere, il libro ha raggiunto uno dei suoi obiettivi principali.
