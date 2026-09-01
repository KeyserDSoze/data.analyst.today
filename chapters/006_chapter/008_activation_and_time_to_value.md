## 6.7 Activation e time-to-value: trovare il primo segnale credibile di valore

Una registrazione è un evento amministrativo. Un onboarding completato è un evento di processo. L'**activation** dovrebbe invece rappresentare il primo momento in cui l'utente ha sperimentato abbastanza valore da rendere plausibile una relazione futura con il prodotto.

Questa distinzione sembra semantica. In realtà cambia completamente ciò che un team ottimizza.

Se definiamo activation come “ha terminato il tutorial”, miglioreremo il tutorial. Se la definiamo come “ha completato il primo lavoro reale con il prodotto”, inizieremo a ottimizzare il percorso verso il valore.

### Un activation event non si scopre con una query magica

È frequente cercare nei dati l'evento che correla maggiormente con la retention e dichiararlo “aha moment”.

È un buon punto di partenza, non una conclusione.

Un candidato credibile dovrebbe avere almeno quattro proprietà:

1. **prossimità al valore** — rappresenta qualcosa che il cliente voleva davvero ottenere;
2. **tempestività** — avviene abbastanza presto da poter guidare onboarding e prodotto;
3. **misurabilità** — può essere osservato in modo coerente;
4. **azionabilità** — il team può progettare un percorso che renda più probabile raggiungerlo.

La correlazione futura con retention aggiunge evidenza, ma non trasforma automaticamente l'evento in una causa.

### Caso simulato/composito: CloudDesk e l'onboarding diventato più facile ma meno utile

**CloudDesk** vende software per piccoli studi professionali. Nel Q1 il team Product ridisegna l'onboarding.

I KPI iniziali sembrano eccellenti:

- completamento onboarding: 61% → 79%;
- tempo medio di onboarding: 18 → 9 minuti;
- drop-off nella configurazione: -42%.

Tre mesi dopo, però, la retention delle nuove coorti è scesa dal 72% al 64%.

L'analista osserva che l'azienda considera “attivato” chi completa tutte le schermate iniziali. Ma quell'evento non richiede che il cliente abbia realmente usato il prodotto per il proprio lavoro.

Viene quindi definito un candidato più vicino al valore:

> creare almeno tre workflow reali e invitare almeno un collega entro sette giorni.

| Coorte | Completa onboarding | Raggiunge il candidato di activation entro 7 giorni | Retention D90 |
| --- | ---: | ---: | ---: |
| Prima del redesign | 61% | 44% | 72% |
| Dopo il redesign | 79% | 36% | 64% |

Il redesign aveva ottimizzato un passaggio facile da misurare, ma non il raggiungimento del valore operativo.

### Correlazione con retention: utile, ma non sufficiente

Tra gli utenti CloudDesk:

- activation entro 48 ore → retention D90 81%;
- activation tra giorno 3 e 7 → 68%;
- activation oltre giorno 7 → 41%.

La relazione è forte.

Ma esistono almeno due spiegazioni:

1. raggiungere rapidamente il valore aumenta davvero la probabilità di restare;
2. clienti più motivati, più semplici da configurare o meglio supportati raggiungono prima il valore **e** restano di più.

La prima è una spiegazione causale. La seconda è confondimento.

Il lifecycle analysis può identificare il pattern. I capitoli su causalità ed esperimenti ci aiuteranno a capire quale intervento produce davvero un cambiamento.

### Time-to-value: non basta sapere quanti arrivano

Una volta definito un candidato di activation, dobbiamo misurare anche **quanto tempo serve per raggiungerlo**.

Per ogni cliente possiamo pensare a:

`TTV = momento del primo valore - momento di ingresso nel lifecycle`

La media da sola può però essere ingannevole.

Se la mediana è 2 giorni ma il P90 è 19 giorni, una parte sostanziale degli utenti sta vivendo un percorso molto diverso dalla maggioranza.

Per questo conviene osservare:

- percentuale che raggiunge il value moment;
- mediana e percentili del TTV;
- TTV per segmento/coorte;
- retention successiva per fascia di TTV;
- motivi di mancata activation.

### Il valore può richiedere più persone

Nei prodotti B2B l'activation non è sempre un evento individuale.

Un software collaborativo può generare valore solo quando:

- un admin configura il workspace;
- altri utenti accettano l'invito;
- almeno un processo viene eseguito in produzione.

In questi casi l'unità di activation dovrebbe essere l'**account**, non il singolo utente.

Questo evita una delle trappole più comuni: celebrare l'engagement di un champion mentre il resto dell'organizzazione non ha adottato il prodotto.

### Primo valore e valore ripetuto

Un singolo successo iniziale non garantisce retention.

È utile distinguere:

- **first value** — il primo risultato significativo;
- **repeat value** — il comportamento di valore viene ripetuto;
- **embedded value** — il prodotto entra stabilmente nel processo del cliente.

Questa progressione prepara il passaggio dalla activation alla retention.

### La domanda operativa

Una buona definizione di activation deve permettere di rispondere:

> Qual è il primo comportamento osservabile che indica che questo cliente ha ottenuto il valore per cui è arrivato, e quanto rapidamente riusciamo a portarlo lì?

Se la risposta è “ha completato tutte le schermate”, probabilmente stiamo ancora misurando il prodotto dal punto di vista del software, non dal punto di vista del cliente.
