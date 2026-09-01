## 9.10 Multiple metriche e varianti: separare scorecard, decisione ed esplorazione

Un esperimento reale può produrre decine o centinaia di metriche.

Questo è utile per capire il sistema.

È anche un modo molto efficiente per trovare qualcosa che sembra interessante per caso.

Il Capitolo 5 ha già introdotto multiple testing. Qui il problema è soprattutto di **governance della scorecard**.

### Tre livelli della scorecard

**Decision metrics**

Primary/OEC e guardrail che entrano formalmente in `SHIP / NO-SHIP`.

**Diagnostic metrics**

Aiutano a capire il meccanismo e localizzare regressioni.

**Exploratory metrics / slices**

Servono a generare ipotesi successive.

Il fatto che tutte siano visualizzate nella stessa pagina non significa che abbiano lo stesso peso inferenziale.

### Caso simulato/composito — La vittoria trovata dopo 48 confronti

Un e-commerce testa A, B, C e D e osserva:

- conversion;
- revenue/user;
- add-to-cart;
- AOV;
- return rate;
- dwell time;
- review click;
- image click.

Poi incrocia:

- desktop/mobile;
- nuovo/returning.

La variante C mostra `+6,8%` sui click alle recensioni dei nuovi utenti mobile con `p = 0,031`.

Ma:

- non era primary;
- il segmento non era pre-specificato;
- la primary revenue/user è piatta;
- decine di confronti sono stati ispezionati.

La conclusione corretta è:

> **“C genera un pattern esplorativo interessante sui review click mobile-new; il test non fornisce però evidenza confermativa sufficiente per ship sulla decision metric.”**

Quell'osservazione può diventare l'ipotesi di un nuovo esperimento.

### Multiple variants aumentano le decisioni possibili

Con quattro arm non esiste soltanto:

```text
B vs A
C vs A
D vs A
```

Il team potrebbe essere tentato di chiedere anche:

```text
B vs C
B vs D
C vs D
```

e poi segmentare ogni contrasto.

Prima del test dobbiamo specificare quali confronti sono **decision-relevant**.

Se l'obiettivo è scegliere la migliore variante rispetto all'attuale prodotto, i confronti treatment-vs-control possono essere primari e i pairwise treatment comparisons secondari.

### Gatekeeping

Una strategia organizzativa semplice può essere:

```text
Gate 1: primary/OEC mostra beneficio materialmente utile?
    ↓ sì
Gate 2: guardrail entro limiti?
    ↓ sì
Gate 3: diagnostics coerenti / nessun red flag?
    ↓ sì
Ship candidate
```

Questo riduce la tentazione di dichiarare una vittoria perché “qualcosa da qualche parte è verde”.

### Multiple testing correction non sostituisce metric relevance

Possiamo usare procedure come:

- Bonferroni;
- Holm;
- Benjamini-Hochberg / FDR;
- gerarchie/gatekeeping.

Ma una scorecard con 500 metriche irrilevanti resta difficile da interpretare anche se il false-discovery control è formalmente corretto.

Nel 2026 Microsoft ExP ha descritto proprio questa sfida: un singolo esperimento può generare **centinaia o migliaia di metriche** e l'aumento di metriche, soprattutto in sistemi agentici, rende centrali sia il controllo delle false discovery sia la **rilevanza delle metriche rispetto al trattamento**.[^ms-tea]

È un punto particolarmente importante nell'era AI.

Un agente può generare 300 segmentazioni in pochi secondi.

La capacità computazionale di cercare pattern cresce più velocemente della capacità statistica di considerarli tutti confermativi.

### Correlated metrics

Molte metriche non sono indipendenti:

- sessions e page views;
- orders e revenue;
- time in app e events/user;
- latency P95 e P99.

Quindi “17 metriche significative” non equivale a 17 prove indipendenti.

Microsoft ExP ha mostrato su scorecard reali che metodi che ignorano in modo inappropriato la correlazione tra metriche possono produrre false-positive behavior molto diverso da quello nominale.[^ms-tea]

Per un Data Analyst il messaggio è:

> non contare le celle verdi come voti indipendenti.

### Segmenti pre-specificati vs discovery

Un segmento può guidare una decisione se era definito prima per una ragione sostantiva:

- nuovo vs returning per novelty;
- market con regolamentazione diversa;
- platform con implementation path differente.

Un segmento scoperto dopo aver esplorato 80 combinazioni è un risultato esplorativo fino a replica.

Questo non lo rende inutile.

Lo colloca nel posto giusto del ciclo:

**scoperta → nuova ipotesi → nuovo test**.

### Scorecard contract

```text
Primary/OEC family:
Guardrail family:
Diagnostic metrics:
Exploratory metrics:
Pre-specified segments:
Variants:
Primary contrasts:
Secondary contrasts:
Multiplicity procedure:
Gatekeeping rule:
Which metrics can change ship decision?
Which findings require replication?
```

> **Una scorecard ampia serve a vedere il sistema. Una decisione affidabile richiede invece una gerarchia che impedisca di trasformare ogni movimento visibile in una nuova definizione di successo.**

[^ms-tea]: Microsoft Research, *Treatment Effect Assessment at Scale: Accounting for Correlated Metrics and Metric Relevance in Modern Experimentation*, 15 luglio 2026: https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/
