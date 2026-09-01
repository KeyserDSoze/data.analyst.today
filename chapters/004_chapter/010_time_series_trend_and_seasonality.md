## 4.9 Il tempo nell'EDA: trend, stagionalità e baseline prima del forecasting

Una variabile temporale non è una dimensione qualsiasi.

Quando osserviamo vendite, traffico, ticket, ordini o domanda giorno dopo giorno, l'ordine delle osservazioni contiene informazione. Un lunedì non è necessariamente confrontabile con una domenica; dicembre non è necessariamente confrontabile con gennaio; due mesi consecutivi possono condividere un trend di fondo.

Nel Capitolo 7 affronteremo in modo sistematico serie temporali, autocorrelazione, decomposizione, anomalie e forecasting.

Qui ci serve un obiettivo più modesto e fondamentale:

> **evitare che l'EDA interpreti come eccezione ciò che il calendario o il trend rendono normale.**

### Caso simulato/composito — Il +92% che diventò +9%

Una catena di palestre osserva che nella prima settimana di gennaio gli accessi sono superiori del **92%** rispetto alla prima settimana di dicembre.

La campagna di Capodanno è partita il 2 gennaio. Il team marketing attribuisce quasi tutto l'incremento alla campagna.

L'analista allunga la serie e confronta la stessa settimana su cinque anni.

Gennaio mostra sistematicamente un forte aumento di accessi e iscrizioni.

Rispetto alla baseline stagionale, l'anno corrente è circa **+9%**.

Il +92% è un fatto descrittivo corretto rispetto a dicembre.

Non è la baseline corretta per stimare quanto sia eccezionale gennaio.

### Tre strutture da cercare prima di interpretare

**Trend**

Un movimento persistente di fondo.

Esempio: ricavi crescono gradualmente da 24 mesi.

**Stagionalità**

Una struttura che tende a ripetersi con frequenza regolare:

- giorno della settimana;
- mese;
- trimestre;
- festività;
- stagione turistica;
- ciclo commerciale.

**Shock o cambi di livello**

Un cambiamento improvviso può essere associato a:

- lancio prodotto;
- modifica prezzo;
- outage;
- campagna;
- nuova regolamentazione;
- evento esterno.

L'EDA può rilevare la coincidenza. Non dimostra automaticamente che l'evento abbia causato il cambiamento.

### La baseline temporale deve seguire il processo

"Rispetto a prima" può voler dire molte cose:

- giorno precedente;
- stessa giornata della settimana precedente;
- media delle ultime quattro settimane;
- stesso mese dell'anno precedente;
- periodo pre-intervento;
- valore atteso per la stagione.

La baseline appropriata dipende dal ciclo naturale del fenomeno.

Un ristorante può confrontare venerdì con gli altri venerdì. Un SaaS B2B potrebbe guardare il mese su anno. Un sito di e-commerce può dover allineare Black Friday e festività mobili, non semplicemente i numeri di giorno del calendario.

### Il grafico temporale deve mostrare anche il denominatore quando serve

Un conteggio può crescere solo perché cresce l'esposizione.

Esempio:

```text
cancellazioni mensili: 900 → 1.100
abbonati attivi:      25.000 → 40.000
```

Il conteggio aumenta, ma il tasso scende.

Per questo un trend di numerator senza denominator può raccontare una storia diversa dal rischio individuale.

### Un confronto before/after è ancora descrittivo

Supponiamo che conversion rate passi da 4,2% a 5,1% subito dopo una release.

L'EDA può dire:

> il livello cambia in coincidenza temporale con la release.

Non può ancora dire:

> la release ha causato +0,9 pp.

Nello stesso momento possono essere cambiati mix di traffico, campagne, stagionalità o altri fattori.

Questa distinzione prepara il lavoro causale dei Capitoli 8 e 9.

### Una sequenza pratica

Per una metrica temporale:

1. mostra la serie grezza;
2. aggiungi il volume o denominatore rilevante;
3. confronta cicli equivalenti;
4. identifica trend e pattern ricorrenti;
5. annota eventi di business noti;
6. verifica se il pattern aggregato cambia per segmento;
7. usa smoothing soltanto come supporto visivo, non come prova.

NIST sottolinea che le osservazioni temporali possono presentare dipendenze e struttura e che stagionalità e trend devono essere riconosciuti nel processo analitico.[^nist-timeseries]

> **Nel tempo, un numero non è "alto" o "basso" in assoluto. È alto o basso rispetto a ciò che era ragionevole aspettarsi in quel momento.**

[^nist-timeseries]: NIST/SEMATECH, *Introduction to Time Series Analysis*. https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm