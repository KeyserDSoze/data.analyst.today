## 9.3 Sample Ratio Mismatch: prima del lift viene la fiducia nel confronto

Se un esperimento è configurato 50/50, ci aspettiamo che il numero di **unità randomizzate osservabili** sia compatibile con quella proporzione. Non serve ottenere esattamente `50,000% / 50,000%`: piccole differenze casuali sono normali. Il problema nasce quando il rapporto osservato è troppo improbabile rispetto all'assignment previsto. Quello è un **Sample Ratio Mismatch (SRM)**.

L'SRM non è un test sul prodotto. È un test sulla promessa del design: *il dataset che stiamo confrontando contiene davvero i due gruppi che pensavamo di avere?*

Microsoft Experimentation Platform tratta l'SRM come un gate di trustworthiness e documenta che analisi con SRM sono generalmente considerate non affidabili finché la causa non è compresa.[^ms-dq] L'ordine operativo è quindi:

```text
SRM PASS?
    ↓ sì
exposure / telemetry PASS?
    ↓ sì
effect analysis
```

### Caso reale documentato — Il carousel MSN

Microsoft Research racconta un test di MSN in cui la variante B aumentava da 12 a 16 le card di un image carousel. Ci si aspettava più engagement; il risultato iniziale mostrava invece un calo. Nello stesso momento il test falliva l'SRM check.

L'indagine trovò un meccanismo controintuitivo: la variante con più contenuto generava abbastanza engagement da confondere un algoritmo di bot detection. Alcuni degli utenti più coinvolti della variante B venivano quindi filtrati dall'analisi.[^ms-srm-case]

Dopo la correzione la conclusione si ribaltò. Il punto non è che l'SRM “aggiusta” il lift; è che ha segnalato che il campione osservato era stato modificato **in modo dipendente dal trattamento**. Gli utenti mancanti non erano missing at random: mancavano proprio perché B aveva cambiato il loro comportamento.

### Il rapporto va calcolato sull'unità giusta

Supponiamo:

```text
allocation configurata: 50/50
A osservati: 1.020.441
B osservati:   973.115
```

Su milioni di unità, anche una deviazione percentuale relativamente piccola può essere incompatibile con il piano. Un test chi-quadro sui conteggi è una soluzione standard, ma prima dobbiamo sapere **che cosa stiamo contando**.

Se randomizziamo `stable_user_id`, contare sessioni non è un assignment check equivalente: la variante potrebbe modificare proprio il numero di sessioni per utente. Conviene distinguere almeno l'**SRM di assignment**, calcolato sulle randomization units assegnate, dall'**SRM di exposure**, che può aiutare a diagnosticare dove il trattamento non viene ricevuto simmetricamente. I rapporti su eventi downstream influenzabili da B non sono sostituti del primo.

### Dove si può rompere la catena

L'SRM è utile perché comprime in un sintomo problemi che possono nascere in punti diversi. L'hashing può essere errato, l'ID instabile o l'eligibility diversa tra rami. Un redirect, un crash o una feature flag possono cambiare l'exposure. Bot filter, join lossy, lag di pipeline o dedup possono perdere eventi selettivamente. Un filtro analitico post-treatment può escludere proprio chi reagisce alla feature.

Per questo l'SRM non è la diagnosi. Dice soltanto:

> **il dataset osservato non sembra essere quello che il design prometteva.**

La diagnostica deve localizzare la rottura lungo assignment → execution/exposure → telemetry/processing → analysis.

Un modo pratico è segmentare il rapporto per piattaforma, app version, country, browser, logged-in/anonymous, giorno/ora o exposure path. Se il totale fallisce ma desktop e iOS passano mentre Android mostra un forte mismatch, abbiamo una direzione di indagine. Queste slice servono a fare debugging, non a inventare una storia di business.

### Salvare il test o ripartire?

La risposta dipende dalla root cause. Se esiste un periodo iniziale chiaramente identificato, circoscritto e non legato all'outcome, può essere possibile definire una finestra valida secondo regole motivate. Se invece il trattamento modifica la probabilità di apparire nel dataset, eliminare ex post “i casi problematici” può aggiungere altro selection bias.

Spesso la scelta più pulita è correggere il problema, riavviare il test e documentare l'incidente. È meno elegante di recuperare ogni run, ma protegge il valore del confronto.

### SRM runbook

```text
Configured allocation:
Randomization unit:
Observed unit counts:
SRM p-value / alert:
Quando è iniziato?
Quali segmenti lo concentrano?
Assignment integrity:
Exposure symmetry:
Telemetry completeness:
Post-treatment filters:
Treatment-dependent missingness plausibile?
Root cause:
Salvage / restart decision:
```

> **Se l'SRM fallisce, la domanda “A o B?” viene sospesa. Prima dobbiamo stabilire se A e B esistono ancora, nei dati, come i due gruppi che avevamo progettato.**

[^ms-dq]: Microsoft Research, *Data Quality: Fundamental Building Blocks for Trustworthy A/B testing Analysis*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis
[^ms-srm-case]: Microsoft Research, *Diagnosing Sample Ratio Mismatch in A/B Testing*: https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/
