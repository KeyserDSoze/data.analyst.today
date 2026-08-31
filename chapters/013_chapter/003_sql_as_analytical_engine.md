# 13.2 SQL: portare il calcolo vicino al dato

SQL è spesso il primo strumento che permette a un Data Analyst di smettere di dipendere da estrazioni manuali e iniziare a lavorare direttamente sulla base informativa dell'organizzazione.

Ma anche qui il punto non è la sintassi.

Il valore di SQL nasce dal fatto che consente di esprimere in modo relativamente dichiarativo una domanda sui dati, lasciando al database o al motore analitico il compito di eseguire il lavoro.

## 13.2.1 Quando SQL è la scelta naturale

SQL è particolarmente adatto quando:

- i dati sono già in database, warehouse o lakehouse interrogabile;
- bisogna filtrare, unire, aggregare e trasformare grandi volumi;
- la logica deve essere ripetibile;
- più persone devono usare la stessa definizione;
- il risultato è tabellare;
- vogliamo evitare di spostare inutilmente milioni di righe su un laptop.

## 13.2.2 Caso realistico: 180 milioni di righe scaricate per calcolare quattro numeri

Un analyst deve calcolare:

- clienti attivi mensili;
- ordini per cliente;
- revenue netta;
- tasso di riacquisto.

Il dataset eventi contiene 180 milioni di righe.

Una soluzione ingenua è esportare tutto in Python e poi aggregare localmente.

Ma il database possiede già indici, partizioni, motore di join, parallelismo e capacità di aggregazione.

Una query SQL che riduce il dato a poche decine di migliaia di righe aggregate prima del trasferimento può essere più veloce, meno costosa e più sicura.

Il principio è semplice:

> **sposta il calcolo verso il dato quando il dato è grande e il calcolo è naturalmente relazionale.**

## 13.2.3 SQL non è sempre sufficiente

SQL diventa meno naturale quando il problema richiede:

- simulazioni iterative complesse;
- algoritmi statistici avanzati;
- ottimizzazione numerica;
- visualizzazioni esplorative sofisticate;
- modelli di machine learning;
- elaborazione di oggetti non tabellari;
- package scientifici specializzati.

In questi casi SQL può preparare il dataset, mentre Python o R eseguono la parte analitica.

## 13.2.4 Il pattern 80/20: SQL per restringere, Python/R per approfondire

Immaginiamo un'analisi churn su 12 milioni di clienti.

In SQL possiamo:

1. definire la popolazione;
2. costruire le feature storiche;
3. aggregare utilizzo e billing;
4. applicare finestre temporali coerenti;
5. estrarre solo il dataset modellistico necessario.

Poi in Python o R possiamo:

- stimare modelli;
- confrontare metriche;
- calibrare probabilità;
- produrre grafici diagnostici;
- testare soglie decisionali.

La scelta non è SQL *contro* Python. È una divisione del lavoro.

## 13.2.5 Il rischio dell'AI-generated SQL

Con i copiloti moderni, una richiesta come:

> «calcola il fatturato medio per cliente negli ultimi 12 mesi»

può produrre in pochi secondi una query plausibile.

Ma il modello non conosce necessariamente:

- se `orders` è a livello ordine o riga ordine;
- se i resi sono in una tabella separata;
- se il cliente guest deve essere escluso;
- se il fatturato è lordo o netto;
- se la data corretta è `order_date`, `invoice_date` o `payment_date`.

Quindi la nuova competenza non è scrivere ogni query a memoria. È saperla revisionare semanticamente.

## 13.2.6 Caso realistico: query più veloce, decisione peggiore

Un team migra una query da Python a SQL e riduce il tempo di elaborazione da 18 minuti a 40 secondi.

Sembra un grande successo.

Poi scopre che la query SQL usa un `INNER JOIN` con la tabella loyalty e quindi elimina tutti i clienti non iscritti al programma.

Il KPI viene calcolato su una popolazione molto più fedele della base reale.

La pipeline è 27 volte più veloce e analiticamente sbagliata.

Questo riassume bene il tema del libro:

> **la performance tecnica non compensa una definizione sbagliata della popolazione.**

## 13.2.7 Regola operativa

Usa SQL quando il problema è principalmente:

**selezionare → collegare → filtrare → aggregare → trasformare dati strutturati**.

Porta il risultato in un altro ambiente quando la domanda diventa:

**stimare → simulare → ottimizzare → visualizzare → modellare**.
