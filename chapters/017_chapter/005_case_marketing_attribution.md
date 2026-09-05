## 17.4 Helio Market — “Quale marketing crea vendite che altrimenti non avremmo avuto?”

> **Caso simulato/composito**, con riferimenti a casi reali documentati dove indicato.

Helio Market, retailer omnicanale, investe **€18 milioni l'anno** in advertising digitale. Il CMO chiede quale canale “porta davvero” più vendite e la dashboard last-click offre una risposta immediata: branded search, ROAS attribuito **11,8x**.

Il problema non è che il numero sia falso. È che il verbo *porta* mescola due oggetti diversi. Attribution descrive dove compare un touchpoint nel percorso osservato; la decisione di budget richiede sapere quante vendite esistono **in più** grazie alla spesa. Per spostamenti materiali di budget il claim necessario è quindi incrementale, non semplicemente attributivo.

La stop rule è conseguente: **nessuna riallocazione rilevante basata soltanto sul conversion credit**.

### Prima ancora della causalità, il percorso deve essere osservabile

Helio vende online e in negozio. Molti utenti vedono advertising digitale e acquistano offline; un modello che osserva soltanto ecommerce può sottostimare alcuni touchpoint per ragioni di coverage prima ancora che per ragioni causali.

La Data Readiness Review verifica quindi campaign exposure, sessioni web/app, loyalty identity, ordini ecommerce e store, media cost e contribution margin, dentro la privacy boundary autorizzata. L'obiettivo non è collegare più identità possibile, ma costruire una popolazione coerente con purpose limitation e governance.

Due casi Google Cloud mostrano bene il valore — e il limite — di questa integrazione. **Hoff** costruì con OWOX un sistema end-to-end su BigQuery per collegare meglio attività online e vendite fisiche e sviluppare nuovi revenue attribution model; la customer story riporta un aumento del **17% dell'online advertising ROI**.[^hoff] **Freshworks** integrò dati di campagne, conversioni, revenue e CRM per analizzare migliaia di campagne e collegare marketing e customer lifecycle; Google riporta un aumento del **50% del ROI** grazie a una maggiore focalizzazione su campagne, regioni e keyword.[^freshworks]

Queste fonti documentano integrazione, attribution e uso operativo degli insight. Non dimostrano che ogni conversione attribuita fosse causalmente incrementale. Nel capstone questa distinzione non è una cautela editoriale marginale: è esattamente il failure mode che stiamo cercando di evitare.

### Il branded search mostra perché credit e incrementality possono divergere

Nel caso Helio, molti utenti che cliccano branded search stavano già cercando esplicitamente il marchio. Due spiegazioni restano quindi compatibili con lo stesso ROAS 11,8x. Il paid branded può proteggere vendite che altrimenti andrebbero perse; oppure può cannibalizzare in parte organic/direct che avrebbe convertito comunque.

L'attribution dashboard non discrimina tra le due ipotesi. Questo è il **method gate** che giustifica una forma di causal identification.

Dove operativamente possibile, il team riduce in modo controllato la pressione paid branded in mercati confrontabili, definendo prima unità geografica, periodo pre-test, trend/composizione, spend realmente ridotto, outcome totale, spillover e criteri di stop. Nel caso simulato i click paid branded scendono molto, una parte del traffico migra verso organic e le vendite totali diminuiscono molto meno dei click. L'**incremental ROAS** risulta quindi molto più basso del ROAS attribuito.

Questo non rende il canale “inutile”. Mostra che **credito osservato e valore incrementale sono oggetti diversi**.

Video prospecting produce il problema opposto. Il last-click assegna poco credito perché molte conversioni arrivano più tardi tramite direct o search; test geografici indicano invece un effetto incrementale maggiore. Uno stesso sistema di attribution può quindi sovrastimare un canale e sottostimarne un altro.

### Non serve trovare un modello unico

Il routing maturo non sostituisce last-click con un altro oracolo. Usa strumenti diversi per decisioni diverse:

- **attribution** per descrivere journey e assist;
- **experiment** quando un grande spostamento è testabile e il valore dell'informazione giustifica l'attesa;
- **MMM** per ragionare su livello aggregato, canali difficili da randomizzare e dinamiche più lunghe, sotto assunzioni esplicite;
- **marginal ROI** per la domanda economicamente decisiva: dove crea più valore il **prossimo euro**, non chi merita il credito per quello già speso.

Il Decision Record confronta quindi tre policy. Riallocare sulla base del last-click è rapido ma espone alla cannibalizzazione nascosta. Aspettare esperimenti perfetti per ogni canale è teoricamente pulito e operativamente impossibile. La scelta preferita è un **sistema di evidenza ibrido**: attribution per leggere il percorso, experiment sui grandi spostamenti testabili, MMM dove appropriato, marginal ROI per allocazione e contribution margin/new-customer economics come outcome.

Una riallocazione materiale procede soltanto quando il range plausibile dell'incremental ROI resta sopra la soglia economica, cannibalizzazione e lag principali sono rappresentati e la conclusione non dipende da un solo modello fragile. Se il range attraversa la decision boundary, comprare un test può valere più del costo dell'attesa.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| branded search attributed ROAS 11,8x | parte del credito paid branded è probabilmente cannibalizzato | incremental ROI stabile a livelli di spesa molto diversi |
| paid click calano più delle vendite totali nel test | prospecting è sottovalutato dal last-click | effetti lunghi e interazioni tra canali |
| parte del traffico migra verso organic | allocation deve essere marginale, non basata sul credito storico | competitor/media-market response |

La headline executive diventa:

> **Il ROAS attribuito sovrastima il valore incrementale del branded search e sottovaluta parte del prospecting. Per il prossimo trimestre proponiamo di riallocare il budget usando evidenza incrementale e marginal ROI, non il solo credito di conversione.**

La review successiva separa attributed revenue, incremental revenue, marginal ROAS, CAC, payback, new-customer rate, contribution margin, cannibalizzazione paid/organic e risposta marginale alla spesa.

Il team sceglie anche cosa **non** fare: non tenta di attribuire causalmente ogni singola conversione a ogni touchpoint. In un sistema complesso quella pretesa può superare l'identificabilità disponibile.

**Percorso effettivo:** Analytical Brief → Data Readiness Review → Causal Identification Brief → Experiment Contract dove il budget move è testabile → Uncertainty Brief → Decision Record → Decision Communication Pack. Attribution e MMM restano strumenti complementari, non fonti automatiche di causal truth.

> **Attribution racconta chi era presente nel percorso. Incrementality cerca di capire chi lo ha cambiato. Marginal ROI decide dove dovrebbe andare il prossimo euro.**

[^hoff]: Google Cloud, *Hoff Case Study*, https://cloud.google.com/customers/hoff
[^freshworks]: Google Cloud, *Freshworks: Analyzing customer touchpoints and sales performance with Google*, https://cloud.google.com/customers/freshworks
