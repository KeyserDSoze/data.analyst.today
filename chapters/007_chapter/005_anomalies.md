## 7.4 Anomalie: un alert è l'inizio dell'indagine, non la conclusione

Un'anomalia è uno scostamento rispetto a ciò che consideriamo **atteso nel contesto corretto**.

La definizione sembra semplice, ma dipende interamente dalla baseline.

Un valore di 50.000 ordini può essere:

- normale il giorno di Black Friday;
- eccezionale in un martedì di febbraio;
- impossibile se il sistema ha capacità massima di 20.000;
- semplicemente incompleto se metà degli eventi è ancora in ritardo.

Per questo anomaly detection non dovrebbe iniziare da “quanto è lontano dalla media?”, ma da:

> **Quale comportamento avremmo considerato normale in questa finestra, dato calendario, trend, stagionalità e stato del dato?**

### Quattro classi che non vanno confuse

Per il lavoro di un Data Analyst è utile distinguere:

**1. Data anomaly** — il business può essere normale, ma il sistema di osservazione è incompleto o errato.

**2. Contextual anomaly** — il valore è estremo rispetto a una baseline generica, ma normale nel contesto specifico.

**3. Business anomaly** — il dato è valido e il comportamento è realmente insolito rispetto a una baseline adeguata.

**4. Structural break** — non cambia soltanto un punto: cambia il processo che genera la serie.

La risposta operativa è diversa in ciascun caso.

### Caso simulato/composito — Il -42% che apparteneva alla pipeline

Un marketplace monitora il GMV ogni quindici minuti.

Alle 14:30 l'alert mostra:

```text
GMV atteso 14:00–14:15: 318.000 €
GMV osservato: 184.000 €
scostamento: -42,1%
```

Il primo impulso è sospendere una campagna e aprire un incidente sul checkout.

L'analista verifica la catena di metriche:

- sessioni: normali;
- add-to-cart: normali;
- checkout iniziati: normali;
- payment success: apparentemente -39%;
- errori del payment gateway: normali.

Poi controlla la **latenza di ingestion**. Il 38% degli eventi `payment_success` ha più di venti minuti di ritardo.

Alle 15:05, una volta arrivati gli eventi, il GMV reale della finestra è 309.000 €, circa -2,8% rispetto all'atteso.

L'anomalia era reale nel dashboard. Non era reale nel processo commerciale.

### Prima regola: verificare l'osservabilità

Per un alert operativo, prima delle ipotesi di business controlliamo:

- freshness;
- completezza;
- ritardo di ingestion;
- duplicati;
- partizioni mancanti;
- variazioni di schema;
- cambi di timezone;
- cambi di definizione della metrica;
- errori upstream/downstream.

Questo non duplica il Capitolo 3. Nel Capitolo 3 valutavamo se un dataset era pronto per l'analisi. Qui il punto è diverso: **una pipeline può essere normalmente affidabile e produrre un incidente temporaneo che imita un'anomalia di business**.

### Contextual anomaly: l'eccezione che era prevista

Un detector segnala ordini +63% rispetto alla media recente durante la finale di Champions League.

Statisticamente il valore può essere estremo. Operativamente può essere esattamente ciò che il business si aspettava.

Se l'evento era noto nel calendario, il problema non è l'algoritmo in senso stretto. È una baseline che non contiene informazione contestuale sufficiente.

Questo è il motivo per cui soglie come:

`alert se |z| > 4`

possono essere utili come primo filtro ma fragili in processi stagionali, promozionali o soggetti a eventi speciali.

### Point, collective e change anomaly

Un punto singolo non è l'unica forma di anomalia.

**Point anomaly** — un valore isolato è insolito.

**Collective anomaly** — ogni punto singolo sembra plausibile, ma la sequenza complessiva è anomala.

**Change-point / structural break** — cambia livello, trend, varianza o altra proprietà della serie.

NIST mostra, nel contesto della rilevazione di change-point, che autocorrelazione e stagionalità devono essere considerate per evitare di interpretare la normale struttura temporale come un numero eccessivo di cambiamenti.[^nist-change]

### Caso simulato/composito — Nessun giorno è terribile, ma il processo è cambiato

Un SaaS monitora il numero giornaliero di ticket critici.

Storicamente oscilla tra 38 e 55. Dopo una nuova release osserva:

`52, 54, 57, 59, 58, 61, 60, 62, 63, 61`

Nessun giorno è abbastanza estremo da superare una soglia di quattro deviazioni standard.

Ma la sequenza mostra un cambiamento persistente di livello.

Un detector concentrato soltanto su point anomaly può non vedere ciò che per operations è molto più importante: **il processo è entrato in un nuovo regime**.

### Anomalia statistica e materialità business

Non ogni scostamento statisticamente insolito merita lo stesso livello di escalation.

Un aumento del 80% su una metrica che vale 200 € al giorno e un calo del 4% su una metrica che vale 30 M€ al giorno possono avere priorità opposte.

Un sistema di alert maturo combina quindi almeno:

- intensità dello scostamento;
- durata/persistenza;
- valore economico;
- criticità operativa;
- confidenza nella qualità del dato;
- possibilità di azione.

### Anomaly triage

Quando arriva un alert, la sequenza consigliata è:

1. **Data health** — la misura è completa e comparabile?
2. **Context** — calendario, promozione, festività, evento noto?
3. **Scope** — quale segmento, geografia, prodotto o step è coinvolto?
4. **Persistence** — punto singolo, sequenza o cambio di livello?
5. **Corroboration** — metriche upstream/downstream confermano il fenomeno?
6. **Materiality** — qual è l'impatto reale?
7. **Hypothesis** — quali meccanismi sono compatibili con l'evidenza?
8. **Next method** — altra diagnostica, causalità, intervento o monitoraggio?

### Il detector non deve “spiegare”

Un sistema automatico può dire:

> “GMV 18% sotto la baseline stagionale, concentrato su Android, dato completo al 99,7%.”

È molto utile.

Dovrebbe essere molto più prudente nel dire:

> “Il calo è causato dal nuovo checkout.”

La seconda frase richiede evidenza sul meccanismo.

Un LLM può proporre ipotesi, ma non trasforma la correlazione temporale in causalità.

### Il campo del Temporal Decision Brief

Per ogni anomalia importante registriamo:

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

> **Un'anomalia statistica è un invito a investigare. La qualità dell'analista si vede da quanto velocemente distingue un evento eccezionale da un sistema di osservazione eccezionalmente sbagliato.**

[^nist-change]: NIST, *Statistical Methods for Change-Point Detection in Surface Temperature Records*, https://www.nist.gov/publications/statistical-methods-change-point-detection-surface-temperature-records
