## 6.4 Retention: misurare se il valore continua nel tempo

Retention non significa semplicemente “l'utente è tornato”. Significa che, dopo un punto di partenza definito, una quota della popolazione continua a compiere il comportamento che rappresenta una relazione ancora viva con il prodotto.

La difficoltà principale non è matematica. È decidere **quale comportamento conta come persistenza del valore** e con quale ritmo sia ragionevole aspettarselo.

Per una banca l'attività può essere una transazione; per un SaaS B2B l'uso di una funzione core; per un e-commerce un nuovo acquisto. Per una piattaforma di viaggio, invece, l'assenza di un secondo acquisto entro trenta giorni può essere perfettamente normale. Una retention utile deve quindi seguire il ciclo naturale del prodotto, non una convenzione universale.

### PulseFit: una retention in crescita che misurava soprattutto aperture

**PulseFit**, app fitness freemium, presenta una retention a trenta giorni del **46%**, in netto miglioramento. La definizione è semplice: utente che apre l'app almeno una volta tra il giorno 21 e il giorno 30.

L'analista riformula la domanda dal punto di vista del valore: che cosa dovrebbe fare un utente che sta realmente continuando a usare il prodotto per il motivo per cui è arrivato? Una seconda metrica considera retained chi completa almeno un allenamento nella stessa finestra. Il tasso scende al **29%**.

Il 46% non era falso. Misurava una relazione più debole, sensibile anche a notifiche, reminder e contenuti gratuiti. Il 29% è più vicino al comportamento core. La decisione cambia: il team smette di leggere l'aumento delle aperture come prova sufficiente di una relazione più sana e torna a studiare perché molti utenti aprono senza completare un workout.

È utile pensare a queste due metriche come **retention di presenza** e **retention di valore**. In alcuni prodotti quasi coincidono; in altri divergono molto. Quando entrambe servono, possono convivere nello stesso dashboard purché sia chiaro quale sostiene davvero la decisione.

### Il calendario della retention deve appartenere al prodotto

Anche la finestra può deformare il significato. D1, D7 e D30 sono naturali per prodotti ad alta frequenza, ma non per tutti i business. Un software payroll può essere usato intensamente una volta al mese; una piattaforma travel può avere cicli di molti mesi.

**TravelNest**, che vende soggiorni leisure, vede soltanto il **14%** dei clienti effettuare una seconda prenotazione entro trenta giorni. Con un benchmark da app consumer ad alta frequenza sembrerebbe un disastro. A dodici mesi, però, il **41%** ha prenotato nuovamente. La metrica a trenta giorni era corretta e contemporaneamente poco utile per il ciclo di acquisto reale. Il team passa quindi a una curva di repeat booking a 3, 6 e 12 mesi, separando business e leisure, che hanno frequenze naturali differenti.

Lo stesso ragionamento vale per la forma tecnica della retention. **Exact retention** chiede se l'utente è attivo in un periodo preciso; **bracket retention** usa una finestra, per esempio i giorni 21–30; **rolling o unbounded retention** considera il ritorno al tempo `t` o in qualunque momento successivo. Non sono tre modi equivalenti di presentare lo stesso numero. Rispondono a domande diverse e devono essere scelti in base al comportamento che vogliamo osservare.

### Persistenza non significa soddisfazione

Retention e soddisfazione possono essere correlate, ma non sono sinonimi. Un cliente può restare perché il prodotto è eccellente, oppure perché il costo di switching è alto, il contratto è annuale, mancano alternative o cancellare è difficile. Al contrario, un cliente soddisfatto può tornare raramente se il bisogno è occasionale.

Per questo la retention va trattata come misura della **persistenza della relazione o del comportamento**, non come giudizio universale sulla qualità dell'esperienza.

Prima di pubblicare un numero di retention dobbiamo poter ricostruire quattro elementi: chi entra nella coorte iniziale, quale evento definisce l'attività, in quale finestra deve avvenire e quale unità stiamo seguendo — utente, account, subscription, logo o revenue. Senza queste definizioni, “retention 62%” è un numero preciso con un significato ancora incompleto.

La domanda professionale non è quindi “qual è la nostra retention?”. È:

> **quale comportamento vogliamo che persista, per quale popolazione e con quale ritmo naturale del prodotto?**

Una volta definita questa persistenza possiamo finalmente interpretare correttamente il suo opposto operativo: che cosa significa davvero perdere un cliente, un account o una parte del valore economico.