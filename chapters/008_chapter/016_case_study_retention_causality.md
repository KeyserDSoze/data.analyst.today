## 8.15 Caso simulato/composito — Quale intervento riduce davvero il churn?

**Asteria Cloud** è un SaaS B2B immaginario con **42 milioni di euro di ARR**. Il churn annualizzato è salito dal **9,6% all'11,8%** e il management vuole aumentare l'investimento in Customer Success. La richiesta sembra semplice: “quale intervento riduce davvero il churn e su quali clienti dovremmo usarlo?”.

In realtà Asteria usa già quattro azioni molto diverse: chiamata proattiva Customer Success, training aggiuntivo, sconto temporaneo del **15%** e revisione tecnica dell'integrazione. Il primo errore sarebbe metterle nella stessa tabella e trattare il churn osservato come una classifica di efficacia:

| Intervento osservato | Churn D90 |
|---|---:|
| nessun intervento | 8,1% |
| chiamata CS | 19,4% |
| training | 14,8% |
| sconto | 22,1% |
| revisione tecnica | 17,3% |

Una lettura ingenua direbbe che ogni intervento peggiora il churn. Ma le azioni vengono attivate proprio quando gli operatori vedono rischio. Il confronto grezzo sta misurando soprattutto **come l'azienda decide di intervenire**.

### L'intervista che cambia il problema

Prima di aprire un modello, il team ricostruisce l'assignment mechanism con Customer Success. Scopre che la chiamata parte quasi automaticamente quando `health_score < 65`; il training viene offerto soprattutto a clienti con bassa adoption ma relazione ancora buona; lo sconto viene deciso dopo conversazioni qualitative con procurement o champion; la revisione tecnica viene proposta quando esistono problemi di integrazione. Alcuni account ricevono più interventi insieme.

Questa informazione vale quanto molte ore di modellazione, perché mostra che non esiste “un dataset neutro degli interventi”. Il dataset registra decisioni operative già basate sul rischio. Di conseguenza la domanda generica “quale intervento funziona?” viene sostituita da quattro estimand differenti.

Per la **chiamata CS** il team vuole l'effetto della chiamata entro 48 ore sul churn D90 per account con health score vicino a 65. Per il **training** vuole l'effetto aggiuntivo tra account con bassa adoption nell'area in cui esistono controlli osservazionalmente comparabili. Per lo **sconto** vuole l'effetto del 15% sul rinnovo tra account eleggibili e ancora contendibili. Per la **revisione tecnica** vuole l'effetto di una sessione standardizzata sul rinnovo D90 degli account con integrazione incompleta.

Appena gli estimand diventano espliciti, diventa anche evidente che non serve — e non sarebbe corretto usare — lo stesso metodo per tutti.

### Chiamata CS — La soglia crea un'opportunità RDD

La policy `health_score < 65` è applicata abbastanza rigidamente. Il team verifica la distribuzione dello score vicino alla soglia, l'assenza di manipolazione evidente, la continuità di ARR, tenure e usage pre-treatment, l'assenza di altri benefit che scattino esattamente a 65 e la stabilità del risultato su bandwidth ragionevoli.

Vicino alla soglia, il churn stimato senza chiamata è **16,2%** e con chiamata **12,7%**: una discontinuità locale di circa `-3,5 pp`.

La conclusione non diventa “le chiamate riducono il churn di 3,5 punti per tutti”. Il claim consentito è più stretto:

> **Vicino alla soglia di health score 65, l'assegnazione della chiamata è compatibile con una riduzione locale del churn di circa 3,5 punti percentuali, sotto le assunzioni RDD.**

Il design è forte proprio perché rinuncia a generalizzare oltre la popolazione che rende credibile il confronto.

### Training — Comparabilità osservata, limite non osservato

Per il training non esiste una soglia o una fonte quasi-random. Il team costruisce quindi comparabilità usando covariate pre-treatment: ARR, industry, tenure, utenti, adoption pre-intervento, health score storico e ticket precedenti. Controlla overlap e balance; una parte degli account enterprise viene esclusa perché non esistono controlli comparabili.

Nel campione con common support il churn è **14,8%** tra i clienti con training e **17,1%** nei matched controls: una differenza di `-2,3 pp`.

Ma le interviste rivelano che la **qualità del champion interno** influenza fortemente la decisione di offrire training e non è registrata bene. Il matching ha migliorato la comparabilità sulle variabili osservate, non ha cancellato il confounding non osservato.

