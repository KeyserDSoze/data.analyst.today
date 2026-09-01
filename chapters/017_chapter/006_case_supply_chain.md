## 17.5 “Come possiamo avere più inventario e più stock-out?”

### Caso simulato/composito: Aster Components

Un produttore di componentistica, **Aster Components**, vede contemporaneamente:

- inventory value `+14% YoY`;
- stock-out in aumento;
- expedite cost in crescita;
- più capitale immobilizzato.

Il COO chiede:

> “Come possiamo avere più stock-out se abbiamo più inventario?”

La domanda sembra contraddittoria soltanto se trattiamo l'inventario come un unico blocco.

La decisione reale non è “aumentare o ridurre stock”. È:

> **dove allocare capitale e buffer per proteggere servizio e produzione al minor costo totale di rischio?**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | riallocare safety stock, reorder point e attenzione supplier |
| Failure cost | fermo linea, lost sales, expedite cost oppure eccesso di working capital |
| Claim necessario | diagnostico + scenario decisionale; non causalità perfetta |
| Reversibilità | media: inventory policy può essere corretta, ma il capitale e i lead time reagiscono lentamente |
| Incertezza critica | domanda, lead time e shortage supplier |
| Stop rule | non aumentare stock totale finché non è chiaro quali SKU generano il rischio |

## 1. L'aggregato nasconde la distribuzione

L'inventario totale è aumentato.

Ma a livello SKU emerge che:

- articoli lenti accumulano scorte;
- componenti critici hanno service level insufficiente;
- la variabilità dei lead time è aumentata;
- forecast error e bias differiscono fortemente per famiglia;
- pochi componenti possono bloccare linee ad alto valore.

La quantità totale di stock non rappresenta la disponibilità dello **stock giusto, nel posto giusto, nel momento giusto**.

## 2. Analytical Data Contract: quale unità stiamo gestendo?

Il team definisce con precisione:

- grain SKU × plant × giorno;
- inventory on hand vs available-to-promise;
- open purchase orders;
- committed stock;
- lead time osservato, non soltanto contrattuale;
- stock-out event;
- lost-sales estimate;
- production stop attribution.

Poi costruisce una scorecard con:

- inventory value;
- days of inventory;
- fill rate;
- stock-out rate;
- order cycle time;
- forecast bias;
- forecast error;
- supplier lead-time variability;
- expedite cost;
- downtime exposure.

Questa fase è un **Analytical Data Contract** perché senza semantica coerente il confronto tra servizio e capitale non è affidabile.

## 3. Segmentare per valore, variabilità e criticità

Gli SKU vengono classificati non soltanto con una ABC economica, ma anche per:

- volume;
- variabilità della domanda;
- criticità produttiva;
- sostituibilità;
- lead time;
- concentrazione supplier;
- costo del fermo linea.

Emergono 37 componenti che rappresentano una piccola parte del valore inventariale ma possono bloccare processi molto più costosi.

Questo cambia la funzione obiettivo.

Un euro di stock in più non ha lo stesso valore su ogni SKU.

## 4. Forecast non equivale a inventory policy

Il team scopre un errore organizzativo: il point forecast viene usato quasi direttamente come piano di riordino.

Ma due SKU con domanda media di 1.000 unità al mese possono richiedere buffer molto diversi se:

- uno è stabile e l'altro volatile;
- uno arriva in tre giorni e l'altro in dodici settimane;
- uno ha tre supplier e l'altro uno solo;
- uno è facilmente sostituibile e l'altro ferma la produzione.

Serve quindi un **Temporal Decision Brief** che colleghi distribuzione della domanda, lead-time uncertainty e costo dell'errore.

## 5. Scenario decisionale

Per i componenti critici il team costruisce scenari:

- lead time normale;
- shock moderato;
- shortage severa;
- domanda sopra forecast;
- supplier failure.

Per ogni scenario valuta:

- probabilità/qualità dell'assunzione;
- stock disponibile;
- produzione a rischio;
- valore economico del fermo;
- costo del buffer aggiuntivo;
- opzioni di sostituzione o riallocazione.

La decisione non cerca di eliminare tutta l'incertezza.

Cerca una policy robusta ai rischi più costosi.

