## 2.15 Stop rule: sapere quando l'analisi ha guadagnato il diritto di fermarsi

Ogni analisi può continuare indefinitamente. Esisterà quasi sempre un altro segmento da esplorare, una sorgente da aggiungere, un modello più sofisticato, una visualizzazione ulteriore o una spiegazione concorrente da verificare. La disponibilità di nuove mosse non implica però che ognuna abbia valore.

Per questo il brief dovrebbe contenere una **stop rule analitica**: non una scadenza arbitraria, ma un criterio che descrive quando la prima fase dispone di evidenza sufficiente per sostenere la decisione oppure quando deve fermarsi perché le fonti disponibili non possono produrre una conclusione credibile.

È diversa dalle stop condition operative degli agenti discusse nel Capitolo 0. Lì governavamo l'autonomia di un sistema. Qui governiamo la profondità di un'indagine umana o assistita.

## Tre modi professionali di chiudere un ciclo

Un'analisi può fermarsi perché l'evidenza è sufficiente: abbiamo eseguito i controlli minimi, la decisione è supportata abbastanza bene e il valore marginale di un'altra settimana di lavoro è basso. Può fermarsi perché abbiamo raggiunto un **limite informativo**: le fonti disponibili non distinguono le ipotesi principali e continuare a modellare gli stessi dati produrrebbe soltanto una versione più elaborata della stessa incertezza. Oppure può fermarsi perché l'indagine ha scoperto un problema diverso e più importante, che richiede un nuovo brief invece di un'espansione silenziosa dello scope.

Questi esiti sono diversi, ma condividono una regola: la chiusura deve essere collegata a ciò che la decisione richiede.

Per una fase diagnostica potremmo stabilire:

> “Terminiamo quando abbiamo validato la metrica, localizzato almeno l'80% del delta e testato le tre ipotesi prioritarie.”

In un problema di tracking potremmo invece decidere:

> “Se il sanity check mostra che il tracking non è comparabile prima e dopo la migrazione, fermiamo l'analisi del trend e apriamo una fase di ricostruzione della metrica.”

Per un forecast operativo:

> “Se gli scenari plausibili portano alla stessa decisione di staffing, non ottimizziamo ulteriormente il modello prima del primo ciclo operativo.”

In tutti e tre i casi la stop rule dice quali condizioni rendono ulteriore precisione poco utile **per quella decisione**.

## Fermarsi richiede controlli minimi

La stop rule non deve diventare un alibi per chiudere troppo presto. Una correlazione iniziale può scomparire dopo una segmentazione; una variazione mensile può essere stagionale; una pipeline può aver cambiato definizione; un risultato aggregato può dipendere soltanto da mix shift. Perciò una regola di sufficienza deve includere le verifiche senza le quali non abbiamo ancora il diritto di concludere.

Qui il collegamento con il Value of Information diventa naturale. All'inizio le verifiche spesso modificano molto il nostro modello del problema. Con il tempo, ogni nuova analisi aggiunge dettagli ma non sposta più la decisione. Quando entriamo in questa zona di rendimenti decrescenti, il perfezionismo può sembrare rigore mentre in realtà sta consumando capacità che avrebbe più valore altrove.

Il timeboxing è utile per controllare questo costo, ma non sostituisce il criterio epistemico. Un checkpoint dopo quattro ore può imporre una review del piano; non rende automaticamente sufficiente l'evidenza. **Il timebox protegge il budget. La stop rule protegge la conclusione.**

Con l'AI la distinzione diventa ancora più importante, perché è economico generare altre segmentazioni, altri modelli e altre spiegazioni. Prima di ogni iterazione dovremmo sapere quale incertezza ci aspettiamo di ridurre. Se non sappiamo rispondere, il fatto che l'analisi successiva sia facile da produrre è un motivo molto debole per eseguirla.

Il campo del brief rimane operativo:

```text
Controlli minimi prima di concludere:
Condizione di evidenza sufficiente:
Condizione di stop per limite dati:
Checkpoint di scope/reframing:
```

> **Rigore non significa continuare finché non restano domande. Significa completare i controlli che la decisione richiede e riconoscere quando nuova analisi non sta più comprando informazione utile.**
