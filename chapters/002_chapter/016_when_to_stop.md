## 2.15 Stop rule: decidere prima quando l'analisi sarà abbastanza

Ogni analisi potrebbe continuare indefinitamente.

Possiamo aggiungere un segmento, un controllo, un modello, una sorgente, un'altra visualizzazione o una nuova ipotesi. L'abbondanza di possibilità non significa che ogni approfondimento abbia valore.

Per questo il brief dovrebbe contenere una **stop rule analitica**: un criterio che indica quando la prima fase dispone di evidenza sufficiente per essere consegnata o quando deve essere fermata perché non può rispondere in modo credibile.

È diversa dalle stop condition operative degli agenti discusse nel Capitolo 0. Qui non stiamo fermando un sistema autonomo: stiamo governando la profondità di un'indagine.

### Tre modi legittimi di fermarsi

**1. Evidenza sufficiente**

La decisione è abbastanza supportata e ulteriore lavoro ha basso valore marginale.

**2. Limite informativo raggiunto**

I dati disponibili non permettono di distinguere le ipotesi principali. Continuare con le stesse fonti produrrebbe soltanto analisi più elaborate della stessa incertezza.

**3. Cambio di domanda**

L'indagine ha rivelato un problema diverso e più importante. Conviene chiudere o aggiornare il brief invece di espandere silenziosamente lo scope.

### Una stop rule deve essere collegata alla decisione

Esempi:

> “La fase diagnostica termina quando abbiamo validato la metrica, localizzato almeno l'80% del delta e testato le tre ipotesi prioritarie.”

oppure:

> “Se il sanity check mostra che il tracking non è comparabile prima e dopo la migrazione, fermiamo l'analisi del trend e apriamo una fase di ricostruzione della metrica.”

oppure:

> “Se i due scenari di forecast portano alla stessa decisione di staffing, non ottimizziamo ulteriormente il modello prima del primo ciclo operativo.”

La stop rule non richiede sempre una percentuale. Richiede una condizione di sufficienza o di impossibilità.

### Fermarsi troppo presto

Anche la fretta è un rischio.

Una correlazione iniziale può scomparire dopo una segmentazione. Una variazione mensile può essere stagionale. Una metrica può essere cambiata dalla pipeline. Un risultato aggregato può nascondere mix shift.

Per questo una stop rule robusta include controlli minimi obbligatori prima della conclusione.

### Rendimenti decrescenti

Un segnale importante è osservare il **marginal value** delle nuove analisi.

Le prime verifiche cambiano molto il nostro modello del problema. Poi ogni nuova analisi aggiunge dettagli ma non modifica più la decisione.

Quando siamo in quella zona, continuare può essere una forma di perfezionismo più che di rigore.

### Timeboxing come strumento, non come criterio epistemico

Dividere il lavoro in checkpoint è utile:

- chiarimento iniziale;
- sanity check;
- prima decomposizione;
- review con stakeholder;
- approfondimento mirato.

Ma “sono finite le quattro ore” non significa automaticamente che l'evidenza sia sufficiente.

Il timebox protegge il costo. La stop rule protegge la qualità della conclusione.

### AI e analisi infinita

Con l'AI è molto facile generare:

- altre segmentazioni;
- altri modelli;
- altre correlazioni;
- altre spiegazioni.

Questa capacità rende ancora più importante sapere **che cosa stiamo cercando di apprendere da ogni iterazione**.

Se non sappiamo quale incertezza dovrebbe ridurre la prossima analisi, probabilmente non dovremmo eseguirla soltanto perché costa poco.

### Campo del brief

```text
Controlli minimi prima di concludere:
Condizione di evidenza sufficiente:
Condizione di stop per limite dati:
Checkpoint di scope/reframing:
```

> **Rigore non significa analizzare per sempre. Significa sapere quali controlli sono necessari prima di avere il diritto di fermarsi.**