## Caso reale documentato: BMW Group e shortage di semiconduttori

AWS documenta come **BMW Group**, durante la shortage globale di semiconduttori, abbia costruito con AWS Professional Services una piattaforma analitica basata su dati di produzione, mercato e input dei supplier per aumentare la trasparenza sulla domanda e supportare la distribuzione delle parti tra mercati.

Fonte: https://aws.amazon.com/solutions/case-studies/bmw-reinvent-2023-analytics/

Un ulteriore approfondimento AWS descrive una soluzione di digital supply management che integra dati di shortage, bill of materials, piani di volume, take rate, dati finanziari e market demand per valutare scenari di allocazione e supportare comitati decisionali cross-funzionali.

Fonte: https://aws.amazon.com/blogs/industries/digital-supply-management-using-advanced-analytics-and-serverless-architecture-on-aws-2/

La lezione è molto più importante della tecnologia usata:

> **la supply chain decision non è un forecast isolato; è un problema di allocazione sotto vincoli, con impatti produttivi e finanziari differenti.**

## Caso reale documentato: Coca-Cola Andina

AWS documenta anche **Coca-Cola Andina**, che ha costruito l'applicazione interna Thanos su una data platform AWS per migliorare la visibilità su inventario, distribuzione e delivery in quattro paesi. Il case study descrive dati aggiornati ogni 15 minuti anziché una volta al giorno e l'uso di modelli per anticipare ordini che rischiano di non essere ricevuti dal cliente.

Fonte: https://aws.amazon.com/solutions/case-studies/coca-cola-andina-analytics-case-study/

Anche qui il valore analitico è l'integrazione tra stato operativo, inventario e azione, non il semplice possesso di più dati.

## 6. Decision Record

Aster Components confronta tre strategie:

### A — Aumentare inventory target del 10% ovunque

Semplice, ma costoso e poco mirato.

### B — Ridurre inventory per recuperare working capital

Migliora il capitale a breve, ma aumenta il rischio sui componenti critici.

### C — Policy differenziata

- safety stock per variabilità e criticità;
- reorder point rivisti;
- supplier monitoring sui componenti critici;
- scenari per lead-time shock;
- riduzione stock sugli slow mover;
- forecast bias review per famiglia;
- alert sui componenti che possono fermare produzione;
- escalation specifica quando l'esposizione economica supera soglia.

La scelta è C.

## 7. Switching condition

La policy viene rivalutata se:

- lead-time distribution cambia regime;
- un supplier critico perde affidabilità;
- il costo del capitale cambia materialmente;
- la domanda cambia mix;
- compaiono alternative di sourcing;
- il costo di downtime cambia.

Questo evita che reorder point e safety stock diventino numeri “sacri” ereditati dal passato.

## 8. Decision Communication Pack

La headline non è:

> “Inventory +14% e stock-out +X%.”

È:

> **“Il problema non è la quantità totale di stock ma la sua allocazione: capitale eccessivo è concentrato su slow mover mentre 37 componenti critici restano esposti a variabilità di domanda e lead time. Proponiamo una policy differenziata, non un aumento generalizzato dell'inventario.”**

Le evidenze principali sono:

1. inventory/service matrix;
2. critical component exposure;
3. lead-time distributions;
4. scenario cost;
5. working-capital trade-off.

## 9. Outcome review

Il successo viene valutato con:

- fill rate;
- stock-out rate;
- inventory value;
- working capital;
- expedite cost;
- production downtime;
- forecast accuracy e bias;
- supplier lead-time reliability.

Una sola metrica non può rappresentare la qualità della policy.

## Cosa abbiamo scelto di non fare

Non serve ottimizzare matematicamente l'intera rete globale prima di correggere 37 esposizioni chiaramente critiche.

Non serve nemmeno massimizzare forecast accuracy se l'errore dominante deriva da lead-time uncertainty o allocation constraints.

La catena effettiva è:

**Analytical Brief → Analytical Data Contract → Data Readiness Review → EDA Evidence Map → Temporal Decision Brief → Decision Record → Decision Communication Pack**

> **La supply chain non si ottimizza massimizzando lo stock o minimizzandolo. Si governa allocando servizio, capitale e rischio dove il costo dell'errore è più alto.**
