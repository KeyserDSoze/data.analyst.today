## 15.7 Switching threshold: quale valore farebbe cambiare decisione?

Nei capitoli precedenti abbiamo già incontrato soglie statistiche, soglie predittive e criteri di rollout.

Qui il concetto è diverso.

La domanda centrale del Decision Record è:

> **quanto deve cambiare una delle assunzioni chiave perché un'altra alternativa diventi preferibile?**

Questa è una **switching threshold**.

### Dalla domanda “qual è la stima?” alla domanda “dove cambia la scelta?”

Supponiamo che un progetto sia conveniente con:

```text
uplift atteso: +6%
costo: €400k
margine incrementale: €650k
```

La stima centrale da sola dice poco sulla robustezza.

Due casi:

**Caso A**

Il progetto diventa negativo se l'uplift scende da 6% a 5,4%.

**Caso B**

Il progetto resta preferibile fino a un uplift di 2%.

Stessa stima centrale.

Decisioni con fragilità completamente diversa.

### Caso pubblico documentato — switching values nel Green Book

Il Green Book 2026 di HM Treasury raccomanda sensitivity analysis e **switching values** per identificare il valore al quale una variabile rende un'opzione non più preferibile o non più value for money.

Fonte: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

Il concetto è molto utile anche nel lavoro analitico aziendale perché sposta l'attenzione da una precisione artificiale a una domanda decisionale concreta:

> “Quanto possiamo sbagliare su questa assunzione prima che la raccomandazione cambi?”

### Le soglie possono riguardare variabili molto diverse

**Economics**

```text
CAC massimo sostenibile
costo implementazione massimo
margine minimo
saving minimo
```

**Performance**

```text
uplift minimo
conversion loss massima
forecast error massimo
```

**Rischio**

```text
probabilità massima di failure
customer complaints massime
churn guardrail
```

**Tempo**

```text
time-to-value massimo
delay oltre il quale l'opzione perde senso
```

**Capacità**

```text
numero minimo di casi trattabili
headcount massimo richiesto
```

### Caso simulato/composito — build vs buy

Un team deve scegliere tra costruire internamente un sistema di reporting o acquistare una soluzione esterna.

Stima centrale:

```text
Build
costo iniziale: €600k
maintenance: €180k/anno
lead time: 8 mesi

Buy
licenza + servizi: €310k/anno
lead time: 2 mesi
```

Dire soltanto “Buy costa meno nel primo anno” è insufficiente.

Il team calcola alcune switching questions:

- a quale costo annuale della licenza Build diventa preferibile?
- a quale maintenance interna Buy continua a dominare?
- quanto vale economicamente arrivare 6 mesi prima?
- quanti anni di utilizzo sono necessari perché il costo iniziale di Build venga recuperato?
- quanto pesa il rischio di lock-in?

La scelta diventa leggibile perché possiamo indicare **le condizioni che la fanno cambiare**.

### Evidence threshold e switching threshold non sono la stessa cosa

**Evidence threshold**

> Quanta evidenza richiediamo prima di agire?

**Switching threshold**

> Quale valore dell'assunzione cambia la preferenza tra alternative?

Sono collegati.

Se la nostra stima di CAC è €1.800 e la switching threshold è €1.850, serve grande precisione prima di investire.

Se la soglia è €3.000, una stima meno precisa può essere sufficiente.

Quindi il livello di evidenza dipende anche dalla **distanza dalla decision boundary**.

### Caso simulato/composito — pricing di Meridian Cloud

Meridian Cloud aumenta il prezzo SMB.

Dopo il cambiamento:

- conversion: -2,1 pp;
- ARPU: +11%;
- revenue per visitor: +4,3%.

Un manager propone rollback immediato perché conversion è peggiorata.

Il Decision Record contiene però:

```text
objective:
contribution margin / visitor

guardrails:
churn 90d
support burden
SMB acquisition volume
```

La domanda non è:

> “conversion è diminuita?”

È:

> “A quale aumento di churn o perdita di acquisition il nuovo prezzo smette di creare valore complessivo?”

Il team definisce queste soglie **prima** di interpretare i dati futuri.

Questo evita di cambiare metrica ogni volta che un outcome è scomodo.

### Una soglia deve avere una regola operativa

Debole:

> “Se il churn peggiora molto, facciamo rollback.”

Forte:

```text
if churn_90d_delta > +1,5 pp
AND sample/readiness gate passed
THEN executive review

if contribution_margin_per_visitor < baseline for 2 mature cohorts
THEN rollback candidate
```

La soglia deve chiarire:

- metrica;
- popolazione;
- finestra;
- maturità del dato;
- azione conseguente.

### Non tutte le soglie devono essere automatiche

Per decisioni complesse, superare una soglia può significare:

- review;
- escalation;
- nuova analisi;
- stop di un rollout;

non necessariamente azione automatica.

Esempio:

```text
supplier delay risk > threshold
→ procurement review
```

non:

```text
→ ordine alternativo automatico
```

se esistono relazioni strategiche e costi non rappresentati dal modello.

### Robustness margin

Possiamo descrivere una decisione con la distanza dalla soglia.

```text
estimated CAC: €1.700
switching CAC: €2.400
margin: €700
```

è molto diverso da:

```text
estimated CAC: €2.320
switching CAC: €2.400
margin: €80
```

Nel secondo caso una piccola revisione del dato può cambiare scelta.

La recommendation dovrebbe comunicarlo:

> “L'opzione è preferita, ma la decisione è vicina al punto di indifferenza.”

### Campo del Decision Record

```text
critical variable:
central estimate/range:
switching value:
distance to threshold:
evidence quality around threshold:
action if crossed:
measurement maturity required:
```

### Regola operativa

Per ogni raccomandazione importante chiediamo:

1. quali 2–5 variabili governano realmente il ranking?
2. a quale valore cambia l'opzione preferita?
3. quanto siamo lontani da quel valore?
4. quanto è affidabile la stima proprio vicino alla soglia?
5. quale azione scatta se la soglia viene superata?
6. la soglia è stata definita prima dell'esito?

> **La stima centrale ci dice dove pensiamo di essere. Lo switching value ci dice quanto deve cambiare il mondo perché dovremmo scegliere diversamente. Per una decisione, spesso la seconda informazione è più preziosa della prima.**
