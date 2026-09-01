## 9.7 MDE e feasibility: quale effetto vale il costo di un esperimento?

Il Capitolo 5 ha già spiegato la relazione tra sample size, effect size, alpha e power.

Qui usiamo quei concetti per una domanda più concreta:

> **Il nostro sistema ha abbastanza traffico per distinguere un effetto che sarebbe abbastanza importante da cambiare la decisione?**

Questa è una verifica di **experiment feasibility**.

### Minimum Detectable Effect non significa “effetto minimo che esiste”

L'MDE è una soglia di sensibilità del design.

Se pianifichiamo un test per rilevare `+0,20 pp`, un effetto reale di `+0,08 pp` può comunque esistere. Il test potrebbe semplicemente non essere abbastanza informativo per distinguerlo dal rumore con la precisione desiderata.

Per questo l'MDE non deve essere scelto perché:

- produce una durata comoda;
- è il default del tool;
- “2% relativo suona ragionevole”.

Deve partire da **materialità e decisione**.

### Caso simulato/composito — QuickPay e la soglia economica

Baseline:

- conversion: 3,80%;
- utenti eleggibili/mese: 4,2 milioni;
- contribution margin per ordine: 17,40 €.

Il PM propone MDE relativo `+2%`, cioè circa `+0,076 pp` assoluti.

Su 4,2 milioni di utenti:

```text
4.200.000 × 0,00076 ≈ 3.192 ordini incrementali/mese
```

Contribution margin lordo indicativo:

```text
3.192 × 17,40 € ≈ 55.500 €/mese
```

Ma il redesign:

- richiede manutenzione su quattro codebase;
- modifica due integration path di pagamento;
- aumenta costi di fraud review;
- ha costo opportunità per altri progetti.

Se un effetto di `+0,076 pp` non giustifica implementazione e rischio, non è la soglia decisionale corretta.

Il team può definire:

> “Ship solo se il beneficio plausibile è almeno +0,15 pp senza violare i guardrail.”

Ora MDE, traffic plan e business threshold parlano la stessa lingua.

### Tre soglie che non vanno confuse

**Minimum effect of interest (MEI)**

Il più piccolo effetto che cambierebbe la decisione business.

**MDE del design**

La dimensione di effetto che il test è progettato a rilevare con certe proprietà statistiche.

**Observed effect**

La stima prodotta dai dati.

Idealmente il design dovrebbe essere abbastanza sensibile intorno al **minimum effect of interest**, non attorno a una soglia scelta per comodità.

### Traffic feasibility

Supponiamo che per l'MDE desiderato servano 900.000 utenti per variante.

Ma soltanto 80.000 utenti/mese sono realmente eleggibili.

La durata teorica supera undici mesi per arm, senza considerare maturity e stagionalità.

La risposta professionale non è:

> “Facciamolo comunque e vediamo.”

Le alternative sono:

- cambiare la domanda;
- usare un outcome più sensibile ma ancora decision-relevant;
- aumentare l'eligible population se semanticamente valido;
- usare variance reduction;
- testare un trattamento più forte;
- accettare che l'esperimento non sia praticabile;
- usare un design diverso.

### Guardrail rari possono determinare la durata

Un test può avere moltissimo power sulla conversione e pochissima informazione su:

- frode rara;
- incidenti;
- churn a 90 giorni;
- severe crash;
- chargeback.

Se uno di questi outcome può bloccare lo ship, il traffic plan deve dichiarare **quanto bene saremo in grado di escludere danni materialmente importanti**.

Non basta dimensionare soltanto la primary metric.

### Clustered experiments

Se randomizziamo 80 negozi anziché 2 milioni di utenti, il volume di transazioni non recupera automaticamente la sensibilità persa.

Il numero e la variabilità dei cluster diventano centrali.

Per questo il feasibility check deve usare l'unità di randomizzazione reale e la struttura di dipendenza del design.

### Exposure rate

Supponiamo:

```text
1.000.000 utenti randomizzati
solo 35% raggiunge la feature
```

Se l'estimand è intent-to-treat, l'effetto medio sugli assegnati sarà diluito dall'esposizione parziale.

Se l'effetto business rilevante è molto piccolo, il test può richiedere molto più traffico di quanto suggerirebbe un calcolo basato soltanto sugli utenti che vedono la feature.

Questa realtà deve essere incorporata **prima** del lancio.

### Sample size non risolve la durata minima

Anche quando il sample requirement viene raggiunto rapidamente, il 9.5 ci ha ricordato che potremmo dover attendere:

- cicli temporali;
- outcome maturity;
- learning/novelty;
- exposure ripetuta.

Quindi:

```text
experiment end = max(
    sample requirement,
    minimum calendar duration,
    outcome maturity requirement
)
```

come principio operativo, non come formula statistica universale.

### Feasibility card

```text
Baseline metric:
Minimum effect of business interest:
MDE planned:
Alpha / desired power:
Randomization unit:
Eligible units/day:
Expected exposure rate:
Variance / baseline rate:
Cluster design effect if any:
Rare guardrail feasibility:
Expected time to sample requirement:
Minimum calendar duration:
Outcome maturity:
Is the experiment decision-useful at this sensitivity?
```

> **Un esperimento sottodimensionato non spreca soltanto traffico. Può consumare settimane per produrre un risultato che, qualunque sia il segno, non distingue le decisioni che ci interessano.**
