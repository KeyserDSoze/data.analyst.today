## 13.3 Python, R e notebook: scegliere programmabilità quando serve libertà metodologica

Python e R diventano particolarmente utili quando il problema richiede una flessibilità che SQL o un foglio esprimono male.

La proprietà importante non è semplicemente “scrivere codice”.

È poter rappresentare in modo esplicito:

```text
input → trasformazione → metodo → diagnostica → output
```

usando librerie, funzioni, cicli, simulazioni e test che possono essere riutilizzati.

### Quando la programmabilità crea valore

Python o R sono spesso una buona scelta quando servono:

- statistica avanzata;
- machine learning;
- simulazioni;
- ottimizzazione;
- bootstrap o procedure iterative;
- text/image processing;
- API e integrazioni custom;
- grafici diagnostici;
- automazioni non naturalmente relazionali.

La domanda utile è:

> **il problema richiede davvero libertà algoritmica oppure stiamo usando codice per un'aggregazione che il warehouse eseguirebbe meglio?**

### Caso simulato/composito — 600 viste del lifecycle

Un marketplace vuole verificare centinaia di combinazioni di paese, categoria, acquisition channel e tenure.

Per ogni combinazione servono:

- numerosità;
- retention;
- intervalli;
- delta rispetto alla baseline;
- grafico;
- ranking dei deterioramenti.

Costruire manualmente centinaia di pivot e chart sarebbe fragile.

Un programma può applicare la stessa funzione a ogni segmento, produrre controlli standard e rendere esplicito ciò che è stato eseguito.

Qui il vantaggio del codice è **sistematicità**.

### Il notebook è un laboratorio, non una garanzia di riproducibilità

Il notebook è potente perché combina:

- testo;
- codice;
- output;
- grafici;
- ragionamento.

È quindi eccellente per:

- EDA;
- prototipazione;
- analisi metodologica;
- confronto di modelli;
- documentazione tecnica interattiva.

Ma introduce un rischio specifico: **hidden state**.

Una cella può dipendere da qualcosa eseguito venti minuti prima e non più visibile nell'ordine del documento.

### Caso simulato/composito — funziona solo sulla sessione di Marco

Un notebook di forecasting produce correttamente il report del venerdì.

Lunedì una collega lo apre e non riesce a riprodurre il risultato.

Scopre che:

- `forecast_input.csv` era un file locale modificato manualmente;
- due celle erano state eseguite fuori ordine;
- una variabile in memoria proveniva da un tentativo precedente;
- la libreria usata aveva una versione diversa;
- un path assoluto puntava alla cartella personale dell'autore.

Il notebook non è “inaffidabile per natura”.

Ma per fidarsi dobbiamo sapere se funziona:

```text
nuovo ambiente
+ input dichiarati
+ esecuzione dall'inizio
= stesso processo
```

### Dal notebook alla libreria o pipeline

Quando una parte del lavoro si stabilizza, può essere utile estrarla.

```text
notebook
├─ narrativa / exploration
├─ chiamate a funzioni stabili
└─ output diagnostici

src/
├─ data preparation
├─ metrics
├─ models
└─ tests
```

Questo non significa che ogni notebook debba diventare un progetto software.

Significa che **logica stabile e riusata** merita una casa più testabile dello stato interattivo.

### Python o R: il contesto conta più dell'identità

Entrambi possono coprire moltissimi problemi analitici.

La scelta dovrebbe considerare:

- ecosistema del team;
- librerie necessarie;
- deployment;
- standard interni;
- facilità di review;
- competenze già presenti;
- interoperabilità con la piattaforma dati.

Un linguaggio leggermente meno elegante per il singolo analyst può essere una scelta migliore se altre otto persone possono mantenerlo.

### La flessibilità ha un costo di governance

Con un linguaggio general purpose possiamo:

- leggere file locali;
- fare chiamate di rete;
- cambiare dati;
- introdurre dipendenze;
- usare librerie arbitrarie;
- serializzare oggetti;
- automatizzare azioni.

Questa libertà aumenta anche il numero dei failure mode.

Per questo, con l'aumentare della criticità, diventano importanti:

- environment/dependency management;
- test;
- version control;
- logging;
- secret management;
- code review;
- separazione tra configurazione e logica.

### Campo del Tooling Decision Record

Se scegliamo Python/R/notebook annotiamo:

```text
method requiring code:
data size after pushdown:
interactive vs recurring:
notebook or module/pipeline:
environment/dependencies:
review owner:
execution environment:
output destination:
reproducibility requirement:
exit condition:
```

Esempio:

> Il notebook resta ambiente esplorativo. Se lo score viene distribuito settimanalmente a Operations, spostare data prep e scoring in codice testato/schedulato e lasciare il notebook come diagnostica.

### Regola operativa

> **Scegli la programmabilità quando riduce la complessità del metodo o rende il processo sistematico. Non scegliere il codice perché rende tecnicamente possibile fare tutto nello stesso posto.**

### Riferimenti

- pandas documentation: https://pandas.pydata.org/docs/
- Project Jupyter: https://jupyter.org/
