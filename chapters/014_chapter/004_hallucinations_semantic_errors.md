# 14.3 Hallucination e semantic errors: quando una risposta convincente è più pericolosa di un errore

Un errore esplicito è spesso facile da gestire. Una risposta fluente, plausibile e sbagliata è molto più insidiosa.

Nel lavoro analitico possiamo distinguere almeno quattro famiglie di errore generate o amplificate dall'AI.

## 1. Hallucination fattuale

Il modello inventa qualcosa che non esiste.

Esempi:

- una colonna `customer_lifetime_value` che non è presente;
- una tabella `fact_revenue_monthly` che il warehouse non contiene;
- una funzione SQL non supportata dal motore usato;
- una fonte, un paper o una definizione non realmente verificata.

## 2. Hallucination strutturale

Il modello immagina uno schema o una relazione errata.

Per esempio assume:

```text
orders.customer_id -> customers.customer_id
```

quando in realtà gli ordini guest usano `identity_id` e molti `customer_id` sono null.

La query può comunque girare e perdere silenziosamente parte della popolazione.

## 3. Semantic error

L'AI usa dati veri ma interpreta male il significato.

È il caso più importante per un Data Analyst.

### Caso pubblico documentato: Copilot e la data sbagliata

Microsoft Learn mostra un esempio in cui Copilot per Power BI riceve una domanda sui profitti per anno ma applica il filtro alla colonna di compleanno del cliente invece che alla date table corretta.

Il modello non ha necessariamente "inventato" il dato. Ha selezionato un campo semanticamente sbagliato all'interno di un modello reale.

Questo esempio è prezioso perché dimostra che la presenza di un semantic model non rende il natural-language analytics infallibile. La documentazione Microsoft raccomanda esplicitamente di ispezionare campi e filtri usati da Copilot e di addestrare gli utenti a valutare criticamente le risposte.

## 4. Hallucination narrativa

I numeri possono essere corretti, ma l'AI costruisce una spiegazione non supportata.

Esempio:

- revenue -12%;
- conversion -9%;
- traffico stabile.

L'AI scrive:

> "Il calo è dovuto probabilmente a una maggiore sensibilità al prezzo dei clienti."

Non c'è alcuna evidenza sul prezzo.

La frase è plausibile, ma è un'ipotesi presentata come spiegazione.

## Un caso realistico: "la campagna ha causato +18%"

Una retail company lancia una campagna CRM sui clienti VIP.

Dati osservati:

- trattati: conversion 14,2%;
- non trattati: conversion 12,0%.

Un assistente AI riassume:

> "La campagna ha aumentato la conversion del 18,3%."

Il calcolo relativo è corretto:

`(14,2 - 12,0) / 12,0 = 18,3%`

Ma la conclusione causale non lo è. I VIP sono selezionati perché più attivi e di valore più alto.

Qui l'errore non è matematico. È epistemologico.

Il modello ha confuso:

**differenza osservata → effetto causale**

Una buona verifica dovrebbe riportare:

> "La conversion è 2,2 punti percentuali più alta nei trattati. Con i dati osservazionali disponibili non possiamo attribuire causalmente la differenza alla campagna."

## Il protocollo di verifica in cinque domande

Per ogni output importante prodotto dall'AI chiediamo:

### 1. Esiste davvero?

Tabelle, colonne, metriche, fonti e funzioni citate sono reali?

### 2. È la cosa giusta?

La colonna scelta rappresenta davvero il concetto business richiesto?

### 3. Il calcolo è riproducibile?

Possiamo ottenere lo stesso numero con una query o un metodo indipendente?

### 4. L'interpretazione segue dai dati?

La conclusione distingue correlazione, previsione e causalità?

### 5. Quanto è sensibile alle assunzioni?

Cambia molto usando altra finestra temporale, denominatore o definizione?

## Un confidence score non è una verifica

Un LLM può esprimere sicurezza anche quando sbaglia. La sicurezza linguistica non è una misura statistica di affidabilità.

Frasi come:

- "sono certo";
- "con alta probabilità";
- "il driver principale è";

non devono essere trattate come evidenza se non derivano da un metodo verificabile.

## Verifica tramite triangolazione

Quando la decisione è importante, confrontiamo più percorsi.

Esempio revenue mensile:

1. query SQL sul warehouse;
2. misura certificata nel semantic layer;
3. reconciliation con finance export;
4. confronto con numero del mese precedente.

Se tre fonti danno €12,4M e l'AI produce €13,8M, il problema non si risolve chiedendo al modello di essere "più preciso". Si ispeziona la logica.

## Risk-based verification

Non tutti gli output richiedono lo stesso livello di controllo.

| Output AI | Rischio | Controllo consigliato |
|---|---:|---|
| spiegazione di una funzione SQL | basso | lettura rapida |
| bozza di query esplorativa | medio | sanity check |
| KPI per management | alto | reconciliation + peer review |
| pricing / credito / compliance | molto alto | review formale + test + approvazione |

Il NIST AI RMF per Generative AI insiste proprio su un approccio basato sul rischio: valutazione, misurazione e gestione devono essere proporzionate all'impatto potenziale dell'uso dell'AI.

> **Più una risposta AI può cambiare una decisione reale, meno possiamo permetterci di valutarla in base a quanto suona convincente.**

### Fonti

- Microsoft Learn, *Use Copilot with semantic models in Power BI*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
