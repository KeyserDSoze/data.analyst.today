## 8.6 DAG: disegnare le assunzioni prima di scrivere la regressione

Un **Directed Acyclic Graph (DAG)** è un modo compatto per rappresentare ipotesi causali tra variabili.

Per un Data Analyst il suo valore principale non è grafico.

È epistemico:

> **obbliga a dichiarare quali relazioni crediamo esistano prima che il modello le nasconda dentro un set di feature.**

### Caso simulato/composito — Campagna di reactivation

Una subscription app vuole stimare l'effetto di una campagna email sul ritorno degli utenti inattivi.

Variabili:

- engagement pre-campagna;
- eleggibilità alla campagna;
- email ricevuta;
- apertura;
- ritorno nell'app;
- churn successivo.

Un DAG plausibile:

```text
engagement_pre -> email
engagement_pre -> ritorno
email -> apertura -> ritorno -> churn
email -----------------> ritorno
```

Già il disegno rende visibili due cose.

**Engagement pre-treatment** può aprire un backdoor path tra email e ritorno.

**Apertura dell'email** è post-trattamento e può essere un mediatore.

Se vogliamo l'effetto totale dell'invio, controllare automaticamente per `open_email` cambia la domanda.

### Il DAG viene prima della feature selection

Nel predictive modeling possiamo lasciare che una procedura selezioni variabili utili alla previsione.

Nella causal inference la domanda è diversa:

> “Quali variabili devo condizionare — e quali devo evitare — per identificare l'effetto definito?”

Questo richiede conoscenza del processo.

### Tre ruoli da non confondere

**Confondente pre-trattamento**

```text
Z -> T
Z -> Y
```

Può richiedere adjustment.

**Mediatore**

```text
T -> M -> Y
```

Controllarlo può bloccare parte dell'effetto totale.

**Collider**

```text
T -> C <- U -> Y
```

Condizionare su `C` può aprire un'associazione non causale.

Queste tre strutture possono apparire tutte come “variabili correlate con treatment e outcome” in una tabella.

Il DAG ci impedisce di trattarle allo stesso modo.

### Caso simulato/composito — Training commerciale

Un'azienda vuole stimare l'effetto di un corso sul revenue trimestrale.

Possibile meccanismo:

```text
training -> chiamate -> demo -> pipeline -> revenue
     \-----------------------------------> revenue
```

Se la domanda è:

> “Qual è l'effetto totale del training?”

controllare per chiamate, demo e pipeline rischia di rimuovere proprio parte del meccanismo.

Se la domanda è invece:

> “Quanto dell'effetto passa attraverso la pipeline?”

entriamo in un problema di mediazione, con assunzioni ulteriori.

### Disegnare anche ciò che non misuriamo

Un errore comune è mettere nel DAG solo le colonne disponibili.

Dovremmo invece inserire anche cause plausibili non osservate:

```text
U_motivazione -> training uptake
U_motivazione -> revenue
```

Il fatto che `U_motivazione` non sia nel warehouse non la rende causalmente inesistente.

Anzi, il DAG può mostrare esplicitamente perché una strategia di adjustment osservazionale non basta.

### Il DAG non dimostra le frecce

Un grafo è un modello del mondo, non una fotografia certa del mondo.

Due analyst o domain expert possono proporre DAG differenti.

Questa è una caratteristica utile: il disaccordo diventa visibile e discutibile **prima** della stima.

Un buon processo è:

1. costruire una prima versione con analyst e stakeholder;
2. chiedere ai domain expert quali frecce mancano;
3. distinguere conoscenza forte da ipotesi debole;
4. verificare se DAG alternativi richiedono adjustment set diversi;
5. documentare la versione usata per la causal claim.

### DAG e tempo

Le frecce devono rispettare una storia temporale plausibile.

Se una variabile viene misurata dopo il trattamento, non può essere trattata come confondente preesistente senza una spiegazione molto specifica.

Quando il processo è dinamico, può essere utile espandere il DAG nel tempo:

```text
usage_t-1 -> treatment_t -> usage_t+1 -> outcome_t+2
     \-------------------------------> outcome_t+2
```

### Il DAG come parte del Causal Identification Brief

Non serve sempre inserire un diagramma elegante nel report finale.

Ma prima di una causal analysis seria dovremmo riuscire a rispondere:

```text
Quali cause comuni aprono backdoor path?
Quali variabili sono mediatori?
Dove possono esserci collider?
Quali cause importanti non sono osservate?
Quali variabili sono post-treatment?
Esistono spillover tra unità?
```

> **Il DAG non rende vere le assunzioni. Le rende visibili, e questo è già un enorme miglioramento rispetto a lasciarle implicite nel codice.**

### Riferimento

- Stanford University, STATS 361, *Causal Inference*: il corso include potential outcomes, observational studies, treatment heterogeneity, mediation, regression discontinuity, interference e graphical models: https://bulletin.stanford.edu/courses/2214431
