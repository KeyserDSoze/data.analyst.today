## 9.1 Unità di randomizzazione, exposure e analisi: quattro livelli da non confondere

Nel Capitolo 8 abbiamo visto perché la randomizzazione può rendere credibile il controfattuale.

Qui la domanda è operativa:

> **che cosa stiamo realmente assegnando, che cosa viene realmente esposto e su quale unità calcoliamo l'outcome?**

Sono domande diverse.

### Quattro unità utili

**Unità di decisione**

Chi o che cosa subirà la policy se il test vince?

**Unità di randomizzazione**

L'entità a cui assegniamo stabilmente A o B.

**Unità di exposure**

L'entità che può effettivamente ricevere il trattamento.

**Unità di analisi**

Il livello a cui definiamo outcome e incertezza.

Possono coincidere. Non devono farlo necessariamente.

### Caso simulato/composito — QuickPay randomizzato per sessione

Il team implementa QuickPay per sessione perché è tecnicamente semplice.

Dopo tre giorni:

| Variante | Sessioni | Conversion rate |
|---|---:|---:|
| A | 512.420 | 3,89% |
| B | 510.976 | 4,11% |

Il risultato sembra favorevole.

Poi l'analista controlla l'identità:

- 27% degli utenti ha avuto più di una sessione;
- 14% ha visto entrambe le esperienze;
- una quota usa sia app sia web.

Lo stesso cliente può quindi:

1. vedere il checkout standard su web;
2. tornare da app;
3. vedere QuickPay;
4. portare apprendimento dalla prima esperienza alla seconda.

Il trattamento non è stabile a livello utente.

Se la decisione riguarda l'esperienza del cliente, randomizzare la sessione può essere il livello sbagliato.

### Persistent bucketing

Una randomizzazione utile deve essere **stabile** per la durata in cui la stabilità è parte del trattamento.

Esempio concettuale:

```text
hash(stable_user_id, experiment_id) -> bucket A/B
```

I problemi iniziano quando lo `stable_user_id` non è davvero stabile:

- cookie cancellati;
- device diversi;
- login tardivo;
- account merge;
- utenti anonimi che diventano autenticati;
- ID rigenerati dopo update.

Il codice di randomizzazione può essere corretto e la semantica dell'identità sbagliata.

### Assignment non significa exposure

Un utente può essere assegnato a B ma non vedere mai la feature perché:

- non raggiunge il checkout;
- non è realmente eleggibile;
- la feature flag fallisce;
- il client è troppo vecchio;
- un crash avviene prima della visualizzazione;
- il componente non carica.

Quindi dobbiamo distinguere almeno:

```text
assigned_B
eligible_B
exposed_B
successfully_rendered_B
```

Analizzare soltanto gli `exposed_B` può però introdurre selection bias se l'exposure è influenzata dal trattamento.

L'Experiment Contract deve dichiarare in anticipo quale popolazione definisce l'estimand e come verranno gestiti assignment ed exposure.

### Account e tenant nei prodotti B2B

In un SaaS collaborativo, randomizzare singoli utenti dello stesso account può essere impossibile o indesiderabile.

Se metà del team vede una nuova permission model e metà no:

- l'esperienza può diventare incoerente;
- gli utenti si influenzano;
- le azioni di uno cambiano gli outcome degli altri.

Per questo nei prodotti enterprise può essere necessario randomizzare a livello **tenant/account**.

Microsoft Research discute esplicitamente le difficoltà dei tenant-randomized experiments: l'unità sperimentale è il tenant, i tenant possono differire enormemente per dimensione e metriche aggregate, e la sensibilità statistica può peggiorare rispetto alla randomizzazione individuale.[^ms-tenant]

### Cluster randomization: il numero di righe non è il numero di unità

Una catena di 180 supermercati testa una procedura di picking.

La procedura viene condivisa tra i dipendenti dello stesso store, quindi randomizza negozi interi.

Potremmo avere:

- 180 store randomizzati;
- 4.000 picker;
- 2 milioni di ordini.

Ma non abbiamo 2 milioni di unità indipendenti di trattamento.

Il design deve rispettare il clustering introdotto dall'assignment.

Questo influenza:

- effective sample size;
- precisione;
- durata;
- analisi.

### Randomization unit diversa dalla metric unit

Supponiamo di randomizzare utenti ma misurare `revenue per user`.

Coerente.

Supponiamo invece di randomizzare account e calcolare una media su tutte le singole azioni come se fossero indipendenti.

Rischiamo di dare peso enorme ai tenant grandi e sottostimare l'incertezza.

Prima del test bisogna decidere:

> **qual è il peso decisionale corretto di ogni unità randomizzata?**

### Cross-device e identity resolution

Un test mobile/web può essere particolarmente fragile.

Domande operative:

- il bucket viene definito da account ID quando disponibile?
- cosa succede prima del login?
- un utente anonimo randomizzato ad A e poi autenticato su un account B cambia variante?
- come vengono deduplicati gli outcome cross-device?

Questo è il punto in cui il Capitolo 3 sull'identità incontra direttamente l'experimentation.

### Randomization card

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

> **La randomizzazione non è soltanto una percentuale 50/50. È una scelta su quale entità deve vivere in un mondo sperimentale coerente.**

[^ms-tenant]: Microsoft Research, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work*: https://www.microsoft.com/en-us/research/articles/why-tenant-randomized-a-b-test-is-challenging-and-tenant-pairing-may-not-work/
