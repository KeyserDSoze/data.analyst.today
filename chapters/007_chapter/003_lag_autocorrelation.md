## 7.2 Lag e autocorrelazione: capire quanta memoria contiene la serie

Una serie temporale non è soltanto una tabella ordinata per data. L'ordine stesso contiene informazione. Se il processo possiede inerzia, calendario o cicli ricorrenti, il valore di oggi può essere informativo sul valore di domani e osservazioni molto vicine possono essere assai meno indipendenti di quanto suggerisca il numero di righe.

Un **lag** è semplicemente la serie vista con un ritardo: su dati giornalieri `lag 1` significa ieri, `lag 7` lo stesso giorno della settimana precedente; su dati mensili `lag 12` richiama lo stesso mese dell'anno precedente. L'**autocorrelazione** misura quanto la serie assomigli a sé stessa a questi ritardi. NIST la utilizza proprio per rendere visibile struttura non casuale e periodicità.[^nist-acf]

### Caso simulato/composito — Il contact center che sembrava caotico

Un contact center osserva:

| Giorno | Chiamate |
| --- | ---: |
| Lun | 8.420 |
| Mar | 7.910 |
| Mer | 7.760 |
| Gio | 7.580 |
| Ven | 7.210 |
| Sab | 4.100 |
| Dom | 3.320 |
| Lun successivo | 8.510 |

La deviazione standard giornaliera è alta. Se trattiamo ogni giorno come un'osservazione intercambiabile, il processo sembra instabile. Ma il lunedì successivo assomiglia molto più al lunedì precedente che alla domenica immediatamente prima. Per il capacity planning, `lag 7` contiene più informazione di `lag 1`.

Questa differenza rende evidente un principio: il lag utile deve avere **significato operativo**, non soltanto essere disponibile nel software. Una domanda urbana può avere memoria a 24 ore e 7 giorni; il traffico web B2B può seguire soprattutto il calendario lavorativo; le vendite mensili possono conservare informazione dal mese precedente e dall'anno precedente; un sensore industriale può avere dipendenza a pochi secondi. In un'azienda aperta cinque giorni su sette, persino “giorno lavorativo precedente” può essere una relazione più sensata del semplice `t-1`.

### Memoria apparente e memoria residua

Una forte autocorrelazione grezza può essere prodotta da trend e stagionalità già visibili. Se le vendite crescono quasi ogni mese, valori adiacenti saranno simili anche senza una dinamica locale particolarmente interessante. Per questo la domanda più utile non è soltanto *quanto è alta l'ACF?*, ma:

> **Dopo aver rappresentato trend, calendario e stagionalità, rimane ancora dipendenza temporale nei residui?**

Se sì, il modello non ha ancora catturato tutta la struttura. Se no, gran parte della memoria osservata era già spiegata dalle componenti sistematiche.

Questa distinzione è importante anche per l'incertezza. Diecimila misure al minuto dello stesso processo persistente non contengono necessariamente l'equivalente di diecimila osservazioni indipendenti. Ignorare la dipendenza seriale può produrre errori standard troppo piccoli, alert eccessivi e una falsa impressione di quanta informazione nuova stiamo raccogliendo. NIST, nel lavoro sui change-point, sottolinea esplicitamente che autocorrelazione e variabilità naturale devono essere considerate quando si cerca di identificare cambiamenti nella serie.[^nist-changepoint]

L'autocorrelazione, però, resta una relazione predittiva, non una spiegazione causale. Se `y_t` è correlato con `y_(t-1)`, il valore precedente non diventa per questo la causa del successivo. Entrambi possono riflettere domanda persistente, capacità, calendario, prezzo, meteo, stock o composizione dei clienti. Il passato può essere informativo senza essere il meccanismo.

Un autocorrelation plot serve quindi soprattutto a formulare domande: compaiono picchi a 7, 14 e 21 giorni? La dipendenza decade lentamente perché la serie non è stazionaria? Dopo decomposizione o trasformazione il residuo assomiglia di più a rumore? La risposta non seleziona automaticamente un algoritmo; definisce quale struttura il modello dovrà riuscire a spiegare.

Nel Temporal Decision Brief la memoria della serie dovrebbe poter essere descritta così:

> **La serie mostra dipendenza rilevante ai lag ______, coerente con ______. Dopo aver controllato per ______, rimane/non rimane struttura seriale materialmente rilevante.**

Il passo successivo è capire se questa memoria opera dentro un processo abbastanza stabile da poter essere trasferito nel tempo, oppure se livello, varianza e relazioni stanno cambiando insieme alla serie.

[^nist-acf]: NIST/SEMATECH e-Handbook of Statistical Methods, “Autocorrelation”, https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm
[^nist-changepoint]: NIST, *Statistical Methods for Change-Point Detection in Surface Temperature Records*, https://www.nist.gov/publications/statistical-methods-change-point-detection-surface-temperature-records
