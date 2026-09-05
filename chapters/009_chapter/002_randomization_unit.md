## 9.1 Randomization, exposure e analysis unit: costruire due mondi coerenti

La randomizzazione è utile solo se l'unità che assegniamo riesce a vivere in una variante abbastanza coerente da rendere interpretabile il confronto. Per questo “50/50” non descrive ancora il design.

Dobbiamo distinguere almeno quattro livelli. L'**unità di decisione** è chi subirà la policy se il test vince; l'**unità di randomizzazione** è ciò che assegniamo stabilmente ad A o B; l'**unità di exposure** è ciò che può realmente ricevere il trattamento; l'**unità di analisi** è il livello a cui definiamo outcome e incertezza. Possono coincidere, ma non dobbiamo assumerlo.

### QuickPay: quando la sessione è troppo piccola

Supponiamo che QuickPay venga randomizzato per sessione perché l'implementazione è semplice. Dopo tre giorni osserviamo:

| Variante | Sessioni | Conversion rate |
|---|---:|---:|
| A | 512.420 | 3,89% |
| B | 510.976 | 4,11% |

Il delta sembra favorevole. Poi controlliamo l'identità: il 27% degli utenti ha più di una sessione, il 14% ha visto entrambe le esperienze e una quota utilizza sia app sia web. Lo stesso cliente può vedere il checkout standard su web, tornare da app, incontrare QuickPay e portare apprendimento dalla prima esperienza alla seconda.

Se la policy finale riguarda l'esperienza del **cliente**, la sessione è una randomization unit troppo piccola. Il test non ha creato due mondi stabili a livello decisionale.

### La stabilità dell'identità è parte della randomizzazione

Un meccanismo concettuale come

```text
hash(stable_user_id, experiment_id) -> bucket A/B
```

è utile solo se `stable_user_id` è davvero stabile. Cookie cancellati, device multipli, login tardivo, account merge, utenti anonimi che diventano autenticati o ID rigenerati dopo un update possono spostare la stessa persona tra varianti senza che l'algoritmo di hashing abbia alcun bug.

Questo è il punto in cui il Capitolo 3 sull'identità entra direttamente nell'experimentation: il codice di randomizzazione può essere corretto mentre la semantica dell'identità è sbagliata.

### Assignment non è exposure

Anche con un bucket stabile, essere assegnati a B non significa aver ricevuto B. Un utente può non arrivare al checkout, non essere realmente eleggibile, usare un client troppo vecchio, subire un crash prima del rendering o non caricare il componente.

Per questo è utile separare eventi come:

```text
assigned_B
eligible_B
exposed_B
successfully_rendered_B
```

Questa distinzione non autorizza però a confrontare automaticamente `exposed_B` con `exposed_A`. Se il trattamento stesso influenza la probabilità di exposure o di restare osservabile, filtrare sui soli exposed può introdurre selection bias. L'Experiment Contract deve quindi dichiarare quale estimand vogliamo — spesso intent-to-treat sull'assignment — e usare exposure soprattutto come diagnostica della delivery del trattamento.

### Quando l'unità deve diventare più grande

Nei prodotti collaborativi B2B, randomizzare singoli utenti dello stesso tenant può creare un'esperienza incoerente e spillover interni. Se metà team vede una nuova permission model e metà no, le azioni di un utente modificano il lavoro degli altri. In questi casi può essere necessario randomizzare a livello **tenant/account**.

Microsoft Research documenta proprio la difficoltà dei tenant-randomized experiments: l'esperienza resta coerente dentro l'organizzazione, ma il numero di unità sperimentali si riduce e i tenant possono avere dimensioni molto diverse, con conseguenze su sensibilità e weighting.[^ms-tenant]

La stessa logica vale per cluster fisici. Se una procedura di picking viene condivisa tra i dipendenti dello stesso supermercato, possiamo avere 180 store randomizzati, 4.000 picker e 2 milioni di ordini. Il numero di righe non diventa il numero di unità indipendenti di trattamento. Il clustering entra direttamente nell'effective sample size e nell'incertezza.

### Randomization unit e metric unit devono parlarsi

Se randomizziamo utenti e misuriamo `revenue per user`, la coerenza è immediata. Se randomizziamo account ma trattiamo ogni singola azione come indipendente, i tenant più grandi possono dominare l'analisi e l'incertezza può essere sottostimata.

La domanda corretta è quindi:

> **qual è il peso decisionale corretto di ciascuna unità randomizzata e quale livello di analisi conserva la dipendenza introdotta dal design?**

Nei test cross-device questa domanda va accompagnata da un'altra: che cosa succede prima del login, come vengono riconciliati bucket anonimi e account autenticati, e come deduplichiamo gli outcome che appartengono alla stessa persona?

### Randomization card

Questa è una delle strutture che merita di restare scansionabile, perché deve essere compilata prima del lancio:

```text
Decision unit:
Randomization unit:
Stable identifier:
Exposure unit:
Analysis unit:
Eligibility moment:
Cross-device behavior:
Persistent bucketing:
Cluster/interference risk:
Assignment vs exposure policy:
Effective number of randomized units:
```

> **La randomizzazione non è una percentuale. È una scelta su quale entità deve vivere in un mondo sperimentale sufficientemente coerente da rappresentare la policy che vogliamo valutare.**

[^ms-tenant]: Microsoft Research, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work*: https://www.microsoft.com/en-us/research/articles/why-tenant-randomized-a-b-test-is-challenging-and-tenant-pairing-may-not-work/
