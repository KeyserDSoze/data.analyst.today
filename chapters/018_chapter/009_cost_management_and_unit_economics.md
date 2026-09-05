## 18.8 Cost-to-serve: una promessa operativa ha anche un'economia

Una piattaforma analitica può diventare tecnicamente più sofisticata e contemporaneamente economicamente peggiore. I costi raramente esplodono per una sola scelta enorme; crescono attraverso migliaia di decisioni ragionevoli prese senza una vista comune: refresh sempre più frequenti, copie regionali, raw history letta da ogni dashboard, ambienti dimenticati, notebook sempre accesi, streaming per decisioni giornaliere, agenti che ripetono query costose, asset che nessuno usa più.

La domanda utile non è quindi “come riduciamo il cloud bill?”, ma:

> **Quale prodotto, consumer o decisione genera questo costo, e il valore ottenuto giustifica il livello di servizio che stiamo pagando?**

È qui che cost management torna dentro l'Analytics Operating Contract. Reliability, freshness e recovery non sono gratis; per questo devono essere lette insieme a criticality, adoption e valore.

## Prima l'allocazione, poi l'ottimizzazione

Un costo aggregato è difficile da governare perché nessuno può collegarlo a una scelta. Per un portfolio analitico servono dimensioni di allocazione abbastanza coerenti con il modo in cui prendiamo decisioni: team, domain, data product, workload, environment, region, consumer class, model/agent, criticality tier.

La FinOps Foundation definisce **Allocation** come la capacità di assegnare costi e utilizzo a team, progetti o altre unità responsabili e di rendere esplicita una strategia anche per i shared cost.

Fonte: https://www.finops.org/framework/capabilities/allocation/

Non tutto deve essere allocato al centesimo. Un costo diretto può essere attribuito a una pipeline o a un modello dedicato. Un shared cost può essere ripartito usando query time, storage, request count o workload unit. Una capability davvero comune — catalogo, governance, observability di base — può anche rimanere finanziata centralmente. La maturità sta nel rendere la scelta visibile e utile, non nel costruire un modello di chargeback più costoso del problema che vuole risolvere.

## Unit economics: dal costo tecnologico al valore servito

La FinOps Foundation definisce la **Unit Economics** come il collegamento tra spesa tecnologica e valore dei prodotti, servizi o attività organizzative e distingue resource-efficiency metrics da business unit metrics.

Fonte: https://www.finops.org/framework/capabilities/unit-economics/

Per analytics possiamo osservare costo per refresh, per milione di eventi, per forecast, per account scored, per decision feed, per consumer attivo o per workload business. Ma una unit metric è utile soltanto se guida un comportamento desiderabile. `Cost per query` può incentivare meno query anche quando la query crea valore. `Cost per decision feed` può essere più vicino al servizio reale. La metrica deve rappresentare l'economia della capability, non soltanto la voce che il provider fattura.

## La dashboard “gratuita” da €31.000 al mese

Un marketplace costruisce una executive dashboard. Nel tempo aggiunge refresh ogni dieci minuti, 34 visualizzazioni, due anni di raw event letti ripetutamente, cinque copie regionali, cinque semantic model quasi identici, export automatici e un agente che ogni ora ricalcola summary e anomalie. Il costo attribuito arriva a circa **€31.000 al mese**.

La prima reazione è “serve più capacità”. Il team invece ricostruisce il demand profile. Il CEO apre il prodotto una volta al giorno; il weekly review usa snapshot giornaliero; soltanto due metriche operative richiedono freshness sotto l'ora; l'80% delle query ripete aggregazioni calcolabili a monte; i cinque modelli regionali possono condividere core semantics; l'agente produce 24 summary al giorno ma ne vengono letti in media 1,7.

Il problema non è una query inefficiente. È un **service-level mismatch**. Il sistema sta pagando near-real-time, duplicazione e compute per consumer che non hanno quel bisogno.

## Freshness economics: ogni minuto in meno deve valere qualcosa

Chiedere “quanto vale davvero un dato più fresco?” è uno dei modi più semplici per riallineare costo e promessa. Un executive dashboard consultato una volta al giorno probabilmente non crea valore proporzionale con refresh ogni dieci minuti. Un fraud decision può invece avere valore elevato per ogni secondo di latency risparmiato. In inventory planning, alcuni segnali possono richiedere near-real-time mentre anagrafiche e dimensioni restano daily.

Non dobbiamo assegnare la freshness dell'elemento più urgente a tutto il prodotto. È una forma di over-engineering particolarmente costosa perché si moltiplica su compute, monitoring, supporto e incident surface.

La stessa logica vale per la history. Raw event retention può avere valore per audit, replay o regolazione, ma non deve essere infinita per default. L'Operating Contract può distinguere hot window, cold/archive, replay requirement, legal retention, delete policy e cost owner. Recoverability ha un valore, ma anche un costo.

## Reliability premium e criticality

Più reliability richiede test, replica, monitoring, recovery, parallel run e capacità umana. Un T1 sovra-ingegnerizzato può costare quanto un T3 senza creare valore equivalente. Per questo cost review e reliability review devono leggere lo stesso contratto: quale failure stiamo proteggendo, quale SLO abbiamo promesso, quanto costa e chi trae valore dalla protezione.

Questo evita due errori opposti. Ridurre un forecast da €2.000 a €1.300 al mese può essere una falsa economia se il servizio evita stock-out per centinaia di migliaia di euro. Mantenere una dashboard da €15.000 al mese che non entra più in alcuna decisione può invece essere un problema di **retirement**, non di tuning.

## Agent cost-to-serve: autonomia senza budget diventa spesa opaca

Con gli agenti AI compaiono costi nuovi: token/model usage, tool call, retry loop, query duplicate, evaluation e human review. Un agente può sembrare economico per singolo task e diventare costoso perché gira troppo spesso, usa sempre il modello più potente, interroga raw data quando esistono aggregate o produce output che nessuno consuma.

Per questo l'Agent Operating Profile dovrà includere anche usage budget, model routing, cache/reuse strategy, cost anomaly threshold e adoption signal. Un runtime budget non è soltanto un controllo finanziario: limita anche loop e blast radius.

Una variazione di costo va poi diagnosticata come qualsiasi anomalia. `Cost-to-serve +45% WoW con usage +3%` è un segnale azionabile. `Cloud bill +8%` molto meno. La causa può essere crescita reale, query regressiva, mancato pruning, nuovo consumer, runaway agent o change di pricing provider. Serve owner e playbook, non soltanto un alert Finance.

## Cost, output, adoption, outcome

La metrica ideale sarebbe “costo per decisione migliorata”, ma spesso non possiamo misurarla direttamente. Possiamo però costruire una gerarchia utile:

**Cost → Output → Adoption → Outcome**.

Quanto costa il prodotto? Quanti feed, forecast o query serve? Quali processi reali lo usano? Quale tempo, rischio o valore cambia? Questa sequenza impedisce di chiamare efficienza il semplice taglio di spesa e prepara la sezione successiva: un prodotto può essere economico, affidabile e comunque inutile se non entra mai in una decisione.

Una review mensile o trimestrale può quindi collegare cost driver, allocated/shared cost, SLO premium, cost per unit, adoption e evidence of value per decidere tra `optimize`, `resize`, `redesign` o `retire`.

> **Un sistema analitico sostenibile non è quello che costa poco. È quello in cui livello di servizio, costo e valore sono leggibili nello stesso Operating Contract, così possiamo distinguere reliability utile da complessità ereditata.**