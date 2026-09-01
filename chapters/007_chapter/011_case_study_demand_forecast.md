## 7.10 Caso end-to-end: il forecast che migliorava la metrica e peggiorava la decisione

Il forecasting diventa realmente utile quando smette di essere valutato come esercizio di accuratezza astratta e viene inserito nel processo che usa la previsione.

Il caso seguente è **simulato/composito**. I numeri sono costruiti per mostrare un problema frequente in retail e supply chain: migliorare l'errore medio e, contemporaneamente, peggiorare il costo operativo.

### Contesto — ElectroOne

**ElectroOne** è una catena europea di elettronica di consumo con negozi fisici ed e-commerce.

Il forecast settimanale serve a pianificare acquisti di circa 8.000 SKU.

Il nuovo modello viene presentato come un successo:

- MAPE vecchio modello: 18,4%;
- MAPE nuovo modello: 12,7%.

Il rollout parte a febbraio.

Tre mesi dopo il CFO osserva:

- stock-out in crescita sui prodotti ad alta marginalità;
- capitale immobilizzato in crescita sui slow mover;
- più richieste di expedite shipping.

La domanda è:

> **Come può il forecast essere migliorato mentre l'inventario peggiora?**

### 1. Series contract — che cosa stavamo davvero prevedendo?

Il modello produce forecast a grain:

`SKU × paese × settimana`

ma gli ordini internazionali vengono presi con lead time molto diversi:

- 1–2 settimane per fornitori locali;
- 4–5 settimane per distribuzione europea;
- 8–10 settimane per alcuni prodotti importati.

Il primo problema è quindi concettuale: il dashboard riporta una sola accuracy media per decisioni che operano su **horizon differenti**.

### 2. Baseline — il modello complesso batte davvero una regola semplice?

Il team ricostruisce il backtest con:

- seasonal naïve;
- vecchio modello;
- nuovo modello.

Sul totale degli SKU il nuovo modello batte il seasonal naïve.

Ma su alcuni segmenti slow mover la differenza è minima; per alcune categorie molto stagionali il seasonal naïve rimane competitivo.

Questo cambia la domanda da:

> nuovo modello sì/no?

A:

> dove la complessità aggiunge davvero informazione?

### 3. Segmentazione dell'errore — ogni SKU pesava allo stesso modo

Gli 8.000 SKU non hanno lo stesso valore operativo:

- 6.700 slow mover;
- 1.100 prodotti intermedi;
- 200 SKU critici che generano circa il 44% del margine.

Il nuovo modello migliora molto sui 6.700 prodotti semplici e peggiora leggermente sui 200 critici.

Il MAPE medio assegna loro un peso che non riflette la materialità economica.

Il KPI globale sta quindi dicendo la verità statistica e nascondendo la verità decisionale.

### 4. Horizon — il modello vince dove non compriamo

La performance viene separata per orizzonte:

| Horizon | Vecchio modello MAE | Nuovo modello MAE |
| --- | ---: | ---: |
| 1 settimana | 31 | 24 |
| 2 settimane | 46 | 39 |
| 4 settimane | 63 | 67 |
| 8 settimane | 89 | 112 |

Il nuovo modello è chiaramente migliore a breve.

Ma molti acquisti critici vengono decisi a 8 settimane.

La metrica aggregata premiava soprattutto un orizzonte che non governava la parte più costosa del processo.

### 5. As-of validation — il calendario promozionale arrivava troppo tardi nel dataset

Circa il 60% degli errori più costosi coincide con settimane promozionali.

Il team scopre che le campagne sono approvate internamente sei settimane prima, ma la feature `promotion_flag` appare nella tabella analitica solo quando la promozione viene pubblicata nel sistema commerciale, circa dieci giorni prima.

L'azienda possiede l'informazione. Il modello non la riceve in tempo per l'horizon più importante.

Non è principalmente un problema di algoritmo.

È un problema di **information architecture**:

> l'informazione utile esiste, ma non è disponibile al forecast origin.

### 6. Context anomaly — un lancio prodotto scambiato per rumore

Un picco di vendite nelle cuffie viene classificato come anomalia.

L'analista collega il calendario commerciale e scopre che coincide con il lancio di una console molto attesa.

Il picco non è un errore da smussare. È un evento di domanda reale e prevedibile se il modello riceve l'informazione corretta.

Questo evita una pratica pericolosa: “pulire” dal training proprio gli eventi che il business deve saper gestire.

### 7. Business loss — sotto e sovrastima non costano uguale

ElectroOne definisce una loss operativa per SKU che incorpora:

- margine perso per stock-out;
- costo di expedite shipping;
- costo di capitale dello stock;
- markdown atteso sull'invenduto;
- lead time.

Il ranking dei modelli cambia.

Un errore di 100 unità su un accessorio a basso margine non è più equivalente a un errore di 100 unità su una console critica.

### 8. Prediction intervals — il punto centrale non deve diventare quantità d'ordine automatica

Il nuovo processo introduce intervalli di previsione e probabilità di superare soglie di domanda.

Per gli SKU a lungo lead time, procurement non usa più automaticamente la media prevista.

La quantità d'ordine dipende anche da:

- costo stock-out;
- costo overstock;
- lead time;
- possibilità di riordino;
- ampiezza dell'intervallo.

Forecast e inventory policy vengono finalmente separati.

### 9. Monitoring — quando il modello smette di battere la baseline

Il team monitora:

- MAE e MASE per horizon;
- bias;
- error P90;
- coverage degli intervalli;
- loss economica;
- performance dei 200 SKU critici;
- rapporto model vs seasonal naïve;
- promozioni e nuovi prodotti.

Se il modello perde contro la baseline per più finestre consecutive in un segmento materiale, viene aperta una revisione.

### 10. Risultato del redesign

Nel caso composito, dopo quattro mesi:

- MAPE globale: 12,7% → 12,3%;
- stock-out sui 200 SKU critici: -21%;
- capitale immobilizzato sui slow mover: -9%;
- expedite shipping: -14%.

Il numero più celebrato inizialmente — il MAPE — cambia pochissimo.

Le decisioni migliorano molto di più.

È esattamente il punto del caso.

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

### La lezione

La domanda iniziale era:

> Quale modello ha il MAPE migliore?

La domanda corretta è diventata:

> **Quale sistema di previsione riduce meglio il costo dell'incertezza sugli SKU e sugli orizzonti che governano le nostre decisioni?**

Il passaggio è fondamentale.

**Errore statistico → segmento → horizon → informazione as-of → uncertainty → business loss → decisione**.

> **Il forecast migliore non è quello che vince una classifica di metriche. È quello che rende meno costosi gli inevitabili errori del futuro.**
