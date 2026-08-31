# 17.5 Caso end-to-end: supply chain, stock-out e decisioni sotto vincoli

Un produttore di componentistica, **Aster Components**, vede aumentare gli stock-out e contemporaneamente il capitale immobilizzato in inventario.

Il COO chiede:

> “Come possiamo avere più stock-out se abbiamo più inventario?”

È il tipo di domanda che sembra contraddittoria finché non si guarda la distribuzione.

## 1. Aggregati che nascondono squilibri

L'inventario totale è +14% YoY.

Ma per SKU emerge che:

- alcuni articoli lenti accumulano scorte;
- alcuni componenti critici hanno service level insufficiente;
- la variabilità dei lead time è aumentata;
- i forecast error sono molto diversi per famiglia prodotto.

La quantità totale di stock quindi non rappresenta la disponibilità dello stock giusto, nel posto giusto e nel momento giusto.

## 2. Definire le metriche operative

Il team distingue:

- inventory value;
- days of inventory;
- fill rate;
- stock-out rate;
- order cycle time;
- forecast bias;
- forecast error;
- supplier lead-time variability;
- lost-sales estimate.

Un aumento dell'inventory value può convivere perfettamente con un peggioramento del fill rate.

## 3. ABC/XYZ e criticità

Gli SKU vengono segmentati non soltanto per valore, ma per:

- volume;
- variabilità della domanda;
- criticità produttiva;
- sostituibilità;
- lead time;
- concentrazione del supplier.

Il problema è particolarmente grave in 37 componenti che rappresentano una piccola parte del valore inventariale ma possono bloccare linee di produzione molto più costose.

## 4. Forecast ≠ inventory policy

Il team scopre anche un errore organizzativo: il forecast point estimate viene usato quasi direttamente come piano di riordino.

Ma la decisione di safety stock dipende anche dall'incertezza.

Due SKU possono avere domanda media 1.000 unità al mese, ma richiedere scorte molto diverse se uno è stabile e l'altro estremamente volatile.

## 5. Caso reale documentato: BMW Group

AWS documenta un caso in cui BMW Group affrontò le difficoltà create dalla shortage globale di semiconduttori costruendo, insieme ad AWS Professional Services, una piattaforma analitica che integrava dati di produzione, mercato e input dei supplier. Il caso è particolarmente utile perché mostra come il problema supply-chain non sia semplicemente “prevedere la domanda”: bisogna combinare vincoli produttivi, disponibilità dei componenti e allocazione tra mercati.

Fonte: https://aws.amazon.com/solutions/case-studies/bmw-reinvent-2023-analytics/

## 6. Un secondo caso reale: Coca-Cola Andina

AWS documenta inoltre il caso di Coca-Cola Andina, che ha usato una data platform e un'applicazione interna per migliorare visibilità su inventario, distribuzione e delivery attraverso più paesi.

Fonte: https://aws.amazon.com/solutions/case-studies/coca-cola-andina-analytics-case-study/

La lezione per l'analista è importante: supply chain analytics collega domanda, inventario, capacità, trasporto e servizio al cliente. Ottimizzare una sola metrica può peggiorare il sistema complessivo.

## 7. Decisione

Aster Components non aumenta semplicemente lo stock totale.

Introduce:

- safety stock differenziato per variabilità e criticità;
- revisione dei reorder point;
- supplier monitoring sui componenti critici;
- scenari per lead-time shock;
- riduzione dello stock su articoli lenti;
- forecast bias review per famiglia;
- alert sulle parti capaci di bloccare la produzione.

## 8. Misurazione

Il successo viene valutato con una scorecard bilanciata:

- fill rate;
- stock-out rate;
- inventory value;
- working capital;
- expedite cost;
- production downtime;
- forecast accuracy e bias;
- supplier lead-time reliability.

> **La supply chain non si ottimizza massimizzando lo stock o minimizzandolo. Si gestisce bilanciando servizio, capitale, rischio e variabilità.**
