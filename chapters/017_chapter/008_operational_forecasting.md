## 17.7 Arcadia Parcel — “Quante persone dobbiamo pianificare lunedì?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

Arcadia Parcel gestisce **38 hub logistici** e deve impegnare personale e contractor per il lunedì successivo. Il team Data Science presenta due forecast: modello A con MAPE **6,8%**, modello B con MAPE **7,4%**. Se la decisione fosse scegliere il modello con errore percentuale medio minore, A vincerebbe.

Operations però osserva che A sottostima sistematicamente proprio nei giorni di picco. E nei picchi l'errore costa molto di più. La decisione reale è quindi:

> **Con quanta capacità dobbiamo impegnarci oggi per minimizzare il costo atteso di lunedì?**

Qui il capstone può essere deliberatamente corto. Non ci serve una nuova famiglia di modelli; ci serve collegare il forecast alla loss function della decisione.

### La metrica del modello e la metrica del business non coincidono

Arcadia stima che un'ora di capacità inutilizzata costi circa **€24**, mentre un'ora di capacità mancante nei picchi generi in media circa **€67** tra overtime, backlog, ritardi e penali SLA. Overforecast e underforecast non sono quindi errori economicamente simmetrici.

Una MAPE media può trattare due errori della stessa magnitudine in modo equivalente. La policy operativa non può farlo.

Il Temporal Decision Brief registra perciò l'orizzonte, la decisione associata, il costo di over/under-capacity, i quantili rilevanti e i vincoli di staffing. Per Milano Hub 3 il point forecast viene sostituito dalla distribuzione che serve alla scelta:

```text
P10 = 74.000 colli
P50 = 82.000
P90 = 94.000
```

Pianificare sopra P50 nei giorni critici non significa credere che P90 sia “più accurato”. Significa accettare più rischio di capacità inutilizzata per ridurre un downside di understaffing molto più costoso.

### B può essere un modello peggiore e una decisione migliore

Il team continua a misurare MAE, bias, calibration degli intervalli, errori per hub/regime e performance sui picchi. Ma confronta anche il costo prodotto dalla policy: overtime, idle labor, SLA penalty, backlog spillover, contractor premium e cost per parcel.

Su questo secondo livello, il modello B — pur avendo MAPE 7,4% contro 6,8% — genera un piano con expected operational cost inferiore nei giorni critici. Il ranking dei modelli cambia perché abbiamo finalmente valutato **l'errore che il business paga**, non soltanto l'errore che la leaderboard conta.

Questa scoperta chiude quasi tutta la decisione. Non serve costruire un terzo modello più sofisticato per dimostrare il punto.

### Il forecast deve essere specifico della decisione e dell'orizzonte

Arcadia usa inoltre quattro finestre che corrispondono a quattro impegni diversi:

| Orizzonte | Decisione |
|---|---|
| 8 settimane | workforce planning e contratti |
| 14 giorni | turni, contractor, ferie |
| 48 ore | fine tuning operativo |
| intra-day | riallocazione tra hub e backlog management |

A otto settimane contano scenario e capacità strutturale; a 48 ore weather, backlog, preorder e segnali recenti possono diventare decisivi. “Il forecast” non è quindi un singolo prodotto universale. La disponibilità informativa e il costo di errore cambiano con il momento in cui dobbiamo agire.

AWS descrive il **driver-based forecasting** come un processo che collega la previsione a driver futuri — per esempio lanci, promozioni, nuovi utenti o cambiamenti architetturali — e richiede di aggiornare le assunzioni quando emergono nuove informazioni.[^aws-driver] Il dominio della fonte è cloud financial management, ma il principio trasferibile è lo stesso: un forecast operativo deve poter incorporare ciò che sappiamo che cambierà il sistema, invece di estrapolare passivamente il passato.

### Anche una buona previsione deve poter degradare

Sciopero, chiusura hub, nuova partnership, meteo estremo, promozione non presente nel training o cambio di cut-off possono rendere il regime corrente poco comparabile al validation history. In questi casi Arcadia non continua a mostrare lo stesso numero con la stessa fiducia. Può passare a intervallo più ampio, scenario manuale, fallback model o override documentato.

`DEGRADE` è un comportamento del sistema decisionale, non un'ammissione di sconfitta.

### La policy, non il modello, è il vero deliverable

Le opzioni finali sono semplici. Usare A e pianificare sul P50 massimizza la metrica media ma sottostima picchi costosi. Usare B sempre sul P50 corregge parte del bias senza incorporare esplicitamente economics. La policy preferita usa **forecast probabilistico + capacity rule**: percentile diverso per hub/regime, contractor flessibili dove l'incertezza è maggiore, override per shock documentati e review basata su decision cost.

La policy cambia se cambia il rapporto **€67/€24**, se i contractor diventano scarsi, il forecast perde calibration, compare un nuovo driver o il backlog modifica la capacità processabile.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| A MAPE 6,8%; B 7,4% | B è più utile nei picchi con la loss attuale | stabilità futura del rapporto costi under/over |
| A sottostima i picchi | percentile > P50 può essere razionale | nuovi regime shock |
| under-capacity €67/h vs idle €24/h | decision loss è criterio più rilevante della sola MAPE | disponibilità/prezzo contractor futuri |
| Milano P10 74k, P50 82k, P90 94k | | |

La headline executive può essere:

> **Il modello con errore medio minore sottostima i picchi, che sono gli errori più costosi. Proponiamo staffing basato sulla distribuzione prevista e sui costi asimmetrici, con percentile e flessibilità diversi per hub.**

L'outcome review misura bias/calibration ma anche overtime, idle hours, SLA breaches, backlog, cost per parcel, contractor premium e differenza tra costo previsto e realizzato.

**Percorso effettivo:** Temporal Decision Brief → Uncertainty Brief → Decision Record → Decision Communication Pack, con Data Readiness Review soltanto quando cambiano fonti o regime.

> **Il caso è volutamente corto: quando il problema è la loss function della policy, un altro decimo di MAPE non è automaticamente altra informazione utile.**

[^aws-driver]: AWS Cloud Financial Management Blog, *Understand and build driver-based forecasting*, https://aws.amazon.com/blogs/aws-cloud-financial-management/understand-and-build-driver-based-forecasting/
