## 17.7 “Quante persone dobbiamo pianificare lunedì?”

### Caso simulato/composito: Arcadia Parcel

**Arcadia Parcel** gestisce 38 hub logistici e deve pianificare il personale per il lunedì successivo.

Il team di Data Science presenta due forecast dei colli giornalieri:

- modello A: MAPE `6,8%`;
- modello B: MAPE `7,4%`.

La conclusione sembra ovvia: A è migliore.

L'operations manager però segnala un problema.

Nei giorni di picco il modello A tende a sottostimare sistematicamente. E proprio lì l'errore costa di più.

La domanda reale non è:

> “Quale forecast ha errore medio minore?”

È:

> **“Con quanta capacità dobbiamo impegnarci oggi per minimizzare il costo atteso di lunedì?”**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | staffing e contractor capacity per hub |
| Failure cost | understaffing → overtime, SLA, backlog; overstaffing → ore inutilizzate |
| Claim necessario | predittivo + decision economics |
| Reversibilità | diminuisce avvicinandosi al giorno operativo |
| Incertezza critica | coda alta della domanda, non soltanto errore medio |
| Stop rule | non scegliere il modello sulla sola MAPE |

## 1. La loss function del modello non è necessariamente quella del business

Supponiamo che:

- un'ora di capacità inutilizzata costi circa `€24`;
- un'ora di capacità mancante nei picchi generi in media `€67` tra overtime, ritardi e penali.

Gli errori non sono simmetrici.

Una metrica media che tratta `+1.000` e `-1.000` unità come errori equivalenti non rappresenta bene la decisione.

Il **Temporal Decision Brief** deve quindi registrare:

- orizzonte;
- decisione collegata;
- costo di overforecast;
- costo di underforecast;
- quantili rilevanti;
- eventuali vincoli minimi/massimi di capacità.

## 2. Dal point forecast alla distribuzione

Per Milano Hub 3 il forecast diventa:

- P10: `74.000` colli;
- P50: `82.000`;
- P90: `94.000`.

Il team smette di trattare `82.000` come “il futuro”.

È una stima centrale dentro una distribuzione.

Nei periodi in cui l'understaffing è molto costoso può essere razionale pianificare su un percentile superiore al P50.

Non perché il P90 sia “più preciso”, ma perché la funzione di costo rende conveniente una posizione più prudente.

## 3. Forecast accuracy e decision loss

Il team introduce due livelli di valutazione.

### Model quality

- MAE;
- bias;
- calibration degli intervalli;
- performance per hub e regime;
- errore sui picchi.

### Decision quality

- overtime cost;
- idle labor cost;
- SLA penalty;
- backlog spillover;
- contractor premium;
- cost per parcel.

Il modello B, pur avendo MAPE medio peggiore, produce un piano operativo con costo atteso inferiore nei giorni critici.

Questa è una lezione generale:

> **un modello può essere inferiore secondo una metrica statistica e superiore secondo la decisione che deve supportare.**

## 4. Orizzonti diversi, decisioni diverse

Arcadia usa quattro orizzonti:

| Orizzonte | Decisione |
|---|---|
| 8 settimane | workforce planning e contratti |
| 14 giorni | turni, contractor, ferie |
| 48 ore | fine tuning operativo |
| intra-day | riallocazione tra hub e backlog management |

Pretendere un unico forecast per tutte le decisioni crea falsa semplicità.

A otto settimane contano scenario e capacità strutturale.

A 48 ore possono contare weather, backlog, preorder e segnali operativi recenti.

Il **dato giusto** cambia con l'orizzonte.

## 5. Un forecast può diventare inutile dopo un cambio di regime

Il team definisce anche eventi che invalidano o degradano il forecast:

- sciopero;
- chiusura hub;
- nuova partnership commerciale;
- meteo estremo;
- promozione non presente nel training;
- cambio di cut-off operativo.

In questi casi il sistema non deve continuare a mostrare lo stesso numero con la stessa fiducia.

Può passare a:

- scenario manuale;
- intervallo più ampio;
- modello fallback;
- override documentato.

Questa è una **stop/degrade condition**, non un fallimento da nascondere.

## Caso pubblico documentato: driver-based forecasting

AWS Cloud Financial Management descrive il **driver-based forecasting** come approccio che collega la previsione a driver futuri — per esempio lanci di prodotto, promozioni, nuovi utenti o cambi architetturali — invece di estrapolare soltanto il trend storico. La guida sottolinea anche l'importanza di documentare e rivedere le assunzioni quando emergono nuove informazioni.

Fonte: https://aws.amazon.com/blogs/aws-cloud-financial-management/understand-and-build-driver-based-forecasting/

Il dominio è cloud spend, ma il principio è generale:

> **una previsione operativa migliora quando i driver della decisione entrano esplicitamente nel modello o negli scenari.**

## 6. Decision Record

Arcadia confronta:

### A — Modello A + staffing sul P50

Migliore MAPE, ma sottostima i picchi e genera costi di shortage elevati.

### B — Modello B + staffing sul P50

Più prudente nei picchi, ma non usa ancora esplicitamente la funzione di costo.

### C — Forecast probabilistico + policy di capacità

- intervalli previsivi;
- percentile scelto in funzione dei costi;
- policy diversa per hub;
- contractor flessibili dove l'incertezza è più alta;
- override documentato per shock di regime;
- review del costo decisionale, non soltanto dell'errore.

La scelta è C.

## 7. Switching condition

La policy cambia se:

- il rapporto tra costo di under/overstaffing cambia;
- la disponibilità di contractor diminuisce;
- il forecast perde calibration;
- compare un nuovo driver operativo;
- il backlog cambia il volume effettivamente processabile.

Il forecast non viene separato dalla policy che lo consuma.

## 8. Decision Communication Pack

La headline non è:

> “Il modello B ha MAPE 7,4%.”

È:

> **“Il modello con errore medio minore sottostima i picchi, che sono gli errori più costosi. Proponiamo staffing basato sulla distribuzione prevista e sui costi asimmetrici, con percentile e flessibilità diversi per hub.”**

Il pack mostra:

1. distribuzione della domanda;
2. costo under/over;
3. expected cost per policy;
4. hub a rischio;
5. stop/degrade conditions.

## 9. Outcome review

Metriche:

- forecast bias e calibration;
- overtime;
- idle hours;
- SLA breaches;
- backlog;
- cost per parcel;
- contractor premium;
- differenza tra costo previsto e realizzato.

## Cosa abbiamo scelto di non fare

Non serve necessariamente il modello con architettura più sofisticata.

Non serve ottimizzare un decimo di punto di MAPE se la policy continua a usare male il forecast.

La catena effettiva è:

**Temporal Decision Brief → Uncertainty Brief → Decision Record → Decision Communication Pack**

con Data Readiness Review quando cambiano fonti o regime.

> **La metrica migliore per un forecast non è quella che premia il modello più elegante. È quella che ci aiuta a evitare gli errori più costosi della decisione.**
