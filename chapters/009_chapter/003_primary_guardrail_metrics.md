## 9.2 Metriche primarie e guardrail: vincere senza fare danni

Un esperimento raramente ha una sola conseguenza. Ottimizzare una metrica senza guardare il resto del sistema può produrre una vittoria locale e una perdita complessiva.

Per questo è utile distinguere almeno tre famiglie di metriche:

- **primary metric**: la metrica principale che rappresenta l'obiettivo del test;
- **secondary metrics**: aiutano a capire il meccanismo e gli effetti collaterali;
- **guardrail metrics**: metriche che non devono peggiorare oltre una soglia accettabile.

### Caso: conversione in aumento, qualità dell'ordine in calo

Il checkout rapido dell'e-commerce viene testato su 620.000 utenti per variante.

Risultato iniziale:

| Metrica | Controllo | Trattamento | Delta |
|---|---:|---:|---:|
| Conversion rate | 3,93% | 4,12% | +0,19 pp |
| Ordini | 24.366 | 25.544 | +4,8% |

Il team Product celebra. Ma l'analista aveva definito guardrail prima dell'esperimento:

| Guardrail | Controllo | Trattamento |
|---|---:|---:|
| Chargeback rate | 0,42% | 0,61% |
| Cancellation rate entro 24h | 2,8% | 3,6% |
| Customer support contacts / 1.000 ordini | 14,1 | 18,7 |

La variante B genera più ordini ma anche più ordini problematici.

Se il margine medio per ordine è 17,40 euro, l'incremento lordo sembra positivo. Ma dopo costi di chargeback, assistenza e cancellazioni, il margine incrementale scende molto.

### Una metrica primaria deve corrispondere alla decisione

La conversione può essere utile, ma se la decisione è “questa esperienza crea più valore sostenibile?”, allora una metrica come revenue netta per utente o contribution margin per utente potrebbe essere più coerente.

La scelta della primary metric deve avvenire **prima** del risultato. Cambiarla dopo aver visto i dati apre la porta al cherry-picking.

### Guardrail non significa metrica decorativa

Una guardrail deve avere una regola di decisione esplicita.

Esempio:

- primary metric: conversion rate;
- criterio di successo: aumento minimo +0,10 pp;
- guardrail chargeback: non oltre +0,08 pp;
- guardrail support contacts: non oltre +10%;
- durata minima: 14 giorni.

A questo punto il test può avere quattro esiti:

1. primary migliora, guardrail ok -> candidato al rollout;
2. primary migliora, guardrail fallisce -> non rollout o redesign;
3. primary non migliora, guardrail ok -> nessuna evidenza sufficiente;
4. primary peggiora -> stop.

### Metric hierarchy

Nei sistemi maturi le metriche formano una gerarchia:

**business outcome -> product behavior -> diagnostic metrics -> system health**

Per un marketplace:

- business outcome: contribution margin;
- product behavior: completed transactions;
- diagnostic: add-to-cart, checkout completion;
- system health: latency, error rate, fraud rate.

Questa struttura evita di confondere una proxy con l'obiettivo finale.

### Errore tipico

Il problema non è avere molte metriche. Il problema è non sapere quali guidano la decisione e quali servono solo a interpretarla.

> Un esperimento ben progettato decide prima che cosa significa vincere e anche che cosa significa vincere troppo caro.