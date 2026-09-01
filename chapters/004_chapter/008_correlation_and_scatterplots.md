## 4.7 Scatter plot e correlazione: guardare la relazione prima di comprimerla

Quando due variabili sembrano muoversi insieme, è naturale voler riassumere la relazione in un numero.

Il coefficiente di correlazione può essere utile.

Ma dovrebbe arrivare **dopo** il grafico, non prima.

NIST considera lo scatter plot uno degli strumenti centrali dell'EDA perché rende visibili forma, gruppi, outlier, cambi di variabilità e relazioni non lineari che un singolo coefficiente può nascondere.[^nist-scatter]

### Pearson: che cosa misura davvero

La correlazione lineare di Pearson assume valori tra `-1` e `1` e misura direzione e intensità dell'associazione **lineare** tra due variabili quantitative.

In termini intuitivi:

- vicino a `+1`: i punti seguono strettamente una relazione lineare crescente;
- vicino a `-1`: relazione lineare decrescente;
- vicino a `0`: poca relazione lineare.

L'ultima frase è importante.

`r ≈ 0` non significa necessariamente "nessuna relazione".

Una relazione a U può essere fortissima e avere correlazione lineare quasi nulla.

### Caso reale documentato — Il quartetto di Anscombe

Nel quartetto di Anscombe, richiamato nell'introduzione del capitolo, quattro dataset condividono praticamente gli stessi valori di:

- media di X;
- media di Y;
- varianze;
- retta di regressione;
- correlazione, circa `0,816`.

Eppure gli scatter plot mostrano:

1. una relazione lineare ragionevole;
2. una struttura chiaramente curva;
3. una relazione dominata da un outlier;
4. quasi tutti i punti allineati verticalmente e un singolo punto ad alta leva che determina la retta.[^nist-anscombe]

È difficile immaginare un argomento più forte per questa regola:

> **non interpretare una correlazione che non hai guardato.**

### Caso simulato/composito — Formazione commerciale e fatturato

Una catena di 64 negozi confronta:

```text
X = ore di formazione commerciale per addetto
Y = fatturato mensile per addetto
```

La correlazione è `0,71`.

Prima di proporre più formazione, l'analista guarda il grafico e nota che:

- i negozi più grandi occupano la parte alta di entrambe le variabili;
- due flagship store sono lontani dal resto;
- all'interno dei piccoli negozi la relazione è molto più debole.

Possibili spiegazioni concorrenti:

- la formazione migliora le vendite;
- i negozi con maggiore budget possono permettersi più formazione;
- i manager migliori producono sia più formazione sia migliori risultati;
- i flagship operano in mercati con domanda maggiore.

La correlazione è un pattern vero nel dataset. La sua interpretazione causale resta aperta.

### Quattro cose che il coefficiente può nascondere

**Non linearità**

La relazione può avere soglie, saturazione o curvature.

Esempio: engagement e retention crescono insieme solo fino a cinque sessioni settimanali, poi si appiattiscono.

**Cluster**

Due segmenti possono produrre una correlazione aggregata che non esiste dentro nessuno dei due.

**Outlier e punti ad alta leva**

Poche osservazioni possono determinare gran parte del coefficiente.

**Eteroschedasticità descrittiva**

La dispersione di Y può crescere con X: non cambia soltanto il centro della relazione, cambia anche la sua variabilità.

Non serve ancora formalizzare un modello. Basta accorgersi che una linea non riassume tutto.

### Correlazioni spurie nel tempo

Due serie crescenti possono risultare fortemente correlate soltanto perché condividono un trend.

Per esempio:

- spesa pubblicitaria crescente;
- ordini crescenti;
- numero di dipendenti crescente;
- dimensione del catalogo crescente.

Se tutte aumentano nel tempo, molte coppie mostreranno correlazioni elevate anche senza un meccanismo diretto.

Per questo, davanti a dati temporali, lo scatter plot va affiancato alla dimensione tempo e a baseline coerenti.

### La matrice di correlazione è una mappa, non una classifica di cause

Con molte variabili è comune produrre una correlation matrix.

Può essere utile per trovare relazioni da esplorare, ma introduce due rischi:

- più coppie osserviamo, più pattern casuali troveremo;
- una correlazione alta può dipendere da ridondanza semantica o da una terza variabile.

Una matrice con 100 variabili contiene 4.950 coppie distinte. È quasi garantito che qualche coefficiente sembri interessante.

La matrice serve quindi a generare domande, non a selezionare automaticamente "i driver".

### Un linguaggio proporzionato

EDA:

> I negozi con più ore di formazione tendono ad avere fatturato per addetto più elevato (`r = 0,71`), ma la relazione è in parte concentrata nei flagship e non identifica un effetto della formazione.

Conclusione troppo forte:

> Ogni ora di formazione aumenta le vendite.

Tra le due frasi c'è tutta la distanza tra associazione e causalità, che affronteremo in modo sistematico nel Capitolo 8.

### Checklist prima di citare una correlazione

- ho guardato lo scatter plot?
- la relazione è plausibilmente lineare?
- pochi punti dominano il risultato?
- esistono cluster?
- il pattern è stabile nei segmenti rilevanti?
- entrambe le variabili condividono un trend temporale?
- sto descrivendo associazione oppure insinuando causalità?

> **Una correlazione comprime una forma. Prima di fidarti della compressione, guarda la forma.**

[^nist-scatter]: NIST/SEMATECH, *Scatter Plot*. https://www.itl.nist.gov/div898/handbook/eda/section3/scatterp.htm
[^nist-anscombe]: NIST/SEMATECH, *An EDA/Graphics Example*. https://www.itl.nist.gov/div898/handbook/eda/section1/eda16.htm