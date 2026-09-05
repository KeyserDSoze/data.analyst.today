## 9.10 Multiple metriche e varianti: una scorecard ampia non deve diventare una definizione mobile di successo

Un esperimento reale può produrre decine o centinaia di metriche. Questa ricchezza è utile per vedere il sistema, localizzare regressioni e generare nuove ipotesi. È anche un modo estremamente efficiente per trovare qualche movimento interessante per puro caso.

Il problema non è avere molte metriche. È trattarle come se tutte avessero la stessa autorità sulla decisione.

Una scorecard matura distingue **decision metrics** — primary/OEC e guardrail che entrano formalmente nello `SHIP / NO-SHIP` — da **diagnostic metrics**, che aiutano a spiegare il meccanismo, e da **exploratory metrics/slices**, che generano ipotesi successive. Possono stare nella stessa pagina, ma non appartengono allo stesso livello inferenziale.

### La vittoria trovata dopo 48 confronti

Un e-commerce testa A, B, C e D su conversion, revenue/user, add-to-cart, AOV, return rate, dwell time, review click e image click, poi separa desktop/mobile e nuovo/returning. La variante C mostra `+6,8%` sui review click dei nuovi utenti mobile con `p = 0,031`.

Il pattern può essere reale. Ma non era primary, il segmento non era pre-specificato, revenue/user è piatta e decine di confronti sono stati ispezionati. La conclusione corretta è quindi esplorativa:

> **C genera un pattern interessante sui review click mobile-new; questo run non fornisce evidenza confermativa sufficiente per cambiare la decisione definita dalla primary.**

Quell'osservazione può diventare l'ipotesi del test successivo. Non deve riscrivere il contract di quello appena concluso.

### Più varianti significano più confronti possibili

Con quattro arm il team può guardare B vs A, C vs A e D vs A, poi B vs C, B vs D, C vs D e infine segmentare ciascuna coppia. Prima del lancio conviene dichiarare quali contrasti sono decision-relevant. Se l'obiettivo è scegliere quale proposta migliora il prodotto rispetto all'attuale, i treatment-vs-control possono essere primari e i confronti tra treatment secondari.

Una semplice gerarchia può essere:

```text
Gate 1: primary/OEC supera la soglia materialmente utile?
    ↓ sì
Gate 2: guardrail entro limiti?
    ↓ sì
Gate 3: health e diagnostics senza red flag?
    ↓ sì
Ship candidate
```

Questo non elimina la statistica della molteplicità, ma impedisce che “qualcosa da qualche parte è verde” diventi una strategia decisionale.

### Correzione statistica e rilevanza sono problemi distinti

Bonferroni, Holm, Benjamini-Hochberg/FDR o procedure gerarchiche possono controllare diversi aspetti della molteplicità. Nessuna di queste rende utile una scorecard composta da centinaia di metriche lontane dal trattamento.

Nel luglio 2026 Microsoft ExP ha descritto esattamente questa sfida: un singolo esperimento può generare **centinaia o migliaia di metriche**, spesso correlate, e la piattaforma deve distinguere movimento reale da false discovery tenendo conto anche della **rilevanza delle metriche rispetto al trattamento**.[^ms-tea]

Il punto è particolarmente importante con sistemi agentici. Un agente può generare centinaia di slice e confronti in pochi secondi. La capacità computazionale di cercare pattern cresce molto più velocemente della quantità di evidenza indipendente contenuta nel test.

Metriche come sessions e page views, orders e revenue, latency P95 e P99 sono inoltre correlate. Diciassette celle verdi non equivalgono a diciassette prove indipendenti. La scorecard deve essere letta come sistema, non come votazione.

### Segmentazione: conferma o discovery

Segmenti definiti prima per una ragione sostantiva — per esempio new vs returning per novelty, market con regolamentazione diversa o platform con implementation path differente — possono avere un ruolo confermativo dichiarato. Una combinazione scoperta dopo aver esplorato ottanta slice resta esplorativa fino a replica.

Questo non svaluta la scoperta. La colloca nel ciclo corretto:

**test → pattern esplorativo → ipotesi nuova → esperimento nuovo**.

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

> **Una scorecard ampia serve a vedere il sistema. Una decisione affidabile richiede invece una gerarchia che impedisca alla definizione di successo di espandersi ogni volta che compare una cella favorevole.**

[^ms-tea]: Microsoft Research, *Treatment Effect Assessment at Scale: Accounting for Correlated Metrics and Metric Relevance in Modern Experimentation*, 15 luglio 2026: https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/
