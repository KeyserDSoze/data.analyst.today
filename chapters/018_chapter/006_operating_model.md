## 18.5 Operating model: decentralizzare il lavoro senza decentralizzare la fiducia

Quando analytics cresce, la domanda organizzativa non è “quanti analyst ci servono?”, ma **quali responsabilità devono stare vicino al dominio e quali capability conviene costruire una volta sola**. Questa scelta determina velocità, qualità, duplicazione, supporto, governance e costo molto più di quanto faccia l'organigramma in sé.

Il capitolo ha già separato decision owner, semantic owner e product owner. L'operating model deve distribuire questi ruoli senza creare due failure mode opposti: un centro che diventa collo di bottiglia semantico per tutta l'azienda, oppure domini autonomi che duplicano metriche, infrastruttura e policy fino a perdere interoperabilità.

## Tre modi di scalare male

La **centralizzazione totale** concentra standard e competenza, ma può produrre backlog infinito, scarsa conoscenza del dominio e un team centrale che finisce per decidere il significato di processi che non conosce abbastanza. La **federazione totale** porta ownership vicino alla decisione, ma può moltiplicare semantic model, pipeline, security pattern e costi. Esiste poi un terzo stato, meno evidente: **centralized approval theater**. Formalmente i domini sono owner; in pratica ogni modifica attraversa una lunga catena centrale. La responsabilità è locale, l'autorità no, e nessuno sa davvero chi sia accountable.

La soluzione non è scegliere ideologicamente tra centro e federazione. È distinguere le capability.

Un **domain analytics/data product team** deve stare vicino al business e possedere use case, semantica locale, feedback e parte del supporto. Una **shared analytics platform** deve fornire orchestration, storage/query capability, CI/CD pattern, observability, catalogo, access primitive, cost metadata e template riutilizzabili. **Governance, risk e security** definiscono policy comuni dove la libertà locale genererebbe rischio sistemico — privacy, identity, retention, classification, audit e interoperabilità. Un **Analytics Enablement/COE** può poi diffondere pattern, formare creator e consumer, sostenere community e trasformare buone pratiche locali in standard.

La piattaforma non deve diventare owner di ogni prodotto. Il COE non deve diventare una report factory né un veto committee. Governance non deve riappropriarsi della decisione di dominio. Il disegno funziona solo se ogni funzione ha una boundary riconoscibile.

## Il valore del modello AWS: significato e capability sono lavori diversi

AWS Prescriptive Guidance, nel descrivere team e responsabilità per un data mesh, separa domain team, self-service data platform team e governance team. I domain team possiedono data product e business use case; il platform team mantiene la soluzione condivisa; governance definisce principi e guardrail. Non serve adottare un data mesh per usare questa struttura: è utile perché rende evidente che **conoscere il significato del dato** e **costruire le capability comuni** sono responsabilità diverse.

Fonte: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/teams-interactions.html

Microsoft descrive analogamente il Center of Excellence come un team interno di esperti tecnici e business che assiste attivamente la community e promuove gli obiettivi di adozione. Anche qui il COE non è definito come owner universale di tutti i contenuti.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-center-of-excellence

## Approval rate: tutti responsabili di un pezzo, nessuno del processo

Una fintech monitora l'approval rate dei pagamenti. Payments Engineering gestisce gateway e provider; Risk modifica regole antifrode; Finance misura il costo delle false decline; Analytics mantiene la dashboard. Quando approval rate scende di quattro punti, Engineering guarda latency, Risk le regole, Finance aspetta un numero riconciliato, Analytics produce breakdown. Tutti sono responsabili di qualcosa; nessuno possiede la **health del decision process end-to-end**.

L'azienda non crea un nuovo team. Rende esplicita la responsabilità: VP Payments come decision owner; Payments Analytics con Finance come semantic owner per economics; Analytics Engineering come product owner; incident commander per SEV-1/2; common runbook e SLO condivisi. Il cambiamento organizzativo non consiste nel nuovo organigramma, ma nel sapere chi può bloccare il dato, attivare fallback e accettare il rischio residuo.

