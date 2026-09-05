## 9.4 Contaminazione e interferenza: quando A modifica il mondo di B

La randomizzazione individuale funziona bene quando possiamo trattare le unità come mondi sufficientemente separati. In molti prodotti questa assunzione è fragile. Un Sales Rep di controllo può copiare il nuovo playbook da un collega trattato; un ranking assegnato ai buyer può cambiare domanda, stock e prezzi dei seller condivisi; una promozione può sottrarre capacità alle unità di controllo.

Qui conviene distinguere due fenomeni. Con **contamination**, una unità di controllo riceve direttamente o indirettamente parte del trattamento. Con **interference/spillover**, il trattamento di una unità cambia l'ambiente o l'outcome di altre unità anche se non ricevono la feature. Entrambi riducono la separazione tra A e B, ma soprattutto possono cambiare **l'estimand** che il test sta misurando.

### Caso simulato/composito — Ranking marketplace randomizzato per buyer

Un marketplace testa una logica che privilegia seller con consegne rapide. Dopo due settimane il buyer-level A/B mostra conversione B +1,7%, GMV +2,4% e delivery time -4,1%.

Nel frattempo i seller reagiscono alla nuova domanda: aumentano stock, cambiano prezzo, spostano promozioni e danno priorità agli SKU più visibili. Queste azioni modificano anche ciò che vedono i buyer di controllo. Il control arm non rappresenta più il marketplace che sarebbe esistito **senza** il trattamento.

Se B produce spillover positivo su A, il contrasto può essere attenuato. Un effetto diretto di +5% accompagnato da +2% di spillover sul controllo può apparire come circa +3%. L'opposto accade se il trattamento sottrae risorse al controllo. In sistemi a capacità limitata, inoltre, una crescita dei trattati può essere soprattutto cannibalizzazione: il seller trattato guadagna GMV che un altro seller perde.

La domanda deve quindi precedere il design: vogliamo stimare l'effetto diretto sul buyer trattato, l'effetto totale sulla piattaforma o l'effetto di equilibrio a rollout completo? Un A/B individuale può essere eccellente per il primo e inadeguato per il terzo.

### Quando la randomization unit deve seguire l'interazione

Se colleghi dello stesso team condividono informazioni, randomizzare il singolo Sales Rep può contaminare il controllo. Se tenant, store, città o community sono internamente molto connessi e relativamente separati tra loro, una **cluster randomization** può creare mondi più coerenti.

Quando invece il sistema è condiviso e non abbiamo abbastanza cluster indipendenti, possiamo alternare trattamento e controllo nel tempo con uno **switchback experiment**. In un mercato ride-hailing, per esempio:

```text
08:00–09:00 A
09:00–10:00 B
10:00–11:00 A
...
```

Il vantaggio è che tutto il mercato vive la stessa policy nella finestra. Il costo è che il tempo diventa parte del design: carryover, stagionalità oraria, autocorrelazione e numero effettivo di periodi indipendenti devono essere modellati. Il Capitolo 7 torna quindi dentro l'esperimento.

Geo experiments, holdout strutturali e saturation experiments rispondono allo stesso principio: scegliere un disegno che rappresenti meglio il mondo della policy, non quello più facile da implementare.

### Concurrent experiments: non ogni interazione è una crisi

Nelle piattaforme mature gli stessi utenti partecipano a molti esperimenti. Microsoft ExP documenta che le interazioni tra test non sono automaticamente frequenti o catastrofiche; il punto è identificare **interazioni materialmente plausibili**, soprattutto quando due trattamenti toccano lo stesso meccanismo o la stessa risorsa condivisa.[^ms-interactions]

Questo evita due estremi: ignorare qualunque interference oppure pretendere di isolare ogni test dal resto del prodotto.

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

> **Quando A può modificare il mondo in cui vive B, il problema non è soltanto più rumore. È che il confronto può non rappresentare più la policy che vogliamo valutare.**

[^ms-interactions]: Microsoft Research, *A/B Interactions: A Call to Relax*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/a-b-interactions-a-call-to-relax/
