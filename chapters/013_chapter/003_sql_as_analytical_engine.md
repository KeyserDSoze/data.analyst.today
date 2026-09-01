## 13.2 SQL: scegliere il luogo del calcolo, non soltanto il linguaggio

Il Capitolo 11 ha già trattato grain, join, trasformazioni e semantica SQL.

Qui la domanda è diversa:

> **Quando conviene che il lavoro analitico avvenga vicino al dato, dentro un motore relazionale o analitico?**

SQL è spesso la scelta naturale non perché sia “più professionale” di uno spreadsheet o di Python, ma perché evita di spostare grandi quantità di dati fuori dal sistema che li gestisce già bene.

### Quando il calcolo appartiene naturalmente al motore dati

SQL è particolarmente adatto quando il problema è dominato da:

- selezione;
- filtri;
- join;
- aggregazioni;
- window calculations;
- trasformazioni tabellari;
- costruzione di popolazioni o feature;
- riuso condiviso della stessa logica.

Se 800 milioni di righe sono già nel warehouse e il risultato finale è una tabella di 20.000 righe, scaricare il dato grezzo su un laptop è spesso un design inefficiente.

### Caso simulato/composito — 180 milioni di righe per quattro KPI

Un analyst deve calcolare:

- clienti attivi;
- ordini per cliente;
- net revenue;
- repeat rate.

Gli eventi sono già nel warehouse.

Due opzioni:

```text
A. esportare 180 milioni di righe → pandas → aggregare
B. aggregare nel warehouse → esportare solo il risultato necessario
```

Se la logica è principalmente relazionale, B riduce:

- trasferimento dati;
- memoria locale;
- copie sensibili;
- tempo di elaborazione;
- dipendenza dal computer dell'analista.

> **Compute near data** è spesso una scelta di semplicità, non di sofisticazione.

### Quando SQL non dovrebbe diventare il martello universale

Alcuni problemi sono esprimibili in SQL ma diventano più difficili da leggere, testare o mantenere quando richiedono:

- simulazioni iterative;
- ottimizzazione numerica;
- statistica specializzata;
- algoritmi scientifici;
- testo, immagini o oggetti non tabellari;
- visual diagnostics complessi;
- workflow modellistici con librerie dedicate.

In questi casi la divisione del lavoro può essere:

```text
SQL → costruisce il dataset analitico
Python/R → esegue il metodo specialistico
SQL/table → riceve il risultato riusabile
```

Non c'è alcun premio per comprimere tutta l'analisi in una query di 1.500 righe.

### Pushdown vs pull-out

Possiamo usare una domanda molto pratica:

> Quale parte del lavoro dovrebbe essere **spinta verso il dato** e quale parte dovrebbe essere **portata nell'ambiente analitico**?

**Pushdown** è spesso sensato per:

- filtri;
- join;
- aggregazioni;
- feature semplici;
- dedup;
- partizionamento della popolazione.

**Pull-out** è spesso sensato quando serve:

- interazione rapida su un dataset già ridotto;
- algoritmo non disponibile nel motore;
- libreria scientifica;
- visualizzazione diagnostica;
- simulazione.

### Caso simulato/composito — la query 27 volte più veloce e sbagliata

Un team riscrive in SQL un processo locale e passa da 18 minuti a 40 secondi.

Poi scopre che la nuova query usa un `INNER JOIN` con la loyalty table e rimuove tutti i clienti non iscritti.

Il sistema è molto più veloce e risponde alla popolazione sbagliata.

Questo è il confine con il Capitolo 11:

- **13:** SQL era il posto giusto per eseguire quel workload?
- **11:** la trasformazione SQL conserva davvero il significato?

Servono entrambe le risposte.

### SQL come asset condiviso

Un altro motivo per spostare una trasformazione da notebook o workbook verso SQL centrale è il riuso.

Se cinque analyst ricostruiscono ogni settimana `net_orders`, la domanda non è più soltanto “chi scrive la query meglio?”.

Potrebbe servire:

```text
raw / source
   ↓
shared transformation
   ↓
certified analytical model
   ↓
consumer diversi
```

Qui lo strumento diventa anche una decisione di ownership.

### Campo del Tooling Decision Record

Per una scelta SQL annotiamo:

```text
data location:
input scale:
expected output scale:
relational workload share:
shared or local logic:
execution frequency:
compute / scan cost:
consumer of output:
reason not to use local processing:
exit condition:
```

Una possibile exit condition:

> Passare parte della logica a Python/R quando la metodologia richiede simulazione o diagnostica statistica che rende la query difficile da verificare.

### Regola operativa

> **Usa SQL quando il problema beneficia dal calcolo vicino al dato e da trasformazioni tabellari condivise. Non usarlo per dimostrare che tutto può essere scritto in SQL.**
