## 15.6 Caso simulato/composito — Aurora Home: dal margine in calo a una decisione difendibile

> **Nota editoriale:** Aurora Home è un caso simulato/composito. Organizzazione, numeri e sequenza sono costruiti per mostrare come usare un Decision Record end-to-end.

Aurora Home è un retailer omnicanale.

Il margine lordo trimestrale scende:

```text
32,8% → 29,9%
```

Il COO apre il meeting con una diagnosi già pronta:

> “Stiamo scontando troppo. Riduciamo le promozioni Furniture.”

È una spiegazione plausibile.

È anche una decisione già implicita prima dell'analisi.

Il team analytics decide di separare:

```text
finding
→ diagnosis
→ alternatives
→ choice
```

### 1. Decisione richiesta

Non:

> “Perché il margine è sceso?”

ma:

> **“Quale intervento sul business Furniture recupera contribution margin con il minor downside accettabile nei prossimi due trimestri?”**

Decision owner: COO + Commercial Director.

Deadline: due settimane, prima della pianificazione Q4.

### 2. Obiettivo e vincoli

Obiettivo primario:

> recuperare almeno 1,5 punti di contribution margin Furniture entro due trimestri.

Guardrail:

- non ridurre conversion complessiva oltre 3%;
- non deteriorare NPS in modo materiale;
- nessun intervento che richieda una ripiattaformazione logistica completa nel trimestre;
- budget implementativo massimo €750k per la prima fase.

Questi vincoli eliminano alcune soluzioni prima ancora di stimarne il valore con grande precisione.

### 3. Finding e materialità

Gross margin:

```text
-2,9 pp
```

Il dato è riconciliato con Finance.

La decomposizione per categoria mostra che Furniture spiega il 61% del deterioramento.

Questa è informazione materialmente decision-relevant.

### 4. La prima ipotesi non regge da sola

Furniture ha più promozioni.

Ma:

```text
net selling price medio: -1,2%
```

Il delta non è sufficiente a spiegare gran parte della compressione del margine.

Il team evita quindi il salto:

```text
promotion ↑
+ margin ↓
→ promotion caused margin decline
```

### 5. Decomposition più profonda

Emergono due componenti forti.

**Product cost**

- costo medio di acquisto: +4,8%;
- aumento concentrato su 15 SKU ad alto volume;
- parte del delta associata a cambio e nuovi termini fornitore.

**Logistics**

- costo medio ordine bulky: €42 → €58;
- share ordini bulky: 18% → 27%;
- alcuni ordini a basso AOV diventano marginalmente negativi dopo fulfilment.

Le promozioni contribuiscono, ma non dominano più la spiegazione.

### 6. Insight

Il finding:

> “Furniture margin -X.”

si trasforma in:

> **“Il deterioramento è soprattutto la combinazione di aumento dei costi di acquisto su pochi SKU ad alto volume e crescita del mix bulky con fulfilment più costoso. Un taglio promozionale generalizzato colpirebbe anche ordini dove la promozione non è il problema principale.”**

Claim level:

- decomposizione descrittiva: forte;
- causalità completa su volume/elasticità: non ancora identificata;
- sufficiente per generare alternative e test reversibili: sì.

### 7. Longlist delle alternative

Il team costruisce una longlist prima di innamorarsi di una soluzione.

```text
A — business as usual
B — taglio generalizzato delle promozioni Furniture
C — surcharge logistico su bulky sotto una soglia economica
D — soglia free-shipping differenziata per bulky
E — rinegoziazione / dual sourcing sui 15 SKU
F — restringere assortimento bulky a contribution margin negativo
G — combinazione C + E con rollout graduale
```

### 8. Shortlist e Recommendation Card

Dopo i vincoli, restano B, C, E e G.

| Dimensione | B: taglio promo | C: surcharge mirato | E: fornitori | G: C + E |
|---|---|---|---|---|
| upside | alto se volume regge | medio | medio-alto | alto |
| evidenza | bassa-media | media-alta | media | media-alta |
| time to value | rapido | rapido | lento | misto |
| reversibilità | alta | alta | media | media-alta |
| downside | conversion/volume | conversion su bulky | supply risk | più complesso |
| costo iniziale | basso | basso-medio | medio | medio |

La tabella non produce un vincitore automatico.

