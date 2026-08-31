# 17.12 Checklist ed esercizi: affrontare un caso end-to-end

Questo capitolo non va memorizzato come una collezione di ricette.

L'obiettivo è allenare la capacità di costruire un percorso analitico quando il problema arriva incompleto, ambiguo e mescola più fenomeni.

## Checklist end-to-end

Prima di concludere un'analisi complessa, verificare:

### Problema e decisione

- Quale decisione deve essere presa?
- Chi è il decision maker?
- Qual è la scadenza?
- Cosa succede se non facciamo nulla?
- Quali alternative reali sono disponibili?

### Dati

- Il grain è corretto?
- Le metriche sono riconciliate?
- Freschezza e completezza sono sufficienti?
- Ci sono cambi di tracking, definizioni o processi?
- I confronti usano periodi e popolazioni coerenti?

### Analisi

- Abbiamo separato aggregato, segmenti e coorti?
- Abbiamo verificato mix shift?
- Abbiamo distinto correlazione e causalità?
- Abbiamo cercato ipotesi alternative?
- Abbiamo quantificato l'incertezza?
- Il modello o il forecast è valutato sulla decisione che deve supportare?

### Economia

- Qual è l'effetto su revenue, costo, margine o rischio?
- Il denominatore economico è quello corretto?
- I costi sono simmetrici?
- La soluzione crea effetti collaterali?
- Quali guardrail servono?

### Decisione

- L'evidenza è sufficiente per agire?
- Possiamo fare un test o un rollout reversibile?
- Qual è il threshold che cambierebbe la scelta?
- Quali condizioni richiedono stop o escalation?

### Comunicazione

- Stiamo distinguendo fatti, inferenze e ipotesi?
- La raccomandazione è proporzionata alla qualità dell'evidenza?
- Il management può capire cosa resta incerto?
- Abbiamo detto come misureremo l'esito?

## Esercizio 1 — Revenue cresce, cash peggiora

Un'azienda B2B SaaS riporta:

- ARR +18%;
- new logo +27%;
- cash collection -9%;
- DSO da 47 a 66 giorni;
- churn stabile.

Il CFO chiede:

> “Perché la crescita non si vede nella cassa?”

Costruire un piano di analisi che consideri almeno:

- billing terms;
- annual vs monthly contracts;
- invoice timing;
- collections;
- customer mix;
- discounts;
- revenue recognition vs cash.

Non partire da uno strumento. Partire dalle ipotesi.

## Esercizio 2 — Conversione in calo dopo una release

Dopo una release mobile:

- checkout conversion -4,2%;
- crash rate +0,3 pp;
- traffic mix invariato;
- Android stabile;
- iOS -7,1%;
- payment failures +5%.

Progettare l'investigazione.

Quali dati servono per distinguere:

- bug UI;
- provider payment;
- release rollout;
- tracking problem;
- mix device/version?

## Esercizio 3 — Campagna apparentemente eccezionale

Una campagna mostra ROAS 6,4.

Ma:

- il 72% dei convertiti era già cliente;
- il canale branded search cresce nello stesso periodo;
- non esiste holdout;
- la campagna viene mostrata più spesso agli utenti più attivi.

Spiegare perché attribution e incrementality non coincidono e proporre un disegno migliore.

## Esercizio 4 — Forecast “più preciso” ma peggiore

Due forecast di domanda:

- A: MAE 920 unità;
- B: MAE 1.040 unità.

A sottostima però i picchi; B li sovrastima leggermente.

Il costo di stock-out è quattro volte il costo di overstock per unità.

Quale modello preferire? Quali informazioni mancano prima di decidere?

## Esercizio 5 — Churn model

Un modello identifica 20.000 clienti ad alto rischio.

Il team retention può contattarne solo 4.000.

Come costruire una priorità migliore del semplice ordinamento per churn probability?

Considerare:

- valore cliente;
- costo intervento;
- probabilità di risposta;
- effetto incrementale;
- capacità operativa.

## Esercizio finale — Il caso senza etichetta

Un marketplace osserva contemporaneamente:

- ordini +9%;
- margin/order -14%;
- NPS -6 punti;
- nuovi seller +35%;
- refund rate +2,1 pp;
- delivery time +0,6 giorni;
- marketing spend +22%.

Il CEO chiede:

> “La crescita è sana?”

Preparare un analytical brief completo con:

1. definizione della decisione;
2. ipotesi ordinate;
3. dati necessari;
4. controlli di qualità;
5. decomposizioni;
6. segmentazioni;
7. eventuali analisi causali;
8. unit economics;
9. esperimenti o rollout;
10. executive summary atteso.

## Chiusura del capitolo

I casi di questo capitolo hanno attraversato domini molto diversi, ma la struttura profonda è rimasta sorprendentemente stabile:

**Problema → Definizione → Dati → Verifica → Decomposizione → Ipotesi → Metodo → Evidenza → Economia → Decisione → Azione → Misurazione**

Questa catena è più importante di qualunque singolo strumento.

Un analista maturo non riconosce soltanto modelli nei dati.

Riconosce **quale tipo di evidenza manca** prima che un'organizzazione possa decidere bene.

> **La tecnica è una componente dell'analisi. La decisione è il suo punto di arrivo.**