## RACI non basta se l'owner non ha capacità operativa

Una RACI può aiutare, ma non crea accountability se l'`Accountable` non ha autorità, il `Responsible` non ha capacity, tutti sono `Consulted` e nessuno riceve l'alert fuori orario. Per ogni ownership dobbiamo chiedere se la persona o il team ha accesso ai sistemi, capacità allocata alla manutenzione, backup, authority di change e incentivi a investire in reliability.

Ownership senza queste condizioni è documentazione.

Lo stesso vale per i team boundary. Un data product può attraversare cinque team; non è necessario eliminare tutte le dipendenze. Serve però che ogni boundary esponga una promessa osservabile:

```text
CRM domain
  ↓ source contract
Revenue product
  ↓ certified metric contract
Executive pack
  ↓ decision deadline
CFO review
```

Più handoff ci sono, più contract, SLO ed escalation devono rendere visibile come un failure si propaga.

## Support model ed escalation

Un prodotto critico non può dipendere soltanto dal canale `#data-help`. T1 può avere un owner di team in business hours. T2 può richiedere primary owner, backup ed escalation al decision owner se la deadline è a rischio. T3 può avere un incident process con authority esplicita per bloccare pubblicazione, attivare fallback, sospendere change e informare gli stakeholder critici.

Anche il supporto va separato: consumer support (“come uso il prodotto?”), data quality support (“il numero non sembra corretto”), access support, incident e change request sono code con priorità diverse. Se tutto entra nello stesso backlog, feature, incident e manutenzione competono senza una policy leggibile.

## Il portfolio consuma capacità anche quando non cambia

Un team che possiede prodotti in esercizio non può pianificare il 100% del tempo su nuove feature. Reliability, incident, semantic debt, tech debt, cost optimization, supporto e deprecation consumano capacità reale. Ignorarli produce l'illusione di scalare perché aumenta il numero di asset mentre diminuisce la probabilità che qualcuno riesca ancora a mantenerli bene.

Qui diventa utile il concetto SRE di **toil**: lavoro operativo manuale, ripetitivo e poco duraturo che tende a crescere linearmente con il servizio. In analytics può significare refresh manuale, mapping aggiornati a mano, reconciliation identica ogni settimana, ticket “quale tabella?”, recovery non automatizzata o access provisioning ripetitivo.

Fonte: https://sre.google/sre-book/part-II-principles/

Non tutto il lavoro manuale è toil. Un'indagine una tantum può essere manuale e ad altissimo valore. Il segnale è diverso: **il lavoro si ripete perché il sistema non ha incorporato l'apprendimento**.

DORA rafforza lo stesso punto dalla prospettiva delivery: continuous delivery non si ottiene eseguendo più spesso il processo precedente; senza redesign e capability adeguate, più frequenza può produrre più failure e burnout.

Fonte: https://dora.dev/capabilities/continuous-delivery/

Per questo l'automazione viene dopo il redesign: chiarire responsibility, eliminare passaggi inutili, definire contract, standardizzare il ricorrente e solo allora automatizzare.

## Operating-model review

Un portfolio maturo dovrebbe chiedere periodicamente quali prodotti hanno owner chiari, quali hanno superato il tier previsto, dove il centro è diventato collo di bottiglia, quali capability sono duplicate, dove il toil cresce linearmente, quali incidenti attraversano troppi handoff, quali prodotti non hanno backup owner e quali dovrebbero essere ritirati.

Questa review non cerca la struttura organizzativa perfetta. Cerca mismatch tra responsabilità, autorità e impatto reale.

> **Federare significa spostare responsabilità vicino al contesto, non spostare il problema della qualità sul consumer. Centralizzare significa creare capability comuni, non assumere che un team centrale possa possedere il significato di tutta l'organizzazione.**

Con ownership e boundary allineati, possiamo ora automatizzare il cambiamento senza trasformare la delivery chain in una macchina che propaga più rapidamente errori semantici.