Rende però chiaro che B ha un upside apparente alto ma poggia sull'assunzione più fragile: volume quasi invariato dopo il taglio promo.

### 9. Switching values

Il team identifica le assunzioni che possono cambiare la preferenza.

Per C:

> il surcharge perde attrattività se la riduzione di conversion sugli ordini interessati supera circa la soglia economica definita dal contribution margin recuperato.

Per E:

> la rinegoziazione perde priorità se il saving ottenibile sui 15 SKU è inferiore al costo/opportunity cost di switching e qualifica fornitori.

Per G:

> la combinazione è preferita se C genera valore nel breve senza oltrepassare il guardrail conversion, mentre E mantiene un saving credibile nel medio termine.

Il team non cerca di fingere che tutte queste soglie siano note con precisione prima del test.

Le usa per definire cosa deve essere misurato.

### 10. La raccomandazione

Analytics raccomanda G:

1. pilotare un surcharge selettivo sugli ordini bulky economicamente fragili;
2. non ridurre in modo generalizzato le promozioni;
3. aprire rinegoziazione/dual sourcing sui 15 SKU più rilevanti;
4. introdurre contribution margin per ordine come metrica decisionale, includendo fulfilment.

Perché G batte B?

- interviene sui driver meglio localizzati;
- preserva più volume promozionale;
- combina una leva rapida e reversibile con una strutturale;
- consente di comprare informazione sulla price sensitivity del surcharge.

### 11. La decisione effettiva

Il COO approva la raccomandazione con una modifica:

- il pilot surcharge parte soltanto su due mercati, non su quattro.

Motivo:

> Operations non ha capacità di gestire contemporaneamente modifiche di fulfilment e pricing in quattro paesi.

Il Decision Record conserva:

```text
analytics recommendation:
2–4 market pilot + supplier action

chosen decision:
2 market pilot + supplier action

reason for difference:
operational capacity constraint
```

Questo è importante: la decisione finale non “smentisce” l'analisi. Integra un vincolo del decision owner.

### 12. Learning contract

Metriche del pilot:

- contribution margin per visitor;
- conversion rate;
- AOV;
- cancellation;
- customer complaints;
- mix bulky;
- repeat behavior degli utenti esposti.

Guardrail:

```text
conversion delta < -3% → review immediata
complaints oltre soglia → review
contribution margin per visitor non migliora → stop
```

Review:

- primo health check dopo 7 giorni;
- decision review dopo 4 settimane.

### 13. Pre-mortem rapido

Prima del rollout il team assume:

> “Tra quattro settimane il pilot è fallito.”

Possibili cause:

- il surcharge riduce conversion più del previsto;
- clienti spostano ordini verso competitor;
- il test coinvolge mix mercati non comparabile;
- costi logistici sono allocati male;
- Customer Service compensa manualmente il surcharge con voucher;
- supplier negotiation richiede molto più tempo.

Da qui nascono nuovi controlli nel learning contract.

### 14. Cosa avrebbe prodotto la diagnosi iniziale

La narrativa iniziale era:

```text
margin down
→ promotions too aggressive
→ cut promotions
```

Il processo revisionato è:

```text
Decision
→ objective + constraints
→ finding
→ decomposition
→ alternatives incl. BAU
→ value/downside/reversibility
→ switching assumptions
→ recommendation
→ owner decision
→ learning contract
```

La differenza non è soltanto “più analisi”.

È una struttura che impedisce alla prima spiegazione plausibile di diventare automaticamente la prima azione.

### Decision Record sintetico

```text
Decision:
come recuperare contribution margin Furniture

Objective:
+1,5 pp entro due trimestri

BAU:
nessun intervento

Preferred option:
pilot surcharge mirato + supplier action

Main evidence:
costo prodotto +4,8%; bulky fulfilment €42→€58; bulky mix 18%→27%

Main uncertainty:
elasticità al surcharge

Reversibility:
alta sul pilot; media sul sourcing

Switching condition:
downside conversion supera valore di margin recovery

Chosen decision:
pilot due mercati + sourcing

Review:
4 settimane
```

> **Il valore dell'analista non è trovare la storia più semplice sul numero che è peggiorato. È costruire un confronto tra alternative abbastanza rigoroso da rendere visibile perché una scelta merita di essere preferita alle altre.**
