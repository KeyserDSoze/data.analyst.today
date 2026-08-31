## 9.8 Potenza statistica e sensibilità: il test può vedere ciò che stiamo cercando?

La potenza statistica è la probabilità di rilevare un effetto reale di una certa dimensione quando quell'effetto esiste. In pratica, misura quanto un esperimento è capace di non perdere un miglioramento vero.

Un test con poca potenza può produrre una lunga sequenza di risultati "non significativi" anche quando il prodotto sta realmente migliorando.

### Caso simulato/composito - La feature che sembrava inutile

Un prodotto collaboration introduce un suggerimento automatico per creare attività da una conversazione. Il team vuole misurare l'aumento di task completati per utente.

Dopo sette giorni:

- controllo: 1,84 task completati per utente;
- trattamento: 1,89;
- differenza: +2,7%;
- p-value: 0,18.

La lettura superficiale è: "la feature non funziona".

L'analista controlla la progettazione. Il test era stato dimensionato per rilevare un aumento del 7%, ma il business sarebbe interessato anche a un +2%. Inoltre la metrica è estremamente rumorosa: una piccola quota di utenti crea decine di task al giorno.

Il risultato non dimostra assenza di effetto. Dice soltanto che **questo esperimento non era abbastanza sensibile per distinguere un effetto del 2-3% dal rumore**.

Dopo aver ridefinito la metrica, aumentato la durata e utilizzato informazione pre-esperimento per ridurre la varianza, la stima resta intorno al +2,5%, ma l'intervallo diventa molto più stretto.

La decisione cambia: rollout graduale, perché l'effetto è piccolo ma rilevante su una base utenti enorme.

### Un caso pubblico: Microsoft e le metriche poco sensibili

Microsoft Experimentation Platform ha documentato casi in cui metriche importanti di Bing, MSN e Microsoft Teams erano troppo rumorose per rilevare variazioni utili con un semplice confronto delle medie. Tecniche di metric design e variance reduction hanno aumentato la sensibilità; in alcuni esperimenti, metriche che apparivano piatte senza correzione mostravano invece movimenti rilevabili dopo l'aggiustamento.

La lezione è importante: **non sempre il problema è che il prodotto non si muove; a volte è la metrica che non riesce a vedere il movimento**.

### Power non significa certezza

Una potenza dell'80% non significa che l'80% dei risultati significativi sia corretto. Significa che, se l'effetto reale è pari all'MDE ipotizzato e le altre assunzioni valgono, il test ha circa l'80% di probabilità di rilevarlo.

La potenza va sempre letta insieme a:

- effect size;
- variabilità;
- alpha;
- durata;
- unità di randomizzazione;
- tasso di esposizione reale;
- qualità della metrica.

### Fonti

- Microsoft Experimentation Platform, *Beyond Power Analysis: Metric Sensitivity Analysis in A/B Tests*.
- Microsoft Experimentation Platform, *Patterns of Trustworthy Experimentation: Pre-Experiment Stage*.
