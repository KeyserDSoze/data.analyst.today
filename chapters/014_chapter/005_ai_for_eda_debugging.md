## 14.4 AI per EDA e debugging: aumentare il search space senza aumentare l'autoinganno

L'AI è molto utile nell'Exploratory Data Analysis perché rende economico generare:

- segmentazioni;
- query diagnostiche;
- possibili anomaly slice;
- controlli sui missing;
- visualizzazioni;
- spiegazioni alternative;
- ipotesi su failure di pipeline.

Questa è una capacità potente.

Ma introduce un nuovo rischio:

> **se possiamo esplorare cento volte più velocemente, possiamo anche trovare cento volte più pattern plausibili che non reggeranno.**

Il problema del workflow non è quindi soltanto trovare più idee.

È governare **search, falsification e promotion dell'evidenza**.

## 14.4.1 L'AI come hypothesis generator

Un uso ad alto valore è chiedere:

> Quali decomposizioni distinguerebbero queste ipotesi?

invece di:

> Qual è la causa?

### Caso simulato/composito — conversion Android

Una travel app vede conversion da 4,7% a 3,9% in due giorni.

Il sistema propone una **hypothesis map**:

| Ipotesi | Pattern atteso | Test discriminante |
|---|---|---|
| bug app | drop per versione | app version × funnel |
| PSP outage | drop per payment rail | error code × PSP |
| tracking issue | orders stabili, session/conversion cambiano | reconciliation backend |
| traffic mix | drop per channel/geo | within-segment comparison |
| inventory | drop concentrato su route/hotel type | availability signal |

Il valore dell'AI non è aver “indovinato il bug”.

È aver trasformato una domanda vaga in **test falsificabili**.

I dati mostrano poi:

- iOS stabile;
- drop Android;
- forte concentrazione su Android 14;
- break tra `payment_started` e `payment_success`;
- `WALLET_TOKEN_EXPIRED` in aumento.

Engineering conferma successivamente un problema nel wallet SDK.

## 14.4.2 Diagnostic search log

Quando l'AI può generare molte esplorazioni, registriamo almeno:

```text
hypothesis
why considered
query/test
result
status: supported | weakened | unresolved
next cheapest discriminating test
```

Questo evita che il processo diventi:

```text
provo 80 slice
→ una sembra interessante
→ la racconto come se fosse la domanda iniziale
```

Il log rende visibile anche il **researcher degree of freedom** introdotto dalla velocità.

## 14.4.3 Search budget

Possiamo stabilire un search budget proporzionato alla fase.

Esempio:

```text
first pass:
- 5 hypothesis families
- 2 test per family
- stop se emerge data-quality failure

second pass:
- approfondire top 2
- cercare almeno 1 falsification test per ipotesi
```

Non è una regola statistica universale.

È un modo per impedire che l'esplorazione illimitata venga scambiata per conferma.

## 14.4.4 Adversarial questioning

Una volta trovata un'interpretazione favorita, usiamo l'AI anche per attaccarla.

Prompt operativo:

> La working hypothesis è che la release Android abbia ridotto conversion. Proponi cinque meccanismi alternativi che produrrebbero lo stesso pattern e per ciascuno il test più economico che potrebbe distinguerlo.

Questo è utile contro:

- confirmation bias umano;
- narrative lock-in del modello;
- correlazioni proxy.

L'AI non deve essere usata soltanto come **generator di spiegazioni**, ma come **generator di obiezioni verificabili**.

## 14.4.5 Debugging come ricerca del primo boundary rotto

Per una pipeline che perde righe, invece di chiedere genericamente:

> Perché mancano dati?

forniamo:

- DAG;
- row count per layer;
- freshness;
- schema changes;
- deploy recenti;
- test falliti.

Poi chiediamo:

> Identifica il primo boundary in cui un invariant cambia e proponi il test minimo per confermarlo.

### Caso simulato/composito — 480.000 order line mancanti

```text
Raw:    2,80M
Silver: 2,80M
Gold:   2,32M
```

Il primo boundary rotto è Silver → Gold.

Un nuovo `INNER JOIN` al product master elimina 480.000 righe associate a SKU nuovi non ancora caricati nella dimensione.

L'AI accelera la diagnosi perché ragiona sulla **localizzazione della perdita**, non perché “conosce la causa”.

## 14.4.6 EDA non è confirmation

Se l'AI scopre dopo decine di slice che un segmento ha un uplift apparente, quel risultato deve restare etichettato come esplorativo finché non supera un gate appropriato.

A seconda della domanda può servire:

- holdout temporale;
- campione indipendente;
- test pre-specificato;
- correzione per molteplicità;
- esperimento;
- Causal Identification Brief.

Il Capitolo 5 ha trattato inferenza e multiple testing. Qui aggiungiamo un fatto operativo:

> **AI riduce il costo di generare confronti, quindi aumenta il bisogno di registrare quali confronti abbiamo generato.**

## 14.4.7 Data-health gate prima della narrativa

Prima che un agente o copilota interpreti un'anomalia, dovrebbe verificare almeno:

```text
freshness
completeness
schema status
grain/key invariants
volume anomalies
known incidents
reconciliation headline KPI
```

Se fallisce un controllo critico, l'output corretto può essere:

> Investigazione business sospesa: il denominatore sessioni è incompleto del 18% dopo il deploy del consent layer.

Questo è più utile di una lista creativa di possibili cause business.

### Campo della AI Analysis Control Sheet

```text
EDA objective:
Hypothesis families:
Search budget:
Diagnostic search log:
Data-health gate:
Current leading hypothesis:
Alternative explanations tested:
Falsification test:
Promotion rule from exploratory to decision evidence:
```

### Regola operativa

> **Usa l'AI per ampliare e strutturare lo spazio delle ipotesi. Poi imponi un processo che renda costoso promuovere un pattern interessante a conclusione: servono falsificazione, log della ricerca e un gate di evidenza.**
