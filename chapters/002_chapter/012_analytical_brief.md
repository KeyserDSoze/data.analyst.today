## 2.11 L'Analytical Brief: il contratto prima dell'analisi

Prima di aprire un notebook o una dashboard, un analista dovrebbe essere in grado di riassumere il lavoro da svolgere in una pagina.

Questo documento può essere chiamato **Analytical Brief**.

Non è burocrazia. È un modo per evitare settimane di lavoro su una domanda non condivisa.

Un Analytical Brief efficace contiene almeno:

### 1. Decisione

Quale decisione dovrà essere presa?

Esempio:

> Decidere se intervenire sul nuovo onboarding e, in caso affermativo, quale fase deve essere prioritaria.

### 2. Problema di business

Quale fenomeno ha motivato la richiesta?

> La retention a 30 giorni dei clienti acquisiti negli ultimi sei mesi è diminuita.

### 3. Domanda analitica primaria

> Quali segmenti e quali fasi del percorso cliente spiegano maggiormente il calo della retention a 30 giorni rispetto alle coorti precedenti?

### 4. Domande secondarie

- Il calo riguarda tutti i canali?
- È concentrato in specifici piani?
- È cambiato il comportamento nei primi sette giorni?
- Ci sono differenze tra versioni dell'onboarding?

### 5. Metriche

Definire esplicitamente:

- metrica principale;
- formula;
- denominatore;
- finestra temporale;
- eventuali guardrail metrics.

### 6. Popolazione

Chi viene incluso e chi escluso?

### 7. Periodo di osservazione

Quale intervallo temporale analizziamo e perché?

### 8. Baseline

Con cosa confrontiamo il risultato?

### 9. Segmentazioni previste

Quali dimensioni sono teoricamente rilevanti?

### 10. Ipotesi iniziali

Quali spiegazioni plausibili vogliamo testare?

### 11. Dati necessari

Quali fonti, tabelle e campi servono?

### 12. Limiti noti

Quali informazioni mancano? Quali bias sono prevedibili?

### 13. Output

L'output finale è una dashboard? Un memo? Un notebook? Una raccomandazione? Un modello?

### 14. Criterio di successo

Come capiremo che l'analisi è stata utile?

Non basta dire "dashboard consegnata".

Un criterio migliore potrebbe essere:

> Il team prodotto dispone di evidenza sufficiente per decidere se modificare l'onboarding e quale fase prioritizzare.

### Un template riutilizzabile

```text
Decisione:

Problema di business:

Domanda analitica primaria:

Domande secondarie:

Metriche:

Popolazione:

Periodo:

Baseline:

Segmentazioni:

Ipotesi:

Dati necessari:

Limiti:

Output:

Criterio di successo:
```

La funzione dell'Analytical Brief è creare allineamento prima dell'esecuzione.

In un ambiente in cui AI, SQL generator e strumenti self-service possono produrre output quasi immediatamente, questo documento diventa ancora più prezioso: rallenta di pochi minuti l'inizio del lavoro e può evitare giorni di analisi sbagliata.
