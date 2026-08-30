## 6.4 Retention: chi torna, quando e per fare cosa

La retention misura la quota di utenti o clienti che continua a essere attiva dopo un certo intervallo di tempo.

La formula sembra semplice:

\[
Retention_t = \frac{Utenti\ ancora\ attivi\ al\ tempo\ t}{Utenti\ iniziali\ della\ coorte}
\]

La difficolta' non e' la divisione. E' decidere cosa significhi "attivo".

Per una banca, un cliente attivo potrebbe essere chi effettua almeno una transazione nel mese. Per una piattaforma video, chi guarda almeno dieci minuti. Per un SaaS B2B, chi utilizza una funzione core. Per un e-commerce, chi effettua un nuovo acquisto.

Una definizione debole produce una retention poco utile.

### Caso: l'app che sembrava trattenere bene gli utenti

PulseFit e' un'app mobile di fitness con modello freemium. Il team di prodotto presenta una retention a 30 giorni del 46%, considerata molto buona rispetto ai mesi precedenti.

La definizione di "retained user" e':

> utente che apre l'app almeno una volta tra il giorno 21 e il giorno 30.

L'analista confronta questa metrica con una definizione piu' vicina al valore del prodotto:

> utente che completa almeno un allenamento tra il giorno 21 e il giorno 30.

La retention scende dal 46% al 29%.

Una parte rilevante degli utenti continuava ad aprire l'app per notifiche, promemoria o contenuti gratuiti, senza utilizzare il comportamento centrale per cui il prodotto era stato progettato.

Il 46% non era falso. Rispondeva semplicemente a una domanda meno utile.

### Retention classica, rolling e unbounded

La retention puo' essere definita in modi diversi.

La retention esatta al giorno 30 chiede se l'utente e' attivo proprio in quella finestra. Una rolling retention puo' chiedere se e' tornato dal giorno 30 in poi. La scelta dipende dal ciclo naturale del prodotto.

Un'app di messaggistica e una piattaforma di prenotazione vacanze non possono usare la stessa idea di frequenza attesa.

### Caso: il falso problema di retention in una piattaforma travel

TravelNest osserva che solo il 14% dei clienti torna entro 30 giorni dalla prima prenotazione. In confronto alle metriche di altre app consumer, il numero sembra disastroso.

Ma il prodotto vende soggiorni leisure. La frequenza naturale di acquisto e' molto piu' bassa.

Quando l'analista misura repeat booking a 12 mesi, la retention commerciale sale al 41%. Il dato a 30 giorni non era sbagliato: era semplicemente incompatibile con il ciclo di acquisto.

La retention va quindi interpretata rispetto al comportamento atteso.

### La domanda da fare prima della formula

Prima di calcolare retention bisogna rispondere a quattro domande:

- qual e' l'evento iniziale che definisce la coorte?
- cosa significa essere ancora attivi?
- quale finestra temporale e' coerente con il prodotto?
- stiamo misurando utenti, account, abbonamenti o ricavi?

La retention non e' una metrica universale. E' una definizione operativa del rapporto tra cliente e prodotto nel tempo.
