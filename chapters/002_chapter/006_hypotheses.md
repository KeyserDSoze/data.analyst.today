## 2.5 Ipotesi: trasformare curiosità in spiegazioni che competono

Una buona analisi esplorativa non coincide con guardare ogni variabile disponibile. Quando il problema è ampio, le ipotesi servono a trasformare curiosità generica in **spiegazioni candidate che possono essere messe in concorrenza**.

Supponiamo che la conversione e-commerce sia diminuita. Potrebbe essere cambiata la qualità del traffico; una nuova versione del checkout potrebbe aver aumentato l'abbandono; il mix di dispositivi potrebbe essersi spostato verso mobile; alcuni prodotti ad alta conversione potrebbero essere meno disponibili; prezzi o condizioni di spedizione potrebbero essere cambiati. È possibile perfino che il fenomeno sia in parte artificiale perché il tracking è stato modificato.

Elencare queste possibilità è un buon inizio, ma non basta. Il valore nasce quando per ciascuna iniziamo a chiedere **che cosa dovremmo osservare se fosse vera e quale evidenza la renderebbe meno credibile**.

## Dall'osservazione alla pretesa

È importante non confondere livelli diversi. “Il calo è concentrato sul mobile” è un'osservazione. “Il calo mobile deriva soprattutto da un aumento dell'abbandono nel passaggio di pagamento” è già un'ipotesi diagnostica. “La nuova interfaccia di pagamento ha provocato parte del calo” è una pretesa causale e richiede un disegno più forte.

Il brief può contenere tutte e tre le frasi, purché sia chiaro il loro status. L'errore nasce quando un pattern osservato viene promosso a spiegazione causale soltanto perché la storia è plausibile.

Un hypothesis tree può aiutare a organizzare lo spazio investigativo. Per il fatturato, ad esempio, possiamo partire dall'identità:

**Fatturato = ordini × valore medio dell'ordine − resi/cancellazioni**

Da qui possiamo chiedere se sono diminuiti gli ordini, se è sceso l'average order value o se sono aumentati resi e cancellazioni. A loro volta gli ordini possono essere scomposti in traffico e conversione, mentre il valore medio può dipendere da prezzo, mix prodotto e sconti. In parallelo dobbiamo lasciare un ramo per la possibilità che sia cambiata la contabilizzazione della metrica.

Questa struttura non dimostra alcuna causa. Riduce però il rischio di saltare direttamente alla spiegazione preferita. Il principio MECE — *Mutually Exclusive, Collectively Exhaustive* — può essere utile come aspirazione per ridurre sovrapposizioni e non dimenticare intere famiglie di spiegazioni, sapendo che nel mondo reale i meccanismi spesso interagiscono.

## Una buona ipotesi contiene il proprio test

Per ogni spiegazione prioritaria dovremmo riuscire a immaginare almeno un'osservazione che la rafforza e una che la indebolisce. Se sospettiamo il nuovo checkout mobile, ci aspettiamo un peggioramento negli utenti esposti alla release, localizzato nel funnel dopo il passaggio modificato. Se lo stesso calo appare negli utenti non esposti o è iniziato settimane prima, l'ipotesi perde forza.

Questo passaggio trasforma la lista di possibili cause in un piano. Il registro delle ipotesi rimane quindi intenzionalmente tabellare:

| Ipotesi | Evidenza attesa se vera | Evidenza che la indebolisce | Dato necessario | Costo verifica | Priorità |
|---|---|---|---|---:|---:|
| Checkout mobile | drop dopo step pagamento sugli esposti | stesso calo sui non esposti | eventi funnel + release | basso | alta |
| Mix canali | calo concentrato nei nuovi canali | conversione cala dentro ogni canale | attribution + sessioni | medio | media |
| Stock-out | categorie colpite spiegano il delta | disponibilità stabile | inventory + catalogo | basso | alta |

La priorità non deve diventare un punteggio pseudo-scientifico. Serve a riconoscere che un controllo rapido capace di eliminare un intero ramo dell'albero può avere più valore di un modello sofisticato applicato a una spiegazione marginale. Impatto potenziale, plausibilità di dominio, disponibilità dei dati, costo di falsificazione e rilevanza decisionale sono criteri sufficienti per ordinare il lavoro.

L'AI può ampliare rapidamente il portafoglio iniziale di ipotesi e proporre controargomenti. Ma proprio perché la generazione costa poco, il registro diventa più importante: ogni candidata deve guadagnarsi attenzione attraverso dati, test e capacità di distinguersi dalle alternative.

> **Un'ipotesi utile non è una storia plausibile. È una storia che ci dice quale osservazione cercare per scoprire se merita ancora fiducia.**
