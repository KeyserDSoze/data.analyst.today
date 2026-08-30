## 6.11 Churn prediction: prevedere chi se ne andrà non significa sapere perché

Una delle richieste più comuni nei team subscription è: “Possiamo costruire un modello che predice il churn?”

La risposta tecnica è spesso sì. La risposta analitica più importante è un'altra: **cosa faremo con quella previsione?**

Un modello predittivo può imparare che alcuni pattern precedono il churn. Ma questo non implica che intervenire su quei pattern riduca il churn.

### Caso: Northstar CRM

Northstar CRM serve circa 18.000 aziende. Il team Data Science costruisce un modello che assegna ogni settimana una probabilità di churn a ciascun account.

Le variabili più importanti risultano:

- numero di login negli ultimi 14 giorni;
- utilizzo delle automazioni;
- numero di ticket al supporto;
- riduzione degli utenti attivi nel workspace;
- mancato utilizzo dell'integrazione contabile.

Il modello ha buone performance di ranking: gli account nel decile di rischio più alto churnano molto più spesso della media.

Il Customer Success team propone quindi una strategia semplice: contattare tutti gli account con pochi login e incentivare l'uso del prodotto.

Il problema è che “pochi login” può essere un **segnale** di un problema, non la sua causa.

### Il caso del cliente che non entra più perché ha già deciso di uscire

Un account può ridurre i login perché:

- il prodotto non funziona bene;
- l'azienda ha cambiato processo;
- ha acquistato un concorrente;
- il champion interno ha lasciato l'azienda;
- il team è stato ridimensionato;
- ha già deciso di non rinnovare.

In alcuni casi aumentare artificialmente i login non cambia nulla.

L'analista distingue quindi tre domande:

1. **Prediction:** chi ha maggiore probabilità di churnare?
2. **Diagnosis:** quali pattern e condizioni sono associati al churn?
3. **Causal intervention:** quali azioni riducono realmente il churn?

Sono tre problemi diversi.

### Un modello utile può essere non causale

Questo non rende inutile il churn model. Può essere estremamente utile per prioritizzare il lavoro del Customer Success.

Se un team può contattare solo 500 clienti al mese, una buona previsione può concentrare l'attenzione sugli account a rischio maggiore.

Ma la successiva decisione — quale intervento usare — richiede evidenza ulteriore.

### Caso: il supporto che “causa” churn

Nel modello Northstar, il numero di ticket support aperti è fortemente associato al churn. Una lettura superficiale potrebbe suggerire di ridurre i contatti con il supporto.

Naturalmente sarebbe assurdo.

È più plausibile che i clienti con problemi aprano ticket e che gli stessi problemi aumentino il rischio di churn.

Il supporto è in parte un **proxy della difficoltà vissuta**, non necessariamente il driver causale.

### Dal risk score al treatment effect

Un passo più maturo consiste nel chiedere non solo “chi è a rischio?”, ma:

> Su quali clienti un certo intervento ha maggiore probabilità di funzionare?

Questo porta verso concetti come uplift modeling, heterogeneous treatment effects e sperimentazione mirata, che incontreremo più avanti.

Per il momento basta fissare una regola:

**Un modello che predice bene il churn non è automaticamente un modello che spiega il churn.**

E un fattore predittivo non è automaticamente una leva di business.
