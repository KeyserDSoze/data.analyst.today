## 2.2 Specificare la decisione prima di progettare l'output

Molte richieste arrivano già nella forma di un deliverable:

- “Mi fai una dashboard?”
- “Mi serve un report settimanale.”
- “Vorrei vedere questi KPI.”
- “Puoi fare un grafico per regione?”

Il deliverable può essere appropriato. Ma non è ancora il requisito fondamentale.

Prima dobbiamo capire **quale decisione, controllo o comportamento dovrebbe migliorare** grazie a quell'output.

### La decision specification

Per il brief è utile annotare cinque elementi.

**Decisione.** Che cosa deve essere scelto, modificato o monitorato?

**Owner.** Chi ha l'autorità di agire?

**Alternative.** Quali opzioni sono realmente disponibili?

**Timing.** Quando deve essere presa la decisione e con quale frequenza si ripete?

**Conseguenze dell'errore.** Che cosa costa agire troppo presto, troppo tardi o nella direzione sbagliata?

Queste informazioni cambiano direttamente il disegno dell'analisi.

### Tre decisioni, tre prodotti diversi

**Monitoraggio operativo.**

Ogni mattina il responsabile logistico deve decidere quali spedizioni richiedono intervento. Qui possono servire dati freschi, alert e un'interfaccia ricorrente.

**Diagnosi ad hoc.**

La conversione è scesa del 12% e il product team deve capire quale parte del funnel investigare. Una EDA mirata e un memo possono essere più utili di una dashboard permanente.

**Scelta tra alternative.**

Il team commerciale deve decidere tra sconto, spedizione gratuita e nessun intervento. Servono scenari, impatto economico, guardrail e incertezza.

Lo stesso database può alimentare tutti e tre i casi. Il prodotto analitico cambia perché cambia la decisione.

### La domanda che smaschera i report senza uso

Prova a completare:

> **“Se scoprissimo che ________, il decision owner potrebbe decidere di ________.”**

Se nessun risultato plausibile porta a una scelta diversa, il lavoro può avere comunque valore informativo, ma non dovremmo presentarlo come decision support senza chiarire il processo che lo userà.

### Decisione e soglia d'azione

Quando possibile, il brief dovrebbe anticipare anche che cosa renderebbe un risultato abbastanza importante da modificare una scelta.

Per esempio:

> “Se il nuovo processo riduce il tempo di evasione di almeno il 10% senza aumentare gli errori oltre 0,5 punti percentuali, valuteremo il rollout.”

Non sempre una soglia può essere definita prima dell'analisi. Ma provare a farlo evita che, dopo aver visto il risultato, si sposti arbitrariamente il criterio con cui lo giudichiamo.

Il **Capitolo 15** entrerà molto più in profondità su soglie, expected value, trade-off e qualità della decisione. Qui la funzione della decision specification è più semplice: **impedire che l'analisi venga progettata senza sapere come verrà usata**.

### Campo del brief

```text
Decisione:
Decision owner:
Alternative disponibili:
Deadline/frequenza:
Costo principale dell'errore:
Soglia o criterio d'azione, se definibile:
```

> **Prima di scegliere il formato dell'output, specifica il comportamento che quell'output dovrebbe rendere più informato.**
