## 8.15 Caso simulato/composito — Quale intervento riduce davvero il churn?

**Asteria Cloud** è un SaaS B2B immaginario con 42 milioni di euro di ARR. Il churn annualizzato è salito dal 9,6% all'11,8%.

Il management vuole aumentare l'investimento in Customer Success e chiede:

> **“Quale intervento riduce davvero il churn e su quali clienti dovremmo usarlo?”**

Sono già in uso quattro azioni:

1. chiamata proattiva Customer Success;
2. sessione di training aggiuntiva;
3. sconto temporaneo del 15%;
4. revisione tecnica dell'integrazione.

### 1. Il confronto osservato produce la conclusione sbagliata

Churn a 90 giorni:

| Intervento osservato | Churn |
|---|---:|
| nessun intervento | 8,1% |
| chiamata CS | 19,4% |
| training | 14,8% |
| sconto | 22,1% |
| revisione tecnica | 17,3% |

Una lettura ingenua direbbe che ogni intervento peggiora il churn.

Ma il trattamento non è assegnato a caso.

Gli operatori intervengono quando vedono rischio.

### 2. Prima del modello: ricostruire l'assignment mechanism

Intervistando Customer Success emerge:

- chiamata: quasi automatica quando `health_score < 65`;
- training: offerto soprattutto a clienti con bassa adoption ma relationship ancora buona;
- sconto: deciso dopo conversazioni qualitative con procurement o champion;
- revisione tecnica: proposta quando sono presenti problemi di integrazione;
- alcuni account ricevono più interventi insieme.

Questa intervista vale quanto molte ore di modellazione.

Rivela che non esiste “un dataset neutro degli interventi”.

Il dataset registra **decisioni operative già basate sul rischio**.

### 3. Scrivere quattro estimand diversi

Il team evita la domanda vaga “quale intervento funziona?”.

Definisce quattro estimand.

**Chiamata CS**

> Effetto della chiamata entro 48 ore sul churn D90 per account con health score vicino a 65.

**Training**

> Effetto del training aggiuntivo sul churn D90 tra account con bassa adoption e area di overlap osservabile.

**Sconto**

> Effetto del 15% discount sul rinnovo tra account eleggibili e ancora contendibili.

**Revisione tecnica**

> Effetto di una sessione tecnica standardizzata sul rinnovo D90 tra account con integrazione incompleta.

Ora è evidente che non serve necessariamente lo stesso metodo per tutti.

### 4. Chiamata CS — Opportunità RDD

La policy `health_score < 65` è applicata in modo abbastanza rigido.

Il team verifica:

- distribuzione dello score vicino a 65;
- assenza di manipolazione evidente;
- continuità di ARR, tenure e usage pre-treatment;
- nessun altro benefit che scatti esattamente a 65;
- risultati con più bandwidth ragionevoli.

Vicino alla soglia:

- churn stimato senza chiamata: 16,2%;
- churn con chiamata: 12,7%;
- discontinuità locale: circa `-3,5 pp`.

**Claim consentito:**

> “Vicino alla soglia di health score 65, l'assegnazione della chiamata è compatibile con una riduzione locale del churn di circa 3,5 punti percentuali, sotto le assunzioni RDD.”

Non:

> “Le chiamate riducono il churn di 3,5 punti per tutti.”

### 5. Training — Matching con limite esplicito

Non esiste una soglia o fonte quasi-random.

Il team usa covariate pre-treatment:

- ARR;
- industry;
- tenure;
- utenti;
- adoption pre-intervento;
- health score storico;
- ticket precedenti.

Controlla overlap e balance. Una parte degli account enterprise viene esclusa perché non esistono controlli comparabili.

Nel campione con common support:

- churn training: 14,8%;
- matched comparison: 17,1%;
- differenza: `-2,3 pp`.

Ma dalle interviste emerge che “qualità del champion interno” influenza fortemente la decisione di offrire training e non è registrata bene.

**Claim consentito:**

> “Nel segmento con overlap, il training è associato a circa 2,3 pp di churn in meno dopo bilanciamento delle covariate osservate; confounding non osservato rimane plausibile.”

Questa è una buona analisi anche se non produce una frase causale forte.

### 6. Sconto — Il dato storico non identifica l'effetto

Gli sconti vengono proposti dopo conversazioni qualitative come:

- “il procurement ha già chiesto exit terms”;
- “il champion sta lasciando l'azienda”;
- “il budget è stato congelato”.

Queste informazioni non sono strutturate nel CRM storico.

Matching e regressione non possono controllarle in modo credibile.

Il team decide quindi:

> **nessuna causal estimate dallo storico.**

Propone un esperimento su account eleggibili per cui esiste vera incertezza operativa sulla concessione dello sconto.

Dire “non identificabile con questi dati” evita di spendere un budget importante su una causal claim inventata.

### 7. Revisione tecnica — Pilot randomizzato

Per nuovi account con integrazione incompleta, l'azienda randomizza la disponibilità immediata di una sessione tecnica standardizzata.

Nel pilot:

- controllo: churn D90 18,0%;
- trattamento: 14,9%;
- differenza: `-3,1 pp`.

L'analisi di heterogeneity, definita prima del test, mostra:

| Complessità integrazione | Effetto stimato |
|---|---:|
| semplice | -0,6 pp |
| media | -2,7 pp |
| complessa | -7,9 pp |

Gli intervalli sono più larghi nei sottogruppi, quindi il team tratta il pattern come una combinazione di evidenza pre-specificata e bisogno di replica.

### 8. Una tabella non deve fingere che tutte le evidenze siano equivalenti

| Intervento | Design disponibile | Scope | Claim |
|---|---|---|---|
| Chiamata CS | RDD | account vicino a score 65 | causale locale, se assumptions reggono |
| Training | matching | area di common support | causale solo sotto no-unmeasured-confounding |
| Sconto | storico fortemente selettivo | nessuno affidabile | effetto non identificato |
| Revisione tecnica | randomized pilot | account eleggibili al pilot | effetto sperimentale nella popolazione studiata |

Questa tabella è più utile di una classifica di coefficienti.

Dice **quanto possiamo fidarci di ogni riga**.

### 9. Causal Identification Brief finale

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

### 10. La lezione professionale

Il contributo dell'analista non è stato applicare quattro tecniche sofisticate.

È stato:

- rifiutare il confronto grezzo;
- ricostruire come nasce il trattamento;
- specificare l'estimand;
- scegliere il design dalla struttura operativa;
- distinguere causalità forte, causalità condizionata e associazione;
- dire esplicitamente dove il dato non consente una risposta;
- collegare evidenza e prossima decisione.

> **La migliore causal analysis non è quella che produce una stima per ogni domanda. È quella che sa distinguere quali domande il sistema di dati può identificare, quali richiedono nuove assunzioni e quali richiedono un nuovo esperimento.**
