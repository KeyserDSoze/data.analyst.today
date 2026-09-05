## 19.1 Quando il task diventa economico, la responsabilità non scompare

Dire che “SQL diventa commodity” è una scorciatoia pericolosa. Fa immaginare una divisione netta tra competenze destinate a sparire e competenze destinate a restare intatte. In realtà un'attività può diventare molto più economica da eseguire senza rendere economica **la responsabilità di sapere se quell'attività è stata eseguita correttamente, sul fenomeno giusto e per la decisione giusta**.

È utile distinguere quindi due dimensioni. La prima è la **task exposure**: quanto un'attività può essere assistita, compressa o automatizzata. L'esposizione tende a crescere quando l'input è abbastanza specificato, l'output segue pattern ricorrenti, esistono molti esempi e il risultato può essere verificato rapidamente. Generare SQL standard, tradurre un dialect, produrre boilerplate Python, creare una visualizzazione di base, scrivere documentazione o costruire una prima query candidate rientrano spesso in questa zona. Non smettono di servire; semplicemente costano meno.

La seconda dimensione è il **responsibility moat**. Non indica un'area magicamente immune all'automazione. Indica la parte del lavoro in cui il valore deriva da contesto non completamente formalizzato, obiettivi in conflitto, semantica business, failure cost, effetti downstream e judgment sotto incertezza. Decidere quale churn sia appropriato per una policy, capire se un confronto osservazionale può sostenere un claim causale, stabilire quale guardrail impedisca a un'ottimizzazione locale di danneggiare il sistema o scegliere se attendere nuova informazione appartengono a questa categoria.

La differenza diventa evidente in un caso semplice. Un analyst deve calcolare la repeat purchase rate a 90 giorni per paese e canale. Con un buon semantic context e AI, una prima query può arrivare in tre minuti. La sintassi può essere impeccabile. Ma prima che il numero abbia significato bisogna ancora decidere se la coorte parte dal primo ordine creato o pagato, come trattare refund e guest identity, se i 90 giorni decorrono dall'ordine o dalla consegna, quale canale usare e soprattutto se il denominatore include soltanto clienti che hanno avuto davvero 90 giorni completi di osservazione.

Se l'AI inserisce anche clienti acquisiti venti giorni fa, la query continuerà a girare perfettamente e la metrica resterà artificialmente depressa per mesi. Il task di scrittura SQL era altamente esposto. Il rischio decisionale no.

Questa distinzione attraversa quasi tutto il lavoro analitico:

| Attività | Task exposure | Responsibility moat |
|---|---:|---:|
| scrivere una query standard | alta | bassa-media |
| verificare grain e cardinalità | media-alta | alta |
| produrre un forecast candidate | alta | media |
| scegliere quale forecast usare per staffing | media | alta |
| creare uno score churn | alta | media |
| decidere chi trattare dati uplift, costo e capacità | bassa-media | molto alta |
| generare un DAG candidate | alta | media |
| decidere se l'effetto è identificato | media | molto alta |
| creare un executive summary | alta | media |
| calibrare claim level e caveat decision-critical | media | molto alta |

La tabella non deve diventare una classifica eterna. Le celle cambieranno con la tecnologia. Il punto è osservare dove il costo di esecuzione sta scendendo più rapidamente del costo della responsabilità.

Da qui segue una conseguenza importante: la tecnica non perde necessariamente valore quando l'AI ne automatizza una parte. Cambia **funzione professionale**. Possiamo distinguere tre ruoli della stessa competenza. Come **execution skill**, serve a produrre l'output. Come **verification skill**, permette di capire se l'output è plausibile e metodologicamente coerente. Come **design skill**, permette di costruire il problema, il metodo e i controlli affinché l'output possa avere valore.

Un analyst che non comprende grain, join, leakage, randomizzazione, standard error, baseline, backtest o unit economics non diventa più strategico perché un agente gli scrive il codice. Diventa più dipendente proprio nel momento in cui l'output appare più professionale.

L'aggiornamento ILO del 2025 sulla GenAI e il lavoro è utile perché studia l'esposizione a livello di task e conclude che, per la maggior parte delle occupazioni, la trasformazione è più plausibile della completa automazione. I lavori contengono combinazioni differenti di attività e continuano a richiedere input umano.

Fonte: https://www.ilo.org/publications/generative-ai-and-jobs-2025-update

Questo evita due narrazioni simmetricamente semplicistiche: “l'AI cancellerà il ruolo” e “non cambierà nulla”. È più plausibile che cambi la composizione del ruolo e, con essa, il premio relativo associato alle diverse capacità.

Per capire come reagire non serve chiedere soltanto “l'AI può fare questa cosa?”. Per ogni attività importante conviene osservare quanto sta diminuendo il costo di esecuzione, quale failure cost resta, che cosa dobbiamo ancora saper verificare e quale responsabilità superiore diventa accessibile se liberiamo tempo dall'esecuzione.

> **La carriera resiliente non si costruisce difendendo i task costosi di ieri. Si costruisce imparando a possedere le responsabilità che emergono quando quei task diventano economici.**