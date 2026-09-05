## 17.5 Aster Components — “Come possiamo avere più inventario e più stock-out?”

> **Caso simulato/composito**, con riferimenti a casi reali documentati dove indicato.

Aster Components vede contemporaneamente inventory value **+14% YoY**, stock-out in aumento, expedite cost in crescita e più capitale immobilizzato. Il COO chiede come possa succedere se l'azienda “ha più inventario”. La contraddizione esiste solo finché trattiamo lo stock come un unico blocco.

La decisione reale non è aumentare o ridurre l'inventario totale. È **dove allocare capitale, safety stock e attenzione supplier affinché il costo del rischio scenda senza immobilizzare capitale dove non serve**. Il failure cost viene da entrambe le direzioni: fermo linea e lost sales da una parte, working capital e obsolescenza dall'altra. Per questo la prima stop rule è già una decisione: **nessun +10% generalizzato ai target finché non sappiamo quali SKU generano davvero l'esposizione**.

### La media inventariale nasconde due economie opposte

A livello SKU emerge che gli slow mover accumulano scorte mentre alcuni componenti critici hanno service level insufficiente. La variabilità dei lead time è aumentata, forecast error e bias cambiano fortemente per famiglia e pochi componenti possono bloccare linee molto più costose del loro valore inventariale.

Prima di ottimizzare, il team deve quindi definire l'oggetto. L'Analytical Data Contract fissa grain **SKU × plant × giorno**, distingue on-hand da available-to-promise, open purchase order da committed stock, usa lead time osservato e non soltanto contrattuale e rende espliciti stock-out event, lost-sales estimate e production-stop attribution.

Questa semantica permette di costruire una vista con inventory value, days of inventory, fill rate, stock-out rate, forecast bias/error, supplier lead-time variability, expedite cost e downtime exposure senza fingere che tutte le metriche abbiano lo stesso peso.

Quando gli SKU vengono classificati anche per variabilità, criticità produttiva, sostituibilità, lead time, concentrazione supplier e costo del fermo, emergono **37 componenti** che rappresentano una parte piccola del valore inventariale ma una quota molto più grande del rischio operativo.

Questo è già un risultato decisionale forte: **un euro di buffer aggiuntivo non ha lo stesso valore su ogni SKU**.

### Il forecast non è la policy di inventario

Aster scopre inoltre che il point forecast viene usato quasi direttamente come piano di riordino. Due componenti con domanda media di 1.000 unità al mese possono però richiedere buffer completamente diversi se uno è stabile e consegnato in tre giorni mentre l'altro è volatile, ha dodici settimane di lead time, un solo supplier e può fermare la produzione.

Qui il Temporal Decision Brief guadagna il diritto di esistere non perché “siamo in supply chain”, ma perché resta aperto un rischio specifico: **come combinare distribuzione della domanda, distribuzione del lead time e costo asimmetrico dell'errore**.

Per i 37 componenti critici il team costruisce quindi scenari di lead time normale, shock moderato, shortage severa, domanda sopra forecast e supplier failure. Per ciascuno confronta stock disponibile, produzione a rischio, costo del fermo, costo del buffer e possibilità di sostituzione o riallocazione. Non cerca di eliminare l'incertezza; cerca una policy che sopravviva ai futuri più costosi.

AWS documenta un pattern simile nel caso **BMW Group** durante la semiconductor shortage: dati di produzione, mercato e input dei supplier furono integrati per aumentare la trasparenza sulla domanda e supportare la distribuzione delle parti tra mercati. Un approfondimento AWS sul digital supply management descrive inoltre l'uso congiunto di shortage data, bill of materials, volume plans, take rate, finance e market demand per confrontare scenari di allocazione.[^bmw][^bmw-dsm]

Anche **Coca-Cola Andina** offre un esempio documentato di come visibilità operativa più tempestiva possa cambiare il processo decisionale: AWS descrive l'applicazione interna Thanos, con aggiornamenti ogni **15 minuti** invece che una volta al giorno, usata per inventory, distribution e delivery analytics in quattro paesi.[^cca]

Questi casi non dimostrano che esista una formula universale di safety stock. Rafforzano il punto più importante: **la supply-chain decision vive nell'integrazione tra stato operativo, vincoli e allocazione, non nel possesso di un forecast isolato**.

### La prima decisione non deve aspettare un optimizer globale

Il Decision Record mette a confronto tre strategie. Aumentare del 10% il target ovunque è semplice ma costoso e poco mirato. Ridurre stock per recuperare working capital migliora il capitale nel breve e può peggiorare proprio gli SKU che bloccano produzione. La policy preferita è differenziata: safety stock per variabilità/criticità, reorder point rivisti, supplier monitoring sui componenti critici, scenario gate per shock di lead time, riduzione degli slow mover e escalation quando l'esposizione economica supera soglia.

La cosa più importante è ciò che il team **non** aspetta. Non costruisce prima un modello matematico dell'intera rete globale. I 37 componenti hanno già evidence sufficiente per un intervento mirato e reversibile; rimandarlo in attesa dell'ottimo globale aumenterebbe il costo dell'attesa senza chiudere un rischio decisionale più importante.

La policy verrà rivalutata quando cambia il regime dei lead time, un supplier critico perde affidabilità, cambia il costo del capitale, il demand mix si sposta, compaiono alternative di sourcing o cambia il costo di downtime. Reorder point e safety stock non diventano così numeri ereditati e immutabili.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| inventory value +14%, stock-out/expedite in aumento | problema dominante è allocazione, non quantità totale | distribuzione futura dei lead time |
| 37 componenti concentrano forte downtime exposure | buffer aggiuntivo ha valore molto diverso per SKU | probabilità/severità dei prossimi supplier shock |
| slow mover sovrastoccati e critici sotto-serviti | policy uniforme distrugge capitale o servizio | effetto completo di nuove fonti di sourcing |

La headline executive può quindi essere:

> **Il problema non è la quantità totale di stock ma la sua allocazione: capitale eccessivo è concentrato su slow mover mentre 37 componenti critici restano esposti a variabilità di domanda e lead time. Proponiamo una policy differenziata, non un aumento generalizzato dell'inventario.**

L'outcome review segue fill rate, stock-out, inventory value, working capital, expedite cost, downtime, forecast bias/error e supplier lead-time reliability. Nessuna singola metrica può rappresentare la qualità della policy.

**Percorso effettivo:** Analytical Brief → Analytical Data Contract → Data Readiness Review → EDA Evidence Map → Temporal Decision Brief sui componenti critici → Decision Record → Decision Communication Pack.

> **La maturità qui consiste anche nel sapere che correggere 37 esposizioni evidenti è una decisione migliore che aspettare l'ottimizzazione perfetta di una rete che non abbiamo bisogno di ottimizzare oggi.**

[^bmw]: AWS, *BMW Group uses AWS to address semiconductor shortage with analytics*, https://aws.amazon.com/solutions/case-studies/bmw-reinvent-2023-analytics/
[^bmw-dsm]: AWS Industries Blog, *Digital supply management using advanced analytics and serverless architecture on AWS*, https://aws.amazon.com/blogs/industries/digital-supply-management-using-advanced-analytics-and-serverless-architecture-on-aws-2/
[^cca]: AWS, *Coca-Cola Andina improves inventory and distribution visibility with analytics*, https://aws.amazon.com/solutions/case-studies/coca-cola-andina-analytics-case-study/
