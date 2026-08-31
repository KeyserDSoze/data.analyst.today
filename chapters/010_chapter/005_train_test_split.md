## 10.5 Train, validation e test: il modello deve funzionare su dati che non ha già visto

Un modello può adattarsi molto bene ai dati storici e fallire appena incontra casi nuovi.

Questa è una delle idee più importanti del machine learning applicato: **misurare quanto il modello generalizza**.

Il modo più semplice è separare i dati in insiemi con ruoli diversi:

- **training set**: usato per stimare il modello;
- **validation set**: usato per scegliere feature, soglie, iperparametri e alternative;
- **test set**: usato alla fine per una valutazione il più possibile imparziale.

In progetti semplici si usa spesso solo train/test. In progetti con tuning o molte iterazioni è meglio separare anche la validazione o usare cross-validation.

### Caso realistico: FinSure e il modello di default

FinSure eroga finanziamenti a piccole imprese. Il team costruisce un modello di rischio con dati dal 2021 al 2025.

Viene fatto uno split casuale 80/20.

Il modello ottiene risultati eccellenti.

Poi viene usato sui nuovi prestiti del 2026 e la qualità cala bruscamente.

Perché?

Nel 2025 FinSure ha cambiato:

- criteri di acquisizione clienti;
- pricing;
- canali commerciali;
- politica di underwriting.

Con uno split casuale, esempi molto simili dello stesso regime operativo finiscono sia nel train sia nel test.

Il test non rappresenta davvero il futuro.

### Split temporale

Quando il modello deve prevedere eventi futuri, spesso è più realistico simulare ciò che accadrà in produzione:

- train: gennaio 2021 – dicembre 2024;
- validation: gennaio – giugno 2025;
- test: luglio – dicembre 2025.

Questo tipo di split può produrre metriche peggiori, ma più credibili.

### Group split

Un altro rischio nasce quando più righe appartengono alla stessa entità.

Supponiamo di prevedere il churn usando snapshot mensili dello stesso cliente. Se gli snapshot di gennaio-maggio finiscono nel train e quello di giugno nel test, il modello potrebbe riconoscere indirettamente il cliente.

Meglio chiedersi:

> l'unità che voglio generalizzare è una riga o un cliente mai visto?

In alcuni casi lo split deve essere fatto per:

- cliente;
- azienda;
- negozio;
- dispositivo;
- paziente;
- regione.

### Caso realistico: MoveNow e i tempi di consegna

MoveNow costruisce un modello di ETA su 12 milioni di consegne.

Split casuale:

- MAE: 5,8 minuti.

Split per nuove città:

- MAE: 11,4 minuti.

Il modello non era “sbagliato”. La prima valutazione rispondeva alla domanda:

> quanto funziona su nuove consegne in contesti già noti?

La seconda rispondeva a:

> quanto funziona quando apriamo una nuova città?

Sono due problemi di business differenti.

### Regola fondamentale

Il test set deve assomigliare il più possibile alla situazione in cui il modello verrà realmente utilizzato.

Non basta dividere le righe. Bisogna simulare la **frontiera informativa e temporale della decisione**.
