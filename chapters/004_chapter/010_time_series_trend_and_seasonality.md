## 4.9 Il tempo nell'EDA: un confronto vale solo rispetto al calendario che lo rende sensato

Una variabile temporale non è una dimensione qualsiasi. Quando osserviamo vendite, traffico, ticket o ordini giorno dopo giorno, l'ordine delle osservazioni contiene informazione: lunedì e domenica possono appartenere a regimi diversi, dicembre e gennaio a stagioni differenti, due mesi consecutivi possono condividere un trend di fondo.

Il Capitolo 7 affronterà serie temporali, autocorrelazione, decomposizione e forecasting. Qui serve una disciplina più elementare: **non chiamare anomalo ciò che il calendario, la stagionalità o il trend rendono normale**.

Immaginiamo una catena di palestre che nella prima settimana di gennaio registra accessi superiori del **92%** rispetto alla prima settimana di dicembre. Una campagna è partita il 2 gennaio e la spiegazione sembra immediata. Quando però l'analista allunga la serie e confronta la stessa settimana su cinque anni, scopre che gennaio mostra sistematicamente un forte aumento di accessi e iscrizioni. Rispetto alla baseline stagionale, l'anno corrente è circa **+9%**.

Il +92% non era sbagliato. Rispondeva alla domanda “quanto è diverso gennaio da dicembre?”. Non rispondeva bene alla domanda “quanto è eccezionale questo gennaio rispetto a ciò che normalmente accade in gennaio?”. La baseline modifica quindi l'interpretazione senza cambiare nessuna osservazione.

## Prima della storia, cerchiamo la struttura temporale

In una serie vogliamo distinguere almeno tre fenomeni descrittivi. Un **trend** è un movimento persistente di fondo. La **stagionalità** è una struttura che tende a ripetersi con una frequenza riconoscibile — giorno della settimana, mese, trimestre, festività, stagione turistica o ciclo commerciale. Uno **shock** o cambio di livello è invece un movimento improvviso che può coincidere con lancio prodotto, prezzo, outage, campagna, regolamentazione o evento esterno.

L'EDA può mostrare la coincidenza tra shock e evento. Non può trasformarla automaticamente in causalità. Se conversion rate passa dal 4,2% al 5,1% subito dopo una release, possiamo dire che il livello cambia in coincidenza con la release; non abbiamo ancora dimostrato che la release abbia causato +0,9 punti percentuali. Nello stesso momento possono essere cambiati traffico, campagne, mix o stagionalità.

La baseline deve quindi seguire il processo. “Rispetto a prima” può significare giorno precedente, stesso giorno della settimana precedente, media delle ultime quattro settimane, stesso mese dell'anno precedente o valore atteso per la stagione. Un ristorante può confrontare venerdì con altri venerdì; un SaaS B2B può preferire il confronto year-over-year; un e-commerce deve spesso allineare Black Friday e festività mobili invece di confrontare lo stesso numero di giorno del calendario.

NIST sottolinea proprio che le osservazioni temporali possono contenere dipendenza, trend e stagionalità e che questa struttura deve essere riconosciuta nell'analisi.[^nist-timeseries]

## Il tempo non sostituisce il denominatore

Un conteggio può aumentare semplicemente perché aumenta l'esposizione. Se le cancellazioni mensili passano da 900 a 1.100 mentre gli abbonati attivi crescono da 25.000 a 40.000, il volume assoluto aumenta ma il tasso diminuisce. Per il team che deve gestire 1.100 cancellazioni il carico cresce; per chi valuta il rischio individuale della base clienti il quadro migliora.

La serie temporale deve quindi conservare, quando serve, numeratore e denominatore. Un trend apparentemente negativo nel conteggio può essere positivo nel tasso, e viceversa.

Un buon primo passaggio operativo rimane deliberatamente semplice: mostrare la serie grezza, affiancare volume o denominatore rilevante, confrontare cicli equivalenti, annotare eventi di business noti e verificare se il pattern aggregato cambia per segmento. Lo smoothing, che useremo nella prossima sezione, può aiutare a vedere il movimento di fondo, ma non crea una baseline corretta e non dimostra un trend.

> **Nel tempo un valore non è alto o basso in assoluto. È alto o basso rispetto a ciò che era ragionevole aspettarsi in quel momento.**

[^nist-timeseries]: NIST/SEMATECH, *Introduction to Time Series Analysis*. https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
