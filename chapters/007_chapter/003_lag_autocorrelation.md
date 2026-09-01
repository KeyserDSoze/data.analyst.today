## 7.2 Lag e autocorrelazione: capire quanta memoria contiene la serie

In un dataset tabellare possiamo talvolta trattare le righe come osservazioni indipendenti. In una serie temporale questa assunzione è spesso sbagliata.

Il valore di oggi può essere informativo sul valore di domani perché il processo possiede **memoria**.

Un **lag** è una versione ritardata della serie:

- lag 1 su dati giornalieri = ieri;
- lag 7 = lo stesso giorno della settimana precedente;
- lag 12 su dati mensili = lo stesso mese dell'anno precedente.

L'**autocorrelazione** misura la relazione tra la serie e sé stessa a lag differenti. NIST la usa per rilevare struttura non casuale e supportare l'identificazione dei pattern temporali.[^nist-acf]

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

La deviazione standard giornaliera è alta. Se ignoriamo il calendario, il processo sembra molto instabile.

Ma il lunedì successivo assomiglia molto più al lunedì precedente che alla domenica immediatamente precedente.

Per la pianificazione del personale, il lag 7 contiene più informazione del lag 1.

La serie non è “rumorosa senza struttura”. Ha una forte memoria settimanale.

### Il lag deve avere significato operativo

Non cerchiamo lags solo perché il software li propone.

Possibili memorie del processo:

- domanda urbana → 24 ore e 7 giorni;
- traffico web B2B → giorno lavorativo precedente e settimana precedente;
- vendite mensili → mese precedente e anno precedente;
- sensori industriali → secondi/minuti precedenti;
- rinnovi annuali → mesi dalla scadenza precedente.

Il calendario aziendale può generare lags che non corrispondono perfettamente a quello civile.

Un business aperto cinque giorni su sette può avere una memoria “giorno lavorativo precedente” più utile del semplice `t-1`.

### Autocorrelazione grezza e autocorrelazione residua

Una forte autocorrelazione può derivare da trend o stagionalità già visibili.

Se le vendite crescono ogni mese, valori vicini saranno simili anche senza una dinamica locale particolarmente interessante.

Per questo è utile chiedere:

> dopo aver rimosso trend e stagionalità, rimane ancora dipendenza temporale?

Se sì, il residuo contiene struttura che il modello non ha ancora catturato.

Se no, gran parte della “memoria” era già spiegata dalle componenti sistematiche.

### Autocorrelazione non è causalità

Se `y_t` è correlato a `y_(t-1)`, non significa che il valore precedente **causi** il successivo.

Entrambi possono essere prodotti da:

- domanda persistente;
- capacità stabile;
- calendario;
- prezzo;
- clima;
- stock;
- composizione dei clienti.

L'autocorrelazione ci dice che il passato contiene informazione sul futuro. Non ci dice il meccanismo causale.

### Perché ignorarla rende l'incertezza troppo piccola

Supponiamo di avere 10.000 misure al minuto provenienti dallo stesso processo molto persistente.

Non possediamo necessariamente l'equivalente informativo di 10.000 osservazioni indipendenti.

Se una tecnica inferenziale assume indipendenza e noi ignoriamo la dipendenza seriale, possiamo:

- sottostimare l'errore standard;
- produrre troppi alert;
- dichiarare cambiamenti più convincenti di quanto siano;
- sovrastimare il valore di nuovi dati molto ravvicinati.

NIST, discutendo change-point su serie autocorrelate, osserva che ignorare l'autocorrelazione può portare a identificare più cambiamenti di quanti ce ne siano realmente.[^nist-changepoint]

### ACF come domanda, non come decorazione

Un autocorrelation plot dovrebbe servire a formulare domande:

- lag 1 è forte perché esiste inerzia?
- compaiono picchi a 7, 14, 21 giorni?
- la dipendenza decade lentamente, suggerendo trend/non stazionarietà?
- dopo la trasformazione o decomposizione il residuo assomiglia maggiormente a rumore?

Il grafico non decide il modello da solo. Aiuta a capire quale struttura deve essere spiegata.

### La domanda operativa

Nel Temporal Decision Brief, la parte sulla memoria dovrebbe poter dire:

> **La serie mostra dipendenza rilevante ai lag ______, coerente con ______. Dopo aver controllato per ______, rimane/non rimane struttura seriale significativa da modellare.**

Questo è molto più utile di scrivere soltanto “ACF alta”.

[^nist-acf]: NIST/SEMATECH e-Handbook of Statistical Methods, “Autocorrelation”, https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm
[^nist-changepoint]: NIST, *Statistical Methods for Change-Point Detection in Surface Temperature Records*, https://www.nist.gov/publications/statistical-methods-change-point-detection-surface-temperature-records
