## 9.4 Contaminazione e interferenza: quando il controllo non resta davvero controllo

Il Capitolo 8 ha introdotto l'**interference** come problema causale: il trattamento assegnato a un'unità può cambiare l'outcome di un'altra.

In un esperimento operativo questo diventa una domanda di design:

> **possiamo creare due mondi abbastanza separati da misurare l'effetto che ci interessa?**

### Contamination e interference non sono identiche

**Contamination**

Un'unità di controllo riceve, direttamente o indirettamente, parte del trattamento.

Esempio: un Sales Rep di controllo copia il nuovo playbook da un collega trattato.

**Interference / spillover**

Il trattamento di una unità modifica l'ambiente o l'outcome di altre unità, anche se queste non ricevono la feature.

Esempio: trattare buyer cambia domanda, prezzo e inventario dei seller condivisi.

Entrambi riducono la separazione tra A e B, ma possono richiedere strategie differenti.

### Caso simulato/composito — Ranking marketplace randomizzato per buyer

Un marketplace testa una logica che dà più visibilità ai seller con consegne rapide.

Randomizzazione iniziale: buyer-level.

Dopo due settimane:

- conversion B: +1,7%;
- GMV B: +2,4%;
- delivery time: -4,1%.

Sembra una vittoria.

Ma i seller reagiscono alla nuova domanda:

- aumentano stock;
- cambiano prezzo;
- spostano promozioni;
- danno priorità agli SKU più visibili.

Queste azioni cambiano anche ciò che vedono i buyer di controllo.

Il control arm non rappresenta più il marketplace che sarebbe esistito **senza** il trattamento.

### Dilution: un effetto reale può sembrare piccolo

Se il trattamento produce spillover positivi sul controllo, il contrasto A/B può essere attenuato.

Esempio:

```text
effetto diretto su B: +5%
spillover su A: +2%
differenza osservata: circa +3%
```

L'esperimento individuale può quindi sottostimare l'effetto di un rollout globale.

L'opposto è possibile se il trattamento sottrae risorse al controllo.

### Cannibalization e sistemi a capacità limitata

Supponiamo di testare una promo che aumenta la visibilità di alcuni ristoranti.

Il GMV dei trattati cresce.

Ma se la domanda totale è quasi fissa, parte della crescita può provenire da ristoranti di controllo.

A livello unitario la variante sembra creare valore; a livello marketplace può stare soprattutto **redistribuendo** valore.

Per questo dobbiamo decidere qual è l'estimand:

- effetto sul singolo seller trattato?
- effetto totale sulla piattaforma?
- effetto di equilibrio al 100% rollout?

### Caso simulato/composito — Lead scoring condiviso

Metà dei Sales Representative riceve un nuovo lead score.

Dopo pochi giorni:

- i commerciali parlano tra loro;
- condividono priorità nel CRM;
- i manager ridistribuiscono lead sulla base delle nuove informazioni.

Il gruppo di controllo inizia a usare indirettamente il trattamento.

Il problema non è solo statistico. È organizzativo.

### Strategie di design

A seconda del sistema possiamo considerare:

**Cluster randomization**

Randomizzare team, store, tenant o community abbastanza isolate.

**Geo experiments**

Usare aree con interazioni limitate, quando geografia e media mix lo permettono.

**Switchback experiments**

Alternare trattamento e controllo nel tempo su sistemi condivisi, per esempio marketplace o logistics, quando una randomizzazione simultanea individuale produce interference forte.

**Holdout strutturali**

Mantenere una popolazione non esposta abbastanza separata per misurare effetti di lungo periodo.

**Modelli espliciti di spillover**

Quando la rete è parte del fenomeno, stimare effetti diretti e indiretti invece di fingere indipendenza.

### Switchback: il tempo diventa unità sperimentale

Supponiamo che una piattaforma ride-hailing modifichi un algoritmo di matching che influenza driver e rider nello stesso mercato.

Randomizzare rider individuali crea equilibrio misto.

Una strategia può essere alternare il mercato tra A e B per finestre temporali:

```text
08:00–09:00 A
09:00–10:00 B
10:00–11:00 A
...
```

Ma introduce nuovi problemi:

- carryover tra finestre;
- stagionalità oraria;
- autocorrelazione;
- numero effettivo di periodi indipendenti.

Il Capitolo 7 ci ricorda che il tempo non può essere trattato come un normale shuffle casuale.

### Concurrent experiments

Nelle piattaforme mature gli stessi utenti possono essere contemporaneamente in più test.

Microsoft ExP documenta che centinaia di esperimenti possono girare nello stesso ecosistema; le interazioni non sono automaticamente catastrofiche, ma gli experiment owner devono conoscere test incompatibili o meccanismi che possono interagire.[^ms-interactions]

Quindi non serve isolare ogni esperimento dal mondo intero.

Serve capire **quali interazioni sono materialmente plausibili**.

### Interference card

```text
Randomization unit:
Con chi interagisce?
Risorse condivise:
Inventory/capacity condivisa:
Treatment può cambiare ambiente del controllo?
Contamination diretta possibile?
Concurrent experiments rilevanti?
Effetto desiderato: diretto, totale, equilibrium?
Design alternativo: cluster / geo / switchback / holdout?
Carryover plausibile?
```

> **Quando A può modificare il mondo in cui vive B, il problema non è “più rumore”. È che il confronto può non rappresentare più la policy che vogliamo valutare.**

[^ms-interactions]: Microsoft Research, *A/B Interactions: A Call to Relax*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/a-b-interactions-a-call-to-relax/
