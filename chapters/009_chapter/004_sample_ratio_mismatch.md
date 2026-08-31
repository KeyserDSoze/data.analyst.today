## 9.3 Sample Ratio Mismatch: quando il 50/50 non è davvero 50/50

Un A/B test può essere statisticamente sofisticato e allo stesso tempo inutilizzabile perché i gruppi non sono comparabili.

Uno dei controlli più importanti è il **Sample Ratio Mismatch**, spesso abbreviato SRM.

Se un esperimento è configurato per assegnare il 50% degli utenti al controllo e il 50% al trattamento, ci aspettiamo una distribuzione compatibile con quella proporzione. Piccole differenze casuali sono normali. Differenze troppo grandi possono indicare un problema nella catena sperimentale.

Microsoft tratta l'SRM come un controllo di qualità fondamentale: una deviazione statisticamente significativa dal rapporto configurato può segnalare problemi di assegnazione, esecuzione, logging, join o analisi e rende il test non affidabile finché la causa non è capita.

### Caso: la variante B sembra perdere, ma mancano proprio gli utenti più coinvolti

Immaginiamo un test su una homepage con allocazione 50/50.

Dopo cinque giorni:

| Variante | Utenti osservati | CTR |
|---|---:|---:|
| A | 1.020.441 | 18,2% |
| B | 973.115 | 17,4% |

Il team conclude che B peggiora l'engagement.

L'analista però nota che la differenza nei volumi è troppo grande. Il test SRM fallisce.

L'indagine trova il problema: nella variante B gli utenti più attivi generano una sequenza di eventi che attiva erroneamente un filtro anti-bot. Proprio gli utenti maggiormente esposti all'effetto del trattamento spariscono dal dataset analitico.

Dopo la correzione della pipeline:

| Variante | CTR corretto |
|---|---:|
| A | 18,2% |
| B | 19,1% |

La conclusione si ribalta.

### Perché guardare soltanto 49% vs 51% non basta

L'entità della deviazione va valutata insieme alla numerosità.

Su 100 utenti, 47 contro 53 può essere del tutto plausibile.

Su 100 milioni di utenti, 49,8 milioni contro 50,2 milioni può invece essere una deviazione estremamente improbabile rispetto a un vero 50/50.

Per questo si usa normalmente un test statistico, ad esempio chi-quadro, sul conteggio delle unità randomizzate.

### Dove nasce un SRM

Le cause possono comparire in diversi punti:

**Assignment**
- hashing errato;
- user ID instabile;
- bucket configurati male;
- ramp-up non simmetrico.

**Execution**
- redirect diverso tra varianti;
- crash o latency che impediscono l'esposizione;
- utenti che possono auto-selezionarsi.

**Telemetry e processing**
- eventi persi;
- filtri applicati diversamente;
- join lossy;
- bot detection influenzata dal trattamento.

**Analysis**
- segmentazioni definite su variabili post-treatment;
- inclusione solo degli utenti che compiono un'azione influenzata dalla variante.

### L'SRM è un sintomo, non una diagnosi

Non basta dire “c'è SRM”. Bisogna capire perché.

La regola operativa è molto semplice:

> Se l'SRM fallisce, non discutere ancora quale variante abbia vinto. Prima ripara la fiducia nei dati.

### Controllo prima del risultato

Nelle piattaforme mature, l'SRM dovrebbe apparire prima delle metriche di business. Questo riduce una tentazione cognitiva pericolosa: cercare di giustificare un problema di qualità quando il risultato ci piace.

### Riferimenti

- Microsoft Research, *Diagnosing Sample Ratio Mismatch in A/B Testing*.
- Microsoft Learn, *Experiments Best Practices and Recommendations*.
