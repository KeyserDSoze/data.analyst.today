## 17.1 Caso end-to-end: “Le vendite stanno scendendo”
Una catena retail multicanale, **Orion Living**, chiude il mese con ricavi a -11,2% rispetto allo stesso mese dell'anno precedente.

Il CEO chiede:

> “È un problema di domanda, prezzo o execution?”

La tentazione è partire subito con una dashboard. Un buon analista parte invece dal framing.

## 1. Definire il fenomeno

“Vendite” può significare almeno:

- ordini;
- pezzi;
- gross sales;
- net sales;
- revenue riconosciuta;
- contribution margin.

Il primo controllo mostra che il -11,2% riguarda **net sales**, non volumi.

## 2. Decomporre il delta

L'analista separa il problema in:

- traffico;
- conversione;
- unità per ordine;
- prezzo medio;
- mix prodotto;
- resi e cancellazioni.

I risultati:

- sessioni: -2,1%;
- conversione: -0,4 pp;
- unità per ordine: stabile;
- prezzo medio: +3,8%;
- return rate: 7,4% → 10,9%.

Il problema non è quindi semplicemente “meno domanda”.

## 3. Cercare dove si concentra il deterioramento

Per canale:

| Canale | Net sales YoY |
|---|---:|
| Store | -3,1% |
| Web desktop | -5,4% |
| Mobile app | -24,8% |

Per categoria, il calo maggiore è nell'arredo voluminoso. Per device, si concentra su iOS. Per geografia, il 64% del delta arriva da tre mercati.

## 4. Verificare data quality prima della spiegazione

Il team nota un'anomalia: i resi iOS sono aumentati soprattutto dopo una nuova release.

Ma prima di concludere che la release abbia causato il problema, vengono controllati:

- completeness degli eventi;
- definizione del return rate;
- versioni app realmente installate;
- date ordine, spedizione e reso;
- eventuali cambiamenti nelle policy di reso.

Si scopre che il tracking è corretto, ma nello stesso periodo è stata estesa la finestra di reso da 30 a 45 giorni in due mercati.

Quindi parte del confronto YoY non è semanticamente omogeneo.

## 5. Costruire ipotesi concorrenti

Le principali ipotesi diventano:

1. peggioramento del prodotto/app;
2. politica di reso più permissiva;
3. mix verso categorie con più resi;
4. deterioramento logistico su articoli bulky;
5. combinazione dei fattori.

## 6. Separare composizione e performance

Standardizzando il mix prodotto e usando finestre di reso comparabili, il deterioramento reale del return rate scende da +3,5 pp a circa +1,4 pp.

Ulteriori analisi mostrano che:

- 0,8 pp sono concentrati sugli ordini bulky;
- 0,4 pp sono associati alla nuova esperienza iOS;
- il resto è diffuso.

Nel segmento bulky, i tempi medi di consegna sono aumentati di 1,7 giorni e i resi per “prodotto danneggiato” sono saliti nettamente.

## 7. Insight

Il finding iniziale era:

> “Le vendite sono -11,2%.”

L'insight diventa:

> “La maggior parte del deterioramento dei net sales non deriva da una contrazione generalizzata della domanda. È spiegata da maggiore incidenza dei resi, soprattutto negli ordini bulky, dove il peggioramento logistico e una parte del rollout iOS hanno ridotto il valore netto degli ordini.”

## 8. Decisione

Non viene lanciato uno sconto generalizzato.

Le azioni sono:

- audit dei carrier bulky nei tre mercati critici;
- rollback controllato di una componente iOS;
- monitoraggio separato di gross sales, returns e net sales;
- confronto con finestre di reso omogenee;
- test su packaging e carrier per gli SKU più danneggiati.

## 9. Misurazione

Il decision record definisce:

- return rate bulky;
- damage-related return rate;
- delivery lead time;
- net sales per session;
- conversion rate iOS;
- guardrail su customer complaints.

La lezione è che una domanda apparentemente semplice richiede spesso di attraversare quasi tutto il mestiere dell'analista:

**semantica → qualità → segmentazione → decomposizione → temporalità → ipotesi → verifica → decisione**.

> **Non chiedere soltanto “quanto è sceso?”. Chiedi quale meccanismo ha trasformato il comportamento operativo in quel numero.**
