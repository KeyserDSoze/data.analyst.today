## 9.11 Marketplace e network experiments: scegliere il design che misura la policy reale

Nel 9.4 abbiamo visto **perché** interference e contamination rompono un A/B individuale semplice.

Qui facciamo il passo successivo:

> **quale design possiamo usare quando il prodotto è un sistema condiviso?**

Nei marketplace, social product, logistics network e sistemi di allocazione, il risultato dipende spesso dall'equilibrio tra più attori.

### Caso simulato/composito — Ranking di un marketplace locale

Un marketplace di servizi testa un ranking che privilegia fornitori con probabilità di accettazione più alta.

Nel buyer-randomized test:

- conversion B: +0,7 pp;
- GMV/buyer: +5,9%;
- time-to-confirm: -11%.

Ma alcuni provider ricevono molta più domanda dal treatment e saturano.

La saturazione modifica disponibilità e prezzo anche per il controllo.

La domanda non è più soltanto:

> “Quale esperienza vede il buyer?”

ma:

> **“Come cambia il marketplace quando questa policy governa una quota crescente della domanda?”**

### Tre estimand possibili

**Direct user effect**

Che cosa succede al buyer assegnato a B rispetto ad A nel mercato misto corrente?

**Total marketplace effect**

Che cosa succede a GMV, fill rate e welfare complessivo se la policy viene applicata al mercato?

**Equilibrium / full-rollout effect**

Che cosa succede dopo che seller, supply, prezzi e comportamento si sono adattati al nuovo sistema?

Un buyer-level A/B può essere utile per il primo e insufficiente per il terzo.

### Cluster randomization

Possiamo randomizzare mercati relativamente indipendenti:

- città;
- zone;
- store catchment;
- community;
- tenant.

Vantaggi:

- riduce spillover tra arm;
- l'unità di trattamento è più vicina all'equilibrio locale.

Costi:

- pochi cluster;
- grande variabilità tra cluster;
- minore power;
- rischio che geografie differiscano strutturalmente.

Non possiamo recuperare il numero effettivo di unità contando milioni di transazioni dentro 20 città.

### Switchback experiments

Se non abbiamo abbastanza mercati indipendenti, possiamo alternare il trattamento **nel tempo** sullo stesso mercato.

Esempio:

```text
Roma
08–10 A
10–12 B
12–14 A
14–16 B
```

oppure randomizzare blocchi di 30/60 minuti con schema bilanciato.

Questo può essere utile per:

- ride-hailing;
- delivery;
- dispatch;
- pricing dinamico;
- ranking condiviso.

Ma il design deve controllare:

- time-of-day seasonality;
- day-of-week;
- carryover;
- inventory che persiste;
- driver/seller che reagiscono lentamente;
- autocorrelazione.

Il Capitolo 7 diventa parte del design sperimentale.

### Carryover

Supponiamo che B incentivi driver a entrare online.

Quando il sistema torna ad A, quei driver possono rimanere disponibili per un'ora.

La finestra A successiva è contaminata dall'effetto precedente.

Possibili strategie:

- washout period;
- blocchi temporali più lunghi;
- modellazione del carryover;
- estimand esplicitamente dinamico.

### Saturation experiment

Un'altra domanda utile è come l'effetto cambia con la percentuale di trattamento.

Possiamo testare cluster con, per esempio:

- 0%;
- 25%;
- 50%;
- 75%;
- 100% exposure.

L'obiettivo è studiare se il trattamento:

- scala linearmente;
- satura;
- cannibalizza;
- produce threshold effects;
- modifica l'equilibrio.

Questo è molto più informativo di assumere che un effetto misurato al 10% resti identico al 100%.

### Two-sided marketplace metrics

Una decisione marketplace dovrebbe spesso includere metriche su entrambi i lati.

Buyer:

- conversion;
- wait time;
- price;
- cancellations.

Seller/supply:

- utilization;
- earnings;
- acceptance;
- concentration;
- churn;
- fairness/distribution quando rilevante.

Platform:

- GMV;
- contribution margin;
- fill rate;
- reliability.

Una policy che migliora buyer conversion distruggendo supply health può avere effetto positivo nel test breve e negativo nel steady state.

### Tenant randomization come caso affine

Microsoft Research documenta difficoltà analoghe negli esperimenti enterprise: quando l'esperienza deve essere coerente all'interno di un'organizzazione, la randomization unit può diventare il **tenant**. Questo preserva coerenza e riduce interference interna, ma rende la statistica più difficile per la forte eterogeneità dei tenant e il numero minore di unità.[^ms-tenant]

Il caso non è un marketplace, ma la logica è la stessa:

> randomizzare al livello in cui l'interazione rende impossibile trattare gli individui come mondi indipendenti.

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

> **Quando il trattamento modifica il mercato, la domanda non è soltanto come randomizzare meglio gli utenti. È quale esperimento rappresenta meglio il mondo che esisterà dopo lo ship.**

[^ms-tenant]: Microsoft Research, *Why Tenant-Randomized A/B Test is Challenging and Tenant-Pairing May Not Work*: https://www.microsoft.com/en-us/research/articles/why-tenant-randomized-a-b-test-is-challenging-and-tenant-pairing-may-not-work/
