## 9.3 Sample Ratio Mismatch: il gate prima del lift

Se un esperimento è configurato 50/50, ci aspettiamo che il numero di **unità randomizzate osservabili** sia compatibile con quella proporzione.

Piccole differenze casuali sono normali.

Una deviazione troppo improbabile è un **Sample Ratio Mismatch (SRM)**.

Il punto non è ottenere esattamente `50,000% / 50,000%`.

Il punto è verificare se il processo che ha costruito i gruppi osservati è coerente con l'assignment configurato.

### Perché l'SRM viene prima dell'effetto

Microsoft Experimentation Platform considera l'SRM un controllo fondamentale di trustworthy experimentation. La documentazione Microsoft afferma che analisi con SRM sono generalmente non affidabili e non dovrebbero guidare decisioni finché il problema non è compreso.[^ms-dq]

L'ordine operativo diventa:

```text
SRM PASS?
    ↓ sì
telemetry / exposure PASS?
    ↓ sì
effect analysis
```

Non:

```text
B +4% !!!
    ↓
forse controlliamo SRM
```

## Caso reale documentato — Il carousel MSN che sembrava peggiorare engagement

Microsoft Research racconta un A/B test di **MSN** sul numero di card di un image carousel. La variante B aumentava le card da 12 a 16 e ci si aspettava maggiore engagement.

Il risultato iniziale mostrava invece un calo.

Contemporaneamente, il test falliva l'SRM check.

L'indagine rivelò un meccanismo sorprendente: la variante B era in realtà abbastanza coinvolgente da generare comportamento che confondeva un algoritmo di bot detection. Alcuni degli utenti più engaged della variante B venivano quindi filtrati dall'analisi.[^ms-srm-case]

Dopo la correzione, la conclusione si ribaltò: la variante con più contenuto aumentava l'engagement.

Questo caso è didatticamente potente perché mostra che:

> **gli utenti mancanti non sono necessariamente un campione casuale degli utenti. Possono mancare proprio perché il trattamento li ha influenzati.**

### Il sintomo: rapporto osservato incompatibile con il piano

Supponiamo:

```text
allocation configurata: 50/50
A osservati: 1.020.441
B osservati:   973.115
```

La domanda non è se la differenza “sembra grande”.

Dipende dalla numerosità.

Su 100 utenti, 47/53 può essere plausibile.

Su milioni di utenti, una deviazione percentuale molto piccola può essere statisticamente incompatibile con l'assignment previsto.

Un test chi-quadro sui conteggi è una soluzione standard.

### Ma quale conteggio?

L'SRM deve essere calcolato sull'unità coerente con il design.

Se randomizziamo `stable_user_id`, contare sessioni può produrre un rapporto diverso anche senza errore di assignment perché una variante può cambiare il numero di sessioni per utente.

Quindi dobbiamo distinguere:

- **SRM di assignment:** randomization units assegnate;
- **SRM di exposure:** unità che hanno realmente raggiunto l'esperienza;
- rapporti su eventi downstream che **possono essere influenzati dal trattamento** e non sono equivalenti a un assignment check.

### Dove può nascere l'SRM

Microsoft Research organizza le cause lungo la catena sperimentale. Operativamente possiamo usare questa tassonomia.

#### Assignment

- hashing errato;
- bucket configuration sbagliata;
- ID instabile;
- ramp non simmetrico;
- eligibility diversa tra rami.

#### Execution / exposure

- redirect differenziali;
- crash prima del rendering;
- client version non supportata;
- feature flag inconsistente;
- trattamento che modifica la probabilità di entrare nel campione analitico.

#### Telemetry / processing

- eventi persi;
- join lossy;
- bot filter differenziale;
- pipeline lag differente;
- dedup diversa tra varianti.

#### Analysis

- filtro post-treatment;
- denominatore definito su un evento influenzato dal trattamento;
- segmentazione che esclude unità in modo differenziale;
- data maturity non uniforme.

#### Interference

In sistemi complessi anche interazioni tra esperimenti o unità possono generare pattern anomali da investigare.

### SRM è un allarme, non la diagnosi

Un SRM significativo non ci dice **perché** il test è rotto.

Ci dice:

> “Il dataset che stai confrontando non sembra essere quello che il design prometteva.”

La responsabilità dell'analista è localizzare la rottura.

### Segmentare l'SRM

Una tecnica diagnostica utile è verificare il rapporto per:

- piattaforma;
- app version;
- country;
- browser;
- giorno/ora;
- logged-in vs anonymous;
- nuovo vs returning user;
- exposure path.

Esempio:

```text
Totale: SRM
Desktop: PASS
Android: forte SRM
iOS: PASS
```

Ora l'indagine ha una direzione.

Attenzione però a non fare decine di segmentazioni e dichiarare causa al primo pattern casuale: il segmentation step serve a **debuggare il sistema**, non a produrre un risultato di business.

### Quando un test può essere salvato?

Dipende dalla causa.

Se il problema riguarda un periodo iniziale chiaramente identificato e indipendente dall'outcome, può essere possibile predefinire una finestra valida e riavviare l'analisi.

Se invece il trattamento stesso ha modificato chi entra nel dataset, rimuovere ex post i casi problematici può creare ulteriore selection bias.

Spesso la scelta più pulita è:

1. correggere il problema;
2. riavviare il test;
3. documentare l'incidente.

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

> **Se l'SRM fallisce, la domanda “A o B?” viene sospesa. La prima domanda diventa “possiamo ancora fidarci del confronto?”.**

[^ms-dq]: Microsoft Research, *Data Quality: Fundamental Building Blocks for Trustworthy A/B testing Analysis*: https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis
[^ms-srm-case]: Microsoft Research, *Diagnosing Sample Ratio Mismatch in A/B Testing*: https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/
