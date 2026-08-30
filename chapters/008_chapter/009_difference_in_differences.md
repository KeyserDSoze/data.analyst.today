## 8.8 Difference-in-Differences: confrontare cambiamenti, non livelli

Quando un trattamento viene introdotto in un gruppo ma non in un altro, e abbiamo dati prima e dopo l'intervento, possiamo talvolta usare il metodo Difference-in-Differences, spesso abbreviato in DiD.

L'idea è semplice:

1. misurare il cambiamento nel gruppo trattato;
2. misurare il cambiamento nel gruppo di confronto;
3. sottrarre il secondo dal primo.

In forma compatta:

`DiD = (Trattati_dopo - Trattati_prima) - (Controllo_dopo - Controllo_prima)`

### Caso - Nuovo layout in 25 negozi

Una catena retail introduce un nuovo layout in 25 negozi del Nord Italia. Altri 25 negozi simili mantengono il layout precedente.

Revenue medio settimanale:

| Gruppo | Prima | Dopo | Variazione |
|---|---:|---:|---:|
| Nuovo layout | 118.000 € | 129.000 € | +11.000 € |
| Controllo | 121.000 € | 126.000 € | +5.000 € |

Il confronto prima/dopo nei negozi trattati suggerirebbe un effetto di +11.000 €.

Ma anche i negozi di controllo crescono di 5.000 €, forse per stagionalità, maggiore traffico o una campagna nazionale.

La stima DiD è quindi:

`11.000 - 5.000 = 6.000 €`

La lettura causale sarebbe: il nuovo layout ha aumentato il revenue settimanale di circa 6.000 € rispetto a ciò che sarebbe accaduto ai negozi trattati in assenza del cambiamento.

Ma questa interpretazione dipende da un'assunzione fondamentale.

### Parallel trends

L'ipotesi chiave è che, senza trattamento, il gruppo trattato avrebbe seguito nel tempo una dinamica simile al gruppo di controllo.

Non è necessario che i due gruppi abbiano lo stesso livello iniziale. Possono partire da revenue diversi. Ciò che conta è la plausibilità di trend paralleli in assenza dell'intervento.

Per questo non basta avere un "prima" e un "dopo". È molto meglio osservare più periodi pre-trattamento e verificare se le traiettorie erano compatibili.

### Caso - La falsa vittoria del nuovo pricing

Un SaaS introduce un nuovo pricing nel Regno Unito, ma non in Francia.

MRR medio per account:

| Mese | UK | Francia |
|---|---:|---:|
| Gen | 186 € | 181 € |
| Feb | 191 € | 182 € |
| Mar | 198 € | 183 € |
| Apr - pricing | 211 € | 184 € |
| Mag | 222 € | 185 € |

Un DiD semplice potrebbe attribuire gran parte dell'aumento UK al pricing.

Ma guardando i mesi precedenti, l'UK aveva già una crescita molto più rapida della Francia prima dell'intervento.

L'assunzione di parallel trends è quindi poco credibile.

Il metodo produce un numero, ma il design non sostiene bene la conclusione causale.

### Shock differenziali

Anche con trend pre-trattamento simili, un altro evento può colpire solo il gruppo trattato nello stesso momento.

Nel caso retail, durante il rollout del nuovo layout potrebbe essere partita una campagna locale esclusiva nei negozi trattati. La DiD attribuirebbe al layout anche l'effetto della campagna.

Occorre quindi cercare:

- campagne contemporanee;
- cambi di assortimento;
- variazioni di prezzo;
- nuove aperture o chiusure concorrenti;
- cambiamenti normativi;
- problemi di supply chain;
- differenze nella qualità del dato.

### Event study e dinamica dell'effetto

Quando abbiamo molti periodi, è utile osservare l'evoluzione dell'effetto prima e dopo il trattamento.

Questo aiuta a capire:

- se esistono pre-trend problematici;
- se l'effetto appare immediatamente;
- se cresce gradualmente;
- se svanisce dopo qualche mese;
- se anticipazioni del trattamento modificano il comportamento già prima dell'entrata in vigore.

### Caso - Policy di smart working

Una società introduce una policy di smart working più flessibile in una business unit e vuole misurare l'impatto sul turnover.

Guardando solo dodici mesi prima e dodici dopo, il turnover scende di 3 punti percentuali rispetto a una business unit di controllo.

L'event study mostra però che il calo era iniziato tre mesi prima dell'introduzione ufficiale, proprio quando era stata annunciata la nuova policy.

Questo non significa necessariamente che la policy non funzioni. Significa che la data di trattamento effettiva potrebbe essere l'annuncio, non la data formale di entrata in vigore.

### DiD non è una scorciatoia automatica

È potente quando il confronto è credibile. È fragile quando viene applicata meccanicamente a due gruppi qualsiasi.

Prima di usarla chiediamo:

1. perché il gruppo trattato ha ricevuto l'intervento?
2. il gruppo di controllo rappresenta un controfattuale plausibile?
3. i trend prima dell'intervento sono comparabili?
4. altri eventi hanno colpito i gruppi in modo differente?
5. l'anticipazione dell'intervento è possibile?
6. il trattamento avviene nello stesso momento per tutti o in momenti diversi?

> **Difference-in-Differences non elimina la necessità di ragionare causalmente. La rende più esplicita.**

## Riferimenti

- World Bank, *Impact Evaluation in Practice*, capitolo 7: Difference-in-Differences.
- World Bank DIME Wiki, *Difference-in-Differences*: confronto dei cambiamenti tra gruppo trattato e gruppo di controllo e centralità dell'assunzione di equal/parallel trends.
