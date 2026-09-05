## 7.4 Anomalie: un alert è l'inizio dell'indagine, non la conclusione

Dopo aver costruito una baseline credibile possiamo definire un'anomalia in modo più rigoroso: **uno scostamento rispetto a ciò che sarebbe stato atteso nel contesto corretto**. La parte difficile non è misurare la distanza. È decidere che cosa costituisca davvero l'atteso.

Cinquantamila ordini possono essere perfettamente normali a Black Friday, eccezionali in un martedì di febbraio, impossibili per un sistema con capacità massima di 20.000 o semplicemente incompleti se metà degli eventi deve ancora arrivare. Per questo anomaly detection non dovrebbe partire da “quanto siamo lontani dalla media?”, ma da:

> **Quale comportamento avremmo considerato normale in questa finestra, dato calendario, struttura della serie e stato del dato?**

Nel lavoro operativo conviene distinguere quattro situazioni perché richiedono risposte diverse. Una **data anomaly** nasce nel sistema di osservazione; una **contextual anomaly** è estrema rispetto a una baseline generica ma normale nel contesto corretto; una **business anomaly** è un vero scostamento del processo; uno **structural break** indica invece che è cambiato il processo stesso, non soltanto un punto.

### Caso simulato/composito — Il -42% che apparteneva alla pipeline

Un marketplace monitora il GMV ogni quindici minuti. Alle 14:30 compare l'alert:

```text
GMV atteso 14:00–14:15: 318.000 €
GMV osservato: 184.000 €
scostamento: -42,1%
```

Sospendere una campagna o aprire un incidente sul checkout sembra una reazione naturale. L'analista, però, segue prima la catena di osservabilità. Sessioni, add-to-cart e checkout iniziati sono normali; `payment_success` appare circa -39%, ma gli errori del gateway non aumentano. Il problema emerge nella pipeline: il **38%** degli eventi `payment_success` ha più di venti minuti di ritardo.

Alle 15:05, quando gli eventi arrivano, il GMV reale della finestra è **309.000 €**, circa **-2,8%** rispetto all'atteso. L'anomalia era reale nel dashboard e quasi inesistente nel processo commerciale.

Questa sequenza spiega perché, davanti a un alert operativo, la prima domanda debba riguardare freshness, completezza, ingestion delay, duplicati, partizioni, schema, timezone, definizione della metrica e dipendenze upstream/downstream. Non è una ripetizione del Capitolo 3: un dataset normalmente affidabile può subire un incidente temporaneo che imita perfettamente un problema di business.

### Il contesto può trasformare un outlier in normalità

Immaginiamo ora un detector che segnala ordini **+63%** rispetto alla media recente durante la finale di Champions League. Statisticamente il valore può essere estremo; operativamente può essere esattamente ciò che il business si aspettava. Se l'evento era noto, il problema non è necessariamente il dato ma una baseline troppo povera di contesto.

Lo stesso limite vale per regole come `alert se |z| > 4`: possono essere un primo filtro, ma diventano fragili in processi stagionali, promozionali o con eventi speciali. Il valore “raro” dipende sempre dal mondo rispetto al quale lo giudichiamo.

### Non tutte le anomalie hanno la forma di un picco

Un detector può cercare un singolo valore estremo e perdere un cambiamento molto più importante. Consideriamo il numero giornaliero di ticket critici di un SaaS, storicamente compreso tra 38 e 55. Dopo una release osserviamo:

`52, 54, 57, 59, 58, 61, 60, 62, 63, 61`

Nessun giorno deve necessariamente superare una soglia estrema. La sequenza, però, mostra un nuovo livello persistente. NIST, nel lavoro sui change-point, sottolinea proprio che autocorrelazione, stagionalità e variabilità naturale devono essere considerate per non scambiare la struttura temporale per cambiamenti inesistenti — o perdere cambiamenti persistenti dietro singoli punti apparentemente plausibili.[^nist-change]

Per questo distinguiamo **point anomaly**, **collective anomaly** e **change-point/structural break**. L'obiettivo non è costruire una tassonomia elegante, ma scegliere l'azione corretta: verificare un evento isolato, investigare una sequenza o riaprire le assunzioni dell'intero modello.

### Insolito non significa importante

Anche la materialità deve entrare nel triage. Un aumento dell'80% su una metrica da 200 € al giorno può essere meno urgente di un calo del 4% su una metrica da 30 M€ al giorno. La priorità dipende da intensità, persistenza, valore economico, criticità operativa, affidabilità del dato e possibilità concreta di agire.

Per questo l'**Anomaly Triage** merita di restare una sequenza operativa:

1. **Data health** — la misura è completa e comparabile?
2. **Context** — calendario, promozione, festività o evento noto spiegano il valore?
3. **Scope** — quale segmento, geografia, prodotto o step è coinvolto?
4. **Persistence** — punto singolo, sequenza o cambio di livello?
5. **Corroboration** — metriche upstream/downstream confermano il fenomeno?
6. **Materiality** — qual è l'impatto reale?
7. **Hypothesis** — quali meccanismi sono compatibili con l'evidenza?
8. **Next method** — altra diagnostica, causalità, intervento o monitoraggio?

Un sistema automatico può essere molto utile se dice: “GMV 18% sotto la baseline stagionale, concentrato su Android, dato completo al 99,7%”. Deve essere molto più prudente prima di affermare: “il nuovo checkout ha causato il calo”. Un LLM può generare ipotesi e accelerare il triage; non converte una coincidenza temporale in prova causale.

Nel Temporal Decision Brief l'anomalia importante viene quindi registrata come evidenza, non come verdetto:

```text
Segnale:
Baseline usata:
Data health:
Contesto di calendario:
Scope / segmenti:
Persistenza:
Tipo: data / contextual / business / structural
Impatto:
Ipotesi plausibili:
Cosa NON è ancora dimostrato:
Azione / escalation:
```

> **Un'anomalia statistica è un invito a investigare. La qualità dell'analista si vede da quanto velocemente distingue un processo eccezionale da un sistema di osservazione eccezionalmente sbagliato.**

Una volta stabilito che il processo possiede struttura sufficientemente stabile e che gli scostamenti sono reali, possiamo fare il salto successivo: usare quella struttura per prevedere il futuro. Anche lì, però, la prima domanda non sarà “quale modello?”, ma “quale decisione e quale baseline dobbiamo battere?”.

[^nist-change]: NIST, *Statistical Methods for Change-Point Detection in Surface Temperature Records*, https://www.nist.gov/publications/statistical-methods-change-point-detection-surface-temperature-records
