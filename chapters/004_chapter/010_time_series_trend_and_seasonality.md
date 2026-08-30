## 4.9 Trend, stagionalità e serie temporali: il tempo non è una dimensione come le altre

Quando i dati sono ordinati nel tempo, le osservazioni non possono essere trattate sempre come punti indipendenti.

Vendite, ticket di assistenza, traffico web, domanda energetica e ordini logistici hanno spesso una struttura interna: trend, stagionalità, cicli, autocorrelazione, shock e cambi di regime. NIST evidenzia proprio questa caratteristica delle serie temporali: i punti osservati nel tempo possono avere dipendenze e strutture che devono essere considerate nell'analisi.[^nist-timeseries]

### Caso: il lunedì peggiore dell'anno

Una catena di palestre osserva che il 7 gennaio gli accessi sono cresciuti del 92% rispetto al 7 dicembre. Il responsabile marketing attribuisce il risultato alla nuova campagna lanciata il 2 gennaio.

Il confronto sembra convincente, ma è metodologicamente debole. Gennaio è storicamente il mese con il maggior numero di nuove iscrizioni e accessi. Confrontare gennaio con dicembre confonde effetto campagna e stagionalità.

L'analista ricostruisce cinque anni di dati settimanali e confronta la prima settimana di gennaio con la stessa settimana degli anni precedenti. La crescita rispetto al normale pattern stagionale è solo del 9%.

Il 92% era reale. L'interpretazione era sbagliata.

### Trend

Il trend è un movimento di fondo persistente nel tempo. Può essere crescente, decrescente o cambiare direzione.

Un'azienda può avere ricavi in crescita del 2% ogni mese ma perdere progressivamente clienti, compensando il calo attraverso aumenti di prezzo. Guardare una sola serie può quindi nascondere la dinamica sottostante.

### Stagionalità

La stagionalità è una variazione che tende a ripetersi con una periodicità riconoscibile: giorno della settimana, mese, trimestre, festività, stagione turistica o ciclo operativo.

NIST usa l'esempio delle vendite retail che tendono a crescere prima di Natale e a diminuire dopo le festività, e raccomanda di incorporare la stagionalità quando è presente.[^nist-seasonality]

### Il confronto giusto

Una buona analisi temporale chiede sempre: rispetto a cosa?

- giorno precedente;
- stessa settimana precedente;
- stesso giorno della settimana;
- stesso mese dell'anno precedente;
- media mobile;
- baseline stagionale;
- forecast atteso.

La scelta dipende dal processo.

Un ristorante non dovrebbe valutare il venerdì sera rispetto al giovedì sera. Un marketplace turistico non dovrebbe confrontare agosto con luglio senza conoscere la stagionalità. Un servizio B2B con rinnovi annuali potrebbe trovare molto più informativo un confronto year-over-year.

La domanda corretta non è semplicemente "il numero è salito?", ma **"è salito più o meno di quanto sarebbe stato ragionevole aspettarsi in quel momento?"**.

[^nist-timeseries]: NIST/SEMATECH, *Introduction to Time Series Analysis*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
[^nist-seasonality]: NIST/SEMATECH, *Seasonality*: https://itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm