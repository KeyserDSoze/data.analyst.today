## 7.12 Esercizi: ragionare nel tempo senza trasformare il forecast in certezza

Gli esercizi di questo capitolo allenano soprattutto la **sequenza del ragionamento**.

Per ogni problema prova a distinguere:

1. baseline;
2. struttura temporale;
3. anomalia;
4. previsione;
5. incertezza;
6. decisione.

### Esercizio 1 — Il lunedì peggiore dell'anno

Una piattaforma B2B registra lead qualificati giornalieri:

- venerdì: 1.840;
- sabato: 620;
- domenica: 410;
- lunedì: 1.370.

Il CMO riceve un alert: “lead -25,5% rispetto a venerdì”.

Sai inoltre che:

- i lunedì precedenti erano 1.310, 1.355, 1.402 e 1.366;
- venerdì era l'ultimo giorno di una campagna;
- il 4% dei lead del lunedì arriva normalmente con un giorno di ritardo.

Costruisci la baseline corretta e scrivi una conclusione in massimo 100 parole.

### Esercizio 2 — Anomalia del business o del dato?

Un marketplace mostra GMV -31% tra le 10:00 e le 11:00.

Hai queste metriche:

| Metrica | Scostamento vs baseline |
| --- | ---: |
| Sessioni | +2% |
| Product views | +1% |
| Add-to-cart | 0% |
| Checkout start | -1% |
| Payment success | -29% |
| Payment gateway errors | +1% |
| Event ingestion delay | +280% |

Classifica l'evento nella gerarchia:

- data anomaly;
- contextual anomaly;
- business anomaly;
- structural break.

Poi elenca le prime cinque verifiche che faresti prima di avvisare il management.

### Esercizio 3 — Seasonal naïve contro modello ML

Un contact center confronta due forecast.

| Horizon | Seasonal naïve MAE | ML MAE |
| --- | ---: | ---: |
| 1 giorno | 420 | 350 |
| 7 giorni | 610 | 590 |
| 28 giorni | 1.040 | 1.180 |

La pianificazione del personale viene chiusa tre settimane prima.

Quale risultato conta di più? Quali altre metriche o segmentazioni chiederesti prima di scegliere il modello?

### Esercizio 4 — Leakage “as-of”

Un retailer prevede vendite a 30 giorni. Nel dataset storico sono disponibili:

- prezzo corrente;
- sconto finale effettivamente applicato;
- previsione meteo aggiornata a 3 giorni;
- stock finale della settimana;
- calendario promo approvato 45 giorni prima;
- categoria prodotto;
- vendite dei 90 giorni precedenti.

Per ciascuna feature indica:

- se può essere usata in un forecast a 30 giorni;
- quale versione `as-of` dovrebbe essere conservata;
- quale rischio di leakage esiste.

### Esercizio 5 — MAPE perfetto, decisione pessima

Un distributore ha 5.000 SKU.

Il modello B riduce il MAPE medio dal 14% al 10% rispetto al modello A.

Ma:

- sui 100 SKU critici A ha MAE 18, B ha MAE 31;
- uno stock-out critico costa mediamente 1.900 €;
- un'unità in eccesso sugli slow mover costa mediamente 7 € al mese;
- B migliora soprattutto sui 4.000 SKU a bassissimo volume.

Disegna una funzione di valutazione più coerente con la decisione. Non serve una formula perfetta: indica pesi, segmenti e metriche che useresti.

### Esercizio 6 — MAPE o MASE?

Tre serie hanno scale molto diverse:

- SKU A: domanda media 10.000 unità;
- SKU B: domanda media 120 unità;
- SKU C: domanda intermittente, molti giorni a zero.

Vuoi confrontare la qualità del forecast tra le tre serie.

Spiega:

1. perché MAE non è direttamente comparabile;
2. perché MAPE è problematico per C;
3. come una metrica scalata rispetto a naïve/seasonal-naïve può aiutare;
4. perché anche MASE non sostituisce il costo economico dell'errore.

### Esercizio 7 — Intervallo nominale 80%, coverage 54%

Un modello produce prediction interval all'80%.

Nel backtest su 500 forecast:

- solo il 54% dei valori reali cade dentro l'intervallo;
- la coverage a 1 giorno è 78%;
- a 30 giorni è 43%;
- le settimane promozionali sono quasi sempre fuori banda.

Che cosa concludi sul modello? Quali parti del Temporal Decision Brief aggiorneresti?

### Esercizio 8 — Il manager vuole un solo numero

Forecast domanda:

- point forecast: 24.000 unità;
- PI 80%: 21.500–27.300;
- probabilità di superare capacità 26.000: 29%;
- costo medio di under-capacity: 95.000 €;
- costo di capacità aggiuntiva preventiva: 18.000 €.

Prepara una raccomandazione breve. Il compito non è scegliere automaticamente il point forecast: devi collegare distribuzione e costo della decisione.

### Esercizio 9 — Caso reale: Google Flu Trends

Nel caso Google Flu Trends, il sistema sovrastimò il livello dell'influenza in 100 settimane su 108 nella finestra documentata da Lazer e colleghi, e gli errori mostrarono autocorrelazione e stagionalità.

Rispondi:

1. Perché questo pattern è più preoccupante di errori grandi ma casuali?
2. Che cosa avrebbe dovuto mostrare un dashboard di monitoring?
3. Perché una baseline basata su dati CDC laggati era un benchmark importante?
4. Quale rischio nasce quando una feature dipende dal comportamento di una piattaforma che modifica il proprio algoritmo?
5. Perché il caso non dimostra che i digital trace data siano inutili?

Riferimento: Lazer et al., *Science* 2014, https://pubmed.ncbi.nlm.nih.gov/24626916/

### Esercizio 10 — Override umano

Un forecast industriale prevede 50.000 pezzi per il mese prossimo.

Il direttore commerciale sa che un cliente che pesa normalmente per il 30% della domanda ha appena firmato un contratto con un concorrente. L'informazione non è ancora nei dati.

Progetta un processo di override che specifichi:

- forecast statistico originale;
- informazione nuova;
- impatto atteso;
- chi approva l'override;
- forecast finale;
- come misurerai ex post se l'override ha migliorato la decisione.

### Esercizio finale — Temporal Decision Brief

Sei Data Analyst di una piattaforma di delivery.

Il board chiede un forecast degli ordini per le prossime otto settimane.

Sai che:

- esiste forte stagionalità settimanale;
- la crescita YoY è +14%;
- due festività mobili cadono in settimane diverse rispetto all'anno precedente;
- la fee di consegna aumenterà del 9% tra tre settimane;
- il modello storico non ha mai visto un aumento di fee così grande;
- il modello attuale ha MASE 0,78 a 1 settimana, 0,96 a 4 e 1,12 a 8 rispetto alla baseline naïve/seasonal-naïve usata per la scala;
- il PI 80% ha coverage storica del 76% a 1 settimana e 59% a 8;
- Operations deve assumere personale temporaneo quattro settimane prima;
- il costo di understaffing è circa tre volte quello di overstaffing moderato.

Compila un **Temporal Decision Brief**:

| Campo | La tua risposta |
| --- | --- |
| Series contract |  |
| Decisione |  |
| Origin / horizon |  |
| Baseline temporale |  |
| Struttura |  |
| Evento/regime change |  |
| Baseline model |  |
| Backtest |  |
| Accuracy per horizon |  |
| Business loss |  |
| Prediction interval / coverage |  |
| Conditions of validity |  |
| Override/scenario |  |
| Monitoring |  |
| Raccomandazione |  |

Chiudi con un executive summary di massimo 180 parole.

La risposta migliore non deve fingere che otto settimane siano prevedibili con la stessa affidabilità della prossima settimana. Deve mostrare **dove il modello aggiunge valore, dove smette di battere la baseline e come il cambio di fee modifica le condizioni di validità**.

### Autovalutazione

A fine capitolo dovresti saper spiegare senza software:

- perché una variazione temporale ha bisogno di una baseline;
- perché autocorrelazione e ordine temporale cambiano l'analisi;
- differenza tra anomalia del dato, contestuale, di business e structural break;
- perché un modello deve battere una baseline credibile;
- perché la validazione deve essere `as-of`;
- differenza concettuale tra MAE, RMSE, MAPE e MASE;
- perché accuracy e business loss non coincidono;
- che cosa significa coverage di un prediction interval;
- perché un regime change può rendere obsoleto un buon modello;
- quando un override umano può essere rigoroso;
- perché forecasting e causalità sono domande diverse.
