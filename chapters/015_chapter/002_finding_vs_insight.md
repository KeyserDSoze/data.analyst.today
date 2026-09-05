## 15.1 Dal finding all'insight: quando l'evidenza cambia davvero lo spazio delle scelte

Uno degli errori più comuni nel lavoro analitico è chiamare *insight* qualsiasi numero non ovvio. Ma sorpresa, spiegazione e utilità decisionale sono proprietà diverse.

Se osserviamo che la conversion desktop è stabile mentre quella mobile scende del 9%, abbiamo un **finding**: descriviamo il fenomeno. Se scopriamo che il calo mobile è concentrato sulle sessioni che attraversano il nuovo checkout e spiega circa il 78% della perdita di ordini, abbiamo localizzato la struttura del problema. Se ipotizziamo che il nuovo checkout abbia introdotto frizione, abbiamo formulato una spiegazione compatibile con l'evidenza. Soltanto quando traduciamo questa conoscenza in un cambiamento nello spazio delle opzioni — per esempio congelare il rollout e usare il vecchio checkout come controllo — arriviamo alla **decision implication**.

La distinzione serve a evitare due scorciatoie:

```text
pattern → causa
pattern → azione
```

Nel primo caso saltiamo il livello di evidenza; nel secondo saltiamo il confronto tra alternative.

In questo libro useremo *insight* in senso operativo: **una sintesi dell'evidenza che modifica materialmente la rappresentazione del problema e, di conseguenza, le decisioni plausibili**. Non deve essere necessariamente causale. Deve però cambiare almeno una cosa importante: dove vediamo il rischio o il valore, quale popolazione consideriamo, quale assunzione precedente smette di reggere, quale alternativa diventa più o meno attraente o quale nuova informazione merita di essere raccolta.

### Quando un segmento cambia il significato dell'aggregato

Consideriamo un e-commerce che confronta la repeat purchase a 90 giorni:

| Canale | Repeat rate |
|---|---:|
| Organic | 34% |
| Referral | 31% |
| Paid Search | 27% |
| Paid Social | 19% |

Il finding è inequivocabile: Paid Social ha la repeat rate più bassa. Se trasformiamo immediatamente questo risultato in una decisione, il budget del canale diventa il bersaglio naturale.

Il team segmenta però per tipo di cliente e scopre che Paid Social porta una quota molto più alta di **first-time category buyers**, che hanno retention inferiore in tutti i canali. Dopo standardizzazione per mix, il gap si riduce fortemente.

Il dato originale non sparisce; cambia ciò che ci autorizza a concludere. La lettura “Paid Social acquisisce clienti peggiori” lascia spazio a una formulazione più utile: una parte importante del gap dipende dalla composizione della popolazione, quindi la decisione deve distinguere almeno **channel execution, audience composition e activation post-acquisto**. Le opzioni diventano tre, non una:

```text
A — ridurre Paid Social
B — cambiare targeting
C — cambiare activation per quel mix di clienti
```

Questo è il valore dell'insight: non una frase più sofisticata, ma uno spazio decisionale meno distorto.

### Un finding può essere vero e non meritare attenzione

La decision relevance richiede anche materialità. Un delta di conversion da 3,842% a 3,807% può essere stimato con grande precisione e restare economicamente irrilevante se vale €4.000 l'anno in un business da miliardi e richiede tre mesi di engineering.

Perciò, prima di promuovere un finding a insight, chiediamo quale quota del KPI cambia, quanta popolazione coinvolge, se il fenomeno persiste, quanto vale in termini economici o di rischio e se esiste una leva plausibile. La materialità non coincide con gli euro: compliance, sicurezza, customer harm, reputazione, fairness e resilienza possono dominare una scelta anche quando non hanno una monetizzazione pulita.

Un test semplice è:

> **Se questa informazione fosse falsa, quale decisione cambierebbe?**

Se la risposta è “nessuna”, potremmo avere un pattern interessante ma non decision-relevant. La domanda successiva è ancora più utile:

> **Quale alternativa guadagna o perde credibilità grazie a questa evidenza?**

Se non sappiamo rispondere, probabilmente siamo ancora nella fase esplorativa.

### L'insight deve trasportare il proprio livello di claim

Il Capitolo 14 ha reso esplicito che la comunicazione non può promuovere automaticamente un claim. La stessa disciplina vale nel Decision Record.

Per esempio:

```text
finding:
refund rate +2,1 pp

localization:
82% del delta in due seller

hypothesis:
catalog quality deterioration

causal status:
non identificato

decision implication:
sospendere temporaneamente autopublish per quei seller e testare QC
```

La decision implication può essere ragionevole perché l'intervento è circoscritto e reversibile; non serve fingere che la causa sia già identificata. Serve invece mantenere visibile la differenza tra ciò che sappiamo, la working hypothesis e il rischio che siamo disposti ad assumere.

Strumenti moderni possono automatizzare la scoperta di trend e anomalie; Power BI, per esempio, documenta funzionalità di Insights che cercano pattern nelle visualizzazioni.[^powerbi-insights] Questo aumenta la velocità di discovery, non risolve automaticamente materialità, stabilità, composizione, causalità, economics o actionability.

Nel Decision Record, un insight che conta può quindi essere sintetizzato così:

```text
finding:
materiality:
where concentrated:
what changed in our understanding:
claim level:
key alternative explanation:
decision implication:
```

> **L'automazione può aumentare il numero di finding. Il lavoro dell'analista è selezionare e qualificare quelli che cambiano davvero il confronto tra alternative.**

[^powerbi-insights]: Microsoft Learn, *Insight types in Power BI*, https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-insight-types
