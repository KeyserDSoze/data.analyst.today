# 14.9 AI per forecasting e modeling: generare modelli non significa validare previsioni

L'AI può costruire in pochi minuti una pipeline che un tempo richiedeva ore: pulizia, feature engineering, split, training, metriche e grafici. Il rischio è confondere la velocità di costruzione con la qualità del modello.

Supponiamo che un'azienda retail chieda:

> “Prevedi le vendite delle prossime otto settimane per 12.000 SKU.”

Un agente può provare automaticamente decine di modelli e restituire una leaderboard. Se il miglior risultato ha MAPE 8,2%, sembra naturale dichiararlo vincitore.

Ma prima dobbiamo sapere:

- lo split è temporale?
- esiste leakage da promozioni future già note nel dataset?
- gli SKU intermittenti sono trattati correttamente?
- il modello funziona anche durante festività e campagne?
- l'errore è accettabile dal punto di vista economico?
- le prediction interval sono calibrate?
- stiamo ottimizzando una metrica che riflette davvero il costo di stockout e overstock?

## Caso realistico: il forecast che migliora e peggiora il business

Un distributore di elettronica utilizza un agente AI per ottimizzare il forecast settimanale.

Vecchio sistema:

- MAE medio: 17,4 unità per SKU-settimana;
- stockout rate: 6,1%;
- inventory days: 41.

Nuovo modello AI:

- MAE: 13,2;
- stockout rate: 7,0%;
- inventory days: 46.

Statisticamente il forecast è migliore. Operativamente il sistema è peggiore.

L'indagine mostra che il modello migliora soprattutto sugli SKU ad alto volume, ma sottostima sistematicamente i prodotti a domanda intermittente e il planning engine reagisce aumentando safety stock su categorie a bassa marginalità.

Il problema non era il training. Era l'interazione tra forecast, segmentazione degli SKU e regole di inventory policy.

## AI come laboratorio di modelli

Un uso maturo dell'AI è trattarla come un laboratorio che propone rapidamente alternative:

1. baseline naive;
2. modello semplice interpretabile;
3. modello più complesso;
4. confronto temporale;
5. analisi errori per segmento;
6. stress test su periodi anomali;
7. valutazione economica;
8. monitoraggio post-deployment.

L'agente può automatizzare gran parte di questi passaggi. L'analista deve decidere quali test sono necessari e cosa significhi “abbastanza buono”.

## Modeling senza culto della leaderboard

Il modello migliore offline può non essere quello migliore in produzione. Possibili ragioni:

- costi di inferenza;
- latenza;
- dati non disponibili online;
- fragilità al drift;
- difficoltà di spiegazione;
- impossibilità di monitorare le feature;
- capacità operativa insufficiente per agire sui risultati.

**L'AI rende economico provare molti modelli. Proprio per questo dobbiamo diventare più severi nel decidere quali meritino di essere usati.**

### Fonte

- NIST AI RMF, measurement and evaluation: https://www.nist.gov/itl/ai-risk-management-framework
