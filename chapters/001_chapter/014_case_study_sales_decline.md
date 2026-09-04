## 1.13 Caso studio: “Le vendite stanno scendendo”

**Caso simulato/composito.** Una teoria del lavoro analitico serve soltanto se riesce a disciplinare una richiesta concreta quando la pressione per trovare rapidamente una spiegazione è alta.

Immaginiamo che il direttore commerciale entri in riunione con una frase semplice:

> “Le vendite stanno scendendo. Voglio capire perché.”

La richiesta sembra già pronta per essere analizzata. In realtà contiene quasi tutti i problemi affrontati nel capitolo: una metrica non definita, una baseline implicita, una spiegazione ancora sconosciuta e una decisione che non è stata dichiarata.

### Prima di spiegare il calo dobbiamo decidere che cosa sta calando

“Vendite” potrebbe significare fatturato lordo o netto, ordini, unità, margine, valore medio dell'ordine oppure ordini acquisiti ma non ancora completati. Ciascuna definizione può muoversi in modo diverso.

L'analista non parte quindi dal dashboard che ha già aperto più spesso. Chiede al direttore quale fenomeno sia rilevante per la scelta che deve prendere.

Il direttore chiarisce che vuole decidere se intervenire su pricing, marketing o assortimento nel trimestre successivo e che, per questa discussione, gli interessa il **fatturato netto degli ordini completati**.

La precisazione sembra piccola, ma cambia l'analisi. Da questo momento resi, cancellazioni e stato dell'ordine non sono più dettagli di implementazione: fanno parte della definizione della metrica che sosterrà la decisione.

### “Scendere” richiede una baseline

Il secondo problema è il confronto. Il mese precedente mostra un calo evidente, ma il business è stagionale. Se l'analista usasse soltanto quella baseline, potrebbe attribuire a un problema operativo ciò che accade normalmente nello stesso periodo dell'anno.

Confronta quindi il fatturato soprattutto con lo stesso periodo dell'anno precedente e con il forecast, controllando che il perimetro dei negozi sia comparabile. Il calo rimane vicino al **10%** in entrambi i confronti.

Ora abbiamo un fenomeno definito e una deviazione che non sembra spiegata soltanto dalla stagionalità. Possiamo iniziare a localizzarla.

### Scomporre il numero prima di costruire una storia

Una prima identità è semplice:

**Ricavi = numero di ordini × valore medio dell'ordine**

Il valore medio è quasi stabile. Il movimento viene soprattutto dal numero di ordini.

L'analista prosegue:

**Ordini = traffico qualificato × conversion rate**

Anche qui emerge una separazione utile. Il traffico complessivo è sostanzialmente stabile, mentre la conversione diminuisce.

Queste identità non dimostrano la causa del problema. Svolgono una funzione precedente: trasformano “le vendite scendono” in componenti osservabili e permettono di smettere di investigare parti del sistema che non stanno spiegando il delta principale.

La decomposizione è quindi un **issue tree**, non una teoria causale.

### La segmentazione restringe ancora lo spazio del problema

Il calo aggregato potrebbe nascondere dinamiche diverse, quindi l'analista lo osserva per segmento, canale, dispositivo e tipo di cliente.

Il quadro cambia rapidamente. L'enterprise cresce mentre il consumer diminuisce. Quasi tutto il delta negativo proviene dall'e-commerce. All'interno dell'e-commerce il desktop è stabile e il mobile peggiora. I clienti esistenti tengono relativamente bene; la perdita è concentrata soprattutto nei nuovi visitatori mobile.

La domanda originale si è trasformata.

Non stiamo più cercando genericamente “perché le vendite sono scese”. Stiamo cercando di capire:

> **“Perché la conversione dei nuovi visitatori mobile è peggiorata?”**

Questa riduzione dello spazio investigativo vale più di molte analisi sofisticate eseguite sull'intera azienda. Abbiamo escluso una grande quantità di storie prima ancora di tentare di scegliere quella corretta.

### Prima delle cause di business, escludere che il fenomeno sia stato prodotto dai dati

A questo punto sarebbe facile cercare immediatamente una spiegazione nel comportamento dei clienti o nelle iniziative commerciali. Ma il fatto che il problema sia concentrato sul mobile rende plausibile anche un artefatto tecnico.

