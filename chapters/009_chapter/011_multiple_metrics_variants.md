## 9.10 Multiple metriche e multiple varianti: più domande, più possibilità di illudersi

In un esperimento reale raramente guardiamo una sola metrica. Ci sono conversion, revenue, retention, latency, error rate, engagement, cancellazioni, support ticket e spesso decine di segmenti.

Il problema è semplice: **più confronti facciamo, più aumenta la probabilità di trovare almeno un risultato apparentemente significativo per puro caso**.

### Caso simulato/composito - La variante vincente trovata dopo 48 confronti

Un e-commerce testa quattro versioni della pagina prodotto: A, B, C e D. Il team osserva:

- conversion rate;
- add-to-cart rate;
- revenue per session;
- average order value;
- return rate;
- tempo sulla pagina;
- click sulle recensioni;
- click sulle immagini.

Poi segmenta i risultati per desktop/mobile e per nuovi/ritornanti.

Quattro varianti, otto metriche e quattro segmentazioni generano decine di confronti. Il team scopre che la variante C aumenta del 6,8% i click sulle recensioni tra i nuovi utenti mobile, con p = 0,031.

La slide del meeting dice: "C migliora significativamente l'engagement".

Ma quella metrica non era primaria, il segmento non era predefinito e il confronto emerge da una lunga esplorazione post-hoc. È esattamente il tipo di risultato che può comparire per caso quando si cercano abbastanza combinazioni.

L'analista ricostruisce la gerarchia decisionale:

1. metrica primaria: revenue per eligible user;
2. guardrail: return rate ed errori checkout;
3. secondary metrics: conversion e add-to-cart;
4. analisi esplorative: segmenti e interaction effects.

Nessuna variante mostra un vantaggio convincente sulla metrica primaria. Il test viene classificato come inconclusivo, mentre il segnale su C viene trasformato in una nuova ipotesi da testare in un esperimento successivo.

### Multiple variants

Con più varianti, non basta chiedere se ogni variante differisce dal controllo. Possiamo avere:

- A vs B;
- A vs C;
- A vs D;
- B vs C;
- B vs D;
- C vs D.

Ogni confronto aggiuntivo aumenta il rischio di false discovery se non è previsto nella strategia statistica.

### Approcci possibili

A seconda del contesto si possono usare correzioni come:

- Bonferroni;
- Holm;
- False Discovery Rate;
- gerarchie di metriche e gatekeeping;
- pre-registrazione delle ipotesi principali.

Nel lavoro di un Data Analyst il concetto più importante non è ricordare tutte le formule, ma **distinguere ciò che era una domanda decisionale predefinita da ciò che abbiamo scoperto esplorando dopo aver visto i dati**.

> Un pattern post-hoc può essere un'ottima ipotesi. Non diventa automaticamente una conferma solo perché il p-value è piccolo.
