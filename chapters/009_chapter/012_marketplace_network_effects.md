## 9.11 Marketplace e network experiments: misurare il mondo che esisterà dopo lo ship

Nei marketplace, nei social product, nelle reti logistiche e nei sistemi di allocazione il trattamento non modifica soltanto l'utente che lo riceve. Cambia spesso l'ambiente condiviso: domanda, offerta, disponibilità, prezzi, congestione e comportamento degli altri attori.

In questi sistemi il design sperimentale deve partire da una domanda più forte di “come randomizziamo gli utenti?”:

> **quale effetto della policy vogliamo conoscere e quale esperimento rappresenta meglio il mondo in cui quella policy sarà usata?**

### Caso simulato/composito — Ranking di un marketplace locale

Un marketplace di servizi privilegia provider con probabilità di accettazione più alta. Nel buyer-randomized test osserviamo conversion B +0,7 pp, GMV/buyer +5,9% e time-to-confirm -11%.

Ma alcuni provider ricevono molta più domanda dal treatment e saturano. La saturazione modifica disponibilità e prezzo anche per i buyer di controllo. L'effetto misurato al 50% di traffico misto non è automaticamente ciò che succederebbe al 100%.

Possiamo infatti voler stimare tre cose diverse. Il **direct user effect** chiede che cosa accade al buyer assegnato a B nel mercato misto corrente. Il **total marketplace effect** chiede come cambiano GMV, fill rate e welfare complessivo. L'**equilibrium/full-rollout effect** include anche l'adattamento successivo di seller, supply, prezzi e comportamento. Un buyer-level A/B può essere ottimo per il primo e insufficiente per il terzo.

### Cluster: separare i mercati quando possiamo

Se città, zone, tenant o community interagiscono molto al loro interno e poco tra loro, possiamo randomizzare cluster. Il trattamento si avvicina così all'equilibrio locale e riduce spillover tra arm.

Il prezzo è statistico: pochi cluster, forte eterogeneità e minore power. Venti città con milioni di transazioni restano venti unità randomizzate, non milioni di esperimenti indipendenti.

### Switchback: usare il tempo quando lo spazio non basta

Se non esistono abbastanza mercati indipendenti, possiamo alternare A e B sullo stesso sistema:

```text
Roma
08–10 A
10–12 B
12–14 A
14–16 B
```

Questo design è utile per ride-hailing, delivery, dispatch, dynamic pricing o ranking condiviso, ma rende il tempo parte dell'inferenza. Time-of-day, day-of-week, autocorrelazione e carryover devono essere gestiti esplicitamente.

Se B incentiva driver a entrare online, per esempio, quei driver possono restare disponibili quando il sistema torna ad A. La finestra successiva non è più un controllo puro. Washout period, blocchi più lunghi o un estimand dinamico diventano scelte di design, non dettagli tecnici.

### Saturation: l'effetto può dipendere dalla percentuale trattata

Un modo per studiare l'equilibrio è variare la quota di trattamento tra cluster o periodi, per esempio 0%, 25%, 50%, 75% e 100%. Se l'effetto satura, cannibalizza o mostra threshold, la curva di saturation è molto più informativa di un singolo contrasto misurato al 10%.

### Una policy two-sided richiede metriche two-sided

Nei marketplace una decisione non può spesso essere giudicata soltanto dal lato buyer. Conversion, wait time, price e cancellation devono convivere con seller utilization, earnings, acceptance, concentration, churn e con metriche di piattaforma come GMV, contribution margin, fill rate e reliability.

Una policy che migliora la conversione dei buyer distruggendo la salute della supply può vincere nel test breve e peggiorare lo steady state. È ancora una volta un problema di Metric Contract, ma applicato a un sistema interdipendente.

Microsoft Research documenta difficoltà analoghe nei tenant-randomized experiments enterprise: quando l'esperienza deve essere coerente dentro l'organizzazione, randomizzare il tenant riduce interference interna ma abbassa il numero effettivo di unità e rende più importante la forte eterogeneità tra cluster.[^ms-tenant]

### Network experiment card

```text
Actors nel sistema:
Shared resources:
Direct effect desired?
Total/equilibrium effect desired?
Interference graph plausibile:
Cluster candidates:
Number of clusters:
Switchback possible?
Carryover duration:
Seasonality controls:
Saturation levels useful?
Two-sided guardrails:
Effect expected to change at 100% rollout?
```

> **Quando il trattamento modifica il mercato, l'esperimento deve rappresentare la policy che vogliamo mettere a regime, non soltanto la variante che riusciamo più facilmente a bucketizzare.**

[^ms-tenant]: Microsoft Research, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work*: https://www.microsoft.com/en-us/research/articles/why-tenant-randomized-a-b-test-is-challenging-and-tenant-pairing-may-not-work/
