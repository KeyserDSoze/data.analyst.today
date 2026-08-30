## 4.7 Correlazione e scatter plot: una relazione non è ancora una spiegazione

Uno degli errori più comuni nell'analisi dati è trasformare troppo velocemente una relazione osservata in una storia causale.

Immaginiamo una catena di 64 negozi. L'analista mette su uno scatter plot due variabili mensili per punto vendita: ore di formazione commerciale e fatturato medio per addetto. Il grafico mostra una relazione positiva molto netta. I negozi con più ore di formazione tendono anche ad avere fatturato più alto.

Il coefficiente di correlazione è 0,71.

È una relazione forte abbastanza da attirare l'attenzione. Ma non basta per concludere che la formazione abbia causato l'aumento del fatturato.

Potrebbero esistere spiegazioni alternative. I negozi più grandi possono avere budget formativi maggiori e, allo stesso tempo, trovarsi in mercati più ricchi. I manager migliori possono investire di più in formazione e gestire meglio il punto vendita. La direzione potrebbe aver assegnato formazione aggiuntiva proprio ai negozi con maggior potenziale.

Lo scatter plot è quindi uno strumento diagnostico: rende visibile una struttura nei dati, ma non dimostra da solo un meccanismo causa-effetto. NIST sottolinea esplicitamente che associazione e causalità sono concetti distinti e che un grafico di dispersione può evidenziare relazioni senza provare la causa.[^nist-scatter]

### Il valore dello scatter plot

Lo scatter plot serve soprattutto a capire la forma della relazione.

Prima di calcolare un coefficiente conviene guardare i punti. Una correlazione sintetizza molto, ma può nascondere:

- relazioni non lineari;
- gruppi distinti;
- outlier influenti;
- soglie;
- saturazione;
- cambi di regime.

Per esempio, immaginiamo una piattaforma SaaS che confronta il numero di sessioni settimanali con la probabilità di rinnovo. Il coefficiente lineare è moderato, 0,42. Ma il grafico mostra che la probabilità di rinnovo cresce rapidamente tra 0 e 5 sessioni, rimane quasi piatta tra 5 e 20 e non aumenta ulteriormente sopra 20.

Una singola correlazione non racconta questa struttura.

### Pearson non è una formula magica

Il coefficiente di correlazione lineare di Pearson misura intensità e direzione di una relazione lineare tra due variabili quantitative. Assume valori tra -1 e 1.

Un valore vicino a 1 indica forte associazione lineare positiva; vicino a -1 forte associazione lineare negativa; vicino a 0 assenza di una relazione lineare evidente.

Ma "vicino a zero" non significa necessariamente "nessuna relazione".

Se la relazione è a U, per esempio, il coefficiente può essere circa zero anche quando X e Y sono fortemente legate.

### Caso: l'e-commerce che quasi tagliò il budget pubblicitario

Un retailer online osserva per 24 mesi la relazione tra spesa advertising e tasso di reso. La correlazione è 0,68. In riunione qualcuno conclude:

> più spendiamo in pubblicità, più clienti sbagliati acquisiamo e più resi generiamo.

L'analista ricostruisce però le serie mese per mese. Scopre che sia la spesa pubblicitaria sia i resi crescono soprattutto a novembre e dicembre, quando aumentano fortemente gli ordini. Il vero driver comune è il volume stagionale.

Quando l'analisi viene rifatta controllando per numero di ordini e mese dell'anno, la relazione diretta tra advertising e resi quasi scompare.

Il dato iniziale non era falso. Era incompleto.

Questa è una lezione fondamentale dell'EDA: **la correlazione è spesso l'inizio di una domanda, non la fine di un'analisi**.

[^nist-scatter]: NIST/SEMATECH, *Scatter Plot*: https://www.itl.nist.gov/div898/handbook/eda/section3/scatterp.htm