L'analista controlla quindi freshness delle sorgenti, ordini mancanti, duplicati, cambi nella definizione di `completed_order`, fusi orari, modifiche al tracking mobile e riconcilia il fatturato con una fonte indipendente.

Il calo rimane.

Questo passaggio non produce una storia interessante da presentare al management, ma aumenta la credibilità di tutte le storie successive. Senza di esso potremmo passare ore a spiegare un cambiamento commerciale che in realtà esiste soltanto nella pipeline.

### Le ipotesi diventano utili quando competono fra loro

Negli stessi giorni sono avvenuti più cambiamenti: è stata rilasciata una nuova versione del checkout mobile, è variato il mix delle campagne, alcune condizioni di spedizione sono cambiate e sono partite promozioni su categorie specifiche.

Tutte sono spiegazioni plausibili. Proprio per questo nessuna dovrebbe essere accettata soltanto perché racconta una storia coerente.

La decomposizione del funnel aggiunge nuova informazione: il peggioramento principale avviene tra selezione del metodo di pagamento e conferma. La timeline mostra che il pattern comincia subito dopo il rollout del nuovo checkout e l'effetto è molto più forte sugli utenti effettivamente esposti alla nuova versione.

Le ipotesi di marketing e assortimento non diventano impossibili, ma spiegano meno bene la localizzazione del problema. L'ipotesi tecnica sale quindi di priorità perché è più coerente con **dove**, **quando** e **su chi** compare il calo.

È importante il linguaggio: non abbiamo ancora dimostrato che il checkout abbia causato la perdita di conversione. Abbiamo costruito un insieme di evidenze che rende questa spiegazione più credibile delle alternative immediate.

### La quantità di evidenza necessaria dipende anche dall'azione disponibile

L'analista stima che circa il **75%** del calo osservato sia concentrato nel funnel mobile interessato dal rollout.

A questo punto entra il livello decisionale. Il nuovo checkout è reversibile rapidamente; sospendere ulteriori rollout costa relativamente poco; ogni giorno di attesa, invece, continua a esporre fatturato al problema.

Non serve quindi aspettare una prova causale perfetta prima di fare qualsiasi cosa. Serve scegliere un'azione che limiti il rischio e produca nuova informazione.

Il team verifica tecnicamente errori e telemetria, sospende l'espansione del rollout e ripristina temporaneamente la versione precedente per una parte del traffico. Poi confronta conversione e failure rate tra le due esperienze e controlla se un eventuale recupero del funnel si traduca anche in ordini e fatturato.

La decisione è importante perché trasforma l'intervento in un nuovo passaggio della catena analitica. Se la versione precedente recupera conversione proprio nel segmento colpito, l'ipotesi tecnica guadagna forza. Se non cambia nulla, dobbiamo tornare alle spiegazioni concorrenti.

L'analisi non finisce quindi con una diagnosi consegnata al direttore. **L'azione diventa una fonte di evidenza.**

### Dove l'AI accelera e dove non decide

Un assistente AI avrebbe potuto generare rapidamente le query di segmentazione, proporre decomposizioni, scrivere controlli di qualità, sintetizzare log, produrre visualizzazioni esplorative e suggerire ipotesi rivali.

Questa capacità avrebbe reso l'indagine più veloce. Non avrebbe però eliminato le decisioni che hanno dato forma al problema: che cosa intendere per fatturato, quale baseline fosse credibile in un business stagionale, perché fosse necessario escludere un artefatto di tracking, quanta evidenza fosse sufficiente per un rollback reversibile e quale risultato successivo avrebbe falsificato la nostra ipotesi.

La documentazione Microsoft su Copilot in Power BI offre un esempio concreto dello stesso principio: la qualità delle risposte dipende dalla preparazione e dalla semantica del modello sottostante.[^ms-copilot]

Il caso può essere riassunto con una sequenza, ma ora sappiamo che ogni freccia contiene un ragionamento:

> **Prima di spiegare un cambiamento, localizzalo. Prima di localizzarlo, definisci metrica e confronto. Prima di definire metrica e confronto, chiarisci la decisione. Dopo avere agito, misura se il sistema ha reagito come la tua spiegazione prevedeva.**

---

### Fonte

[^ms-copilot]: Microsoft Learn, *Use Copilot with semantic models in Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
