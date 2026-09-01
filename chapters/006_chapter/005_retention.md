## 6.4 Retention: misurare se il valore continua nel tempo

Retention non significa semplicemente “l'utente è tornato”. Significa che, dopo un punto di partenza definito, una quota della popolazione continua a compiere il comportamento che rappresenta una relazione ancora viva con il prodotto.

La difficoltà non è la formula. È la semantica.

Per una banca, essere attivo può significare effettuare almeno una transazione. Per un SaaS B2B può significare usare una funzione core. Per un e-commerce può essere un nuovo acquisto. Per una piattaforma di viaggio, invece, l'assenza di un secondo acquisto entro trenta giorni può essere del tutto normale.

Una retention utile deve rispettare il **ritmo naturale del prodotto**.

### Caso simulato/composito: PulseFit e la retention che misurava aperture, non valore

**PulseFit** è un'app fitness freemium. Il team Product presenta una retention a 30 giorni del 46%, in netto miglioramento.

La definizione è:

> utente che apre l'app almeno una volta tra il giorno 21 e il giorno 30.

L'analista chiede però che cosa dovrebbe fare un utente che sta realmente ricevendo valore dal prodotto.

Viene costruita una seconda definizione:

> utente che completa almeno un allenamento tra il giorno 21 e il giorno 30.

La retention scende al 29%.

Il 46% non era falso. Misurava però soprattutto la capacità dell'app di generare un'apertura, anche tramite notifiche e contenuti gratuiti. Il 29% era più vicino al comportamento core.

La decisione cambia: invece di ottimizzare soltanto push notification e reminder, il team torna a studiare perché molti utenti aprono l'app senza completare un workout.

### Retention di presenza e retention di valore

È utile distinguere almeno due livelli.

**Retention di presenza**: l'utente torna in qualche forma.

**Retention di valore**: l'utente torna e compie il comportamento che rappresenta il valore centrale.

In alcuni prodotti le due metriche coincidono quasi. In altri divergono molto.

Un dashboard sano può mostrarle entrambe, purché sia chiaro quale delle due sostiene davvero la decisione.

### Il tempo deve seguire il prodotto

Confrontare indiscriminatamente `D1`, `D7` e `D30` tra business diversi produce benchmark spesso inutili.

Un'app di messaggistica può aspettarsi utilizzo quotidiano. Un software di payroll può essere usato intensamente una volta al mese. Una piattaforma di prenotazione vacanze può avere un ciclo naturale di molti mesi.

### Caso simulato/composito: TravelNest e il falso problema a 30 giorni

**TravelNest** vende soggiorni leisure. Solo il 14% dei clienti effettua una seconda prenotazione entro trenta giorni.

Il numero sembra pessimo se confrontato con prodotti consumer ad alta frequenza.

A dodici mesi, però, il 41% ha prenotato nuovamente.

La metrica a trenta giorni non era sbagliata: era disallineata con il ciclo di acquisto.

L'analista sostituisce quindi il singolo KPI con una curva di repeat booking a 3, 6 e 12 mesi e separa clienti business e leisure, che hanno frequenze naturali differenti.

### Exact, bracket e rolling retention

La retention può essere costruita in modi diversi.

- **Exact retention**: l'utente è attivo in uno specifico periodo, per esempio esattamente nella settimana 4.
- **Bracket retention**: l'utente è attivo in una finestra, per esempio tra il giorno 21 e il 30.
- **Rolling o unbounded retention**: l'utente torna al tempo `t` o in qualunque momento successivo.

Non sono versioni intercambiabili dello stesso numero. Possono rispondere a domande molto diverse.

Per un prodotto usato in modo intermittente, la rolling retention può essere più informativa. Per un comportamento che deve ripetersi con cadenza precisa, una finestra specifica può essere preferibile.

### Retention non significa soddisfazione

Un cliente può restare perché:

- il prodotto è eccellente;
- il costo di switching è alto;
- esiste un contratto annuale;
- mancano alternative;
- il processo di cancellazione è difficile.

Allo stesso modo, un cliente soddisfatto può non tornare spesso perché il bisogno è raro.

La retention è quindi una misura di **persistenza del comportamento o della relazione**, non una misura universale di soddisfazione.

### Le quattro definizioni che devono accompagnare il numero

Prima di pubblicare una retention, l'analista dovrebbe poter dichiarare:

1. **coorte iniziale** — chi entra nel denominatore;
2. **evento retained** — quale comportamento conta come attività;
3. **finestra** — quando deve avvenire;
4. **unità** — utente, account, abbonamento, logo o revenue.

Senza queste quattro informazioni, “retention 62%” è una percentuale molto precisa con un significato ancora incompleto.

La domanda corretta non è quindi:

> Qual è la nostra retention?

È:

> Quale comportamento vogliamo che persista, in quale popolazione e con quale ritmo naturale?
