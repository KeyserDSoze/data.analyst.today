## 8.10 Regression discontinuity: quando una soglia crea un quasi-esperimento

Molti processi aziendali applicano regole di eleggibilità basate su una soglia:

- sconto disponibile sopra un certo valore;
- account manager assegnato oltre un ARR minimo;
- finanziamento approvato sopra un credit score;
- bonus riconosciuto oltre una performance threshold;
- programma retention attivato sotto un certo health score.

Queste soglie possono creare opportunità di identificazione causale.

### Caso realistico: programma retention per clienti a rischio

Una società SaaS decide che tutti i clienti con health score inferiore a **60** ricevano automaticamente una chiamata proattiva dal Customer Success.

Dopo tre mesi il team vuole sapere se la chiamata riduce il churn.

Confrontare tutti i trattati con tutti i non trattati sarebbe pessimo: i trattati sono, per definizione, clienti più a rischio.

Ma possiamo osservare clienti appena sotto e appena sopra la soglia:

- score 58-59: ricevono il trattamento;
- score 60-61: non lo ricevono.

Se il punteggio è continuo e non manipolabile, questi clienti possono essere molto simili in tutto tranne che nell'accesso all'intervento.

Risultato nei 30 giorni:

| Fascia | Trattamento | Churn |
|---|---|---:|
| 58-59 | sì | 13,2% |
| 60-61 | no | 16,7% |

Il salto locale è di circa **-3,5 punti percentuali**.

Questa è l'intuizione della **Regression Discontinuity Design (RDD)**.

### Perché funziona

La World Bank descrive l'RDD come un metodo quasi-sperimentale che confronta unità immediatamente sopra e sotto un cutoff che determina l'eleggibilità. L'idea è che molto vicino alla soglia i gruppi siano simili, mentre il trattamento cambia in modo discontinuo.

### Sharp e fuzzy RDD

Nella **sharp RDD**, la soglia determina perfettamente il trattamento.

Esempio:

- score < 60 -> chiamata;
- score >= 60 -> nessuna chiamata.

Nella **fuzzy RDD**, la soglia cambia fortemente la probabilità del trattamento, ma non la determina perfettamente.

Per esempio alcuni account manager possono chiamare anche clienti con score 61 oppure saltare alcuni clienti con score 59.

### L'effetto è locale

Una RDD non dimostra necessariamente che il programma funzioni allo stesso modo per tutti.

L'effetto stimato vale soprattutto **intorno alla soglia**.

Se la chiamata aiuta un cliente con health score 59, non possiamo automaticamente concludere che avrebbe lo stesso effetto su un cliente con score 25.

### Manipolazione della soglia

Supponiamo che i commerciali sappiano che sopra i 100.000 euro di ARR un cliente riceve supporto premium. Potrebbero anticipare o riclassificare contratti per superare la soglia.

Se le unità possono manipolare il running variable, la comparabilità locale può rompersi.

### Un caso pricing

Un retailer B2B concede spedizione gratuita agli ordini sopra **500 euro**.

Il management osserva che gli ordini sopra 500 euro hanno un repeat rate più alto e conclude che la spedizione gratuita aumenta la fedeltà.

Un'analisi RDD confronta ordini appena sotto e appena sopra la soglia, per esempio 480-499 contro 500-519 euro, osservando il repeat purchase nei 90 giorni successivi.

Se emerge un salto netto nel repeat rate proprio a 500 euro, l'ipotesi causale diventa più credibile.

### Checklist RDD

Prima di fidarsi del disegno chiedere:

1. la soglia determina davvero il trattamento?
2. il punteggio è misurato in modo affidabile?
3. può essere manipolato?
4. le covariate sono continue intorno alla soglia?
5. esistono altri cambiamenti che avvengono allo stesso cutoff?
6. la finestra scelta è abbastanza stretta da garantire comparabilità ma abbastanza ampia da fornire dati?

### Regola pratica

> **Una soglia amministrativa può trasformarsi in un quasi-esperimento, ma solo se vicino alla soglia cambia il trattamento e non cambia contemporaneamente tutto il resto.**

### Riferimenti

- World Bank DIME Wiki, *Regression Discontinuity*.
- World Bank, *Impact Evaluation in Practice*, capitolo sulla regression discontinuity.
