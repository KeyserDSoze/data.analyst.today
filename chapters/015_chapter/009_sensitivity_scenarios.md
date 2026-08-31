## 15.8 Sensitivity analysis e scenario planning: quanto è fragile la decisione?
Una raccomandazione può sembrare solida finché non tocchiamo una delle sue assunzioni.

Per questo una buona analisi non dovrebbe limitarsi a produrre un punto stimato. Dovrebbe chiedersi:

> **“Quanto deve cambiare il mondo perché la nostra decisione non sia più quella giusta?”**

Questa è la logica della sensitivity analysis.

## Dalla stima centrale agli switching values

La guida Green Book del governo britannico raccomanda di testare le assunzioni chiave e di calcolare gli **switching values**: i valori ai quali un'opzione smette di essere preferibile o di rappresentare value for money.

È un'idea estremamente utile anche nell'analytics aziendale.

Supponiamo che un progetto sembri conveniente se:

- uplift atteso: +6%;
- costo implementazione: €400.000;
- margine incrementale annuo: €650.000.

La domanda non è solo se il business case è positivo.

La domanda è:

> “A quale uplift il progetto smette di creare valore?”

Se basta scendere dal 6% al 5,4% perché il progetto diventi negativo, la decisione è fragile.

Se invece resta positiva fino al 2%, è molto più robusta.

## One-way sensitivity

Variamo una sola assunzione alla volta.

Esempio:

| Assunzione | Base | Scenario basso | Scenario alto |
|---|---:|---:|---:|
| uplift conversione | 6% | 2% | 9% |
| costo progetto | €400k | €600k | €300k |
| margine medio | €48 | €35 | €55 |

Questo metodo aiuta a capire quali variabili governano davvero la decisione.

## Scenario planning

La sensitivity analysis cambia singole assunzioni.

Lo scenario planning combina più cambiamenti coerenti.

Possiamo costruire:

- **scenario downside**;
- **scenario base**;
- **scenario upside**.

Non servono scenari fantasiosi. Devono essere plausibili e internamente coerenti.

## Caso realistico: un nuovo hub logistico

Aster Logistics valuta un nuovo hub per servire il Centro Italia.

Nel business case base:

- investimento: €4,8M;
- risparmio annuo trasporti: €1,45M;
- riduzione delivery time: 0,7 giorni;
- crescita volumi attesa: +8% annuo.

Il progetto sembra chiaramente interessante.

L'analista però costruisce tre scenari.

### Downside

- crescita volumi: +1%;
- carburante stabile;
- risparmio trasporti: €0,85M;
- costo progetto: €5,5M.

### Base

- crescita: +8%;
- risparmio: €1,45M;
- costo: €4,8M.

### Upside

- crescita: +12%;
- carburante più caro;
- risparmio: €1,9M;
- costo: €4,6M.

La decisione resta positiva nel base e nell'upside, ma nel downside il payback si allunga drasticamente.

A quel punto la domanda diventa:

> “Possiamo strutturare il progetto in fasi per preservare optionality?”

Questo è più utile di fingere che il forecast centrale sia la verità.

## Real options e reversibilità

La Green Book 2026 richiama anche la logica delle **real options**: quando l'incertezza è alta e la decisione è costosa da invertire, può essere utile progettare flessibilità e rinviare parte dell'impegno fino a quando emergerà nuova informazione.

In pratica:

- pilot prima del rollout;
- contratto modulare invece di pluriennale;
- capex in fasi;
- rollout regionale;
- soglie di go/no-go.

La domanda cambia da:

> “Qual è l'opzione perfetta?”

a:

> **“Quale opzione ci mantiene forti anche se il futuro è diverso dalla nostra stima centrale?”**

## Ottimismo e forecast error

Un altro punto importante della Green Book è l'**optimism bias**: costi e tempi tendono spesso a essere sottostimati, mentre benefici e velocità di realizzazione vengono sovrastimati.

Un team maturo usa dati storici per confrontare:

**forecast iniziale vs risultato reale**

su progetti simili.

Questo permette di correggere sistematicamente l'ottimismo invece di trattarlo come un problema caratteriale.

## Una regola operativa

Prima di raccomandare una decisione importante, chiediamoci:

1. quali sono le 3–5 assunzioni più importanti?
2. quale deve cambiare meno per invertire la scelta?
3. quali assunzioni sono sotto il nostro controllo?
4. quali possiamo osservare prima di impegnarci completamente?
5. possiamo costruire una decisione più reversibile?

**Una decisione robusta non è quella che funziona solo nello scenario centrale. È quella che continua ad avere senso in un intervallo plausibile di futuri.**

Fonti di riferimento:

- UK HM Treasury, *The Green Book 2026*: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
- Green Book supplementary guidance on optimism bias: https://www.gov.uk/government/publications/green-book-supplementary-guidance-optimism-bias
