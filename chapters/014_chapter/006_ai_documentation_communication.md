## 14.5 AI per documentazione e comunicazione: migliorare la forma senza cambiare il livello di evidenza

L'AI è molto efficace nel trasformare un artefatto analitico in linguaggio per audience diverse.

Può aiutare con:

- documentazione SQL;
- metric card;
- data dictionary;
- note metodologiche;
- executive summary;
- FAQ;
- commenti al codice;
- traduzione tecnica-business;
- editing e concisione.

Il rischio specifico è diverso dalla generazione di codice.

Qui il sistema può prendere un'analisi corretta e **renderla più sbagliata mentre la rende più leggibile**.

## 14.5.1 Il Semantic Preservation Contract

Quando chiediamo una riscrittura definiamo ciò che può cambiare e ciò che deve restare invariato.

Esempio:

```text
May change:
- ordine delle frasi
- lessico
- lunghezza
- esempi esplicativi

Must preserve:
- numeri e unità
- popolazione
- periodo
- direction/magnitude
- uncertainty
- causal status
- limitations
- recommendation strength
```

Questo è il **Semantic Preservation Contract**.

### Caso simulato/composito — una riscrittura che inventa causalità

Testo originale:

> I clienti che completano il tutorial entro 24 ore mostrano retention D30 più alta di 9,4 punti percentuali. Il confronto è osservazionale e non identifica l'effetto causale del tutorial.

Riscrittura automatica:

> Completare il tutorial entro 24 ore aumenta la retention D30 di 9,4 punti percentuali.

La seconda frase è più corta.

Ha però cambiato il claim da **association** a **causal effect**.

Con la claim ladder della sezione precedente:

```text
originale: L2
riscrittura: L4
```

Una trasformazione editoriale non è autorizzata a fare questo salto.

## 14.5.2 Semantic diff

Per output importanti chiediamo non solo la nuova versione, ma un **semantic diff**.

```text
Numeri modificati?           NO
Periodo modificato?          NO
Population modificata?       NO
Uncertainty rimossa?         NO
Claim level aumentato?       NO
Limitations eliminate?       NO
Recommendation più forte?    NO
```

Il controllo può essere parzialmente automatizzato, ma il reviewer resta responsabile per claim materialmente importanti.

## 14.5.3 Metric card da codice: inference vs knowledge

Un sistema può leggere SQL e inferire:

- tabelle;
- filtri;
- join;
- colonne;
- aggregazioni.

Non può dedurre con certezza soltanto dal codice:

- perché una business rule esiste;
- chi la possiede;
- quale decisione supporta;
- se una eccezione è intenzionale;
- se la definizione è ancora approvata.

Per questo la documentazione generata dovrebbe distinguere:

```text
EXTRACTED FROM CODE
- date field: payment_captured_at
- excludes status = cancelled

REQUIRES OWNER CONFIRMATION
- business meaning of net revenue
- refund recognition policy
- intended consumer
- known exceptions
```

Questa distinzione evita che una deduzione plausibile diventi improvvisamente documentazione ufficiale.

## 14.5.4 Caso simulato/composito — forecast per il board

Forecast Q4:

```text
point estimate: €48,2M
80% interval: €44,9M–€51,7M
two large deals dominate upside
recent volatility above historical norm
```

Output aggressivo:

> Il Q4 chiuderà a €48,2M.

Output coerente con l'evidenza:

> La stima centrale è €48,2M; l'intervallo predittivo all'80% è €44,9–51,7M. Due deal enterprise spiegano gran parte dell'upside e la volatilità recente rende l'outlook meno stabile del normale.

L'AI è utile per comprimere il messaggio **se il contract impedisce di comprimere anche l'incertezza**.

## 14.5.5 Tradurre per audience senza creare tre verità

Stesso problema tecnico:

> SCD2 joinata usando current record invece della versione point-in-time.

Per Data Engineering:

> Il join non usa la surrogate key storica della fact e riclassifica retroattivamente gli attributi.

Per Product:

> Stiamo attribuendo agli utenti storici il piano che hanno oggi, non quello che avevano al momento dell'evento.

Per Executive:

> Una parte della crescita apparente deriva da riclassificazione storica, non da nuovo comportamento.

Sono traduzioni diverse.

Devono mantenere lo stesso **evidence core**.

## 14.5.6 Quote, fonti e numeri: no semantic autocomplete

Quando un documento contiene fonti esterne, il sistema non deve completare automaticamente:

- titolo di paper;
- autore;
- percentuali;
- benchmark;
- citazioni;
- URL.

Questi elementi devono provenire da una fonte recuperata/verificata oppure essere marcati come non verificati.

Un riferimento bibliografico fluente ma inventato è un failure del tipo **entity/factual confabulation**.

## 14.5.7 Approval boundary

Non tutti i testi hanno la stessa conseguenza.

```text
bozza interna          → review leggera
nota metodologica      → owner review
executive KPI summary  → evidence/claim review
comunicazione esterna  → processo di approvazione appropriato
```

La AI Analysis Control Sheet deve quindi documentare anche **chi può approvare la forma finale**.

### Campo della AI Analysis Control Sheet

```text
Communication artifact:
Audience:
Source analytical artifact:
Semantic Preservation Contract:
Claim level allowed:
Numbers/source verification:
Semantic diff result:
Reviewer:
External/public approval required?:
```

### Regola operativa

> **L'AI può tradurre un'analisi tra linguaggi e audience. Non deve tradurla tra livelli di certezza. Chiarezza, brevità e persuasività sono miglioramenti solo se il significato resta invariato.**
