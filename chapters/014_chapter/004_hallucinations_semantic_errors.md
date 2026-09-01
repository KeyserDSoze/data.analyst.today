## 14.3 Confabulation, semantic error e narrative overreach: classificare l'errore prima di correggerlo

Una risposta palesemente rotta è spesso meno pericolosa di una risposta convincente che fallisce in un punto nascosto della catena.

Per verificare bene un output AI dobbiamo prima chiedere:

> **che tipo di errore potrebbe essere?**

“Hallucination” è una parola utile, ma troppo larga se raccoglie problemi molto diversi.

Nel lavoro analitico distinguiamo almeno sei famiglie.

## 14.3.1 Entity / factual confabulation

Il sistema introduce qualcosa che il contesto autorizzato non supporta.

Esempi:

- tabella inesistente;
- colonna inventata;
- funzione non disponibile;
- fonte bibliografica non verificata;
- numero attribuito a un report che non lo contiene.

Controllo:

```text
existence / source verification
```

## 14.3.2 Structural error

Gli oggetti esistono, ma la relazione assunta è sbagliata.

Esempio:

```text
orders.customer_id → customers.customer_id
```

quando i guest order usano un identity layer separato.

La query può girare e rimuovere silenziosamente una popolazione.

Controllo:

```text
grain + keys + join cardinality + population reconciliation
```

## 14.3.3 Semantic error

Il sistema usa un campo vero per rappresentare il concetto sbagliato.

Questo è spesso il failure mode più importante in analytics.

### Caso reale documentato — Copilot filtra la data sbagliata

Microsoft Learn mostra pubblicamente un esempio di Copilot in Power BI in cui l'utente chiede quale paese abbia prodotto il profitto più alto nel 2024/2023.[^ms-wrong-date]

Nel modello esistono dati per quegli anni usando la date table corretta.

Copilot però finisce per filtrare la colonna **Birthday** della tabella Customer invece della date table marcata nel modello.

Microsoft usa l'esempio per mostrare che, anche con prompt e modello, gli output possono essere inaccurati e che gli utenti devono ispezionare campi e filtri utilizzati.

Questo è un caso perfetto di semantic error:

```text
campo reale
+ query plausibile
+ concetto temporale sbagliato
```

La soluzione non è soltanto “promptare meglio”.

Può richiedere:

- schema più semplice per l'AI;
- campi ambigui esclusi;
- istruzioni;
- verified answers;
- training degli utenti alla verifica.

## 14.3.4 Computational error

La semantica è corretta, ma il calcolo è implementato male.

Esempi:

- percentuale calcolata con denominatore errato;
- media di medie non pesata;
- intervallo di confidenza sbagliato;
- filtro booleano invertito;
- bug nel codice generato.

Controllo:

```text
fixture + unit test + independent calculation
```

## 14.3.5 Narrative overreach

I numeri possono essere corretti, ma il testo dice più di ciò che dimostrano.

Esempio:

```text
revenue -12%
conversion -9%
traffic stabile
```

Output:

> Il calo è dovuto a una maggiore sensibilità al prezzo.

Non abbiamo mostrato nulla sul prezzo.

La frase ha trasformato:

```text
pattern osservato
→ meccanismo causale inventato
```

Controllo:

```text
claim classification
```

## 14.3.6 Action overreach

L'output può essere ragionevole, ma il sistema compie un'azione più forte di quella autorizzata.

Esempi:

- da “questa query sembra costosa” a cancellare una tabella intermedia;
- da “questa campagna sottoperforma” a sospenderla automaticamente;
- da “questi account sono high risk” a inviare incentivi senza budget/policy approval.

Questo failure mode nasce dalla **permission boundary**, non dalla qualità del linguaggio.

Controllo:

```text
action authorization + approval gate
```

## 14.3.7 Caso simulato/composito — +18,3% non è un treatment effect

Un retailer invia una campagna CRM a clienti VIP.

Dati:

```text
trattati:      conversion 14,2%
non trattati:  conversion 12,0%
```

L'AI calcola correttamente:

```text
(14,2 - 12,0) / 12,0 = +18,3%
```

Poi scrive:

> La campagna ha aumentato la conversion del 18,3%.

Il problema non è aritmetico.

I destinatari sono stati selezionati perché già più attivi e di valore più alto.

Il claim consentito è:

> La conversion osservata è 2,2 punti percentuali più alta nel gruppo trattato; il confronto osservazionale non identifica l'effetto incrementale della campagna.

Il Capitolo 8 ha fornito il Causal Identification Brief.

L'AI Analysis Control Sheet deve quindi poter dire:

```text
causal claim allowed: NO
```

## 14.3.8 Claim ladder

Per evitare narrative overreach classifichiamo il livello massimo di affermazione consentito.

**L0 — Extraction**

> Il valore è 4,6%.

**L1 — Description**

> È aumentato di 0,8 punti.

**L2 — Localization / association**

> Il delta è concentrato nei clienti con tenure <90 giorni.

**L3 — Prediction**

> Il modello stima maggiore probabilità futura per questo gruppo.

**L4 — Causal claim**

> L'intervento produce una differenza nel risultato.

**L5 — Recommendation**

> Dovremmo scegliere l'azione A date evidenza, costi e vincoli.

Ogni gradino richiede evidenza aggiuntiva.

Un sistema non dovrebbe salire di livello soltanto perché può produrre una frase più convincente.

## 14.3.9 Verifica per triangolazione

Per un KPI importante possiamo confrontare:

```text
AI-generated query
vs certified semantic metric
vs finance/operational reconciliation
vs historical order-of-magnitude
```

Se l'AI produce €13,8M e due percorsi indipendenti producono circa €12,4M, non chiediamo semplicemente:

> sei sicuro?

Ispezioniamo:

- population;
- date;
- joins;
- filters;
- duplicates;
- definition version.

La sicurezza linguistica del modello non è una misura di affidabilità statistica.

## 14.3.10 Risk-based verification

Il NIST Generative AI Profile propone un approccio di risk management proporzionato al contesto e include esplicitamente measurement ed evaluation nella gestione dei sistemi generativi.[^nist-profile-14]

Nel nostro workflow questo diventa:

| Output | Conseguenza | Gate minimo |
|---|---|---|
| spiegazione sintassi | bassa | review rapida |
| query esplorativa | moderata | fixture + sanity check |
| KPI management | alta | reconciliation + peer review |
| recommendation economica rilevante | alta | evidence review + assumptions |
| write/action automatico | molto alta | eval + permission + approval/rollback |

La categoria non dipende dal modello usato.

Dipende da ciò che l'output può cambiare nel mondo reale.

### Campo della AI Analysis Control Sheet

```text
Potential failure class:
Claim level requested:
Claim level supported:
Existence check:
Structural/semantic check:
Computational check:
Independent reconciliation:
Action authorization:
Unresolved uncertainty:
```

### Regola operativa

> **Non verificare un output AI chiedendoti soltanto “è giusto?”. Chiediti dove potrebbe essere sbagliato: oggetto, struttura, significato, calcolo, interpretazione o azione. Ogni classe richiede un controllo diverso.**

[^ms-wrong-date]: Microsoft Learn, *Use Copilot with semantic models in Power BI*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^nist-profile-14]: NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
