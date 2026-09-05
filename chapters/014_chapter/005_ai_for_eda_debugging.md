## 14.4 AI per EDA e debugging: ampliare il search space senza promuovere il primo pattern interessante

L'AI è molto utile nell'EDA perché rende economico generare segmentazioni, query diagnostiche, controlli sui missing, visualizzazioni, ipotesi alternative e possibili failure boundary. Questa velocità ha però un costo epistemico: se possiamo esplorare cento volte più rapidamente, possiamo anche trovare cento volte più pattern plausibili che non reggeranno.

Il workflow deve quindi governare tre cose: **search, falsification e promotion dell'evidenza**.

### Usare l'AI come hypothesis generator

Una richiesta utile non è "qual è la causa?", ma:

> Quali decomposizioni distinguerebbero queste ipotesi?

Una travel app vede conversion scendere da `4,7%` a `3,9%` in due giorni. Il sistema costruisce una hypothesis map:

| Ipotesi | Pattern atteso | Test discriminante |
|---|---|---|
| bug app | drop per versione | app version × funnel |
| PSP outage | drop per payment rail | error code × PSP |
| tracking issue | ordini stabili, session/conversion cambiano | reconciliation backend |
| traffic mix | drop per channel/geo | within-segment comparison |
| inventory | drop concentrato su route/hotel type | availability signal |

Il valore non è aver indovinato il bug. È aver trasformato una domanda vaga in test falsificabili. I dati mostrano poi iOS stabile, drop Android, concentrazione su Android 14, break tra `payment_started` e `payment_success` e aumento di `WALLET_TOKEN_EXPIRED`. Solo dopo Engineering conferma un problema nel wallet SDK.

### Diagnostic search log e search budget

Quando il costo di generare esplorazioni crolla, aumenta il bisogno di registrare quali esplorazioni abbiamo fatto. Un **Diagnostic Search Log** può essere molto semplice:

```text
hypothesis
why considered
test/query
result
status: supported | weakened | unresolved
next cheapest discriminating test
```

Questo evita il pattern "provo 80 slice, una sembra interessante, la racconto come se fosse la domanda iniziale". Possiamo anche fissare un **search budget**: per esempio cinque famiglie di ipotesi nel primo passaggio, due test per famiglia e stop immediato se emerge un data-quality failure; nel secondo passaggio approfondiamo soltanto le ipotesi migliori e cerchiamo almeno un test che possa indebolirle.

Non è una regola statistica universale. È una disciplina contro il researcher degree of freedom che l'AI rende più economico esercitare.

### Usare l'AI anche per attaccare l'ipotesi favorita

Una volta emersa una working hypothesis, chiediamo al sistema di proporre meccanismi alternativi compatibili con lo stesso pattern e il test più economico per distinguerli. Questo è utile contro confirmation bias umano e narrative lock-in del modello. L'AI non deve essere soltanto un generatore di spiegazioni; può diventare un **generatore di obiezioni verificabili**.

### Debugging: trovare il primo boundary rotto

La stessa logica funziona sulle pipeline. Invece di chiedere genericamente "perché mancano dati?", forniamo DAG, row count per layer, freshness, schema changes, deploy recenti e test falliti. Poi chiediamo di identificare il primo invariant che cambia.

Esempio:

```text
Raw:    2,80M
Silver: 2,80M
Gold:   2,32M
```

Il primo boundary rotto è `Silver → Gold`. Un nuovo `INNER JOIN` al product master elimina 480.000 order line associate a SKU nuovi non ancora presenti nella dimensione. L'AI accelera la diagnosi perché aiuta a **localizzare la perdita**; la causa viene confermata dal controllo sul join.

### Data-health gate prima della narrativa

Prima di interpretare un'anomalia, il sistema deve verificare almeno freshness, completeness, schema status, grain/key invariants, volume anomalies, incidenti noti e reconciliation del KPI headline. Se fallisce un controllo critico, l'output corretto può essere:

> Investigazione business sospesa: il denominatore sessioni è incompleto del 18% dopo il deploy del consent layer.

Questo è più utile di una lista creativa di cause business.

### EDA non è confirmation

Se dopo decine di slice emerge un uplift apparente, il risultato resta esplorativo finché non supera un gate adeguato: holdout temporale, campione indipendente, test pre-specificato, correzione per molteplicità, esperimento o Causal Identification Brief. Il Capitolo 5 ha già trattato multiple testing; qui aggiungiamo una conseguenza operativa:

> **Se l'AI riduce il costo di generare confronti, dobbiamo rendere più visibile quali confronti sono stati generati prima di promuoverne uno a evidenza decisionale.**

La AI Analysis Control Sheet registra obiettivo EDA, hypothesis families, search budget, search log, data-health gate, alternative testate, falsification test e regola di promozione dall'esplorazione alla decisione.

> **Usa l'AI per ampliare e strutturare lo spazio delle ipotesi. Poi rendi costoso promuovere un pattern interessante a conclusione: servono falsificazione, log della ricerca e un gate di evidenza.**
