## 6.6 Dall'aggregato al punto di rottura: combinare segmento, coorte e funnel

Segmentazione, coorti e funnel diventano davvero utili quando smettono di essere tre viste separate e vengono usati come passaggi successivi della stessa diagnosi: **chi** contribuisce al cambiamento, **da quando** e **dove** il percorso inizia a divergere.

### Asteria CRM: il churn attribuito troppo presto al prezzo

**Asteria CRM** è un SaaS B2B europeo con circa **18.000 account paganti**. Nel primo semestre aumenta del **12%** il listino del piano Professional. Due mesi dopo il churn mensile complessivo passa dal **2,7% al 3,6%**.

La storia sembra già pronta: abbiamo alzato i prezzi e i clienti stanno scappando. È plausibile, ma i dati non la sostengono ancora.

La prima apertura per piano produce questo quadro:

| Piano | Churn prima | Churn dopo |
| --- | ---: | ---: |
| Starter | 3,8% | 5,4% |
| Professional | 2,5% | 2,8% |
| Enterprise | 1,1% | 1,2% |

Il piano interessato dall'aumento di prezzo peggiora poco; il deterioramento maggiore è sullo Starter. Il pricing non può essere escluso completamente — potrebbero esistere effetti indiretti o cambi di mix — ma smette di essere la spiegazione dominante.

Il team guarda allora le nuove coorti Starter alla stessa età. La retention D90 evolve così:

| Coorte | Retention D90 |
| --- | ---: |
| Gennaio | 79% |
| Febbraio | 78% |
| Marzo | 77% |
| Aprile | 69% |
| Maggio | 66% |
| Giugno | 65% |

La rottura comincia ad aprile. Nella stessa finestra Asteria aveva lanciato una nuova campagna self-service per microimprese, aumentando fortemente i trial Starter. La segmentazione per canale restringe ancora il problema:

| Canale | Retention D90 |
| --- | ---: |
| Organic | 80% |
| Partner | 84% |
| Paid search | 76% |
| Nuova campagna paid social | 51% |

A questo punto non stiamo più indagando “il churn dell'azienda”. Stiamo osservando soprattutto **nuove coorti Starter provenienti dalla campagna paid social**.

Il funnel dei primi quattordici giorni mostra dove queste coorti divergono. Il percorso osservato è trial avviato → importazione contatti → prima pipeline → primo task assegnato → almeno tre utenti invitati. Le registrazioni crescono, ma solo il **22%** degli utenti della nuova campagna completa l'importazione dei contatti, contro il **47%** degli altri canali.

La timeline rende il pattern ancora più interpretabile. Il messaggio pubblicitario prometteva “CRM operativo in cinque minuti”, mentre il prodotto richiedeva migrazione dati, configurazione della pipeline e collaborazione del team. L'ipotesi più coerente diventa quindi che la campagna stia acquisendo una popolazione con aspettative e intent diversi, molti dei quali non raggiungono un primo valore operativo abbastanza presto.

È una diagnosi molto più forte della spiegazione iniziale, ma resta osservazionale. Non abbiamo dimostrato che cambiare il messaggio, ridisegnare l'onboarding o annullare il pricing produrrà una determinata variazione della retention.

Questa distinzione cambia comunque la decisione. Asteria non annulla immediatamente l'aumento di prezzo del Professional. Separa il monitoraggio Starter/Professional, rivede targeting e promessa della campagna, porta nel dashboard il passaggio trial → importazione → primo workflow e decide di definire una metrica di activation entro quattordici giorni da verificare con un intervento controllato.

Il valore dell'analisi non è avere “trovato la causa”. È avere trasformato:

> il churn sale, probabilmente per il prezzo

in:

> **il deterioramento è concentrato nelle nuove coorti Starter acquisite da un nuovo canale e si manifesta prima del raggiungimento del valore iniziale.**

Questa frase separa meglio ciò che sappiamo da ciò che dobbiamo ancora testare. Il passo successivo è quindi naturale: definire che cosa intendiamo davvero per **primo valore** e quanto tempo impiega il cliente a raggiungerlo.