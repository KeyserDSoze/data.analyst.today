## 19.6 Decision span: quanto vicino lavori alla scelta?

Il Capitolo 15 ha già costruito il Decision Record e distinto finding, insight, recommendation e decisione. Qui interessa una conseguenza professionale di quel metodo. Quando produrre un'analisi diventa meno costoso, cresce il valore di chi sa accompagnare l'evidenza abbastanza vicino alla scelta da renderla utile, senza superare né il claim consentito né l'authority posseduta.

Chiamiamo questa ampiezza **decision span**.

| Livello | Che cosa possiedo | Domanda dominante |
|---|---|---|
| Output | query, report, dataset, dashboard, modello | ho prodotto correttamente l'oggetto richiesto? |
| Evidence | fenomeno, segmenti, incertezza, caveat, interpretazione | che cosa possiamo sostenere? |
| Alternatives | opzioni, costi, guardrail, switching value | che cosa possiamo fare e che cosa cambierebbe la preferenza? |
| Decision design | policy, experiment, rollout, allocation, escalation | come trasformiamo l'evidenza in un meccanismo di azione controllabile? |
| Decision system | evidenza ricorrente, semantica, automazione, feedback | come fa il processo a continuare a decidere bene nel tempo? |

Aumentare decision span non significa prendere il posto del manager. Il CFO, il COO o un Product VP possono conoscere vincoli strategici, contrattuali, organizzativi o politici che non sono interamente rappresentati nei dati. Per questo la recommendation analitica e la decisione scelta restano oggetti distinti, con un decision owner esplicito. Il valore dell'analista sta nel ridurre l'ambiguità e rendere leggibili alternative e trade-off, non nell'usurpare authority.

Un caso sul churn rende concreto il salto. Una SaaS company osserva churn mensile al `7,8%` contro target `6,5%`; Enterprise è al `4,1%`, SMB al `10,9%` e i clienti low-usage al `18,3%`. Un breakdown corretto è già evidenza utile. Ma se il team retention può intervenire soltanto su una parte degli account, la decisione richiede altro: Customer Success call, onboarding intensivo, technical review, discount o nessun intervento competono tra loro e consumano capacità differenti.

A quel punto la domanda non è più “chi ha churn risk alto?”. Diventa: **su quali account, con quale intervento e dato il nostro vincolo operativo abbiamo sufficiente valore atteso per agire?** Il modello predittivo resta importante, ma diventa un input del sistema di decisione.

È lo stesso salto che abbiamo incontrato in altri capitoli. Una probabilità di churn dell'82% non contiene una recommendation senza customer value, costo dell'intervento, uplift plausibile, capacità e guardrail. Un forecast non decide lo staffing finché la distribuzione prevista non incontra una loss function operativa. Un experiment non termina con l'uplift finché non esiste una rollout policy. Un effetto causale richiede sapere per quale popolazione il claim vale. Un agente non è pronto a operare finché authority, failure cost ed escalation non sono definiti.

Questa vicinanza alla decisione richiede anche **outcome awareness**. L'analista non possiede necessariamente l'outcome finale, ma dovrebbe sapere quale decisione è stata presa, che cosa è stato implementato davvero, quali guardrail si sono mossi e quale assunzione va aggiornata dopo l'esito. Senza questo ritorno di informazione, il lavoro si interrompe proprio nel punto in cui potrebbe produrre apprendimento professionale.

L'AI rende il decision span ancora più importante perché può saltare facilmente dalla domanda alla recommendation. Scenari, ranking ed executive summary possono essere prodotti quasi nello stesso momento. La velocità crea una scorciatoia pericolosa:

`output → recommendation`

Il percorso professionale deve invece preservare:

**evidence → alternatives → uncertainty → trade-off → recommendation → decision owner → outcome review**

Non perché ogni caso richieda un processo pesante, ma perché ogni salto rimosso deve essere giustificato dal rischio, non dalla facilità con cui il sistema genera la pagina successiva.

Sviluppare decision span significa quindi cercare progressivamente problemi in cui non ci limitiamo a ricevere i dati, ma impariamo a chiedere quale decisione è aperta, quali alternative sono reali, quale informazione potrebbe cambiarne il ranking, come verrà misurato l'outcome e quando il processo merita di diventare ricorrente.

> **Quando produrre analisi diventa economico, cresce il valore di saper portare l'evidenza verso una decisione senza oltrepassare ciò che sappiamo, ciò che possiamo dimostrare e ciò che siamo autorizzati a decidere.**