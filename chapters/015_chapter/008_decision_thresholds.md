## 15.7 Switching threshold: dove cambia la scelta?

Nei capitoli precedenti abbiamo incontrato soglie statistiche, soglie predittive e criteri di rollout. Qui la soglia ha un significato diverso: **quale valore deve assumere una delle nostre assunzioni perché un'altra alternativa diventi preferibile?**

Questa è una *switching threshold*. Sposta l'attenzione dalla precisione della stima centrale alla robustezza della decisione.

Supponiamo che un progetto abbia uplift atteso +6%, costo €400k e margine incrementale €650k. In un primo caso il progetto diventa negativo se l'uplift scende appena a 5,4%; in un secondo resta preferibile fino al 2%. La stima centrale è identica. La fragilità della recommendation è completamente diversa.

Il *Green Book 2026* usa esplicitamente sensitivity analysis e **switching values** per identificare il valore al quale un'assunzione rende un'opzione non più value for money o meno attraente di un'alternativa.[^green-book-switching] Nel nostro contesto la domanda diventa:

> **Quanto possiamo sbagliare su questa assunzione prima che dovremmo scegliere diversamente?**

Le soglie possono riguardare economics, performance, rischio, tempo o capacità: CAC massimo sostenibile, costo implementazione massimo, uplift minimo, conversion loss massima, churn guardrail, time-to-value oltre il quale l'opzione perde senso oppure numero minimo di casi che Operations può realmente trattare.

### Build vs buy: il valore è nelle condizioni che ribaltano il confronto

Un team deve scegliere tra costruire internamente un sistema di reporting o acquistare una soluzione esterna.

```text
Build
costo iniziale: €600k
maintenance: €180k/anno
lead time: 8 mesi

Buy
licenza + servizi: €310k/anno
lead time: 2 mesi
```

Dire che Buy costa meno nel primo anno non basta. Il Decision Record deve chiedere: a quale costo annuale della licenza Build diventa preferibile? A quale maintenance interna Buy continua a dominare? Quanto vale economicamente arrivare sei mesi prima? Quanti anni di utilizzo servono per recuperare il costo iniziale di Build? Quanto pesa il lock-in?

La decisione diventa leggibile quando possiamo descrivere **le condizioni che la fanno cambiare**.

### Evidence threshold e switching threshold rispondono a domande diverse

L'**evidence threshold** chiede quanta evidenza vogliamo prima di agire. La **switching threshold** chiede quale valore cambia la preferenza tra opzioni.

I due concetti si incontrano nella distanza dal decision boundary. Se stimiamo CAC €1.800 e la soglia è €1.850, una piccola revisione del dato può ribaltare la scelta: serve informazione molto più precisa. Se la soglia è €3.000, una stima meno stretta può essere sufficiente.

Quindi il livello di evidenza non dipende soltanto dalla criticità della decisione, ma anche da **quanto siamo vicini al punto di indifferenza**.

### Meridian Cloud: non cambiare metrica dopo aver visto l'esito

Meridian Cloud aumenta il prezzo SMB. Dopo il cambiamento:

- conversion: -2,1 pp;
- ARPU: +11%;
- revenue per visitor: +4,3%.

Un manager propone rollback perché conversion è peggiorata. Ma il Decision Record aveva definito come obiettivo contribution margin per visitor e come guardrail churn a 90 giorni, support burden e SMB acquisition volume.

La domanda rilevante non è quindi “conversion è diminuita?”, ma:

> **A quale aumento di churn o perdita di acquisition il nuovo prezzo smette di creare valore complessivo?**

Definire queste soglie **prima** dei dati futuri impedisce di cambiare metrica ogni volta che un outcome è scomodo.

Una soglia deve inoltre contenere la propria regola operativa. “Se il churn peggiora molto, facciamo rollback” è ambiguo. Una policy più seria specifica metrica, popolazione, finestra, maturità del dato e conseguenza:

```text
if churn_90d_delta > +1,5 pp
AND sample/readiness gate passed
THEN executive review

if contribution_margin_per_visitor < baseline for 2 mature cohorts
THEN rollback candidate
```

Superare la soglia non significa sempre azione automatica. Può attivare una review, un'escalation, una nuova analisi o lo stop di un rollout quando esistono costi e vincoli non rappresentati dal modello.

### Robustness margin

La distanza tra stima e soglia è una misura intuitiva della fragilità:

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

Nel secondo caso una piccola revisione può cambiare ranking. La recommendation dovrebbe dirlo apertamente: **l'opzione è preferita, ma siamo vicini al punto di indifferenza**.

Nel Decision Record conserviamo quindi:

```text
critical variable:
central estimate / range:
switching value:
distance to threshold:
evidence quality around threshold:
action if crossed:
measurement maturity required:
```

> **La stima centrale dice dove pensiamo di essere. Lo switching value dice quanto deve cambiare il mondo perché dovremmo scegliere diversamente. Per una decisione, spesso la seconda informazione è più preziosa della prima.**

[^green-book-switching]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
