# 16.4 Gerarchia visiva e cognitive load

Quando tutto sembra importante, niente lo è davvero.

Una dashboard o una slide può contenere numeri corretti ma costringere il lettore a troppo lavoro cognitivo:

- capire dove guardare;
- distinguere segnale e contesto;
- ricostruire la gerarchia;
- ricordare definizioni;
- confrontare scale incompatibili;
- leggere legende lontane dal dato;
- filtrare mentalmente informazioni irrilevanti.

Questo costo cognitivo riduce la probabilità che il messaggio venga compreso correttamente.

## La gerarchia visiva è una forma di priorità

Se un KPI è la decisione centrale, deve essere facile da trovare.

Se un valore è secondario, non dovrebbe competere visivamente con il messaggio principale.

Possiamo costruire gerarchia usando:

- posizione;
- dimensione;
- contrasto;
- prossimità;
- spazio bianco;
- ordine;
- annotazioni.

Non serve trasformare ogni dashboard in un poster.

Serve evitare che il lettore debba indovinare cosa conta.

## Caso realistico: quattro KPI, sedici colori

Una fintech prepara una dashboard rischio con quattro metriche davvero importanti:

- default rate;
- loss given default;
- approval rate;
- fraud loss.

La pagina usa però sedici colori diversi per segmenti, prodotti, stati, alert e regioni.

Il risultato è visivamente ricco ma cognitivamente rumoroso.

Durante una review, il management dedica diversi minuti a discutere un segmento colorato in rosso perché sembra “critico”.

In realtà quel rosso indica soltanto una categoria prodotto.

La dashboard viene ridisegnata:

- colore neutro per il contesto;
- enfasi solo sugli scostamenti che richiedono attenzione;
- label dirette;
- meno legende;
- alert separati dal codice colore delle categorie.

Il dato non cambia.

Cambia la probabilità di interpretarlo bene.

## Ridurre il lavoro di memoria

Un principio utile è evitare di costringere il lettore a ricordare informazioni presenti altrove.

Esempio debole:

- linea blu = current year;
- linea verde = prior year;
- linea tratteggiata = target;
- legenda in alto a destra;
- grafico in basso a sinistra.

Esempio migliore:

- etichettare direttamente le linee vicino alla loro estremità.

In generale, quando possibile:

- metti label vicino al dato;
- metti il contesto vicino alla metrica;
- metti la spiegazione vicino all'anomalia.

## Precisione apparente e falsa importanza

Un KPI mostrato come `31,847362%` comunica una precisione che raramente è utile alla decisione.

La quantità di decimali dovrebbe dipendere dalla domanda.

Se una decisione cambia solo oltre una differenza di 0,5 punti percentuali, mostrare sei decimali non aggiunge valore.

Può anzi suggerire una certezza inesistente.

## Lo spazio bianco non è spazio sprecato

Lo spazio bianco separa concetti.

Aiuta a capire quali elementi appartengono allo stesso gruppo e quali no.

Riempire ogni centimetro disponibile aumenta spesso il numero di elementi visibili ma diminuisce la leggibilità dell'insieme.

## Una regola pratica

Per ogni pagina chiediamoci:

1. dove guarderà l'utente nei primi tre secondi?
2. è il punto giusto?
3. cosa dovrebbe capire entro dieci secondi?
4. quali dettagli può esplorare dopo?
5. cosa possiamo rimuovere senza perdere capacità decisionale?

Microsoft raccomanda di considerare il pubblico, mettere in evidenza le informazioni più importanti e rimuovere elementi non essenziali quando una pagina diventa troppo affollata.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-tips-and-tricks-for-creating-reports

**La gerarchia visiva non serve a decorare la priorità. Serve a renderla immediatamente percepibile.**
