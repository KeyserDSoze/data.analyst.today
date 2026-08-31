# 18.10 Governance per AI e agenti

Quando un sistema analitico incorpora AI o agenti, la superficie di rischio cambia.

Un processo tradizionale esegue una sequenza relativamente definita.

Un agente può invece:

- scegliere strumenti;
- generare query;
- interrogare fonti diverse;
- sintetizzare evidenze;
- proporre azioni;
- iterare autonomamente.

Questo aumenta la capacità, ma rende ancora più importante definire confini.

## Governance non significa bloccare l'autonomia

L'obiettivo non è richiedere approvazione umana per ogni operazione.

È graduare l'autonomia in base al rischio.

Un agente che prepara una bozza di descrizione KPI può avere libertà elevata.

Un agente che modifica un semantic model certificato deve avere controlli molto più forti.

Un agente che può inviare ordini, modificare prezzi o agire su clienti richiede soglie ancora più alte.

## Le dimensioni da governare

### Accesso

Quali dati può leggere?

Quali sistemi può modificare?

### Autorità

Può soltanto suggerire o può anche eseguire?

### Evidenza

Deve conservare query, fonti, trasformazioni e risultati intermedi?

### Verifica

Quali controlli deterministici devono essere superati?

### Escalation

Quando deve fermarsi e chiedere una decisione umana?

### Audit

Possiamo ricostruire cosa ha fatto e perché?

### Versioning

Quale modello, prompt, toolset e policy erano in uso?

## Caso realistico: l'agente che ottimizza troppo bene

Un retailer costruisce un agente per ottimizzare automaticamente la spesa promozionale.

L'obiettivo assegnato è massimizzare il contribution margin settimanale.

L'agente riduce drasticamente gli incentivi su clienti con bassa probabilità di conversione.

Nel breve periodo il margine migliora.

Dopo alcune settimane emerge però che il sistema ha quasi eliminato l'acquisizione in segmenti nuovi e poco conosciuti, perché il modello aveva maggiore incertezza proprio su quei clienti.

L'agente ha ottimizzato correttamente il criterio assegnato.

Il criterio era incompleto.

Mancavano guardrail su:

- acquisizione nuovi clienti;
- esplorazione;
- copertura segmenti;
- rischio di feedback loop.

## Human oversight come design, non come frase

Scrivere “human in the loop” in una policy non basta.

Bisogna specificare:

- chi è l'owner;
- quali eventi richiedono review;
- quali soglie fermano l'agente;
- quali azioni sono reversibili;
- quanto tempo ha il reviewer;
- quali evidenze deve vedere.

Questo riprende il principio del Capitolo 0:

> **Possiamo delegare l'esecuzione. Non possiamo delegare la responsabilità.**

## Risk-based autonomy

Una matrice semplice può usare due dimensioni:

| Impatto | Reversibilità | Autonomia consigliata |
|---|---|---|
| basso | alta | elevata |
| medio | alta | moderata |
| alto | media | limitata |
| alto | bassa | approvazione umana obbligatoria |

Non è una legge universale, ma costringe il team a esplicitare il rischio.

## Governance degli eval

Un agente non dovrebbe essere valutato soltanto su esempi ideali.

Gli eval dovrebbero includere:

- casi normali;
- edge case;
- dati incompleti;
- conflitti tra fonti;
- istruzioni ambigue;
- tentativi di azione fuori scope;
- situazioni in cui la risposta corretta è fermarsi.

Il sistema più maturo non è quello che agisce sempre.

È quello che sa quando **non** agire.

## Fonti

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
