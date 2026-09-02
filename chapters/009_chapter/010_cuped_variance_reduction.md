## 9.9 CUPED e variance reduction: più precisione senza inventare più traffico

Una volta scelti estimand, randomization unit e metrica, possiamo chiederci:

> **possiamo stimare lo stesso effetto con meno rumore usando informazione che esisteva prima del trattamento?**

Una delle tecniche più note è **CUPED — Controlled-experiment Using Pre-Experiment Data**.

L'intuizione è semplice: se il comportamento pre-esperimento predice bene la metrica durante il test, possiamo rimuovere parte della variabilità prevedibile che non è causata dal trattamento.

### Non serve a correggere una randomizzazione rotta

CUPED non ripara:

- SRM;
- contamination;
- treatment-dependent missingness;
- metriche semanticamente sbagliate;
- leakage post-treatment;
- un campione che non rappresenta la decisione.

Microsoft Research descrive variance reduction come un modo per aumentare precisione/power di un esperimento **senza aumentare la probabilità di una decisione sbagliata**, quando lo stimatore è costruito correttamente.[^ms-vr]

Quindi l'ordine rimane:

```text
experiment health
    ↓
valid design
    ↓
variance reduction
```

non il contrario.

### Caso simulato/composito — Watch time molto persistente

Una piattaforma video testa una nuova home.

La metrica è minuti visti per utente.

Nel periodo precedente al test:

- alcuni utenti guardavano meno di 30 minuti/settimana;
- altri oltre 1.000.

Questa eterogeneità persiste anche durante il test e rende rumoroso il confronto.

Se `watch_time_pre` è fortemente correlato con `watch_time_during`, può essere usato come covariata per spiegare parte della differenza individuale già presente prima dell'esperimento.

Il risultato utile non è:

> “correggiamo perché il trattamento aveva casualmente utenti più pesanti.”

È:

> **“usiamo una caratteristica pre-treatment predittiva per ridurre la varianza dello stimatore dell'effetto.”**

La randomizzazione resta la fonte della comparabilità causale.

### Perché deve essere pre-treatment

Supponiamo di usare come covariata:

`watch_time_primi_3_giorni_del_test`

La variante può già avere influenzato quel valore.

Aggiustare per una variabile post-treatment rischia di modificare l'estimand o introdurre bias.

Una covariata CUPED tipica deve essere definita su una finestra precedente all'assegnazione/esposizione pertinente.

### Quando aiuta molto

Variance reduction tende a essere più utile quando:

- la metrica ha forte persistenza individuale;
- esiste storico per molte randomization units;
- la covariata pre-period è misurata bene;
- la metrica è rumorosa;
- il traffico è costoso o il randomization level è aggregato.

### Quando aiuta poco

Può avere beneficio limitato quando:

- molti utenti sono nuovi;
- il pre-period è poco correlato con l'outcome;
- l'identità non è stabile tra pre-period e experiment period;
- il comportamento è dominato da eventi nuovi;
- la metrica è già poco variabile.

La tecnica non deve diventare un default rituale.

### Caso reale documentato — Microsoft Experimentation Platform

Microsoft ExP usa CUPED come tecnica di variance reduction e descrive il beneficio come un **effective traffic multiplier**: in alcuni contesti la riduzione della varianza produce una precisione simile a quella che si otterrebbe con più traffico, ma il guadagno varia molto tra metriche e prodotti.[^ms-vr]

La stessa Microsoft include variance reduction tra le leve usate per rendere praticabili anche test con traffico più modesto, per esempio in cambi infrastrutturali interni.[^ms-infra]

Questo non significa che gli utenti virtualmente “aumentino”.

Significa che stiamo sfruttando meglio informazione già disponibile.

### CUPED e nuovi utenti

Se una grande quota della popolazione non ha storico, dobbiamo dichiarare:

- chi dispone della covariata;
- come trattiamo i missing;
- se la disponibilità di storico cambia per variante;
- se il risultato aggiustato conserva la popolazione decisionale desiderata.

Non dobbiamo restringere silenziosamente il test ai returning users soltanto per rendere CUPED più efficace.

### Variance reduction card

```text
Outcome metric:
Pre-treatment covariate:
Pre-period:
Correlation with outcome:
Coverage della covariata:
Missingness policy:
Expected variance reduction:
Randomization unit coerente?
Covariata sicuramente pre-treatment?
Raw estimate:
Adjusted estimate:
Precision gain:
```

È utile mostrare raw e adjusted result quando questo migliora auditabilità e comprensione.

> **Variance reduction non crea più evidenza dal nulla. Riduce il rumore sfruttando informazione pre-treatment che sappiamo già essere predittiva dell'outcome.**

[^ms-vr]: Microsoft Research, *Deep Dive Into Variance Reduction*: https://www.microsoft.com/en-us/research/articles/deep-dive-into-variance-reduction/
[^ms-infra]: Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp
