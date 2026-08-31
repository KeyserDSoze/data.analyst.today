## 9.17 Checklist operativa: un esperimento affidabile dall'idea alla decisione

Un buon A/B test non nasce dalla query finale. Nasce molto prima, quando il team decide cosa vuole imparare e quale decisione dovrà prendere.

Questa checklist riassume il flusso operativo del capitolo.

### Prima del test

- Qual è la decisione che il test deve supportare?
- Qual è l'ipotesi causale?
- Qual è l'unità di randomizzazione?
- Qual è la popolazione eleggibile?
- Qual è la metrica primaria?
- Quali sono le guardrail metrics?
- Qual è il MDE rilevante per il business?
- Qual è il sample size necessario?
- Qual è la durata minima per coprire cicli temporali rilevanti?
- Esistono rischi di contaminazione o network effects?
- Quali segmenti devono essere controllati?
- Esistono esperimenti concorrenti potenzialmente interagenti?
- Quali criteri determinano stop anticipato, rollback o invalidazione?

### Durante il test

- L'allocazione osservata rispetta quella prevista?
- Esiste Sample Ratio Mismatch?
- L'assignment è stabile?
- La treatment exposure è corretta?
- Il logging è completo?
- Le metriche pre-trattamento sono bilanciate?
- Le guardrail sono sane?
- Il team sta facendo peeking non previsto?
- Sono comparsi incidenti operativi o cambiamenti esterni importanti?

### Alla fine del test

- Il test ha raggiunto il sample size previsto?
- La finestra temporale è sufficiente?
- La metrica primaria si è mossa?
- Quanto è grande l'effetto?
- Qual è l'intervallo di confidenza?
- L'effetto è economicamente rilevante?
- Le guardrail sono compatibili con il rollout?
- Esistono effetti eterogenei importanti?
- I risultati sono coerenti con la meccanica attesa?
- Ci sono segnali di novelty o learning effect?
- Il risultato è replicabile o richiede un secondo test?

### Dopo il test

- Rollout immediato o progressivo?
- Quali metriche monitorare durante il rollout?
- Quali sono le soglie di rollback?
- Quali segmenti erano poco rappresentati?
- Cosa abbiamo imparato anche se il test è neutro?
- Il risultato modifica la nostra understanding del prodotto?
- L'esperimento deve essere documentato per evitare test duplicati?

### Il documento minimo di chiusura

Ogni esperimento importante dovrebbe lasciare una traccia con:

1. domanda;
2. ipotesi;
3. design;
4. popolazione;
5. metriche;
6. health checks;
7. risultati;
8. incertezza;
9. decisione;
10. rollout/rollback plan;
11. learnings.

> **Un esperimento non è concluso quando conosciamo il p-value. È concluso quando il team sa cosa ha imparato, quale decisione prende e quali rischi restano.**
