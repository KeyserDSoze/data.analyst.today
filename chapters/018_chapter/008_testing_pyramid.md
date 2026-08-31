# 18.7 Una testing pyramid per analytics

Un errore analitico può nascere a livelli diversi.

Possiamo avere:

- una colonna mancante;
- una chiave duplicata;
- un join many-to-many inatteso;
- una metrica semanticamente diversa;
- una pipeline aggiornata ma incompleta;
- un numero tecnicamente corretto ma incompatibile con il processo reale.

Per questo non esiste un singolo test che “garantisce la qualità”.

Serve una piramide di controlli.

## Livello 1 — Test strutturali

Sono economici e frequenti.

Controllano:

- schema;
- tipo;
- `NOT NULL`;
- unicità;
- foreign key;
- valori ammessi.

Sono necessari, ma non sufficienti.

Una tabella può rispettare perfettamente lo schema e contenere una revenue duplicata del 40%.

## Livello 2 — Test statistici e di distribuzione

Controllano se il comportamento dei dati è plausibile:

- volume giornaliero;
- quota di missing;
- distribuzione;
- range;
- cardinalità;
- cambi improvvisi rispetto alla storia.

Non sempre una deviazione è un errore. Una campagna può davvero raddoppiare il traffico.

Quindi questi test spesso producono alert, non fallimenti automatici.

## Livello 3 — Test di riconciliazione

Qui confrontiamo sistemi o viste indipendenti.

Esempi:

- revenue del warehouse vs ledger finanziario;
- ordini completati vs pagamenti catturati;
- utenti attivi vs eventi di sessione;
- totale fatture vs totale righe aggregate.

La riconciliazione è potente perché verifica una proprietà di business, non soltanto una proprietà tecnica.

## Livello 4 — Test semantici

Sono più difficili da automatizzare.

Domande tipiche:

- il denominatore della conversion è ancora quello corretto?
- il churn include account sospesi?
- la revenue è gross o net?
- la data di riferimento è order date o recognition date?
- l'utente “attivo” corrisponde ancora alla definizione adottata dal business?

Molti bug più pericolosi vivono qui.

## Livello 5 — Test decisionali

Il livello più alto verifica se l'asset continua a supportare la decisione per cui è stato creato.

Una dashboard può essere tecnicamente perfetta e non essere più utile perché il processo operativo è cambiato.

## Caso realistico: tutti i test verdi, decisione sbagliata

Un retailer monitora il cancellation rate.

Tutti i test passano:

- schema corretto;
- nessun missing;
- volumi coerenti;
- percentuale nel range storico.

Ma durante un cambiamento operativo, gli ordini annullati automaticamente per frode vengono riclassificati come `closed_by_system` invece di `cancelled`.

Il cancellation rate appare migliorato.

La customer experience non è migliorata affatto.

Un test semantico o una riconciliazione con gli esiti finali ordine avrebbe intercettato il problema.

## Principio operativo

Più saliamo nella piramide:

- i test sono meno numerosi;
- costano di più;
- richiedono maggiore conoscenza di business;
- intercettano errori più difficili da vedere.

> **La data quality non è una batteria di test. È una strategia di evidenze ridondanti.**
