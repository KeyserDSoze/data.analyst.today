# 17.7 Forecasting operativo: una previsione utile deve cambiare un'azione

Un forecast non è utile perché è accurato in astratto.

È utile se migliora una decisione che deve essere presa prima che il futuro sia noto.

## Caso composito: NorthRiver Logistics

NorthRiver gestisce 38 hub logistici e deve pianificare il personale per il lunedì successivo.

Il team usa un forecast dei colli giornalieri.

Storicamente la metrica usata per valutare il modello è MAPE.

Il modello A ha MAPE 6,8%.

Il modello B ha MAPE 7,4%.

Il team considera A migliore.

Ma l'operations manager segnala un problema: nei giorni di picco il modello A tende a sottostimare sistematicamente.

Questa sottostima è costosa perché produce:

- straordinari;
- ritardi;
- penali SLA;
- backlog che si trascina nei giorni successivi.

Il modello B ha errore medio leggermente peggiore ma distribuzione più prudente nei picchi.

## L'errore possibile: ottimizzare la metrica del modello invece della decisione

La domanda corretta non è:

> “Quale modello ha MAPE più basso?”

È:

> “Quale previsione produce il miglior piano operativo dati costi asimmetrici di overstaffing e understaffing?”

Se un'ora di personale inutilizzata costa €24 ma un'ora mancante nei picchi genera in media €67 tra overtime, ritardi e penali, gli errori non sono simmetrici.

Un forecast point-only nasconde questo problema.

## Dal point forecast alla distribuzione

Per ogni hub il team passa da una singola previsione a intervalli previsivi.

Esempio per Milano Hub 3:

- forecast centrale: 82.000 colli;
- P10: 74.000;
- P50: 82.000;
- P90: 94.000.

Il piano personale non viene più costruito automaticamente sul P50.

Nei periodi con forte costo di understaffing viene usato un percentile più alto.

## Decision threshold

La scelta può essere formalizzata come problema di costo atteso.

Per ogni possibile livello di staffing stimiamo:

- costo del personale;
- costo atteso di capacità mancante;
- costo di flessibilità last-minute;
- probabilità degli scenari.

Il valore del forecast è quindi nella sua integrazione con una funzione di decisione.

## Il forecast cambia anche per orizzonte

NorthRiver usa modelli diversi per:

- 8 settimane: workforce planning;
- 14 giorni: turni e contractor;
- 48 ore: fine tuning operativo;
- intra-day: riallocazione.

Pretendere un unico forecast per tutte le decisioni crea falsa semplicità.

## Caso pubblico: driver-based forecasting e unit economics

AWS descrive un approccio di driver-based forecasting in cui unit metrics vengono collegate ai driver di business per stimare costi futuri e utilizzo delle risorse. Nell'esempio, il costo per chiamata API viene usato per stimare l'impatto di milioni di chiamate aggiuntive e valutare alternative architetturali e operative. Il punto metodologico è importante: il forecast diventa utile quando collega volumi previsti, unit economics e decisioni concrete. 

Fonte: AWS Cloud Financial Management, *Understand and build driver-based forecasting*.

## Metodo operativo

Prima di valutare un forecast chiedere:

1. quale decisione anticipa;
2. quanto costa sovrastimare;
3. quanto costa sottostimare;
4. quale orizzonte serve;
5. se serve una distribuzione invece di un punto;
6. quali variabili esterne possono cambiare il regime;
7. come verrà misurato l'impatto operativo.

> **La metrica migliore per un forecast è spesso quella che riflette meglio il costo della decisione sbagliata.**
