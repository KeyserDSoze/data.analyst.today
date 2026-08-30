## 5.3 Indipendenza: quando due eventi non si influenzano davvero

Due eventi sono indipendenti quando conoscere il verificarsi di uno non cambia la probabilità dell'altro.

Formalmente:

\[
P(A|B)=P(A)
\]

oppure, in modo equivalente:

\[
P(A \cap B)=P(A)P(B)
\]

La definizione è semplice. Il problema è che nel mondo reale molti eventi che sembrano indipendenti non lo sono affatto.

### Caso realistico: il rischio di consegna sottostimato

Una società di food delivery vuole stimare la probabilità che un ordine subisca almeno uno tra due problemi:

- ritardo del rider;
- ritardo del ristorante.

Dai dati storici risulta:

- 8% degli ordini ha ritardo del rider;
- 6% ha ritardo del ristorante.

Un'analisi superficiale assume indipendenza e calcola la probabilità che entrambi avvengano:

\[
0,08 \times 0,06 = 0,0048
\]

quindi 0,48%.

Ma quando l'analista guarda i dati reali scopre che la probabilità congiunta è 1,9%.

Perché?

Le due cause condividono fattori comuni:

- pioggia intensa;
- picchi serali;
- eventi sportivi;
- zone con traffico critico;
- ristoranti sovraccarichi che trattengono i rider.

Gli eventi non sono indipendenti.

Assumere indipendenza aveva sottostimato di quasi quattro volte la probabilità del problema combinato.

### Dipendenza nascosta da una variabile comune

Supponiamo di osservare una relazione tra:

- probabilità di reso;
- richiesta di assistenza prima dell'acquisto.

Potremmo concludere che il contatto con il customer care aumenta i resi.

Ma entrambe le variabili potrebbero dipendere da un terzo fattore: la complessità del prodotto.

I prodotti complessi generano più domande e più resi.

Quindi i due eventi risultano associati senza che uno causi necessariamente l'altro.

La probabilità ci prepara già al ragionamento sui confondenti.

### Perché moltiplichiamo troppo facilmente

Molti modelli di rischio iniziali fanno qualcosa di simile:

> probabilità guasto componente A × probabilità guasto componente B

oppure:

> probabilità click × probabilità conversione

oppure:

> probabilità ritardo fornitore × probabilità ritardo trasporto

La moltiplicazione è corretta solo sotto determinate condizioni.

Se gli eventi condividono cause, stagionalità o vincoli operativi, l'assunzione può fallire.

### Un test pratico prima della formula

Prima di assumere indipendenza chiediamoci:

**Esiste un fattore che potrebbe influenzare entrambi gli eventi?**

Nel business la risposta è spesso sì.

Tempo, prezzo, canale, segmento cliente, geografia, campagna, capacità operativa e stagionalità sono tutte fonti comuni di dipendenza.

### Indipendenza non significa assenza di relazione visibile

Due variabili possono mostrare poca correlazione lineare e non essere indipendenti.

La correlazione misura soltanto un particolare tipo di associazione. L'indipendenza è un concetto più forte.

Questo diventerà ancora più importante quando studieremo relazioni non lineari e modelli predittivi.

### La domanda dell'analista

Quando una probabilità viene costruita combinando più eventi, non chiediamo soltanto:

**“La formula è corretta?”**

Chiediamo:

**“L'assunzione di indipendenza è plausibile nel processo reale?”**

Ancora una volta, la parte più difficile non è il calcolo. È capire il sistema che stiamo modellando.
