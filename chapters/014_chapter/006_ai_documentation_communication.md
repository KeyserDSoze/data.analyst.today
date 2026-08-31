# 14.5 AI per documentazione e comunicazione: accelerare la traduzione senza alterare il significato

Una parte enorme del lavoro analitico non consiste nel calcolare numeri, ma nel renderli comprensibili, verificabili e riusabili.

L'AI può aiutare molto in:

- documentazione di query e metriche;
- data dictionary;
- descrizioni di semantic model;
- commenti nel codice;
- executive summary;
- note metodologiche;
- traduzione tra linguaggio tecnico e business;
- preparazione di FAQ;
- revisione di presentazioni.

Ma anche qui esiste un rischio specifico: migliorando la forma, l'AI può involontariamente modificare la sostanza.

## Caso realistico: una frase più elegante, ma causalmente sbagliata

Testo originale dell'analista:

> "I clienti che completano il tutorial entro 24 ore mostrano retention D30 più alta di 9,4 punti percentuali. Il confronto è osservazionale e non dimostra che il tutorial causi l'aumento."

Versione riscritta automaticamente:

> "Completare il tutorial entro 24 ore aumenta la retention D30 di 9,4 punti percentuali."

La seconda frase è più corta e più sicura. Ed è metodologicamente peggiore.

L'AI ha eliminato proprio la cautela più importante.

## Separare contenuto e stile

Una buona strategia è dire esplicitamente:

> "Migliora chiarezza e concisione senza cambiare il livello di certezza, la distinzione tra correlazione e causalità, i valori numerici o le limitazioni metodologiche."

Per output sensibili, possiamo anche chiedere un diff concettuale:

> "Dopo la riscrittura, elenca ogni modifica che potrebbe aver cambiato il significato analitico."

## Documentare metriche con una struttura standard

L'AI può aiutare a trasformare una formula dispersa in una scheda metrica coerente.

Esempio:

### Metric card — Net Revenue

- **Business definition:** ricavi da ordini pagati meno refund riconosciuti;
- **Grain:** giorno × mercato × canale;
- **Date field:** `payment_captured_at`;
- **Currency:** EUR a FX rate mensile finance;
- **Excluded:** test orders, fraud confirmed, full cancellations;
- **Owner:** Finance Analytics;
- **Freshness:** D+1 entro 07:00 CET;
- **Known limitations:** refund tardivi possono retroagire sul mese precedente.

Un assistente AI può produrre una prima bozza da SQL, semantic model e documentazione esistente, ma il metric owner deve validarla.

## Il valore del linguaggio su più livelli

Lo stesso risultato può essere spiegato diversamente a seconda dell'audience.

### Per un data engineer

> "Il delta nasce da una SCD2 joinata con current flag invece che point-in-time key."

### Per un product manager

> "Stavamo attribuendo agli utenti storici il piano che hanno oggi, non quello che avevano quando hanno compiuto l'azione."

### Per un executive

> "Circa un terzo della crescita apparente dipende da una riclassificazione storica dei clienti, non da comportamento nuovo."

L'AI è molto utile in questa traduzione, a condizione che il nucleo analitico venga preservato.

## Caso realistico: board summary di un forecast

Forecast revenue Q4:

- point estimate: €48,2M;
- 80% interval: €44,9M–€51,7M;
- forte dipendenza da due enterprise deal;
- regime recente più volatile dello storico.

Un summary troppo aggressivo potrebbe dire:

> "Il Q4 chiuderà a €48,2M."

Una comunicazione migliore è:

> "La stima centrale è €48,2M, ma l'intervallo all'80% è €44,9–51,7M. Due deal enterprise spiegano gran parte dell'upside e la volatilità recente rende il forecast meno stabile del normale."

L'AI può aiutare a comprimere il messaggio senza eliminare l'incertezza.

## Generare documentazione dal codice: utile ma non sufficiente

Da una query SQL l'AI può inferire:

- tabelle usate;
- filtri;
- join;
- aggregazioni;
- colonne derivate.

Non può però sapere con certezza:

- perché quella logica esiste;
- chi la possiede;
- quale decisione supporta;
- quali eccezioni business non sono visibili nel codice.

Per questo la documentazione generata deve distinguere:

**ciò che il codice mostra** da **ciò che il business intende**.

> **L'AI può rendere una spiegazione più chiara. Solo l'analista può garantire che resti vera.**
