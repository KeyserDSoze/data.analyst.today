## 9.9 CUPED e variance reduction: ridurre rumore senza confondere precisione e validità

Dopo aver stabilito che randomizzazione, exposure, telemetria e metriche sono sane possiamo chiedere se lo stesso effetto può essere stimato con meno rumore usando informazione **pre-treatment**. È qui che entra **CUPED — Controlled-experiment Using Pre-Experiment Data**.

L'intuizione è semplice: se il comportamento precedente all'esperimento predice bene la metrica durante il test, una parte della variabilità osservata non riguarda il trattamento. Possiamo usare quella covariata per ottenere uno stimatore dell'effetto con errore standard più piccolo.

Microsoft Research descrive CUPED come variance reduction dello **stimatore del treatment effect**, non come modifica della varianza del dato grezzo, e come una leva che aumenta la power senza aumentare la probabilità di una decisione sbagliata quando l'estimatore è costruito correttamente.[^ms-vr]

L'ordine è quindi:

```text
experiment health
    ↓
valid design
    ↓
variance reduction
```

CUPED non ripara SRM, contamination, treatment-dependent missingness, metriche semanticamente sbagliate o un estimand incoerente.

### Caso simulato/composito — Watch time persistente

Una piattaforma video testa una nuova home usando minuti visti per utente. Nel periodo precedente alcuni utenti guardavano meno di 30 minuti a settimana e altri oltre 1.000; questa eterogeneità persiste durante il test.

Se `watch_time_pre` è fortemente correlato con `watch_time_during`, la covariata pre-period può spiegare parte delle differenze individuali che esistevano comunque. La randomizzazione resta la fonte della comparabilità causale; CUPED usa informazione precedente per rendere più precisa la stima di quella differenza.

È una distinzione importante. Non stiamo “correggendo perché B aveva utenti peggiori”. Stiamo sfruttando una variabile pre-treatment predittiva per ridurre la varianza dello stimatore.

### Perché il pre-period è un confine causale

Usare `watch_time_primi_3_giorni_del_test` come covariata può essere pericoloso perché B potrebbe aver già modificato quel valore. Aggiustare per una variabile post-treatment può cambiare l'estimand o introdurre bias. La finestra CUPED deve quindi essere anteriore al momento in cui il trattamento può influenzare il comportamento rilevante.

Il beneficio tende a essere maggiore quando la metrica ha forte persistenza individuale, lo storico copre molte randomization units e la covariata è misurata bene. Aiuta poco quando molti utenti sono nuovi, l'identità non è stabile tra pre-period e experiment period o il comportamento è dominato da eventi completamente nuovi.

### Effective traffic multiplier non significa utenti virtuali

Microsoft ExP descrive il guadagno di CUPED anche come **effective traffic multiplier**: ridurre la varianza può produrre una precisione simile a quella che avremmo ottenuto con più traffico.[^ms-vr] Non significa che il campione sia diventato più grande o più rappresentativo. Significa che abbiamo usato meglio informazione già disponibile.

Questo punto è cruciale se soltanto una parte degli utenti possiede storico. Non dobbiamo restringere silenziosamente il test ai returning users per rendere CUPED più efficace. Dobbiamo dichiarare coverage della covariata, policy sui missing e popolazione a cui appartiene il risultato aggiustato.

Mostrare raw e adjusted estimate può essere utile per auditabilità: se la variance reduction funziona come previsto, il centro della stima dovrebbe restare compatibile mentre la precisione migliora, non trasformare magicamente un test rotto in un risultato affidabile.

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

> **Variance reduction compra precisione, non validità. Prima dobbiamo sapere che il confronto è credibile; solo allora ha senso cercare di stimarlo con meno rumore.**

[^ms-vr]: Microsoft Research, *Deep Dive Into Variance Reduction*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/deep-dive-into-variance-reduction/
