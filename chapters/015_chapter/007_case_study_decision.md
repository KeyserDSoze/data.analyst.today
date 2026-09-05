## 15.6 Caso simulato/composito — Aurora Home: dal margine in calo a una decisione difendibile

> **Nota editoriale:** Aurora Home è un caso simulato/composito. Organizzazione, numeri e sequenza sono costruiti per mostrare come usare un Decision Record end-to-end.

Aurora Home è un retailer omnicanale. Il margine lordo trimestrale scende dal 32,8% al 29,9% e il COO apre il meeting con una diagnosi già pronta: “Stiamo scontando troppo. Riduciamo le promozioni Furniture.”

È una spiegazione plausibile, ma contiene già una decisione prima che l'analisi abbia separato finding, diagnosis, alternative e choice.

Il team riformula quindi la domanda. Non “perché il margine è sceso?”, ma:

> **Quale intervento sul business Furniture recupera contribution margin con il minor downside accettabile nei prossimi due trimestri?**

Decision owner: COO + Commercial Director. Deadline: due settimane, prima della pianificazione Q4. L'obiettivo primario è recuperare almeno **1,5 punti di contribution margin Furniture entro due trimestri**. I guardrail sono altrettanto espliciti: conversion complessiva non oltre -3%, nessun deterioramento materiale dell'NPS, nessuna ripiattaformazione logistica completa nel trimestre e budget implementativo massimo di €750k per la prima fase.

Questi vincoli fanno già parte dell'analisi: un'opzione che li viola non merita una stima raffinata del beneficio.

### Il primo finding restringe il problema, ma non identifica ancora la leva

Il gross margin è sceso di 2,9 punti percentuali e il dato è riconciliato con Finance. La decomposizione mostra che Furniture spiega il 61% del deterioramento. Questo è materiale e decision-relevant.

La prima ipotesi del COO, però, non regge da sola. Le promozioni Furniture sono aumentate, ma il net selling price medio è sceso soltanto dell'1,2%. La dinamica non basta a spiegare la maggior parte della compressione del margine.

Una decomposizione più profonda porta a due componenti più forti. Sul **product cost**, il costo medio di acquisto è salito del 4,8%, con gran parte dell'aumento concentrata su 15 SKU ad alto volume e una combinazione di cambio e nuovi termini fornitore. Sulla **logistica**, il costo medio degli ordini bulky è passato da €42 a €58 mentre la share bulky è cresciuta dal 18% al 27%; alcuni ordini a basso AOV diventano marginalmente negativi dopo fulfilment.

Le promozioni contribuiscono, ma non dominano più la spiegazione. Il finding si trasforma quindi in un insight più utile:

> **Il deterioramento è soprattutto la combinazione di aumento dei costi di acquisto su pochi SKU ad alto volume e crescita del mix bulky con fulfilment più costoso. Un taglio promozionale generalizzato colpirebbe anche ordini in cui la promozione non è il driver principale.**

Il claim resta calibrato: la decomposizione descrittiva è forte; la causalità completa su elasticità e volume non è ancora identificata; l'evidenza è però sufficiente per costruire alternative e test reversibili.

### La longlist impedisce alla prima soluzione di diventare il confronto

Prima di stimare l'opzione preferita, il team costruisce una longlist:

```text
A — business as usual
B — taglio generalizzato delle promozioni Furniture
C — surcharge logistico su bulky sotto una soglia economica
D — soglia free-shipping differenziata per bulky
E — rinegoziazione / dual sourcing sui 15 SKU
F — restringere assortimento bulky a contribution margin negativo
G — combinazione C + E con rollout graduale
```

Dopo aver applicato i vincoli restano B, C, E e G.

| Dimensione | B: taglio promo | C: surcharge mirato | E: fornitori | G: C + E |
|---|---|---|---|---|
| upside | alto se volume regge | medio | medio-alto | alto |
| evidenza | bassa-media | media-alta | media | media-alta |
| time to value | rapido | rapido | lento | misto |
| reversibilità | alta | alta | media | media-alta |
| downside | conversion/volume | conversion su bulky | supply risk | più complesso |
| costo iniziale | basso | basso-medio | medio | medio |

La tabella non produce un vincitore automatico. Mostra però perché B è fragile: il suo upside dipende dall'assunzione meno difendibile, cioè che il volume regga dopo il taglio promozionale.

### Le switching conditions trasformano l'incertezza in un piano di misura

Per C, il surcharge perde attrattività se la riduzione di conversion sugli ordini interessati supera il valore recuperato in contribution margin. Per E, la rinegoziazione perde priorità se il saving sui 15 SKU scende sotto il costo e l'opportunity cost di switching/qualifica fornitori. G resta preferibile se la leva C produce valore nel breve senza oltrepassare il guardrail conversion mentre E conserva un saving credibile nel medio termine.

Non tutte queste soglie sono note con precisione prima del test. Proprio per questo servono: indicano **quali variabili devono essere misurate per poter cambiare idea**.

Analytics raccomanda G: pilotare un surcharge selettivo sugli ordini bulky economicamente fragili, evitare un taglio promozionale generalizzato, aprire rinegoziazione/dual sourcing sui 15 SKU più rilevanti e introdurre contribution margin per ordine — fulfilment incluso — come metrica decisionale.

G batte B perché interviene sui driver meglio localizzati, preserva più volume promozionale, combina una leva rapida e reversibile con una strutturale e compra informazione sulla price sensitivity del surcharge.

### La decisione finale incorpora un vincolo operativo che l'analisi non deve nascondere

Il COO approva la recommendation con una modifica: il pilot surcharge parte su **due mercati**, non quattro. Operations non ha capacità di gestire contemporaneamente modifiche di fulfilment e pricing in quattro paesi.

Il Decision Record conserva la differenza:

```text
analytics recommendation:
2–4 market pilot + supplier action

chosen decision:
2 market pilot + supplier action

reason for difference:
operational capacity constraint
```

La decisione finale non smentisce l'analisi. Aggiunge un vincolo legittimo del decision owner e ne lascia traccia.

### Il learning contract chiude il ciclo

Il pilot misura contribution margin per visitor, conversion rate, AOV, cancellation, customer complaints, mix bulky e repeat behavior degli utenti esposti. I guardrail sono operativi:

```text
conversion delta < -3% → review immediata
complaints oltre soglia → review
contribution margin per visitor non migliora → stop
```

Il primo health check avviene dopo 7 giorni; la decision review dopo 4 settimane.

Prima del rollout il team esegue anche un rapido pre-mortem assumendo che, tra quattro settimane, il pilot sia fallito. Le cause candidate includono conversion molto peggiore del previsto, spostamento verso competitor, mix di mercati poco comparabile, allocazione errata dei costi logistici, compensazioni manuali del surcharge tramite voucher e una rinegoziazione fornitori molto più lenta. Queste ipotesi non diventano “rischi da slide”: generano nuovi controlli nel learning contract.

La diagnosi iniziale era:

```text
margin down
→ promotions too aggressive
→ cut promotions
```

Il processo finale è:

```text
Decision
→ objective + constraints
→ finding
→ decomposition
→ alternatives incl. BAU
→ value / downside / reversibility
→ switching assumptions
→ recommendation
→ owner decision
→ learning contract
```

Il Decision Record sintetico è:

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
