# 15.1 Finding, insight e spiegazione: non sono la stessa cosa

Uno degli errori più comuni nel lavoro analitico è chiamare *insight* qualsiasi numero non ovvio.

Ma un finding può essere sorprendente senza essere utile, e una spiegazione può essere plausibile senza essere dimostrata.

## Tre livelli diversi

### 1. Finding

> “La conversione desktop è stabile, quella mobile è scesa del 9%.”

Descrive il fenomeno.

### 2. Insight

> “Il calo mobile è concentrato sulle sessioni che usano il nuovo checkout e spiega circa il 78% della perdita di ordini.”

Collega il fenomeno alla struttura del problema.

### 3. Spiegazione causale

> “Il nuovo checkout ha causato il calo.”

Questa è un'affermazione più forte e richiede evidenza più forte.

Il fatto che un pattern sia utile per investigare non significa che sia già causale.

## Caso realistico: il canale che sembrava “peggiore”

Un e-commerce confronta la repeat purchase rate a 90 giorni per canale di acquisizione:

| Canale | Repeat rate |
|---|---:|
| Organic | 34% |
| Referral | 31% |
| Paid Search | 27% |
| Paid Social | 19% |

Il finding è chiaro: Paid Social ha retention peggiore.

La conclusione immediata sarebbe ridurre il budget.

Ma il team segmenta per tipo di cliente e scopre che Paid Social porta una quota molto più alta di first-time category buyers, clienti che storicamente hanno retention più bassa in tutti i canali.

Dopo standardizzazione per mix, il gap si riduce fortemente.

Il finding non scompare.

Cambia il significato.

L'insight diventa:

> “Paid Social acquisisce un mix di clienti strutturalmente più difficile da trattenere; la performance del canale va valutata separando qualità del traffico, composizione del pubblico e activation post-acquisto.”

Questo produce una decisione molto diversa da:

> “Paid Social non funziona.”

## Il test dell'insight

Un possibile test è chiedere:

**Se questa informazione fosse falsa, cambierebbe la decisione?**

Se la risposta è no, probabilmente stiamo descrivendo qualcosa di interessante ma non decision-relevant.

Un secondo test:

**Quale comportamento o scelta cambia grazie a questa informazione?**

Se non sappiamo rispondere, l'analisi potrebbe essere ancora incompleta.

## Gli insight automatici non sono decisioni automatiche

Strumenti moderni possono trovare automaticamente trend, anomalie e correlazioni. La documentazione Power BI, per esempio, descrive funzionalità di Insights che analizzano report e visualizzazioni per evidenziare trend, anomalie e pattern interessanti.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-insight-types

Queste funzionalità sono utili per discovery.

Ma trovare un pattern non risolve automaticamente:

- se il pattern è materialmente importante;
- se è stabile;
- se dipende dal mix;
- se è causale;
- se è azionabile;
- se il costo dell'intervento è giustificato.

> **L'automazione può aumentare il numero di finding. Il lavoro dell'analista è aumentarne la qualità decisionale.**
