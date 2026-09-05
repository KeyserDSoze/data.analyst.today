## 2.11 L'Analytical Brief: il contratto prima dell'analisi

A questo punto i pezzi costruiti nelle sezioni precedenti possono essere riuniti. Un **Analytical Brief** è una specifica breve che descrive che cosa stiamo cercando di capire, perché conta, quale decisione deve diventare più informata, quale evidenza servirà e quando il lavoro potrà considerarsi sufficientemente completo.

Per molte analisi basta una pagina. La lunghezza non è il punto: ciò che conta è rendere esplicite le dipendenze che altrimenti emergerebbero durante l'esecuzione, quando cambiare direzione è già più costoso.

Il brief parte dal problema di business e dalla decisione, non dal dataset. Se la repeat purchase dei nuovi clienti sembra deteriorarsi, per esempio, il problema può essere la capacità di trasformare il primo ordine in una relazione ripetuta. La decisione potrebbe riguardare dove investire fra acquisizione, post-purchase experience e riattivazione. Solo a quel punto possiamo formulare una domanda diagnostica, scegliere la repeat purchase rate a 90 giorni come outcome, definire quali coorti sono mature, stabilire una baseline e chiedere quali segnali servano per distinguere le spiegazioni concorrenti.

Questa sequenza è importante perché i campi del brief non sono indipendenti. Una modifica alla domanda può cambiare la metrica; una modifica alla metrica può cambiare la popolazione; una nuova ipotesi può richiedere un dato che non esiste; un gap dati può ridurre la pretesa massima dell'analisi; una decisione più rischiosa può richiedere controlli e stop rule diversi.

## Dal problema alla promessa dell'analisi

La prima parte del brief dovrebbe mantenere vicini **problema**, **decisione** e **domanda analitica**. Il problema spiega perché il lavoro esiste. La decisione specifica chi potrà agire, con quali alternative e con quale costo dell'errore. La domanda traduce quel bisogno in qualcosa che dati e metodo possono mettere alla prova.

Subito dopo conviene dichiarare il **tipo di domanda e la pretesa massima**. Una frase come:

> “Diagnostica. L'analisi localizzerà il deterioramento e restringerà le ipotesi, ma non attribuirà automaticamente causalità ai driver osservati.”

protegge il progetto da una deriva frequente: iniziare con un'analisi osservazionale e finire con una raccomandazione formulata come se avessimo identificato un effetto causale.

## Metriche e scope rendono il fenomeno osservabile

Una volta stabilita la promessa, dobbiamo definire l'outcome, i driver e gli eventuali guardrail, insieme alla popolazione a cui si applicano. Qui entrano numeratore, denominatore, unità di analisi, finestra temporale, maturazione ed esclusioni.

Queste scelte devono essere lette come un blocco unico. Se l'outcome è repeat purchase a 90 giorni, non possiamo includere nel denominatore clienti acquisiti ieri. Se la decisione riguarda il valore economico delle campagne, una segmentazione per acquisition channel diventa probabilmente prioritaria. Se il fenomeno è stagionale, la baseline year-over-year può essere più informativa del mese precedente.

La baseline e le segmentazioni non completano la dashboard: completano **il significato del confronto**.

## Ipotesi e dati trasformano il brief in un piano di verifica

Le ipotesi prioritarie dicono quali spiegazioni metteremo per prime sotto pressione. Per ognuna dovremmo sapere che cosa ci aspettiamo di osservare se fosse vera, che cosa la indebolirebbe e quale dato permetterebbe di distinguerla dalle alternative.

Da qui nascono i requisiti dati. Alcuni segnali sono required perché senza di essi l'outcome o il confronto non possono essere ricostruiti; altri sono useful perché aumentano la profondità; altri ancora sono proxy e devono essere accompagnati dai loro limiti. Se una fonte richiesta non esiste o ha grain incompatibile, il brief deve registrare il gap e il suo impatto sulla domanda.

Il **metodo iniziale** viene scelto soltanto a questo punto. Non serve anticipare ogni query. Serve definire il percorso minimo capace di guadagnarsi la conclusione: sanity check dei dati e della metrica, ricostruzione dell'outcome, confronto con la baseline, decomposizione e segmentazione, test delle ipotesi prioritarie e quantificazione dell'impatto che conta per la decisione.

## Rischi, output e stop rule chiudono il contratto

Il brief deve infine registrare i limiti già conosciuti: tracking cambiato, identità instabile, campioni piccoli, proxy imperfetti, popolazioni non comparabili o dati immaturi. Documentarli prima dell'analisi non significa decidere che il lavoro fallirà; significa sapere quali condizioni potrebbero abbassare la forza della conclusione.

Solo dopo ha senso specificare l'output. Un memo, un notebook riproducibile, un dataset, una dashboard, un modello o una proposta di esperimento sono mezzi diversi. Il formato dovrebbe derivare dalla decisione e dalla frequenza con cui l'informazione dovrà essere usata, non dalla forma con cui il requester ha aperto il ticket.

La **stop rule** stabilisce invece quando il primo ciclo avrà prodotto abbastanza evidenza o quando dovrà fermarsi perché i dati non consentono di distinguere le ipotesi. Per una diagnosi potremmo concordare:

> “Concludiamo la prima fase quando abbiamo validato la metrica, localizzato almeno l'80% del delta osservato e testato le tre ipotesi prioritarie, oppure quando emerge un limite dati che impedisce di distinguerle.”

Il criterio di successo non sarà quindi “dashboard consegnata”, ma qualcosa di più vicino a:

> “Il decision owner dispone di evidenza sufficiente per scegliere il prossimo intervento e conosce le incertezze che rimangono.”

## Template riutilizzabile

La forma strutturata ha valore proprio qui, perché il brief deve poter essere copiato, compilato, revisionato e versionato:

```text
Problema di business:

Decisione:
Decision owner:
Alternative:
Deadline/frequenza:
Costo principale dell'errore:

Domanda analitica primaria:
Tipo di domanda / pretesa massima:
Domande secondarie:

Outcome metric:
Driver metrics:
Guardrails:
Target/soglia, se nota:

Popolazione:
Esclusioni:
Unità di analisi:
Periodo / campo temporale:
Maturazione:
Fuori scope:

Baseline:
Segmentazioni previste:

Ipotesi prioritarie:

Dati required:
Dati useful/proxy:
Gap noti:

Metodo iniziale:
Limiti/rischi:

Output:
Stop rule:
Criterio di successo:
```

## Un documento vivo, ma non invisibilmente mutevole

Il brief non è una promessa che nulla cambierà. Una buona analisi produce informazioni nuove e può rendere necessario modificare scope, metrica o perfino domanda. La disciplina consiste nel rendere quella modifica esplicita.

Se durante il sanity check scopriamo che la metrica storica è rotta, il piano non dovrebbe continuare silenziosamente come se nulla fosse. Il brief viene aggiornato, il decision owner viene riallineato e la ricostruzione della misura può diventare la nuova priorità. Se una nuova ipotesi richiede una fonte che non esiste, possiamo aprire una fase successiva invece di espandere indefinitamente il primo ciclo.

In un ambiente in cui AI e strumenti self-service possono produrre output quasi immediatamente, questi pochi minuti di attrito hanno un valore particolare: vengono spesi nel punto in cui cambiare idea costa meno.

> **Il brief non rallenta l'analisi. Separa la velocità di esecuzione dalla fretta di impegnarsi su una domanda non ancora progettata.**
