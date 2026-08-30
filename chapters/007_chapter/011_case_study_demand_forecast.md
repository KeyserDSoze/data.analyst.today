## 7.10 Caso studio completo: il forecast che sembrava eccellente e costava milioni

Una catena europea di elettronica di consumo utilizza un forecast settimanale per pianificare gli acquisti di circa 8.000 SKU distribuiti tra negozi fisici ed e-commerce.

Il nuovo modello viene presentato come un successo: il MAPE medio scende dal 18,4% al 12,7%.

Il rollout parte a febbraio.

Tre mesi dopo, però, emergono due segnali inattesi:

- stock-out in crescita sui prodotti ad alta marginalità;
- capitale immobilizzato in crescita sui prodotti a bassa rotazione.

La domanda del CFO è semplice:

> "Com'è possibile che il forecast sia migliorato mentre l'inventario è peggiorato?"

### Primo livello: il KPI aggregato

Il team aveva confrontato i modelli su un'unica metrica media.

Su 8.000 SKU:

- 6.700 sono prodotti a bassa rotazione;
- 1.100 sono prodotti intermedi;
- 200 generano quasi il 44% del margine.

Il nuovo modello migliora molto sui 6.700 SKU semplici e peggiora leggermente sui 200 critici.

Poiché ogni SKU pesa allo stesso modo nel MAPE medio, il miglioramento sui prodotti meno importanti domina il KPI.

### Secondo livello: l'orizzonte di previsione

Il modello viene poi valutato separatamente a 1, 2, 4 e 8 settimane.

| Orizzonte | Vecchio modello MAE | Nuovo modello MAE |
|---|---:|---:|
| 1 settimana | 31 | 24 |
| 2 settimane | 46 | 39 |
| 4 settimane | 63 | 67 |
| 8 settimane | 89 | 112 |

Il nuovo modello è migliore sul breve periodo ma peggiore proprio sull'orizzonte usato dagli acquisti internazionali, che richiedono lead time lunghi.

### Terzo livello: promozioni

Il team scopre poi che circa il 60% degli errori più costosi si concentra nelle settimane promozionali.

La ragione è operativa: le promozioni vengono decise sei settimane prima, ma il dataset usato per il forecast contiene la variabile promozionale solo quando la campagna viene pubblicata sui sistemi commerciali, circa dieci giorni prima del lancio.

Il modello, quindi, non ha accesso a un'informazione che l'azienda possiede già.

Questo non è un problema di algoritmo. È un problema di architettura informativa.

### Quarto livello: anomalie apparenti

Un picco di vendite su una categoria di cuffie viene inizialmente classificato come anomalia. L'analista incrocia il calendario commerciale e scopre che coincide con il lancio di una console molto attesa.

L'evento non è rumore. È informazione di contesto non rappresentata nel modello.

### La soluzione

Il team cambia approccio:

1. introduce metriche di errore pesate per margine e costo di stock-out;
2. valuta i modelli per orizzonte di forecast;
3. confronta sempre il modello con una baseline seasonal-naive;
4. integra il calendario promozionale pianificato;
5. crea segmenti separati per fast mover, slow mover e prodotti critici;
6. introduce intervalli di previsione;
7. definisce alert quando la distribuzione degli errori cambia significativamente.

Dopo quattro mesi il MAPE complessivo non migliora molto: passa dal 12,7% al 12,3%.

Ma gli stock-out sui 200 SKU più importanti diminuiscono del 21%, e il capitale immobilizzato sui slow mover scende del 9%.

### La lezione

Se il team avesse ottimizzato ancora il MAPE globale, avrebbe probabilmente continuato a migliorare il numero sbagliato.

Il lavoro analitico corretto è stato invece collegare:

**errore statistico → tipo di prodotto → orizzonte → costo operativo → decisione**.

> **Il forecast migliore non è quello con la metrica più bella. È quello che riduce meglio il costo dell'incertezza nella decisione reale.**