Il claim rimane quindi condizionato:

> **Nel segmento con overlap, il training è associato a circa 2,3 pp di churn in meno dopo bilanciamento delle covariate osservate; confounding non osservato rimane plausibile.**

Questa è una buona analisi proprio perché non finge di avere una causal claim più forte di quella che il dato sostiene.

### Sconto — Quando la risposta professionale è “non identificato”

Lo sconto viene concesso dopo conversazioni qualitative come “il procurement ha già chiesto exit terms”, “il champion sta lasciando l'azienda” o “il budget è stato congelato”. Queste informazioni non sono strutturate nel CRM storico. Sono però esattamente il tipo di variabili che influenzano sia assegnazione dello sconto sia rinnovo.

Matching e regressione non possono controllarle in modo credibile. Il team decide quindi:

> **nessuna causal estimate dallo storico.**

Propone un esperimento su account eleggibili per cui esista vera incertezza operativa sulla concessione del discount. Non produrre un coefficiente evita di trasformare un buco di measurement in una falsa certezza causale.

### Revisione tecnica — Il pilot randomizzato cambia la qualità dell'evidenza

Per nuovi account con integrazione incompleta, Asteria randomizza la disponibilità immediata di una sessione tecnica standardizzata. Nel pilot il churn D90 è **18,0%** nel controllo e **14,9%** nel trattamento, per una differenza di `-3,1 pp`.

L'eterogeneità era stata definita prima del test:

| Complessità integrazione | Effetto stimato |
|---|---:|
| semplice | -0,6 pp |
| media | -2,7 pp |
| complessa | -7,9 pp |

Gli intervalli sono più larghi nei sottogruppi, quindi il team non trasforma subito il `-7,9 pp` in una policy definitiva. Il pattern è coerente con l'ipotesi e merita replica, ma la precisione per segmento è inferiore a quella dell'effetto complessivo.

### Quattro numeri, quattro livelli di evidenza

La sintesi utile non è una classifica degli effect size. È una tabella che conserva **design e scope**:

| Intervento | Design disponibile | Scope | Claim |
|---|---|---|---|
| Chiamata CS | RDD | account vicino a score 65 | causale locale, se assumptions reggono |
| Training | matching | area di common support | causale solo sotto no-unmeasured-confounding |
| Sconto | storico fortemente selettivo | nessuno affidabile | effetto non identificato |
| Revisione tecnica | randomized pilot | account eleggibili al pilot | effetto sperimentale nella popolazione studiata |

Questa tabella è molto più utile di una classifica di coefficienti perché dice **quanto possiamo fidarci di ogni riga e per chi**.

Il team chiude con un Causal Identification Brief:

```text
DECISIONE
Allocare capacità Customer Success tra quattro interventi.

ESTIMAND
Definito separatamente per ogni trattamento.

ASSIGNMENT
Soglia / giudizio umano / randomizzazione a seconda dell'intervento.

CONFOUNDING
Molto forte nello storico, soprattutto per sconto e problemi tecnici.

IDENTIFICATION
RDD per chiamata; matching per training; nessuna stima storica per sconto;
RCT pilot per revisione tecnica.

DIAGNOSTICS
Continuity e bandwidth RDD; overlap/balance matching;
compliance e baseline checks nel pilot.

EFFECT
Non un unico numero: effetti con scope e incertezza differenti.

EXTERNAL VALIDITY
RDD locale; matching solo nell'area di overlap;
pilot applicabile alla popolazione eleggibile studiata.

DECISIONE
Prioritizzare evidence-generating rollout e interventi con effect × economics favorevole;
testare lo sconto prima di scalarlo.

PROSSIMO TEST
Replica del technical pilot e randomized eligibility per discount.
```

Il contributo dell'analista non è stato applicare quattro tecniche sofisticate. È stato rifiutare il confronto grezzo, ricostruire l'assignment mechanism, specificare estimand diversi, scegliere il design dalla struttura operativa, distinguere causalità forte, causalità condizionata e associazione, e dire esplicitamente dove il dato non consente una risposta.

> **La migliore causal analysis non è quella che produce una stima per ogni domanda. È quella che distingue quali domande il sistema di dati può identificare, quali richiedono nuove assunzioni e quali richiedono un nuovo esperimento.**
