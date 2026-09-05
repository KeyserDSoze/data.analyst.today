## 14.5 AI per documentazione e comunicazione: migliorare la forma senza cambiare l'evidenza

L'AI è molto efficace nel trasformare un artefatto analitico in linguaggio per audience diverse: documentazione SQL, metric card, data dictionary, executive summary, FAQ, commenti al codice o traduzione tecnico-business. Il rischio specifico, però, è diverso dalla generazione di codice. Qui un sistema può prendere un'analisi corretta e **renderla più sbagliata mentre la rende più leggibile**.

### Semantic Preservation Contract

Quando chiediamo una riscrittura definiamo ciò che può cambiare e ciò che deve restare invariato:

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
- direction / magnitude
- uncertainty
- causal status
- limitations
- recommendation strength
```

Questo è il **Semantic Preservation Contract**. Serve perché la qualità editoriale non autorizza un salto nella claim ladder.

Prendiamo un testo corretto:

> I clienti che completano il tutorial entro 24 ore mostrano retention D30 più alta di 9,4 punti percentuali. Il confronto è osservazionale e non identifica l'effetto causale del tutorial.

Una riscrittura più breve può diventare:

> Completare il tutorial entro 24 ore aumenta la retention D30 di 9,4 punti percentuali.

La seconda frase è più fluida, ma trasforma un'associazione in un causal effect. L'AI non ha alterato il numero; ha alterato il **livello di evidenza**.

### Semantic diff

Per output importanti chiediamo anche un controllo esplicito:

```text
Numeri modificati?           NO
Periodo modificato?          NO
Population modificata?       NO
Uncertainty rimossa?         NO
Claim level aumentato?       NO
Limitations eliminate?       NO
Recommendation più forte?    NO
```

Il semantic diff può essere parzialmente automatizzato, ma la responsabilità resta sul reviewer quando il claim è materialmente importante.

### Documentare da codice: extracted vs inferred

Un sistema può leggere SQL e ricavare tabelle, filtri, join e aggregazioni. Non può dedurre con la stessa certezza perché una business rule esiste, chi la possiede o quale decisione supporta. Per questo una metric card generata dovrebbe distinguere:

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

Una deduzione plausibile non diventa automaticamente documentazione ufficiale.

### Comprimere senza cancellare l'incertezza

Consideriamo un forecast Q4:

```text
point estimate: €48,2M
80% interval: €44,9M–€51,7M
two large deals dominate upside
recent volatility above historical norm
```

Scrivere "Il Q4 chiuderà a €48,2M" rende il messaggio più semplice e l'evidenza peggiore. Una sintesi coerente mantiene invece stima centrale, intervallo, concentration risk e instabilità recente. L'AI può comprimere la forma **se il contract impedisce di comprimere anche l'incertezza**.

### Audience diverse, evidence core unico

Lo stesso problema tecnico può essere tradotto in modi diversi. Una SCD2 joinata sul current record può essere descritta a Data Engineering come errore sulla surrogate key storica, a Product come attribuzione agli utenti storici del piano che hanno oggi, e a un executive come riclassificazione retroattiva che altera una parte della crescita apparente. Sono tre superfici linguistiche dello stesso **evidence core**.

Lo stesso principio vale per fonti, quote e numeri. Titoli di paper, benchmark, URL o percentuali non devono essere completati per plausibilità: devono provenire da una fonte verificata oppure essere dichiarati come non verificati. Un riferimento bibliografico fluente ma inventato resta una confabulation fattuale.

### Approval boundary

Anche la review della comunicazione dipende dalla conseguenza. Una bozza interna può richiedere review leggera; una nota metodologica richiede owner review; un executive KPI summary richiede evidence/claim review; una comunicazione esterna segue il processo di approvazione appropriato. La AI Analysis Control Sheet registra quindi audience, artefatto sorgente, Semantic Preservation Contract, claim level consentito, verifica di numeri/fonti, semantic diff e approvatore.

> **L'AI può tradurre un'analisi tra linguaggi e audience. Non deve tradurla tra livelli di certezza. Chiarezza, brevità e persuasività sono miglioramenti solo se il significato resta invariato.**
