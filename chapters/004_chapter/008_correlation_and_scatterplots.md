## 4.7 Scatter plot e correlazione: comprimere una relazione solo dopo averla guardata

Quando due variabili sembrano muoversi insieme, un coefficiente di correlazione offre una sintesi molto seducente: un solo numero per descrivere direzione e intensità del movimento congiunto. Proprio per questo è facile attribuirgli più significato di quanto abbia guadagnato.

La regola esplorativa è semplice: **prima guardiamo la forma, poi la comprimiamo**. NIST considera lo scatter plot uno degli strumenti centrali dell'EDA perché rende visibili relazioni non lineari, cluster, osservazioni influenti e cambiamenti della dispersione che un singolo coefficiente può nascondere.[^nist-scatter]

La correlazione lineare di Pearson varia tra `-1` e `1` e descrive quanto strettamente due variabili quantitative seguano una relazione **lineare**. Un valore vicino a `+1` indica un allineamento crescente molto forte, vicino a `-1` un allineamento decrescente, vicino a `0` poca associazione lineare. L'aggettivo è fondamentale: una relazione a U può essere strutturalmente fortissima e avere correlazione prossima a zero.

Il quartetto di Anscombe rende visibile l'errore opposto. Quattro dataset possono condividere quasi la stessa correlazione, circa `0,816`, e la stessa retta di regressione pur contenendo una relazione lineare plausibile, una curva, un outlier dominante e un singolo punto ad alta leva che determina quasi tutto il risultato.[^anscombe][^nist-anscombe] Il coefficiente non è sbagliato. È una compressione troppo aggressiva per distinguere strutture incompatibili.

## Una correlazione osservata non contiene il proprio meccanismo

Immaginiamo 64 negozi di una catena commerciale e definiamo `X` come ore di formazione per addetto e `Y` come fatturato mensile per addetto. La correlazione è `0,71`. Sarebbe facile trasformarla nella raccomandazione “facciamo più formazione”.

Lo scatter plot mostra però che i negozi più grandi si trovano nella parte alta di entrambe le variabili, due flagship store sono molto distanti dal resto e, dentro il gruppo dei negozi piccoli, la relazione è molto più debole. A questo punto il pattern rimane vero nel dataset, ma le spiegazioni concorrenti diventano evidenti: la formazione può migliorare le vendite; i negozi con maggior budget possono permettersi più formazione; manager migliori possono produrre entrambe; i flagship possono operare in mercati con domanda maggiore.

L'EDA non deve scegliere immediatamente una di queste storie. Deve rendere difficile confondere l'associazione con l'effetto di un intervento.

Lo scatter plot aiuta anche a riconoscere quattro strutture che il coefficiente comprime male. Una relazione può essere **non lineare**, con soglie o saturazione; può essere prodotta da **cluster** che non mostrano la stessa relazione al proprio interno; può dipendere da **pochi punti ad alta leva**; oppure la variabilità di `Y` può cambiare con `X`, così che una singola linea descriva soltanto il centro mentre la dispersione cresce o si restringe.

## Il tempo può fabbricare correlazioni convincenti

Con dati temporali il rischio aumenta. Se spesa pubblicitaria, ordini, dimensione del catalogo e numero di dipendenti crescono tutti nel corso degli anni, molte coppie mostreranno correlazioni elevate semplicemente perché condividono un trend. Lo scatter plot deve quindi essere letto insieme alla dimensione temporale, alla stagionalità e alla baseline. Il movimento congiunto non dice quale variabile preceda l'altra né se esista un meccanismo diretto.

Lo stesso principio vale per una correlation matrix. Con 100 variabili esistono 4.950 coppie distinte: qualche coefficiente elevato emergerà quasi inevitabilmente. La matrice è una **mappa per decidere dove guardare**, non una classifica automatica dei driver di business.

Per questo il linguaggio deve rimanere proporzionato all'evidenza. Possiamo scrivere:

> I negozi con più ore di formazione tendono ad avere fatturato per addetto più elevato (`r = 0,71`), ma la relazione è in parte concentrata nei flagship e non identifica un effetto della formazione.

Non abbiamo ancora il diritto di scrivere:

> Ogni ora di formazione aumenta le vendite.

Tra le due frasi c'è il confine tra EDA e causalità che verrà affrontato nel Capitolo 8.

Prima di citare una correlazione, quindi, vogliamo sapere se abbiamo guardato il grafico, se la forma è plausibilmente lineare, se pochi punti o cluster dominano il risultato, se il pattern sopravvive nei segmenti rilevanti e se entrambe le variabili condividono un trend temporale. Solo allora il coefficiente diventa una sintesi utile della struttura che abbiamo già compreso.

> **Una correlazione comprime una forma. Prima di fidarti della compressione, guarda la forma che l'ha prodotta.**

---

### Fonti

[^nist-scatter]: NIST/SEMATECH, *Scatter Plot*. https://www.itl.nist.gov/div898/handbook/eda/section3/scatterp.htm
[^anscombe]: F. J. Anscombe, *Graphs in Statistical Analysis*, The American Statistician, 27(1), 1973, pp. 17–21. https://doi.org/10.1080/00031305.1973.10478966
[^nist-anscombe]: NIST/SEMATECH, *An EDA/Graphics Example*. https://www.itl.nist.gov/div898/handbook/eda/section1/eda16.htm
