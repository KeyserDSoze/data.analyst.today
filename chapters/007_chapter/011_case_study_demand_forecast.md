## 7.10 Caso end-to-end: il forecast che migliorava la metrica e peggiorava la decisione

Il forecasting diventa utile quando smette di essere valutato come esercizio di accuratezza astratta e viene inserito nel processo che usa la previsione. Il caso seguente è **simulato/composito** e mostra un problema frequente in retail e supply chain: migliorare l'errore medio e, contemporaneamente, peggiorare il costo operativo.

### ElectroOne: il modello “migliore” che crea più problemi

**ElectroOne** è una catena europea di elettronica di consumo con negozi fisici ed e-commerce. Il forecast settimanale serve a pianificare gli acquisti di circa **8.000 SKU**. Il nuovo modello viene presentato come un successo perché il MAPE passa da **18,4%** a **12,7%**.

Il rollout parte a febbraio. Tre mesi dopo, però, il CFO vede crescere gli stock-out sui prodotti ad alta marginalità, il capitale immobilizzato sugli slow mover e le richieste di expedite shipping. La domanda diventa inevitabile:

> **Come può il forecast essere migliorato mentre l'inventario peggiora?**

La prima risposta emerge dal **series contract**. Il modello prevede a grain `SKU × paese × settimana`, ma gli ordini internazionali hanno lead time molto diversi: **1–2 settimane** per fornitori locali, **4–5** per distribuzione europea, **8–10** per alcuni prodotti importati. Una sola accuracy media sta quindi comprimendo decisioni prese a orizzonti differenti.

Il team ricostruisce allora il backtest includendo seasonal naïve, vecchio modello e nuovo modello. Nel totale, la nuova soluzione batte il seasonal naïve. Su alcuni slow mover il vantaggio è minimo; in categorie molto stagionali la baseline semplice rimane competitiva. La domanda non è più “nuovo modello sì o no?”, ma **dove la complessità aggiunge davvero informazione?**

### La media globale nasconde il valore economico

Gli 8.000 SKU non hanno lo stesso peso. Circa **6.700** sono slow mover, **1.100** hanno comportamento intermedio e appena **200 SKU critici generano circa il 44% del margine**. Il nuovo modello migliora molto sui 6.700 prodotti semplici e peggiora leggermente proprio sui 200 critici.

Il MAPE medio è corretto, ma assegna implicitamente importanza a errori che il business non considera equivalenti. La metrica sta descrivendo bene l'errore e male la decisione.

La separazione per horizon rende il problema ancora più evidente:

| Horizon | Vecchio modello MAE | Nuovo modello MAE |
| --- | ---: | ---: |
| 1 settimana | 31 | 24 |
| 2 settimane | 46 | 39 |
| 4 settimane | 63 | 67 |
| 8 settimane | 89 | 112 |

Il nuovo modello è migliore a breve e peggiore esattamente dove vengono presi molti degli acquisti critici. L'accuracy aggregata premiava soprattutto un orizzonte che non governava la parte più costosa del processo.

### L'informazione esisteva, ma non arrivava al forecast origin

Circa il **60% degli errori più costosi** coincide con settimane promozionali. La promozione, però, viene approvata internamente sei settimane prima e compare nella feature `promotion_flag` soltanto quando viene pubblicata nel sistema commerciale, circa dieci giorni prima.

Il business conosce già un'informazione utile. La pipeline del modello non la rende disponibile all'horizon in cui procurement deve agire. Non è principalmente un problema di algoritmo: è un problema di **information architecture**.

Lo stesso errore di interpretazione emerge quando un picco nelle cuffie viene classificato come anomalia e poi “smussato”. Il calendario commerciale mostra che coincide con il lancio di una console molto attesa. Il picco non è rumore da eliminare: è domanda reale e, se il modello ricevesse l'informazione corretta, anche prevedibile.

### Dall'accuracy alla business loss

ElectroOne ridefinisce la funzione di valutazione includendo margine perso per stock-out, expedite shipping, costo del capitale immobilizzato, markdown atteso e lead time. Un errore di 100 unità su un accessorio a basso margine non viene più trattato come equivalente a 100 unità su una console critica.

Il ranking dei modelli cambia.

Anche la policy di ordine cambia. Per gli SKU a lungo lead time procurement non usa più automaticamente il point forecast: considera prediction interval, costo di stock-out, costo di overstock, lead time e possibilità di riordino. Forecast e decisione di inventory vengono finalmente separati.

Il monitoraggio viene poi disegnato per osservare il sistema che conta davvero: MAE e MASE per horizon, bias, P90 dell'errore, coverage degli intervalli, business loss, performance sui 200 SKU critici, rapporto tra modello e seasonal naïve, promozioni e nuovi prodotti. Se la baseline torna a battere il modello per più finestre consecutive in un segmento materiale, viene aperta una revisione.

### Il risultato del redesign

Nel caso composito, dopo quattro mesi:

- MAPE globale: **12,7% → 12,3%**;
- stock-out sui 200 SKU critici: **-21%**;
- capitale immobilizzato sugli slow mover: **-9%**;
- expedite shipping: **-14%**.

Il numero celebrato inizialmente cambia pochissimo. Le decisioni migliorano molto di più. È precisamente il punto del caso.

### Temporal Decision Brief — ElectroOne

| Campo | Evidenza |
| --- | --- |
| Serie | domanda settimanale `SKU × paese` |
| Decisione | replenishment e acquisti con lead time 1–10 settimane |
| Baseline | seasonal naïve |
| Struttura | forte stagionalità e impatto promozionale/categoria |
| Anomaly triage | eventi di lancio non vanno trattati automaticamente come rumore |
| Horizon critico | 4–8 settimane per acquisti internazionali |
| As-of issue | promotion plan disponibile al business prima che alla feature pipeline |
| Accuracy | nuovo modello forte a 1–2 settimane, debole a 4–8 |
| Segmento critico | 200 SKU = ~44% del margine |
| Business loss | stock-out, expedite, capitale, markdown |
| Incertezza | prediction interval usati nella policy di ordine |
| Monitoring | model vs baseline, bias, P90 error, coverage, loss |
| Condition of validity | calendario promo e product launch devono essere disponibili/aggiornati |
| Decisione | modello usato per segmento/horizon, non come vincitore globale unico |

La domanda iniziale era “quale modello ha il MAPE migliore?”. Dopo l'analisi, la domanda corretta diventa:

> **Quale sistema di previsione riduce meglio il costo dell'incertezza sugli SKU e sugli orizzonti che governano le nostre decisioni?**

Il percorso del capitolo converge qui: **errore statistico → segmento → horizon → informazione as-of → uncertainty → business loss → decisione**.

> **Il forecast migliore non è quello che vince una classifica di metriche. È quello che rende meno costosi gli inevitabili errori del futuro.**
